# スライス2（stopを最後まで）

str = 'understand'
# print(str[:1])

# [a:]としてstopの値を記述しない時、処理をstopさせるindexは末尾になる。（正確には末尾＋１）
# つまり、最後まで取得することができる。

# 今回は奇数番目の値を取りたいので1から最後まで1個飛ばしで取得する。
print(str[1::2])

