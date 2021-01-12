# 11/14：繰り返し

# =========================================

# for文 ================
  # for 変数 in range(繰り返す回数）:
  # 	繰り返したい処理
for i in range(5):
  print(i)

# break ================
for i in range(5):
  print(i)
  if i == 3:
    break
# => 0
#    1
#    2
#    3

for i in range(5):
  if i == 3:
    break
  print(i)
  # => 0
#    1
#    2

# continue ================
for i in range(5):
  if i == 3:
    continue
  print(i)
# => 0
#    1
#    2
#    3
#    4

# for文のネスト
print("============================")
for i in range(3):
  for j in range(3):
    print(i, j, sep="-")
print("============================")

# リストを格納
array = [2, 4, 6, 8]
sum = 0 #変数を定義
for i in array:
  sum += i #リストの中を全部足してる
  # sum = sum + i
  # 1→sum = 0+2 = 2    sum += 2
  # 2→sum = 2+4 = 6    sum += 4
  # 3→sum = 6+6 = 12   sum += 6
  # 4→sum = 12+8 = 20  sum += 8
print(sum) # => 20

# 実践   1/14から14/14を文字列として出力 ================
for i in range(15):
  if i == 0:
    continue
  print(f"{i}/14：")
