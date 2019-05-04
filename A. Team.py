# http://codeforces.com/contest/231/problem/A
problems = int(input())

contestList = list()
new = list()

for i in range(problems):
    new = list(map(int, input().split()))
    contestList.append(new)

counter = 0

for set in contestList:
    if (set[0] == 1 and set[1] == 1)\
            or \
            (set[1] == 1 and set[2] == 1)\
            or \
            (set[0] == 1 and set[2] == 1)\
            or \
            (set[0] == 1 and set[1] == 1 and set[2] == 1):
        counter += 1

print(counter)