pay = int(input('당신의 시급? : '))

if pay > 8350:
    print('최저시급보다 높습니다!')
else:
    print('최저시급보다 낮습니다!')

numbers = [1, 5, 2, 33, 5, 435, 21, 242]
for num in numbers:
    if num % 2 == 0 and num > 5:
        print(num)

articles = ['오마이걸 퀸덤', '우주소녀 인기가요 1위', '러블리즈 까메오 3차 강연 승리']

for a in articles:
    if '오마이걸' in a:
        print(a)