import re

calculation = input()
s = re.findall(r'\d+', calculation)
if int(s[0]) + int(s[1]) == int(s[2]):
    print("YES")
else:
    print("NO")
