#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def deal(s):
            cur = 0
            dealed_s = []
            while cur< len(s):
                if s[cur] == '#':
                    if dealed_s:
                        dealed_s.pop()
                else:
                    dealed_s.append(s[cur])
                cur +=1
            return str(dealed_s)
        return deal(S) == deal(T)
a=Solution().backspaceCompare(S = "a#c", T = "b")
print(a)