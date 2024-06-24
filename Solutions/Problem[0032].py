"""
Project Euler Problem 32
"""
def d(n): #Return 1 and 2-digit factors only. Think about it.
    factors = set()
    for i in range(1, round(n**0.5) + 1):
        if n % i == 0:
            factors.add(str(i))
            factors.add(str(int(n / i)))
    return sorted(set(int(i) for i in factors if len(i) == 2 or len(i) == 1))

def checker(n):
    for i in d(n):
        mmp = f"{i}{int(n/i)}{n}"
        mmp = mmp.replace("0", "") #Written as 1 through 9, it cannot include 0.
        nums = set(j for j in mmp)
        if len(nums) == 9:
            return True
    return False
total = 0
for i in range(1234, 9877):
    if checker(i):
        total += i
print(total)
