# 総復習 =============================================

# li = list(range(23,56))
# for i in li:
#   print( "print(\" " + str(i) + ' ====================== \")')

# 23 存在確認 ======================
li = [11,22,33,44,55]
if 44 in li:
  print(True)
else:
  print(False)

# 24 タプル ======================
tuple = (li[0], li[-1])
print(tuple)
# 25 辞書 ======================
# 26 ======================
dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
print(list(dic.keys()))

print(" 27 ====================== ")
print(" 28 ====================== ")

print(list(dic.items()))

print(" 29 ====================== ")
d = {'apple':10, 'grape':20, 'orange':30}
d['apple'] = d.get('apple', -1)
d['painapple'] = d.get('painapple', -1)
print(d)

print(" 30 ====================== ")
str = 'training'
print(str[1:5])

print(" 31 ====================== ")

s = 'understand'
print(s[1::2])

print(" 32 ====================== ")
print(s[::-1])
print(" 33 集合 ====================== ")
print(" 34 ====================== ")
print(" 35 ====================== ")
print(" 36 ====================== ")
print(" 37  ====================== ")

data1 = {'A':1, 'B':2}
data2 = "hoge"
data3 = {1,2,3,4,5}

print(type(data1))
print(" 38 ====================== ")
print(" 39 ====================== ")
print(" 40 リストを文字列に ====================== ")

s_li = ['This', 'is', 'a', 'sentence' ]
print(' '.join(s_li))

print(" 41 ====================== ")
li = [11,2,7,13,5]
print(max(li))

print(" 42 ====================== ")
print(" 43 ====================== ")
print(" 44 sorted ====================== ")

sort_list = sorted(li)
print(sort_list)

li.sort()
print(li)

print(" 45 lambda ====================== ")

li = [{'a': 6, 'b': 7, 'c': 6},
      {'a': 4, 'b': 2, 'c': 3},
      {'a': 1, 'b': 5, 'c': 8}]

print(
  sorted(li, key=lambda x: x['b'], reverse=True)
)
# リストの中に辞書が入ってた時にソートするならlambdaとkeyとsortedの組み合わせ

print(" 46 ====================== ")
print(" 47 内包表記 ====================== ")

li = [5,4,3,2,1]
new_li = [ idx + elem for idx, elem in enumerate(li) ]
print(new_li)

print(" 48 例外処理====================== ")
a = 0
b = 5

try:
  print(a/b)
except ZeroDivisionError:
  print("zero division")

try:
  print(b/a)
except ZeroDivisionError:
  print("zero division")

print(" 49 ====================== ")
a = 10
b = 5

print(a|b, a&b, a^b)

print(" 50 ====================== ")
import math as m

theta = m.pi/2
print(m.sin(theta)**2 + m.cos(theta)**2)

print(" 51 for文のネスト ====================== ")

list1 = list(range(1,32))
list2 = list(range(1,13))
counter = 0
for elem1 in list1:
  for elem2 in list2:
    if elem1 % 10 == elem2 % 10:
      counter += 1
print(counter)

print(" 52 ====================== ")
dic = {'two':324, 'four':830, 'three':493, 'one':172, 'five':1024}
dic_items = list(dic.items())
sorted_list = sorted(dic_items, key=lambda x:x[1])
ans = [elem[0] for elem in sorted_list]
print(ans)


# 『list』は予約語だから絶対変数にするな！！！


print(" 53 ====================== ")
print(" 54 ====================== ")
print(" 55 ====================== ")

