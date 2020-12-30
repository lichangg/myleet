#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
import heapq
# 暴力法
# 执行用时：7244 ms, 在所有 Python3 提交中击败了5.06%的用户
# 内存消耗：16.4 MB, 在所有 Python3 提交中击败了5.24%的用户
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        count = 0
        set_index = set()
        for i in g:
            for index, j in enumerate(s):
                if j>=i and index not in set_index:
                    count +=1
                    set_index.add(index)
                    break

        return count

# 小根堆优化
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        count = 0
        hq = []
        for j in s:
            heapq.heappush(hq, -j)
        for i in g:
            if not hq:
                break
            if i<= -hq[0]:
                heapq.heappop(hq)
                count+=1
        return count

a=Solution().findContentChildren(g = [1,2,3], s = [1,1])
print(a)