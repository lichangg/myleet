#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 暴力枚举所有子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ''
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                t_str = s[i:j]
                if t_str == t_str[::-1] and len(t_str) > len(max_str):
                    max_str = t_str

        return max_str

# 自己写的中心扩展法,不够优雅,复杂度O(N**2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ''
        for index, i in enumerate(s):
            one_cur = 0
            while index - one_cur >= 0 and index + one_cur <= len(s) - 1 and s[index - one_cur] == s[index + one_cur]:
                max_str = max_str if len(max_str) > 2 * one_cur + 1 else s[index - one_cur:index + one_cur + 1]
                one_cur += 1
            two_cur = 0
            while index - two_cur >= 0 and index + two_cur + 1 <= len(s) - 1 and s[index - two_cur] == s[index + 1 + two_cur] and s[index] == s[
                index + 1]:
                max_str = max_str if len(max_str) > 2 * two_cur + 2 else s[index - two_cur:index + 2 + two_cur]
                two_cur += 1

        return max_str

# 官方的中心扩展法,比较优雅,时间可以缩短一半(为啥可以比上面缩短一半,搞不懂)
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

# Manacher马拉车算法,暂时看不懂,复杂为O(n),非常牛逼,待学
class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]

a = Solution().longestPalindrome('cdddc')
print(a)
