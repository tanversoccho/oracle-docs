
**Lead → Qualification → Opportunity → Customer → Sales → Follow-up**

### 1. CRM main modules

I would structure it like this:

```text
CRM
├── Dashboard
├── Leads
├── Customers
├── Contacts
├── Opportunities
├── Activities / Follow-ups
├── Campaigns
├── Tasks
└── Reports
```

### 2. Lead Management

A **Lead** is a potential customer who has not yet become a confirmed customer.

Important fields:

| Field                 | Example                                       |
| --------------------- | --------------------------------------------- |
| Lead ID               | LD-000125                                     |
| Lead Date             | 25-Aug-2026                                   |
| Lead Name             | ABC Trading Ltd.                              |
| Contact Person        | Mr. Rahim                                     |
| Mobile                | 01XXXXXXXXX                                   |
| Email                 | [rahim@example.com](mailto:rahim@example.com) |
| Company               | ABC Trading                                   |
| Lead Type             | New Business                                  |
| Lead Source           | Website                                       |
| Industry              | Manufacturing                                 |
| Location              | Dhaka                                         |
| Interested Product    | ERP Software                                  |
| Estimated Value       | ৳500,000                                      |
| Expected Closing Date | 30-Sep-2026                                   |
| Salesperson           | Tanver                                        |
| Lead Status           | Qualified                                     |
| Lead Priority         | High                                          |
| Remarks               | Interested in ERP                             |

### 3. Lead Type

Don't make **Lead Type** the same thing as **Lead Source**.

**Lead Type** describes *what kind of business opportunity it is*:

* New Customer
* Existing Customer
* New Business
* Cross Sell
* Up Sell
* Renewal
* Repeat Business
* Partner/Reseller
* Government
* Corporate
* Individual

You can make these configurable from a **CRM Setup → Lead Type** screen.

### 4. Lead Source

This tells you **where the lead came from**:

* Website
* Facebook
* LinkedIn
* Email
* Phone Call
* Referral
* Existing Customer
* Salesperson
* Exhibition/Event
* Advertisement
* Partner
* Walk-in
* Other

This distinction is important for reporting.

For example:

> **Lead Type:** New Customer
> **Lead Source:** Website

### 5. Lead Status

A useful lifecycle:

```text
New
 ↓
Contacted
 ↓
Qualified
 ↓
Requirement Identified
 ↓
Proposal/Quotation
 ↓
Negotiation
 ↓
Won / Lost
```

You could also have:

* Unqualified
* On Hold
* Follow-up Required
* Converted

### 6. Lead Qualification

When a salesperson receives a lead, they should be able to record:

* Requirement
* Budget
* Decision maker
* Purchase timeline
* Interested products
* Expected quantity
* Expected sales value
* Competitor
* Probability %
* Qualification remarks

A simple qualification model could be:

**Hot / Warm / Cold**

or a score:

```text
Lead Score: 75/100
```

### 7. Customer Information

Once a lead becomes a customer, maintain a separate customer profile.

#### Basic information

* Customer ID
* Customer Code
* Customer Name
* Customer Type
* Company Name
* Customer Category
* Industry
* Business Type
* TIN
* BIN/VAT
* Website

#### Contact information

* Contact person
* Designation
* Mobile
* Phone
* Email
* Alternative contact

#### Address

* Head Office
* Billing Address
* Shipping Address
* District
* Division
* Country

#### Business information

* Salesperson
* Territory
* Customer Group
* Credit Limit
* Payment Terms
* Currency
* Preferred Contact Method

### 8. Contacts

A company can have multiple contacts, so don't put everything into the customer table.

For example:

```text
ABC Corporation
│
├── Mr. Rahim — Managing Director
├── Mr. Karim — Purchase Manager
├── Ms. Sara — Accounts Manager
└── Mr. Hasan — IT Manager
```

Contact fields:

* Contact ID
* Customer ID
* Name
* Designation
* Department
* Mobile
* Email
* Contact type
* Primary contact
* Decision maker
* Active/Inactive

### 9. Opportunity Management

A lead can become an **Opportunity** when there is a real sales possibility.

Example:

```text
Lead
ABC Corporation
       ↓
Qualified
       ↓
Opportunity
ERP Implementation
       ↓
Quotation
৳2,500,000
       ↓
Negotiation
       ↓
Won
```

Opportunity fields:

* Opportunity ID
* Customer/Lead
* Opportunity name
* Product/service
* Estimated value
* Probability
* Expected closing date
* Salesperson
* Stage
* Competitor
* Requirement
* Remarks

### 10. Activities / Follow-up

This is very important for a sales CRM.

Each lead/customer should have an activity timeline:

```text
25-Aug  Phone Call
        Discussed ERP requirement

27-Aug  Meeting
        Demonstration scheduled

30-Aug  Follow-up
        Customer requested quotation

02-Sep  Email
        Quotation sent
```

Activity types:

* Phone Call
* Email
* Meeting
* Visit
* Demo
* Follow-up
* Task
* Note

Fields:

