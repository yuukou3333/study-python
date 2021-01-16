# join

s_li = ['This', 'is', 'a', 'sentence']
sent = ' '.join(s_li)
print(sent)

# ' '.join(list)はリストの要素を結合することができる
# joinの前の、' 'では結合文字を指定できる。今回は空白を用いている。

sent_2 = ''.join(s_li)
print(sent_2)
# => Thisisasentence


