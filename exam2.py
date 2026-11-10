# 문제 : 실행되는 출력문에는 `참` 그렇지 않으면 `거짓` 이라고 적어주세요.
# 조건 : `참1`, `참2`, `거짓1` 이런 순으로 적어주세요.

# 개념시작
if ( True ):
  print("참")
    
if ( False ):
  print("거짓")
# 개념끝

# 문제시작
a = 10

# `==` => 같다.
if ( a == 10 ):
  print("참1")

# `!=` => 같지 않다.
if ( a != 10 ):
  print("거짓1")

if ( a > 10 ):
  print("거짓2")

if ( a >= 10 ):
  print("참2")

b = 10

if ( a == b ):
  print("참3")

# c 에는 true or false 이 담긴다.
c = a != b

if ( c ):
  print("거짓3")

if ( c == False ):
  print("참4")

# `not` => 반전
if ( not c ):
  print("참5")

if ( not(not c) ):
  print("거짓4")

d = True

if ( c != d ):
  print("참6")

if ( 10 > 5 and -6 > -10 and 10 != 10 ):
  print("거짓5")

if ( 10 < 5 and -6 < -10 and 10 != 10 or 10 > 5 ):
  print("참7")

print("=============================")

# 문제 : 10대, 20대, 30대 중 나이에 맞는 변수를 출력해주세요.

age = 15 # 25로 바꿔서 실행해보세요. 15로도 바꿔서 실행해보세요.
if age >=10 and age < 19:
    print("10대")
elif age >=20 and age < 29:
    print("20대")
elif age >=30 and age < 39:
    print("30대")

print("==============================")

# 문제 : 할인 대상인지 아닌지 출력해주세요.
# 조건 : 나이가 19세 이하이거나 60세 이상이면 할인 대상입니다.
# 조건 : `and, or`없이 풀어야 합니다.
# 조건 : 2가지 이상의 방법으로 풀어야 합니다.

age = 33
if age <= 19:
    print("== 정답 v1 ==")
    print("할인 대상입니다.")
elif age > 19:
    if age < 60:
        print("할인 대상이 아닙니다.")


if age >= 60:
    print("== 정답 v2 ==")
    print("할인 대상입니다.")
elif age < 60:
    if age > 19:
        print("할인 대상이 아닙니다.")

print("==============================")

# 문제 : 1부터 300까지 출력해주세요.
i = 1
while i <= 300:
   print(i)
   i += 1

print("==============================")  

# 문제 : 100부터 -25까지 출력해주세요.
i = 100   
while i >= -25:
   print(i)
   i -= 1

print("==============================")  

# 문제 : 1부터 100 사이의 짝수만 출력해주세요.(개념 : while, if, %)
i = 1
while i <= 100:
    if i % 2 == 0:
      print(i)
    i += 1

print("==============================") 

# 문제 : 1부터 1000 사이의 수 중에서 3의 배수만 출력해주세요.
i = 1
while i <= 1000:
    if i % 3 == 0:
      print(i)
    i += 1

print("==============================")  

# 문제 : 1부터 5까지의 합을 출력해주세요.(개념 : while)
i = 1
a = 0
while i <= 5:
   a += i
   i += 1
print(a)


print("==============================") 

#문제 : 1부터 100까지의 수 중에서 짝수의 합을 출력해주세요.(개념 : while, if, %)

i = 1
a = 0
while i <= 100:
    if i % 2 == 0:
      a += i
    i += 1
print(a)

print("==============================")

i = 1
while i <= 10:
    j = 1
    while j <= 3:
      print(j)
      j += 1
    i += 1

print("==============================")

# 문제 : for문으로 1부터 100까지 출력

for i in range(1, 101):
   print(i)

print("==============================")

# 문제 : for문으로 100부터 1까지 출력
for i in range(100, 0, -1):
   print(i)

print("==============================")

# 문제 : for문으로 구구단 1단 ~ 9단 출력
for i in range(1,10):
   print(f"{i}단")
   for j in range(1,10):
    print(f"{i} * {j} = {i * j}")

print("==============================")

# 문제 : 함수를 사용해서 코드량을 확 줄여주세요.
def dan_8():
    dan = 8
    i = 1
    while i <= 9:
        print("{} * {} = {}".format(dan, i, dan * i))
        i += 1

for i in range(1,10):
   print(f"== {i}번째 구구단 8단 출력 ==")
   dan_8()

print("==============================")

def dan_n(dan):
    i = 1
    while i <= 9:
        print("{} * {} = {}".format(dan, i, dan * i))
        i += 1

for i in range(1,10):
   print(f"== {i}번째 구구단 8단 출력 ==")
   dan_n(10)

print("==============================")

# 문제 : 함수를 사용해서 코드량을 확 줄여주세요.
def print_n_dan(dan):
    print("== {}단 ==".format(dan))
    i = 1
    while i <= 9:
        print("{} * {} = {}".format(dan, i, dan * i))
        i += 1

for i in range(1,10):
   print_n_dan(i)

print("==============================")

def add(a, b):
    j = a + b
    return j

x = add(10,20)
print(x)

print("==============================")




