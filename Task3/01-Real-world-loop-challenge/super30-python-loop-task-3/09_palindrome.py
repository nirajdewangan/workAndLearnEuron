# 09_palindrome.py

text = input("Enter a string: ")

is_palindrome = True

left = 0
right = len(text) - 1

while left < right:

    if text[left] != text[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

if is_palindrome:
    print(text, "is a palindrome.")
else:
    print(text, "is not a palindrome.")