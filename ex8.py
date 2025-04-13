"""
Exercise 8: Create a Python set such that it shows the element from both lists in a pair. The solution
 should take two or more iterables (like list, dict, string), aggregates them in a tuple, and
 returns it.

 Given:
 first_list = [2, 3, 4, 5, 6, 7, 8]
 second_list = [4, 9, 16, 25, 36, 49, 64]

 Expected Output:
 Result is {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)} (edited
"""

def pair_lists(first_list, second_list):
    if len(first_list) != len(second_list):
        print("Lists lengths do not match!")
        return
    result = set()
    for i in range(len(first_list)):
        pair = (first_list[i], second_list[i])
        result.add(pair)
    result = sorted(result, key=lambda x: x[0])
    return result

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result = pair_lists(first_list, second_list)
print(result)
