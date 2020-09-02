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

# 虽然这只是一道简单题,但是多看看评论区的题解, 能学的东西挺多的

# 这个算法背后的思想是无序子数组中最小元素的正确位置可以决定左边界，最大元素的正确位置可以决定右边界。
# 双指针同时从左右两端扫描全数组,寻找上界和下界,学到了,时间O(N),空间O(1)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 1:
            return 0

        left = size - 2
        right = 1
        cur_min = nums[-1]
        cur_max = nums[0]
        up = 0
        down = 1

        # 由于两个指针迭代的步数是相同的，所以没必要分两次循环，在一次循环里同时移动两次指针即可。
        while left >= 0 and right < size:
            if nums[left] > cur_min:
                down = left
            else:
                cur_min = nums[left]
            if nums[right] < cur_max:
                up = right
            else:
                cur_max = nums[right]
            left -= 1
            right += 1

        return up - down + 1



b = [1, 2, 3,3,3,2, 5]
a = Solution().findUnsortedSubarray(b)
print(a)
