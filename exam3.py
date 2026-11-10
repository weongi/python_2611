# 문제 : 입력받은 정수가 소수인지 아닌지 알려주는 함수를 구현해주세요.

def is_prime_number(num):
    cnt = 0
    if num >= 2:
        for i in range(1, num+1):
            if num % i == 0:
                cnt += 1
                if cnt >= 3:
                    return False

    if cnt == 2:
        return True

    return False

print("3은 소수입니다 : {}".format(is_prime_number(3)))
print("4는 소수입니다 : {}".format(is_prime_number(4)))
print("5는 소수입니다 : {}".format(is_prime_number(5)))
print("6는 소수입니다 : {}".format(is_prime_number(6)))
print("7는 소수입니다 : {}".format(is_prime_number(7)))
print("25는 소수입니다 : {}".format(is_prime_number(25)))
print("1000은 소수입니다 : {}".format(is_prime_number(1000)))

print("==============================")

# 문제 : 리스트에 순서대로 2, 1, 5, 6, 7를 한 번에 담아주세요.
list1 = [2, 1, 5, 6, 7]

print("==============================")

# 문제 : 비어있는 리스트를 만들고, 순서대로 2, 1, 5, 6, 7를 하나씩 담아주세요.
list2 = []
list2.append(2)
list2.append(1)
list2.append(5)
list2.append(6)
list2.append(7)

print("==============================")

# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 그리고 '+=' 연산자를 이용해서 '토', '일' 을 한번에 추가해주세요.

list3 = ['월', '화', '수', '목', '금'] 
list3 += ['토','일']
print(list3)

print("==============================")

# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 그리고 가장 마지막 요소를 출력해주세요.
list4 = ['월', '화', '수', '목', '금']
print(list4[4])

print("==============================")

# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 그리고 while문을 이용해서 요소 전부 출력해주세요.
list5 = ['월', '화', '수', '목', '금']

i = 1
while i <= len(list5):
    print(list5[i-1])
    i += 1

print("==============================")

# 문제 : 리스트에 순서대로 2, 1, '오', 6, 7를 한번에 담아주세요. 그리고 리스트 안에 있는 '오'를 정수 5로 변경해주세요.
list6 = [2, 1, '오', 6, 7]

list6[2] = 5
print(list6)
if '오' in list6:
    x = list6.index('오')
    list6[x] = 5
print(list6)

print("==============================")

# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. '화'가 리스트 안에 들어있는지 알려주세요.
list7 = ['월', '화', '수', '목', '금']

if '화' in list7:
    print("있다")

# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. '화'가 리스트 안에서 몇 번째 데이터 인지 알려주세요.
list8 = ['월', '화', '수', '목', '금']

print(list8.index('화'))

print("==============================")

# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 리스트에 있는 '금'을 삭제하는 3가지 방법을 보여주세요.
list9 = ['월', '화', '수', '목', '금']
if '금' in list9:
    x = list9.index('금')
    list9.pop(x)
    print("list9 =",list9)

list10 = ['월', '화', '수', '목', '금']
list10.remove('금')
print("list10 =", list10)

list11 = ['월', '화', '수', '목', '금']
if '금' in list11:
    x = list11.index('금')
    del list11[x]
    print("list11 =", list11)

print("==============================")

# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담기
month = {
    "1월" : 31,
    "2월" : 28,
    "3월" : 31,
    "4월" : 30,
    "5월" : 31,
    "6월" : 30,
    "7월" : 31,
    "8월" : 31,
    "9월" : 30,
    "10월" : 31,
    "11월" : 30,
    "12월" : 31
}
print(month)

print("==============================")

# 문제 : 딕셔너리에 각 달의 마지막 날들을 반복문을 통해 담기

month = {}

for i in range(1,13):
    if i == 2:
        month[f"{i}월"] = 28
    elif i == 4 or i == 6 or i == 9 or i == 11: # elif i in [4,6,9,11]
        month[f"{i}월"] = 30
    else:
        month[f"{i}월"] = 31
print(month)

print("==============================")

print('== 예제 1 ==')
s = '안녕하세요.' # [0,1,2,3,4,5]

print('s의 길이 출력')
print(len(s))

#문자열[시작:종료-1:간격]
print('s를 이루는 문장 중에서 앞에 거 2개 출력')
print(s[0:2])

print('s를 이루는 문장 중에서 문자 하나 건너 뛰고 1개 출력')
print(s[1:2])
print(s[1])

print('s를 이루는 문장 중에서 문자 4개 출력')
print(s[0:4]) # s[:4]
print(s[-6:-2])

print('s를 이루는 문장 중에서 앞에 문자 3개 건너 뛰, 나머지 전부 출력')
print(s[3:]) # s[3:len(s)]

print("==============================")

print('=== 예제 2 ==')
s = '안녕하세요.'

print("s를 이루는 문자를 하나씩 출력, while")
i = 0
while i < len(s):
    print(s[i])
    i += 1

print('s를 이루는 문자를 역순으로 하나씩 출력, while')
i = len(s) -1
while i >= 0:
    print(s[i])
    i -= 1

print('s를 이루는 문자를 하나씩 출력, for')
for c in s:
    print(c)

print('=== 예제 3 ===')
s = 'a안b녕c하d세e요f'

print('s를 이루는 문장 중에서 한글만 출력')
print(s[1] + s[3] + s[5] + s[7]+ s[9])
print(s[1:len(s):2])

print('s를 이루는 문장 중에서 한글만 출력, for if, or , continue')
s = 'a안b녕c하d세e요f'
for c in s:
    if c == 'a' or c == 'b' or c == 'c' or c == 'd' or c == 'e' or c == 'f':
        continue
    print(c)

print('s를 이루는 문장 중에서 한글만 출력, for, if, and')
for c in s:
    if c != 'a' and c != 'b' and c != 'c' and c != 'd' and c != 'e' and c != "f":
        print(c)

print("s를 이루는 문장 중에서 한글만 출력, for, not in")
for c in s:
    if c not in['a','b','c','d','e','f']:
        print(c)

print("==============================")

class Person:
    def hello(self):
        print('hi')

jin = Person() # Jin은 Person의 인스턴스
jin.hello()

print("==============================")

class Person():
    def __init__(self): ##클래스에서 속성(변수)을 만드는 방법
        self.hello = '안녕하세요'
        

    def hi(self):
        print(self.hello)

jin = Person() # 이 때 __init__ 메서드가 실행됐다
jin.hi()

print("==============================")

class Person():
    def __init__(self, name, age, hobby): ##클래스에서 속성(변수)을 만드는 방법
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.hobby = hobby
        

    def introduce(self):
        print(f"{self.hello}, 저는 {self.age}살 {self.name}이고 {self.hobby}입니다")

jin = Person("사원기", 32, "게임")
jin.introduce() 

print("==============================")

class Person:
    pass

jin = Person() # 인스턴트 생성
jin.name = '진' # 인스턴스를 생성한 뒤 속성 추가 --> 이렇게 생성하면 특정 하나만을 위한 속성

print("==============================")

# 클래스 외부에서는 접근 불가, 클래스 내부에서만 사용 가능한 private attribute
class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight # 외부에서 접근 불가하는 __weight 

jin = Person("진", 22, 80)
#jin.weight -= 20

#print(jin.weight)

print("==============================")

class Person():
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

# 클래스 속성
class Person:
    folder = [] # 클래스 속성 (공용)

    def add_filese(self, file):
        self.folder.append(file)

jin = Person()
jin.add_filese('txt')

kim = Person()
kim.add_filese('img')

print(jin.folder)
print(kim.folder)


