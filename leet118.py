class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        ans = [[1], [1, 1]]

        for i in range(2, numRows):
            ans_i = []
            ans_i.append(1)
            for j in range(1, i):
                new = ans[i - 1][j - 1] + ans[i - 1][j]
                ans_i.append(new)
            ans.append(ans_i)
            ans_i.append(1)
        return ans