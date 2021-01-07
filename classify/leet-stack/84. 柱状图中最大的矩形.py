#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 思路1. 单调栈
# 1. 遍历数组并维护一个单调递增的栈stack, 遇到比stack[-1]大的数就压入
# 2. 遇到比stack[-1]小的数则进入循环pop,直到栈顶元素比当前的item小 (意思就是在到pop出的栈顶元素比item小之前,以pop出来的元素为高的矩形不可能扩张到item)
    # - 循环内以pop出的元素为高
    # - 以pop出的栈顶元素索引和item的索引距离为底
    # - 取max(cur_max,高乘底)
#   因为后pop的元素肯定比先pop的要小,所以pop到哪儿就以哪儿为高是肯定不会错的
# 3. 遍历结束后有可能会出现stack里面还有元素的情况. 这意思也就是在数组中索引大于stack内的索引的值不会比stack内的索引值更小了
#   - 遍历stack, 以height[当前索引值]值为高, len(height)-当前索引值为底, 算出面积
# 我吐了.总是错
# class Solution:
#     def largestRectangleArea(self, heights) -> int:
#         stack = [-1]
#         cur_max = float('-inf')
#
#         for index, item in enumerate(heights):
#             while len(stack)>1 and heights[stack[-1]]>=item:
#
#                 h_index = stack.pop()
#                 dis = index - h_index
#
#                 cur_max = max(cur_max, dis * heights[h_index])
#
#             stack.append(index)
#         # for i in range(len(stack)-1):
#         #     cur_max = max(cur_max, heights[stack.pop()]*(len(heights)-1-stack[-1]))
#         return cur_max



a=Solution().largestRectangleArea([5,4,1,2])
print(a)