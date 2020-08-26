numStr = input('Enter any number: ')

# find number of digits in array
leng = len(numStr)

totalSymmetry = 0

if leng % 2 > 0:
    totalSymmetry+=1

# get fist part of number(str)
firsPart = numStr[:leng//2]

# get fist part of number(str), below if for odd and even count of digits
if leng % 2 > 0:
    secondPart = numStr[leng//2+1:]
else:    
    secondPart = numStr[leng//2:]

# reverse second part string
secondPartReversed = secondPart[::-1]

# get half String len
halfLen = len(firsPart)

# finally count summetry numbers
for i in range(0, halfLen):
    if firsPart[i] == secondPartReversed[i]:
        totalSymmetry+=1

print(f'it is our result: {totalSymmetry}')



