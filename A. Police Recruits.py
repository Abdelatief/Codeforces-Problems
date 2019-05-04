# http://codeforces.com/contest/427/problem/A
n = int(input())
timeList = list(map(int, input().split()))
manpower = 0
crimes = 0
for event in timeList:
    if event > 0:
        manpower += event
    else:
        if manpower > 0:
            manpower -= 1
        else:
            crimes += 1
print(crimes)
