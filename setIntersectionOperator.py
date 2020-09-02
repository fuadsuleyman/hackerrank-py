#Task link https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

englishSetLen = int(input())
englishSetStr = input()
englishSetToList = englishSetStr.split()
# print(firstSetToList)
englishSetToListToInt = list(map(int, englishSetToList))
# print(firstSetToListToInt)
englishSet = set(englishSetToListToInt)
# print(englishSet)

frenchSetLen = int(input())
frenchSetStr = input()
frenchSetToList = frenchSetStr.split()
# print(secondSetToList)
frenchSetToListToInt = list(map(int, frenchSetToList))
# print(secondSetToListToInt)
frenchSet = set(frenchSetToListToInt)
# print(frenchSet)

SameSetEngFre = englishSet.intersection(frenchSet)
lenSame = len(SameSetEngFre)

print(lenSame)