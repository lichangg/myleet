#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 双指针的解法
# 执行用时：48 ms, 在所有 Python3 提交中击败了76.44%的用户
# 内存消耗：14.7 MB, 在所有 Python3 提交中击败了54.00%的用户
# class Solution:
#     def removeDuplicates(self, nums) -> int:
#         slow = 0
#         fast = 0
#         if not nums:
#             return 0
#         while fast<len(nums)-1:
#             fast +=1
#             if nums[slow] != nums[fast]:
#                 slow +=1
#                 nums[slow]=nums[fast]
#                 continue
#         for _ in range(fast-slow):
#             nums.pop()
#
#         print(nums)
#         return slow+1

#比较优雅一点,for直接代替了fast指针, 但是缺乏改数组的操作
class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        print(nums)
        return i + 1

a=Solution().removeDuplicates([1,2,3,3,3,4,5])
print(a)