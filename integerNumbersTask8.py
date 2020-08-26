# Dördrəqəmli tam ədəd verilib.
# Onun bütün rəqəmlərinin fərqli olub-olmadığını müəyyənləşdirin.

num = input("Enter 4 digits number: ")
arrNumsStr = []

# create string digits array
for digit in num:
    if digit != '-':
        arrNumsStr.append(digit)

print(arrNumsStr)

def uniqueList(arr):
    uniqueArr = []
    for i in arr:
        if i not in uniqueArr:
            uniqueArr.append(i)
    return uniqueArr

uniArr = uniqueList(arrNumsStr)
print(uniArr)

if len(uniArr) == len(arrNumsStr):
    print('YES')
else:
    print('NO')
