#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 思路1.
# 很典型的在遍历的时候需要回溯去找到第一个大于(或小于)当前item的元素
# 1. 遍历数组, 并开始维护一个单调递减的栈(遇到一个更小的元素就压入栈)
# 2. 当遇到一个不小于栈顶元素的元素后进入循环pop,直到栈顶元素比当前item大
# 3. 循环中需要找到floor, 然后计算此时形成的水洼大小
# 4. 累加水洼
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        rain = 0
        for index, item in enumerate(height):
            while stack and item >= height[stack[-1]]:
                floor = stack.pop()
                if not stack:
                    break
                # 因为是单调递减栈, 所以此时stack[-1]必定大于等于floor, 由于进入了此条件, item天然的也大于floor,
                # 此时可以算出以stack[-1]为左挡板, item为右挡板时的水洼大小
                dis = index - stack[-1] - 1
                rain += (min(height[stack[-1]], item) - height[floor]) * dis
            stack.append(index)
        return rain



a=Solution().trap([4,2,0,3,2,5])
print(a)