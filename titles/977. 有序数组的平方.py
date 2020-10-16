#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        if len(A) == 0:
            return A

        index = 0
        while index < len(A):
            if A[index] > 0:
                break
            index += 1
        left = [i**2 for i in A[:index]]
        left.reverse()
        right = [i**2 for i in A[index:]]
        return self.merge(left, right)

    def merge(self, l1, l2):
        l1_index = 0
        l2_index = 0
        new_l = []
        while l1_index < len(l1) and l2_index < len(l2):
            if l1[l1_index] > l2[l2_index]:
                new_l.append(l2[l2_index])
                l2_index += 1
            else:
                new_l.append(l1[l1_index])
                l1_index += 1
        new_l.extend(l1[l1_index:])
        new_l.extend(l2[l2_index:])
        return new_l

# 别人的解法....直接排序, 比我上面还快...
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(num * num for num in A)



a = Solution().sortedSquares([-1])
print(a)
