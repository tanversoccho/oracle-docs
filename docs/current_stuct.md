# FG Production Floor to Warehouse Operation Process Flow (AS-IS)

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-15 | Operations Team | Initial AS-IS documentation |

## 1. Executive Summary
This document outlines the current (AS-IS) operational process for Finished Goods (FG) moving from the production floor to the warehouse at the manufacturing facility. The process involves multiple departments including Production, Quality Control, Inventory Management, and Warehouse Operations.

**Key Terms:**
- FG: Finished Goods
- ERP: Enterprise Resource Planning (SAP/Oracle)
- CDC: Central Distribution Center
- WIP: Work In Progress
- SKU: Stock Keeping Unit
- QA: Quality Assurance
- GRN: Goods Receipt Note

## 2. Process Overview

### 2.1 Current State Flowchart

```mermaid
flowchart TD
    A["Kiln output and WIP Stock at Production Floor or Line"]
    B["FG Packing and Leveling - Auto and Manual"]
    C["Pallet Making and mark the pallet card - Manual"]
    D{"Direct Delivery from Production Floor?"}
    E{"Checking FG Availability"}
    F["Delivery from FG Warehouse"]
    G["Follow the Direct Delivery Process"]
    H["FG Received from plant and transfer to FG warehouse physically"]
    I["Create ERP Batch and Inter org transfer to FG warehouse location CDC in ERP"]
    J["FG Inventory and Warehouse Updated"]
    K["Production and Inventory team confirm Actual Production and Receiving FG data"]
    L["Get Production data and warehouse location info via WhatsApp group"]
    M["Cross check physical production data with ERP data by audit and store department"]
    N["Auto Leveling except size 20 X 30 FG"]

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

Version

