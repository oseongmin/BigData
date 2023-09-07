import numpy as np
import random

#v = np.array([1, 3, -9, 2])
#v = np.array([1, 3, -9, 2], dtype='int64')
#v = np.array([
#	[1, 3, -9, 2],
#	[71, 13, -22, 7]])
#print(v.ndim, v.shape, v.data, v.dtype, v.strides)
#print(v)
num = int(input("변수 입력 : "))
l = list()
for i in range(num):
	l.append(random.randint(1, 100))

v = np.array(l, dtype='int16')
print(v, v.ndim, v.data, v.dtype, v.strides)
