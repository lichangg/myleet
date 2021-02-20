#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 下面这个思路是错的,最后过不了这个用例"apjesgpsxorukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxc"
# 暂时没想出来哪儿错了
# class Solution:
#     def minCut(self, s: str) -> int:
#         return self.recur(s)-1
#
#     def recur(self, s):
#         if len(s) == 0:
#             return 0
#         end, start = self.longestPalindrome(s)
#         l = self.recur(s[:end])
#         r = self.recur(s[start+1:])
#         return l+r+1
#     def expandAroundCenter(self, s, left, right):
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return left + 1, right - 1
#
#     def longestPalindrome(self, s: str):
#         start, end = 0, 0
#         for i in range(len(s)):
#             left1, right1 = self.expandAroundCenter(s, i, i)
#             left2, right2 = self.expandAroundCenter(s, i, i + 1)
#             if right1 - left1 > end - start:
#                 start, end = left1, right1
#             if right2 - left2 > end - start:
#                 start, end = left2, right2
#         return start, end

# 重要题
# 设dp[i][j]是从i到j需要切的刀数,设个屁,不能这么设置,
# 应该这样设置, 设置dp[i]是到i为止需要分割的次数
# 那么需要分两种情况:
# 1. 若s[0:i]已经是回文串(包含索引为i的字符), 那么dp[i]就直接等于0了
# 2. 若s[0:i]不是回文串, 那就需要寻找切割点,遍历0到i的索引,设为j
#   - 若s[j:i]已经是回文串了,算出dp[0:j]的切割数, 然后+1得到dp[i]的一个可能的值
#   - 将这些可能的值取最小值就是dp[i]   (此处若用列表存这这些值最后算min好像还更快一点)
# 3. 初始化的时候按最差的情况来, 即所以字符都要单独切割成回文串(注意啊!!!)
class Solution:
    def minCut(self, s: str) -> int:
        size = len(s)
        if size < 2:
            return 0
        dp = [i for i in range(size)]
        for i in range(1, size):
            tmps = s[0:i+1]
            if tmps == tmps[::-1]:
                dp[i] = 0
                continue
            # 枚举分割点
            tmp = dp[i]
            for j in range(i):
                tmps = s[j+1:i+1]
                if tmps == tmps[::-1]:
                    tmp = min(tmp, dp[j] + 1)
            dp[i] = tmp

        return dp[size - 1]



a = Solution().minCut("abbcba")
print(a)
