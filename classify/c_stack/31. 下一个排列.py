#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 我这思路牛逼,单调栈+快排
class Solution:
    def nextPermutation(self, nums) -> None:

        l = len(nums)
        stack = []
        lastpop = None
        i = l - 1
        while i >= 0:
            while stack and nums[stack[-1]] > nums[i]:
                lastpop = stack.pop()
            if lastpop:
                flg = i
                break
            stack.append(i)
            i -= 1
        if not lastpop:
            nums.sort()
        else:
            nums[lastpop], nums[flg] = nums[flg], nums[lastpop]

            self.quick_sort(nums, i+1, len(nums)-1)

            # tmp = nums[i + 1:]
            # tmp.sort()
            # nums[i + 1:] = tmp

    def quick_sort(self,nums, start, end):
        l = start
        r = end
        if l >= r:
            return
        while l < r:
            while l < r and nums[r] >= nums[l]:
                r -= 1
            nums[r], nums[l] = nums[l], nums[r]
            while l < r and nums[l] <= nums[r]:
                l += 1
            nums[r], nums[l] = nums[l], nums[r]
        self.quick_sort(nums, start, l - 1)
        self.quick_sort(nums, l + 1, end)


a = [5,4,7,5,3,2]
Solution().nextPermutation(a)
print(a)
