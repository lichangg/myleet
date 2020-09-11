#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 自己写的,超时
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         def dps(wordDict, path):
#             for j in range(len(wordDict)):
#                 cur_path = path + wordDict[j]
#                 if cur_path not in s:
#                     continue
#                 elif cur_path == s:
#                     return True
#                 else:
#                     res = dps(wordDict,cur_path[:])
#                     if res:
#                         return res
#         res = dps(wordDict, '')
#         if res:
#             return True
#         else:
#             return False


#
# 使用记忆化函数，保存出现过的 backtrack(s)backtrack(s)，避免重复计算。
# 定义回溯函数 backtrack(s)backtrack(s)
#   若 ss 长度为 00，则返回 TrueTrue，表示已经使用 wordDictwordDict 中的单词分割完。
#   初试化当前字符串是否可以被分割 res=Falseres=False
#   遍历结束索引 ii，遍历区间 [1,n+1)[1,n+1)：
#       若 s[0,\cdots,i-1]s[0,⋯,i−1] 在 wordDictwordDict 中：res=backtrack(s[i,\cdots,n-1])\ or\ resres=backtrack(s[i,⋯,n−1]) or res。解释：保存遍历结束索引中，可以使字符串切割完成的情况。
#   返回 resres
# 返回 backtrack(s)backtrack(s)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if(not s):
                return True
            res=False
            for i in range(1,len(s)+1):
                if(s[:i] in wordDict):
                    # 保证为True的res能返回出来
                    res=back_track(s[i:]) or res
                    # 这样能过,但是竟然也没有快一点,奇怪了
                    # if res:
                    #     break
            return res
        return back_track(s)

# 动态规划,学到了
# 初始化 dp=[False,⋯,False]，长度为 n+1。n 为字符串长度。dp[i]dp[i] 表示 s 的前 i 位是否可以用 wordDict 中的单词表示。
# 初始化 dp[0]=True，空字符可以被表示。
# 遍历字符串的所有子串，遍历开始索引 i，遍历区间 [0,n)：
#   遍历结束索引 j，遍历区间 [i+1,n+1)[i+1,n+1)：
#       若 dp[i]=True 且 s[i,⋯,j) 在 wordDict 中：dp[j]=True
# 返回 dp[n]

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n=len(s)
#         dp=[False]*(n+1)
#         dp[0]=True
#         for i in range(n):
#             # j最大值也就是n,
#             for j in range(i+1,n+1):
#                 if(dp[i] and (s[i:j] in wordDict)):
#                     dp[j]=True
#         return dp[-1]

# 二刷, 这个会超时
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.res = False
        def dfs(word, s):
            len_w = len(word)
            if word == s[:len_w]:
                if len_w == len(s):
                    self.res = True
                for w in wordDict:
                    dfs(w, s[len_w:])


        for i in wordDict:
            dfs(i,s)
        return self.res
# 二刷,思路同上,做个优化,优化失败, 方向错了,主要是在于有大量重复计算比如s='aaaaaaaaaaabb',wordDict=['a','aa','aaaaab']而不是startwith或者len耗时
# 需要有一个缓存数组存着之前走过的结果
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.res = False
        self.mem = {}
        def dfs(curpath, word, s,index):
            curpath = curpath + word

            if s == curpath:
                self.res=True
                return
            if s[index:] in self.mem or s[index:].startswith(word):
                self.mem[s[index:]] = 1
                for w in wordDict:
                    dfs(curpath, w, s,len(curpath))


        for i in wordDict:
            dfs('',i,s,0)
        return self.res

# 这是缓存节点的优化方式
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memory = {}
        def dfs(s1):
            if s1 in memory:
                return memory[s1]
            for word in wordDict:
                if s1 == word:
                    return True
                if s1.startswith(word):
                    ans = dfs(s1[len(word):])
                    memory[s1] = ans
                    if ans:
                        return True
            return False
        return dfs(s)

a=Solution().wordBreak(s = "aaab", wordDict = ["a","aa","aab"])
print(a)