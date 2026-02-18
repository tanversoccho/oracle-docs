# FG Production Floor to Warehouse Operation Process Flow (AS-IS)

This flowchart illustrates the current (AS-IS) operational process for Finished Goods (FG) moving from the production floor to the warehouse. It covers steps including packing, palletizing, delivery options, inventory updates, and cross-checking production data with ERP systems.

**Key Terms:**

- FG: Finished Goods  
- ERP: Enterprise Resource Planning  
- CDC: Central Distribution Center  
- WIP: Work In Progress  

**Notes:**

- Auto Leveling is performed except for size 20 X 30 FG.  
- Production and Inventory teams confirm production data before ERP batch creation.  
- Cross-checking ensures data integrity between physical stock and ERP.

---

```mermaid
flowchart TD

    A["Kiln output and WIP Stock at Production Floor or Line"]
    B["FG Packing and Leveling - Auto and Manual"]
    C["Pallet Making and mark the pallet card - Manual"]
    D{"Direct Delivery from Production Floor"}
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
