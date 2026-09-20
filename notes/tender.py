#!/usr/bin/env python3
"""
BDJobs TENDER/EOI Scraper - Fixed Version
"""

import json
import csv
import re
import time
from datetime import datetime
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


class BDJobsTenderScraper:
    def __init__(self):
        self.url = "https://bdjobs.com/h/"
        self.tenders = []

    def scrape(self):
        print("=" * 80)
        print("📊 BDJobs TENDER/EOI Scraper")
        print("=" * 80)

        with sync_playwright() as p:
            print("🌐 Launching browser...")
            browser = p.chromium.launch(
                    headless=False,  # Use visible browser for better rendering
                    args=['--no-sandbox', '--disable-dev-shm-usage', '--disable-blink-features=AutomationControlled']
                    )
            page = browser.new_page()

            # Set user agent
            page.set_extra_http_headers({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                })

            print(f"🔍 Loading {self.url}...")
            page.goto(self.url, timeout=60000)

            # Wait longer for content
            print("⏳ Waiting for page to fully load...")
            page.wait_for_timeout(5000)

            # Click on TENDER link in navigation if needed
            try:
                tender_link = page.locator("text=TENDER/ EOI").first
                if tender_link:
                    print("✅ Found TENDER link in navigation")
                    tender_link.click()
                    page.wait_for_timeout(3000)
            except:
                print("⚠️ Could not find TENDER link in navigation")

            # Wait for content to load
            page.wait_for_timeout(5000)

            # Get page content
            html = page.content()

            # Save for debugging
            with open('debug_page.html', 'w', encoding='utf-8') as f:
                f.write(html)
            print("💾 Saved page source to debug_page.html")

            # Try multiple methods to find tender cards
            tenders = []

            # Method 1: Find by selector
            cards = page.query_selector_all('app-tender-card')
            print(f"📊 Found {len(cards)} app-tender-card elements")

            for card in cards:
                try:
                    # Get organization
                    org_elem = card.query_selector('div[title]')
                    organization = org_elem.get_attribute('title') if org_elem else "Unknown"

                    # Get link and title
                    link_elem = card.query_selector('a[href]')
                    if link_elem:
                        title = link_elem.inner_text().strip()
                        href = link_elem.get_attribute('href')
                        title = re.sub(r'^[▶►]\s*', '', title).strip()
                    else:
                        title = "Tender item"
                        href = "#"

                    if href and href.startswith('//'):
                        href = 'https:' + href
                    elif href and href.startswith('/'):
                        href = 'https://bdjobs.com' + href

                    # Get logo
                    logo = "https://via.placeholder.com/60x60?text=BD"
                    img = card.query_selector('img')
                    if img:
                        logo = img.get_attribute('src') or logo
                        if logo.startswith('//'):
                            logo = 'https:' + logo

                    if title and len(title) > 5 and title != 'Tender item':
                        tenders.append({
                            'organization': organization,
                            'title': title,
                            'link': href,
                            'logo': logo
                            })
                except Exception as e:
                    continue

            # Method 2: If no cards found, try finding by text
            if not tenders:
                print("🔍 Trying alternative method...")
                # Get all text content
                body_text = page.inner_text('body')

                # Find tender-related items using regex
                tender_pattern = r'([A-Za-z\s]+?)\n([A-Za-z\s\-]+?)\n(?:https?://[^\s]+)'
                matches = re.findall(tender_pattern, body_text)

                for org, title in matches:
                    if 'Tender' in title or 'EOI' in title or 'Proposal' in title:
                        tenders.append({
                            'organization': org.strip(),
                            'title': title.strip(),
                            'link': '#',
                            'logo': 'https://via.placeholder.com/60x60?text=BD'
                            })

            browser.close()

        # Remove duplicates
        self.tenders = self._remove_duplicates(tenders)

        print(f"\n📊 Found {len(self.tenders)} unique tender items\n")

        return self.tenders

    def _remove_duplicates(self, data):
        seen = set()
        unique = []
        for item in data:
            if item['link'] not in seen:
                seen.add(item['link'])
                unique.append(item)
        return unique

    def save_json(self, filename='tenders.json'):
        if not self.tenders:
            print("⚠️ No data to save!")
            return False

        output = []
        for i, tender in enumerate(self.tenders, 1):
            output.append({
                "id": i,
                "organization": tender['organization'],
                "title": tender['title'],
                "link": tender['link'],
                "logo": tender.get('logo', 'https://via.placeholder.com/60x60?text=BD'),
                "scraped_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "source": "bdjobs",
                "type": "Tender/EOI"
                })

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        print(f"💾 Saved {len(output)} tenders to {filename}")
        return True

    def save_csv(self, filename='tenders.csv'):
        if not self.tenders:
            print("⚠️ No data to save!")
            return False

        fieldnames = ['id', 'organization', 'title', 'link', 'logo', 'scraped_date', 'source', 'type']

        with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for i, tender in enumerate(self.tenders, 1):
                writer.writerow({
                    "id": i,
                    "organization": tender['organization'],
                    "title": tender['title'],
                    "link": tender['link'],
                    "logo": tender.get('logo', 'https://via.placeholder.com/60x60?text=BD'),
                    "scraped_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "source": "bdjobs",
                    "type": "Tender/EOI"
                    })

        print(f"💾 Saved {len(self.tenders)} tenders to {filename}")
        return True

    def print_results(self, limit=None):
        if not self.tenders:
            print("⚠️ No tenders to display!")
            return

        print("\n" + "=" * 80)
        print(f"📊 TENDER/EOI RESULTS ({len(self.tenders)} items)")
        print("=" * 80)

        items = self.tenders[:limit] if limit else self.tenders

        for i, tender in enumerate(items, 1):
            print(f"\n{i}. {tender['organization']}")
            print(f"   📌 {tender['title'][:80]}")
            if tender.get('link') and tender['link'] != '#':
                print(f"   🔗 {tender['link']}")


def main():
    scraper = BDJobsTenderScraper()

    # Scrape with visible browser for better results
    results = scraper.scrape()

    if results:
        scraper.print_results(limit=20)
        print("\n" + "=" * 80)
        print("💾 SAVING RESULTS")
        print("=" * 80)
        scraper.save_json('tenders.json')
        scraper.save_csv('tenders.csv')

        print("\n" + "=" * 80)
        print(f"✅ SUCCESS: {len(results)} tenders scraped!")
        print("📁 Files: tenders.json, tenders.csv")
        print("=" * 80)
    else:
        print("\n❌ No tenders found!")
        print("💡 Try running with headless=False to see what's happening")


if __name__ == "__main__":
    main()
