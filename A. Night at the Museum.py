# http://codeforces.com/contest/731/problem/A
lettersStr = 'abcdefghijklmnopqrstuvwxyz'
letters = list(lettersStr)  # from 0 to 25
startPointer = 0
endPointer = 25
total = 0
word = input()
pointer1 = 0
pointer2 = 0

for char in word:
    charPointer = letters.index(char)
    counter1 = 0
    counter2 = 0
    while pointer1 != charPointer:
        counter1 += 1
        if pointer1 != 25:
            pointer1 += 1
        else:
            pointer1 = 0

    pointer1 = charPointer

    while pointer2 != charPointer:
        counter2 += 1
        if pointer2 != 0:
            pointer2 -= 1
        else:
            pointer2 = 25

    pointer2 = charPointer

    if counter1 < counter2:
        total += counter1
    else:
        total += counter2
print(total)

