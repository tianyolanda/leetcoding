class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # method 1:
        # space_num=0
        # letter = 0
        # for i in range(len(s)-1):
        #     if s[i].isspace():
        #         if not s[i+1].isspace():
        #             letter = 0
        #         else: continue
        #     else:
        #         letter += 1
        # if s[-1].isspace():
        #     return letter
        # else: return letter+1

        # method 2:
        l = s.replace(',', ' ').split()
        if not l:
            return 0
        else: return len(l[-1])