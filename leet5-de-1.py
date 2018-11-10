# 查找最大公共字串：暴力法
s = "abcabcmmmawer"
sr = "aaabcmmwwwer"

# sr = s[::-1]
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
        if len(pair) > maxlenth:
            pairmax = pair
            maxlenth = len(pair)

print(pairmax)
# lenthpairall = []
# for n in range(len(pairall)):
#     lenthpairall.append(len(pairall[n]))

# index = lenthpairall.index(max(lenthpairall))
# print(pairall[index])






# print(result)

