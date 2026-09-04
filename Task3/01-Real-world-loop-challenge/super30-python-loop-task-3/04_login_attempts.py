# 04_login_attempts.py

correct_password = "python123"

for attempt in range(1, 4):

    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful!")
        break

    print("Incorrect password.")

    remaining = 3 - attempt

    if remaining > 0:
        print("Attempts remaining:", remaining)

else:
    print("Maximum attempts reached. Login blocked.")