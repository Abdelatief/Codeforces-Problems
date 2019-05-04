# http://codeforces.com/contest/158/problem/A
n, k = map(int, input().split())

scoreList = list(map(int, input().split()))

score = scoreList[k - 1]
counter = 0
for num in scoreList:
    if num >= score and num > 0:
        counter += 1

print(counter)