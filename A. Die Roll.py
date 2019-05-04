# http://codeforces.com/contest/9/problem/A
rolls = list(map(int, input().split()))

maxRoll = max(rolls)

top = (6 - maxRoll) + 1

if top == 1:
    print('1/6')
elif top == 2:
    print('1/3')
elif top == 3:
    print('1/2')
elif top == 4:
    print('2/3')
elif top == 5:
    print('5/6')
elif top == 6:
    print('1/1')
elif top == 0:
    print('0/1')

