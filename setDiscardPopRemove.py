# Task Link https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
# print(s)

countOfOperations = int(input())
for stamp in range(countOfOperations):
    strList = []
    strList.append(input())
    if strList[0][0] == 'p':
        s.pop()
    elif strList[0][0] == 'd':
        s.discard(int(strList[0][-1]))
    elif strList[0][0] == 'r':
        s.remove(int(strList[0][-1]))
# print(s)

sum = 0
for num in s:
    sum+=num

print(sum)