# http://codeforces.com/contest/118/problem/A
string = input()

stringList = list(string)
finalStringList = list()
vowels = ['a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'I', 'U', 'y', 'Y']

for char in stringList:
    if char not in vowels:
        finalStringList.extend("." + char)

string = "".join(finalStringList)

print((string.lower()))