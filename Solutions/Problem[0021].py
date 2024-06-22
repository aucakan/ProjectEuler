"""
Project Euler Problem 21
"""
def d(n):
    factors = set()
    for i in range(1, round(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(int(n / i))
    return sum(factors) - n

amicable_numbers = set()
for a in range(1, 10000):
    if a == d(d(a)) and d(a) != a:
        amicable_numbers.add(a)
        amicable_numbers.add(d(a))

print(sum(amicable_numbers)) #31626
        