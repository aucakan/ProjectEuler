"""
Project Euler Problem 67
"""

with open("0067_triangle.txt", "r") as t:
    tri = t.read().split("\n")[:-1]
    lst = [[int(j) for j in i.split()] for i in tri]
    for i in range(1, len(lst.copy())):
        for j in range(len(lst[-2])):
            lst[-2][j] += max(lst[-1][j], lst[-1][j + 1])
        lst.pop(-1)
    print(lst)
