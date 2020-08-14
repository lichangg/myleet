#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 还是二分查找的问题,只不过找到中间值后还需要向两边搜查
# 执行用时：36 ms, 在所有 Python3 提交中击败了92.09%的用户
# 内存消耗：14.7 MB, 在所有 Python3 提交中击败了16.58%的用户
# class Solution:
#     def searchRange(self, nums, target: int):
#         if not nums:
#             return [-1,-1]
#         start,end = 0, len(nums)-1
#         while start<=end:
#             mid = (end + start)//2
#             if target>nums[mid]:
#                 start = mid + 1
#             elif target<nums[mid]:
#                 end = mid-1
#             else:
#                 l=mid
#                 r = mid
#                 while l>0:
#                     if nums[l-1]!=target:
#                         break
#                     l-=1
#                 while r<len(nums)-1:
#                     if nums[r+1]!=target:
#                         break
#                     r+=1
#                 return [l,r]
#         return [-1,-1]




a=Solution().searchRange([],0)
print(a)