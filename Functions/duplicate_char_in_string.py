def duplicate_char_in_string(string):
    result = ""
    for char in string:
        if char not in result:
            result += char.lower().strip()
    return result


print(duplicate_char_in_string("Hemanth Kandalla"))
