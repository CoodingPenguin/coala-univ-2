MAX = 10

# for문
for i in range(1, MAX):
    print(i)
    print('반복하기')
print('끝1')

print("="*20)

for i in range(0, MAX, 3):
    print(i)
    print('반복하기')
print('끝2')

print("="*20)

players = ['황의조', '손흥민', '권창훈', '정우영', '백승호']

# range를 이용한 출력
for i in range(0, 5):
    print(players[i])

print("="*20)

for i in range(len(players)):
    print(players[i])

print("="*20)

# iterator를 활용한 출력
for i in players:
    print(i)