# http://codeforces.com/contest/1167/problem/A
input_number = int(input())
phones = []
for i in range(input_number):
    length = int(input())
    phone = [int(char) for char in input()]
    d = {'length': length, 'phone': phone}
    phones.append(dict(d))

for d in phones:
    if d['length'] > 10 and 8 in d['phone'] and 0 <= d['phone'].index(8) <= d['length'] - 11:
        print('YES')
    else:
        print('NO')
