print('일반계산기 프로그램입니다!')
first = int(input('계산할 첫번째 값을 입력해주세요 : '))
second = int(input('계산할 두번째 값을 입력해주세요 : '))

print('\n두 개의 값 : {0} 와 {1}'.format(first, second))

print('\n더하기 값 (a + b) :', first+second)
print('빼기 값 (a - b) :', first-second)
print('곱하기 값 (a * b) :', first*second)
print('정수 나누기 값 (a // b) :', first//second)
print('실수 나누기 값 (a / b) :', first/second)
print('나머지 값 (a % b) :', first%second)