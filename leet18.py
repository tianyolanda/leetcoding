nums = [1, 0, -1, 0, -2, 2]
target = 0
answ = []
nums.sort()

for i in range(len(nums)-3):
    for j in range(i+1,len(nums)-2):
        l = j+1
        r = len(nums) - 1
        if j > i + 1 and nums[j] == nums[j - 1]:
            continue
        while l<r:
            sum = nums[i]+nums[j]+nums[l]+nums[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                answ_now = [nums[i],nums[j],nums[l],nums[r]]
                answ_now.sort()
                if answ_now not in answ:
                    answ.append(answ_now)
                while l<r and nums[l] == nums[l+1]:
                    l += 1
                while l<r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1

print(answ)

