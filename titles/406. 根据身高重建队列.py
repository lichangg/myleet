#!/usr/bin/env python
# -*- coding:utf-8 -*-
#首先要记得一点，高的人不会受低的人影响，所以优先处理高的人，排序完后，按从高到低和优先级处理，先处理高的并且序号小的，序号便是插入的位置
# 还是有点难想
from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for i in people:
            res.insert(i[1], i)
        return res


a=Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2],[8,3]])

print(a)