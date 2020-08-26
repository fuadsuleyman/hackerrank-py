ar_count = int(input("Please enter size of Array: "))
numsStr = input("Please enter numbers of array by space between: ")

arr = list(map(int, numsStr.split()))

def sumArrayNumbers(arr):
    sum = 0
    for num in arr:
        sum = sum + num
    return sum

result = sumArrayNumbers(arr)
print(result)