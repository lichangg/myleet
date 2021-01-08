#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 思路1. 单调栈
class StockSpanner:

    def __init__(self):
        self.prices = []
        self.stack = []
    def next(self, price: int) -> int:
        self.prices.append(price)
        cur_index = len(self.prices) - 1
        # for index, p in enumerate(self.prices):
        while self.stack and price >= self.prices[self.stack[-1]]:
            self.stack.pop()
        self.stack.append(cur_index)
        if len(self.stack) == 1:
            return cur_index + 1
        return cur_index - self.stack[-2]



b=[100, 80, 60, 70, 60, 75, 85]
s=StockSpanner()
for i in b:
    a = s.next(i)
    print(a)
