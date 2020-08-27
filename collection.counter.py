# Task Link https://www.hackerrank.com/challenges/collections-counter/problem

# "Please enter number of shoes: "
numOfShoes = int(input())

# f"Please enter {numOfShoes} sizees by space between: "
sizesStr = input()

# convert to list sizes
listOfSizes = list(map(int, sizesStr.split()))

# "Please enter number of customers: "
numOfCustomers = int(input())

# print(listOfSizes)

sizesFromCustomer = []
pricesFromCustomer = []

# f"Enter {order+1} order size and price by space between: "
for order in range(numOfCustomers):
    orderStr = input()
    temp = list(map(int, orderStr.split()))
    sizesFromCustomer.append(int(temp[0]))
    pricesFromCustomer.append(int(temp[1]))

# print(f"sizes from customer {sizesFromCustomer}")
# print(f"prices from customer {pricesFromCustomer}")

profit = 0

for size in range(len(sizesFromCustomer)):
    if sizesFromCustomer[size] in listOfSizes:
        listOfSizes.remove(sizesFromCustomer[size])
        profit+=pricesFromCustomer[size]

# f'Raghu profit is: {profit}'
print(profit)