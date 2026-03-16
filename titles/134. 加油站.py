#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 该题有个推论:
# 总加油量>=总耗油量一定有解,反之一定无解
from typing import List


# 一刷, 暴力法
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def func(n):
            remain = 0
            j = n
            while j < len(gas):
                remain += gas[j]
                if remain >= cost[j]:
                    remain -= cost[j]
                    j += 1
                else:
                    return
            i = 0
            while i < n:
                remain += gas[i]
                if remain >= cost[i]:
                    remain -= cost[i]
                    i += 1
                else:
                    return
            return n

        for idx in range(len(gas)):
            if func(idx) != None:
                return idx
        else:
            return -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        i = 0
        while i < l:
            acc = gas[i]
            n = i
            while acc >= cost[n]:
                acc -= cost[n]
                n += 1
                if n > l-1:
                    n = 0
                acc += gas[n]
                # 表示走完了一圈
                if n == i:
                    return n
            # 此处贪心非常能提高效率
            # 如果n比i小了说明上面循环中断点是在i前面，由于i的前面肯定是已经先判断过了的，能过的话早就返回值了
            if n < i:
                return -1
            else:
                i = n+1
        return -1


a = Solution().canCompleteCircuit(
[2,3,4],
[3,4,3]
)
print(a)
