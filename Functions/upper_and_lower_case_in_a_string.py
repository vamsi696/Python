def upper_and_lower_case_in_a_string(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        else:
            lower += 1
    return upper, lower


print(upper_and_lower_case_in_a_string("Hello World Python Programming"))
