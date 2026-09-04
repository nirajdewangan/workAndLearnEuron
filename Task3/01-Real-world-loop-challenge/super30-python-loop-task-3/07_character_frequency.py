# 07_character_frequency.py

text = input("Enter a string: ")

frequency = {}

for character in text:

    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

print("Character Frequency:")

for character, count in frequency.items():
    print(character, "->", count)