# http://codeforces.com/contest/443/problem/A
import re
print(len(set(re.sub(r'{|}|\s|,', '', input()))))
