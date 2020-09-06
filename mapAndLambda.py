# Task Link https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

n = int(input())
# print(n)

def fib(n):
    # if n == 0:
    #     return [0]
    # elif n == 1:
    #     return [0, 1]
    # else:
    #     lst = fib(n-1)
    #     lst.append(lst[-1] + lst[-2])
    #     return lst
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibList = fib(n)
resultList = []

for i in fibList:
    resultList.append(i**3)

print(*resultList)


# Elegant way
cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))