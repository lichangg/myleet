#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


# 思路1.
# 这题很自然先想到单调增栈，但是用一个栈很难做，因为这一个栈只能找到左边界， 并不能找到右边界，所以还需要一个递减栈找到右边界
# 需要特别注意的点是在确定左右边界的时候和以往不同，需要找到弹出过的数值（即索引）中的最小值（左边界用最小）和最大值（右边界用最大）
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        l = len(nums)-1
        for index, item in enumerate(nums):
            while stack and item < nums[stack[-1]]:
                l = min(l, stack.pop())
            stack.append(index)
        stack = []
        r = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                r = max(r, stack.pop())
            stack.append(i)
        if r>l:return r-l+1
        if r<=l:return 0


# 这个思路也蛮有意思的
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/si-lu-qing-xi-ming-liao-kan-bu-dong-bu-cun-zai-de-/

a = Solution().findUnsortedSubarray([2,1])
print(a)
