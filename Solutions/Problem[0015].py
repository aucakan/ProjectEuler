"""
Project Euler Problem 15
"""

def counter(x: tuple, memory = {}):
    if x in memory:
        return memory[x]
    a, b = x
    if a == 1 and b == 1:
        return 2
    if a == 0 or b == 0:
        return 1
    if a >= 1 and b >= 1:
        m = (a-1, b)
        n = (a, b-1)
        memory[x] = counter(m, memory) + counter(n, memory)
        return memory[x]
print(counter((20, 20)))

