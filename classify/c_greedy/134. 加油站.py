#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
# 汽车的邮箱容量无限

# 仍然暴力法,不过可以用贪心优化
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l  =len(gas)
        i = 0
        diff = []
        while i<l:
            diff.append(gas[i] - cost[i])
            i+=1

        def valid(idx):
            cp_idx = idx
            s=0
            while cp_idx<l:
                s+=diff[cp_idx]
                if s<0:
                    return False
                cp_idx +=1
            cp_idx = 0
            while cp_idx<idx:
                s+=diff[cp_idx]
                if s<0:
                    return False
                cp_idx+=1
            return True
        for idx, item in enumerate(diff):
            if item < 0:
                continue
            if valid(idx):
                return idx

        return -1

# 用贪心优化
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # 先从第一个加油站开始遍历
        i = 0
        while i < n:
            # 初始可获得的汽油及消耗汽油均为 0
            sum_of_gas = 0
            sum_of_cost = 0
            # 开始检查是否能够走完一圈
            count = 0
            while count < n:
                # 因为道路是环形的，注意索引
                j = i + count if i + count < n else i + count - n
                # 统计可获得汽油量及消耗量总和，进行比较
                sum_of_gas += gas[j]
                sum_of_cost += cost[j]
                # 获得汽油量小于消耗量时，表示汽油无法支撑到下一个加油站
                if sum_of_gas < sum_of_cost:
                    break
                # 若油量支持驶向下个站，则继续检查
                count += 1

            # 如果 count 等于 n，表示走完所有的加油站，
            # 那么返回起始加油站编号 i
            if count == n:
                return i
            # 否则起始点将重置为最后能到达的加油站的下一个加油站，//todo 此处就是贪心的点,index直接加到刚才能到的那个站的下一站,而不是一个个加
            # 其中 i + count 表示能到达的最后一个加油站
            else:
                i = i + count + 1
        # 若均无法走完一圈，返回 -1
        return -1



a=Solution().canCompleteCircuit(gas  = [1,2,3,4,5],
                                cost = [3,4,5,1,2])
print(a)