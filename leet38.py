class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return '1'
        se = '1'
        i = 1
        while i < n: #i只是编号叠加1，2，3，4，5
            j = 0
            j_past = 0
            n_past = se[0]
            new = ''
            while True:
                if se[j] != n_past:
                    new += str(j-j_past)
                    new += n_past
                    n_past = se[j]
                    j_past = j
                j += 1
                if j == len(se):
                    new += str(j-j_past)
                    new += n_past
                    break
            se = new
            i += 1

        return new
so = Solution()
print(so.countAndSay(1))
