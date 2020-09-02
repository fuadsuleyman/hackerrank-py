# Task Link https://www.hackerrank.com/challenges/py-set-mutations/problem


# base set
n = int(input())
baseSet = set(map(int, input().split()))
# print(baseSet)

numberOfSets = int(input())

for i in range(numberOfSets):
    operators = []
    # operators.append(input())
    temp = list(map(str, input().split()))
    # print(temp)
    secendarySet = set(map(int, input().split()))
    if temp[0][0] == 'i':
        baseSet.intersection_update(secendarySet)
    elif temp[0][0] == 'u':
        baseSet.update(secendarySet)
    elif temp[0][0] == 's':
        baseSet.symmetric_difference_update(secendarySet)
    elif temp[0][0] == 'd':
        baseSet.difference_update(secendarySet)

# print(baseSet)

sum = 0
for num in baseSet:
    sum+=num

print(sum)