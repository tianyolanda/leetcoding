x = 1233321
answ = True
if x <0:
    answ = False

x = str(x)

if len(x) < 2:
    answ = True

for i in range(len(x)//2):
    if x[i] != x[len(x)-i-1]:
        answ = False

print(answ)