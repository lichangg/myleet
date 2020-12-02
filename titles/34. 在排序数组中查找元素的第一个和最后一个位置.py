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

# 二刷时直接被二分法的边界问题搞崩溃, 我总是想着mid由mid自己得到,但是可以直接通过头指针和尾指针得到,统一了逻辑就不会有问题
# 写的逻辑还是有点蠢
class Solution:
    def searchRange(self, nums, target: int):
        n = len(nums)
        first = 0
        last = n - 1
        flag = False
        while first <= last:
            mid = (last + first) // 2
            if nums[mid] > target:
                last = mid - 1
            elif nums[mid] < target:
                first = mid + 1
            else:
                flag = True
                start = end = mid
                # 此处的逻辑写的还是太蠢了, 好好看看上面那个方法的逻辑
                l = 1
                r = 1
                while l <= mid:
                    if nums[mid - l] == target:
                        start -= 1
                    l += 1
                while r <= n - 1 - mid:

                    if nums[mid + r] == target:
                        end += 1
                    r += 1
                break
        if flag:
            return [start, end]
        else:
            return [-1, -1]




# 三刷仍然是被二分法拦住, 我真是吐了
class Solution:
    def searchRange(self, nums, target: int):

        def mid_search(nums_c):
            left = 0
            right = len(nums_c) -1
            while left<=right:
                mid = (left+right)//2
                if nums_c[mid]<target:
                    left = mid+1
                elif nums_c[mid]> target:
                    right = mid-1
                else:
                    return mid

        mid_index = mid_search(nums)
        if mid_index==None:
            return [-1,-1]
        else:
            start = end = mid_index
            while start > 0:
                if nums[start-1] != nums[mid_index]:
                    break
                start -=1
            while end < len(nums)-1:
                if nums[end+1] != nums[mid_index]:
                    break
                end +=1

            return [start, end]

a = Solution().searchRange([1], 1)
print(a)