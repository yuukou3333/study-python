# 演習1(for文のネスｔ)

li_1 = list(range(1,32))
li_2 = list(range(1,13))

counter = 0
for elem_1 in li_1:
  for elem_2 in li_2:
    # 1のくらいが正しいかどうかは10で割った余りを確認すれば良い
    if elem_1%10 == elem_2%10:
      counter += 1

print(counter)
