# http://codeforces.com/contest/339/problem/A

numList = [int(x) for x in input().split('+')]
numList.sort()
length = len(numList)
for i in range(1, (length * 2) - 1, 2):
    numList.insert(i, '+')
for element in numList:
    print(element, end='')
