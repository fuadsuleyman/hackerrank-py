# Üçrəqəmli tam ədəd verilib.
# Bu ədədin yüzlüklərinin və onluqlarının yerini dəyişməklə alınan ədədi çıxışa verin.

num = input("Enter 3 digits number: ")
newNum = ''
newNum += num[1]
newNum += num[0]
newNum += num[2]
lastNum = ''
if newNum[0] == '0':
    lastNum = newNum[1:]
else:
     lastNum = newNum 

print(f'new number {lastNum}')