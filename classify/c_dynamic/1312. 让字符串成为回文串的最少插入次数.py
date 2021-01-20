#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 这种思路还是不对, 解决不了源字符串中心是偏向两边的情况
class Solution:
    def minInsertions(self, s: str) -> int:
        head = 0
        tail = len(s) - 1
        count = 0
        while head < tail:
            if s[head] == s[tail]:
                head += 1
                tail -= 1
            else:
                if s[head + 1] == s[tail]:
                    head += 1
                    count += 1
                elif s[head] == s[tail - 1]:
                    tail -= 1
                    count += 1
                else:
                    count += 2
                    head += 1
                    tail -= 1
        return count
# 动态规划
# 定义dp[i][j]为区间s[i:j](包含索引为i,j的字符)成为回文串的最少插入字符数
#   - 若s[i] == s[j]说明最外层已经是回文了, 只要用里面的回文状态转移出来就行,也就是dp[i][j] = dp[i+1][j-1]
#   - 若s[i] != s[j]说明最外层不是回文,这时候可以从这两个状态转移出来, 一个是dp[i+1][j],一个是dp[i][j-1], 取两者中较小的再+1就行
# 还要解决的问题是初始的s[i:j]怎么取, 这里需要遍历枚举, 代码中span为子区间长度, 由span得到j, 也就是把所有的i, j可以取到的值都取到, 不断更新dp数组
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for span in range(2, n + 1):
            for i in range(n - span + 1):
                j = i + span - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][n - 1]

a = Solution().minInsertions('leetcode')
print(a)
