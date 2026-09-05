# ============================================================
# 7. SHOPPING CART
# ============================================================

def cart_add(cart):
    """Add a product to shopping cart."""
    name = input("Enter product name: ")
    price = float(input("Enter product price: ₹"))

    cart.append({
        "name": name,
        "price": price
    })

    print("Product added.")


def cart_remove(cart):
    """Remove a product from shopping cart."""
    name = input("Enter product name to remove: ")

    for product in cart:
        if product["name"].lower() == name.lower():
            cart.remove(product)
            print("Product removed.")
            return

    print("Product not found.")


def cart_view(cart):
    """Display shopping cart."""
    if len(cart) == 0:
        print("Cart is empty.")
        return

    print("\nShopping Cart:")

    for product in cart:
        print(product["name"], "- ₹", product["price"])


def calculate_cart_bill(cart):
    """Calculate total cart bill."""
    total = 0

    for product in cart:
        total += product["price"]

    return total


def shopping_cart():
    """Run shopping cart application."""
    cart = []

    while True:
        print("\n--- SHOPPING CART ---")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Cart")
        print("4. Calculate Bill")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            cart_add(cart)

        elif choice == "2":
            cart_remove(cart)

        elif choice == "3":
            cart_view(cart)

        elif choice == "4":
            print("Total Bill: ₹", calculate_cart_bill(cart))

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


shopping_cart()