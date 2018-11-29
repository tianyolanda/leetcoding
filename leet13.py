s = 'LIV'
num = 0
rules = (
(4, 'IV'), (9, 'IX'), (40, 'XL'), (90, 'XC'), (1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'), (400, 'CD'), (900, 'CM'),
(100, 'C'), (500, 'D'), (1000, 'M'))

for index,roman in rules: # 循环每一个rules里的数
    while roman in s:
        num += index
        s = s.replace(roman,'',1) # 1是指替换一次

print(num)