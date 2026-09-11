# ============================================================
# 3. INVENTORY MANAGEMENT
# ============================================================
def get_non_negative_float(prompt):
    """Keep asking until the user enters a non-negative number."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Value cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_non_negative_int(prompt):
    """Keep asking until the user enters a non-negative integer."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Value cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def add_inventory_product(products):
    """Add a product to inventory using validated price and quantity."""
    name = input("Enter product name: ").strip()
    price = get_non_negative_float("Enter price: ")
    quantity = get_non_negative_int("Enter quantity: ")
    products[name] = {"price": price, "quantity": quantity}
    print("Product added successfully.")


def display_inventory(products):
    """Display all inventory products."""
    if len(products) == 0:
        print("Inventory is empty.")
        return

    print("\nInventory:")

    for name, details in products.items():
        print(name, "- Price: ₹", details["price"], "- Quantity:", details["quantity"])


def search_inventory_product(products):
    """Search for a product by name."""
    name = input("Enter product name to search: ")

    if name in products:
        print(name, products[name])
    else:
        print("Product not found.")


def update_inventory_quantity(products):
    """Update quantity of an existing product using validation."""
    name = input("Enter product name: ")

    if name not in products:
        print("Product not found.")
        return

    products[name]["quantity"] = get_non_negative_int("Enter new quantity: ")

    print("Quantity updated.")


def calculate_inventory_value(products):
    """Calculate total value of inventory."""
    total = 0

    for details in products.values():
        total += details["price"] * details["quantity"]

    return total


def inventory_management():
    """Run inventory management application."""
    products = {}

    while True:
        print("\n--- INVENTORY MANAGEMENT ---")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Search Product")
        print("4. Update Quantity")
        print("5. Total Inventory Value")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_inventory_product(products)

        elif choice == "2":
            display_inventory(products)

        elif choice == "3":
            search_inventory_product(products)

        elif choice == "4":
            update_inventory_quantity(products)

        elif choice == "5":
            print("Total Inventory Value: ₹", calculate_inventory_value(products))

        elif choice == "6":
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    inventory_management()