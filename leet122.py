class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # method 2:
        profit = 0
        i = 0

        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i + 1] <= prices[i]:
                i += 1
            valley = prices[i]

            while i < len(prices) - 1 and prices[i + 1] > prices[i]:
                i += 1
            peak = prices[i]

            profit += peak - valley

        return profit

        # method 1:
        # profit = 0
        # i = 1
        # while i < len(prices):
        #     if prices[i] > prices[i-1]:
        #         profit += prices[i] - prices[i-1]
        #     i +=1
        # return profit