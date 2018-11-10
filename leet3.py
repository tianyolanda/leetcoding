s = "abcabcbb"
# s = "pwdaadwsws"
m = {}
left = 0
res = ""
reslen = 0

for i in range(len(s)):
    if (s[i] not in m) or (m[s[i]] < left):
        if reslen > i-left+1:
            res = s[left:left + reslen]
        else:
            res = s[left:i+1]
        reslen = max(reslen, i - left + 1)
    else:
        left = m[s[i]]
    m[s[i]] = i+1 #从1开始记录

# res = s[left:left+reslen]

print(reslen)
print(res)
# print(m)




