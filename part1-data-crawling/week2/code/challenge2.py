data = ['조회수: 1,500', '조회수: 1,002', '조회수: 300', '조회수: 251', '조회수: 13,432', '조회수: 998']
sum = 0

print("[Level 1]")
for i in data:
    print(i)
print("="*30)

print("[Level 2]")
data_int = []
for i in data:
    num = i[5:].replace(',', '')
    data_int.append(int(num))
    print(num)
print("="*30)

print("[Level 3]")
for i in data_int:
    sum += i
    print(i)
print('총 합 : ', sum)