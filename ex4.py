"""
 Exercise 4: Remove the duplicate characters from the String and print it
 Sample Output:
 The given string is: resources After removing duplicates characters the new string is: resouc
"""

def remove(s):
    print(s)
    if not isinstance(s, str):
        print("Not a valid string!")
        return
    new_string = ""
    for c in s:
        if c not in new_string:
            new_string = new_string + c

    return new_string

r = remove("resources")
print(r,"is True?",r=="resouc")
