# http://codeforces.com/contest/709/problem/A
numberOfOranges, maxSize, capacity = map(int, input().split())
orangesList = list(map(int, input().split()))
juice = 0
overflow = 0
for orange in orangesList:
    if orange <= maxSize:
        juice += orange
        if juice > capacity:
            overflow += 1
            juice = 0
print(overflow)
