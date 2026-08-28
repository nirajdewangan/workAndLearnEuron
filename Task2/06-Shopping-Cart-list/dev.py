# Shopping Cart Using a Python List

cart = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]

# Display all products
print("All Products:", cart)

# Access first and last products
print("First Product:", cart[0])
print("Last Product:", cart[-1])

# Add Webcam
cart.append("Webcam")
print("After adding Webcam:", cart)

# Insert USB Hub at index 2
cart.insert(2, "USB Hub")
print("After inserting USB Hub:", cart)

# Remove Mouse
cart.remove("Mouse")
print("After removing Mouse:", cart)

# Remove the last item using pop()
removed_item = cart.pop()
print("Removed Item:", removed_item)
print("After pop():", cart)

# Find the index of Monitor
monitor_index = cart.index("Monitor")
print("Index of Monitor:", monitor_index)

# Count occurrences of Laptop
laptop_count = cart.count("Laptop")
print("Count of Laptop:", laptop_count)

# Create a copy of the cart
cart_copy = cart.copy()
print("Copied Cart:", cart_copy)

# Reverse the cart
cart.reverse()
print("Reversed Cart:", cart)

# Sort products alphabetically
cart.sort()
print("Sorted Cart:", cart)


# List Method Explanations
print("\nList Method Differences:")

print("append(): Adds one item to the end of a list.")
print("extend(): Adds multiple items from another iterable to the end of a list.")
print("insert(): Adds an item at a specific index.")
print("remove(): Removes the first matching value from a list.")
print("pop(): Removes and returns an item, by default the last item.")
print("clear(): Removes all items from the list.")
print("copy(): Creates a shallow copy of the list.")
print("sort(): Sorts the items of the list.")
print("reverse(): Reverses the current order of the list.")