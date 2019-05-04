# http://codeforces.com/contest/236/problem/A
username = input()

strSet = set(username)

if len(strSet) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
