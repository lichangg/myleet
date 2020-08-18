#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 若出现了新的高度且不以当前索引为起始索引的矩形就可以开始比较这两新矩形面积,若新矩形较大,则收缩窗口
# 若出现了新的高度且但是以当前索引为起始索引的矩形就只更新最大矩形
# 最矮的矩形和次矮的矩形
# 放弃,也不知道思路对不对
# class Solution:
#     def largestRectangleArea(self, heights) -> int:
#         l,r = 0,1
#         cur_max= 0
#         window_h = float('inf')
#         def window(left, right):
#
#         while 1:
#             while r<len(heights-1):
#                 if window_h!=heights[r]:
#
#                 window_h = min(window_h, heights[r])
#
#                 cur_max = max(heights[l]*(r-l),cur_max)
#                 r+=1

# 思路找到每一个索引向两侧扩散能得到的最大面积, 再在这些最大面积中取最大的
# 具体操作是以当前i为中心向左右分别找到第一个比heights[i]小的柱子索引,这样就保证了左右两极限索引中间的最大柱子始终为(right_i - left_i - 1) * heights[i]
class Solution:
    def largestRectangleArea(self, heights) -> int:
        res = 0
        n = len(heights)
        for i in range(n):
            left_i = i
            right_i = i
            while left_i >= 0 and heights[left_i] >= heights[i]:
                left_i -= 1
            while right_i < n and heights[right_i] >= heights[i]:
                right_i += 1
            res = max(res, (right_i - left_i - 1) * heights[i])
        return res

#单调堆栈,有空看看
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         stack = [-1]
#         max_res = 0
#         for i in range(len(heights)):
#             while len(stack) > 1 and heights[i] <= heights[stack[-1]]:
#                 max_res = max(max_res, heights[stack.pop()] * (i - stack[-1] - 1))
#             stack.append(i)
#         for i in range(len(stack)-1):
#             max_res = max(max_res, heights[stack.pop()]*(len(heights)-1-stack[-1]))
#         return max_res

a=Solution().largestRectangleArea([2,1,5,6,2,3])
print(a)