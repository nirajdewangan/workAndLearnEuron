# 05_product_filter.py

products = {
    "Laptop": 55000,
    "Phone": 30000,
    "Headphones": 2000,
    "Mouse": 700,
    "Keyboard": 1500
}

print("Products costing more than ₹2,000:")

for product, price in products.items():
    if price > 2000:
        print(product, "-", price)