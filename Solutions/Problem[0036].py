"""
Project Euler Problem 36
"""
def binary(x):
    return bin(x)[2:]

total = 0
for i in range(1, 10**6):
    a = str(i)[::-1]
    b = str(binary(i))[::-1]
    if a == str(i) and b == str(binary(i)):
        total += i
print(total) #872187
