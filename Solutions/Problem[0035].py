"""
Project Euler Problem 35
"""
from time import time
start = time()
def is_prime(x):
    if x < 2:
        return False
    if x < 4:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    if x > 4:
        for i in range(5, int(x**0.5) + 1, 6):
            if x % i == 0 or x % (i + 2) == 0:
                return False
        return True

def rotations(x):
    rot = set(int(str(x)[i:] + str(x)[:i]) for i in range(len(str(x))))
    return sorted(rot)
    
circular_primes = {2}
for i in range(3, 10**6, 2):
    if any(l in str(i) for l in "024568"): #If there is a 5 in i, then 5/i for one of the circulations of i.
           continue
    control = True    
    for j in rotations(i):
        if is_prime(j) == False:
            control = False
            break
    if control:
        circular_primes.add(i)

print(len(circular_primes)) #55
print(time()-start, "seconds")