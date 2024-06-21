"""
Project Euler Problem 14
"""

def is_even(x):
    if x % 2 == 0:
        return True
    return False

def chain(x: list): # x is a 1 element list
    while x[-1] != 1:
        if is_even(x[-1]):
            x.append(int(x[-1] / 2))
        else:
            x.append(int(3*x[-1] + 1))
    return x

print(chain([13]))
lst = [( i, len(chain([i])) ) for i in range(1, 10**6)]
lst.sort(key=lambda x: x[1], reverse= True)
print(lst[0][0]) #837799
  