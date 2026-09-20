# CRM System Architecture — Detailed Design

Based on the salesperson's workflow report, here's a complete system architecture to build this CRM.

---

## 1. High-Level Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐               │
│  │  Web App     │  │  Mobile App  │  │  Admin Panel │               │
│  │  (React/Next)│  │ (React Native│  │  (React)     │               │
│  │              │  │  / Flutter)  │  │              │               │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘               │
└─────────┼─────────────────┼─────────────────┼───────────────────────┘
          │                 │                 │
          └─────────────────┼─────────────────┘
                            │ HTTPS / WSS
┌───────────────────────────▼─────────────────────────────────────────┐
│                     API GATEWAY / BFF                                │
│  (Kong / AWS API Gateway / Nginx + Rate Limiting + Auth)            │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────────┐
│                    APPLICATION LAYER (Services)                      │
│                                                                      │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐        │
│  │  Lead      │ │  Contact   │ │  Deal      │ │  Activity  │        │
│  │  Service   │ │  Service   │ │  Service   │ │  Service   │        │
│  └────────────┘ └────────────┘ └────────────┘ └────────────┘        │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐        │
│  │  Comms     │ │  Quote     │ │  Forecast  │ │  Reporting │        │
│  │  Service   │ │  Service   │ │  Service   │ │  Service   │        │
│  └────────────┘ └────────────┘ └────────────┘ └────────────┘        │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐        │
│  │ Automation │ │Integration │ │  Admin/    │ │  Notif.    │        │
│  │  Engine    │ │  Service   │ │  Auth      │ │  Service   │        │
│  └────────────┘ └────────────┘ └────────────┘ └────────────┘        │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────────┐
│                      DATA LAYER                                      │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                 │
│  │ PostgreSQL   │ │   Redis      │ │  Elasticsearch│                │
│  │ (Primary DB) │ │ (Cache/Queue)│ │  (Search)     │                │
│  └──────────────┘ └──────────────┘ └──────────────┘                 │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                 │
│  │  S3/MinIO    │ │  ClickHouse  │ │  RabbitMQ/   │                 │
│  │ (Files/Docs) │ │ (Analytics)  │ │  Kafka       │                 │
│  └──────────────┘ └──────────────┘ └──────────────┘                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Technology Stack Recommendation

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| **Frontend Web** | React + Next.js + TypeScript + Tailwind | SSR, fast, component reuse |
| **Mobile** | React Native (or Flutter) | Code sharing with web |
| **API Gateway** | Kong / AWS API Gateway | Auth, rate limiting, routing |
| **Backend** | Node.js (NestJS) or Python (FastAPI/Django) | Fast dev, async, typed |
| **Primary DB** | PostgreSQL | Relational integrity, JSONB for custom fields |
| **Cache** | Redis | Sessions, queues, real-time counters |
| **Search** | Elasticsearch / OpenSearch | Full-text search across leads/contacts |
| **Analytics** | ClickHouse | OLAP for reports/forecasting |
| **Queue** | RabbitMQ / Kafka | Async jobs, automation, webhooks |
| **File Storage** | AWS S3 / MinIO | Attachments, quotes, recordings |
| **Auth** | Keycloak / Auth0 / Supabase Auth | SSO, RBAC, MFA |
| **Realtime** | WebSockets (Socket.io) | Live pipeline updates, notifications |
| **Infra** | Docker + Kubernetes (EKS) | Scalability, isolation |
| **CI/CD** | GitHub Actions + ArgoCD | Automated deploys |
| **Monitoring** | Prometheus + Grafana + Sentry | Metrics, logs, errors |

---

## 3. Database Schema (Core Modules)

### 3.1 Lead Management

