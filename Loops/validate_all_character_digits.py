s = "12345a"

for ch in s:
    if not ch.isdigit():
        print(f"Non-digit character found: {ch}")
        break
else:
    print("All characters are digits.")
