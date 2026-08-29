# Student Profile Using Dictionary

student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python",
    "city": "Bangalore",
    "marks": 88
}

# Print the complete dictionary
print("Complete Dictionary:", student)

# Print student's name
print("Student Name:", student["name"])

# Print student's course
print("Course:", student["course"])

# Print all keys
print("All Keys:", student.keys())

# Print all values
print("All Values:", student.values())

# Print all key-value pairs
print("All Items:", student.items())

# Change marks from 88 to 92
student["marks"] = 92
print("Updated Marks:", student["marks"])

# Add email
student["email"] = "rahul@example.com"
print("Email:", student["email"])

# Add phone
student["phone"] = "9876543210"
print("Phone:", student["phone"])

# Remove city
removed_city = student.pop("city")
print("Removed City:", removed_city)

# Use get() to retrieve name
student_name = student.get("name")
print("Name Using get():", student_name)

# Demonstrate update()
student.update({"course": "Advanced Python"})
print("After update():", student)

# Create a copy of the dictionary
student_copy = student.copy()
print("Student Copy:", student_copy)

# Print final dictionary
print("Final Student Dictionary:", student)


# Dictionary Method Explanations
print("\nDictionary Method Explanations:")

print("keys(): Returns all keys from the dictionary.")
print("values(): Returns all values from the dictionary.")
print("items(): Returns all key-value pairs from the dictionary.")
print("get(): Returns the value of a specified key.")
print("update(): Updates existing values or adds new key-value pairs.")
print("pop(): Removes a specified key and returns its value.")
print("copy(): Creates a shallow copy of the dictionary.")