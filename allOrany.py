# Task Link https://www.hackerrank.com/challenges/any-or-all/problem

n = int(input())
# print(n)
strList = list(map(str, input().split()))
# print(strList)
# flagPolindrom = False
# for i in strList:
#     if i == i[::-1]:
#         flagPolindrom = True
flagPolindrom = any(i == i[::-1] for i in strList)
# print(flagPolindrom)
intList = []
for i in strList:
    intList.append(int(i))
# flagPositive = False
flagPositive = all(i > 0 for i in intList)
# print(flagPositive)
if flagPositive == True and flagPolindrom == True:
    print(True)
else:
    print(False)