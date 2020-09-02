# Task link https://www.hackerrank.com/challenges/py-set-add/problem

countOfStamps = int(input())
stampsList = []
for stamp in range(countOfStamps):
    stampsList.append(input())

# print(stampsList)
newSet = set(stampsList)
# print(newSet)
print(len(newSet))

popi = newSet.pop()
print(newSet)



