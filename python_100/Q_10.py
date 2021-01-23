l = []
for i in range(1, 31):
    if i % 3 == 0 and '3' in str(i):
        l.append(i)

print(f'作成したリスト : {l}')
