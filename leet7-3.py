# 最快的解法：转换为字符串，直接倒序输出

x = -12345
if x < 0:
    flag = -1
else:
    flag = 1

x_str = str(abs(x))
x_reverse = int(x_str[::-1])

if x_reverse <= 2**31-1:
    output = flag * x_reverse
else:
    output = 0

print(output)