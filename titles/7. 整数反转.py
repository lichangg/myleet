#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        if s.startswith('-'):
            a=int('-' + s[1::][::-1])


        else:
            a = int(s[::-1])

        if a<-2**31 or a>2**31-1:
            a=0
        return a

a=Solution().reverse(123)
print(a)