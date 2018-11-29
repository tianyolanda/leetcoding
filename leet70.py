class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = []
        def c_r(rest, t_n):
            if rest == 0:
                ans.append(t_n)
                return
            elif rest == 1:
                t_n += '1'
                ans.append(t_n)
                return
            else:
                c_r(rest - 1, t_n + '1')
                c_r(rest - 2, t_n + '2')

        c_r(n, '')
        return len(ans)

so = Solution()
print(so.climbStairs(3))
