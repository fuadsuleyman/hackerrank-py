numsStr = input("Please enter 3 numbers of by space between: ")

arr = list(map(int, numsStr.split()))

arr.sort()

print(f'Median Number is: {arr[1]}')