# リスト（forによる捜査、enumerate）

# 自分の回答1 ====================================
# l = [1,2,3,4,5]
# for i in range(4):
#   if i%2 == 0:
#     print(l[i])

# enumerateを使うとforループの中でタプル型やリスト型のインデックスを取得できる
# for i, name in enumerate(l):
#     print(i, name)
# => 
# 0 Alice
# 1 Bob
# 2 Charlie

# 自分の回答2 ====================================
list = [1,2,3,4,5]
for i, ans in enumerate(list):
  if i%2 == 0:
    print(ans)

# for idx, elem in enumerate(list):
#   if 条件式
#     処理
# のようにして活用する。

# 2日後に解いた回答
li = [1,2,3,4,5]
for idx, elem in enumerate(li):
  if idx%2 == 0:
    print(elem)

# forの隣のidx, elemは順番に読まれるため、反対にしたら、出力は1,3になるため注意が必要

# 模範解答 ====================================
li = [1,2,3,4,5]
for idx, elem in enumerate(li):
    if idx % 2 == 0:
        print(elem)

# 要素はelem、インデックスはidxとしたら見やすい。

# 参考）
# Python, enumerateの使い方: リストの要素とインデックスを取得 https://note.nkmk.me/python-enumerate-start/
