#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0
        i = 0
        res = []
        while i < l-1:

            if nums[i + 1] > nums[i]:
                i += 1
                continue
            res.append(i)
            n = i
            while n < l-1:
                if nums[n + 1] < nums[n]:
                    n += 1
                else:
                    break
            i = n
        if not res:
            return 0 if nums[-1]<nums[0] else l-1
        return res[0]

a = Solution().findPeakElement( [2,1])
print(a)
