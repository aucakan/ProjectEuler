"""
Project Euler Problem 33
"""
from fractions import Fraction
lst = set()
for i in range(10,99):
    for j in range(i+1, 100):        
        a = str(i)
        b = str(j)
        c = int(i)/int(j)
        for k in a:
            if k in b and k != "0":
                new_a = a.replace(k, "")
                new_b = b.replace(k, "")
                if new_a != "" and new_b != "" and new_b != "0": 
                    if int(new_a)/int(new_b) == c and int(new_a) < int(new_b):
                        lst.add((i, j))
prod = 1
for i, j in lst:
    prod *= Fraction(i, j)
print(prod) #100
    