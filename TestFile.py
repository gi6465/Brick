import random

BrickList = list()
BrickNum = int(input("Number of Bricks : "))
for i in range(BrickNum):
    BrickTempList = list()
    # BrickTempList.append(int(input("Brick Height : ")))
    # BrickTempList.append(int(input("Brick Weight : ")))
    # BrickTempList.append(int(input("Brick Width : ")))

    BrickTempList.append(int(random.randrange(10, 10000)))
    BrickTempList.append(int(random.randrange(10, 10000)))
    BrickTempList.append(int(random.randrange(10, 10000)))

    print("! Brick", str(i+1), "saved successfully.")
    BrickList.append(BrickTempList)

for j in range(0, len(BrickList)-1):
    for i in range(0, len(BrickList)-1-j):
        if BrickList[i][1] < BrickList[i+1][1]:
            temp = BrickList[i]
            BrickList[i] = BrickList[i+1]
            BrickList[i+1] = temp

print(BrickList)
HeightDict = dict()
for i in range(0, len(BrickList)):
    SaveBrickList = list()
    SaveBrickList.append(BrickList[i])
    Height = BrickList[i][0]
    for j in range(0, len(BrickList)-1-i):
        if BrickList[i+j][2] >= BrickList[i+1+j][2]:
            Height += BrickList[i+1+j][0]
            SaveBrickList.append(BrickList[i+1+j])
    HeightDict[Height] = SaveBrickList

HeightList = list(HeightDict.keys())
print(HeightList)
TallHeight = sorted(HeightList, reverse=True)[0]
print(TallHeight)
print(HeightDict)
print('Combination of the tallest tower is '+str(HeightDict[TallHeight])+'. \nThe height is '+str(TallHeight)+'m.\n')
for i in range(len(HeightDict[TallHeight]),0,-1):
    print(HeightDict[TallHeight][i-1])
