"""
Project Euler Problem 46
"""
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

def is_square(x):
    sqroot = x**0.5
    if sqroot == int(sqroot):
        return True
    return False
   
primes = [i for i in range(3, 10**6, 2) if is_prime(i)]
 
checker = True
num = 35
while checker:
    if is_prime(num):
        num += 2
        continue
    for prime in primes:
        if prime > num:
            break
        else:
            if is_square((num - prime)/2):
                checker = True
                break
            else:
                checker = False
    num += 2
    
print(num - 2) #5777
