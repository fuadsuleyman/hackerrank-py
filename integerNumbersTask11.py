# Beşrəqəmli ədəd verilib.
# Bu ədədin rəqəmlərinin kvadratları cəmini tapın.

num = input("Enter 5 digits number: ")
arrNumsStr = []

# create string digits array
for digit in num:
    if digit != '-':
        arrNumsStr.append(digit)

# convert to num array
numArr = []
for num in arrNumsStr:
    numArr.append(int(num))

sumOfExpo = 0

for num in numArr:
    sumOfExpo+= num*num

print(sumOfExpo)