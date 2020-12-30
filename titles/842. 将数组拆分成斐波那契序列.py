#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

#//todo
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def recur(first, second, ind):
            cur = first + second
            str_cur = str(cur)
            if ind+len(str_cur) > len(S) or S[ind:ind+len(str_cur)] != str_cur:
                return
            else:
                if ind+len(str(cur)) == len(S) + 1:
                    return 1
                else:
                    return recur(second, cur, ind+len(str_cur))
        def valid(first_end, second_end):
            first = int(S[:first_end])
            second = int(S[first_end+1:second_end+1])
            if recur(first, second, second_end):
                return first,second
        for i in range(1,len(S)):
            for j in range(i+1, len(S)):
                r = valid(i,j)
                if r:
                    return r
        else:
            return False
a=Solution().splitIntoFibonacci('123456579')
print(a)