#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 效率太低了
# 执行用时：1436 ms, 在所有 Python3 提交中击败了5.02%的用户
# 内存消耗：17.1 MB, 在所有 Python3 提交中击败了19.52%的用户
# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.q = []
#         self.min = []
#     def push(self, x: int) -> None:
#         self.q.insert(0, x)
#         if self.min:
#             push_index = 0
#             for index, i in enumerate(self.min):
#                 if i < x:
#                     continue
#                 else:
#                     push_index = index
#                     break
#             else:
#                 self.min.append(x)
#                 return
#             self.min.insert(push_index,x)
#         else:
#             self.min.append(x)
#
#
#     def pop(self) -> None:
#         a=self.q[0]
#         self.q.remove(a)
#         self.min.remove(a)
#
#     def top(self) -> int:
#         return self.q[0]
#
#     def getMin(self) -> int:
#         return self.min[0]
import math

# min_stack有点计数的一i是
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        # 来个同步pop, min_stack的栈顶元素始终在同步追加而保持是最小值
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

minStack =MinStack()
print(minStack.push(-2))
print(minStack.push(0))
print(minStack.push(-3))
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())

