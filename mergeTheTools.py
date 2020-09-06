# def merge_the_tools(string, k):
    # your code goes here

# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)

string = input()
k = int(input())

print(string)
# print(type(string))
print(k)
lenSTR = len(string)
print(f'daxil etdiyim str uzunlugu: {lenSTR}')
newSubLen = len(string) // k
print(newSubLen)
str1 = string
tempStr = string
for h in range(k):
    tempSet = set()
    tempList = []
    for i in range(newSubLen):
        # tempSet.add(tempStr[0])
        if tempStr[0] not in tempList:
            tempList.append(tempStr[0])
        # print(f'tempSet: {tempSet}')
        # print(f'tempList: {tempList}')
        tempStr = tempStr[1:]
        # print(f'silme ile: {tempStr}')
    # print(f'subsetler: {tempSet}')
    # print(f'sublistler: {tempList}')
    # print(f'ic dovr bitenden sonra string: {tempStr}') 
    resultStr = ''
    for st in tempList:
        resultStr+=st
    print(resultStr)
    # print('------------------------')
