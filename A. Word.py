# http://codeforces.com/contest/59/problem/A

word = input()
upperCount = 0
lowerCount = 0

for char in word:
    if char.islower():
        lowerCount += 1
    else:
        upperCount += 1

if lowerCount >= upperCount:
    print(word.lower())
else:
    print(word.upper())
