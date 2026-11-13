import numpy as np

scores = np.array([[70, 85, 90],
                   [65, 75, 80],
                   [95, 60, 70],
                   [80, 90, 85]])

bonus = np.array([5, 10, 15])

# 1. 모든 학생의 점수에 과목별 보너스 점수를 더해주세요.
print(scores + bonus)
sb = scores + bonus
# 2. 보너스 점수를 더한 결과에서 100점을 초과한 점수는 100점으로 변경해주세요.
sbc =np.clip(sb,0,100)
print(sbc)

# 3. 변경된 점수를 기준으로 각 학생의 평균 점수를 구해주세요.
print(sbc.mean(axis=1))

# 4. 변경된 점수를 기준으로 각 과목의 평균 점수를 구해주세요.
print(sbc.mean(axis=0))

# 5. 변경된 점수에서 90점 이상인 데이터가 총 몇 개인지 구해주세요.
print(np.count_nonzero(sbc[sbc>=90]))

# 6. 변경된 점수를 기준으로총점이 가장 높은 학생의 번호를 출력해주세요.
# (학생 번호는 1번부터 시작)
total = sbc.sum(axis = 1)
print(total.argmax() + 1)


# 7. 변경된 점수를 기준으로 각 학생의 평균이 85점 이상이면 '우수',
#    그렇지 않으면 '일반'을 출력해주세요.
print(np.where(sbc.mean(axis=1)>= 85, "우수", "일반"))