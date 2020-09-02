# Task Link https://www.hackerrank.com/challenges/py-check-subset/problem

numberOftest = int(input())

flag = None

for i in range(numberOftest):
    lenSetA = int(input())
    setA = set(map(int, input().split()))
    lenSetB = int(input())
    setB = set(map(int, input().split()))
    setA.symmetric_difference_update(setB)
    # print(f'lenSetA = {len(setA)}')
    # print(f'lenFerq {lenSetA} - {lenSetB} = {lenSetB - lenSetA}')
    # print(f'setA after {setA}')
    if len(setA) == lenSetB - lenSetA:
        flag = True
        print(flag)
    else:
        flag = False
        print(flag)