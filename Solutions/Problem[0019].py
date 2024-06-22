"""
Project Euler Problem 19
"""

import datetime

#Solution 1
count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if datetime.date(year, month, 1).weekday() == 6:
            count += 1
print(count)
            
#Solution 2 (For other types of problems)                       
start = datetime.date(1901, 1, 1) 
end = datetime.date(2000, 12, 31)
counter = 0

while start != end:
    start += datetime.timedelta(days = 1)
    if start.weekday() == 6 and start.day == 1:
        counter += 1

print(counter)

