## 题目描述
```
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5

```

## 前置知识

- [链表](https://github.com/azl397985856/leetcode/blob/master/thinkings/basic-data-structure.md)


链表的题目 90% 的bug都出现在：

1. 头尾节点的处理
2. 指针循环引用导致死循环

因此大家对这两个问题要保持 100% 的警惕。

## 关键点解析

- 链表的基本操作（删除指定节点）
- 虚拟节点 dummy 简化操作


#azl 
Python Code:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = ListNode(0)
        prev.next = head
        cur = prev
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return prev.next
```
