"""
Project Euler Problem 6
"""
sum_of_squares = 0
sum_of_numbers = 0
for i in range(1, 101):
    sum_of_squares += i**2
    sum_of_numbers += i
result = sum_of_numbers**2 - sum_of_squares
print(result)
