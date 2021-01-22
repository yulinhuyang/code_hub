#eric wang 提供有序数组 Python3 代码

def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    
    if n == 0:
        return 0
    
    slow, fast = 0, 1
    
    while fast < n:
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
            
        fast += 1
        
    return slow + 1
    
#eric wang 提供有序链表 Python3 代码

def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head:
        return head
    
    slow, fast = head, head.next
    
    while fast:
        if fast.val != slow.val:
            slow.next = fast
            slow = slow.next
            
        fast = fast.next

    # 断开与后面重复元素的连接   
    slow.next = None
    return head
