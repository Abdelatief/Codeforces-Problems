# http://codeforces.com/contest/567/problem/A
n = int(input())
cities = list(map(int, input().split()))

for i in range(n):
    maxValue = max(abs(cities[i] - cities[0]), abs(cities[i] - cities[-1]))
    if i == 0:
        minValue = abs(cities[i] - cities[i + 1])
    elif i == n - 1:
        minValue = abs(cities[i] - cities[i - 1])
    else:
        minValue = min(abs(cities[i] - cities[i + 1]), abs(cities[i] - cities[i - 1]))
    print(minValue, maxValue)