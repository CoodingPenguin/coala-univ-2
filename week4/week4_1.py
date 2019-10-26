singers = ['오마이걸', '러블리즈', '드림캐처', '우주소녀']
songs = ['불꽃놀이', '종소리', '데자부', '부탁해']

# 파일 열기 없으면 생성( 파일 이름, write/read/append )
f = open('hitsong.csv', 'w')


for i in range(len(singers)):
    print(singers[i])
    print(songs[i])

    # 파일에 출력
    f.write(singers[i] + ',' + songs[i] + '\n')

# 파일 닫아줌 (아니면 계속 돌아감)
f.close()