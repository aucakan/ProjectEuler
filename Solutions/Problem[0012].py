"""
Project Euler Problem 12
"""

def list_factors(x):
    lst = []
    xn = round(x**0.5)
    for i in range(1, xn + 1):
        if x % i == 0:
            lst.append(i)
            if x / i not in lst:
                lst.append(int(x / i))
    return sorted(lst)

tri_nums = [1]
index = 2
while len(list_factors(tri_nums[-1])) < 500:
    tri_nums.append(tri_nums[-1] + index)
    index += 1
print(tri_nums[-1])


