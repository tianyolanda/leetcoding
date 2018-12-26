import math


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import math
        l = 0
        r = len(nums) - 1
        last_t_l = -1
        last_t_r = -1
        while r >= l:
            mid = (l + r) >> 1
            if nums[mid] == target:
                t_l = mid - 1
                last_t_l = mid
                while t_l > l:
                    t_lmid = (t_l + l) >>1
                    if nums[t_lmid] == target:
                        last_t_l = t_l
                        t_l = t_lmid
                        continue
                    if nums[t_lmid] < target:
                        l, t_l = t_lmid + 1, last_t_l
                if last_t_l == t_l + 1:
                    if nums[t_l] == target:
                        last_t_l = t_l
                t_r = mid + 1
                last_t_r = mid
                while r > t_r:
                    t_rmid =  math.ceil((r + t_r)/2)
                    # t_rmid = t_r + (r - t_r) // 2
                    if nums[t_rmid] == target:
                        last_t_r = t_r
                        t_r = t_rmid
                        continue
                    if nums[t_rmid] > target:
                        r, t_r = t_rmid - 1, last_t_r
                if last_t_r == t_r - 1 and t_r < len(nums):
                    if nums[t_r] == target:
                        last_t_r = t_r
                break

            if nums[mid] > target:
                r = mid - 1
            if nums[mid] < target:
                l = mid + 1

        if last_t_l == -1 :last_t_l = last_t_r
        if last_t_r == -1 :last_t_r = last_t_l


        return [last_t_l, last_t_r]


so = Solution()
print(so.searchRange([8],
8))
# print(math.ceil(0.88))