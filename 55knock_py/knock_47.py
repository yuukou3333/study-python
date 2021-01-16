# 内包表記
li = [5,4,3,2,1]

new_li = [idx + elem for idx, elem in enumerate(li)]
print(new_li)

# 内包表記とはあるリストから別のリストを作る時に使われる。
# forを三項演算子風にかいてリストに格納するような形にするとできる
# [繰り返したい処理 for elem in list]
