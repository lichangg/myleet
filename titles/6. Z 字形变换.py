#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:return s
        res = ['' for _ in range(numRows)]
        idx, flag = 0, -1
        for string in s:
            res[idx] += string
            if idx == 0 or idx == numRows-1:flag = -flag
            idx +=flag
        return ''.join(res)

a=Solution().convert('PAYPALISHIRING', 3)
print(a)