# 文字列を数値に

a = "34"
b = "43"
sum = int(a) + int(b)
print(sum)

# intメソッドは『,』『.』が文字列に入っているとValue Errorになるため、replace(',','')などで置き換える必要がある。
# Pythonで数字の文字列strを数値int, floatに変換 https://note.nkmk.me/python-str-num-conversion/
