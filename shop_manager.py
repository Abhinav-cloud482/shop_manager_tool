import json
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt

INVENTORY_FILE = "inventory.json"
CUSTOMER_FILE = "customers.json"
SALES_FILE = "sales.json"

# -------------------------------
# File Handling
# -------------------------------
def load_file(file):
    if not os.path.exists(file):
        return {}
    with open(file, "r") as f:
        return json.load(f)

def save_file(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# -------------------------------
# Customer Database
# -------------------------------
def add_customer():
    customers = load_file(CUSTOMER_FILE)

    name = input("Customer Name: ")
    phone = input("Phone: ")
    address = input("Address: ")

    customers[name] = {
        "phone": phone,
        "address": address
    }

    save_file(CUSTOMER_FILE, customers)
    print("Customer added!\n")

def view_customers():
    customers = load_file(CUSTOMER_FILE)
    for name, info in customers.items():
        print(f"{name} | {info['phone']} | {info['address']}")
    print()

# -------------------------------
# Inventory
# -------------------------------
def add_item(data):
    name = input("Item name: ")
    qty = int(input("Qty: "))
    price = float(input("Price: "))
    threshold = int(input("Low stock threshold: "))

    data[name] = {"quantity": qty, "price": price, "threshold": threshold}
    save_file(INVENTORY_FILE, data)

def view_inventory(data):
    for name, i in data.items():
        print(f"{name} | Qty:{i['quantity']} | ₹{i['price']}")
    print()

# -------------------------------
# PDF Invoice (Improved Layout)
# -------------------------------
def generate_invoice(customer, bill_items, total, gst, final_total):
    filename = f"invoice_{datetime.now().strftime('%H%M%S')}.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "INVOICE")

    # Customer Details
    c.setFont("Helvetica", 10)
    c.drawString(50, 720, f"Name: {customer['name']}")
    c.drawString(50, 705, f"Phone: {customer['phone']}")
    c.drawString(50, 690, f"Address: {customer['address']}")

    # Table Header
    y = 650
    c.drawString(50, y, "Item")
    c.drawString(200, y, "Qty")
    c.drawString(250, y, "Price")
    c.drawString(320, y, "Total")

    y -= 20

    for item in bill_items:
        c.drawString(50, y, item['name'])
        c.drawString(200, y, str(item['qty']))
        c.drawString(250, y, str(item['price']))
        c.drawString(320, y, str(item['total']))
        y -= 20

    # Totals
    c.drawString(50, y-10, f"Subtotal: {total}")
    c.drawString(50, y-25, f"GST: {gst}")
    c.drawString(50, y-40, f"Final Total: {final_total}")

    c.save()
    print("Invoice generated!\n")

# -------------------------------
# POS Billing System
# -------------------------------
def create_bill():
    inventory = load_file(INVENTORY_FILE)
    customers = load_file(CUSTOMER_FILE)
    sales = load_file(SALES_FILE)

    cust_name = input("Enter customer name: ")

    if cust_name not in customers:
        print("Customer not found. Add first.")
        return

    customer = {
        "name": cust_name,
        "phone": customers[cust_name]["phone"],
        "address": customers[cust_name]["address"]
    }

    bill_items = []
    total = 0

    while True:
        item = input("Scan/Add item (or done): ")
        if item == "done":
            break

        if item not in inventory:
            print("Item not found")
            continue

        qty = int(input("Qty: "))

        if qty > inventory[item]["quantity"]:
            print("Stock not enough")
            continue

        price = inventory[item]["price"]
        item_total = qty * price

        inventory[item]["quantity"] -= qty

        bill_items.append({
            "name": item,
            "qty": qty,
            "price": price,
            "total": item_total
        })

        total += item_total

    gst = total * 0.05
    final_total = total + gst

    print(f"Total: {final_total}")

    # Save sales
    sale_id = str(datetime.now())
    sales[sale_id] = {
        "customer": cust_name,
        "items": bill_items,
        "total": final_total,
        "date": sale_id
    }

    save_file(SALES_FILE, sales)
    save_file(INVENTORY_FILE, inventory)

    generate_invoice(customer, bill_items, total, gst, final_total)

# -------------------------------
# Sales Reports + Charts
# -------------------------------
def sales_report():
    sales = load_file(SALES_FILE)

    dates = []
    totals = []

    for s in sales.values():
        date = s["date"].split(" ")[0]
        dates.append(date)
        totals.append(s["total"])

    print("Total Sales:", sum(totals))

    plt.bar(dates, totals)
    plt.xticks(rotation=45)
    plt.title("Sales Report")
    plt.tight_layout()
    plt.show()

# -------------------------------
# MAIN MENU
# -------------------------------
def main():
    inventory = load_file(INVENTORY_FILE)

    while True:
        print("\n==== POS SYSTEM ====")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Add Customer")
        print("4. View Customers")
        print("5. Create Bill (POS)")
        print("6. Sales Report")
        print("7. Exit")

        ch = input("Choice: ")

        if ch == "1":
            add_item(inventory)
        elif ch == "2":
            view_inventory(inventory)
        elif ch == "3":
            add_customer()
        elif ch == "4":
            view_customers()
        elif ch == "5":
            create_bill()
        elif ch == "6":
            sales_report()
        elif ch == "7":
            break

if __name__ == "__main__":
    main()