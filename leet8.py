str = '91283472332'
str = str.lstrip()
# print(str)

output = ''
answ = 0
flag = 1
for i in range(len(str)):
    if i == 0:
        if ord(str[i]) == 45 and i+1 < len(str) and str[i+1].isdigit():
            flag = -1
            continue
        if ord(str[i]) == 43 and i+1 < len(str) and str[i+1].isdigit():
            continue

    if str[i].isdigit():
        output += str[i]
    else:
        break

if output != '':
    answ = flag * int(output)
if answ >= 2**31-1:
    answ = 2**31-1
if answ <= -2**31:
    answ = -2**31
# answ = int(str)
print(answ)