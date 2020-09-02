#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 暴力法,会超时的
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res =[]
        for index, i in enumerate(T):
            for j_index in range(index, len(T)):
                if T[j_index]>i:
                   res.append(j_index - index)
                   break
            else:
                res.append(0)
        return res

# 单调栈的解法,也太优雅了,学到了
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 可以维护一个存储下标的单调栈，从栈底到栈顶的下标对应的温度列表中的温度依次递减。
        # 如果一个下标在单调栈里，则表示尚未找到下一次温度更高的下标。
        ans = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:    # 栈不为空 && 栈顶温度小于当前温度
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans



a=Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
print(a)