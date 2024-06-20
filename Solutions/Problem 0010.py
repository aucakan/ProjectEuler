"""
Project Euler Problem 10
"""
def is_prime(x):
    if x <= 1:
        return False
    if x >= 2:
        for i in range(2, round(x**0.5) + 1):
            if x % i == 0:
                return False
        return True                

"1"
primes = [i for i in range(1, 2*10**6) if is_prime(i) == True]
print(sum(primes))

"2"
# s = 0
# for i in range(1, 2*10**6):
#     if is_prime(i):
#         s += i        
# print(s)

"3"
"""
#Most efficient solution
#Limit is not included

def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * limit
    for num in range(2, limit):
        if sieve[num]:
           primes.append(num)
           for i in range(num * num, limit, num):
               sieve[i] = False
    return primes

primes = sieve_of_eratosthenes(2*10**6)
print(sum(primes))
"""