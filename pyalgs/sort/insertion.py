from typing import List, TypeVar

TKey = TypeVar('TKey', int, float)

def insertion(arr: List[TKey]) -> List[TKey]:
  """Implements insertion sort on a list of keys."""
  for i in range(1, len(arr)):
    key = arr[i]
    # insert key into the sorted subarray arr[0 ... j-1]
    j = i - 1
    while j > -1 and arr[j] > key:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key
  return arr