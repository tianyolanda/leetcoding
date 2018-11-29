class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 遇到该类型题（N进制），立马分析是否要【按位运算】
        # 1. 如何拆分位
        # 2. 如何整除取余数（是否需要+1、-1）
        # 3. 使用几个例子做一下题，就有思路了
        ans = ''
        while n:
            k = (n - 1) % 26
            ans += chr(65 + k)
            n = (n - 1) // 26

        return (ans[::-1])


