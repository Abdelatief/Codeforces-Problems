# http://codeforces.com/contest/799/problem/A

neededCakes, bakingTime, cakesRound, ovenBuildTime = map(int, input().split())

totalTime1 = 0
readyCakes = 0
while readyCakes < neededCakes:
    totalTime1 += bakingTime
    readyCakes += cakesRound

totalTime2 = 0
readyCakes = 0
i = 0
j = 0
while readyCakes < neededCakes:
    cycle1 = (i % bakingTime) + 1
    if cycle1 == bakingTime:
        readyCakes += cakesRound
    if i >= ovenBuildTime:
        cycle2 = (j % bakingTime) + 1
        if cycle2 == bakingTime:
            readyCakes += cakesRound
        j += 1
    i += 1

totalTime2 = i

if totalTime2 < totalTime1:
    print('YES')
else:
    print('NO')