```sql
CREATE TABLE leads (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id       UUID NOT NULL,
    first_name      VARCHAR(100),
    last_name       VARCHAR(100),
    email           VARCHAR(255),
    phone           VARCHAR(50),
    company_name    VARCHAR(255),
    job_title       VARCHAR(150),
    source          VARCHAR(50),        -- website, referral, cold_call, ads
    source_detail   JSONB,              -- UTM params, campaign id
    score           INTEGER DEFAULT 0,  -- computed hot/warm/cold
    status          VARCHAR(30) DEFAULT 'new',
                    -- new | contacted | qualified | converted | lost
    owner_id        UUID,               -- assigned sales rep
    custom_fields   JSONB,
    created_at      TIMESTAMPTZ DEFAULT NOW(),
    updated_at      TIMESTAMPTZ DEFAULT NOW(),
    converted_at    TIMESTAMPTZ
);

CREATE INDEX idx_leads_tenant_status ON leads(tenant_id, status);
CREATE INDEX idx_leads_owner ON leads(owner_id);
CREATE INDEX idx_leads_email ON leads(email);
```

### 3.2 Contacts & Accounts

```sql
CREATE TABLE accounts (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id       UUID NOT NULL,
    name            VARCHAR(255) NOT NULL,
    industry        VARCHAR(100),
    website         VARCHAR(255),
    parent_id       UUID REFERENCES accounts(id),  -- hierarchy
    annual_revenue  NUMERIC(15,2),
    employee_count  INTEGER,
    owner_id        UUID,
    custom_fields   JSONB,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE contacts (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id       UUID NOT NULL,
    account_id      UUID REFERENCES accounts(id),
    first_name      VARCHAR(100),
    last_name       VARCHAR(100),
    email           VARCHAR(255),
    phone           VARCHAR(50),
    linkedin_url    VARCHAR(255),
    role            VARCHAR(50),   -- decision_maker | influencer | gatekeeper
    tags            TEXT[],
    custom_fields   JSONB,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE contact_roles (
    contact_id      UUID REFERENCES contacts(id),
    account_id      UUID REFERENCES accounts(id),
    role_type       VARCHAR(50),
    PRIMARY KEY (contact_id, account_id, role_type)
);
```

### 3.3 Deals / Opportunities

```sql
CREATE TABLE pipelines (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id       UUID NOT NULL,
    name            VARCHAR(100),
    is_default      BOOLEAN DEFAULT FALSE
);

CREATE TABLE pipeline_stages (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pipeline_id     UUID REFERENCES pipelines(id),
    name            VARCHAR(100),   -- Discovery, Demo, Proposal...
    position        INTEGER,
    probability     INTEGER,        -- default win prob %
    rotting_days    INTEGER         -- alert if no activity
);

CREATE TABLE deals (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id       UUID NOT NULL,
    account_id      UUID REFERENCES accounts(id),
    primary_contact UUID REFERENCES contacts(id),
    title           VARCHAR(255),
    value           NUMERIC(15,2),
    currency        VARCHAR(3) DEFAULT 'USD',
    stage_id        UUID REFERENCES pipeline_stages(id),
    probability     INTEGER,
    expected_close  DATE,
    actual_close    DATE,
    status          VARCHAR(20) DEFAULT 'open',  -- open | won | lost
    win_reason      TEXT,
    loss_reason     TEXT,
    owner_id        UUID,
    last_activity_at TIMESTAMPTZ,
    custom_fields   JSONB,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE deal_competitors (
    deal_id         UUID REFERENCES deals(id),
    competitor_name VARCHAR(150),
    notes           TEXT
);
```

### 3.4 Activities & Tasks

```sql
CREATE TABLE activities (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id       UUID NOT NULL,
    type            VARCHAR(30),  -- call | email | meeting | note | task
    subject         VARCHAR(255),
    body            TEXT,
    outcome         VARCHAR(50),  -- connected | no_answer | busy
    related_to_type VARCHAR(20),  -- lead | contact | deal | account
    related_to_id   UUID,
    owner_id        UUID,
    due_at          TIMESTAMPTZ,
    completed_at    TIMESTAMPTZ,
    priority        VARCHAR(10),  -- low | medium | high
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_activities_related ON activities(related_to_type, related_to_id);
CREATE INDEX idx_activities_owner_due ON activities(owner_id, due_at);
```

