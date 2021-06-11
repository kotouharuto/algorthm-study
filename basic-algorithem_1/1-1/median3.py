# 3つの整数値を読み込んで中央値を求めて表示
def med3(a, b, c):
 if a >= b:
  if b >= c:
   return b
  elif a <= c:
   return a
  else:
   return c
 elif a > c:
  return a
 elif b > c:
  return c
 else:
  return b

print('3つの整数の中央値を求めます。')
a = int(input('整数aの値：'))
b = int(input('整数bの値：'))
c = int(input('整数cの値：'))

print(f'中央値は{med3(a, b, c)}です。')