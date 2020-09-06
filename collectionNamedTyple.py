# Task Link https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

# headers = list(map(str, input().split))
n = int(input())
headers = list(map(str, input().split()))
marksIndex = None

for index in range(len(headers)):
    if headers[index] == 'MARKS':
        marksIndex = index
# print(marksIndex)
allMarks = []

for i in range(n):
    line = list(map(str, input().split()))
    allMarks.append(line[marksIndex])


# print(allMarks)

sumOfMarks = 0

for mark in allMarks:
    sumOfMarks+=int(mark)

result = sumOfMarks / n
print("%.2f" % result)
