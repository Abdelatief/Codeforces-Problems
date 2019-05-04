# http://codeforces.com/contest/265/problem/A
stones = input()
instructions = input()
index = 0

for i in range(len(instructions)):
    if instructions[i] == stones[index]:
        index += 1

print(index + 1)
