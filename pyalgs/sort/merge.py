# from typing import List, TypeVar

# TKey = TypeVar('TKey', int, float)

# def _merge_arrs(arr_a: List[TKey], arr_b: List[TKey]):
#   """"""
#   len_a, len_b = len(arr_a), len(arr_b)
#   i, j = 0, 0
#   arr = []
#   while i < len_a and j < len_b:
#     if arr_a[i] < arr_b[j]:
#       arr.append(arr_a[i])
#       i += 1
#     elif arr[i] >= arr_b[j]:
#       arr.append(arr_b[j])
#       j += 1
#   if i == len_a:
#     while j < len_b:
#       arr.append(arr_b[j])
#       j += 1
#   elif j == len_b:
#     while i < len_a:
#       arr.append(arr_a[i])
#       i += 1
#   return arr

# def merge(arr: List[TKey], p:int, r:int) -> List[TKey]:
#   """"""
#   if p < r:
#     q = (p+r)//2
#     arr_a = merge(arr, p, q)
#     arr_b = merge(arr, q + 1, r)
#     _merge_arrs(arr, p, q, r)