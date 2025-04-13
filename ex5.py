"""
 Exercise 5: Given a String find whether it is a valid 10-digit phone number. Number should be in format
 xxx-xxx-xxxx E.g 234-456-9999
"""
import re

def valid(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    if not isinstance(phone, str):
        print("Not a valid string!")
        return
    if re.match(pattern, phone):
        return True
    else:
        return False

test_true = "234-456-9999"
test_false = "2341-456-9999"

r_true = valid(test_true)
r_false = valid(test_false)

print(r_true,r_false)
