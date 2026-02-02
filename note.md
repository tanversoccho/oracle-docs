# oracle 

---

## 🏢 What is **Oracle E-Business Suite (EBS)**?

**Oracle EBS** is a huge **ERP (Enterprise Resource Planning)** system made by Oracle.

Think of it as a **complete software ecosystem** that runs an entire company:

* Finance 💰
* HR 👥
* Supply Chain 📦
* Manufacturing 🏭
* Projects 📊
* Procurement 🛒
  …and more.

Each area is divided into **modules**. Companies pick the modules they need.

---

## 📦 What is an **EBS Module**?

A **module** in Oracle EBS = a **functional area of business** with its own screens, tables, workflows, and reports.

Examples:

| Area         | Module Name           |
| ------------ | --------------------- |
| Accounting   | General Ledger (GL)   |
| Buying       | Purchasing (PO)       |
| Selling      | Order Management (OM) |
| Inventory    | Inventory (INV)       |
| Supply Chain | SCM                   |
| Warehousing  | WMS                   |

Modules are **connected**, so data flows between them automatically.

Example:
Sales Order → Inventory Check → Shipping → Invoice → Accounting Entry
All across different modules.

---

## 🚚 What is **SCM Module** in Oracle EBS?

**SCM = Supply Chain Management**

This isn’t just one screen — it’s a **group of modules** that manage the movement of goods from supplier → warehouse → customer.

### Core SCM Modules in EBS

| Module                      | What It Does                               |
| --------------------------- | ------------------------------------------ |
| Inventory (INV)         | Tracks items, stock levels, subinventories |
| Purchasing (PO)         | Creates purchase orders to suppliers       |
| Order Management (OM)   | Handles customer sales orders              |
| Bills of Material (BOM) | Defines product components                 |
| Work in Process (WIP)   | Manufacturing jobs                         |
| Shipping Execution      | Delivery and shipment tracking             |
| Advanced Pricing        | Pricing rules and discounts                |

👉 In short: **SCM controls product flow and stock**.

---

## 🏬 What is **WMS Module** in Oracle EBS?

**WMS = Warehouse Management System**

This is an **advanced extension** of the Inventory module.

While **Inventory** tracks *how many items you have*,
**WMS tracks exactly WHERE they are inside the warehouse**.

### What WMS Handles

| Feature                           | Explanation                            |
| --------------------------------- | -------------------------------------- |
| 📍 **Locator Control**            | Exact bin/shelf/rack location          |
| 📦 **LPN (License Plate Number)** | Tracks items inside boxes/pallets      |
| 🤖 **Barcode/RF Devices**         | Handheld scanners for warehouse staff  |
| 🔄 **Putaway Rules**              | Where new items should be stored       |
| 🧭 **Picking Rules**              | Best location to pick items for orders |
| 📊 **Cycle Counting**             | Physical stock counting                |
| 🚚 **Wave Picking**               | Bulk picking for many orders           |

### Example

Without WMS:

> “We have 500 laptops in warehouse.”

With WMS:

> “50 laptops → Rack A / Shelf 3
> 200 laptops → Rack B / Bin 12
> 250 laptops → Pallet P-443”

It gives **warehouse-level intelligence**.

---

## 🧠 Simple Difference

| Module  | Focus                                                          |
| ------- | -------------------------------------------------------------- |
| **SCM** | Big picture supply chain (buying, storing, selling, shipping)  |
| **WMS** | Detailed warehouse operations (bins, racks, scanners, pallets) |

So:

> SCM = Supply Chain Management
> WMS = Warehouse Control System

Love it — now we’re getting into **real Oracle EBS technical territory** 🔥
I’ll split this into **SCM core tables** and **WMS tables**.

---

# 📦 ORACLE EBS – SCM IMPORTANT TABLES

## 🏷️ 1️⃣ Inventory (INV) Tables

These track items and stock.

| Table  | Purpose  |
| --- | --- |
| MTL_SYSTEM_ITEMS_B | Master item definition (item name, UOM, type) |
| MTL_SYSTEM_ITEMS_TL| Item description (language-wise)    |
| MTL_PARAMETERS | Inventory organization setup |
| MTL_ONHAND_QUANTITIES_DETAIL| Current on-hand stock by locator |
| MTL_RESERVATIONS| Reserved quantities for orders  |
| MTL_DEMAND| Demand for items  |
| MTL_MATERIAL_TRANSACTIONS| Every inventory movement (issues, receipts, transfers) |
| MTL_TRANSACTION_TYPES| Type of inventory transactions  |
| MTL_TXN_REQUEST_HEADERS| Move order headers |
| MTL_TXN_REQUEST_LINES| Move order lines |

💡 **Most important** for stock:
👉 `MTL_ONHAND_QUANTITIES_DETAIL`
👉 `MTL_MATERIAL_TRANSACTIONS`

---

## 🛒 2️⃣ Purchasing (PO) Tables

These manage suppliers and purchase orders.

