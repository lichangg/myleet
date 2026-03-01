#!/usr/bin/env python
# -*- coding:utf-8 -*-


def func(nums, n):
    size = len(nums)
    remain = n
    l=r = 0
    min_val = remain
    # 这个退出循环的条件还蛮怪的
    while r<size or remain <= 0:
        if remain >0:
            min_val = min(min_val, remain)
            remain -= nums[r]
            r +=1
        elif remain < 0:
            remain += nums[l]
            l +=1
        else:
            return 0
    return min_val

print(func(nums=[7,1,3,2],n=12))