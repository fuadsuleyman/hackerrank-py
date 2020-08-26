# Üçrəqəmli tam ədəd verilib.
# Bu ədədin rəqəmlərini sağdan sola oxuduqda alınan ədədi çıxışa verin.

num = input("Enter 3 digits number: ")
newNum = ''

newNum = num[::-1]

lastNum = ''

if newNum[0] == '0':
    lastNum = newNum[1:]
else:
     lastNum = newNum

print(lastNum)

