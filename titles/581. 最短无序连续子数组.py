#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 适配失败，目前过不了[1,2,4,5,3]，放弃适配
# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         n = len(nums)
#         j = 0
#         max_num = float('-inf')
#         start = 0
#         start_flag = False
#         end = 0
#         i = 0
#         while j < n - 1:
#             max_num = max(max_num, nums[j])
# 
#             if nums[j] <= nums[j + 1] and nums[j + 1] >= max_num:
#                 if nums[j] != nums[j + 1]:
#                     i = j + 1
#                 j += 1
#                 continue
# 
#             if not start_flag:
#                 start = i
#                 start_flag = True
#             end = j + 1
#             j += 1
#         if not end:
#             return 0
#         return end - start + 1


b = [1,2,4,5,3]
a = Solution().findUnsortedSubarray(b)
print(a)
