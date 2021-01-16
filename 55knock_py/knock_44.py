# 昇順ソート(sorted())

# 非破壊的なsorted() 組み込み関数
print('sorted ========================= \n')

li = [5,3,1,4,2]
print(sorted(li))
print(li)
# 降順にしたいなら第一引数にシーケンス、第二引数にreverse=Trueを入れる
print(sorted(li, reverse=True))

# 破壊的なsort リスト型のメソッド ========================
print('sort ========================= \n')
# 文字列やタプルなどには使えない
li.sort()
# .sort()が返すのはNoneなので注意。処理が終わってから使う。
print(li)
print(li.sort()) # => None
# 降順はsortの引数にreverse=Trueを入れる
li.sort(reverse=True)
print(li)
