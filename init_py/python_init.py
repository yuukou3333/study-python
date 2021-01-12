# 5/14：Hello World 出力
# 6/14：変数とは
# 7/14：データ型
# 8/14：リスト
# 9/14：演算子
# 10/14：条件式

# =========================================

print("Hello World")

# =========================================
num = 1
print(num)

# 大文字小文字は区別される
Num = 2
print(Num)

# 予約語はダメ
# return = 3
# print(return)
# =========================================
# 数値型
num1 = 123
num2 = 1.23

print(type(num1))
print(type(num2))

# 文字列型
str = "Hello"
print(type(str))

# ブール型 Boolean型
a = 1
b = 2
bool = 2 > 1  
print(bool) # => True
print(type(bool)) # => <class 'bool'>

# =========================================
# リスト
list = ["sato", "suzuki", "takahashi"]
print(list)
print(list[0])

# 要素の変更
list[1] = "tanaka"
print(list)

# 多次元リスト
list_02 = [ ["sato", "suzuki"], ["takahashi", "tanaka"]]
print(list_02[0][1]) # => suzuki

# =========================================
# 演算子（代入演算子）
x = 10
y = 20

x = x+10
print(x) # => 20
x += 10
print(x) # => 30

x += y
print(x) # => 50

# =========================================
# 条件分岐
age = 0
if age >= 20:
  print("adult")
elif age == 0:
  print("baby")
else:
  print("child")
# =========================================


