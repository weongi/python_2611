import numpy as np


print('===== 문제 1. 원하는 열 선택 및 평균 계산 =====')

arr = np.array([
    [4, 8, 2, 6],
    [7, 3, 9, 1],
    [5, 10, 12, 0]
])

# 1. 배열에서 네 번째 열과 두 번째 열을 순서대로 선택하여 새로운 배열을 만들어주세요.
# 예상 결과
# [[ 6  8]
#  [ 1  3]
#  [ 0 10]]

c = arr[:,[3,1]]
print(c)


# 2. 선택한 배열에서 각 행의 평균을 구해주세요.
print(arr.mean(axis=1))
# 3. 선택한 배열에서 가장 큰 값을 출력해주세요.
print(arr.max())


print('===== 문제 2. 음수 데이터 처리 및 분류 =====')

arr = np.array([
    [-3,  5, -1, 8],
    [ 7, -4,  6, 2],
    [-2, -5,  0, 9]
])

# 1. 배열에서 음수인 데이터만 출력해주세요.
print(arr[arr<0])
# 2. 음수를 모두 0으로 변경한 새로운 배열을 만들어주세요.
#    단, 원본 배열은 변경하지 않습니다.
print(np.where(arr<0,0,arr))
# 3. 원본 배열에서 각 행마다 음수가 몇 개 있는지 출력해주세요.
print(np.count_nonzero(arr < 0,axis = 1))
# 4. 각 행에서 음수가 2개 이상이면 '확인', 그렇지 않으면 '정상'으로 분류해주세요.
print(np.where(np.count_nonzero(arr < 0,axis = 1) >= 2,"확인","정상"))

print('===== 문제 3. 점수 보정 및 우수 학생 찾기 =====')

scores = np.array([
    [75, 80, 90],
    [85, 70, 95],
    [60, 90, 80],
    [95, 85, 90]
])

bonus = np.array([5, 10, 15])

# 1. 각 학생의 점수에 과목별 보너스 점수를 더한 새로운 배열을 만들어주세요.
#    첫 번째 과목 : +5점
#    두 번째 과목 : +10점
#    세 번째 과목 : +15점
sb = scores + bonus
print(sb)
# 2. 보너스 적용 후 100점을 초과하는 값은 100점으로 변경해주세요.
print(np.clip(sb,0,100))
s = np.clip(sb,0,100)
# 3. 보정된 점수를 기준으로 각 학생의 평균 점수를 구해주세요.
avg = s.mean(axis=1)
print(avg)
# 4. 평균 점수가 가장 높은 학생의 번호를 출력해주세요. (학생 번호는 1번부터 시작)
print(avg.argmax() +1 )
# 5. 평균 점수가 90점 이상이면 '우수', 그렇지 않으면 '일반'으로 분류해주세요.
print(np.where(avg >= 90,"우수","일반"))


print('===== 문제 4. 조건을 만족하는 행 추출 =====')

arr = np.array([
    [4, 6, 8, 2],
    [9, -1, 7, 5],
    [2, 3, 0, 4],
    [8, 10, 6, 8],
    [12, 3, -2, 7]
])

# 다음 두 조건을 모두 만족하는 행을 찾아주세요.
# 조건 1. 양수가 3개 이상일 것
# 조건 2. 행의 평균이 5 이상일 것
selected = []
for i in range(arr.shape[0]):
    row = arr[i] # 현재 행


    positive = np.count_nonzero(row > 0) # 양수 개수

    avg = row.mean()

    if positive >= 3 and avg >= 5:
        selected.append(i)


# 1. 조건을 만족하는 행의 인덱스를 출력해주세요.
print(selected)
# 2. 조건을 만족하는 행만 추출해주세요.
for i in selected:
    print(arr[i]) # 이건 한줄씩 나옴

result = arr[selected]
print(result)

# 3. 조건을 만족하는 행이 총 몇 개인지 출력해주세요.
print(len(result))
# 힌트 : for문과 if문을 사용해도 됩니다.



print('===== 문제 5. 구역별 합계 비교 =====')

arr = np.array([
    [1, 2, 9, 10],
    [3, 4, 11, 12],
    [5, 6, 13, 14],
    [7, 8, 15, 16]
])

# 배열을 다음과 같이 4개의 구역으로 나눠주세요.
# [ 1  2] | [ 9 10]
# [ 3  4] | [11 12]
# --------+--------
# [ 5  6] | [13 14]
# [ 7  8] | [15 16]

a = arr[:2, :2].sum()
b = arr[:2, 2:].sum()
c = arr[2:, :2].sum()
d = arr[2:, 2:].sum()


# 1. 각 구역의 합계를 구해주세요.
print(a)
print(b)
print(c)
print(d)
# 2. 구역별 합계를 다음 형태의 2차원 배열로 만들어주세요.

# [[왼쪽 위 합계, 오른쪽 위 합계],
#  [왼쪽 아래 합계, 오른쪽 아래 합계]]
result = np.array([[a,b],[c,d]])
print(result)

# 3. 합계가 가장 큰 구역의 위치를 (행, 열) 형태로 출력해주세요.
index = result.argmax()
position = np.unravel_index(index, result.shape)
print(position)
# 4. 가장 큰 합계도 출력해주세요.
big = result.max()
print(big)
# 힌트 : 반복문 없이 슬라이싱으로 해결할 수 있습니다.