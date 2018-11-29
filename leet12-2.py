num = 3999
# MMMCMXCIX

vl = [1000,500,100,50,10,5,1]
sl = ['M','D','C','L','X','V','I']

count = 0
result = ''
res = num
while res > 0:
    newres = res - vl[count]
    if newres >= 0:
        result += sl[count]
        res = newres
    else:
        count += 1

result = result.replace('DCCCC','CM') # 900
result = result.replace('LXXXX','XC') # 90
result = result.replace('VIIII','IX') # 9

result = result.replace('CCCC','CD') # 400
result = result.replace('XXXX','XL') # 40
result = result.replace('IIII','IV') # 4

print(result)