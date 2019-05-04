# http://codeforces.com/contest/474/problem/A
shift = input()
message = input()

keyboard = 'qwertyuiopasdfghjkl;zxcvbnm,./'
original_message = ''

if shift == 'R':
    for char in message:
        original_message += keyboard[keyboard.index(char) - 1]
else:
    for char in message:
        original_message += keyboard[keyboard.index(char) + 1]

print(original_message)