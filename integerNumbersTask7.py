# Üçrəqəmli tam ədəd verilib.
# Onun rəqəmlərinin cəmini və hasilini tapın.

num = input("Enter 3 digits number: ")
arrNumsStr = []

# create string digits array
for digit in num:
    if digit != '-':
        arrNumsStr.append(digit)

arrNumsInt = []

# convert to integer digits array
for dig in arrNumsStr:
    arrNumsInt.append(int(dig))

sum = 0
# find sum of digits
for num in arrNumsInt:
    sum+=num

product = 1
# find product of digits
for num1 in arrNumsInt:
    product *= num1

print(f'{sum} {product}')
