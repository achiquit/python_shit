"""Turn the mortality dataset from txt to csv."""

__author__ = "Andre Chiquito - andre.chiquit.ooo"

# txt = open('C:/Users/Andre/OneDrive - University of North Carolina at Chapel Hill/My Stuff/School/UNC-CH/UNC-CH Stuff/Lab Stuff/Deepest Beliefs Lab/Curtis Puryear/Learning Python/mortality_data/mortality_data.txt', 'w')

# print(txt)

# txt.close()

# with open('C:/Users/Andre/OneDrive - University of North Carolina at Chapel Hill/My Stuff/School/UNC-CH/UNC-CH Stuff/Lab Stuff/Deepest Beliefs Lab/Curtis Puryear/Learning Python/mortality_data/mortality_data.txt') as txt:
#     [print(line) for line in txt.readlines()]

with open('C:/Users/Andre/OneDrive - University of North Carolina at Chapel Hill/My Stuff/School/UNC-CH/UNC-CH Stuff/Lab Stuff/Deepest Beliefs Lab/Curtis Puryear/Learning Python/mortality_data/mortality_data.txt', 'r+') as txt:
    print(txt)
    for line in txt:
        print(line)
        print(txt)
    contents = txt.read()
    print(contents)