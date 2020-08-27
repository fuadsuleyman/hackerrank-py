# Task Link https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


heightsSetLen = int(input())
heightsSetStr = input()
heightsSetToList = heightsSetStr.split()
# print(firstSetToList)
heightsSetToListToInt = list(map(int, heightsSetToList))
# print(firstSetToListToInt)
heightsSet = set(heightsSetToListToInt)
sum = 0
for height in heightsSet:
    sum+=height
# print(heightsSet)
# print(sum)
result = sum / len(heightsSet)
print(result)
