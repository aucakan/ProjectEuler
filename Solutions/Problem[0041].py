"""
Project Euler Problem 41
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
        perms.add(int(st))
    return perms

def is_prime(x):
    if x < 2:
        return False
    if x < 4:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    if x > 4:
        for i in range(5, int(x**0.5) + 1, 6):
            if x % i == 0 or x % (i + 2) == 0:
                return False
        return True

primes = set()
for i in range(2, 10):
    our_list = list(range(1, i))
    for j in perm(our_list):
        if is_prime(j):
            primes.add(j)
            
print(max(primes)) #7652413
print(time() - start, "seconds")
    