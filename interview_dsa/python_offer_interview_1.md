### 21 调整数组顺序使奇数位于偶数前面


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





判断奇偶的方法： nums[left] & 1 == 1 是奇数，否则是偶数

双指针：首尾双指针，快慢双指针

### 22 合并两个有序链表

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
		
		
a,b  = b,c ----> a = b    b = c
		
非交换传数

### 26 树的子结构

	
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A,B):
            if B == None:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left,B.left) and recur(A.right,B.right)

        return bool(A and B) and (recur(A,B) or  self.isSubStructure(A.left,B) or  self.isSubStructure(A.right,B))	
	


if not A 判空法

树天生为了递归左右子树而存在


二叉树的："recur  +   isSub法"

### 27  二叉树的镜像

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        left = self.mirrorTree(root.right)
        right = self.mirrorTree(root.left)

        root.left,root.right = left,right

        return root

### 28 对称的二叉树


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

		
连续 not 判断
