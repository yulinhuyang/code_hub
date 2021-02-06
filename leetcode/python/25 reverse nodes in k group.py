## 题目描述

```
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

 

示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5


//AZL

_Python3 Cose_

```python
class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode, terminal):
        cur = head
        pre = None
        while cur != terminal:
            next = cur.next
            cur.next = pre

            pre = cur
            cur = next
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ans = ListNode()
        ans.next = head
        pre = ans

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return ans.next
            next = tail.next
            head, tail = self.reverse(head, tail, tail.next)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = next
            pre = tail
            head = next
        
        return ans.next

//AZL 扩展 1

- 要求从后往前以`k`个为一组进行翻转

```py

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k < 2:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        count = 0
        while cur:
            count += 1
            if count % k == 0:
                pre = self.reverse(pre, cur.next)
                # end 调到下一个位置
                cur = pre.next
            else:
                cur = cur.next
        return dummy.next
    # (p1, p4） 左右都开放

    def reverse(self, p1, p4):
        prev, curr = p1, p1.next
        p2 = curr
        # 反转
        while curr != p4:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # 将反转后的链表添加到原链表中
        # prev 相当于 p3
        p1.next = prev
        p2.next = p4
        # 返回反转前的头， 也就是反转后的尾部
        return p2

# @lc code=end
