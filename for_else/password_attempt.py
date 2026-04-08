correct_password = "admin123"
attempts = ["test", "hello", "admin123"]

for attempt in attempts:
    if attempt == correct_password:
        print("Password is correct!")
        break
else:
    print("All password attempts failed.")
