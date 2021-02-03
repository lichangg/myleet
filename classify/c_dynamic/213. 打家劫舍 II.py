#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


# 题中的房间是单排排列的；而这也是此题的难点。
# 环状排列意味着第一个房子和最后一个房子中只能选择一个偷窃，因此可以把此环状排列房间问题约化为两个单排排列房间子问题：
# 1. 在不偷窃第一个房子的情况下（即 nums[1:]nums[1:]），最大金额是 p_1p
# 2. 在不偷窃最后一个房子的情况下（即 nums[:n-1]nums[:n−1]），最大金额是 p_2p

# 对于第一个房间来说，存在偷与不偷的情况，如果偷，则最后一家一定不能偷，将其置为0即可，以此数组为基准运行198题的代码得到一个结果。如果不偷，那么把第一家置为0，最后一家无所谓，运行198题代码，又得到一个结果。返回两个结果较大的一个即可。


# 分偷nums[1:]和nums[0:-1]两种情况
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        dp1 = [[0] * 2 for _ in range(n - 1)]
        nums1 = nums[:-1]
        dp2 = [[0] * 2 for _ in range(n - 1)]
        nums2 = nums[1:]
        for i in range(n - 1):
            dp1[i][0] = max(dp1[i - 1][1], dp1[i - 1][0])
            dp1[i][1] = dp1[i - 1][0] + nums1[i]

        for j in range(n - 1):
            dp2[j][0] = max(dp2[j - 1][1], dp2[j - 1][0])
            dp2[j][1] = dp2[j - 1][0] + nums2[j]

        return max(dp1[-1][0], dp1[-1][1], dp2[-1][0], dp2[-1][1])
a = Solution().rob(nums =[1,3,1,3,100])
print(a)
