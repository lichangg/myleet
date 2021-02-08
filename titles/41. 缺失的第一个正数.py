#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 终极土办法
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        n = 0
        while i < len(nums):
            if nums[i] < 1:
                i += 1
                continue
            if i != 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            if n + 1 != nums[i]:
                return n + 1

            n += 1
            i += 1
        else:
            return n + 1

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        nums = set(nums)
        set_nums = set(nums)
        if len(set_nums)== 1 and set_nums.pop() == 1:
            return 2
        i = 0

        while i < len(nums):
            if i+1 not in set_nums:
                return i+1
            else:
                i+=1
        else:
            return i+1


# 置换可满足空间O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            # 只有在(1,n)范围的数才有可能有用且它的正确位置索引需要是它的值-1, 其他范围内的数没用的, 另外还得满足即将交换的两个数不相等,相等会进入死循环
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

print(a)
