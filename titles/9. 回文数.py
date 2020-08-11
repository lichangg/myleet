#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        div, mod = divmod(len(s), 2)
        if div == 0:
            return True
        if mod:
            left = s[:div]
            right = s[div+1:]
        else:
            left=s[:div]
            right = s[div:]
        if left == right[::-1]:
            return True
        else:
            return False