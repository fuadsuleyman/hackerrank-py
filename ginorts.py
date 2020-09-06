# Task Link https://www.hackerrank.com/challenges/ginorts/problem
nLine = list(map(str, input().split()))
# print(nLine)

# for simvol in nLine:
#     if simvol.islower():
#         lowerList.append(simvol)
# print(lowerList)
resLower = [char for char in nLine[0] if char.islower()] 
resLower.sort()
# print(resLower)
resUpper = [char for char in nLine[0] if char.isupper()]
resUpper.sort()
# print(resUpper)
resDigit = [char for char in nLine[0] if char.isdigit()]
resDigit.sort()
# print(resDigit)

oddList = []
evenList = []
for dig in resDigit:
    if int(dig) % 2 == 0:
        evenList.append(dig)
    else:
        oddList.append(dig)
# print(oddList)
# print(evenList)

resultStr = ''
for s in resLower:
    resultStr+=s
for s in resUpper:
    resultStr+=s
for s in oddList:
    resultStr+=s
for s in evenList:
    resultStr+=s

print(resultStr)