
## 题目描述

```

合并  k  个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

```



Python3 Code：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)

        # basic cases
        if lenth == 0: return None
        if lenth == 1: return lists[0]
        if lenth == 2: return self.mergeTwoLists(lists[0], lists[1])

        # divide and conqure if not basic cases
        mid = n // 2
        return self.mergeTwoLists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:n]))


    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        c1, c2, c3 = l1, l2, res
        while c1 or c2:
            if c1 and c2:
                if c1.val < c2.val:
                    c3.next = ListNode(c1.val)
                    c1 = c1.next
                else:
                    c3.next = ListNode(c2.val)
                    c2 = c2.next
                c3 = c3.next
            elif c1:
                c3.next = c1
                break
            else:
                c3.next = c2
                break

        return res.next
```