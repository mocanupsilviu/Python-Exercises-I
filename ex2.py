"""
Exercise 2: Find the first most frequent character in a given string (edited)
"""

def most_frequent_character(s):
    if not s:
        print("None or empty string!")
        return
    dict = {c: s.count(c) for c in set(s)}
    #print(dict)
    freq = max(dict.values())
    for c in s:
        if dict[c] == freq:
            print("The first most frequent char in the string is:", c)
            return

most_frequent_character("successes")
most_frequent_character(None)
most_frequent_character("")
