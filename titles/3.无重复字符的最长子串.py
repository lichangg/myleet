#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 自己瞎写的错的
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         slide_str=''
#         max_len = 0
#         max_str = ''
#         for index, i in enumerate(s):
#             if slide_str and i in slide_str:
#                 if max_len < len(slide_str):
#                     max_len = len(slide_str)
#                     max_str = slide_str
#                 repeat_index = slide_str.index(i)
#                 slide_str = slide_str[repeat_index:]
#
#             else:
#                 slide_str += i
#         max_len = len(max_str) or len(slide_str)
#         return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:






a=Solution().lengthOfLongestSubstring('pwwkew')
print(a)