### 3.5 Communication Hub

```sql
CREATE TABLE messages (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id       UUID NOT NULL,
    channel         VARCHAR(20),  -- email | whatsapp | sms | call
    direction       VARCHAR(10),  -- inbound | outbound
    from_address    VARCHAR(255),
    to_address      VARCHAR(255),
    subject         VARCHAR(255),
    body            TEXT,
    thread_id       UUID,
    related_to_type VARCHAR(20),
    related_to_id   UUID,
    status          VARCHAR(20),  -- sent | delivered | opened | replied
    opened_at       TIMESTAMPTZ,
    replied_at      TIMESTAMPTZ,
    metadata        JSONB,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE email_templates (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id       UUID NOT NULL,
    name            VARCHAR(150),
    subject         VARCHAR(255),
    body_html       TEXT,
    variables       JSONB,
    created_by      UUID
);
```

### 3.6 Quotations & Proposals

```sql
CREATE TABLE products (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id       UUID NOT NULL,
    sku             VARCHAR(50),
    name            VARCHAR(255),
    description     TEXT,
    unit_price      NUMERIC(15,2),
    currency        VARCHAR(3),
    tax_rate        NUMERIC(5,2)
);

CREATE TABLE quotes (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id       UUID NOT NULL,
    deal_id         UUID REFERENCES deals(id),
    quote_number    VARCHAR(50) UNIQUE,
    version         INTEGER DEFAULT 1,
    status          VARCHAR(20),  -- draft | sent | viewed | signed | rejected
    subtotal        NUMERIC(15,2),
    discount        NUMERIC(15,2),
    tax             NUMERIC(15,2),
    total           NUMERIC(15,2),
    valid_until     DATE,
    pdf_url         VARCHAR(500),
    signed_at       TIMESTAMPTZ,
    signature_url   VARCHAR(500),
    created_by      UUID,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE quote_items (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    quote_id        UUID REFERENCES quotes(id) ON DELETE CASCADE,
    product_id      UUID REFERENCES products(id),
    description     TEXT,
    quantity        NUMERIC(10,2),
    unit_price      NUMERIC(15,2),
    discount        NUMERIC(15,2),
    total           NUMERIC(15,2)
);

CREATE TABLE quote_approvals (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    quote_id        UUID REFERENCES quotes(id),
    approver_id     UUID,
    status          VARCHAR(20),  -- pending | approved | rejected
    comments        TEXT,
    acted_at        TIMESTAMPTZ
);
```

### 3.7 Automation & Workflows

```sql
CREATE TABLE workflows (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id       UUID NOT NULL,
    name            VARCHAR(150),
    trigger_type    VARCHAR(50),  -- lead_created | stage_changed | no_activity
    trigger_config  JSONB,
    conditions      JSONB,
    actions         JSONB,        -- [{type: send_email, template_id: ...}]
    is_active       BOOLEAN DEFAULT TRUE,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE workflow_runs (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    workflow_id     UUID REFERENCES workflows(id),
    entity_type     VARCHAR(20),
    entity_id       UUID,
    status          VARCHAR(20),  -- running | success | failed
    started_at      TIMESTAMPTZ,
    finished_at     TIMESTAMPTZ,
    error           TEXT
);
```

### 3.8 Admin, Auth & Audit

```sql
CREATE TABLE tenants (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name            VARCHAR(150),
    plan            VARCHAR(30),
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE users (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id       UUID REFERENCES tenants(id),
    email           VARCHAR(255) UNIQUE,
    password_hash   VARCHAR(255),
    full_name       VARCHAR(150),
    role            VARCHAR(30),  -- rep | manager | admin
    manager_id      UUID REFERENCES users(id),
    territory       VARCHAR(100),
    is_active       BOOLEAN DEFAULT TRUE
);

CREATE TABLE audit_logs (
    id              BIGSERIAL PRIMARY KEY,
    tenant_id       UUID,
    user_id         UUID,
    action          VARCHAR(50),
    entity_type     VARCHAR(50),
    entity_id       UUID,
    before_state    JSONB,
    after_state     JSONB,
    ip_address      INET,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);
```

