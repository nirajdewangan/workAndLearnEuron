# Intermediate Loops & Loop Control

## Objective

Practice Python loops and loop-control concepts including:

- for loop
- break
- continue
- for-else
- range()
- enumerate()
- nested loops

---

## Question 1: Skip Numbers Divisible by 5

Print numbers from 1 to 100 but skip numbers divisible by 5.

### Approach

I used a `for` loop with `range(1, 101)`.

For each number, I checked whether it is divisible by 5 using the modulo operator `%`.

If the number is divisible by 5, `continue` skips the current iteration.

---

## Question 2: Find First Number Divisible by 7 and 11

Iterate from 1 to 100 and stop when the first number divisible by both 7 and 11 is found.

### Approach

I used a `for` loop to check every number.

The condition checks:

`number % 7 == 0 and number % 11 == 0`

When the first matching number is found, `break` stops the loop.

The first matching number is `77`.

---

## Question 3: Search a Number Using For-Else

Search for a user-provided number inside a list.

### Approach

I used a `for` loop to compare the user input with each number in the list.

If the number is found, the program prints `Number Found` and uses `break`.

If the loop completes without finding the number, the `else` block prints `Number Not Found`.

---

## Question 4: Display Names Using enumerate()

Given:

`names = ["Aman", "Ravi", "Sudhanshu", "Priya", "Anjali"]`

### Approach

I used `enumerate()` to get both the position and name while looping through the list.

I used `start=1` so numbering begins from 1 instead of 0.

---

## Question 5: Increasing Star Pattern

Required pattern:

*
**
***
****
*****

### Approach

I used a `for` loop from 1 to 5.

During each iteration, the star character is repeated according to the current row number.

---

## Question 6: Decreasing Star Pattern

Required pattern:

*****
****
***
**
*

### Approach

I used `range(5, 0, -1)`.

The negative step decreases the row value from 5 to 1, producing fewer stars on each line.

---

## Question 7: Multiplication Tables From 1 to 10

Generate multiplication tables from 1 to 10.

### Approach

I used nested loops.

The outer loop selects the table number from 1 to 10.

The inner loop multiplies that number by values from 1 to 10.

---

## Question 8: Numbers Divisible by Both 3 and 5

Find all numbers between 1 and 200 divisible by both 3 and 5.

### Approach

I used a `for` loop from 1 to 200.

For each number, I checked:

`number % 3 == 0 and number % 5 == 0`

Only numbers satisfying both conditions are printed.

---

## Question 9: Remove Duplicates Without set()

Create a new list containing only unique values without using `set()`.

### Approach

I created an empty list called `unique_numbers`.

I looped through the original list and checked whether each number was already present in the new list.

If it was not present, I added it using `append()`.

---

## Question 10: Count Positive, Negative and Zero Numbers

Given:

`numbers = [10, -4, 8, -2, 0, 15, -9, 21]`

### Approach

I created three counters:

- positive
- negative
- zeros

I used a loop with `if`, `elif`, and `else` to classify each number and increase the appropriate counter.

---

## Question 11: Prime Number Check

Determine whether a user-provided number is prime.

### Approach

A prime number is greater than 1 and has only two factors: 1 and itself.

I used a loop to check possible divisors.

If any divisor divides the number exactly, the number is not prime and `break` stops the loop.

If no divisor is found, the number is prime.

---

## Question 12: Prime Numbers Between 1 and 100

Print all prime numbers between 1 and 100.

### Approach

I used nested loops.

The outer loop checks each number from 2 to 100.

The inner loop checks whether the current number has any divisor other than 1 and itself.

If a divisor is found, `break` stops checking that number.

If no divisor is found, the number is printed as prime.

---

## Concepts Practiced

This task helped me practice:

- Python `for` loops
- `range()`
- `break`
- `continue`
- `for-else`
- `enumerate()`
- Nested loops
- Conditional statements
- List operations
- Pattern generation
- Prime-number logic