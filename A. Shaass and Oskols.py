# http://codeforces.com/contest/294/problem/A
n = int(input())
birdsList = list(map(int, input().split()))
numOfShots = int(input())
shots = []

for i in range(numOfShots):
    shots.append(list(map(int, input().split())))

for i in range(numOfShots):
    x = shots[i][0]
    x -= 1
    y = shots[i][1]
    if n == 1:
        birdsList[0] = 0
        break
    if x == 0:
        birdsList[x + 1] += birdsList[x] - y
    elif x == n - 1:
        birdsList[x - 1] += y - 1
    else:
        birdsList[x + 1] += birdsList[x] - y
        birdsList[x - 1] += y - 1
    birdsList[x] = 0

for wire in birdsList:
    print(wire)
