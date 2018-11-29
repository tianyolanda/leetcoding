# for i in range(3,-1,-1): # range(起始，结束，步长)
#     print(i)
import os
strs = ["flower", "floo", "flm", "flight", "flowerazzz"]
prefix = ""
if strs =="":
    prefix = ""
max_s = max(strs) # 每一个字母，根据ascii码排序：
# 比如：先同时查看strs每个元素的第一个字母的ascii值：f，大家都相同，分不出谁大谁小，那么开始查看所有人的第二个字母
# 第二个字母都是l也分不出来，
# 第三个字母，o的ascii码最大，i的ascii最小，因此max(strs)="flowerazzz"
# min(strs) = "flight"
# 这样分的好处的，之后的筛选直接选择最大和最小的两个值的共同前缀就好，因为如果他们俩的前缀相同，就代表了所有元素的前缀都相同。如果他俩不同，那就证明也更没法找到其他共同前缀
min_s = min(strs)

# prefix = min_s
for index,char in enumerate(min_s):
    # print(index,char)
    if char != max_s[index]:
        prefix = min_s[:index]
        break

print(max_s)
print(min_s)
print("prefix:",prefix)
