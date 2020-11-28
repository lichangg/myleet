#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import Counter
from typing import List

# 傻逼了,若A数组全是重复的数字a, 如果a对应有n种方案, 那最后结果比正确结果就会少(len(A)-1)*n个,这还是在其他数组没有重复的情况下,
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # A.sort()
        # B.sort()
        # C.sort()
        # D.sort()
        count = 0
        dic_A = {}
        for index, a in enumerate(A):
            dic_A[a] = index
        valid_set= set()
        for b in B:
            for c in C:
                for d in D:
                    virt = 0 - b - c - d
                    if (b,c,d) in valid_set:
                        count+=1
                    else:
                        if virt in dic_A:
                            count += 1
                            valid_set.add((b,c,d))
        return count

# 直接两两分组,将复杂度降为O(n**2), 秀啊,而且这里面先用一个counter保存结果,第二轮遍历就用上了,我之前还count两轮,傻吧
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic_ab = []
        for index_a, a in enumerate(A):
            for index_b, b in enumerate(B):
                dic_ab.append(a+b)
        count_ab = Counter(dic_ab)
        count=0
        for c in C:
            for d in D:

                count+=count_ab[-c-d]
        return count

a=Solution().fourSumCount([-1, -1],
                        [-1, 1],
                        [-1, 1],
                        [1, -1])
print(a)