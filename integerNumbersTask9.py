# Dördrəqəmli tam ədəd verilib.
# Bu ədədin yazılışında ardıcıl gələn 3 və 7 rəqəmlərinin olub-olmadığını müəyyənləşdirin.

num = input("Enter 4 digits number: ")
arrNumsStr = []

# create string digits array
for digit in num:
    if digit != '-':
        arrNumsStr.append(digit)

print(arrNumsStr)

temp = []
threeNumIndex = None
flag = 0

for i in range(len(arrNumsStr)):
    if len(temp) == 0 and arrNumsStr[i] == '3':
        temp.append(arrNumsStr[i])
        threeNumIndex = i 
    if len(arrNumsStr) > 0 and arrNumsStr[i] == '7' and threeNumIndex+1 == i:
        print('YES')
        flag += 1
if flag == 0:
    print('NO')