"""
Project Euler Problem 1
"""
"List Comprehension"

p1 = [i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]
print(sum(p1))

"Second Solution"

l = []
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        l.append(i)
print(sum(l))