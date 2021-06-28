# ボトムアップ解析

def recur2(n: int) -> int:
 if n > 0:
  recur2(n - 2)
  print(n)
  recur2(n - 1)

x = int(input('整数を入力してください：'))

recur2(x)