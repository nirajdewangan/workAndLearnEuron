# Python Data Type Laboratory

# Integer variables
age = 36
year = 2026

# Float variables
salary = 80.0
temperature = 36.5

# String variables
name = "Niraj"
city = "Bengaluru"

# Boolean variables
likes_python = True
is_learning = True

# List variables
skills = ["Python", "React", "JavaScript"]
numbers = [10, 20, 30]

# Tuple variables
coordinates = (10, 20)
languages = ("Python", "JavaScript")

# Set variables
unique_numbers = {1, 2, 3, 4}
technologies = {"Python", "React", "AWS"}

# Dictionary variables
profile = {
    "name": "Niraj",
    "city": "Bengaluru"
}

experience = {
    "years": 12,
    "learning": "Python"
}

# Print values and data types
print("Age:", age, type(age))
print("Year:", year, type(year))

print("Salary:", salary, type(salary))
print("Temperature:", temperature, type(temperature))

print("Name:", name, type(name))
print("City:", city, type(city))

print("Likes Python:", likes_python, type(likes_python))
print("Is Learning:", is_learning, type(is_learning))

print("Skills:", skills, type(skills))
print("Numbers:", numbers, type(numbers))

print("Coordinates:", coordinates, type(coordinates))
print("Languages:", languages, type(languages))

print("Unique Numbers:", unique_numbers, type(unique_numbers))
print("Technologies:", technologies, type(technologies))

print("Profile:", profile, type(profile))
print("Experience:", experience, type(experience))


print("\nType Conversion Examples:")

# String to Integer
converted_int = int("100")
print('int("100"):', converted_int, type(converted_int))
print("Explanation: String '100' is converted into integer 100.")

# String to Float
converted_float = float("45.67")
print('float("45.67"):', converted_float, type(converted_float))
print("Explanation: String '45.67' is converted into float 45.67.")

# Integer to String
converted_string = str(500)
print("str(500):", converted_string, type(converted_string))
print("Explanation: Integer 500 is converted into string '500'.")

# Integer to Boolean
converted_bool = bool(1)
print("bool(1):", converted_bool, type(converted_bool))
print("Explanation: Non-zero integer 1 is converted into True.")

# Tuple to List
converted_list = list((1, 2, 3))
print("list((1, 2, 3)):", converted_list, type(converted_list))
print("Explanation: Tuple (1, 2, 3) is converted into a list.")

# List to Tuple
converted_tuple = tuple([1, 2, 3])
print("tuple([1, 2, 3]):", converted_tuple, type(converted_tuple))
print("Explanation: List [1, 2, 3] is converted into a tuple.")

# List to Set
converted_set = set([1, 2, 2, 3])
print("set([1, 2, 2, 3]):", converted_set, type(converted_set))
print("Explanation: List is converted into a set and duplicate value 2 is removed.")