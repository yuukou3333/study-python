# 例外処理（try/except）

a = 0
b = 5

try:
  print(a/b)
except:
  print('zero division')

try:
  print(b/a)
except:
  print('zero division')

# 例外処理 ======================
# try:の下には行いたい処理を、
# except:の下にはraiseしたい回避策を。


# division・・・分け目
# except・・・例外
