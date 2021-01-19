#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 我吐了,放弃[1][2,3,4],[2][1,3,4]
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         count = 0
#         nums1_idx = nums2_idx=0
#         m = len(nums1)
#         n = len(nums2)
#         if m == 1 and n == 1:
#             return (nums1[0]+nums2[0])/2
#         if m == 0:
#             di, mod = divmod(n,2)
#             return nums2[di] if mod else (nums2[di-1] + nums2[di])/2
#         if n == 0:
#             di, mod = divmod(m,2)
#             return nums1[di] if mod else (nums1[di-1] + nums1[di])/2
#         di,mod = divmod(m+n,2)
#         while nums1_idx<m and nums2_idx<n:
#             if nums1[nums1_idx] < nums2[nums2_idx]:
#                 next_num = nums1[nums1_idx]
#                 nums1_idx+=1
#                 if count >=di:
#                     break
#             else:
#                 next_num = nums2[nums2_idx]
#                 nums2_idx+=1
#                 if count>=di:
#                     break
#             pre_num = next_num
#             count += 1
#         else:
#
#             if nums1_idx == m:
#                 if mod:
#                     return nums2[di-m]
#                 else:
#                     if di - m -1 >= 0:
#                         pre_num = nums2[di - m -1]
#                     return (nums2[di-m] + pre_num)/2
#             else:
#                 if mod:
#                     return nums1[di-n]
#                 else:
#                     if di - n -1 >= 0:
#                         pre_num = nums2[di - n -1]
#                     return (nums1[di-n] + pre_num)/2
#         if mod:
#             return next_num
#         else:
#             return (pre_num+next_num)/2




a=Solution().findMedianSortedArrays([2],[1,3,4])
print(a)