#!/usr/bin/env python
# -*- coding:utf-8 -*-
#自己写的实在太慢了, 又是找旋转点,又是二分查找的
# 执行用时：60 ms, 在所有 Python3 提交中击败了5.29%的用户
# 内存消耗：13.8 MB, 在所有 Python3 提交中击败了52.01%的用户
# class Solution:
#     def search(self, nums,target: int) -> int:
#         if not nums:
#             return -1
#         def findMin(nums) -> int:
#             if len(nums) == 1:
#                 return nums[0]
#             if len(nums) == 2:
#                 return min(nums[0], nums[1])
#             div, mod = divmod(len(nums), 2)
#             left = nums[:div + 1]
#             right = nums[div + 1:]
#
#             res1 = findMin(left)
#             res2 = findMin(right)
#             return min(res1, res2)
#
#         min_num = findMin(nums)
#         minindex = nums.index(min_num)
#         def middle_search(nums, target):
#             first  = 0
#             last = len(nums)-1
#             while first <= last:
#                 mid = (last + first) // 2
#                 if target > nums[mid]:
#                     first = mid+1
#                 elif target < nums[mid]:
#                     last = mid-1
#                 else:
#                     return mid
#
#             return -1
#         if minindex == 0:
#             return middle_search(nums,target)
#
#         if nums[0]>target:
#             sub  = nums[minindex:]
#
#             middle_index = middle_search(sub, target)
#             return -1 if middle_index == -1 else middle_index + minindex
#         elif nums[0] < target:
#             sub = nums[:minindex]
#
#             middle_index = middle_search(sub, target)
#             return -1 if middle_index == -1 else middle_index
#
#         else:
#             return 0

# 此处的二分法比较巧妙, 因为即便排序数组是经过旋转了的,在二分点处仍然是要么左边有序要么右边有序,
# 接下来需要利用有序的的一边来判断target是在左还是右
# 不过效率仍然慢....
# 执行用时：56 ms, 在所有 Python3 提交中击败了5.29%的用户
# 内存消耗：13.9 MB, 在所有 Python3 提交中击败了22.67%的用户
class Solution:
    def search(self, nums, target: int) -> int:
        left , right = 0 , len(nums) - 1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

a=Solution().search([1,3], 3)
print(a)