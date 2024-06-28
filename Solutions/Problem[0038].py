"""
Project Euler Problem 38
"""
def ninedigit(x):
    num = ""
    multiplier = 1
    while len(num) < 9:
        num += str(x*multiplier)
        multiplier += 1
    if len(num) == 9:
        return num
def pandigitalcheck(x):
    for i in range(1,10):
        if str(i) not in x:
            return False
    return True

lst = set(ninedigit(x) for x in range(1, 10000) if ninedigit(x) != None and pandigitalcheck(ninedigit(x)))
print(max(lst)) #932718654
