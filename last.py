import numpy as np

arr = np.array([[3, 6, 9],
                [2, 4, 8],
                [5, 7, 1]])

# 문제
# 1. arr의 shape과 ndim을 출력하시오.
# 2. 열 방향 평균을 구하시오.
# 3. 행 방향 최댓값을 구하시오.
# 4. arr을 전치행렬로 만든 후 shape을 출력하시오.
# 5. arr을 1차원으로 펼친 뒤 최솟값을 구하시오.
# 6. arr을 (1, 9) 형태로 reshape 하시오.

print(arr.shape,arr.ndim)
print(arr.mean(axis=0))
print(arr.max(axis=1))
print(arr.T.shape)
print(arr.flatten().min())
print(arr.reshape(1, 9))

print("=======================")
import numpy as np

arr = np.array([[1.5, 2.5, 3.5, 4.5],
                [5.5, 6.5, 7.5, 8.5]])

# 문제
# 1. arr의 dtype과 itemsize를 출력하시오.
# 2. axis=0 기준 합을 구하시오.
# 3. axis=1 기준 평균을 구하시오.
# 4. arr을 (4,2) 형태로 reshape 하시오.
# 5. reshape한 배열을 전치한 결과의 shape을 구하시오.
# 6. arr.flatten()으로 만든 배열의 shape은 무엇인가?

print(arr.dtype, arr.itemsize)
print(arr.sum(axis = 0))
print(arr.mean(axis = 1))
print(arr.reshape(4,2))
print(arr.reshape(4,2).T.shape)
print(arr.flatten().shape)





