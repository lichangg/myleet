#!/usr/bin/env python
# -*- coding:utf-8 -*-
#//TODO 思路可以
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        list_n = list(str(N))
        r = len(list_n) - 1
        res = []
        while r - 1 >= 0:
            if list_n[r] >= list_n[r-1]:
                res.append(list_n[r])
            else:
                list_n[r-1] = str(int(list_n[r-1]) - 1)
                res = ['9'] * (len(res) + 1)
            r -= 1
        if list_n[r] != '0':
            res.append(list_n[r])
        return int(''.join(res[::-1]))




a=Solution().monotoneIncreasingDigits(10000)
print(a)
