#!/usr/bin/env python
# -*- coding:utf-8 -*-
a = [4,0,1,9,-4]

def quick_sort(nums):
    l = 0
    r = len(nums)-1
    def s(nums, l, r):
        if l >= r:
            return
        while l<r and nums[r] >= nums[l]:
            r-=1
        nums[r], nums[l] = nums[l], nums[r]
        while l<r and nums[l] <= nums[r]:
            l+=1
        nums[r], nums[l] = nums[l], nums[r]
        s(nums, 0, l-1)
        s(nums, l+1, r)


    s(nums, l, r)
quick_sort(a)
print(a)





