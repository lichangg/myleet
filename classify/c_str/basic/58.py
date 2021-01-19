#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(" ")
        print(l)
        for i in l[::-1]:
            if i != "":
                return len(i)

a=Solution().lengthOfLastWord("hefds ")
print(a)