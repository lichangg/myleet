#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 以为和84题差不多,都是从当前坐标出发扩散,只不过从左右两个方向扩大到了上下左右四个方向, 结果裂开,不能这样搞
# class Solution:
#     def maximalRectangle(self, matrix) -> int:
#         max_area = 0
#         n = len(matrix)
#         m = len(matrix[0])
#         for i in range(n):
#             for j in range(m):
#                 left, right, up, down = (i, j), (i, j), (i, j), (i, j)
#                 while left[1] >= 0 and int(matrix[left[0]][left[1]]) > 0:
#                     left = (left[0], left[1] - 1)
#
#                 while right[1] < m and int(matrix[right[0]][right[1]]) > 0:
#                     right = (left[0], right[1] + 1)
#
#                 while up[0] >= 0 and int(matrix[up[0]][up[1]]) > 0:
#                     up = (up[0] - 1, up[1])
#
#                 while down[0] < n and int(matrix[down[0]][down[1]]) > 0:
#                     down = (down[0] + 1, down[1])
#                 max_area = max(max_area, (right[1] - left[1] - 1) * (down[0] - up[0] - 1))
#         return max_area

# 学到了
# 可将此题转换为84题, 真是精妙啊,
# 步骤:将每一层与之前层聚合转化成84题中的输入
# 聚合注意事项,当前层和当前层往上都是1则叠加,当前层为0则为0表示该列不可用
# 另外要注意的就是需遍历每一层得到每一层的最大面积,最后一层的面积不一定是最大的
# 将
# 例如输入
#               ["1","0","1","0","0"]
#               ["1","0","1","1","1"]
#               ["1","1","1","1","1"]
#               ["1","0","0","1","0"]
# 可以观察发现到
# 第一层柱状图的高度["1","0","1","0","0"]，最大面积为1；
# 第二层柱状图的高度["2","0","2","1","1"]，最大面积为3；
# 第三层柱状图的高度["3","1","3","2","2"]，最大面积为6；
# 第四层柱状图的高度["4","0","0","3","0"]，最大面积为4；
class Solution:
    # 该方法即是84题的方法
    def largestRectangleArea(self, heights):
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
    def maximalRectangle(self, matrix) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        temp = [[ 0 for x in range(n)] for y in range(m) ]
        for i in range(m):

            for j in range(n):
                if matrix[i][j] != '0':
                    temp[i][j] = temp[i-1][j] + 1 if i >0 else 1
                else:
                    temp[i][j] = 0
        max_area = 0
        for l in temp:
            area = self.largestRectangleArea(l)
            max_area = max(max_area, area)
        return max_area
b = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "0", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
# b=[
#     ["1", "0", "1"],
#     ["1", "0", "1"],
# ]
a = Solution().maximalRectangle([[1]])
print(a)
