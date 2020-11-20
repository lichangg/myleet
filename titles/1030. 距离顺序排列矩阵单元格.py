#!/usr/bin/env python
# -*- coding:utf-8 -*-
# sort(key=)这个方法是个好东西啊,一定要掌握
from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        points = [[i, j] for i in range(R) for j in range(C)]
        points.sort(key=lambda x:abs(x[0]-r0) + abs(x[1]-c0))
        return points

a = Solution().allCellsDistOrder(R = 2, C = 3, r0 = 1, c0 = 2)
print(a)
