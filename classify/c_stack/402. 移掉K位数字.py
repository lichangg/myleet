#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 思路1. 单调栈

#写的真是不优雅啊
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return '0'
        stack = []
        pop_res = []
        for index, item in enumerate(num):
            while stack and item < num[stack[-1]]:
                bigger = stack.pop()
                pop_res.append(bigger)
                if len(pop_res) == k:
                    break
            if len(pop_res) == k:
                break
            stack.append(index)

        while len(pop_res) < k:
            pop_res.append(stack.pop())
        res = ''
        for i, j in enumerate(num):
            if i not in pop_res:
                res +=j
        res = res.lstrip('0')
        if not res:
            return '0'
        return res

#优雅一点 可转化了求保留K位后的最小子序列
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        k = len(num) - k
        stack = []
        for index, i in enumerate(num):
            while stack and int(stack[-1]) > int(i) and len(num) - index > k - len(stack):
                stack.pop()
            if len(stack) < k:
                stack.append(i)
            else:
                continue
        return ''.join(stack).lstrip('0') or "0"
a=Solution().removeKdigits(num = "112", k =1)
print(a)