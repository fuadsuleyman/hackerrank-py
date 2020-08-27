# Task Link https://www.hackerrank.com/challenges/py-set-difference-operation/problem

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

differenceSet = englishSet.difference(frenchSet)
leng = len(differenceSet)
# print(unionedSet)
print(leng)