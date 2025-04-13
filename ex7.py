"""
Exercise 7: Create a list by picking an odd-index items from the first list and even index items from
 the second

 Given two lists, l1 and l2, write a program to create a third list l3 by picking an
 odd-index element from the list l1 and even index elements from the list l2.

 Given:
 l1 = [3, 6, 9, 12, 15, 18, 21]
 l2 = [4, 8, 12, 16, 20, 24, 28]

 Expected Output:

 Element at odd-index positions from list one
 [6, 12, 18]

 Element at even-index positions from list two
 [4, 12, 20, 28]

 Printing Final third list
 [6, 12, 18, 4, 12, 20, 28]
"""

def third_list(l1_, l2_):
    l3_ = []

    for i in range(0, len(l1_)):
        if i%2 != 0:
            l3_.append(l1_[i])

    for i in range(0, len(l2_)):
        if i % 2 == 0:
            l3_.append(l2_[i])

    return l3_

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3 = third_list(l1, l2)

print(l3)
print(l3 ==  [6, 12, 18, 4, 12, 20, 28])