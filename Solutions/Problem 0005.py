"""
Project Euler Problem 5
"""

def gcd(a, b):
    c = min(a, b)
    factors = [i for i in range(1, c + 1) if a % i == 0 and b % i == 0]
    return max(factors)

def lcm(a, b):
    return int(a*b / gcd(a, b))

def lcm_c(lis):
    while len(lis) > 1:
        a = lis.pop(-1)
        b = lis.pop(-1)
        lis.append(lcm(a, b))
    return lis[0]

print(lcm_c(list(range(1, 21))))

"Ömür boyu bekleten çözüm, yani çözüm sayılmaz."
# def control(n):
#     for i in range(1,21):
#         if n % i != 0:
#             return False
#     return True

# x = 2520           
# while control(x) != True:
#     print(x)
#     x += 1
# print(x)
    
