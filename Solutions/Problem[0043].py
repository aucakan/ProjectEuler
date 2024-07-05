"""
Project Euler Problem 43
"""
from itertools import permutations as P
from time import time

start = time()

def perm(x: list):
    All = list(P(x))
    perms = set()
    for perm in All:
        st = ""
        for el in perm:
            st += str(el)
        perms.add(st)
    return perms

desired = set()
for i in perm([0,1,2,3,4,5,6,7,8,9]):
    if int(i[1:4]) % 2 != 0:
        continue
    if int(i[2:5]) % 3 != 0:
        continue
    if int(i[3:6]) % 5 != 0:
        continue
    if int(i[4:7]) % 7 != 0:
        continue
    if int(i[5:8]) % 11 != 0:
        continue
    if int(i[6:9]) % 13 != 0:
        continue
    if int(i[7:10]) % 17 != 0:
        continue
    desired.add(int(i))
    
print(sum(desired))
print(time() - start, "seconds")
