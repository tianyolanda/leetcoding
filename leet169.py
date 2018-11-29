class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        n = 0
        m = nums[0]
        l = len(nums)-1
        for i in nums:
            if i != m:
                n -= 1
                if n == 0: 
                    m = i
            if i == m:
                n += 1
            if n >= l:
                return m   
        return m 