* Activity ID
* Lead/Customer ID
* Activity type
* Date/time
* Assigned employee
* Subject
* Description
* Next follow-up date
* Status
* Outcome

### 11. CRM Dashboard

Your dashboard could show:

**Lead Overview**

* Total Leads
* New Leads
* Contacted
* Qualified
* Unqualified
* Hot Leads
* Converted Leads
* Lost Leads

**Sales Pipeline**

* Total Opportunities
* Pipeline Value
* Won Value
* Lost Value
* Expected Revenue

**Follow-ups**

* Today's Follow-ups
* Overdue Follow-ups
* Upcoming Follow-ups

**Sources**

* Website leads
* Facebook leads
* Referral leads
* Phone leads
* Exhibition leads

This lets management answer:

> "Where are our leads coming from, which salesperson is handling them, and how many are actually converting?"

### 12. Recommended database structure

For an enterprise Sales/CRM application, I'd roughly use:

```text
CRM_LEAD
CRM_LEAD_TYPE
CRM_LEAD_SOURCE
CRM_LEAD_STATUS
CRM_LEAD_ACTIVITY

CRM_CUSTOMER
CRM_CUSTOMER_TYPE
CRM_CUSTOMER_CATEGORY
CRM_CUSTOMER_ADDRESS

CRM_CONTACT
CRM_CONTACT_TYPE

CRM_OPPORTUNITY
CRM_OPPORTUNITY_STAGE

CRM_ACTIVITY
CRM_TASK
CRM_FOLLOWUP

CRM_CAMPAIGN
CRM_CAMPAIGN_LEAD
```

The key relationship:

```text
                  ┌── Activities
                  │
Lead ──> Qualification ──> Opportunity
 │                            │
 │                            ↓
 └──────────────────────> Customer
                              │
                              ├── Contacts
                              ├── Addresses
                              ├── Activities
                              ├── Opportunities
                              └── Sales
```

### Most important master/setup data

If you're preparing the **CRM module specification for your Sales App**, I would make these configurable masters:

* Lead Type
* Lead Source
* Lead Status
* Lead Priority
* Customer Type
* Customer Category
* Industry
* Business Type
* Contact Type
* Opportunity Stage
* Activity Type
* Lost Reason
* Customer Status
* Territory
* Salesperson
* Customer Segment

This gives you a CRM that can later connect cleanly to **quotation → sales order → invoice → collection**.


## 1. CRM Module Structure

```text
CRM
│
├── Dashboard
│
├── Lead Management
│   ├── Lead List
│   ├── Create Lead
│   ├── Lead Details
│   ├── Lead Conversion
│   └── Lead Follow-up
│
├── Customer Management
│   ├── Customer List
│   ├── Create Customer
│   ├── Customer Details
│   ├── Contacts
│   └── Addresses
│
├── Opportunity Management
│   ├── Opportunity List
│   ├── Create Opportunity
│   ├── Pipeline
│   └── Opportunity Details
│
├── Activity Management
│   ├── Calls
│   ├── Meetings
│   ├── Visits
│   ├── Emails
│   ├── Tasks
│   └── Follow-ups
│
├── CRM Masters
│   ├── Lead Type
│   ├── Lead Source
│   ├── Lead Status
│   ├── Lead Priority
│   ├── Customer Type
│   ├── Customer Category
│   ├── Industry
│   ├── Opportunity Stage
│   ├── Activity Type
│   └── Lost Reason
│
└── Reports
    ├── Lead Report
    ├── Lead Conversion
    ├── Sales Pipeline
    ├── Customer Report
    ├── Follow-up Report
    └── Salesperson Performance
```

# 2. Lead Management

This should probably be the **main CRM screen**.

### Lead fields

| Field                 | Required | Example                               |
| --------------------- | -------- | ------------------------------------- |
| Lead ID               | Auto     | LD-000001                             |
| Lead Date             | Yes      | 25-Aug-2026                           |
| Lead Name             | Yes      | ABC Trading                           |
| Company Name          | No       | ABC Trading Ltd.                      |
| Contact Person        | Yes      | Md. Rahim                             |
| Designation           | No       | Purchase Manager                      |
| Mobile                | Yes      | 017XXXXXXXX                           |
| Phone                 | No       | 02XXXXXXXX                            |
| Email                 | No       | [rahim@abc.com](mailto:rahim@abc.com) |
| Lead Type             | Yes      | New Customer                          |
| Lead Source           | Yes      | Website                               |
| Industry              | No       | Manufacturing                         |
| Customer Type         | No       | Corporate                             |
| Location              | No       | Dhaka                                 |
| Product/Service       | No       | ERP Software                          |
| Estimated Value       | No       | ৳500,000                              |
| Expected Closing Date | No       | 30-Sep-2026                           |
| Salesperson           | Yes      | Tanver                                |
| Priority              | Yes      | High                                  |
| Status                | Yes      | New                                   |
| Description           | No       | ERP requirement                       |
| Remarks               | No       | Interested                            |

### Lead status

I recommend:

```text
NEW
 ↓
CONTACTED
 ↓
QUALIFIED
 ↓
REQUIREMENT_IDENTIFIED
 ↓
PROPOSAL
 ↓
NEGOTIATION
 ↓
WON
```

Alternative ending:

```text
                    ┌── WON
NEGOTIATION ────────┤
                    └── LOST
```

Don't hard-code these values if possible. Keep them in a master table.

---

# 3. Lead Type

Create a separate **Lead Type Master**.

Example:

| Code       | Lead Type         |
| ---------- | ----------------- |
| NEW        | New Customer      |
| EXISTING   | Existing Customer |
| CROSS_SELL | Cross Sell        |
| UP_SELL    | Up Sell           |
| RENEWAL    | Renewal           |
| REPEAT     | Repeat Business   |
| PARTNER    | Partner/Reseller  |

Fields:

```text
Lead Type ID
Lead Type Code
Lead Type Name
Description
Sort Order
Active
```

---

# 4. Lead Source

Keep this separate from Lead Type.

Example:

| Code        | Source           |
| ----------- | ---------------- |
| WEBSITE     | Website          |
| FACEBOOK    | Facebook         |
| LINKEDIN    | LinkedIn         |
| REFERRAL    | Referral         |
| PHONE       | Phone Call       |
| EMAIL       | Email            |
| EVENT       | Exhibition/Event |
| SALESPERSON | Salesperson      |
| PARTNER     | Partner          |
| WALKIN      | Walk-in          |

This allows management to answer:

> Which marketing/sales channel produces the most customers?

---

# 5. Lead Priority

Simple:

```text
LOW
MEDIUM
HIGH
URGENT
```

You can also use colors in the UI, but store the **code**, not the color.

---

# 6. Customer Management

Once a lead is converted, it becomes a customer.

### Customer master

```text
Customer ID
Customer Code
Customer Name
Customer Type
Customer Category
Industry
Business Type
TIN
BIN/VAT
Website
Salesperson
Territory
Customer Status
Credit Limit
Payment Terms
Currency
Remarks
```

### Customer Type

Examples:

```text
INDIVIDUAL
CORPORATE
GOVERNMENT
NGO
SME
DEALER
DISTRIBUTOR
RESELLER
```

### Customer Category

This is different from Customer Type.

For example:

```text
PREMIUM
STANDARD
REGULAR
VIP
STRATEGIC
```

---

# 7. Customer Address

Don't put multiple addresses directly into the customer table.

Use:

```text
CRM_CUSTOMER_ADDRESS
```

Fields:

| Field          | Example      |
| -------------- | ------------ |
| Address ID     | 1001         |
| Customer ID    | C-00001      |
| Address Type   | Billing      |
| Address Line 1 | 25 Motijheel |
| Address Line 2 | Suite 4B     |
| District       | Dhaka        |
| Division       | Dhaka        |
| Country        | Bangladesh   |
| Postal Code    | 1000         |
| Primary        | Yes          |

Address Type:

```text
BILLING
SHIPPING
OFFICE
FACTORY
HOME
OTHER
```

---

# 8. Contact Management

One customer can have many contacts.

```text
ABC Ltd.
│
├── Rahim — Managing Director
├── Karim — Purchase Manager
├── Sara — Accounts Manager
└── Hasan — IT Manager
```

### Contact fields

```text
Contact ID
Customer ID
Contact Name
Designation
Department
Mobile
Phone
Email
Contact Type
Is Primary
Is Decision Maker
Is Active
Remarks
```

Contact Type:

```text
DECISION_MAKER
PURCHASER
ACCOUNTS
TECHNICAL
ADMIN
OTHER
```

---

# 9. Opportunity Management

A **Lead** tells you *who might buy*.

An **Opportunity** tells you *what they might buy and how much it could be worth*.

Example:

```text
Lead
ABC Ltd.
   ↓
Qualified
   ↓
Opportunity
ERP Implementation
   ↓
৳2,500,000
   ↓
Negotiation
   ↓
Won
```

### Opportunity fields

```text
Opportunity ID
Opportunity Number
Lead ID
Customer ID
Opportunity Name
Product/Service
Description
Estimated Value
Probability
Expected Closing Date
Salesperson
Stage
Competitor
Lost Reason
Remarks
```

---

# 10. Opportunity Stage

Recommended:

```text
PROSPECTING
QUALIFICATION
REQUIREMENT
DEMO
PROPOSAL
NEGOTIATION
CLOSED_WON
CLOSED_LOST
```

Each stage can have a probability.

| Stage         | Probability |
| ------------- | ----------: |
| Prospecting   |         10% |
| Qualification |         20% |
| Requirement   |         40% |
| Demo          |         50% |
| Proposal      |         70% |
| Negotiation   |         85% |
| Won           |        100% |
| Lost          |          0% |

Then your CRM can calculate:

**Weighted Pipeline = Opportunity Value × Probability**

---

# 11. Activity / Follow-up Management

Every lead/customer should have an activity timeline.

Example:

```text
25-Aug
📞 Phone Call
Discussed ERP requirement.

27-Aug
🏢 Meeting
Customer requested product demo.

29-Aug
📧 Email
Quotation sent.

02-Sep
📞 Follow-up
Customer will make decision next week.
```