| Table                     | Purpose                   |
| ------------------------- | ------------------------- |
| **PO_HEADERS_ALL**        | Purchase Order header     |
| **PO_LINES_ALL**          | PO line items             |
| **PO_LINE_LOCATIONS_ALL** | Shipment schedules        |
| **PO_DISTRIBUTIONS_ALL**  | Accounting distributions  |
| **PO_VENDORS**            | Supplier master           |
| **PO_VENDOR_SITES_ALL**   | Supplier sites            |
| **RCV_SHIPMENT_HEADERS**  | Receiving shipment header |
| **RCV_SHIPMENT_LINES**    | Receiving lines           |
| **RCV_TRANSACTIONS**      | Receiving transactions    |

💡 Receiving stock into inventory flows from
`PO → RCV_TRANSACTIONS → MTL_MATERIAL_TRANSACTIONS`

---

## 📦 3️⃣ Order Management (OM) Tables

These handle customer sales orders.

| Table                        | Purpose                            |
| ---------------------------- | ---------------------------------- |
| OE_ORDER_HEADERS_ALL     | Sales order header                 |
| OE_ORDER_LINES_ALL       | Sales order lines                  |
| OE_ORDER_HOLDS_ALL       | Order holds                        |
| WSH_DELIVERY_DETAILS     | Delivery line details              |
| WSH_DELIVERY_ASSIGNMENTS | Delivery assignments               |
| WSH_NEW_DELIVERIES       | Delivery header                    |
| RA_CUSTOMER_TRX_ALL      | AR Invoice header (after shipping) |

💡 Order Flow:
`OM Order → Shipping → AR Invoice`

---

# 🏬 ORACLE WMS IMPORTANT TABLES

WMS adds warehouse-level control on top of Inventory.

---

## 📍 Locator & Warehouse Structure

| Table                         | Purpose                                |
| ----------------------------- | -------------------------------------- |
| **MTL_ITEM_LOCATIONS**        | Warehouse locators (rack/bin/shelf)    |
| **MTL_SECONDARY_INVENTORIES** | Subinventories (stores, staging, etc.) |

---

## 📦 LPN (License Plate Number) Tables

These track cartons/pallets.

| Table                         | Purpose                 |
| ----------------------------- | ----------------------- |
| **WMS_LICENSE_PLATE_NUMBERS** | LPN master              |
| **WMS_LPN_CONTENTS**          | Items inside each LPN   |
| **WMS_LPN_HISTORY**           | LPN transaction history |

---

## 🤖 Warehouse Execution Tables

| Table                    | Purpose                                    |
| ------------------------ | ------------------------------------------ |
| **WMS_TASKS**            | Warehouse tasks (pick, putaway, replenish) |
| **WMS_DISPATCHED_TASKS** | Tasks sent to RF devices                   |
| **WMS_TASK_HISTORY**     | Completed tasks history                    |
| **WMS_WAVE_HEADERS**     | Wave picking header                        |
| **WMS_WAVE_LINES**       | Wave picking lines                         |

---

## 🔄 Rules Engine (Putaway / Picking Rules)

| Table                     | Purpose              |
| ------------------------- | -------------------- |
| **WMS_RULES**             | Warehouse rules      |
| **WMS_STRATEGIES**        | Rule strategies      |
| **WMS_RULE_RESTRICTIONS** | Conditions for rules |

---

# 🔥 MOST ASKED TABLES IN INTERVIEWS

If someone asks about **SCM/WMS technical knowledge**, mention these confidently:

| Area            | Must-Know Tables                             |
| --------------- | -------------------------------------------- |
| Items           | `MTL_SYSTEM_ITEMS_B`                         |
| Onhand          | `MTL_ONHAND_QUANTITIES_DETAIL`               |
| Transactions    | `MTL_MATERIAL_TRANSACTIONS`                  |
| Purchase Orders | `PO_HEADERS_ALL`, `PO_LINES_ALL`             |
| Sales Orders    | `OE_ORDER_HEADERS_ALL`, `OE_ORDER_LINES_ALL` |
| Shipping        | `WSH_DELIVERY_DETAILS`                       |
| Locators        | `MTL_ITEM_LOCATIONS`                         |
| LPN             | `WMS_LICENSE_PLATE_NUMBERS`                  |
| Tasks           | `WMS_TASKS`                                  |

---

Let’s map the **full warehouse/product movement flow** with tables and interface points.

---

# 🔄 Oracle EBS SCM/WMS Table Flow (Technical Developer Perspective)

This is **step-by-step from Purchase → Inventory → Warehouse → Order → Ship → Invoice**.

---

## 1️⃣ Purchase Order (PO) → Receiving

**Goal:** Bring items from suppliers into inventory.

| Step                  | Oracle Module | Tables Used                                                 | Notes                                      |
| --------------------- | ------------- | ----------------------------------------------------------- | ------------------------------------------ |
| Create Purchase Order | PO            | `PO_HEADERS_ALL`, `PO_LINES_ALL`, `PO_LINE_LOCATIONS_ALL`   | PO header/lines created in standard tables |
| Ship from Supplier    | PO → RCV      | `RCV_SHIPMENT_HEADERS`, `RCV_SHIPMENT_LINES`                | Receiving shipment creation                |
| Receive Goods         | RCV           | `RCV_TRANSACTIONS`, `RCV_TRANSACTION_DISTRIBUTIONS`         | Quantity, lot, serial tracked              |
| Post to Inventory     | INV           | `MTL_MATERIAL_TRANSACTIONS`, `MTL_ONHAND_QUANTITIES_DETAIL` | Updates stock levels automatically         |

