#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])

    merged, inv_merge = merge_and_count(left, right, 0, 0, [])

    return merged, inv_left + inv_right + inv_merge

def merge_and_count(left, right, i, j, merged):
    if i < len(left) and j < len(right):
        if left[i] <= right[j]:
            return merge_and_count(left, right, i + 1, j, merged + [left[i]])
        else:
            return merge_and_count(left, right, i, j + 1, merged + [right[j]]) + (len(left) - i,)
    else:
        return merged + left[i:] + right[j:], 0

if __name__ == "__main__":
    arr = [1, 3, 5, 2, 4, 6]
    sorted_arr, inversions = count_inversions(arr)

    print("Исходный массив:", arr)
    print("Количество инверсий:", inversions)