### Activity fields

```text
Activity ID
Activity Date
Activity Type
Lead ID
Customer ID
Opportunity ID
Employee/Salesperson
Subject
Description
Outcome
Next Follow-up Date
Status
Priority
Remarks
```

### Activity Type

```text
CALL
EMAIL
MEETING
VISIT
DEMO
FOLLOW_UP
TASK
NOTE
```

---

# 12. Follow-up

This deserves its own functionality.

Salesperson should see:

### Today's Follow-ups

```text
┌──────────────────────────────────────────────┐
│ Today's Follow-ups                           │
├──────────────────────────────────────────────┤
│ ABC Ltd.     Call       10:00 AM    HIGH     │
│ XYZ Ltd.     Meeting    12:30 PM    MEDIUM   │
│ DEF Ltd.     Follow-up  03:00 PM    HIGH     │
└──────────────────────────────────────────────┘
```

Statuses:

```text
PENDING
COMPLETED
CANCELLED
RESCHEDULED
```

---

# 13. Lost Reason

When an opportunity/lead is lost, don't just store `"Lost"`.

Store the reason.

```text
PRICE
COMPETITOR
NO_BUDGET
NO_REQUIREMENT
TIMING
CUSTOMER_UNRESPONSIVE
PRODUCT_NOT_SUITABLE
PROJECT_CANCELLED
OTHER
```

This becomes extremely useful for management reports.

---

# 14. CRM Dashboard

I'd make the dashboard look roughly like:

```text
┌────────────────┬────────────────┬────────────────┐
│ Total Leads    │ Qualified      │ New Customers  │
│     1,250      │      420       │      125       │
└────────────────┴────────────────┴────────────────┘

┌────────────────┬────────────────┬────────────────┐
│ Open Deals     │ Pipeline Value │ Won This Month │
│      185       │   ৳25.5M       │    ৳8.2M       │
└────────────────┴────────────────┴────────────────┘

Lead Sources
────────────────────────────────
Website       ████████████  320
Referral      ████████      210
Facebook      ██████        150
Salesperson   █████         120

Today's Follow-ups
────────────────────────────────
10:00  ABC Ltd.      Call
12:30  XYZ Ltd.      Meeting
15:00  DEF Ltd.      Follow-up
```

---

# 15. Database Design

Since you're likely using an enterprise/Oracle-style system, I'd separate **transaction tables** and **master tables**.

### Masters

```text
CRM_LEAD_TYPE
CRM_LEAD_SOURCE
CRM_LEAD_STATUS
CRM_LEAD_PRIORITY

CRM_CUSTOMER_TYPE
CRM_CUSTOMER_CATEGORY
CRM_INDUSTRY
CRM_BUSINESS_TYPE

CRM_CONTACT_TYPE
CRM_ACTIVITY_TYPE

CRM_OPPORTUNITY_STAGE
CRM_LOST_REASON
CRM_CUSTOMER_STATUS
```

### Transactions

```text
CRM_LEAD
CRM_LEAD_ACTIVITY

CRM_CUSTOMER
CRM_CUSTOMER_ADDRESS
CRM_CONTACT

CRM_OPPORTUNITY

CRM_ACTIVITY
CRM_FOLLOWUP
```

### Relationship

```text
                       ┌──────────────┐
                       │   LEAD       │
                       └──────┬───────┘
                              │
                    Qualification
                              │
                              ▼
                       ┌──────────────┐
                       │ OPPORTUNITY  │
                       └──────┬───────┘
                              │
                       Won / Conversion
                              │
                              ▼
                       ┌──────────────┐
                       │  CUSTOMER    │
                       └──────┬───────┘
                              │
              ┌───────────────┼──────────────┐
              ▼               ▼              ▼
          CONTACT         ADDRESS        ACTIVITY
```

# 16. Important audit fields

Because this is a business application, **every important table should have standard audit columns**:

```text
CREATED_BY
CREATED_DATE
UPDATED_BY
UPDATED_DATE
STATUS
```

For transactional data, also consider:

```text
COMPANY_ID
BRANCH_ID
FINANCIAL_YEAR_ID
```

If your application supports multiple companies/branches, add these from the beginning rather than redesigning later.

---

# 17. CRM → Sales integration

The most important part is not just CRM itself. It should connect to the rest of the Sales App:

```text
                    CRM
                     │
                  LEAD
                     │
                QUALIFIED
                     │
               OPPORTUNITY
                     │
                QUOTATION
                     │
                SALES ORDER
                     │
                 DELIVERY
                     │
                  INVOICE
                     │
                 RECEIVABLE
                     │
                 PAYMENT
```

So I'd avoid designing CRM as an isolated module.

### Recommended final module map

```text
SALES APPLICATION
│
├── CRM
│   ├── Leads
│   ├── Customers
│   ├── Contacts
│   ├── Opportunities
│   ├── Activities
│   └── Follow-ups
│
├── SALES
│   ├── Quotations
│   ├── Sales Orders
│   ├── Deliveries
│   └── Sales Invoices
│
├── ARM
│   ├── Receivables
│   ├── Collections
│   └── Payments
│
└── REPORTS
```