---

## 4. Service Layer Design

### 4.1 Service Responsibilities

| Service | Responsibility | Key Endpoints |
|---------|---------------|---------------|
| **Lead Service** | CRUD, scoring, dedup, assignment | `POST /leads`, `POST /leads/:id/convert` |
| **Contact Service** | Contacts, accounts, hierarchy | `GET /contacts`, `POST /accounts` |
| **Deal Service** | Pipeline, stages, rotting alerts | `PATCH /deals/:id/stage`, `GET /pipeline` |
| **Activity Service** | Tasks, calls, meetings, timeline | `POST /activities`, `GET /timeline/:entityId` |
| **Comms Service** | Email, WhatsApp, SMS, calls | `POST /messages/send`, `GET /inbox` |
| **Quote Service** | Quotes, products, approvals, e-sign | `POST /quotes`, `POST /quotes/:id/sign` |
| **Forecast Service** | Weighted pipeline, targets | `GET /forecast?period=Q1` |
| **Reporting Service** | Dashboards, win/loss, custom reports | `GET /reports/:type` |
| **Automation Engine** | Workflow triggers, actions | Internal + `POST /workflows` |
| **Integration Service** | Gmail, Outlook, Twilio, Zapier | OAuth callbacks, webhooks |
| **Notification Service** | In-app, email, push | `GET /notifications` |
| **Auth/Admin Service** | RBAC, tenants, audit | `POST /auth/login`, `GET /audit-logs` |

### 4.2 Inter-Service Communication

- **Synchronous**: REST/gRPC for request-response (e.g., Deal Service → Contact Service to fetch account).
- **Asynchronous**: Event bus (Kafka/RabbitMQ) for domain events:
  - `lead.created` → triggers scoring, auto-assignment
  - `deal.stage_changed` → triggers task creation, forecast recalc
  - `quote.signed` → triggers deal stage update, notification
  - `activity.logged` → updates deal `last_activity_at`

### 4.3 Event-Driven Flow Example

```
[Lead Created] 
    │
    ▼
Event: lead.created
    │
    ├──► Scoring Service (compute score)
    ├──► Dedup Service (check duplicates)
    ├──► Assignment Service (round-robin / territory)
    ├──► Workflow Engine (trigger drip sequence)
    └──► Notification Service (notify rep)
```

---

## 5. API Design (REST + WebSocket)

### 5.1 REST Conventions

```
GET    /api/v1/leads?status=new&owner_id=...&page=1&limit=50
POST   /api/v1/leads
GET    /api/v1/leads/:id
PATCH  /api/v1/leads/:id
DELETE /api/v1/leads/:id
POST   /api/v1/leads/:id/convert    → creates contact + account + deal
```

### 5.2 Sample Payloads

**Create Lead**
```json
POST /api/v1/leads
{
  "first_name": "Jane",
  "last_name": "Doe",
  "email": "jane@acme.com",
  "company_name": "Acme Corp",
  "source": "website",
  "source_detail": { "utm_source": "google", "utm_campaign": "q1" }
}
```

**Move Deal Stage**
```json
PATCH /api/v1/deals/abc-123/stage
{
  "stage_id": "stage-proposal-uuid",
  "note": "Proposal sent via email"
}
```

### 5.3 WebSocket Channels

```
ws://api/v1/ws?token=...
  ├── pipeline:updates      → real-time kanban updates
  ├── notifications:user    → task reminders, mentions
  └── inbox:new_message     → incoming email/WhatsApp
```

---

## 6. Frontend Architecture

### 6.1 Web App Structure (Next.js)

