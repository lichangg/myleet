#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 汉明距离指两个二进制数位上的数不一样的个数
# 异或操作, 相同为0,不同为1
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        b=x^y
        s=str(bin(b))
        return s.count('1')

