### 21 调整数组顺序使奇数位于偶数前面

```python
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        
        left = 0 
        right = len(nums) -1
        while left <= right:
            if nums[left] & 1 == 1:
                left += 1
                continue 
            if nums[right] & 1 == 0:
                right -= 1
                continue
            nums[left],nums[right] = nums[right],nums[left]
        return nums
```




判断奇偶的方法： nums[left] & 1 == 1 是奇数，否则是偶数

双指针：首尾双指针，快慢双指针

### 22 合并两个有序链表

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next,l1 = l1, l1.next
            else:
                cur.next,l2 = l2, l2.next
            cur = cur.next
        if l1: 
            cur.next = l1
        else:
            cur.next = l2
        
        return dum.next
```		
		
a,b  = b,c ----> a = b    b = c
		
非交换传数

### 26 树的子结构

```python
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A,B):
            if B == None:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left,B.left) and recur(A.right,B.right)

        return bool(A and B) and (recur(A,B) or  self.isSubStructure(A.left,B) or  self.isSubStructure(A.right,B))	
```	


if not A 判空法

树天生为了递归左右子树而存在


二叉树的："recur  +   isSub法"

### 27  二叉树的镜像

```python
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        left = self.mirrorTree(root.right)
        right = self.mirrorTree(root.left)

        root.left,root.right = left,right

        return root
```

### 28 对称的二叉树

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(left,right):
            if not left  and not right :
                return True
            if not left or not right  or  left.val != right.val:
                return False
            return recur(left.left,right.right) and recur(left.right,right.left)

        if not root:
            return True

        return recur(root.left,root.right)
```
		
连续 not 判断


### 22 链表中倒数第k个节点

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:

        if head == None:
            return None

        former = head
        for i in range(k):
            former = former.next

        latter = head 
        while former:
            former = former.next
            latter = latter.next

        return latter
```


双指针:former later 快慢指针（倒数计数）


### 23  反转链表

```python

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head == None:
            return None

        cur = head.next
        prev = head
        prev.next = None
        while cur:
            next = cur.next        
            cur.next = prev 
            prev = cur
            cur = next

        return prev
```


双指针: pre cur next  前后指针（换序）

dummy链表法： 

	dummy = ListNode(0)

	return dummy.next	


### 24  复杂链表的复制


#### 方法1: 链表法  复制-调整-拆分

```python

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return None
        
        cur = head
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp 
            cur = tmp.next
        
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
            
        pre = head
        res = cur = head.next
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next

            cur = cur.next
            pre = pre.next
        
        pre.next = None
        
        return res
```

#### 方法2: 字典法

```python

	class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        
        dict = {}
        cur = head
        while cur:
            dict[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            dict[cur].next = dict.get(cur.next)
            dict[cur].random = dict.get(cur.random)
            cur = cur.next
        
        return dict[head]
```


字典的常规操作:
	
	dic = {}
	
	增加新元素: dict['Age'] = 8
	
	访问键值: dict['Age']、dict.get('Age')(键不存在时，返回None)
	
	遍历字典: dict.items()方法获取字典的各个元素即“键值对”的元祖列表
	
```python

	dict = {1: 1, 2: 'aa', 'D': 'ee', 'Ty': 45}
	for key, value in dict.items():
	    print(key, value)
	    
```

