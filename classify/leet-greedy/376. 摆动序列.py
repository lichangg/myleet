#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 思路一,动态规划
# 1. 前导:数组内部有连续相同的元素可视为只有一个, 另外:
#   - 设up[i]是以i之前某个元素nums[x]作为结尾,且到x时是上升的最长子序列长度
#   - 设down[i]是以i之前某个元素nums[x]作为结尾,且到x时是下降的最长子序列长度
# 2. 则状态转移方程:
#   - 对于up数组
#       - 当nums[i]<nums[i-1]时: up[i] = up[i-1]
#       - 当nums[i]>nums[i-1]时: up[i] = max(up[i-1], down[i-1]+1)
#   - 对于down数组
#       - 当nums[i]<nums[i-1]时: down[i] = max(up[i-1]+1, down[i-1])
#       - 当nums[i]>nums[i-1]时: down[i] = down[i-1]
# 3. 取max(up[i], down[i])作为结果
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        l = len(nums)
        up = [1] * l
        down = [1] * l
        for i in range(1, l):
            if nums[i]>nums[i-1]:
                up[i] = max(up[i-1], down[i-1]+1)
                down[i] = down[i-1]
            elif nums[i]<nums[i-1]:
                down[i] = max(up[i-1]+1, down[i-1])
                up[i] = up[i-1]
            else:
                down[i] = down[i-1]
                up[i] = up[i-1]
        return max(up[l-1], down[l-1])

# 思路2. 贪心
# 关键在于: “过渡元素” 是干扰项，可以跳过
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        prevdiff = nums[1] - nums[0]
        ret = (2 if prevdiff != 0 else 1)
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
                ret += 1
                prevdiff = diff

        return ret

a = Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
print(a)
