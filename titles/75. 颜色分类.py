#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用了一个hashmap记录当前指针的数对应应该放在哪个索引,另外还涉及到数值两两交换时存在的特殊情况
# 执行用时：48 ms, 在所有 Python3 提交中击败了22.56%的用户
# 内存消耗：13.6 MB, 在所有 Python3 提交中击败了74.38%的
# 没想到一刷的时候我就能想出来这么厉害的方式
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = {0: 0, 1: 0, 2: 0}
        for index, i in enumerate(nums):

            if i == 0:
                nums[index], nums[hashmap[0]] = nums[hashmap[0]], nums[index]
                # 这个是特殊的
                if nums[index] == 1:
                    nums[index], nums[hashmap[1]] = nums[hashmap[1]], nums[index]
                hashmap[0] += 1
                hashmap[1] += 1
                hashmap[2] += 1
            elif i == 1:
                nums[index], nums[hashmap[1]] = nums[hashmap[1]], nums[index]
                hashmap[1] += 1
                hashmap[2] += 1
            else:
                nums[index], nums[hashmap[2]] = nums[hashmap[2]], nums[index]
                hashmap[2] += 1
        print(nums)


Solution().sortColors([1,0,2, 0, 2, 1, 1, 0,1])
