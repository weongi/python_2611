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

