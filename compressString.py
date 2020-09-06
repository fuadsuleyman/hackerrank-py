# Task Link https://www.hackerrank.com/challenges/compress-the-string/problem

# chars = "0123456789"
# check_string = "i am checking this string to see how many times each character appears"

# resultList = []
# for char in chars:
#   count = check_string.count(char)
#   if count > 1:
#     print(f'{char}, {count}')
#     resultList.append(f'({char}, {count})')

# print(resultList)
# check_string = input()
# chars = "abcdefghijklmnopqrstuvwxyz"
# check_string = "i am checking this string to see how many times each character appears"

# count = {}
# for s in check_string:
#   if s in count:
#     count[s] += 1
#   else:
#     count[s] = 1
# print(count)
# for key in count:
#   if count[key] > 1:
#     print(f'{key}, {count[key]}')
#     print(count)

#bu valueni duz verir
# sorted_d = sorted(count.items(), key = lambda kv:kv[1], reverse = True)
# sorted_d = sorted(count.items(), key=lambda x: (x[1],x[0]), reverse=True)
# sorted_d = sorted(count.items(), key=lambda t: t[::-1], reverse=True)
# print(sorted_d)

# def reverse_tuple(t):
#     return t[::-1]

# sorted_d = sorted(count.items(), key=reverse_tuple)

# printCount = 0
# for i in sorted_d:
    # printCount+=1
    # if printCount < 3 or printCount == 3:
#    print(f'{i[0]} {i[1]}')

# reverse=True
# d = { "a":4, "c":3, "b":12 }
# d_view = [ (v,k) for k,v in count.items() ]
# print(f'd_view: {d_view}')
# print(d_view[0])
# d_view.sort(reverse=True) 
# for v,k in d_view:
#     print(f'{k}: {v}')

# words = {'fall':4, 'down':4, 'was':3, 'a':3, 'zebra':2, 'bitter':1, 'betty':1}
# sorted_words = [v for v in sorted(count.items(), key=lambda (k, v): (-v, k))]
# sorted_words = sorted(words.iteritems(), key=lambda(k,v): (-v,k))
# print(sorted_words)

# asagidaki kod ishleyir
from collections import Counter
# for letter, counts in sorted(Counter(input()).most_common(),key = lambda x:(-x[1],x[0]))[:3]:
#     print(f'{letter} {counts}')

s = sorted(input())
print(s)
c = Counter(s).most_common(3)
print(c)
print(type(c))
for i,j in c:
    print(i, j)


