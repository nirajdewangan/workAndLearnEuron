# 03_student_marks_analysis.py

marks = [78, 92, 45, 67, 88, 53, 99]

above_90 = 0
between_75_89 = 0
between_50_74 = 0
below_50 = 0

for mark in marks:
    if mark >= 90:
        above_90 += 1
    elif mark >= 75:
        between_75_89 += 1
    elif mark >= 50:
        between_50_74 += 1
    else:
        below_50 += 1

print("90+:", above_90)
print("75-89:", between_75_89)
print("50-74:", between_50_74)
print("Below 50:", below_50)