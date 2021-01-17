# 演習5（Jaccard係数）

# Jaccard係数・・・集合A,Bの類似度を計算する方法
# Jaccard(A,B)=|A∩B|/|A∪B|=AとBの積集合の要素数/AとBの和集合の要素数

list1 = [12,23,34,45,56,67,78,89]
list2 = [21,32,43,45,65,67,78,98]

set1 = set(list1)
set2 = set(list2)

inter_set_len = len(set1 & set2)
union_set_len = len(set1 | set2)

ans = inter_set_len/union_set_len
print(ans)

# A.intersection(B) == A | B
# A.union(B) == A & B

