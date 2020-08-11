#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 暴力枚举所有子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ''
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                t_str = s[i:j]
                if t_str == t_str[::-1] and len(t_str) > len(max_str):
                    max_str=t_str

        return max_str


a=Solution().longestPalindrome('a')
print(a)
