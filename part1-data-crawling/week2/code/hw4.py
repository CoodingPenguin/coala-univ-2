def print_players(players):
    for p in players:
        print(p)

players = ['황의조', '황의찬', '구자철', '이재성', '기성용']

print('현재 경기 중인 선수 : ')
print_players(players)
print('-'*40)

idx = int(input('OUT 시킬 선수 번호 : '))
name = input('IN 할 선수 이름 : ')
print('-'*40)
del players[idx]
players.append(name)

print('교체 결과 : ')
print_players(players)