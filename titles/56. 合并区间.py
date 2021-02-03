#!/usr/bin/env python
# -*- coding:utf-8 -*-
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# class Solution:
#     def merge(self, intervals):
#
#         intervals.sort(key=lambda x:x[0])
#         index = 0
#         while index<len(intervals)-1:
#             while 1 and index+1<=len(intervals)-1:
#                 if intervals[index][1] >=intervals[index+1][0]:
#                     intervals[index] = [min(intervals[index] + intervals[index+1]), max(intervals[index] + intervals[index+1])]
#                     intervals.remove(intervals[index+1])
#                 else:
#                     break
#             index+=1
#         return intervals

class Solution:
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


class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        i = 0
        while 1:
            if i > len(intervals) - 2:
                break
            if intervals[i][1] < intervals[i + 1][0]:
                i += 1
                continue
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i] = [intervals[i][0], max(intervals[i][1], intervals[i + 1][1])]
                intervals.pop(i + 1)
        return intervals

#
a = Solution().merge([[1,4],[4,5]])
print(a)
