#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split(' ')
        li = list(filter(None, li))
        return ' '.join(li[::-1])

a=Solution().reverseWords("a good   example")
print(a)