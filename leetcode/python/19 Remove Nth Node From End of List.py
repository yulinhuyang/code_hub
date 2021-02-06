## 题目描述

```
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

```

## 前置知识

- 链表
- 双指针



def removeNthFromEnd(self, head, n):
    slow = fast = head
    for i in range(n):
        fast = fast.next
    if not fast: return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head