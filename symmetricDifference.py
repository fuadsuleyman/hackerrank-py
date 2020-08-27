# Task Link https://www.hackerrank.com/challenges/symmetric-difference/problem

# her iki set-i musteriden qebul edirik
# her set ucun difference methodunu veririk
# difference methodundan cixanlari ayri ayi setrde capa veririk union-la

# a.difference(b) # Values which exist in a but not in b
# {9, 5}

# a.union(b) # Values which exist in a or b
# {2, 4, 5, 9, 11, 12}

firstSetLen = int(input())
firstSetStr = input()
firstSetToList = firstSetStr.split()
# print(firstSetToList)
firstSetToListToInt = list(map(int, firstSetToList))
# print(firstSetToListToInt)
firtsSet = set(firstSetToListToInt)
# print(firtsSet)

secondSetLen = int(input())
secondSetStr = input()
secondSetToList = secondSetStr.split()
# print(secondSetToList)
secondSetToListToInt = list(map(int, secondSetToList))
# print(secondSetToListToInt)
secondSet = set(secondSetToListToInt)
# print(secondSet)

difFirstSet = firtsSet.difference(secondSet)
difSecondSet = secondSet.difference(firtsSet)
# print(difFirstSet)
# print(difSecondSet)

unionSet = difFirstSet.union(difSecondSet)

convertedToList = list(unionSet)
convertedToList.sort()

for item in convertedToList:
    print(item)
