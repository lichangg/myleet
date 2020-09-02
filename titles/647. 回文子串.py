#!/usr/bin/env python
# -*- coding:utf-8 -*-
#直接深度遍历+剪枝, 但是好像复杂度很高
# 执行用时：1064 ms, 在所有 Python3 提交中击败了5.04%的用户
# 内存消耗：15.2 MB, 在所有 Python3 提交中击败了36.35%的用户
class Solution:
    def is_huiwen(self,s):
        if s== s[::-1]:
            return True
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        def dfs(begin, s,path):
            if begin>=len(s):
                return
            curpath = path + s[begin]
            if self.is_huiwen(curpath):
                self.count+=1
            dfs(begin+1,s,curpath)
        for index, i in enumerate(s):
            dfs(index,s,'')
        return self.count

# 中心扩展法,这个时间是O(N**2),空间是O(1),厉害多了
# 思路是从中心点往两边扩散, 所有的单个字符和所有的连续双字符都是中心点

# 执行用时：168 ms, 在所有 Python3 提交中击败了65.57%的用户
# 内存消耗：13.5 MB, 在所有 Python3 提交中击败了95.79%的用户
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.res = 0

        def helper(i, j):
            # 扩散操作一旦有扩散的左右两字符串不一致的情况就立即终止
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                self.res += 1

        for i in range(n):
            #从中心点是单字符的出发开始向相变扩散找
            helper(i, i)
            #从中心点是双字符的出发开始向两边扩散找
            helper(i, i + 1)
        return self.res




a=Solution().countSubstrings('abbac')
print(a)