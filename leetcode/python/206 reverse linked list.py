## 题目描述

反转一个单链表。

```
示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

```

## 前置知识

- [链表

## 关键点解析

- 链表的基本操作（交换）
- 虚拟节点 dummy 简化操作
- 注意更新 current 和 pre 的位置， 否则有可能出现溢出

Python Code:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        prev = None
        cur = head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev



#递归


Python 实现

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        ans = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return ans
```