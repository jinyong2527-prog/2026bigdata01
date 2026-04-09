#배열의 구조와 정보를 파악할 때 사용합니다.(arr가 배열일 때)
#arr.shape:
#arr.ndim:
#arr.dtype:
#arr.size:
import numpy as np

#array01 =np.random.random((2,3,3))
array01 =np.random.random((4,2))
print(array01)
print(array01.shape,array01.dtype, array01.ndim, array01.size)
print(array01.T)