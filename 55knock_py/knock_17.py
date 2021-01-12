# リスト（結合）

li1 = [1,2,3]
li2 = [4,5]
sum_li = li1 + li2
print(sum_li)

# extend(list)でも足せる。
# 例
li1.extend(li2)
print(li1)

# このときprint(li1.extend(li2))とするとNoneになるので注意。
