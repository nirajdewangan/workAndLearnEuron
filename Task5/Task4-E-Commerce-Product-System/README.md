# E-Commerce Product System

A beginner-friendly Python OOP project for managing products, stock, prices, and purchases.

## Requirements Covered

- `Product` class
- Product ID, name, price, category, and stock quantity
- `display_product()` method
- `update_stock()` method
- `calculate_total_price(quantity)` method
- Static method `Product.is_valid_price(price)`
- Five different product objects
- Buying products and updating stock

## Additional Features

- Price validation
- Stock validation
- Purchase quantity validation
- Insufficient-stock protection
- `buy_product()` helper that calculates the total and reduces stock

## Project Structure

```text
ecommerce-product-system/
├── product_system.py
├── README.md
├── YOUTUBE_SCRIPT.md
├── sample_output.txt
└── youtube-thumbnail.png
```

## How to Run

Open a terminal in this folder and run:

```bash
python product_system.py
```

On some systems, use:

```bash
python3 product_system.py
```

## Static Method Examples

```python
Product.is_valid_price(500)   # True
Product.is_valid_price(-50)   # False
```

## Author

Niraj Kumar Dewangan
