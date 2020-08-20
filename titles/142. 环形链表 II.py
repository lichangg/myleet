#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 这题和141题好像都没啥意思
class Solution(object):
    def detectCycle(self, head):
        visited = set()

        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next

        return None

