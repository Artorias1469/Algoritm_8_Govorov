#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])

    merged, inv_merge = merge_and_count(left, right)

    return merged, inv_left + inv_right + inv_merge

def merge_and_count(left, right):
    merged = []
    inversions = 0
    i = j = 0

    def merge():
        nonlocal i, j, inversions
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1

    def merge_remaining():
        nonlocal i, j
        merged.extend(left[i:])
        merged.extend(right[j:])

    while i < len(left) and j < len(right):
        merge()

    merge_remaining()

    return merged, inversions

if __name__ == "__main__":
    arr = [1, 3, 5, 2, 4, 6]
    sorted_arr, inversions = count_inversions(arr)

    print("Исходный массив:", arr)
    print("Количество инверсий:", inversions)
