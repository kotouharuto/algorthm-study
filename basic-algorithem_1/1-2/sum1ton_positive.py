# 1からnまでの総和を求める(nに正の整数値を読み込む)

print('1からnまでの総和を求める。')

while True:
 n = int(input('nの値：'))
 if n > 0:
  break

sum = 0
i = 1

for i in range(1, n + 1):
 sum += i
 i += 1

print(f'1から{n}までの総和は{sum}です。')