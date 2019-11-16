birth = input('생년월일을 6자리로 입력해주세요. (yymmdd) : ')
print('-'*40)
print('당신의 생일은 {0}년{1}월{2}일입니다.'.format(birth[:2], birth[2:4], birth[4:]))