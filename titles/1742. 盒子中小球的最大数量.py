#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import Counter


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        tmp = []
        for i in range(lowLimit, highLimit+1):
            acc= 0
            tmp_num = i
            while tmp_num >0:
                div, mod = divmod(tmp_num, 10)
                tmp_num = div
                acc+=mod

            tmp.append(acc)
        c = Counter(tmp)
        return c.most_common(1)[0][1]

a=Solution().countBalls(27,100)
print(a)