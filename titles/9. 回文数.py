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
# 题目要求不能将数字转为字符串后处理. 所以智能用+-*/反转数字然后做对比
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertedNumber = 0
        # 此处是将整数反转的方法,学到了
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
        return x == revertedNumber or x == revertedNumber // 10