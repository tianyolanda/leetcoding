nums = [-1,0,1,1,55]
target = 3
answ = []
if len(nums)<3:
    flag = False
    answ = []
reach = abs((nums[1]+nums[2]+nums[3])-target)

nums.sort()
flag = True # 判断是否还继续
for i in range(len(nums)-2):
    if not flag:
        break
    if i > 0 and nums[i] == nums[i-1]:
        continue
    left = i+1
    right = len(nums) - 1
    while left < right:
        reach_new = nums[i]+nums[left]+nums[right]-target
        if reach_new == 0:
            answ = [nums[i], nums[left], nums[right]]
            flag = False
            break

        if abs(reach_new) < reach:
            reach = reach_new
            answ = [nums[i],nums[left],nums[right]]

        while left < right and nums[left] == nums[left+1]:
            left += 1
        while left < right and nums[right] == nums[right-1]:
            right -= 1

        if reach_new > 0:
            right -= 1
        if reach_new < 0:
            left += 1
print(answ)
