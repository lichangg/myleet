#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        self.res = []
        last = 0
        def find_last(aim, S):
            for index, i in enumerate(S[::-1]):
                if i == aim:
                    return len(S) - index
        for index_i, i in enumerate(S):
            if index_i<last:
                continue
            last =find_last(i, S)
            j = index_i
            while j<last:
                j_last = find_last(S[j], S)
                last = max(j_last, last)
                j+=1
            self.res.append(last-index_i)
        return self.res

# 官方解答, 比上述算法要快
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = [0] * 26
        # 此处非常巧妙的先统计了各个字母最后出现的位置
        for i, ch in enumerate(S):
            last[ord(ch) - ord("a")] = i

        partition = list()
        start = end = 0
        for i, ch in enumerate(S):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1

        return partition

a=Solution().partitionLabels('qiejxqfnqceocmy')
print(a)