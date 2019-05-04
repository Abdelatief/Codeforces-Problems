# http://codeforces.com/contest/766/problem/A
a = input()
b = input()

if a == b:
    print(-1)
elif len(a) > len(b):
    print(len(a))
else:
    print(len(b))
