# nums = [-1, 0, 1, 2, -1, -4]
nums =[-1,0,1,2,-1,-4]
answ=[]

nums.sort()
print(nums)
for i in range(len(nums)-2):
    if i>0 and nums[i] == nums[i-1]:
        continue
    left = i + 1
    right = len(nums)-1
    while left < right:
        sum_now = nums[i]+nums[left]+nums[right]
        if sum_now < 0:
            left += 1
        elif sum_now > 0:
            right -= 1
        else:
            # print([numi, nums[left], nums[right]])
            answ.append([nums[i], nums[left], nums[right]])
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while right > left and nums[right] == nums[right-1]:
                right -= 1
            left += 1
            right -= 1

print(answ)