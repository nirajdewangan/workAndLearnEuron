# Create a Mini E-Commerce Dataset

products = [
    {
        "name": "Laptop",
        "price": 70000,
        "brand": "Dell"
    },
    {
        "name": "Phone",
        "price": 40000,
        "brand": "Samsung"
    },
    {
        "name": "Tablet",
        "price": 30000,
        "brand": "Apple"
    }
]

# Print all products
print("All Products:", products)

# Print first product
print("First Product:", products[0])

# Print second product's price
print("Second Product Price:", products[1]["price"])

# Print third product's brand
print("Third Product Brand:", products[2]["brand"])

# Change first product's price
products[0]["price"] = 75000
print("Updated First Product Price:", products[0]["price"])

# Add rating to the second product
products[1]["rating"] = 4.5
print("Second Product With Rating:", products[1])

# Add another product manually
products.append(
    {
        "name": "Smartwatch",
        "price": 20000,
        "brand": "Noise"
    }
)

# Print final dataset
print("Final Dataset:", products)


# Explanation
print("\nConcept Explanation:")

print("List: Stores multiple product dictionaries.")
print("Dictionary: Stores product details as key-value pairs.")
print("Indexing: Used to select a product from the list.")
print("Keys: Represent fields such as name, price, and brand.")
print("Values: Represent the actual data stored against each key.")