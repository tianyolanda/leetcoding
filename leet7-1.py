# 自己的解法。。。pop and push

x = 2**31-1
output = 0
m = 2**31-1
print(m)
n = -2**31
print(n)
flag = 0
remainders = []

if x < 0:
    x = -x
    flag = 1

res = x
q = round(res/10)

while round(res/10) > 0:
    remainder = res%10 # 0,9,8,7,
    remainders.append(remainder)
    res = round(res//10)

if res !=0:
    remainders.append(res%10)

digit = len(remainders)
print(remainders)

for i in range(len(remainders)):
    output += remainders[i] * (10 ** (digit-1))
    digit -= 1

if flag == 1:
    output = -output

if output > 2**31-1 or output < -2**31:
    output = 0

print(output)
