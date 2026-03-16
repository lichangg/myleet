#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def numDecodings(self, s: str) -> int:

        self.cache = {}

        def recur(start, end):
            if s[start] == '0' or start > end:
                return 0
            if (start, end) in self.cache:
                return self.cache[(start, end)]
            if 1 <= int(s[start:end + 1]) <= 10 or int(s[start:end + 1]) == 20: return 1
            if 11 <= int(s[start:end + 1]) <= 26: return 2

            res = recur(start, end - 1) + recur(start + 1, end) - recur(start + 1, end - 1)
            self.cache[(start, end)] = res
            return res

        return recur(0, len(s) - 1)


a = Solution().numDecodings('1212')
print(a)
