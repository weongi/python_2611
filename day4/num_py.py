# Numpy : 파이썬에서 수학과 데이터 분석을 쉽게 할 수 있도록 도와주는 라이브러리
# ndArray : 숫자를 여러 차원으로 저장할 수 있는 배열
# Numpy로 할 수 있는 것들
# - 숫자 묶음 생성
# - 평균, 합계, 최댓값
# - 배열
# - 2차원 표 (행렬)
import numpy as np

print("==============================")

# 일반 리스트
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

print("==============================")

# numpy
a = np.array([1, 2, 3]) #array는 수학용 배열(모든 원소가 같은타입) -> 넘파이랑 비슷해보이지만 좀 다름
b = np.array([4, 5, 6])
print(a + b)

print("==============================")

# numpy2
np.array([1,2,3,4]) # 1차원 ndArray 생성(1차원 배열 생성)

print("==============================")

# 1차원 배열 : 숫자가 한 줄로 늘어선 형태
# 2차원 배열 : 숫자가 가로와 세로로 된 표 모양
# 3차원 배열 : 2차원 배열이 여러 장 겹친 입체 모양

# 2차원 ndArray 생성
# 1차원 배열 두개가 리스트로 묶인 형태
arr2 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

arr3 = np.array([[[1, 2, 3, 4], [1, 2, 3, 4]],
                [[5, 6, 7, 8],[5, 6, 7, 8]]])

print("2차원 배열")
print(arr2)
print("3차원 배열")
print(arr3)

print("==============================")

# numpy4
a = np.array([1, 2, 3, 4])

print(a + 1)
print(a * 2)
print(a ** 2)

print("==============================")

# numpy5
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])
arr3 = np.array([[[0.1, 0.2, 0.3, 0.4],[5, 6, 7, 8]],
                 [[1, 2, 3, 4], [5, 6, 7, 8]]])

# ndim : 배열의 차원 수
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# shape : 배열의 형태(배열 구조를 튜플로 보여줌)
print(arr1.shape) # (4,) 
print(arr2.shape) # (2, 4_) = 8 
print(arr3.shape) # (2, 2, 4) = 16 

# size : 배열의 총 개수
print(arr1.size)
print(arr2.size)
print(arr3.size)

# dtype : 배열 요소의 데이터 타입
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)

# itemsize : 배열 원소 하나가 차지하는 메모리 크기
print(arr1.itemsize)
print(arr2.itemsize)
print(arr3.itemsize)

# data : 배열의 실제 데이터가 저장된 메모리 버퍼(buffer 주소)
print(arr1.data)
print(arr2.data)
print(arr3.data)

print("==============================")

# numpy 6
# ndArray T : 전치 행렬(행/열을 서로 바꾸는 것)
arr = np.array([[1,2,3],
                [4,5,6]])
print('원래 배열')
print(arr)

print('전치 배열')
print(arr.T)

print("==============================")

# numpy7
arr = np.array([[1,2,3],
                [4,5,6]])
print('원래 배열')
print(arr)

print('1차원으로 펼친 배열')
print(arr.flatten())

flat = arr.flatten() # flatten()은 복사본(copy)을 만든다
flat[0] = 100
print('배열 출력')
print(flat)
print('flatten한 arr')
print(arr.flatten())

print("==============================")

# numpy8
# ndArray.reshape(): 배열 모양 바꾸기
arr = np.array([[1,2,3],[4,5,6]])

print('원래 배열')
print(arr)

# reshape 할 때 원본과 size가 같아야함(원하는 배열로 바꾸기 위해 사이즈가 똑같아야한다는말 같음 )
arr2 = arr.reshape(2, 3) # 2행 3열 반환
print('rshape 배열')
print(arr2)

print("==============================")
# ndArray.sum() : 합계 구하기
# axis : 어느 축을 기준으로 계산할 것인가(행 이냐 열이냐)
# 0은 열 방향 합, 1은 행 방향 합 
arr = np.array([[1,2,3],
                [4,5,6]])

print('전체 합 :', arr.sum())
print('열 방향 합 :', arr.sum(axis = 0))
print('행 방향 합 :', arr.sum(axis = 1))

print("==============================")

# numpy10
# ndArray.mean() : 평균 구하기
arr = np.array([[1,2,3],
                [4,5,6]])

print('전체 평균 :', arr.mean())
print('열 방향 평균 :', arr.mean(axis = 0))
print('행 방향 평균 :', arr.mean(axis = 1))

