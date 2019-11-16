# 변수는 값을 담는 그릇
a = 'Hello World!'  # 문자열
b = 3               # 정수
c = -11             # 정수

print(a)
print(b)
print(c)

# 출력 시 ,로 띄어쓰기 가능
print(a, b, c)
print(b+c)

# 변수 가지고 연산 가능
d = b - c
print(d)

# 문자열로 +연산 가능
a = 'hello '
b = 'world!'
c = a + b
print(c)

# 문자열로 *연산 가능
a = 'aaaaa! '
print(a*3)

# 숫자랑 문자열 결합 시 error남
# str로 변환해줘야함
a = 1000
b = '원'
a = str(a)
print(a+b)

# Ctrl+/ : 전부 주석 처리