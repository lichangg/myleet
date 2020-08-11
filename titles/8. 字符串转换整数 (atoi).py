#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re


class Solution:
    def myAtoi(self, string: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', string.lstrip())), 2 ** 31 - 1), -2 ** 31)


a=Solution().myAtoi('-4849.68')
print(a)