def is_palindrome(s):
    s = s.lower().replace(" ", "")
    reversed = s[::-1]

    print(f"{s} == {reversed}")
    return s == reversed


print(is_palindrome("Hemanth"))
