#!/usr/bin/env python
# -*- coding:utf-8 -*-

def merge(n1, n2):
    tmp = []
    x = len(n1)
    y = len(n2)
    i = j = 0
    while i < x and j < y:
        while i < x and j < y and n1[i] <= n2[j]:
            tmp.append(n1[i])
            i += 1
        while i < x and j < y and n1[i] > n2[j]:
            tmp.append(n2[j])
            j += 1
    if i == x:
        tmp.extend(n2[j:])
    else:
        tmp.extend(n1[i:])
    return tmp


def merge_sort(nums):
    if len(nums)<=1:
        return nums
    mid = len(nums) // 2
    l = merge_sort(nums[0:mid])
    r = merge_sort(nums[mid:])
    res = merge(l, r)
    return res

a=merge_sort([8,9,7,2,79,2,4,8,1,87,1])
print(a)
