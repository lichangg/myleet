#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
# 汽车的邮箱容量无限

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l  =len(gas)
        i = 0
        diff = []
        while i<l:
            diff.append(gas[i] - cost[i])
            i+=1

        def valid(idx):
            s=0
            while idx<l:
                s+=diff[idx]
                if s<0:
                    return False


        for idx, item in enumerate(diff):
            if item < 0:
                continue
            if valid(idx):
                return True

        return False



a=Solution().canCompleteCircuit(gas  = [1,2,3,4,5],
                                cost = [3,4,5,1,2])
print(a)