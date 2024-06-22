"""
Project Euler Problem 29
"""
seq = set()
for a in range(2,101):
    for b in range(2, 101):
        seq.add(a**b)
        seq.add(b**a)
print(len(seq)) #9183