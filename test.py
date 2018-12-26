# s = ""
# l = s.replace(',', ' ').split()
# print(l)

# m = [1,1,2,2,3]
# for i in range(0,len(m),2):
#     print(i)

# hashmap = {}
# hashmap['mmm'] = 0
# hashmap['mme'] = 0
# if hashmap.__contains__('mmm'):
#     print('yes')
#
# nums = [0,1,2,3,4,5,6,7]
# i = 4
# nums[i:] = nums[i:][::-1]
# nums= nums[::-1]
# print(nums)
# print((3+4)>>1)

# board = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
#
# print((board[3].count('8')))

# list = [1,2,3,4,5]
# l2 = [i for i in list if i < 4]
# print(l2)
#
# def test():
#   for i in range(6):
#     try:
#       print('try',i)
#       return i
#     finally:
#       print('f')
#
# test()
import numpy as np
a = np.array([1,2,3,4,5])
b = a-1
print(b)