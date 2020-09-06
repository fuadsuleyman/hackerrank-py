# task Link https://www.hackerrank.com/challenges/input/problem

firstLine = list(map(int, input().split()))
print(firstLine)
x = firstLine[0]
result = firstLine[1]
expression = input()
evalResult = eval(expression)
if evalResult == result:
    print('True')
else:
    print('False')