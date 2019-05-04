# http://codeforces.com/contest/746/problem/B
n = input()
code = list(input())
even = len(code) % 2 == 0
word = [code[0]]
code.remove(code[0])

if not even:
    while len(code) != 0:
        char = code[0]
        elements = len(word)
        if elements % 2 == 0:
            word.append(char)
        else:
            word.insert(0, char)
        code.remove(char)
else:
    while len(code) != 0:
        char = code[0]
        elements = len(word)
        if elements % 2 == 0:
            word.insert(0, char)
        else:
            word.append(char)
        code.remove(char)

print("".join(word))
