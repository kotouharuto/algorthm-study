# 1からnまでの総和を求める(while文)
print('1からnまでの総和を求めます。')
n = int(input('nの値：'))

sum = 0
i = 1

# while文は、繰り返しを続けるかどうかの判定を、処理実行の「前」に行うループ
while i <= n: # nが1以下の間繰り返す
 sum += i # sumにiの値を加える
 i += 1 # iに1を加える
print(f'1から{n}までの総和は{sum}です。')

# 1からnまでの総和を求める(for文のバージョン)
print('1からnまでの総和を求めます。')
n = int(input('nの値：'))

sum = 0
for i in range(1, n + 1):
 sum += i #sumにiを加える

print(f'1から{n}までの総和は{sum}です')