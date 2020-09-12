#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 一战此题， 递归暴力枚举，暴力枚举失败
class Solution:

    def minInsertions(self, s: str) -> int:
        self.mem = [float('inf') for _ in range(len(s))]
        for index, i in enumerate(s):
            if index > 1 and index == s[index - 1]:
                self.mem[index] = self.mem[index - 1]
                continue
            if index < len(s) - 2 and i == s[index + 1]:
                l = index
                r = index + 1
            else:
                l = r = index

            offset = 1
            count = 0
            s_copy = list(s)
            while 1:
                if r + offset >= len(s_copy):
                    count += len(s_copy[:l - offset + 1])
                    break
                if l - offset < 0:
                    count += len(s_copy[r + offset:])
                    break

                if s_copy[l - offset] != s_copy[r + offset]:
                    s_copy.insert(offset, s_copy[r + offset])
                    l += 1
                    r += 1
                    count += 1

                offset += 1
            self.mem[index] = count
        return min(self.mem)

# 这题可以通过求出s和s[::-1]的最长公共子序列的长度max_len
# 也可以表述为求s的最长回文子序列的长度max_len
# 然后len(s)-max_len就行
# 暂时不明白为什么这样就行
# 注释：子串和子序列的区别：
#   一个字符串 s 被称作另一个字符串 S 的子串，表示 s 在 S 中出现了。
#   一个字符串 s 被称作另一个字符串 S 的子序列，说明从序列 S 通过去除某些元素但不破坏余下元素的相对位置（在前或在后）可得到序列 s 。
#   比如，“中出”是“我们中出了一个叛徒”的子串（同时也是子序列）。而“XQ”是“LXTQL”的子序列，而不是子串。
s = 'abcacbac'
a = Solution().minInsertions(s)
print(a)
