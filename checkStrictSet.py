# Task Link https://www.hackerrank.com/challenges/py-check-strict-superset/problem

setA = set(map(int, input().split()))

numOfOtherSets = int(input())
lenA = len(setA)
lenSum = 0

for i in range(numOfOtherSets):
    otherSet = set(map(int, input().split()))
    lenSum+=len(otherSet)
    setA.symmetric_difference_update(otherSet)
    # print(setA)

# print(f'setAlenA {lenA} - lensum {lenSum}')
if len(setA) == lenA - lenSum and len(setA) > 0:
    print(True)
else:
    print(False)



