# http://codeforces.com/contest/268/problem/A`
gamesNum = int(input())
inputList = list()
gamesList = list()
for game in range(gamesNum):
    inputList = list(map(int, input().split()))
    gamesList.append(inputList)

counter = 0
for j in range(gamesNum - 1):
    for k in range(j + 1, gamesNum):
        if gamesList[j][0] == gamesList[k][1]:
            counter += 1
        if gamesList[j][1] == gamesList[k][0]:
            counter += 1

print(counter)