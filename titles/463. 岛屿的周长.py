#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 牛逼这思路
# 直接遍历，如果当前值为1，加4（四条边），如果左边有1，减2（两条边重合），上面有1，减2。
# 最后相加即可
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    res+=4
                    if i-1>=0 and grid[i-1][j]==1:
                        res-=2
                    if j-1>=0 and grid[i][j-1]==1:
                        res-=2
        return res

