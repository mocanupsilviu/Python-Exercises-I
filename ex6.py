"""
 Exercise 6: Find whether a number is a Perfect number E.g A perfect number is a positive integer that is
 equal to the sum of its positive divisors, excluding the number itself. For instance, 6 has
 divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number.
"""

def test_perfect(n):
    if n <= 0:
        print(n,"Not a valid positive integer.")
        return
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    sum_divisors = sum(divisors)
    if sum_divisors == n:
        return True
    else:
       return False

r_true = test_perfect(6)
r_false = test_perfect(7)

print(r_true, r_false)

