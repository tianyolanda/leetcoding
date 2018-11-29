class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        if len(a)<len(b):# 让a是长，b是短
            temp = a
            a = b
            b = temp
        i = -1
        c = 0
        while i >= -len(a) :
            if i >= -len(b):
                b_ = b[i]
            else:
                b_ = 0
            s = int(a[i])+int(b_)+c
            res += str(s%2)
            c = s//2
            i -= 1
        if c == 1:
            res += '1'
        return res[::-1]