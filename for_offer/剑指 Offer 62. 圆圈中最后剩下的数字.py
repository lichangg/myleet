#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        def recur(start, li, m):
            if len(li) == 1:
                return li[0]
            tmp = start + m-1
            idx = tmp % len(li)
            del li[idx]
            return recur(idx, li, m)

        return recur(0, list(range(n)), m)


a = Solution().lastRemaining(10, 17)
print(a)
