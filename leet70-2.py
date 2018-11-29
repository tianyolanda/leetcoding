class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] + [1] + [2] + [0] * (n - 2)
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]



so = Solution()
print(so.climbStairs(7))
