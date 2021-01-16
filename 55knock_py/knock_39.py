# split(文字を指定して文字列を分割)

# 空白で区切ってリスト化
lang = 'C C++ // python java'
print(lang.split())

# ,は空白ってことみたい
# .sprit()は何も指定しなければ『,』（空白）で区切ってリストで返す
# 

print(lang.split('/')) # => ['C C++ ', '', ' python java']
print(lang.split('p')) # => ['C C++ // ', 'ython java']
# 何を基準に分割するかを決める
