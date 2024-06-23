"""
Project Euler Problem 12
"""
def list_factors(x):
    factors = set()
    for i in range(1, round(x**0.5) + 1):
        if x % i == 0:
            factors.add(i)
            factors.add(int(x / i))
    return sorted(factors)

tri_nums = [1]
index = 2
while len(list_factors(tri_nums[-1])) < 500:
    tri_nums.append(tri_nums[-1] + index)
    index += 1
print(tri_nums[-1]) #76576500
