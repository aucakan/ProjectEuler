"""
Project Euler Problem 40
"""
st = ""
num = 0
while len(st) < 10**6 + 1:
    st += str(num)
    num += 1

product = 1
for i in range(7):
    product *= int(st[10**i])
print(product) #210