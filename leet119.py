class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        ans = [[1], [1, 1]]

        for i in range(2, rowIndex + 1):
            ans_i = []
            ans_i.append(1)
            for j in range(1, i):
                new = ans[i - 1][j - 1] + ans[i - 1][j]
                ans_i.append(new)
            ans.append(ans_i)
            ans_i.append(1)
        return ans[rowIndex]
    