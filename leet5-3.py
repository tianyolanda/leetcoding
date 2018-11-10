# 查找最长回数：方法三（时间复杂度 O(n*n))
# 遍历字符串,以每个字符为中心,左右扩散看是否相等,注意奇偶情况!

# 本方法同时处理奇数和偶数的回文串:
# 首先判断该数字右边有没有重复数字,有的话,右指针就一直右移,直到重复数字结束/或到边界停止,[此时将整体指针也右移,在最外层循环跳过中间这些重复的数字不再进行查找了]
# 检查完所有重复数字了,就开始进行左/右相等判断,到边界停止


s = "lkklweedjjjdemm"
s = "cbbd"
# s = "a"
# s = "ac"

maxLen = 0
i = 0
start = 0
if len(s) < 2:
    maxLen =1
    start = 0

while i < len(s):
    size = min(i,len(s)-i)

    if size < maxLen/2:
        i += 1
    else:
        left = i
        right = i
        while right < len(s) -1 and s[right] == s[right+1]: # 如果[当前数]右侧出现[重复的数]
            right += 1  # 则right指针一直右移, 直到重复数结束

        i = right + 1 # 整体指针也直接右移

        while left>0 and right<len(s)-1 and s[left-1]==s[right+1]:
            left -= 1
            right += 1

        if maxLen < right-left+1:
            maxLen = right - left + 1
            start = left


print(s[start:start+maxLen])

