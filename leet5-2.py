# # 查找最长回数：方法二（时间复杂度也挺高）
# 和1不一样的是查找最大公共字串：2d数组法
# 同样，在每轮都会判断公共子字符串是否符合原索引

s = "babad"
sr = s[::-1]
maxlenth = 0
pairall = []
pairmax = ""
matrix = [[0 for j in range(len(s)+1)] for i in range(len(s)+1)]

for i in range(len(s)):
    for j in range(len(sr)):
        if s[i] == sr[j]:
            matrix[i+1][j+1] = matrix[i][j] + 1 # 相同则累加
            if j == len(s) + matrix[i+1][j+1] - i -2:
                if matrix[i+1][j+1] > maxlenth:
                    maxlenth = matrix[i+1][j+1]
                    pairmax = s[i+1-maxlenth:i+1]

# print(matrix)
print(pairmax)
# lenthpairall = []
# for n in range(len(pairall)):
#     lenthpairall.append(len(pairall[n]))

# index = lenthpairall.index(max(lenthpairall))
# print(pairall[index])






# print(result)

