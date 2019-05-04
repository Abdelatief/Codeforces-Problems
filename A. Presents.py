# http://codeforces.com/contest/136/problem/A
n = int(input())
inputList = list(map(int, input().split()))
outputList = [0 for i in range(n)]

for item in inputList:
    outputList[item - 1] = inputList.index(item) + 1

for item in outputList:
    print(item, end=' ')
