# 辞書の値のソート

dic = {'two':324, 'four':830, 'three':493, 'one':172, 'five':1024}
# 辞書をitemsメソッドでキーと値をタプルにしてリスト化
items_list = list(dic.items())
# リストをソート。この時タプルの値の方をkeyとして昇順ソートする
sorted_items_list = sorted(items_list, key=lambda x:x[1])

# print(sorted_items_list)
# => [('one', 172), ('two', 324), ('three', 493), ('four', 830), ('five', 1024)]

# タプルの欲しい値だけを取得（リストから別のリストを作るので内包表記）
ans = [elem[0] for elem in sorted_items_list]
print(ans)
