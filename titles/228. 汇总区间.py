#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 执行用时：40 ms, 在所有 Python3 提交中击败了67.93%的用户
# 内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.17%的用户
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:return []
        res = []
        start = 0
        for i in range(len(nums)):
            if start >= i and start != 0:
                continue
            start = i
            temp = [nums[start]]
            while start <= len(nums) - 2 and nums[start] + 1 == nums[start + 1]:
                temp.append(nums[start + 1])
                start += 1
            if len(temp) == 1:
                str_temp = str(temp[0])
            else:
                str_temp = str(temp[0]) + '->' + str(temp[-1])
            res.append(str_temp)
        return res


a = Solution().summaryRanges([-1])
print(a)