```
/app
  /(auth)/login
  /(dashboard)
    /leads          → list + detail + convert
    /contacts       → list + detail + timeline
    /accounts
    /deals          → kanban + list + detail
    /activities     → tasks + calendar
    /inbox          → unified communication
    /quotes         → builder + list
    /reports        → dashboards
    /settings       → admin, users, fields
/components
  /ui               → buttons, modals, tables
  /leads            → LeadTable, LeadForm, LeadScoreBadge
  /deals            → KanbanBoard, DealCard, StageColumn
  /shared           → Timeline, ActivityFeed, FileUpload
/lib
  /api              → API client (React Query)
  /hooks            → useLeads, useDeals, useAuth
  /store            → Zustand/Redux for global state
```

### 6.2 Key UI Patterns

- **Kanban Board**: drag-drop with optimistic updates, WebSocket sync.
- **Timeline**: infinite scroll, grouped by date, filterable by type.
- **Global Search**: Elasticsearch-backed, Cmd+K palette.
- **Quick Add**: 1-click lead/task creation from anywhere.

---

## 7. Mobile & Offline Architecture

```
┌─────────────────────────────────────┐
│  Mobile App (React Native)          │
│  ┌───────────────────────────────┐  │
│  │  Local SQLite / WatermelonDB  │  │
│  │  (offline queue + cache)      │  │
│  └──────────────┬────────────────┘  │
│                 │ sync              │
│  ┌──────────────▼────────────────┐  │
│  │  Sync Engine                  │  │
│  │  - conflict resolution        │  │
│  │  - delta sync                 │  │
│  │  - retry on reconnect         │  │
│  └──────────────┬────────────────┘  │
└─────────────────┼───────────────────┘
                  │ HTTPS
          ┌───────▼────────┐
          │  API Gateway   │
          └────────────────┘
```

**Offline features:**
- Local queue for activities, notes, stage changes.
- GPS check-in stored locally, synced when online.
- Business card scanner (OCR on-device via ML Kit).
- Voice-to-text using platform APIs.

---

## 8. Integration Architecture

```
┌──────────────────────────────────────────────────────────┐
│                  Integration Service                      │
│                                                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│  │  OAuth      │  │  Webhook    │  │  Sync       │       │
│  │  Manager    │  │  Receiver   │  │  Workers    │       │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘       │
│         │                │                │              │
│  ┌──────▼────────────────▼────────────────▼──────┐       │
│  │           Connector Registry                   │       │
│  │  Gmail | Outlook | Twilio | WhatsApp | Tally  │       │
│  │  QuickBooks | Mailchimp | Zapier | Slack      │       │
│  └────────────────────────────────────────────────┘       │
└──────────────────────────────────────────────────────────┘
```

**Patterns:**
- **OAuth 2.0** for user-authorized integrations (Gmail, Outlook).
- **Webhooks** for inbound events (email replies, call status).
- **Polling workers** for systems without webhooks (Tally, some ERPs).
- **Zapier/Make** for long-tail integrations via REST hooks.

---

## 9. Automation Engine Design

```
Trigger → Conditions → Actions
```

**Triggers:**
- `lead.created`, `deal.stage_changed`, `activity.completed`
- `time.based` (cron: no activity in X days)
- `webhook.received`

**Conditions:**
- Field comparisons (`deal.value > 10000`)
- Logical operators (AND/OR)
- Time windows

**Actions:**
- Send email / WhatsApp
- Create task
- Update field
- Assign owner
- Call webhook
- Delay / wait

**Implementation:**
- Workflow definitions stored as JSON.
- Executed by a durable workflow engine (Temporal / Camunda / custom on BullMQ).
- Each run logged in `workflow_runs` for audit.

---

## 10. Reporting & Analytics Architecture

```
┌──────────────┐     CDC      ┌──────────────┐    ┌──────────────┐
│ PostgreSQL   │ ───────────► │  ClickHouse  │───►│  Metabase /  │
│ (OLTP)       │  (Debezium)  │  (OLAP)      │    │  Superset    │
└──────────────┘              └──────────────┘    └──────────────┘
```

