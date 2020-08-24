#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0; sign = '+'
        for i in range(len(s)):
            # 两位数及以上的字符串转为数字的方法
            if s[i].isdigit():
                num = num*10 + int(s[i])
            # 当前若遍历到一个符号时，先进行上一个运算符号的运算
            if s[i] in '+-*/' or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                # 当上一个符号是乘除时立马先运算出一个结果
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0; sign = s[i]
        return sum(stack)
a=Solution().calculate('-3-2*1-1')
print(a)