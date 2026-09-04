# Python for Loop Fundamentals

## Objective

The objective of this task is to build strong fundamentals in Python iteration using:

- `for` loops
- `range()`
- Strings
- Lists
- Dictionaries
- Conditional statements
- User input
- Loop-based calculations

This assignment contains 12 programs demonstrating different practical uses of Python `for` loops.

---

## Question 1: Print Numbers from 1 to 100

### Task

Print all numbers from 1 to 100 using a `for` loop.

### Approach

I used `range(1, 101)` with a `for` loop.

The ending value of `range()` is excluded, so `101` is used to include `100`.

### Example Output

1 2 3 4 5 ... 98 99 100

---

## Question 2: Print Even Numbers from 1 to 100

### Task

Print all even numbers between 1 and 100.

### Approach

I looped through numbers from 1 to 100 and used the modulo operator `%`.

If:

`number % 2 == 0`

the number is even.

### Example Output

2 4 6 8 10 ... 96 98 100

---

## Question 3: Print Odd Numbers from 1 to 100

### Task

Print all odd numbers between 1 and 100.

### Approach

I used a `for` loop and checked:

`number % 2 != 0`

If the remainder after division by 2 is not zero, the number is odd.

### Example Output

1 3 5 7 9 ... 95 97 99

---

## Question 4: Multiplication Table

### Task

Take an integer from the user and print its multiplication table from 1 to 20.

### Approach

I accept an integer using `input()` and convert it using `int()`.

Then I use:

`range(1, 21)`

to multiply the entered number from 1 through 20.

### Sample Input

5

### Sample Output

5 x 1 = 5  
5 x 2 = 10  
5 x 3 = 15  
...  
5 x 20 = 100

---

## Question 5: Calculate Sum from 1 to n

### Task

Calculate the sum of numbers from 1 to a user-provided number without using `sum()`.

### Approach

I created a variable called `total` with an initial value of 0.

The loop goes from 1 to `n` and adds each number to `total`.

This variable works as an accumulator.

### Sample Input

10

### Sample Output

Sum from 1 to 10 is: 55

---

## Question 6: Calculate Factorial

### Task

Calculate the factorial of a number without using any built-in factorial function.

### Approach

I initialized:

`factorial = 1`

Then I used a `for` loop to multiply the factorial value by every number from 1 to the entered number.

For example:

`5! = 1 × 2 × 3 × 4 × 5`

### Sample Input

5

### Sample Output

Factorial of 5 is: 120

The program also checks for negative numbers because factorial is not defined for negative integers.

---

## Question 7: Numbers Divisible by 3

### Given

`numbers = [12, 7, 9, 20, 33, 42, 8, 15]`

### Task

Print only numbers divisible by 3.

### Approach

I iterate through the list using a `for` loop.

For every number, I check:

`number % 3 == 0`

If the condition is true, the number is printed.

### Output

12  
9  
33  
42  
15

---

## Question 8: Languages and Their Lengths

### Given

`languages = ["Python", "Java", "C++", "JavaScript", "Go"]`

### Task

Print every programming language along with its length.

### Approach

I iterate through the list using a `for` loop.

For every language, I use `len()` to calculate the number of characters.

### Output

Python - 6  
Java - 4  
C++ - 3  
JavaScript - 10  
Go - 2

---

## Question 9: Iterate Through a Dictionary

### Given

student information containing:

- Name
- Age
- Course
- City

### Task

Print every dictionary key and value.

### Approach

I use:

`student.items()`

This provides both the key and its corresponding value during each iteration.

### Output

name : Rahul  
age : 22  
course : Data Science  
city : Bangalore

---

## Question 10: Count Vowels

### Task

Count the number of vowels in a user-provided string.

### Approach

I initialize:

`vowel_count = 0`

Then I iterate through every character in the string.

The string is converted to lowercase so uppercase and lowercase vowels can be handled using the same condition.

For each character, I check whether it exists in:

`aeiou`

If it does, the counter is increased.

### Sample Input

Python Programming

### Sample Output

Number of vowels: 4

---

## Question 11: Reverse a String Using a For Loop

### Task

Reverse a user-provided string without using `[::-1]` or `reversed()`.

### Approach

I start with an empty string:

`reversed_text = ""`

Then I iterate through every character.

Each new character is placed before the existing reversed string:

`reversed_text = character + reversed_text`

This gradually builds the reversed string.

### Sample Input

Python

### Sample Output

Original String: Python  
Reversed String: nohtyP

---

## Question 12: Find the Largest Number Without max()

### Task

Find the largest number in a list without using the built-in `max()` function.

### Approach

I initially assume that the first element is the largest:

`largest = numbers[0]`

Then I iterate through the list.

If the current number is greater than `largest`, I update the `largest` variable.

### Example List

`[12, 45, 7, 89, 34, 67, 23]`

### Output

Largest Number: 89

---

# Concepts Practiced

Through this assignment, I practiced:

- Python `for` loops
- `range()`
- List iteration
- String iteration
- Dictionary iteration
- `items()`
- Conditional statements
- Modulo operator `%`
- User input
- `int()` conversion
- `len()`
- Accumulator variables
- Factorial calculation
- String manipulation
- Finding values without shortcut functions

---

# Key Learning

A `for` loop allows us to process elements of a sequence one by one.

`range()` is useful when a program needs to repeat an operation a specific number of times.

Loops can also be combined with conditions to solve problems such as:

- Finding even and odd numbers
- Checking divisibility
- Calculating totals
- Calculating factorials
- Processing strings
- Iterating through lists
- Iterating through dictionaries
- Finding the largest value

---

# Repository

Repository Name:

`super30-python-loop-task`

The repository contains the Python source code and this README file explaining the approach used for each question.

---

# Author

Niraj Kumar Dewangan

# Course

Super30 Python - Work & Learn