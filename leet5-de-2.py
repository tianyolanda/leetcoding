# 查找最大公共字串：2d数组法
# 思想：建立一个二维数组，保存连续位相同与否的状态

s = "abcabcmmmawer"
sr = "aaabcmmwwwer"

# sr = s[::-1]
maxlenth = 0
pairall = []
pairmax = ""
matrix = [[0 for j in range(len(s)+1)] for i in range(len(s)+1)]

for i in range(len(s)):
    for j in range(len(sr)):
        if s[i] == sr[j]:
            matrix[i+1][j+1] = matrix[i][j] + 1 # 相同则累加
        if matrix[i+1][j+1] > maxlenth:
            maxlenth = matrix[i+1][j+1]
            print(maxlenth)
            pairmax = s[i+1-maxlenth:i+1]

# print(matrix)
print(pairmax)
# lenthpairall = []
# for n in range(len(pairall)):
#     lenthpairall.append(len(pairall[n]))

# index = lenthpairall.index(max(lenthpairall))
# print(pairall[index])






# print(result)

