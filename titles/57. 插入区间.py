#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # 这就是56题的方法
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并，合并的操作中实际上只需要考虑索引为1的元素是两区间中最大的就行了，索引为0的元素由于初始进行了sort，所以不需要换
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)

a=Solution().insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])
print(a)


