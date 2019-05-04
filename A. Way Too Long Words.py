# http://codeforces.com/problemset/problem/71/A
n = int(input())
wordList = list()
for i in range(n):
    wordList.append(input())

for word in wordList:
    if len(word) > 10:
        print(word[0] + str(len(word)-2) + word[-1])
    else:
        print(word)