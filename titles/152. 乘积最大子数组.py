#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 由于存在负数，那么会导致最大的变最小的，最小的变最大的。因此还需要维护当前最小值imin
# 最小值相当于一直保存着一个可能变最大的一个数
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans, imax, imin = float("-inf"), 1, 1
        for i in nums:
            if i > 0:
                imax = max(imax * i, i)
                imin = min(imin * i, i)
            else:
                tmp = imax
                imax = max(i, imin * i)
                imin = min(i, tmp * i)
            ans = max(ans, imax)
        return ans




# 我真是吐了,留下了没有技术的泪水
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        print(nums)
        print(reverse_nums)
        return max(nums + reverse_nums)

a=Solution().maxProduct([-10,1,2,3,1,2,3,6])
print(a)