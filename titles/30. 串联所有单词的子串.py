#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def findSubstring(self, s: str, words):
        from collections import Counter
        if not s or not words: return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        words = Counter(words)
        print(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                cur_Counter[w] += 1
                cur_cnt += 1
                while cur_Counter[w] > words[w]:
                    left_w = s[left:left + one_word]
                    left += one_word
                    cur_Counter[left_w] -= 1
                    cur_cnt -= 1
                if cur_cnt == word_num:
                    res.append(left)
        return res


# 二刷,深度搜素法,可惜过不了"aaa", ["a","a"], 因为re.finditer这个方法是有问题的,比如在'aaa'里面找'aa'只会返回0
# class Solution:
#     def findSubstring(self, s: str, words):
#         import re
#         n = len(words)
#         self.s = s
#         self.res = []
#
#         def dfs(path, n, exclude_idx, words):
#             path += words[exclude_idx]
#             if n == 0:
#                 t = re.finditer(path, self.s)
#                 for i in t:
#                     self.res.append(i.span()[0])
#                 return
#             words.pop(exclude_idx)
#             for index, i in enumerate(words):
#                 dfs(path, n - 1, index, words[:])
#
#         for index, i in enumerate(words):
#             dfs('', n - 1, index, words[:])
#
#         return list(set(self.res))

# 二刷, 边界条件要注意啊, 感觉复杂度有点高
# 执行用时：4356 ms, 在所有 Python3 提交中击败了5.32%的用户
# 内存消耗：13.7 MB, 在所有 Python3 提交中击败了85.25%的用户
class Solution:
    def findSubstring(self, s: str, words):
        word_len = len(words[0])
        s_len = len(s)
        hashmap = {}
        self.res = []
        for i in words:
            hashmap[i] = hashmap.get(i, 0) + 1
        i = 0

        while i <= s_len - word_len:
            temp_hashmap = hashmap.copy()
            j = i
            while j <= s_len - word_len :
                cur_s = s[j:j + word_len]
                if cur_s in temp_hashmap:
                    temp_hashmap[cur_s] -= 1
                    if temp_hashmap[cur_s] == 0:
                        temp_hashmap.pop(cur_s)
                        if not temp_hashmap:
                            self.res.append(i)
                            break
                else:
                    break
                j += word_len
            i += 1
        return self.res

a = Solution().findSubstring("a", ["a"])
print(a)
