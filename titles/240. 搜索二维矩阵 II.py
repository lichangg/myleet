#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 学到了
# 矩阵一共四个特殊点, 选择一个合适的遍历起始点很重要
# 选左上角，往右走和往下走都增大，不能选, 其实是会增多判断次数, 不太合适
# 选右下角，往上走和往左走都减小，不能选, 其实是会增多判断次数, 不太合适
# 选左下角，往右走增大，往上走减小，可选
# 选右上角，往下走增大，往左走减小，可选
# 例如选左下为起始点, 指针只会往上或往右走复杂度为O(m+n)
# 假如现在选左下角做起点, 每次会选择走上还是走右.这就相当于是二叉搜索树了
class Solution:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True

        return False

# 暴力法的时间复杂度为O(mn),这样就没有用到矩阵已经排好了序的性质
# 更快的是可以对行进行二分法搜索,复杂度就降到了O(mlogn),暂时不知道怎么同时再用到列的排序

a = Solution().searchMatrix()
print(a)
