"""
Project Euler Problem 30
"""
nums = set()
for i in range(1, 6*9**5 + 1): #999999 -> 354294 (maximum value of the sum for 6-digit numbers)
    total = 0
    for j in str(i):
        total += int(j)**5
    if total == i:
        nums.add(i)
print(sum(nums) - 1) #1 is not included
          