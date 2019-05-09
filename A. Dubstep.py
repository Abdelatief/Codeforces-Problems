from re import sub
string = input()
output = sub(r'WUB', ' ', string)
print(output.strip())
