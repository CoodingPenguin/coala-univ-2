string1 = '브이넥 라이트 다운 베스트'
string2 = '    25,990원    '

print(string1)
print(string2)

# 문자열 인덱싱
print(string1[0])
print(string1[2])
print(string2[6])

# 문자열 인덱싱 : 뒤로 접근
print(string1[-1])
# print(string2[16])

# 문자열 슬라이싱
print(string1[0:3])
print(string1[-6:-4])
print(string1[:])

# replace 메서드 : 문자열 대체
string1 = string1.replace('라이트', '헤비')
print(string1)

# strip 메서드 : whitespace 제거
# string2 = string2.strip()
# print(string2)

# 불필요한 문자 없애기
# string2 = string2.replace(',', '')
# string2 = string2[:-1]

# chain rule: 연쇄적으로 하는 것
# 근데 보기 안 좋으니까 나눠서 보여주자
string2 = string2.strip().replace(',', '')[:-1]

string2 = int(string2)
print(string2 + 10000)