# Task Link https://www.hackerrank.com/challenges/py-collections-deque/problem
from collections import deque

d = deque()

numOfComands = int(input())

for i in range(numOfComands):
    newStr = list(map(str, input().split()))
    if len(newStr) == 1:
        if newStr[0][-1] == 'p':
            d.pop()
        else:
            d.popleft()
    else:
        if len(newStr[0]) == 6:
            d.append(int(newStr[1]))
        else:
            d.appendleft(int(newStr[1]))

# d.reverse()
# print(d)
for i in d:
    print(i, end=" ")

# print(d[0])

# strSum = ''
# for i in d:
#     strSum+=str(i)
#     if i == 0 and d[i] != d[-1]:
#         strSum+=' '
# print(strSum)    