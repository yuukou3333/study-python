dic = {}
for i in range(1,31):
  if i%3 == 0:
    index = f"{i//3}番目"
    dic[index] = i

print(f"作成した辞書：{dic}")
