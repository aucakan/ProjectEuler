"""
Project Euler Problem 28
"""
from time import time
start = time()

num_of_el = 0
sum = 1 #We add the 1 in the center first
for i in range(3, 1003, 2):
    ur = i**2 #upper right corner    
    num_of_el += 8 #Trivial. For each edge +2 elements.
    delta = int(num_of_el/4) #Difference between corners in each step.
    sum += 4*ur - 6*delta #The corners are: ur, ur - 1*delta, ur - 2*delta, ur - 3*delta
print(sum) #669171001
    
print(time() - start, "seconds")    

#Second Solution
def total(x):
    n = (x - 1)/2
    return int(16*(n**3)/3 + 10*(n**2) + 26*n/3 + 1)
print(total(1001))
#If you wonder where this formula came from, you can email me.
#I derived this in my notebook.