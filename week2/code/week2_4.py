# 리스트 정의
players = ['황의조', '손흥민', '권창훈', '정우영', '백승호']
print(players)

# 리스트 인덱싱
print(players[0])
print(players[1])
print(players[2])

# 리스트 슬라이싱
print(players[1:3])

# append 메서드 : element 추가
players.append('김승규')
players.append('김민재')
print(players)

# insert 메서드 : 해당 index에 추가
players.insert(2, '이헌영')
print(players)

# del : element 제거
del players[4]
print(players)

