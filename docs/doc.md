# Finished Goods Production Floor to Warehouse Process Flow (As-Is)

## Document Control

| Version | Date       | Author          | Changes                 |
|---------|------------|-----------------|-------------------------|
| 1.0     | 2026-02-15 | Operations Team | Initial as-is documentation |

## 1. Executive Summary

This document outlines the current (as-is) operational process for finished goods (FG) moving from the production floor to the warehouse at the manufacturing facility.

**Key Terms:**
- **FG:** Finished Goods
- **ERP:** Enterprise Resource Planning (SAP/Oracle)
- **CDC:** Central Distribution Center
- **WIP:** Work in Progress
- **QA:** Quality Assurance
- **GRN:** Goods Receipt Note

## 2. Process Overview

### 2.1 Current State Flowchart

```{.mermaid format=png}
flowchart TD
    A["Kiln Output and WIP Stock at Production Floor"]
    B["FG Packing and Leveling<br>(Auto and Manual)"]
    C["Pallet Making and Pallet Card Marking<br>(Manual)"]
    D{"Direct Delivery from Production Floor?"}
    E{"Check FG Availability"}
    F["Delivery from FG Warehouse"]
    G["Follow Direct Delivery Process"]
    H["Physical Transfer: Plant to FG Warehouse"]
    I["Create ERP Batch and Inter-Org Transfer<br>to FG Warehouse (CDC)"]
    J["FG Inventory and Warehouse Updated"]
    K["Production and Inventory Teams Confirm<br>Actual Production and Receiving Data"]
    L["Receive Production Data and Warehouse Location<br>via WhatsApp Group"]
    M["Cross-Check Physical Production Data<br>with ERP Data (Audit Team)"]
    N["Auto Leveling (Except Size 20x30 FG)"]

    A --> B
    B --> C
    B --> N
    C --> D

    D -- Yes --> E
    D -- No --> H

    E -- Yes --> G
    E -- No --> F

    G --> I
    H --> I

    K --> L
    L --> I

    I --> J
    I --> M
```

## 3. Key Stakeholders

| Role | Department |
|------|------------|
| Production Supervisor | Production |
| Quality Inspector | QA |
| Inventory Controller | Inventory Management |
| Warehouse Lead | Warehouse |
| Auditor | Audit Team |

## 4. Current Process Pain Points

| Issue | Impact |
|-------|--------|
| Manual pallet card marking | Data entry errors, misplacement |
| WhatsApp communication | Delayed updates, no audit trail |
| No real-time visibility | Production delays |
| Size 20x30 exception | Manual handling required |
| Batch creation after physical movement | System update lag |
| Manual audit cross-check | Delayed discrepancy detection |

## 5. Key Metrics

| KPI | Current | Target |
|-----|---------|--------|
| Inventory Accuracy | 92% | 99% |
| Transfer Lead Time | 5 hours | 3 hours |
| System Update Lag | 4 hours | 1 hour |
| Documentation Accuracy | 87% | 98% |

## 6. Process Automation Roadmap

### 6.1 Automation Overview

To address current pain points, the following automation initiatives are planned to streamline the FG transfer process, reduce manual errors, and enable real-time visibility.

### 6.2 Automation Solutions

| Pain Point | Automation Solution | How It Works | Benefit |
|------------|--------------------|--------------|---------|
| Manual pallet card marking | Barcode scanning at source | Print GS1-128 barcodes at packing station; scan at pallet creation to auto-validate against ERP | Eliminate manual writing, real-time data capture, prevent mislabeling |
| WhatsApp communication delays | WhatsApp Business API + ERP integration | Automated notifications triggered by ERP events: pallet ready, in transit, received, batch created | 70% reduction in follow-up delays, audit trail created |
| No real-time visibility | Mobile scanning throughout movement | Scan pallet at load (status: in transit), scan at warehouse receipt (status: received at bin), auto-update inventory | Real-time track and trace, reduced transfer time |
| System update lag | Trigger ERP batch creation from scans | Pallet labeled → creates pending batch; pallet received → auto-completes inter-org transfer, updates inventory | Real-time inventory, elimination of manual data entry |
| Manual audit cross-check | Continuous validation with alerts | System compares physical scans with expected output instantly; flags discrepancies immediately; auto-generates end-of-shift reports | Instant discrepancy detection, reduced audit effort |

### 6.3 Technology Requirements

| Need | Low-Cost Option | Enterprise Option |
|------|-----------------|-------------------|
| Barcode scanning | Smartphone + scanning app | Industrial scanners + WMS |
| Label printing | Desktop label printers | High-speed auto-labelers |
| WhatsApp integration | Twilio + custom code | ERP WhatsApp API module |
| ERP/WMS | Upgrade existing ERP modules | Full WMS implementation |

### 6.4 Implementation Roadmap



### 6.5 Expected Results After Automation

| Metric | Current | Target After Automation |
|--------|---------|------------------------|
| Inventory Accuracy | 92% | 99%+ |
| Transfer Lead Time | 5 hours | <2 hours |
| System Update Lag | 4 hours | Real-time |
| Documentation Accuracy | 87% | 98%+ |
| Manual Data Entry | 100% | <10% |

---

