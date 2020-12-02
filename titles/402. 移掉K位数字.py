#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 该题可转化为求保留K位后的最小子序列
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        k = len(num) - k
        stack = []
        for index, i in enumerate(num):
            while stack and int(stack[-1]) > int(i) and len(num) - index > k - len(stack):
                stack.pop()

            # 这里千万别忘了,只有要保留的stack长度不足时才会继续添加,否则跳过了
            if len(stack) < k:
                stack.append(i)
            else:
                continue
        return ''.join(stack).lstrip('0') or "0"


a = Solution().removeKdigits(num="9", k=1)
print(a)
