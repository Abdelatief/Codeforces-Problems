# http://codeforces.com/contest/318/problem/A
n, k = map(int, input().split())

if n % 2 == 0:
    if k <= n // 2:
        number = 1 + (k - 1) * 2
    else:
        k -= n // 2
        number = 2 + (k - 1) * 2
    print(number)
else:
    if k <= (n // 2) + 1:
        number = 1 + (k - 1) * 2
    else:
        k -= (n // 2) + 1
        number = 2 + (k - 1) * 2
    print(number)
