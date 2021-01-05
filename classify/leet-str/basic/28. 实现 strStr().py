#!/usr/bin/env python
# -*- coding:utf-8 -*-
# str.find就是干这个事儿的

# 思路1：滑动窗口固定为needle的长度， 然后滑动显示haystack，相等则返回
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1

# 思路2：
# 1. 设置双指针a(扫描haystack), b(扫描needle),起始都是0
# 2. a,b同时扫描.若出现相等位置则记录该起始索引start
# 3. 一旦发现不匹配,b回退到0,a回退到start+1
# 重复上述步骤,找到或找完为止
b='hello'
c='ll'
a=Solution().strStr(b,c)
print(a)
