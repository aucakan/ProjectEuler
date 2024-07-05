"""
Project Euler Problem 44
"""
import sys

pentagons = [int((3*i**2 - i)/2) for i in range(1, 10000)]
optimum = {int((3*i**2 - i)/2) for i in range(1, 10000)}

for i in range(len(pentagons)):
    for j in range(i + 1, len(pentagons)):
        if pentagons[j] - pentagons[i] in optimum:
            if pentagons[j] + pentagons[i] in optimum:
                print(pentagons[j] - pentagons[i]) #5482660
                sys.exit()
                