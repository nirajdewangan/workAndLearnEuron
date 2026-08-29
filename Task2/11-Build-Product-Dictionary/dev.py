# Build a Product Dictionary

laptop = {
    "brand": "Dell",
    "model": "XPS 15",
    "price": 120000,
    "ram": "16GB",
    "storage": "512GB SSD",
    "available": True
}

# Display the complete product
print("Laptop:", laptop)

# Print brand
print("Brand:", laptop["brand"])

# Print model
print("Model:", laptop["model"])

# Print price
print("Price:", laptop["price"])

# Change price
laptop["price"] = 135000
print("Updated Price:", laptop["price"])

# Add processor information
laptop["processor"] = "Intel Core i7"
print("Processor:", laptop["processor"])

# Add GPU information
laptop["gpu"] = "NVIDIA RTX 4050"
print("GPU:", laptop["gpu"])

# Change RAM to 32GB
laptop["ram"] = "32GB"
print("Updated RAM:", laptop["ram"])

# Remove available
laptop.pop("available")
print("After Removing Available:", laptop)

# Print all keys
print("All Keys:", laptop.keys())

# Print all values
print("All Values:", laptop.values())

# Print all items
print("All Items:", laptop.items())


# Create a second product dictionary for a mobile phone

mobile = {
    "brand": "Samsung",
    "model": "Galaxy S23",
    "price": 75000,
    "ram": "8GB",
    "storage": "256GB",
    "available": True
}

print("\nMobile Product:", mobile)