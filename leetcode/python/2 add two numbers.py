## 题目描述

```
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```



```py
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res=ListNode(0)
        head=res
        carry=0
        while l1 or l2 or carry!=0:
            sum=carry
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            # set value
            if sum<=9:
                res.val=sum
                carry=0
            else:
                res.val=sum%10
                carry=sum//10
            # creat new node
            if l1 or l2 or carry!=0:
                res.next=ListNode(0)
                res=res.next
        return head

```