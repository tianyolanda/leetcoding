class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        minbuy = 2 ** 31 - 1
        for b in prices:
            if b < minbuy:
                minbuy = b
            elif b - minbuy > profit:
                profit = b - minbuy

        return profit