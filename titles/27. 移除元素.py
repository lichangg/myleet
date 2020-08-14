#!/usr/bin/env python
# -*- co|ding:utf-8 -*-
#
class Solution:
    def removeElement(self, nums, val: int) -> int:
        if not nums:
            return 0
        j=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j +=1
        for _ in range(len(nums)-j):
            nums.pop()
        return j

a=Solution().removeElement([1,2,2,3,4],3)
print(a)