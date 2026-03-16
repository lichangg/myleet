#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 暴力法先行,这样肯定会超时
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = []
        for i in range(l):
            count = 0
            for j in range(i+1,l):
                if nums[j]<nums[i]:
                    count +=1
            res.append(count)
        return res

# 此题和剑指offer51题极为类似，以后再看
a=Solution().countSmaller([5,2,6,1])
print(a)