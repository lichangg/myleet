#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from collections import defaultdict
# 贪心在于找钱的时候优先使用掉10元的
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ihave = defaultdict(int)
        for i in bills:
            if i == 5:
                ihave[5]+=1
            elif i == 10:
                if ihave[5] == 0:
                    return False
                else:
                    ihave[5]-=1
                    ihave[10]+=1
            else:
                if ihave[5] == 0:
                    return False
                if ihave[10] > 0:
                    ihave[10]-=1
                    ihave[5]-=1
                elif ihave[10] ==0:
                    if ihave[5]<=2:
                        return False
                    ihave[5]-=3
        return True
a=Solution().lemonadeChange([5,5,10,10,20])
print(a)