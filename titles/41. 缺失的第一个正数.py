#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        cur_hasnt = set()
        while i < len(nums):
            if i != nums[i] and i not in cur_hasnt:
                cur_hasnt.add(i)
            if nums[i] not in
            if cur_hasnt == nums[i]:
                dp[i] = dp[i-1] + 1
            else:
                cur_hasnt = i
                dp[i] = dp[i - 1]
            i += 1

        return dp[-1]
a=Solution().firstMissingPositive([3,4,-1,1])
print()
