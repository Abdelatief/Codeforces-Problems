# http://codeforces.com/contest/431/problem/A
calories = list(map(int, input().split()))

stripes = list(map(int, input()))

total = 0

for stripe in stripes:
    total += calories[stripe - 1]

print(total)