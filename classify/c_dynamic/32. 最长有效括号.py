#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_len = 0
        for idx, i in enumerate(s):
            if i == '(' or not stack or s[stack[-1]] == ')':
                stack.append(idx)
                continue
            else:
                stack.pop()
                if not stack:
                    max_len = idx-0+1
                    continue
                max_len=max(max_len, idx-stack[-1])
        return max_len


s = ")()()(())"
a = Solution().longestValidParentheses(s)
print(a)
