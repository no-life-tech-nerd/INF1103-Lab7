import json
from logging import warning
from os import environ, getcwd
from Product import Product
from Inventory import Inventory

errorCount = int(0)

dataFile = f"{str(environ.get('DATA_PATH') or getcwd())}/inventory.json"

def int_input(message: str) -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            warning("\nInput must be an integer, try again!\n")

def load_inventory() -> list[Product]:
    try:
        with open(dataFile, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found, using empty inventory.")
        return []
    l = []
    for p in data:
        try:
            l.append(Product(product_id=int(p["product_id"]), name=str(p["name"]), price=float(p["price"]), stock=int(p["stock"])))
        except ValueError:
            warning(f"\nError while loading data for product ID {p["product_id"]}, check if the types are valid.")
    return l

def save_inventory(i: Inventory) -> None:
    products = []
    try:
        for p in i.get_products():
            products.append({
                "product_id": p.get_product_id(),
                "name": p.get_name(),
                "price": p.get_price(),
                "stock": p.get_stock()
            })
    except:
        warning("\nError while transforming inventory data for JSON save!\n")
    with open(dataFile, 'w') as file:
        json.dump(products, file)

inventory = Inventory(load_inventory())

while True:
    print("\n========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

    option = input("Enter option: ")

    if option == "1":
        inventory.display_all()

    elif option == "2":
        print("Add New Product")
        print("---------------")
        newProdId = int_input("Enter product ID: ")
        newName = input("Enter product name: ")
        try:
            newPrice = round(float(input("Enter product price: ")), 2)
        except ValueError:
            warning("\nInput must be a float of up to 2 decimal places, try again!\n")
        else:
            newStock = int_input("Enter stock quantity: ")
            inventory.add_product(Product(product_id = newProdId, name = newName, price = newPrice, stock = newStock))

    elif option == "3":
        print("Update Stock")
        print("------------")
        prodId = int_input("Enter product ID: ")
        stock = int_input("New Stock Quantity: ")
        inventory.update_product_stock(prodId, stock)

    elif option == "4":
        print("Search Product")
        print("--------------")
        prodId = int_input("Enter product ID: ")
        inventory.search_inventory(prodId)

    elif option == "5":
        print("\nSaving inventory...")
        save_inventory(inventory)

    elif option == "6":
        print("\nSaving inventory before exit...")
        save_inventory(inventory)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please try again.")
