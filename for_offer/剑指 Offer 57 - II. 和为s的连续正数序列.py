#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        l = r = 1
        window = 0
        while r <= target:
            if window < target:
                window +=r
                r+=1
            elif window > target:
                window -=l
                l +=1
            else:
                res.append(list(range(l, r)))
                window -= l
                l+=1

        return res


a = Solution().findContinuousSequence(target=9)
print(a)
