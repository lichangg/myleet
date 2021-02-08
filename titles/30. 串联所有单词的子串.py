#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 重点题
from typing import List


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
# 可优化的地方如下:
# 现在的方法是逐个字符前进的,例如对于"barfoofoobarthefoobarman", words = ["bar","foo","the"],
# 其实可以逐个单词前进, 但是这样会导致有些单词组合拿不到, 比如要是起点是0的话,智能拿到"bar","foo",这些而拿不到"arf"
# 要解决这个问题可以把起点设置为 0到word_len-1这几个值,这样就能保证能拿到所有单词组合
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
            while j <= s_len - word_len:
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


# 别人写的优化,首先这是逐个单词搜素的,很厉害,学到了
# 另外优化的点在于
# 1. 对子串有头尾两个指针, 当遇到不符合的单词就将下一个头指针直接指到上一个尾指针的右边
# 2. 每个子串从后往前搜索
# 对于第一点比较好理解, 第二点的优化之处是在与例如对于 "barfoothefoobarman", ["foo","bar"]
# 如果从前往后, 当搜完barfoo后, 会搜foothe, 先foo再the, 因为上一轮搜过了foo, foo是成功的(也就是会重复搜这个) the不行
# 如果从后往前, 当搜完barfoo后, 会搜foothe, 先the再foo, the是失败的, 直接跳出
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        w_len, s_len = len(words[0]), len(s)
        t_len = w_len * len(words)  # 子串的长度

        word_dict = {}  # words的哈希表
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1

        ans = []
        for offset in range(w_len):
            lo, lo_max = offset, s_len - t_len
            while lo <= lo_max:
                tmp_dict = word_dict.copy()
                match = True
                for hi in range(lo + t_len, lo, -w_len):  # 从尾到头搜索单词
                    word = s[hi - w_len: hi]
                    if word not in tmp_dict or tmp_dict.get(word, 0) == 0:
                        match = False
                        break  # 当前单词不符合要求 直接停止这个子串的搜索
                    tmp_dict[word] -= 1
                if match:
                    ans.append(lo)
                lo = hi  # 对lo直接赋值 这就是相比法二优化的地方
        return ans
a = Solution().findSubstring(  s = "barfoothefoobarman",
  words = ["foo","bar"])
print(a)


# 别人的滑动窗口,时间略逊于上面的方法,以后再看
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words: return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        words = Counter(words)
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


# 再刷
# 遇到类似这种直接陷进去"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",['a','a','a','a','a','a','b']
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         tmp = []
#         word_l = len(words[0])
#         s_l = len(s)
#         for i in range(0, s_l):
#             copy_words = words[::]
#             start = i
#             while start + word_l < s_l+1 and copy_words:
#                 cur_word = s[start:start+word_l]
#                 if cur_word in copy_words:
#                     copy_words.remove(cur_word)
#                     start += word_l
#                 else:
#                     break
#             else:
#                 if not copy_words:
#                     tmp.append(i)
#         return tmp


from collections import defaultdict
import queue


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        dic_need = defaultdict(int)
        word_l = len(words[0])
        s_l = len(s)
        res = []
        for i in words:
            dic_need[i] += 1

        for start in range(word_l):
            q = queue.Queue()
            for i in range(start, s_l, word_l):
                cur_word = s[i:i + word_l]
                if cur_word not in dic_need:
                    if q.qsize() >= 1:
                        dic_need[q.get_nowait()] += 1
                    continue

                dic_need[cur_word] -= 1
                q.put(cur_word)
                for k, v in dic_need.items():
                    if v > 0:
                        break
                else:
                    res.append(i - word_l * (len(words) - 1))
                if q.qsize() >= 1:
                    dic_need[q.get_nowait()] += 1
        return res


a = Solution().findSubstring(  s = "barfoothefoobarman",
  words = ["foo","bar"])
print(a)
