#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
#学到了
#1、如果 i 为偶数，那么f(i) = f(i/2)
# 因为 i/2 本质上是i的二进制左移一位，低位补零，所以1的数量不变。
# 2、如果 i 为奇数，那么f(i) = f(i - 1) + 1
# 因为如果i为奇数，那么 i - 1必定为偶数，而偶数的二进制最低位一定是0，
# 那么该偶数 +1 后最低位变为1且不会进位，所以奇数比它上一个偶数bit上多一个1，即 f(i) = f(i - 1) + 1。

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num + 1):
            if i % 2 == 0:
                res.append(res[i // 2])
            else:
                res.append(res[i - 1] + 1)
        return res

