#!/usr/bin/env python
# -*- coding:utf-8 -*-
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2) -> float:
# 找到两个数组合起来后第k小的数
def helper(nums1, nums2, k):
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1  # 保持nums1比较长
    if len(nums2) == 0:
        return nums1[k - 1]  # 短数组空，直接返回
    if k == 1:
        return min(nums1[0], nums2[0])  # 找最小数，比较数组首位
    t = min(k // 2, len(nums2))  # 保证不上溢
    if (nums1[t - 1] >= nums2[t - 1]):
        return helper(nums1, nums2[t:], k - t)
    else:
        return helper(nums1[t:], nums2, k - t)


num1 = [1, 2, 3, 4, 5, 6]
num2 = [1, 2, 3, 4, 5]

print(helper(num1, num2, 11))
