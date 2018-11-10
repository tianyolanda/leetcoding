import numpy as np
import time

time1=time.time()
nums = [2,7,13,11]
target = 9
x = np.zeros((0, 0))
x = np.reshape(nums, (len(nums), 1))
y = x + nums # 一个竖着的矩阵和一个list相加,得出的是一个二维的,两两相加的矩阵

result = np.asarray(np.where(y == target)).T # 会有两个结果,选择第一个
time2=time.time()

print(result[0])
print(time2-time1)
