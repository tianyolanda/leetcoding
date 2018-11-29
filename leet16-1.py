class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lala = []
        answ = float("inf")
        nums.sort()
        n = len(nums)
        flag = True  # 判断是否还继续
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                answ_new = nums[i] + nums[left] + nums[right]-target
                if answ_new == 0:
                    answ = answ_new
                    lala = [nums[i], nums[left], nums[right]]
                    return answ,lala

                if abs(answ_new) < abs(answ):
                    answ = answ_new
                    lala = [nums[i],nums[left],nums[right],i,left,right]
                    # while left+1 < right and nums[left] == nums[left + 1]:
                    #     left += 1
                    # while left < right-1 and nums[right] == nums[right - 1]:
                    #     right -= 1

                if answ_new > 0:
                    right -= 1
                if answ_new < 0:
                    left += 1
        return answ+target,lala

so = Solution()
result,lalala = so.threeSumClosest([0,1,2],3)
print(result)
print(lalala)