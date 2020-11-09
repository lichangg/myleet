#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res_dic = {}
        for point in points:
            cur = point[0]**2 + point[1]**2
            res_dic[tuple(point)] = cur
        order_res_dic = sorted(res_dic.items(),key=lambda x:x[1])
        return [list(p) for p,v in order_res_dic[:K]]
a=Solution().kClosest(points = [[3,3],[5,-1],[-2,4]], K = 2)
print(a)
