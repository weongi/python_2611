# Matplotlib = 데이터를 표현 할 수 있게 해주는 파이썬 라이브러리(차트 같은거 만들어준다~)
# figure -> 큰도화지 
# subplots -> 도화지 원에 나눠진 작은 칸들

import matplotlib.pyplot as plt

#기본 스타일 적용
plt.style.use('default')


#plt.plot([2, 4, 6, 8]) # y값만 전달 --> x는 자동으로 0 1 2 3이 설정
x = [1, 3, 5, 7]
y = [2, 4, 6, 8]
plt.plot([1, 3, 5, 7], [2, 4, 6, 8]) # x값과 y값 설정 plt.plot(x, y)랑 똑같음
plt.show() #만든걸 화면으로 보여줌

fig = plt.figure() # 큰도화지를 만든다

#(행 개수, 열 개수, 위치값)
fig.add_subplot(1, 2, 1)
fig.add_subplot(1, 2, 2)
plt.show()

fig2 = plt.figure()
fig2.add_subplot(1, 2, 1)
fig2.add_subplot(2, 2, 2)
plt.show()

fig3 = plt.figure()
a1 = fig3.add_subplot(1, 2, 1)
a2 = fig3.add_subplot(1, 2, 2)

x = range(0, 10)
y = range(5, 15)
a1.plot(x, y, 'c*')

q = range(0, 50)
w = range(0, 50)
a2.plot(q, w, 'mp')

plt.show()

fig = plt.figure()


plt.style.use("ggplot")
a = fig.add_subplot(111) # 1행 1열짜리 영역에서 1번째 위치에 그래프생성
x = [3, 4] # 막대의 위치(좌표 기준)
y = [1, 2] # 막대의 높이(값 기준)

labels = ['english', 'math'] # x축 라벨 이름(tick 이름)
colors =['red', 'blue'] # 각 막대에 적용할 색상

a.bar(x,y, tick_label = labels, color = colors) # 세로 막대

a.barh(x,y, tick_label = labels, color = colors) # 가로막대  
plt.show()

