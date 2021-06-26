# 固定長スタッククラス

from typing import Any

class FixedStack:
 # 固定長スタッククラス

 class Empty(Exception):
  # 空のFixedStackに対してpopあるいはpeekが呼び出された時に送出する例外
  pass

 class Full(Exception):
  # 満杯のFixedStackに対してpashが呼び出された時に送出する例外
  pass

 def __init__(self, capacity: int = 256) -> None:
  # 初期化
  self.stk = [None] * capacity # スタックの本体
  self.capacity = capacity
  self.ptr = 0

 def __len__(self) -> int:
   # スタックに積まれているデータ数を返す
   return self.ptr

 def is_empty(self) -> bool:
  # スタックはからであるかどうか
  return self.ptr <= 0

 def is_full(self) -> bool:
  # スタックは満杯か
  return self.ptr >= self.capacity

 def push(self, value: Any) -> None:
  # スタックにvalueをプッシュ
  if self.is_full():
   raise FixedStack.Full # raiseは送出
  self.stk[self.ptr] = value
  self.ptr += 1

 def pop(self) -> Any:
  # スタックからデータをポップ(頂上のデータを取り出す)
  if self.is_empty():
   raise FixedStack
  self.ptr -= 1
  return self.stk[self.ptr]

 def peek(self) -> Any:
  # スタックからデータをピーク(頂上のデータを覗き見)
  if self.is_empty():
   raise FixedStack.Empty
  return self.stk[self.ptr - 1]

 def clear(self) -> None:
  # スタックを空にする(全要素の削除)
  self.ptr = 0

 def find(self, value: Any) -> Any:
  # スタックからvalieを探して添字(見つからなければ-1)を返す
  for i in range(self.ptr -1, -1, -1): # 頂上側から線形探索
   if self.stk[i] == value:
    return i # 探索成功
  return -1 # 探索失敗

 def count(self, value: Any) -> bool:
  # スタックに含まれるvalueの個数を返す
  c = 0
  for i in range(self.ptr): # 底側から線形探索
   if self.stk[i] == value:
    c += 1 # 入っている
 def __contains__(self, value: Any) -> bool:
  # スタックにvalueは含まれているか
  return self.count(value)

 def dump(self) -> None:
  # ダンプ(スタック内の全データを底->頂上の順に表示)
  if self.is_empty():
   print('スタックは空です。')
  else:
   print(self.stk[:self.ptr])

 