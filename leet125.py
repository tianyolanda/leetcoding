class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        print(s)
        s = s.lower()
        s = re.sub('[^0-9a-z]','',s)
        print(s)
        s1 = s[::-1]
        return s1==s

so = Solution()
so.isPalindrome("A man000, a plan, a canal: Panama")