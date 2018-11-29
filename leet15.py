# 超时了。。。时间复杂度太高
# nums = [-1, 0, 1, 2, -1, -4]
nums = [-1,0,1,2,-1,-4]

answ=[]

if len(nums) < 3:
    answ = []
for i,num_1 in enumerate(nums[:-2]):
    a = i + 1
    while a < len(nums)-1:
        b = a + 1
        while b < len(nums):
            if num_1 + nums[a] + nums[b] == 0:
                answ_new = [num_1,nums[a],nums[b]]
                answ_new.sort()
                if answ_new not in answ:
                    answ.append(answ_new)
            b += 1
        a += 1
# answ.sort(reverse=True)
print(answ)