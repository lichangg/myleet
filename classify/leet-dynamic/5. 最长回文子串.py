#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 思路1中心扩撒
# 总是考虑不好中心是两个字符的情况
# class Solution:
#     def expand(self, index):
#         i = 0
#         while index - i >= 0 and index + i <= len(self.s) - 1:
#             if self.s[index - i] == self.s[index + i]:
#                 i+=1
#                 continue
#             else:
#                 break
#         l = index-i+1
#         r = index+i-1
#         i-=1
#         return l,r,2*i+1
#     def longestPalindrome(self, s: str) -> str:
#         self.max = 0
#         self.s =s
#         self.l = 0
#         self.r = 0
#         for i in range(len(s)-1):
#             l,r,m = self.expand(i)
#             if m>self.max:
#                 self.max = m
#                 self.l = l
#                 self.r = r
#             else:
#                 continue
#         return s[self.l:self.r+1]

# 还是思路1, 解决中心是两个字符的情况一次解决不了就弄两个啊
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            #直接弄两个情况,不就解决了
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]


a=Solution().longestPalindrome("abba")
print(a)