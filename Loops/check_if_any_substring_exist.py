s = "Interview"
substrings = ["view", "inter", "test"]

s_lower = s.lower()  # Convert the string to lowercase for case-insensitive comparison

for sub in substrings:
    if sub.lower() in s_lower:
        print(f"'{sub}' is a substring of '{s}'.")

else:
    print("No substrings found in the string.")
