#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


# 合并区间类题目,此题本质还是求交集,有两种思路
# 1.  可以思考如果按左端排序会出现这种状况 [[0, 9], [0, 6], [7, 8]]
# 此时开始遍历, 发现[0,9]包含了[0,6],然后还继续往后包含了[7,8],你以为能一箭三雕, 但是不行,因为[0,6]和[7,8]无交集,所以裂开
# 但是如果还右端断续, 就会是[[0,6][7,8][0,9]]若当前区间和下个区间没有交集,则箭数+1
# 所以按右端排序
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        count = 1
        cur = points[0]
        index = 1
        while index<len(points):
            if cur[1]<points[index][0]:
                cur = points[index]
                count+=1
            index+=1
        return count

# 思路2: 其实也是可以按左端排序的, 毕竟反正是求交集, 更新一下当前区间就行,这样貌似会慢一点点
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[0])

        count = 1
        cur = points[0]
        index = 1
        while index<len(points):
            conmon = [max(cur[0],points[index][0]), min(cur[1],points[index][1])]
            if conmon[0]>conmon[1]:
                count+=1
                cur = points[index]
            else:
                cur = conmon
            index+=1
        return count
a = Solution().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])
print(a)
