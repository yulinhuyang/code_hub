## 题目描述

```
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

 

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

```

## 前置知识

- 链表


def partition(self, head, x):
    h1 = l1 = ListNode(0)
    h2 = l2 = ListNode(0)
    while head:
        if head.val < x:
            l1.next = head
            l1 = l1.next
        else:
            l2.next = head
            l2 = l2.next
        head = head.next
    l2.next = None
    l1.next = h2.next
    return h1.next



//azl

Python3 Code:

```python
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """在原链表操作，思路基本一致，只是通过指针进行区分而已"""
        # 在链表最前面设定一个初始node作为锚点，方便返回最后的结果
        first_node = ListNode(0)
        first_node.next = head
        # 设计三个指针，一个指向小于x的最后一个节点，即前后分离点
        # 一个指向当前遍历节点的前一个节点
        # 一个指向当前遍历的节点
        sep_node = first_node
        pre_node = first_node
        current_node = head

        while current_node is not None:
            if current_node.val < x:
                # 注意有可能出现前一个节点就是分离节点的情况
                if pre_node is sep_node:
                    pre_node = current_node
                    sep_node = current_node
                    current_node = current_node.next
                else:
                    # 这段次序比较烧脑
                    pre_node.next = current_node.next
                    current_node.next = sep_node.next
                    sep_node.next = current_node
                    sep_node = current_node
                    current_node = pre_node.next
            else:
                pre_node = current_node
                current_node = pre_node.next

        return first_node.next
```