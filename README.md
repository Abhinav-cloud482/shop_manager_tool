# shop_manager_tool
A Python-based Point of Sale (POS) and inventory management system with customer tracking, automated billing, PDF invoice generation, and sales analytics visualization.


# Shop Manager (POS System)

A simple **Command-Line Point of Sale (POS) System** built in Python to manage **inventory, customers, billing, and sales reports** with PDF invoice generation.


## Features

* Inventory Management (Add/View items)
* Customer Management (Add/View customers)
* POS Billing System
* Automatic PDF Invoice Generation
* Sales Reports with Charts
* JSON-based Data Storage (No database required)


## Project Structure

```
├── shop_manager.py      # Main application
├── inventory.json       # Inventory data
├── customers.json       # Customer database
├── sales.json           # Sales records
├── invoice_*.pdf        # Generated invoices
```


## Requirements

Install dependencies before running :-

```bash
pip install reportlab matplotlib
```


## How to Run

```bash
python shop_manager.py
```


## Menu Options

```
==== POS SYSTEM ====
1. Add Item
2. View Inventory
3. Add Customer
4. View Customers
5. Create Bill (POS)
6. Sales Report
7. Exit
```


## Billing Workflow

1. Select **Create Bill (POS)**
2. Enter customer name
3. Add items (type `done` to finish)
4. System will :-

   * Calculate total + GST (5%)
   * Update inventory
   * Save sale data
   * Generate PDF invoice automatically


## Sample Invoice Output

* Includes :-

  * Customer details
  * Item list (Qty, Price, Total)
  * Subtotal
  * GST (5%)
  * Final Total

Generated file :-

```
invoice_<timestamp>.pdf
```

---

## Sales Report

* Displays :-

  * Total sales amount
  * Bar chart of sales by date


## Data Storage

All data is stored locally using JSON files:

### `inventory.json`

```json
{
  "Shampoo": {
    "quantity": 318,
    "price": 185.0,
    "threshold": 15
  }
}
```

### `customers.json`

```json
{
  "Rajeev Sharma": {
    "phone": "+91 9001000001",
    "address": "Bhopal, India"
  }
}
```

### `sales.json`

```json
{
  "timestamp": {
    "customer": "Rajeev Sharma",
    "items": [...],
    "total": 1225.0
  }
}
```


## Key Concepts Used

* File Handling (JSON)
* CLI-based User Interaction
* Basic Inventory Logic
* PDF Generation using `reportlab`
* Data Visualization using `matplotlib`


## Limitations

* No database (uses JSON files)
* No authentication system
* Single-user CLI application
* No error handling for invalid inputs (can be improved)


## Future Improvements

* Add GUI (Tkinter / Web App)
* Multi-user support
* Barcode scanning
* Stock alerts based on threshold
* Advanced analytics dashboard
* Database integration (SQLite/MySQL)


## Author

Developed as a simple POS system project using Python.


## License

This project is open-source and free to use.
