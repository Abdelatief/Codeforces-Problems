# http://codeforces.com/contest/266/problem/A
n = int(input())

colorsList = list(input())
first = 0
second = 1
counter = 0
while second < len(colorsList) and len(colorsList) > 0:
    if colorsList[first] == colorsList[second]:
        colorsList.remove(colorsList[first])
        counter += 1
    if len(colorsList) > second:
        if colorsList[first] != colorsList[second]:
            first += 1
            second += 1

'''      
while second < len(colorsList) and len(colorsList) > 0:
    if colorsList[first] == colorsList[second]:
        colorsList.remove(colorsList[first])
        counter += 1
    try:
        if colorsList[first] != colorsList[second]:
            first += 1
            second += 1
    except:
        break
'''

print(counter)