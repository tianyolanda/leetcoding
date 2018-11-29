class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # method 4
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

        # method 3:
        # a = 0
        # for i in nums:
        #     a ^= i
        # return a

        # method 2:
        # return 2*sum(set(nums)) - sum(nums)

        # method 1:
#         nums.sort()
#         for i in range(0,len(nums)-1,2):
#             if nums[i] != nums[i+1]:
#                 return nums[i]
#         return nums[-1]