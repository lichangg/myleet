#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ''

        for i in s:
            if i.isalpha() or i.isdigit():
                news += i.capitalize()
        return news == news[::-1]
a=Solution().isPalindrome("1a2")
print(a)