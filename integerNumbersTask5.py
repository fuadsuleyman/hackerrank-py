# Üçrəqəmli tam ədəd verilib.
# Onun sağdan birinci rəqəmini pozub ədədin soluna yazdılar. Alınan ədədi çıxışa verin.

num = input("Enter 3 digits number: ")
newNum = ''
newNum = num[2] + num[0:2]

lastNum = ''
if newNum[0] == '0':
    lastNum = newNum[1:]
else:
     lastNum = newNum

print(lastNum)