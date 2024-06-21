"""
Project Euler Problem 20
"""

from math import factorial

lst = [int(i) for i in str(factorial(100))]
print(sum(lst))