# 수학 모듈
import math

print(math.sqrt(16))
print(math.pow(2, 3))

print("==============================")

import random

print(random.randint(1, 100))

print("==============================")

#내가 만든 모듈을 사용 (ex1 파일꺼 가져온거임)
import ex1

print(ex1.funA())

print("==============================")

#날짜/시간 모듈
import datetime

print(datetime.datetime.now())

print("==============================")

#시간 제어 모듈
import time

time.sleep(3)

print("==============================")

#시스템 모듈
import sys

print(sys.version)

print("==============================")

#운영체제 모듈
import os

print(os.close)

print("==============================")

#데이터 형식 모듈
import json
data = {
    'name' : 'jin',
    'age' : 22
}

print(json.dumps(data)) #json형식으로 변환

print("==============================")

# 정규표현식 모듈
import re

print(bool(re.match('hi', 'hi python'))) #문자열이 hi로 시작하는지 확인

print("==============================")

# CSV 파일 모듈
import csv

with open('test.csv', 'w', newline ='') as f: #test csv를 f로 불러온다
    csv.writer(f).writerow(['name', 'score']) # f에다가 name, score 데이터를 입력

print("==============================")

# 자료구조 모듈
from collections import Counter

print(Counter('apple')) #문자열에서 각 글자의 개수를 셈

print("==============================")

# Python 유니코드 / 인코딩 핵심 정리
text = '파이썬'
print(text)
print(len(text))

# 문자 <-> 유니코드 변환
print(ord('가')) # 문자를 유니코드로 변환
print(chr(44032)) # 유니코드를 문자로 변환

# 인코딩
# Encode : 문자열을 바이트(byte)로 바꾸는 작업
# 파일 저장이나 네트워크 전송 시 사용됨
encoded = text.encode('utf-8')
print(encoded)

# Decode : 인코딩의 반대 과정 : 문자열로 다시 복원하는 과정
decoded = encoded.decode('utf-8')
print(decoded)


# 인코딩이 맞지 않으면 오류 발생
try:
    wrong = encoded.decode('cp949')
    print(wrong)
except UnicodeDecodeError:
    print('인코딩 방식이 맞지 않아 오류 발생')

print("==============================")

# 클로저(Closure) 데코레이터(Decorator)

# 클로저 : 내부 함수가 자신이 정의된 외부 함수의 변수들을 기억하고, 외부 함수의 실행
print('=== 1단계: 함수 안에 함수 만들기 ===')
def outer():
    print("outer 함수가 실행되었습니다")

    def inner():
        print('inner 함수가 실햄되었습니다.')

    return inner # 함수 자체를 반환  / 함수를 실행하고 그 결과를 반환

func = outer() 
func()

print('\n=== 2단계: 클로저 ====')
# 클로저는 '외부 함수의 변수를 기억하는 내부 함수'입니다.
def make_multiplier(x):
    # x는 make_multiplier 함수의 지역 변수
    
    def multiplier(n):
        # 내부 함수 multiplier는
        # 바깥 함수의 변수 x를 사용할 수 있다.

        return x * n 
    
    return multiplier

times3 = make_multiplier(3)
print(times3(10))
print(times3(5))

print('=== 3단계: 클로저 ===')

# 데코레이터는 '함수를 꾸며주는 함수'
# 내부 구조는 클로저와 매우 유사 
def decorator(func):
    #func는 꾸며줄 함수
    def wrapper():
        print('함수 실행 전')
        func()
        print('함수 실행 후')

    return wrapper

def say_hello():
    print("안녕하세요")

decorated = decorator(say_hello) # @decorator로 사용 가능한데 잘 모르겠음
decorated()
say_hello()

print('\n==== 4단계: 매개변수가 있는 데코레이터 ====')

def decorator_width_args(func):
    def wrapper(name):
        print('실행 전')
        func(name)
        print('실행 후')
    return wrapper

@decorator_width_args
def say_name(name):
    print('이름 :', name)

say_name('홍길동')

print("==============================")
#  어노테이션(Annotation) : 타입을 명시한다 1. 가독성향상, 2. 코드이해

# 기본 변수
age = 30

# 어노테이션 추가
age: int = 30 # 변수이름: 자료형 = 값

print(age)

print("==============================")

# 함수 어노테이션
def add(a: int, b: int) -> int: # a값 int, b값 int  ->(리턴값)도 int
    return a + b

print(add(3, 5))

# 리스트, 딕셔너리 어노테이션
# 리스트 안에 int가 들어간다는 의미
nums : list[int] = [1, 2, 3]

# 딕셔너리 타입 지정
person : dict[str, int] = {
    'age' : 30,
    'height' : 170
}

print("==============================")

# 정규 표현식 : 문자열에서 특정한 규칙이나 패턴을 가진 데이터를 추출, 검색, 치환하기 위한 표현 방식
# --> 쓰는이유 : 문자열 검색, 데이터 추출, 문자열 치환, 입력값 검사, 데이터 정제
import re

print('=== 정규 표현식 ===')
text = '내 혈압은 12mmHg 입니다.'
print('120' in text)

# 정규표현식
pattern = r'\d+' # 숫자 연속된것을 찾겠다

result = re.findall(pattern, text)

print(result)

print("=== 정류 표현식 : 기본 패턴 ===")
sample = "abc123xyz456"

# 숫자 찾기
print(re.findall(r'\d+', sample)) # +를 하면 연속으로 추출하고, 없으면 하나씩 추출
                                  # * -> 0개 이상, ? -> 0개 또는 1개
# 문자 찾기
print(re.findall(r'[a-z]+', sample))

print("=== 정규 표현식 : 특정 형식 찾기 ===")

data = '이메일은 test123@gmail.com 입니다.'
email_pattern = r'\w+@\w+\.\w+'
emails = re.findall(email_pattern, data)

print(emails)

# \w -> 문자 또는 숫자
# @ -> @answk
# \, -> .은 정규식에서 특수 문자이기 때문에 \를 붙여야함

print("=== 정규 표현식 : re모듈 주요 함수 ===")

# re.findall
# re.search() : 찾는다
# re.match() : 문자열 패턴 검사
# re.fullmathch() : 전체가 같은지 패턴 검사
# re.sub()
# re.split()

print("=== 정규 표현식 : 문자열 치환(replace 대신 re.sub) ===")

text2 = '가격은12000원 입니다.'

# 숫자 제거
new_text = re.sub(r'\d+', '', text2)
print(new_text)

print("=== 정규 vs 일반 문자열 처리 비교 ===")

text3 = "몸무게: 70kg, 키 : 170cm"

# 단순 split 사용
print(text3.split(','))

# 정규식으로 숫자만 추출
nums = re.findall(r'\d+', text3)
print(nums)

# 정규식 쓰는이유 : 1. 크롤링 데이터에서 숫자만 추출, 2. 단위 제거, 3. 특정 형식 데이터를 찾기 4. 불필요한 특수 문자 제거