Below is a practical starting schema

## 1. Master tables

These tables contain configurable CRM values.

### `CRM_LEAD_TYPE`

```sql
CREATE TABLE CRM_LEAD_TYPE (
    LEAD_TYPE_ID      NUMBER GENERATED BY DEFAULT AS IDENTITY,
    LEAD_TYPE_CODE    VARCHAR2(30) NOT NULL,
    LEAD_TYPE_NAME    VARCHAR2(100) NOT NULL,
    DESCRIPTION       VARCHAR2(500),
    SORT_ORDER        NUMBER DEFAULT 1,
    IS_ACTIVE         CHAR(1) DEFAULT 'Y' NOT NULL,

    CREATED_BY        NUMBER,
    CREATED_DATE      TIMESTAMP DEFAULT SYSTIMESTAMP,
    UPDATED_BY        NUMBER,
    UPDATED_DATE      TIMESTAMP,

    CONSTRAINT PK_CRM_LEAD_TYPE PRIMARY KEY (LEAD_TYPE_ID),
    CONSTRAINT UK_CRM_LEAD_TYPE_CODE UNIQUE (LEAD_TYPE_CODE),
    CONSTRAINT CK_CRM_LEAD_TYPE_ACTIVE CHECK (IS_ACTIVE IN ('Y','N'))
);
```

Example:

```text
NEW_CUSTOMER
EXISTING_CUSTOMER
CROSS_SELL
UP_SELL
RENEWAL
REPEAT_BUSINESS
PARTNER
```

---

### `CRM_LEAD_SOURCE`

```sql
CREATE TABLE CRM_LEAD_SOURCE (
    LEAD_SOURCE_ID    NUMBER GENERATED BY DEFAULT AS IDENTITY,
    SOURCE_CODE       VARCHAR2(30) NOT NULL,
    SOURCE_NAME       VARCHAR2(100) NOT NULL,
    DESCRIPTION       VARCHAR2(500),
    SORT_ORDER        NUMBER DEFAULT 1,
    IS_ACTIVE         CHAR(1) DEFAULT 'Y' NOT NULL,

    CREATED_BY        NUMBER,
    CREATED_DATE      TIMESTAMP DEFAULT SYSTIMESTAMP,
    UPDATED_BY        NUMBER,
    UPDATED_DATE      TIMESTAMP,

    CONSTRAINT PK_CRM_LEAD_SOURCE PRIMARY KEY (LEAD_SOURCE_ID),
    CONSTRAINT UK_CRM_LEAD_SOURCE_CODE UNIQUE (SOURCE_CODE),
    CONSTRAINT CK_CRM_LEAD_SOURCE_ACTIVE CHECK (IS_ACTIVE IN ('Y','N'))
);
```

Examples:

```text
WEBSITE
FACEBOOK
LINKEDIN
REFERRAL
PHONE
EMAIL
EVENT
WALK_IN
SALESPERSON
PARTNER
```

---

### Other master tables

I recommend these:

```text
CRM_LEAD_STATUS
CRM_LEAD_PRIORITY
CRM_CUSTOMER_TYPE
CRM_CUSTOMER_CATEGORY
CRM_CUSTOMER_STATUS
CRM_INDUSTRY
CRM_BUSINESS_TYPE
CRM_CONTACT_TYPE
CRM_ACTIVITY_TYPE
CRM_OPPORTUNITY_STAGE
CRM_LOST_REASON
```

Don't put these values directly into `CRM_LEAD` as strings.

For example, prefer:

```text
LEAD_STATUS_ID = 3
```

instead of:

```text
LEAD_STATUS = 'QUALIFIED'
```

That gives you configurable masters.

---

# 2. Main Lead table

This is the most important CRM transaction table.

