# ============================================================
# 6. EMPLOYEE SALARY ANALYZER
# ============================================================

def salary_total(salaries):
    """Calculate total payroll."""
    total = 0

    for salary in salaries:
        total += salary

    return total


def salary_highest(salaries):
    """Return highest salary."""
    highest = salaries[0]

    for salary in salaries:
        if salary > highest:
            highest = salary

    return highest


def salary_lowest(salaries):
    """Return lowest salary."""
    lowest = salaries[0]

    for salary in salaries:
        if salary < lowest:
            lowest = salary

    return lowest


def salaries_above_average(salaries, average):
    """Return salaries above average."""
    result = []

    for salary in salaries:
        if salary > average:
            result.append(salary)

    return result


def employee_salary_analyzer():
    """Run Employee Salary Analyzer."""
    salaries = [35000, 50000, 42000, 75000, 60000, 90000]

    total = salary_total(salaries)
    average = total / len(salaries)
    highest = salary_highest(salaries)
    lowest = salary_lowest(salaries)
    above_average = salaries_above_average(salaries, average)

    print("\n--- EMPLOYEE SALARY ANALYZER ---")
    print("Salaries:", salaries)
    print("Total Payroll:", total)
    print("Average Salary:", average)
    print("Highest Salary:", highest)
    print("Lowest Salary:", lowest)
    print("Above Average Salaries:", above_average)

employee_salary_analyzer()