> **Tip:** If you use **interface tables**, you can bulk load POs via `PO_HEADERS_INTERFACE` + `PO_LINES_INTERFACE`.

---

## 2️⃣ Inventory → WMS Putaway

**Goal:** Store items in proper warehouse locations (bins/racks).

| Step                | Module | Tables                                          | Notes                             |
| ------------------- | ------ | ----------------------------------------------- | --------------------------------- |
| Assign Subinventory | INV    | `MTL_SECONDARY_INVENTORIES`                     | Subinventory = storage area       |
| Assign Locator      | WMS    | `MTL_ITEM_LOCATIONS`                            | Exact rack/bin for the item       |
| LPN Creation        | WMS    | `WMS_LICENSE_PLATE_NUMBERS`, `WMS_LPN_CONTENTS` | Track pallets/cartons             |
| Warehouse Task      | WMS    | `WMS_TASKS`, `WMS_DISPATCHED_TASKS`             | Tasks generated for RF scanners   |
| Complete Task       | WMS    | `WMS_TASK_HISTORY`                              | Task completed, inventory updated |

> Stock is now **physically in warehouse** and correctly tracked.

---

## 3️⃣ Order Management → Picking

**Goal:** Pick items to fulfill customer sales orders.

| Step                | Module | Tables                                                                   | Notes                                    |
| ------------------- | ------ | ------------------------------------------------------------------------ | ---------------------------------------- |
| Sales Order Entry   | OE     | `OE_ORDER_HEADERS_ALL`, `OE_ORDER_LINES_ALL`                             | Standard sales order tables              |
| Assign Shipments    | WSH    | `WSH_NEW_DELIVERIES`, `WSH_DELIVERY_DETAILS`, `WSH_DELIVERY_ASSIGNMENTS` | Delivery header & lines created          |
| Generate Pick Tasks | WMS    | `WMS_TASKS`                                                              | Picking rules applied (FIFO, FEFO, etc.) |
| Pick Confirmation   | WMS    | `WMS_TASK_HISTORY`, `MTL_MATERIAL_TRANSACTIONS`                          | Updates inventory on hand                |

> Picking is guided by **WMS rules** (strategies, zones, wave picking).

---

## 4️⃣ Shipping → Invoicing

**Goal:** Ship items to customer and generate invoice.

| Step                | Module | Tables                                                      | Notes                       |
| ------------------- | ------ | ----------------------------------------------------------- | --------------------------- |
| Ship Confirmation   | WSH    | `WSH_DELIVERY_DETAILS`, `WSH_NEW_DELIVERIES`                | Status updated to shipped   |
| Update Inventory    | INV    | `MTL_MATERIAL_TRANSACTIONS`, `MTL_ONHAND_QUANTITIES_DETAIL` | Stock reduced               |
| Generate AR Invoice | AR     | `RA_CUSTOMER_TRX_ALL`, `RA_CUSTOMER_TRX_LINES_ALL`          | Invoice posted for customer |

---

## 5️⃣ Key Interface Tables (Developer Focus)

| Purpose                      | Table                                        |
| ---------------------------- | -------------------------------------------- |
| Import POs                   | `PO_HEADERS_INTERFACE`, `PO_LINES_INTERFACE` |
| Import Sales Orders          | `OE_HEADERS_IFACE_ALL`, `OE_LINES_IFACE_ALL` |
| Import Receipts              | `RCV_TRANSACTIONS_INTERFACE`                 |
| Import Inventory Adjustments | `MTL_TRANSACTIONS_INTERFACE`                 |
| WMS Task Updates             | `WMS_TASKS_INTERFACE`                        |

> Interface tables are **developer-friendly**: you load data here, run standard programs, and Oracle moves it into the base tables automatically.

---

## 🔹 Visual Flow Summary (Simplified)

```
Supplier
   ↓ (PO)
PO_HEADERS_ALL + PO_LINES_ALL
   ↓ (Receive)
RCV_SHIPMENT_HEADERS / RCV_TRANSACTIONS
   ↓ (Inventory Update)
MTL_MATERIAL_TRANSACTIONS → MTL_ONHAND_QUANTITIES_DETAIL
   ↓ (Warehouse Putaway)
WMS_TASKS → WMS_LPN_CONTENTS
   ↓ (Sales Order Picking)
OE_ORDER_HEADERS_ALL / OE_ORDER_LINES_ALL → WMS_TASKS
   ↓ (Ship)
WSH_DELIVERY_DETAILS → MTL_MATERIAL_TRANSACTIONS
   ↓ (Invoice)
RA_CUSTOMER_TRX_ALL → AR
```

> Each arrow is a **data movement** handled by Oracle programs or workflows.