```sql
CREATE TABLE CRM_LEAD (
    LEAD_ID                 NUMBER GENERATED BY DEFAULT AS IDENTITY,
    LEAD_NO                 VARCHAR2(30) NOT NULL,

    LEAD_DATE               DATE DEFAULT SYSDATE NOT NULL,

    LEAD_NAME               VARCHAR2(200) NOT NULL,
    COMPANY_NAME            VARCHAR2(200),

    CONTACT_PERSON          VARCHAR2(150),
    DESIGNATION             VARCHAR2(100),

    MOBILE_NO               VARCHAR2(30),
    PHONE_NO                VARCHAR2(30),
    EMAIL                   VARCHAR2(150),

    LEAD_TYPE_ID            NUMBER,
    LEAD_SOURCE_ID          NUMBER,
    LEAD_STATUS_ID          NUMBER,
    LEAD_PRIORITY_ID        NUMBER,

    INDUSTRY_ID             NUMBER,
    CUSTOMER_TYPE_ID        NUMBER,

    ADDRESS                 VARCHAR2(500),
    DISTRICT                VARCHAR2(100),
    COUNTRY                 VARCHAR2(100),

    PRODUCT_ID              NUMBER,

    ESTIMATED_VALUE         NUMBER(18,2),
    CURRENCY_CODE           VARCHAR2(10),

    EXPECTED_CLOSE_DATE     DATE,

    SALES_PERSON_ID         NUMBER,

    LEAD_SCORE              NUMBER(5,2),

    DESCRIPTION             VARCHAR2(1000),
    REMARKS                 VARCHAR2(1000),

    CONVERTED_FLAG          CHAR(1) DEFAULT 'N' NOT NULL,
    CONVERTED_DATE          DATE,

    CREATED_BY              NUMBER,
    CREATED_DATE            TIMESTAMP DEFAULT SYSTIMESTAMP,
    UPDATED_BY              NUMBER,
    UPDATED_DATE            TIMESTAMP,

    CONSTRAINT PK_CRM_LEAD PRIMARY KEY (LEAD_ID),
    CONSTRAINT UK_CRM_LEAD_NO UNIQUE (LEAD_NO),

    CONSTRAINT CK_CRM_LEAD_CONVERTED
        CHECK (CONVERTED_FLAG IN ('Y','N')),

    CONSTRAINT FK_CRM_LEAD_TYPE
        FOREIGN KEY (LEAD_TYPE_ID)
        REFERENCES CRM_LEAD_TYPE(LEAD_TYPE_ID),

    CONSTRAINT FK_CRM_LEAD_SOURCE
        FOREIGN KEY (LEAD_SOURCE_ID)
        REFERENCES CRM_LEAD_SOURCE(LEAD_SOURCE_ID)
);
```

---

# 3. Customer table

Once a lead is converted, you create a customer.

```sql
CREATE TABLE CRM_CUSTOMER (
    CUSTOMER_ID            NUMBER GENERATED BY DEFAULT AS IDENTITY,
    CUSTOMER_CODE          VARCHAR2(30) NOT NULL,
    CUSTOMER_NAME          VARCHAR2(200) NOT NULL,

    CUSTOMER_TYPE_ID       NUMBER,
    CUSTOMER_CATEGORY_ID   NUMBER,
    CUSTOMER_STATUS_ID     NUMBER,

    INDUSTRY_ID            NUMBER,
    BUSINESS_TYPE_ID       NUMBER,

    TIN_NO                 VARCHAR2(50),
    BIN_NO                 VARCHAR2(50),
    WEBSITE                VARCHAR2(200),

    SALES_PERSON_ID        NUMBER,
    TERRITORY_ID           NUMBER,

    CREDIT_LIMIT           NUMBER(18,2),
    PAYMENT_TERM_ID        NUMBER,

    CURRENCY_CODE          VARCHAR2(10),

    PHONE_NO               VARCHAR2(30),
    EMAIL                  VARCHAR2(150),

    REMARKS                VARCHAR2(1000),

    CREATED_BY             NUMBER,
    CREATED_DATE           TIMESTAMP DEFAULT SYSTIMESTAMP,
    UPDATED_BY             NUMBER,
    UPDATED_DATE           TIMESTAMP,

    CONSTRAINT PK_CRM_CUSTOMER PRIMARY KEY (CUSTOMER_ID),
    CONSTRAINT UK_CRM_CUSTOMER_CODE UNIQUE (CUSTOMER_CODE)
);
```

---

# 4. Customer Address

Don't put billing and shipping addresses directly into `CRM_CUSTOMER`.

Use a child table:

```sql
CREATE TABLE CRM_CUSTOMER_ADDRESS (
    ADDRESS_ID             NUMBER GENERATED BY DEFAULT AS IDENTITY,
    CUSTOMER_ID            NUMBER NOT NULL,

    ADDRESS_TYPE           VARCHAR2(30) NOT NULL,

    ADDRESS_LINE1          VARCHAR2(250),
    ADDRESS_LINE2          VARCHAR2(250),

    CITY                   VARCHAR2(100),
    DISTRICT               VARCHAR2(100),
    DIVISION               VARCHAR2(100),
    POSTAL_CODE            VARCHAR2(20),
    COUNTRY                VARCHAR2(100),

    IS_PRIMARY             CHAR(1) DEFAULT 'N',

    CREATED_BY             NUMBER,
    CREATED_DATE           TIMESTAMP DEFAULT SYSTIMESTAMP,
    UPDATED_BY             NUMBER,
    UPDATED_DATE           TIMESTAMP,

    CONSTRAINT PK_CRM_CUSTOMER_ADDRESS
        PRIMARY KEY (ADDRESS_ID),

    CONSTRAINT FK_CRM_CUSTOMER_ADDRESS
        FOREIGN KEY (CUSTOMER_ID)
        REFERENCES CRM_CUSTOMER(CUSTOMER_ID),

    CONSTRAINT CK_CRM_ADDRESS_PRIMARY
        CHECK (IS_PRIMARY IN ('Y','N'))
);
```

`ADDRESS_TYPE` can be:

```text
BILLING
SHIPPING
OFFICE
FACTORY
HOME
OTHER
```

---

# 5. Contact table

A customer can have multiple contacts.

