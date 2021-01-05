#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        max_discover = float('-inf')
        count = 0
        for mi,ma in intervals:
            if mi<max_discover:
                count+=1
                if ma<max_discover:
                    max_discover = ma

            else:
                max_discover = max(ma,max_discover)
        return count

a=Solution().eraseOverlapIntervals([])
print(a)
