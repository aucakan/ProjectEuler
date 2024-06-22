"""
Project Euler Problem 24
"""
from itertools import permutations as p

lst = sorted(p([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
desired = lst[10**6 - 1]
ans = ""
for i in desired:
    ans += str(i)
print(ans) #2783915460
