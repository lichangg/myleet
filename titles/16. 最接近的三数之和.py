#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 自己写得双指针,结合三数之和的双指针思想, 效率比较低 但是好像别人写的也没好多少,反正都是O(n^2)
# 执行用时：152 ms, 在所有 Python3 提交中击败了32.48%的用户
# 内存消耗：13.8 MB, 在所有 Python3 提交中击败了7.17%的用户
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        mymin = abs(target - nums[0] - nums[1] - nums[2])
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l=i+1
            r = len(nums) - 1
            while l < r:
                if target - (nums[i] + nums[l] + nums[r]) == 0:
                    res = target
                    return res

                elif target - (nums[i] + nums[l] + nums[r]) > 0:
                    if mymin > abs(target - nums[i] - nums[l] - nums[r]):
                        mymin = abs(target - nums[i] - nums[l] - nums[r])
                        res = nums[i] + nums[l] + nums[r]
                    l+=1
                else:
                    if mymin > abs(target - nums[i] - nums[l] - nums[r]):
                        mymin = abs(target - nums[i] - nums[l] - nums[r])
                        res = nums[i] + nums[l] + nums[r]
                    r-=1

        return res
a=Solution().threeSumClosest([-1,2,1,-4],1)
print(a)