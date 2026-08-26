# String Cleaning Challenge

message = " Welcome To Python Programming Class "

print("Original Message:", message)

# Remove extra spaces from beginning and end
cleaned_message = message.strip()
print("After strip():", cleaned_message)

# Convert to lowercase
lowercase_message = cleaned_message.lower()
print("Lowercase:", lowercase_message)

# Convert to uppercase
uppercase_message = cleaned_message.upper()
print("Uppercase:", uppercase_message)

# Convert to title case
titlecase_message = cleaned_message.title()
print("Title Case:", titlecase_message)

# Replace Python with Advanced Python
replaced_message = cleaned_message.replace("Python", "Advanced Python")
print("After replace():", replaced_message)

# Check whether string starts with Welcome
starts_with_welcome = cleaned_message.startswith("Welcome")
print("Starts with Welcome:", starts_with_welcome)

# Check whether string ends with Class
ends_with_class = cleaned_message.endswith("Class")
print("Ends with Class:", ends_with_class)

# Count occurrences of o
count_o = cleaned_message.count("o")
print("Count of 'o':", count_o)

# Find position of Programming
programming_position = cleaned_message.find("Programming")
print("Position of Programming:", programming_position)

# Split sentence into words
words = cleaned_message.split()
print("Split into words:", words)