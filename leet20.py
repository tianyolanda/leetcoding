class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        cl = ['(', '{', '[']
        cr = [')', '}',']']
        # pair = {'(':')', '{', '['}
        l = []

        for i in s:
            if i in cl:
                l += [i]
            else:
                if not l:
                    return False
                elif cl.index(l[-1]) == cr.index(i):
                    l.pop()
                else:
                    return False
        if l:
            return False
        else:
            return True

so=Solution()
print(so.isValid(""))
