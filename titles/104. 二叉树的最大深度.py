#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def maxDepth(self, root) -> int:
        return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right))+1

