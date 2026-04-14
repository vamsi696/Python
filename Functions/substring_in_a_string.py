def substring_in_a_string(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.append(string[i:j])
    return substrings


print(substring_in_a_string("abc"))
