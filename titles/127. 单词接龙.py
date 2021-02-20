#!/usr/bin/env python
# -*- coding:utf-8 -*-
import collections
from typing import List

# 无脑用递归, 直接超时, 因为有些分支虽然也能到终点,但是很远,用贪心
# class Solution:
#
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         self.c = []
#         self.recur(beginWord, endWord, wordList, 1) or 0
#         if self.c:
#             return min(self.c)
#         else:
#             return 0
#
#
#     def filter_func(self,word1, word2):
#
#         i = 0
#         count = 0
#         while i < len(word1):
#             if word1[i] != word2[i]:
#                 count += 1
#             i+=1
#         if count > 1:
#             return False
#         else:
#             return True
#     def recur(self, beginWord: str, endWord: str, wordList: List[str], step):
#         if beginWord == endWord:
#             self.c.append(step)
#         if endWord not in wordList:
#             return
#         li_word = [i for i in wordList if self.filter_func(beginWord, i)]
#         new_wordList = wordList[:]
#         new_wordList = list(set(new_wordList) - set(li_word))
#         for i in li_word:
#                 res = self.recur(i, endWord, new_wordList, step+1)
#                 if res:
#                     return res

# 贪心仍然超时
# class Solution:
#     def filter_func(self,word1, word2):
#
#         i = 0
#         count = 0
#         while i < len(word1):
#             if word1[i] != word2[i]:
#                 count += 1
#             i+=1
#         if count == 1:
#             return True
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         self.end = endWord
#         def check(begin, wordList, step, li_word):
#             if self.end not in wordList or step<0:
#                 return
#             if begin == self.end:
#                 return True
#             new_li_word = [i for i in wordList if self.filter_func(begin, i)]
#             new_wordList = wordList[:]
#             new_wordList = list(set(new_wordList) - set(li_word))
#             for b in new_li_word:
#                 res = check(b, new_wordList, step-1, li_word)
#                 if res:
#                     return res
#
#
#         for i in range(len(wordList)):
#             res = check(beginWord, wordList, i, [])
#             if res:
#                 return i+1
#         else:
#             return 0

# 别人的单向BFS, 耗时160ms
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st = set(wordList)
        if endWord not in st:
            return 0
        m = len(beginWord)

        queue = collections.deque()
        queue.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        while queue:
            cur, step = queue.popleft()
            if cur == endWord:
                return step

            for i in range(m):
                for j in range(26):
                    tmp = cur[:i] + chr(97 + j) + cur[i + 1:]
                    if tmp not in visited and tmp in st:
                        queue.append((tmp, step + 1))
                        visited.add(tmp)

        return 0

# 别人的双向BFS,耗时120
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st = set(wordList)
        if endWord not in st:
            return 0
        m = len(beginWord)
        lvisited = set()
        rvisited = set()
        lqueue = collections.deque()
        rqueue = collections.deque()

        lqueue.append(beginWord)
        rqueue.append(endWord)

        lvisited.add(beginWord)
        rvisited.add(endWord)
        step = 0

        while lqueue and rqueue:
            if len(lqueue) > len(rqueue):
                lqueue, rqueue = rqueue, lqueue
                lvisited, rvisited = rvisited, lvisited
            step += 1
            for k in range(len(lqueue)):
                cur = lqueue.popleft()
                if cur in rvisited:
                    return step

                for i in range(m):
                    for j in range(26):
                        tmp = cur[:i] + chr(97 + j) + cur[i + 1:]
                        if tmp not in lvisited and tmp in st:
                            lqueue.append(tmp)
                            lvisited.add(tmp)

        return 0

# 无向图的思想,有点深奥,暂时看不懂,不过貌似最后计算的是两节点的最短距离,
# 参考:https://leetcode-cn.com/problems/word-ladder/solution/dan-ci-jie-long-by-leetcode-solution/
# 而基于这个思路的话实际上可以构造出一个树,根就是beginword,然后计算begin和end两节点的最短距离,这样好想一些(暂未验证)//TODO
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1

        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)

        addEdge(beginWord)
        if endWord not in wordId:
            return 0

        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]
        dis[beginId] = 0

        que = collections.deque([beginId])
        while que:
            x = que.popleft()
            if x == endId:
                return dis[endId] // 2 + 1
            for it in edge[x]:
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    que.append(it)

        return 0

# 再刷
# 这种方式过不了23号用例会超时,因为单词列表内的单词互相之间的距离进行了多次重复计算,如果能用cache存下各单词之间的距离就会好很多
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.used= defaultdict(int)
        self.min_path = float('inf')
        def distance(w1, w2):
            l = 0
            w_len = len(w1)
            dis = 0
            while l < w_len and dis <=1:
                if w1[l]!=w2[l]:
                    dis+=1
                l+=1
            return dis

        def dfs(cur_word, path):

            self.used[cur_word] = 1
            for word in wordList:
                if distance(cur_word, endWord) == 0:
                    self.min_path = min(self.min_path, path)

                if not self.used[word] and distance(word,cur_word)==1:
                    dfs(word, path+1)
            self.used[cur_word] = 0
        dfs(beginWord, 1)
        if self.min_path == float('inf'):return 0
        return self.min_path

# 怪不得要用上队列, 先进先出
# 这里巧妙的利用队列先进先出的特性进行BFS
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def distance(w1, w2):
            l = 0
            w_len = len(w1)
            dis = 0
            while l < w_len and dis <=1:
                if w1[l]!=w2[l]:
                    dis+=1
                l+=1
            return dis
        self.visited = set()
        self.visited.add(beginWord)
        li = collections.deque()
        li.append((beginWord, 1))
        while li:
            word, dis = li.popleft()
            for w in wordList:
                if word == endWord:
                    return dis
                if w in self.visited:
                    continue
                elif distance(word,w)==1:
                    self.visited.add(w)
                    li.append((w, dis+1))

        return 0

a=Solution().ladderLength(
beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
)
print(a)