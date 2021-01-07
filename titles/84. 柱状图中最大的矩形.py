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
# 学到了
# 思路找到每一个索引向两侧扩散能得到的最大面积, 再在这些最大面积中取最大的
# 具体操作是以当前i为中心向左右分别找到第一个比heights[i]小的柱子索引,这样就保证了左右两极限索引中间的最大柱子始终为(right_i - left_i - 1) * heights[i]
# 搞了半天这个方法是超时的,学到个屁
from typing import List


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


# 单调栈,有空看看
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_res = 0
        for i in range(len(heights)):
            while len(stack) > 1 and heights[i] <= heights[stack[-1]]:
                max_res = max(max_res, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        for i in range(len(stack)-1):
            max_res = max(max_res, heights[stack.pop()]*(len(heights)-1-stack[-1]))
        return max_res

# 二刷,暴力法, 会超出时间限制
class Solution:
    def largestRectangleArea(self, heights) -> int:
        max_area = 0
        if not heights: return 0

        def get_area(start, end):
            return min(heights[start:end + 1]) * (end - start + 1)

        for index, i in enumerate(heights):
            for j in range(index, len(heights)):
                max_area = max(max_area, get_area(index, j))
        return max_area

# 二刷,从每个柱子向两边扩散找到以该柱子为高的最大矩形, 夫再度O(N**2),还是超时
class Solution:
    def largestRectangleArea(self, heights) -> int:
        max_area = 0
        for index, i in enumerate(heights):
            l = r = index
            while l -1>= 0 and heights[l-1] >= i:
                l -= 1
            while r+1 < len(heights) and heights[r+1] >= i:
                r += 1
            max_area = max(max_area, i * (r - l + 1))
        # a=Solution().largestRectangleArea([2,1,5,6,2,3])
        return max_area


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        left_i = [0] * n
        right_i = [0] * n
        left_i[0] = -1
        right_i[-1] = n
        for i in range(1, n):
            tmp = i - 1
            while tmp >= 0 and heights[tmp] >= heights[i]:
                tmp = left_i[tmp]
            left_i[i] = tmp
        for i in range(n - 2, -1, -1):
            tmp = i + 1
            while tmp < n and heights[tmp] >= heights[i]:
                tmp = right_i[tmp]
            right_i[i] = tmp
        # print(left_i)
        # print(right_i)
        res = 0
        for i in range(n):
            res = max(res, (right_i[i] - left_i[i] - 1) * heights[i])
        return res


# 虽然代码不是这个题解的,但是思路是, 写的很好
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/bao-li-jie-fa-zhan-by-liweiwei1419/
# 主题思路仍然是遍历数组找到[以该值为高度的最大矩形面积], 之前的方式是左右指针向两边扩散, 相当于又遍历一遍,所以复杂度O(N**2)
# 既然目的是找到[以该值为高度的最大矩形面积], 以[2,1,5,6,2,3], 遍历到2时,尚且不知道以2为高度的最大矩形面积,但是遍历到1时就知道了(但是以1为高度的最大面积还是不知道的)
# 然后遍历到5(此时1,5都不知道), 再到6(1,5,6都不知道), 但是到2的时候(6可以弹出来, 因为它的max_area知道了, 5也可以弹出来, 但是1仍然是不知道的)
# 此种方式完美符合栈的结构, 所以可以结合单调栈优化(保持栈内最后一个元素始终是最大)
# 不过这里还存在栈内存索引还是存数据的问题, 存索引就好了
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        # 此处首尾添加0非常精妙
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            #print(stack)
            # 由于单调栈的特性, 处于stack最后一个位置的元素肯定是比其前面的元素都要大的, 在往后遍历的过程中,
            # 当找到了比该元素小的值时则可以说找到了以该元素的值为高度的最大矩形面积
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res

a = Solution().largestRectangleArea([2,1,5,6,2,3])
print(a)
