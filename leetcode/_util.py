#!/usr/bin/env python3
import math
from typing import Optional, List
from functools import lru_cache


def build_heap(arr: List[int], n: int):
    for i in range(n // 2, 0, -1):
        heapify(arr, n, i)


def heapify(arr: List[int], n: int, i: int):
    while True:
        max_pos = i
        if i * 2 <= n and arr[i] < arr[i * 2]:
            max_pos = i * 2
        if i * 2 + 1 <= n and arr[max_pos] < arr[i * 2 + 1]:
            max_pos = i * 2 + 1
        if max_pos == i:
            break  # no swap, stop
        arr[i], arr[max_pos] = arr[max_pos], arr[i]
        i = max_pos


def heap_sort(arr: List[int], n: int):
    build_heap(arr, n)

    k = n
    while k > 1:
        arr[1], arr[k] = arr[k], arr[1]
        k -= 1
        heapify(arr, k, 1)


if __name__ == '__main__':
    arr1 = [0]
    heap_sort(arr1, 0)
    assert arr1 == [0]

    arr1 = [0, 1]
    heap_sort(arr1, 1)
    assert arr1 == [0, 1]

    arr1 = [0, 5, 2]
    heap_sort(arr1, 2)
    assert arr1 == [0, 2, 5]

    arr1 = [0, 9, 6, 3, 1, 5]
    heap_sort(arr1, 5)
    assert arr1 == [0, 1, 3, 5, 6, 9]
