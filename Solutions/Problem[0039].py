"""
Project Euler Problem 39
"""

def howmany(x):
    count = 0
    for i in range(x//3, x//2): #By the triangle inequality. One side cannot exceed x//2.
        for j in range((x - i)//2, i): #Prevents k to be greater than j. It generally works.
            k = x - i - j
            if k**2 + j**2 == i**2 and k < j and k > 0:
                count += 1
    return count

max_count = 0
best_i = 0
for i in range(1,1000):
    if howmany(i) > max_count:
        max_count = howmany(i)
        best_i = i
print(max_count, best_i) #8 840

