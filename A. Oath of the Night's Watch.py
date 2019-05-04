# http://codeforces.com/contest/768/problem/A
n = int(input())
stewards = list(map(int, input().split()))

if len(stewards) < 3:
    print(0)
else:
    count = 0
    weakest = min(stewards)
    strongest = max(stewards)
    for man in stewards:
        if weakest < man < strongest:
            count += 1
    print(count)
