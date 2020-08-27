#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用一个辅助栈, 太优雅了,学到了
# 栈内的元素存储为一个元组,元组里面放当前串和下个[]里面的串需要乘上的倍数,我吐了
# 当出现'['存元组入栈
# 当遇到']'弹出来一起处理
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            # 注意可能会有连续数字
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res

# 递归,以后在看//TODO
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)


s = "3[a]2[bc]"
a = Solution().decodeString(s)
print(a)
