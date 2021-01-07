#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 思路1
# 1. 初始化观察数组res
# 2. 遍历温度数组, 维护单调递减栈stack, 遇到更低温度就压入栈
# 3. 遇到更高温则进入循环:
#   - stack弹出当前栈内最低温的索引, 用当前item的index减就得到了需要等待的天数
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for index, item in enumerate(T):
            while stack and item > T[stack[-1]]:
                floor_idx = stack.pop()
                res[floor_idx] = index - floor_idx
            stack.append(index)
        return res
a=Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
print(a)