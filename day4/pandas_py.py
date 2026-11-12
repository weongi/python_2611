import pandas as pd

df = pd.DataFrame(

    {

        "Name": [

            "Braund, Mr. Owen Harris",

            "Allen, Mr. William Henry",

            "Bonnell, Miss Elizabeth",

        ],

        "Age": [22, 35, 58],

        "Sex": ["male", "male", "female"],

    }

)
print("전체 출력")
print(df)

# 열 하나씩 출력 
# 결과는 dataFram이 아니라, Series 라는 1차원 자료 구조로 나옴
print("열 하나씩 출력")
print(df['Name'])
print(df['Age'])
print(df['Sex'])

print("타입 출력")
print(type(df))
print(type(df['Age']))

print("이름이 Age인 Series 생성")
ages = pd.Series([22, 35, 44], name='Age')
print(ages)

print("DataFRame에서 특정 열 꺼내기")
print(df['Age'])

print("기본 통계 함수")
print("max : 최댓값")
print("최대 나이 :",df['Age'].max())

print("max : 최소값")
print("최소 나이 :",df['Age'].min())

print("max : 평균")
print("평균 나이 :",df['Age'].mean())

print("요약 통계 정보 보기")
print(df.describe()) # 숫자형 열에 대해 '요약 통계 정보'를 한번에 보여줌

print("DataFRame의 전체 요약 정복")
print(df.info) # 전체 요약을 간단하게 보여줌 

print(" DataFram에서 특정 행을 선택하는 방법 2가지")
# iloc : "위치(Position)"로 선택(0번째, 1번째 처럼 순서/번호)
# loc : '라벨(Label)'로 선택(index에 붙어있는 이름으로 접근)

# iloc
# - index의 값이 뭐든 상관없이 몇번째 줄이냐로 가져옴
# ex) df.iloc[0] ==> 첫번째 행 0의 위치를 가져옴
print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[2])

# loc
# - index 라벨로 접근
# index를 '이름'으로 바꾸면(ex : Name열을 index로 지정) --> loc은 인덱스를 명사로 바꿀때 쓰기 유용한듯?( 이름, 순서 등)
print(df.iloc[0])

print("상위/하위 데이터 출력")
# head() : 상위 5개 행만 보여줌
# tail() : 하위 5개 행만 보여줌

print(df.head())
print(df.head(2)) # --> 2개만 나옴

print(df.tail())
print(df.tail(2)) # --> 2개만 나옴

print("열 수정")
# 새로운 열 추가
df["Survived"] = [0, 1, 1]
print(df)

# 열 이름 바꾸기
df = df.rename(columns ={'Sex' : 'Gender'})
print(df)

df = df.drop('Survived', axis = 1) # 열 삭제 0은 행 삭제
print(df)

print("결측치(NAN) 처리") # 결측치란 값이 비어있는 상태 , pandas에서 nan으로 표시(None을 넣어도 자동 변환됨)

print(df)
print(df.isnull()) # null이 있는지 확인

df2 = df.copy() # df를 복제

df2.loc[1, 'Age'] = None # 인덱스 1에 age에 None 삽입
print(df2.isnull())

print(df2.dropna(axis = 0)) # 결측치가 있는 행을 제거한다 1이면 열을 제거한다
print(df2)
print(df2.fillna(0)) # 결측치를 0으로 채워줌 다른 숫자넣으면 그 숫자로 채워준다

print(df2['Age'].fillna(df['Age'].mean)) # Age에 결측치가 있으면 Age의 평균값으로 채운다

print(df2.fillna(method='ffill')) #이전 버전
print(df2.ffill()) # 바로 위의(위 행) 값으로 결측치를 채움

print(df2.bfill()) # 바로 아래의(아래 행) 값으로 결측치를 채움





