#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 有空看
# trie数结构可以1. 自动补全2. 拼写检查3. IP 路由 (最长前缀匹配)4. T9 (九宫格) 打字预测等等, 其作用还有与hash表还有平衡树的区别可以参考这个
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/shi-xian-trie-qian-zhui-shu-by-leetcode/
class Node:
    def __init__(self, val=None, next=[], isEnd=False):
        self.val = val
        self.next = {i.val: i for i in next}
        self.isEnd = isEnd


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tmp = self.node
        for i in word:
            if i not in tmp.next:
                tmp.next[i] = Node(i)
            tmp = tmp.next[i]
        tmp.isEnd = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmp = self.node
        for i in word[:-1]:
            if i not in tmp.next:
                return False
            tmp = tmp.next[i]
        if word[-1] not in tmp.next:
            return False
        if tmp.next[word[-1]].isEnd:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp = self.node
        for i in prefix:
            if i not in tmp.next:
                return False
            tmp = tmp.next[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

