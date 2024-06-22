"""
Project Euler Problem 27
"""
from time import time
start = time()

def is_prime(x): #This is the most efficient way that I found. It take less time than Miller-Rabin Test, AKS Primality Test, Sieve Eratosthenes Algorithm.
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
    
max_n = 0
best_a = 0
best_b = 0              
for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while is_prime(n**2 + a*n + b):
            n += 1
        if n > max_n:
            max_n = n
            best_a = a
            best_b = b
print(f"n: {max_n}, a: {best_a}, b: {best_b}, product: {best_a*best_b}") #n: 71, a: -61, b: 971, product: -59231
print(time() - start, "seconds")
