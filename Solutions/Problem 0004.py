"""
Project Euler Problem 4
"""

p4 = []
for i in range(100, 1000):
    for j in range(100, 1000):
        a = str(i*j)
        if a == a[::-1]:
            p4.append(int(a))
print(max(p4))

        
        
