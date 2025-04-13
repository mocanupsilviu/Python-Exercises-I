"""
 Exercise 1: Check if a given string is a palindrome or not.
"""

def is_palindrome(s):
    if not isinstance(s, str):
        print("Not a valid string!")
        return
    return s == s[::-1]

print("is True? ",is_palindrome("madam"))
print("is False ?",is_palindrome("woman"))