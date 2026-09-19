"""A small e-commerce Product System using Python OOP."""


class Product:
    """Represent a product in an e-commerce inventory."""

    def __init__(self, product_id, name, price, category, stock_quantity):
        if not self.is_valid_price(price):
            raise ValueError("Price must be greater than zero.")

        if not isinstance(stock_quantity, int) or stock_quantity < 0:
            raise ValueError("Stock quantity must be a non-negative integer.")

        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.category = category
        self.stock_quantity = stock_quantity

    def display_product(self):
        """Display complete product information."""
        print(f"Product ID : {self.product_id}")
        print(f"Name       : {self.name}")
        print(f"Price      : Rs. {self.price:.2f}")
        print(f"Category   : {self.category}")
        print(f"Stock      : {self.stock_quantity}")

    def update_stock(self, new_quantity):
        """Replace the current stock with a valid new quantity."""
        if not isinstance(new_quantity, int) or new_quantity < 0:
            print("Stock update failed: Quantity must be a non-negative integer.")
            return False

        self.stock_quantity = new_quantity
        print(f"Stock updated for {self.name}: {self.stock_quantity} units")
        return True

    def calculate_total_price(self, quantity):
        """Calculate and return the price for a positive quantity."""
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")

        return self.price * quantity

    def buy_product(self, quantity):
        """Buy a product when sufficient stock is available."""
        if not isinstance(quantity, int) or quantity <= 0:
            print("Purchase failed: Quantity must be a positive integer.")
            return None

        if quantity > self.stock_quantity:
            print(
                f"Purchase failed for {self.name}: "
                f"Only {self.stock_quantity} units are available."
            )
            return None

        total_price = self.calculate_total_price(quantity)
        self.update_stock(self.stock_quantity - quantity)
        print(
            f"Purchased {quantity} x {self.name} "
            f"for Rs. {total_price:.2f}"
        )
        return total_price

    @staticmethod
    def is_valid_price(price):
        """Return True when price is numeric and greater than zero."""
        return (
            isinstance(price, (int, float))
            and not isinstance(price, bool)
            and price > 0
        )


def main():
    """Create five products and demonstrate purchases and stock updates."""
    laptop = Product("P101", "Laptop", 55000, "Electronics", 8)
    headphones = Product("P102", "Wireless Headphones", 2500, "Electronics", 25)
    book = Product("P103", "Python Programming Book", 799, "Books", 40)
    shoes = Product("P104", "Running Shoes", 3200, "Fashion", 20)
    smartwatch = Product("P105", "Smart Watch", 6500, "Wearables", 15)

    products = [laptop, headphones, book, shoes, smartwatch]

    print("E-COMMERCE PRODUCT SYSTEM")
    print(f"Total products created: {len(products)}")

    for product in products:
        print("\n--- Product Details ---")
        product.display_product()

    print("\n--- Buying Products ---")
    laptop.buy_product(2)
    book.buy_product(3)

    print("\n--- Manual Stock Update ---")
    headphones.update_stock(30)

    print("\n--- Insufficient Stock Test ---")
    smartwatch.buy_product(20)

    print("\n--- Price Validation ---")
    print(f"Is Rs. 500 a valid price? {Product.is_valid_price(500)}")
    print(f"Is Rs. -50 a valid price? {Product.is_valid_price(-50)}")


if __name__ == "__main__":
    main()
