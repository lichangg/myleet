#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 思路1 暴力
# 这也能让我给想出来, 不容易
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        short = len(s)
        long = len(t)
        s_idx= 0
        l_idx = 0
        while s_idx < short:

            while l_idx < long:
                if t[l_idx] == s[s_idx]:
                    l_idx += 1
                    break
                l_idx +=1
            else:
                return False

            s_idx+=1
        return True


a=Solution().isSubsequence(s = "axc", t = "acx")
print(a)