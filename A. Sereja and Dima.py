# http://codeforces.com/contest/381/problem/A
n = input()

cardsList = list(map(int, input().split()))

sereja = 0
dima = 0

for i in range(len(cardsList)):
    if cardsList[0] > cardsList[-1]:
        score = cardsList[0]
    else:
        score = cardsList[-1]

    cardsList.remove(score)

    if i % 2 == 0:
        sereja += score
    else:
        dima += score

print(sereja, dima)