#!/usr/bin/env python
# -*- coding:utf-8 -*-
#效率太低超时了
class Solution:
    def threeSum(self, nums:list):
        res = []
        for index1, i in enumerate(nums):
            index2 = index1 + 1
            for _ in range(len(nums) - index1 - 1):
                if 0-i-nums[index2] in nums[index2+1:]:
                    temp = [i, nums[index2], 0 - i - nums[index2]]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
                index2 += 1

        return res

a=Solution().threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])
print(a)
# a=[0, 1, -1]
# a.sort()
# print(a)
