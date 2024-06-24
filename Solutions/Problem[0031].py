"""
Project Euler Problem 31
"""
from time import time
#########################################
start = time()
total_ways = 1 #200
for a in range(0, 201):
    for b in range(0, 201 - a, 2):
        for c in range(0, 201-a-b, 5):
            for d in range(0, 201-a-b-c, 10):
                for e in range(0, 201-a-b-c-d, 20):
                    for f in range(0, 201-a-b-c-d-e, 50):
                        for g in range(0, 201-a-b-c-d-e-f, 100):
                            if a + b + c + d + e + f + g == 200:
                                total_ways += 1
print(total_ways, time()-start, "seconds")
#########################################
#Dynamic Programming (Best solution)
start2 = time()
def total_ways(target):
    coins  = {1, 2, 5, 10, 20, 50, 100, 200}
    ways = [0] * (target + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]
    return ways[target]

print(total_ways(200), time()-start2, "seconds")

#########################################
start3 = time()
def tuple_addition(t1, t2):
    a,b,c,d,e,f = t1
    g,h,i,j,k,l = t2
    return (a+g, b+h, c+i, d+j, e+k, f+l)

#def tuple_addition(t1, t2):
#    return tuple(x + y for x, y in zip(t1, t2)) #not efficient
        
s = {(0,0,0,0,0,1)}
for a in range(0, 101):
    for b in range(0, 101 - a, 2):
        for c in range(0, 101-a-b, 5):
            for d in range(0, 101-a-b-c, 10):
                for e in range(0, 101-a-b-c-d, 20):
                    for f in range(0, 101-a-b-c-d-e, 50):
                            if a + b + c + d + e + f == 100:
                                s.add((a,b,c,d,e,f))
setfor200 = set()
for i in s:
    for j in s:
        setfor200.add(tuple_addition(i, j))
print(len(setfor200) + 1, time() - start3, "seconds")
