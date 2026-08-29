# Nested Dictionary Challenge

employee = {
    "name": "Amit",
    "department": "Engineering",
    "skills": {
        "language": "Python",
        "database": "PostgreSQL",
        "cloud": "AWS"
    },
    "salary": 80000
}

# Print employee name
print("Employee Name:", employee["name"])

# Print department
print("Department:", employee["department"])

# Print complete skills dictionary
print("Complete Skills:", employee["skills"])

# Print programming language
print("Programming Language:", employee["skills"]["language"])

# Print database
print("Database:", employee["skills"]["database"])

# Print cloud technology
print("Cloud Technology:", employee["skills"]["cloud"])

# Change Python to Python + JavaScript
employee["skills"]["language"] = "Python + JavaScript"
print("Updated Language:", employee["skills"]["language"])

# Change salary
employee["salary"] = 95000
print("Updated Salary:", employee["salary"])

# Add experience
employee["experience"] = 3
print("Experience:", employee["experience"])

# Add another skill under the skills dictionary
employee["skills"]["framework"] = "Django"
print("Updated Skills:", employee["skills"])

# Print updated employee dictionary
print("Updated Employee:", employee)


# Nested Dictionary Explanation
print("\nNested Dictionary Explanation:")

print('employee["name"] accesses a value from the main dictionary.')
print('employee["skills"] accesses the complete nested skills dictionary.')
print('employee["skills"]["language"] accesses language inside skills.')
print('employee["skills"]["database"] accesses database inside skills.')
print('employee["skills"]["cloud"] accesses cloud inside skills.')