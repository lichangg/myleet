#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


# 直接双指针不就解决了么,我真是蠢啊
# 执行用时：40 ms, 在所有 Python3 提交中击败了85.63%的用户
# 内存消耗：14.3 MB, 在所有 Python3 提交中击败了76.43%的用户
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while j <= len(nums) - 1:
            if nums[j] == 0:
                j += 1
                continue
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        for x in range(i, len(nums)):
            nums[x] = 0


# 上面的方法虽然也是O(n)但是遍历了两次,实际上可以只遍历一次
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 0
        # 两个指针i和j
        j = 0
        for i in range(len(nums)):
            # 当前元素!=0，就把其交换到左边，等于0的交换到右边
            if nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


# 二刷其实是失败, 看了题解才写出来
class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                continue
            i += 1
            j += 1
        print(nums)


# 三刷
class Solution(object):
    def moveZeroes(self, nums):
        idx_0 = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[idx_0] = nums[i]
                idx_0 += 1
            i += 1
        for j in range(idx_0, len(nums)):
            nums[j] = 0
        return nums
b = [3, 0, 0, 1, 0, 3, 12]
a=Solution().moveZeroes(b)
print(a)
