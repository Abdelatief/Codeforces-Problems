# http://codeforces.com/contest/520/problem/A
n = input()
string = input()

string_set = set(string.lower())

if len(string_set) == 26:
    print('YES')
else:
    print('NO')