print("==============================")

# numpy11
# ndArray.min() , ndArray.max() : 최소, 최대값
arr = np.array([[1,2,3],
                [4,5,6]])

print('전체 최소값 :', arr.min())
print('열 방향 최소값  :', arr.min(axis = 0))
print('행 방향 최소값  :', arr.min(axis = 1))

print('전체 최대값 :', arr.max())
print('열 방향 최대값 :', arr.max(axis = 0))
print('행 방향 최대값 :', arr.max(axis = 1))

print("==============================")

# numpy12
# 1) np.zeros(shape) --> 지정한 모양으로 배열을 만들고 0으로 다 채움
#   - 주로 초기 값이 0인 배열이 필요할 때 사용(누적합, 버퍼 마스크)
#   - shape은 튜플로 넣음 : (행, 열 또는 (층, 행, 열))
print(np.zeros((3, 4))) # 3행 4열의 2차원 배열 생성, 전부 0 

print("==============================")

# numpy13
# 2) np.ones(shape) --> 지정한 모양으로 배열을 만들고 1로 다 채움
#   - 기준값을 1로 시작하거나, 가중치/마스크의 기본값으로 자주 사용
print(np.ones((2, 3, 4))) # 3차원 배열 생성 2층 각 층은 3행 4열

print("==============================")

# numpy14
# 3) np.full(shape, full_value)
#   - 지정한 shape(모양으로 배열을 만들고, 모든 원소를 특정 값으로 채움)
#   - 임의의 상수로 초기화 할 때 사용

print("==============================")

# numpy15
# 4) *_like 계열 : np.zeros_lik / np.ones_like / np.full)like
#   - like 말 그대로 다른 배열을 보고 똑같이 따라 만듬
#   - 즉, 기존 배열의 shape을 가져와서 새 배열을 생성
#   - 장점 : 1) shape을 매번 직접 적을 필요가 없음(실수 줄어듬), 2) 기본적으로

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

print(np.zeros_like(arr2))
print(np.ones_like(arr2))
print(np.full_like(arr2,2))

print("==============================")

# numpy16
# np.random 모듈은 다양한 난수 생성 기능 제공
# 머신러닝, 시뮬레이션, 데이터 생성, 테스트 데이터 제작 등에 사용

# 1) randint(시작값, 끝값, size)
# 지정 범위 안에서 정수형 난수 생성
# - 시작값 이상
# - 끝값 미만(끝값은 포함되지 않음)
# - size는 생성할 배열의 shape(모양)

print(np.random.randint(-100, 100, (2, 3))) # - 100이상 100미만 정수이면서 2행 3열로 배열을 생성

# 2) seed(숫자)
# 난수 생성의 초기 상태 고정
# 같은 seed를 주면 항상 같은 난수 결과가 나옴

np.random.seed(1) # 난수 생성 기준을 1로 고정
print(np.random.randint(0, 10, (2,3)))

np.random.seed(2) # 난수 생성 기준을 2로 고정
print(np.random.randint(0, 10, (2,3)))

print("==============================")

# 인덱싱(Indexing) : 특정 위치에 있는 하나의 값을 가져오는 방법
# 슬라이싱(slicing) : 일정 범위를 잘라서 여러 값을 가져오는 방법

arr1 = np.array([1, 2, 3, 4]) # 1차원 배열, shape = (4,)
arr2 = np.array([[1, 2, 3, 4],  # 2차원 배열, shape = (2, 4)
                 [5, 6, 7, 8]])

# 1차원 배열 인덱싱 
print("파이썬 기본 리스트 예시")
li = [1, 2, 3,4]
print(li[0])

print('1차원 배열 인덱싱')
print(arr1[0])

# 2차원 배열 인덱싱
# 기본 형태 : arr2[행, 열]
print('2차원 배열 인덱싱')
print(arr2[0, 1])

print(arr2[1, 2])

# 2차원 배열 슬라이싱
# 기본 형태 : arr2[행 범위, 열 범위]
print(arr2[0:2, 1:3])

# fancy 인덱싱 : 인덱스 번호를 리스트/배열로 여러개 전달
print('1차원 배열 fancy 인덱싱')
print(arr1[[0,1,3]])

print('2차원 배열 fancy 인덱싱')
print(arr2[[0,1], [1,3]])

print('fancy 인덱싱 + 슬라이싱')
print(arr2[:, [0, 3]]) # 행은 전체 선택 열은 0번과 3번만 선택


