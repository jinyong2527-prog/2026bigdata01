# 1) 넘파이 배열 생성
#리시트로 생성: np.array([1,2,3])
#연속 값 생성: np.arange(0,10,2)(0부터 10미만까지 2씩 증가)
#특수배열:
#np.zeros((2,3)) : 0으로 채워진 2행3열
#np.ones((2,3)) : 1로 채워진 2행3열
#np.full((2,3)) :모든 요소를 2행3열
#import numpy as np
import numpy as np

l1=[1,2,3]
array01 = np.array(l1)
print(l1)
print(array01)

array02 = np.arange(0,10,2)
print(array02)

array03 = np.zeros((2,3))
print(array03)

array04 = np.ones((2,3))
print(array04)

array05 = np.full((2,3),-1)
print(array05)

array06 =np.random.rand(2,3)
print(array06)

# 2) 넘파이 배열 속성
#배열의 구조와 정보를 파악할 때 사용합니다.(arr가 배열일 때)
#arr.shape:
#arr.ndim:
#arr.dtype:
#arr.size:

#array08 =np.random.random((2,3,3))
array08 =np.random.random((4,2))
print(array08)
print(array08.shape,array01.dtype, array01.ndim, array01.size)
print(array08.T)
