# Task Link https://www.hackerrank.com/challenges/zipped/problem

firstLine = list(map(int,input().split()))
# print(firstLine)

loopCount = firstLine[1]
# print(f'loopCount: {loopCount}')

sumList = []
for i in range(loopCount):
    nextList = list(map(float,input().split()))
    sumList+=[nextList]

# print(sumList)
result1 = list(zip(*sumList))
# print(result1)

lastResult = []
for i in result1:
    # print(i)
    sum = 0
    for k in i:
        sum+=k
    print(sum/loopCount)


# for i in sumList:
#     print(i)