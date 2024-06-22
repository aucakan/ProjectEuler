"""
Project Euler Problem 22
"""
def worth(x:str):
    w = 0
    alph = ["","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in x:
        w += alph.index(i)
    return w

with open("0022_names.txt", "r") as n:
    name = n.read().replace('"', "")
    names = sorted(name.split(","))
    lst = [worth(i)*(names.index(i) + 1) for i in names]
    print(sum(lst)) #871198282
         