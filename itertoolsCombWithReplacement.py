from itertools import combinations_with_replacement

a = list(map(str,input().split()))
# print(a)
# dividedStr = list(map(str, a[0]))
# print(dividedStr)
secondValue = int(a[1])
myList0 = list(combinations_with_replacement(a[0],secondValue))
print(type(a[1]))
lastList = []
for comb in myList0:
    str1 = ''
    tempList=[]
    for co in comb:
        # print(co)
        tempList.append(co)
        if len(tempList) == secondValue:
            tempList.sort()
            for t in tempList:
                str1+=t        
    # if len(lastList) > 0 and str1 != '':
    words = str1.split()
    # print(f'word {words}')
    lastList.append(str1)

# print(lastList)

lastList.sort()

for combi in lastList:
    print(combi)

# print list(combinations_with_replacement('12345',2))

# myList = list(combinations_with_replacement(a,2))

# print(myList)