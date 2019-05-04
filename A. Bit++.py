# http://codeforces.com/contest/282/problem/A
n = int(input())
statements = [input() for x in range(n)]

x = 0
for line in statements:
    if line == 'X++' or line == '++X':
        x += 1
    else:
        x -= 1

print(x)
