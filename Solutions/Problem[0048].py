"""
Project Euler Problem 48
"""
total = 0
for i in range(1, 1001):
    total += i**i
print(int(str(total)[-10:]))