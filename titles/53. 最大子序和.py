#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 学到了
# 思路:指针滑倒某个位置时,看看前面已经算好的和是不是小于0,小于0就是累赘就直接不要了
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

# 二刷，比之前简洁许多了
class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = float('-inf')
        i=0
        si=0
        while i< len(nums):
            if si <0:
                si=0

            si+=nums[i]
            max_sum = max(max_sum,si)
            i+=1
        return max_sum






a=Solution().maxSubArray([-3,4,-1,2,1,-5,4])
print(a)