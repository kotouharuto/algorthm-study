# 非負の整数の階上値を求める

def factorial(n: int) -> int:
 # 非負の整数nの階上を再帰的に求める
 if n > 0:
  return n * factorial(n - 1)
 else:
  return 1

if __name__ == '__main__':
 n = int(input('何の階上：'))
 print(f'{n}の階上は{factorial(n)}です。')