```sql
CREATE TABLE CRM_CONTACT (
    CONTACT_ID             NUMBER GENERATED BY DEFAULT AS IDENTITY,
    CUSTOMER_ID            NUMBER NOT NULL,

    CONTACT_NAME           VARCHAR2(150) NOT NULL,
    DESIGNATION            VARCHAR2(100),
    DEPARTMENT             VARCHAR2(100),

    CONTACT_TYPE_ID        NUMBER,

    MOBILE_NO              VARCHAR2(30),
    PHONE_NO               VARCHAR2(30),
    EMAIL                  VARCHAR2(150),

    IS_PRIMARY             CHAR(1) DEFAULT 'N',
    IS_DECISION_MAKER      CHAR(1) DEFAULT 'N',
    IS_ACTIVE              CHAR(1) DEFAULT 'Y',

    REMARKS                VARCHAR2(500),

    CREATED_BY             NUMBER,
    CREATED_DATE           TIMESTAMP DEFAULT SYSTIMESTAMP,
    UPDATED_BY             NUMBER,
    UPDATED_DATE           TIMESTAMP,

    CONSTRAINT PK_CRM_CONTACT PRIMARY KEY (CONTACT_ID),

    CONSTRAINT FK_CRM_CONTACT_CUSTOMER
        FOREIGN KEY (CUSTOMER_ID)
        REFERENCES CRM_CUSTOMER(CUSTOMER_ID),

    CONSTRAINT CK_CRM_CONTACT_PRIMARY
        CHECK (IS_PRIMARY IN ('Y','N')),

    CONSTRAINT CK_CRM_CONTACT_DECISION
        CHECK (IS_DECISION_MAKER IN ('Y','N')),

    CONSTRAINT CK_CRM_CONTACT_ACTIVE
        CHECK (IS_ACTIVE IN ('Y','N'))
);
```

---

# 6. Opportunity

This represents an actual sales opportunity.

```sql
CREATE TABLE CRM_OPPORTUNITY (
    OPPORTUNITY_ID          NUMBER GENERATED BY DEFAULT AS IDENTITY,
    OPPORTUNITY_NO          VARCHAR2(30) NOT NULL,

    LEAD_ID                 NUMBER,
    CUSTOMER_ID             NUMBER,

    OPPORTUNITY_NAME        VARCHAR2(200) NOT NULL,

    PRODUCT_ID              NUMBER,

    OPPORTUNITY_STAGE_ID    NUMBER,

    ESTIMATED_VALUE         NUMBER(18,2),
    PROBABILITY             NUMBER(5,2),

    EXPECTED_CLOSE_DATE     DATE,

    SALES_PERSON_ID         NUMBER,

    COMPETITOR              VARCHAR2(200),

    LOST_REASON_ID          NUMBER,

    DESCRIPTION             VARCHAR2(1000),
    REMARKS                 VARCHAR2(1000),

    CREATED_BY              NUMBER,
    CREATED_DATE            TIMESTAMP DEFAULT SYSTIMESTAMP,
    UPDATED_BY              NUMBER,
    UPDATED_DATE            TIMESTAMP,

    CONSTRAINT PK_CRM_OPPORTUNITY
        PRIMARY KEY (OPPORTUNITY_ID),

    CONSTRAINT UK_CRM_OPPORTUNITY_NO
        UNIQUE (OPPORTUNITY_NO),

    CONSTRAINT CK_CRM_OPPORTUNITY_PROB
        CHECK (PROBABILITY BETWEEN 0 AND 100)
);
```

---

# 7. Activity table

This is where calls, meetings, visits, emails, etc. are stored.

```sql
CREATE TABLE CRM_ACTIVITY (
    ACTIVITY_ID             NUMBER GENERATED BY DEFAULT AS IDENTITY,

    LEAD_ID                 NUMBER,
    CUSTOMER_ID             NUMBER,
    CONTACT_ID              NUMBER,
    OPPORTUNITY_ID          NUMBER,

    ACTIVITY_TYPE_ID        NUMBER NOT NULL,

    ACTIVITY_DATE           TIMESTAMP DEFAULT SYSTIMESTAMP,

    SUBJECT                 VARCHAR2(250) NOT NULL,
    DESCRIPTION             VARCHAR2(2000),

    OUTCOME                 VARCHAR2(1000),

    SALES_PERSON_ID         NUMBER,

    NEXT_FOLLOWUP_DATE      DATE,

    STATUS                  VARCHAR2(30) DEFAULT 'PENDING',

    CREATED_BY              NUMBER,
    CREATED_DATE            TIMESTAMP DEFAULT SYSTIMESTAMP,
    UPDATED_BY              NUMBER,
    UPDATED_DATE            TIMESTAMP,

    CONSTRAINT PK_CRM_ACTIVITY
        PRIMARY KEY (ACTIVITY_ID)
);
```

This lets you create a timeline like:

```text
Lead
 ├── Phone Call
 ├── Meeting
 ├── Email
 ├── Demo
 └── Follow-up
```

---

# 8. Follow-up table

