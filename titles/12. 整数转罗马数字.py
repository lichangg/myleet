#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 这个答案很好: https://leetcode-cn.com/problems/integer-to-roman/solution/tan-xin-ha-xi-biao-tu-jie-by-ml-zimingmeng/
# 空间时间都是O(1)
class Solution:
    def intToRoman(self, num: int) -> str:
        # 使用哈希表，按照从大到小顺序排列
        hashmap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        res = ''
        for key in hashmap:
            if num // key != 0:
                count = num // key  # 比如输入4000，count 为 4
                res += hashmap[key] * count
                num %= key
        return res