- **CDC** (Change Data Capture) streams Postgres changes to ClickHouse.
- **Pre-aggregated tables** for dashboards (daily/weekly/monthly).
- **Custom Report Builder**: query builder UI → SQL generation → results cache.

**Key Reports:**
- Pipeline velocity, stage conversion, win/loss, sales cycle length.
- Activity vs. outcome correlation.
- Rep leaderboards, target vs. achievement.

---

## 11. Security & Multi-Tenancy

| Concern | Approach |
|---------|----------|
| **Auth** | JWT + refresh tokens, OAuth2, SAML/SSO for enterprise |
| **RBAC** | Role-based (`rep`, `manager`, `admin`) + record-level sharing rules |
| **Tenant Isolation** | `tenant_id` on every table; row-level security (RLS) in Postgres |
| **Encryption** | TLS in transit, AES-256 at rest, field-level for PII |
| **Audit** | `audit_logs` table + immutable log stream |
| **Rate Limiting** | API Gateway per-tenant and per-user |
| **GDPR** | Data export, right-to-be-forgotten, consent tracking |
| **Secrets** | HashiCorp Vault / AWS Secrets Manager |

---

## 12. Deployment & Scalability

### 12.1 Kubernetes Topology

```
┌─────────────────────────────────────────────────┐
│  Ingress (NGINX / ALB)                          │
│    ├── api.example.com   → API Gateway          │
│    ├── app.example.com   → Web Frontend         │
│    └── ws.example.com    → WebSocket Service    │
└─────────────────────────────────────────────────┘
         │
┌────────▼────────────────────────────────────────┐
│  Namespaces                                      │
│  ├── crm-core      (services, HPA 3-20 pods)    │
│  ├── crm-workers   (automation, sync, jobs)     │
│  ├── crm-data      (Postgres, Redis, ES)        │
│  └── crm-observ    (Prometheus, Grafana, Loki)  │
└─────────────────────────────────────────────────┘
```

### 12.2 Scaling Strategy

- **Horizontal**: stateless services auto-scale on CPU/RPS.
- **Database**: read replicas for reporting; partitioning for `activities`, `messages`, `audit_logs`.
- **Cache**: Redis for sessions, hot data, rate limits.
- **Queue**: Kafka for high-throughput events; RabbitMQ for task queues.
- **CDN**: CloudFront/Cloudflare for static assets and PDFs.

---

## 13. Build Phases (Aligned with Salesperson's Priority)

| Phase | Modules | Deliverables |
|-------|---------|--------------|
| **Phase 1 (MVP)** | Lead, Contact, Deal, Activity | Auth, core CRUD, Kanban, timeline |
| **Phase 2** | Comms, Quote, Reporting | Unified inbox, quote builder, dashboards |
| **Phase 3** | Automation, Forecast, Mobile | Workflow engine, forecasting, RN app |
| **Phase 4** | Integrations, Admin, AI | Gmail/Outlook, RBAC, AI scoring/drafting |

---

## 14. AI Layer (Phase 4)

| Feature | Implementation |
|---------|---------------|
| **Lead Scoring** | Gradient boosting on historical conversions |
| **Next Best Action** | LLM + rules on deal context |
| **Email Drafting** | GPT-based, fine-tuned on rep's past emails |
| **Deal Risk Scoring** | Features: activity recency, stage duration, engagement |
| **Call Transcription** | Whisper API → summary → CRM note |
| **Duplicate Detection** | Fuzzy matching (Levenshtein + embeddings) |

---

## 15. Summary Diagram — End-to-End

```
[Web/Mobile] → [API Gateway] → [Microservices] → [Postgres/Redis/ES/ClickHouse]
                    │                  │
                    │                  ├── [Event Bus] → [Automation] → [Actions]
                    │                  ├── [Integration Service] → [Gmail/Twilio/...]
                    │                  └── [Notification Service] → [Email/Push/In-app]
                    │
                    └── [WebSocket] → real-time updates to clients
```

---
