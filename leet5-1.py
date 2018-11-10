# 查找最长回数：方法一（时间复杂度最高）
# 1. 将自身反转
# 2. 查找自己与反转的最大公共字串：暴力法
# 3. 查找同时要判断【该公共字串的索引是否符合反转前索引】
s = "abcabcmmmawer"
# sr = "aaabcmmwwwer"
sr = s[::-1]
maxlenth = 0
pairall = []
pairmax = ""
for i in range(len(s)):
    for j in range(len(sr)):
        pair = ""
        k = i
        v = j
        while s[k] == sr[v]:
            pair += s[k]
            if k == len(s)-1 or v == len(sr)-1:
                break
            k += 1
            v += 1
        if j == len(s) - len(pair) - i:
            pairall.append(pair)
            if len(pair) > maxlenth:
                pairmax = pair
                maxlenth = len(pair)
print(len(pairmax))
print(pairmax)


