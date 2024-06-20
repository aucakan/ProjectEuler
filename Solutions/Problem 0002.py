"""
Project Euler Problem 2
"""

fib = [1, 2]
sum = 0
while fib[-1] < 4*10**6:
    fib.append(fib[-1] + fib[-2])
if fib[-1] >= 4*10**6:
    fib.pop(-1)
for i in fib:
    if i % 2 == 0:
        sum += i
print(sum)

