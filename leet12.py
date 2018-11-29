num = 3999
result = ''
rules = ((1000,'M'),
         (900,'CM'),
         (500,'D'),
         (400,'CD'),
         (100,'C'),
         (90,'XC'),
         (50,'L'),
         (40,'XL'),
         (10,'X'),
         (9,'IX'),
         (5,'V'),
         (4,'IV'),
         (1,'I'))

for index,s in rules: # 循环每一个rules里的数
    while True: # 每个数可以循环很多次，只要【原数-本轮rules的数字】依然大于0
        newnum = num - index
        if newnum >= 0:
            result += s
            num = newnum
        else:
            break
print(result)