# 最慢的解法

x = 123455
answ = (1, -1)[x < 0] * int(str(abs(x))[::-1])
# (1, -1)[x < 0] 这个现在还没太搞明白，从结果看来是：
# 如果后面的判断项返回true就选择-1，如果false就选择1

if (answ >= - 2 ** 31 and answ <= 2 ** 31 - 1):
    output = answ
else:
    output = 0

print(output)