# aからbまでの総和を求める(for文)
print('aからbまでの総和を求めます。')

a = int(input('整数a：'))
b = int(input('整数b：'))

# aとbを昇順にソート
if a > b:
 a, b = b, a

sum = 0
for i in range(a, b + 1):
 sum += i

print(f'{a}から{b}までの総和は{sum}です')