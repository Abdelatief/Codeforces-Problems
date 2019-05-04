# http://codeforces.com/contest/732/problem/A
k, r = map(int, input().split())

shovels = 1

while ((shovels * k) - r) % 10 != 0 and (shovels * k) % 10 != 0:
    shovels += 1

print(shovels)