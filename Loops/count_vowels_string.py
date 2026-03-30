text = "Hello World, welcome to Python programming!"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("The number of vowels in the string is:", count)
