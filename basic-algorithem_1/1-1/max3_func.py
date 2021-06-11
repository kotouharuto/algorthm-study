# 3つの整数値の最大値を求めて表示(関数で確認)
def max3(a, b, c):
 maximum = a
 if b > maximum:
  maximum = b
 if c > maximum:
  maximum = c
 return maximum

a = int(input('整数を入力してください：'))
b = int(input('整数を入力してください：'))
c = int(input('整数を入力してください：'))

maxnum = max(a, b, c)
print(f'3つの整数値の最大値は「{maxnum}」です。')