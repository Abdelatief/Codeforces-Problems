# http://codeforces.com/contest/770/problem/A
passwordLength, distinctSymbols = map(int, input().split())
alphabets = 'abcdefghijklmnopqrstuvwxyz'

characters = alphabets[:distinctSymbols]
password = ''
for i in range(passwordLength):
    password += characters[i % distinctSymbols]
print(password)
