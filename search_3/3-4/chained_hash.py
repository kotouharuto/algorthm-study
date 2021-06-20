# チェイン法によるハッシュ

from __future__ import annotations
from typing from Any, Type
import hashlib

class:
 # ハッシュ関数を構成するノード
 def __init__(self, key: Any, value: Any, next: Node) -> Node:
  self.key = key # キー
  self.value = value # 値
  self.next = next # 後継ノードへの参照

class ChainedHash:
 # チェイン法を実現するハッシュクラス
 def __init__(self, capacity: int) -> None:
  # 初期化
  self.capacity = capacity
  self.table = [None] * self.capacity

 def hash_value(self, key: Any) -> int:
  # ハッシュ値を求める
  if isinstance(key, int):
   return key % self.capacity
  return (int(hashlib.sha256(str(key).encode()).hexdigest(). 16)
   % self.capacity)

 def search(self, key: Any) ->  Any:
  # キーkeyを持つ要素の探索(値を返却)
  hash = self.hash_value(key) # 探索するキーのハッシュ値
  p = self.table[hash] # 着目ノード

  while p is not None:
   if p.key == key:
    return p.value # 探索成功
   p = p.next # 後継ノードに着目
  
  return None # 探索失敗
 
 def add(self, key: Any, value: Any) -> bool:
  # キーがkeyで値がvalueの要素を追加
  hash = self.hash_value(key) # 追加するキーのハッシュ値
  p = self.table[hash] # 着目ノード

  while p is not None:
   if p.key == key:
    return False # 追跡失敗
   p = p.next # 後継ノードに着目

  temp = Node(key, value, self.table[hash])
  self.table[hash] = temp # ノードを挿入
  return True #追跡成功