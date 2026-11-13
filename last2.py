import numpy as np
# 1) 불리언 인덱싱
#  - 조건에 맞는 데이터만 추출하는 방법
#  - True에 해당하는 데이터만 선택하여 새로운 배열 생성

arr = np.array([10, 20, 30, 40 ,50])

# 조건식 확인
print(arr > 25)

print(arr[arr > 25])

arr2 = np.array([[10, 20, 30],
                 [40, 50, 60]])

print(arr2[arr2 >= 40])

# np.where()
# - 조건에 따라 서로 다른 값을 선택하는 함수
# - np.where(조건, 참일 때 값, 거짓일 때 값)

print("np.were")
result = np.where(arr >= 30, 1, 0)
print(result)

scores = np.array([80, 20, 66, 78, 54])
result = np.where(scores >= 60, '합격', '불합격')
print(result)

# 조건에 해당하는 위치 찾기
result = np.where(arr >= 30)
print(result[0])

# np.count_nonzero()
# - 배열에서 0이 아닌 개수를 구하는 함수
# - True는 개수를 셀 때 1, False 0으로 취급
arr = np.array([0, 10, 0, 20, 0, 0, 30])
print(np.count_nonzero(arr))

arr = np.array([10, 20, 30, 40, 50])
print(np.count_nonzero(arr >= 30)) # 조건식 만족한 것의 개수를 셀 수 도있음

arr = np.array([1, 2, 3, 4, 5, 6])
print(np.count_nonzero(arr % 2 == 0)) # 짝수 개수를 셀때

# np.argmax()
# - 배열에서 최댓값이 있는 위치(인덱스)를 반환
# - 최댓값이 여러 개면 첫 번째 위치 반환

print("np.argmax()")

arr = np.array([10, 40, 60, 80, 20])
print(arr.max())
print(arr.argmax())

arr2 = np.array([[10, 30, 70],
                 [90, 20, 50]])
print(arr2.argmax())
print(arr2.argmax(axis=0)) # 열별 최대값 인덱스를 구할수도 있다
print(arr2.argmax(axis=1)) # 행별 최대값 인덱스를 구할수도 있다

# np.unravel_index()
# - 1차원 인덱스를 다차원 배열의 좌표로 변환하는 함수
# - 2차원 배열에서 최댓값이 몇 행, 몇 열인지 확인 할 때 사용
# np.unravel_index(인덱스,배열의 shape)

print("np.unravel_index()")

arr = np.array([[10, 20, 30],
                 [40, 50, 60]])

# 최댓값의 인덱스 확인
index = arr.argmax()
print(index)

# 1차원 인덱스를 2차원 좌표로 변환
position = np.unravel_index(index, arr.shape)
print(position)
print(arr[position])

# np.clip()
# - 배열의 값을 지정한 최소, 최대 범위로 제한하는 함수
# - 최솟값보다 작으면 최솟값으로 변경
# - 최댓값보다 크면 최댓값으로 변경
# - 범위 안의 값은 그대로 유지
# - np.clip(배열, 최솟값, 최댓값)

print("np.clip()")

arr = np.array([10, 40, 50, 90, 100])
result = np.clip(arr, 20, 100)
print(result)

scores = np.array([70, 90, 110, 135])
result = np.clip(scores, 0, 100)
print(result)

# 브로드캐스팅(Boradcasiong)
# - 서로 다른 형태의 배열 끼리 연산할 수 있도록 하는 기능
# - 배열의 크기가 달라도 일정한 조건을 만족하면 연산 가능
# - 작은 배열을 큰 배열에 맞춰 연산하는 방식
# - 실제로 배열을 복사해서 늘릴 필요는 없음

print("브로드캐스팅")
arr = np.array([10, 20, 30])
print(arr + 5)

# 2차원 배열과 1차원 배열 연산
arr1 = np.array([1, 2, 3])
arr2 = np.array([[10, 20, 30],
                 [40, 50, 60]])
print(arr1 + arr2)