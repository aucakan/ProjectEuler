"""
Project Euler Problem 34
"""
from math import factorial

lst = []
for i in range(3, 2540160):
    a = str(i)
    total = 0
    for j in a:
        total += factorial(int(j))
    if total == i:
        lst.append(i)
print(sum(lst))
        