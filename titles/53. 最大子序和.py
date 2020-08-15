#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 0
        max_sum = nums[0]
        sum = nums[0]
        for i in nums[1:]:
            if sum < 0:
                sum = i
            else:
                sum +=i
            max_sum = max(sum,max_sum)

        return max_sum

a=Solution().maxSubArray([-3,4,-1,2,1,-5,4])
print(a)