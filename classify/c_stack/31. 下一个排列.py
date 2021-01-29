#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def nextPermutation(self, nums) -> None:

        l = len(nums)
        stack = []
        lastpop = None
        i = l-1
        while i>=0:
            while stack and nums[stack[-1]]>nums[i]:
                lastpop = stack.pop()
            if lastpop:
                flg = i
                break
            stack.append(i)
            i -=1
        if not lastpop:
            nums.sort()
        else:
            nums[lastpop], nums[flg] = nums[flg], nums[lastpop]
            tmp = nums[i+1:]
            tmp.sort()
            nums[i+1:] = tmp





a=[9,8,7]
Solution().nextPermutation(a)
print(a)

