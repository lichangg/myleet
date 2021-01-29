#!/usr/bin/env python
# -*- coding:utf-8 -*-
a = [2,4,3,7]

def quick_sort(nums,start, end):
    l = start
    r = end
    if l >= r:
        return
    while l< r:
        while l<r and nums[r] >= nums[l]:
            r-=1
        nums[r], nums[l] = nums[l], nums[r]
        while l<r and nums[l] <= nums[r]:
            l+=1
        nums[r], nums[l] = nums[l], nums[r]
    quick_sort(nums, start, l-1)
    quick_sort(nums, l+1, end)


quick_sort(a, 0, len(a)-1)
print(a)





