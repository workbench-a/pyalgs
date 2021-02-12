from typing import List, TypeVar

TKey = TypeVar('TKey', int, float)

def selection(arr: List[TKey]) -> List[TKey]:
  """"""
  for i in range(0, len(arr)):
    j = 0
    key = arr[i]
    while j < i:
      if arr[j] < key:
        j += 1
      elif arr[j] >= key:
        key = arr[j]
        arr[j] = arr[i]
        arr[i] = key
        j += 1
  return arr