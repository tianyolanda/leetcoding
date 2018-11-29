def lala(nums,val):
    nums.sort()
    flag = 0
    i = 0
    while i < len(nums):
        if nums[i] == val:
            del nums[i]
            flag = 1
            continue
        elif flag == 1:
            return len(nums)
        i += 1
    return (len(nums))

nums = [1,4,3,3,3,3]
val = 3

result = lala(nums,val)
print(result)