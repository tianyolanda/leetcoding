s = "PAYPALISHIRING"
s = "ABCD"
numRows = 2
snew = ""


flag = 0
if s == "" or len(s) == 1 or len(s) == 2 or numRows == 1:
    snew = s
    flag = 1

blocklength = 2 * (numRows - 1)

if len(s)% blocklength==0:
    blocknums = len(s)// blocklength
else:
    blocknums = (len(s) // blocklength) + 1

residue = len(s) % blocklength

if flag ==0:
    for i in range(numRows): # i是每个block中指针挪动(也是排序矩阵的行)
        left = 0
        right = 0
        for j in range(blocknums): # j是每个block的标号
            left = j* blocklength + i
            right = (j+1)* blocklength - i
            if i == 0: # 第一个数
                snew += s[left]
            elif i == numRows-1: # 最后一个数
                middle = j*blocklength+numRows-1
                if middle <len(s):
                    snew += s[middle]
            else:
                if left < len(s):
                    snew += s[left]
                if right < len(s):
                    snew += s[right]

print(snew)