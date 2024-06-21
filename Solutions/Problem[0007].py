"""
Project Euler Problem 7
"""

def is_prime(x):
    if x <= 1:
        return False
    if x >= 2:
        for i in range(2, round(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

primes = []
x = 2
while len(primes) < 10001:
    if is_prime(x) == True:
        primes.append(x)
    x += 1
print(primes[-1])
