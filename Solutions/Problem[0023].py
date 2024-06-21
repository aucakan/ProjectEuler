"""
Project Euler Problem 23
"""

def sum_factors(x): #Modified version of the function in Problem 12
    lst = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            lst.add(i)
            lst.add(x / i)
    return int(sum(lst) - x)

abun_nums = {i for i in range(1, 28124) if sum_factors(i) > i}

sums = set()
for i in set(range(1, 28124)):
    for j in abun_nums:
        if i - j in abun_nums:       
            sums.add(i)
            break
print(sum(range(1,28124)) - sum(sums))
            
        