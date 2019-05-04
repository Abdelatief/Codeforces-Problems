# http://codeforces.com/contest/228/problem/A
shoesList = list(map(int, input().split()))
uniqueShoes = list()

uniqueShoes.append(shoesList[0])

for shoe in shoesList:
    if shoe not in uniqueShoes:
        uniqueShoes.append(shoe)

print(4 - len(uniqueShoes))
