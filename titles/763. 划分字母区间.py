#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 先用贪心试试
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        count = 1
        self.res = []
        def find_valid_compose(count):

        for i in range(1, len(S)):
            if not find_valid_compose(i):
                break

        return self.res


a=Solution().partitionLabels()
print(a)