"""
Project Euler Problem 37
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
             
def is_truncatable(x):
    xs = str(x)
    for i in range(len(xs)):
        if not is_prime(int(xs[i:])):
            return False
        if not is_prime(int(xs[:len(xs) - i])):
            return False
    return True

truncatables = set()
candidate = 23
while len(truncatables) < 11:
    if str(candidate)[0] in "14689" or str(candidate)[-1] in "19": #It is for optimizing the code.
        candidate += 2
        continue
    if any(i in str(candidate)[1:-1] for i in "024568"): #It is for optimizing the code.
        candidate += 2
        continue
    if is_truncatable(candidate):
        truncatables.add(candidate)
    candidate += 2

print("Answer:", sum(truncatables)) #748317
print(time() - start, "seconds")
