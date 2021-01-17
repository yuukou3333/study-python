# 演習4（word2freq）

doc = 'i bought an apple .\ni ate it .\nit is delicious .'
word2freq = {}

# 改行文字でsplit
sents = doc.split('\n')
# => ['i bought an apple .', 'i ate it .', 'it is delicious .']

for sent in sents:
  # 文章を単語ごとに分ける(リストに格納)
  words = sent.split()
  # => ['i', 'bought', 'an', 'apple', '.']
  #    ['i', 'ate', 'it', '.']
  #    ['it', 'is', 'delicious', '.']
  for word in words:
    word2freq[word] = word2freq.get(word, 0) +1

print(word2freq)
# => {'i': 2, 'bought': 1, 'an': 1, 'apple': 1, '.': 3, 'ate': 1, 'it': 2, 'is': 1, 'delicious': 1}

# 内包表記を使用
print(word2freq)
# 学び ===============================
# リストに対してsplitやreplaceは使えない。（Stringのメソッドのため）
