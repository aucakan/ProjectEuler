"""
Project Euler Problem 3
"""
def is_prime(x):
    if x <= 1:
        return False
    if x >= 2:
        for i in range(2, round(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

def factor(x):
    factors = [i for i in range(1, round(x**0.5) + 1) if x % i == 0 and is_prime(i) == True]
    return factors

print(factor(13195))
print(factor(600851475143))            