#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for _ in range(n - 2):
            a, b = b, a + b
        return b


# 二刷,代码格式优化一下
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2: return n
        a, b = 1, 2
        for _ in range(n - 2):
            a, b = b, a + b
        return b


a = Solution().climbStairs(5)
print(a)