For a serious sales system, I would make follow-up a separate transaction instead of relying only on `CRM_ACTIVITY`.

```sql
CREATE TABLE CRM_FOLLOWUP (
    FOLLOWUP_ID             NUMBER GENERATED BY DEFAULT AS IDENTITY,

    LEAD_ID                 NUMBER,
    CUSTOMER_ID             NUMBER,
    OPPORTUNITY_ID          NUMBER,

    ASSIGNED_TO             NUMBER NOT NULL,

    FOLLOWUP_DATE           DATE NOT NULL,
    FOLLOWUP_TIME           VARCHAR2(10),

    FOLLOWUP_TYPE_ID        NUMBER,

    SUBJECT                 VARCHAR2(250) NOT NULL,
    REMARKS                 VARCHAR2(1000),

    STATUS                  VARCHAR2(30) DEFAULT 'PENDING',

    COMPLETED_DATE          DATE,
    COMPLETION_REMARKS      VARCHAR2(1000),

    CREATED_BY              NUMBER,
    CREATED_DATE            TIMESTAMP DEFAULT SYSTIMESTAMP,
    UPDATED_BY              NUMBER,
    UPDATED_DATE            TIMESTAMP,

    CONSTRAINT PK_CRM_FOLLOWUP
        PRIMARY KEY (FOLLOWUP_ID)
);
```

---

# 9. Lead History

This is **very important**.

You should know how a lead changed over time.

For example:

```text
25-Aug   New
26-Aug   Contacted
28-Aug   Qualified
30-Aug   Proposal
05-Sep   Negotiation
10-Sep   Won
```

Create:

```sql
CREATE TABLE CRM_LEAD_HISTORY (
    HISTORY_ID              NUMBER GENERATED BY DEFAULT AS IDENTITY,

    LEAD_ID                 NUMBER NOT NULL,

    OLD_STATUS_ID           NUMBER,
    NEW_STATUS_ID           NUMBER,

    OLD_ASSIGNED_TO         NUMBER,
    NEW_ASSIGNED_TO         NUMBER,

    ACTION_TYPE             VARCHAR2(50),

    REMARKS                 VARCHAR2(1000),

    CREATED_BY              NUMBER,
    CREATED_DATE            TIMESTAMP DEFAULT SYSTIMESTAMP,

    CONSTRAINT PK_CRM_LEAD_HISTORY
        PRIMARY KEY (HISTORY_ID),

    CONSTRAINT FK_CRM_LEAD_HISTORY_LEAD
        FOREIGN KEY (LEAD_ID)
        REFERENCES CRM_LEAD(LEAD_ID)
);
```

This gives you an audit trail for CRM.

---

# 10. Lead → Customer conversion

I'd handle conversion like this:

```text
CRM_LEAD
   │
   │ Qualified
   ▼
CRM_OPPORTUNITY
   │
   │ Won
   ▼
CRM_CUSTOMER
   │
   ├── CRM_CONTACT
   ├── CRM_CUSTOMER_ADDRESS
   └── Sales Transactions
```

Keep the original `LEAD_ID` in the customer/opportunity relationship where useful, so you can trace:

> **Which lead created this customer?**

---

# 11. Overall Oracle CRM ER structure

```text
                         ┌─────────────────┐
                         │  CRM_LEAD_TYPE  │
                         └────────┬────────┘
                                  │
┌─────────────────┐               │
│ CRM_LEAD_SOURCE │───────────────┤
└─────────────────┘               │
                                  ▼
                         ┌─────────────────┐
                         │    CRM_LEAD     │
                         └───────┬─────────┘
                                 │
                  ┌──────────────┼──────────────┐
                  │              │              │
                  ▼              ▼              ▼
           LEAD_HISTORY      ACTIVITY      OPPORTUNITY
                                                │
                                                │
                                                ▼
                                         ┌─────────────┐
                                         │  CUSTOMER   │
                                         └──────┬──────┘
                                                │
                              ┌─────────────────┼───────────────┐
                              │                 │               │
                              ▼                 ▼               ▼
                           CONTACT           ADDRESS        ACTIVITY
```

## 12. One important improvement for your Sales App

Since you're using **Oracle**, I wouldn't create a separate table for every tiny dropdown unless there's a business reason.

For example, these can be proper masters:

```text
CRM_LEAD_TYPE
CRM_LEAD_SOURCE
CRM_LEAD_STATUS
CRM_LEAD_PRIORITY
CRM_OPPORTUNITY_STAGE
CRM_ACTIVITY_TYPE
CRM_LOST_REASON
```

But things like:

```text
BILLING
SHIPPING
HOME
OFFICE
```

can simply be controlled with a check constraint or a centralized lookup table, depending on how configurable the application needs to be.

Also, if your Sales App already has **employee, product, branch, company, territory, payment term, and user** tables, **do not duplicate them inside CRM**. Reference the existing master tables with foreign keys.

### Recommended next step

For an Oracle project, the next useful artifact is a **complete CRM ERD + all table DDL with PK/FK/indexes/sequences and sample master data**.

**Which do you want next: `full DDL` or `ERD first`?**
