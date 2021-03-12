#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


# 这种暴力法虽然好想，但是会超时
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        l = len(nums)
        self.count = 0
        for i in range(l):
            for j in range(i + 1, l):
                if nums[i] > nums[j]:
                    self.count += 1
        return self.count


# 利用归并排序， 分的时候什么都不用做，合的时候计算逆序对，此题和315题几乎一模一样
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0

        def merge(left, right):
            if not left or not right: return left or right
            len_l = len(left)
            len_r = len(right)
            tmp = []
            l, r = 0, 0
            while l < len_l and r < len_r:
                while l < len_l and r < len_r and left[l] <= right[r]:
                    if l - len(tmp) > 0:
                        self.count += l - len(tmp)
                    tmp.append(left[l])
                    l += 1
                while r < len_r and l < len_l and right[r] < left[l]:
                    if len_l + r - len(tmp) > 0:
                        self.count += len_l + r - len(tmp)

                    tmp.append(right[r])
                    r += 1
            tmp += left[l:]
            tmp += right[r:]
            return tmp

        def split(nums):
            if len(nums) <= 1:
                return nums
            size = len(nums)
            mid = size // 2
            left = split(nums[:mid])
            right = split(nums[mid:])
            return merge(left, right)
        split(nums)
        return self.count


a = Solution().reversePairs([1,3,2,3,1])
print(a)
