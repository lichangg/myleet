#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 思路1. 暴力法也挺快的 76ms
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         res = [-1] * len(nums1)
#         for index1, item1 in enumerate(nums1):
#             start_index = nums2.index(item1)
#             for i in range(start_index+1, len(nums2)):
#                 if item1 < nums2[i]:
#                     res[index1] = nums2[i]
#                     break
#         return res

# 思路2.单调栈
# 因为反正num1是nums2的子集， 且都不含重复元素， 那就很好办，直接遍历num2就能找完所有数字右边第一个比它大的数
#  1. 遍历num2， 维护一个单调减的stack， 遇到更小的压入
#  2. 遇到更大的就循环弹出， 弹到stack[-1]更大，此时stack[-1]就是右边第一个比当前item大的数
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        dic, stack = {}, []

        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack: dic[nums2[i]] = stack[-1]
            stack.append(nums2[i])

        return [dic.get(x, -1) for x in nums1]

# 注意num1里面的元素nums2都有,且他们都没有重复元素,所以在选测试用例的时候要注意
a=Solution().nextGreaterElement([1,3,5],[6,5,8,3,6,1,7])
print(a)