#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 虽然自己写的这个能过,但是好像不太合适
class Solution:
    def findMin(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0],nums[1])
        div, mod = divmod(len(nums), 2)
        left = nums[:div+1]
        right = nums[div+1:]

        res1=self.findMin(left)
        res2=self.findMin(right)
        return min(res1,res2)

a=Solution().findMin([8,1,2,3,4,5,6,7])
print(a)


