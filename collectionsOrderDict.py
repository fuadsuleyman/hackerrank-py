from collections import OrderedDict

# ordinary_dict = {}
# ordinary_dict['a ve b'] = 1 
# ordinary_dict['b'] = 2 
# ordinary_dict['c'] = 3 
# ordinary_dict['d'] = 4 
# ordinary_dict['e'] = 5 
# ordinary_dict['f'] = 6

# print(ordinary_dict)

# ordinary_dictionary = OrderedDict()
# ordinary_dictionary['a'] = 1 
# ordinary_dictionary['b'] = 2 
# ordinary_dictionary['c'] = 3 
# ordinary_dictionary['d'] = 4 
# ordinary_dictionary['e'] = 5 
# ordinary_dictionary['f'] = 6

# print(ordinary_dictionary)
# print(ordinary_dictionary([0]))
numOfItems = int(input())

ordinary_dictionary = OrderedDict()

for i in range(numOfItems):
    newStr = list(map(str, input().split()))
    intValue = int(newStr[-1])
    del newStr[-1]
    strKey = ''
    for i in range(len(newStr)):
        strKey+=newStr[i]
        if i == 0 and newStr[i] != newStr[-1]:
            strKey+=' '
    if strKey not in ordinary_dictionary:
        ordinary_dictionary[strKey] = intValue
    else:
        ordinary_dictionary[strKey]+=intValue

for key, value in ordinary_dictionary.items():
    print(f'{key} {value}')

# print(ordinary_dictionary)



# print(newStr)

# intValue = int(newStr[-1])
# print(f'intValue: {intValue}')
# del newStr[-1]

# strKey = ''
# for i in range(len(newStr)):
#     strKey+=newStr[i]
#     if i == 0:
#         strKey+=' '
# print(newStr)
# print(f'strKey: {strKey}')



# if key not in d:
#     d[key] = value

# if strKey not in ordinary_dictionary:
#     ordinary_dictionary[strKey] = intValue
# else:
#     ordinary_dictionary[strKey]+=intValue
