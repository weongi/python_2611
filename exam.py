# 문제 : `안녕하세요.`를 10번 출력해주세요.
print("안녕하세요.")
print("안녕하세요.")
print("안녕하세요.")
print("안녕하세요.")
print("안녕하세요.")
print("안녕하세요.")
print("안녕하세요.")
print("안녕하세요.")
print("안녕하세요.")
print("안녕하세요.")

print("=============================")

print("""
안녕하세요.
안녕하세요.
안녕하세요.
안녕하세요.
안녕하세요.
안녕하세요.
안녕하세요.
안녕하세요.
안녕하세요.
안녕하세요.
""")

print("=============================")

print("안녕하세요\n안녕하세요\n안녕하세요\n안녕하세요\n안녕하세요\n안녕하세요\n안녕하세요\n안녕하세요\n안녕하세요\n안녕하세요\n")

print("=============================")

print("안녕하세요\n" * 10)

print("=============================")

x = 10
y = 5

x  = y # x = 5 
y = 10 

print(x)
print(y)

print("=============================")

# 포맷팅  
print("x = ",x)
print("y = ",y)

print(f"x =  {x}")
print(f"y =  {y}")

print("x = {}".format(x))
print("y = {}".format(y))

print("=============================")

x = 10 
y = 5

z = y
y = x
x = z
print("x = ",x)
print("y = ",y)

print("=============================")

a = 10
b = 20 
print(str(a) + str(b))

print("=============================")

a = '3'
b = '6'
print(int(a)+ int(b))

print("=============================")

a = '3.1'
b = '6.1'
print(float(a)+ float(b))

print("=============================")

a = '3.1'
b = '6.1'
a = float(a)
b = float(b)
print(int(a)+ int(b))

print("=============================")

a = '3.1'
b = '6.1'
print(int(float(a))+int(float(b)))

print("=============================")

print("안녕")
input()
print("잘가")

print("=============================")

print("문장을 입력 해주세요 : ", end ="")
line = input()
print(line)

print("=============================")

line2 = input("문장을 입력해 : ")
print(line2)
print(line2.split(','))

print("=============================")

line3 = input("문장을 입력해랏 : ")
print(line3.strip())

print("=============================")

line4 = input().strip().split() # --> input하고 strip하고 split 순서대로 진행

print("=============================")

line5= map(int, input().strip().split(','))

print("=============================")




















