

#### 09. 用两个栈实现队列

class CQueue:

    def __init__(self):

        self.stack_list1 = []
        self.stack_list2 = []


    def appendTail(self, value: int) -> None:

        self.stack_list1.append(value)

        return value

    def deleteHead(self) -> int:

        if self.stack_list2  == []:
            while len(self.stack_list1)!=0:
                self.stack_list2.append(self.stack_list1.pop(-1))

        if self.stack_list2 == []:
            return -1
        else:
            value = self.stack_list2.pop(-1)
            return value

#### 11. 旋转数组的最小数字

class Solution:
    def minArray(self, numbers: List[int]) -> int:

        low = 0
        high = len(numbers)-1

        while low < high:
            mid = int((high + low )/2)
            if numbers[mid] > numbers[high]:
                low = mid +1 
            elif numbers[mid] < numbers[high]:
                high = mid
            else:
                high = high - 1

        return numbers[low]


#### 12 矩阵中的路径

 ```python
    class Solution:
        def exist(self, board: List[List[str]], word: str) -> bool:

            def dfs(i,j,k):
                if not  0 <= i < len(board) or  not   0 <= j < len(board[0]) or board[i][j]!= word[k]:
                    return False 

                if k  == len(word) - 1:
                    return True

                board[i][j] = ''
                res = dfs(i-1,j,k+1) or dfs(i+1,j,k+1) or dfs(i,j-1,k+1) or dfs(i,j+1,k+1)
                board[i][j] = word[k]

                return res 

            for i in range(len(board)):
                for j in range(len(board[0])):
                   if dfs(i,j,0):
                       return True

            return False
 ```           
**Notes**

注意这里的board[i][j] = '' 操作，再board[i][j]=word[k]撤销操作


#### 13  机器人的运动范围

 ```python
    def digit_num(num):
        sum = 0
        while num:
            sum = sum + num%10
            num = num//10
        return sum

    class Solution:
            def movingCount(self, m: int, n: int, k: int) -> int:

                vis = set([(0,0)])

                for i in range(m):
                    for j in range(n):
                        if ((i-1,j) in vis or (i,j-1) in vis) and digit_num(i) + digit_num(j) <= k:
                            vis.add((i,j))

                return len(vis)
```


**Notes:**

**set**

用set来表示一个无序不重复元素的序列。set的只要作用就是用来给数据去重。 

可以使用大括号 { } 或者 set() 函数创建集合

eg: 

添加一对数：

vis = set([(0, 0)])

vis.add((i, j))


/ 除以，带小数

//整除

**dict**

创建字典：

d = {key1 : value1, key2 : value2 }

eg；

dict = {'a': 1, 'b': 2, 'b': '3'}

**tuple**

tup1 = ('physics', 'chemistry', 1997, 2000)

#### 14 减绳子

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        
        
        if n <=3: 
            return  n - 1
        
        a = n // 3
        b = n % 3
        if b == 0:
            return int(math.pow(3,a))   
        if b == 1:
            return int(math.pow(3,a-1)*4)
        
        return int(math.pow(3,a)*b)
``` 
 
notes: 

求幂 math.pow()

枚举归纳法


#### 15 二进制中1的个数

```python

class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n:
            n = n&(n-1)
            sum = sum + 1
                    
        return sum
```
		
二进制串读入

一定要先枚举分析题，举例测试题	

#### 16 数值的整数次方

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            x = 1/x
            n = -n
        
        result = 1.0
        while n:
            if n&1:
                result = result * x
            n = n >> 1
            x = x * x
        
        return result  
```

快速幂解析（二分法角度）

移位 + 快速幂

#### 17 打印从1到最大的n位数

```python
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10 ** n):
            res.append(i)
        return res
```

**  乘方

#### 18  删除链表的节点

```python
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        
        if head.val == val:
            return head.next
        
        pre = head
        cur = head.next
        
        while cur  and cur.val != val:
            pre = cur
            cur = cur.next
        
        if cur:
            pre.next = cur.next
        
        return head
```

pre cur  双指针循进

python传值和引用,

值传：列表、字典、集合

引用传：数值、元组、字符串



#### 19 字符串匹配

超时解法：

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = p

        if s == pattern:
            return True
        if not pattern:
            return False
        if len(pattern)>1 and pattern[1] == '*':
            if(s and s[0]==pattern[0]) or (s and pattern[0] == '.'):
                return self.isMatch(s,pattern[2:]) \
                    or self.isMatch(s[1:],pattern) \
                    or self.isMatch(s[1:],pattern[2:])
            else:
                return self.isMatch(s,pattern[2:])
        elif s and (s[0] == pattern[0] or pattern[0]=='.'):
                return self.isMatch(s[1:],pattern[1:])
        return False
 
 
str可以直接切片使用

DP解法：

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def match(i,j)->bool:
            if i == 0:
                return False
            if s[i-1] == p[j-1] or p[j-1] == '.':
                return  True   
            return False
            
        m = len(s)
        n = len(p)
        
        dp = [[False]*(n+1) for i in range(m+1)]
        dp[0][0] = True
        
        for i in range(m+1):
            for j in range(1,n+1):
               if p[j-1]== '*':
                    dp[i][j] |= dp[i][j-2]
                    if match(i,j-1):
                        dp[i][j] |= dp[i-1][j]
               else:
                   if match(i,j):
                        dp[i][j] |= dp[i-1][j-1]
        
        return dp[m][n]
```
		
dp[i][j]:表示s的前i个字符和p中的前j个字符是否匹配。

dp数字、循环大小都要用size+1 

第i个和实际索引i-1的对应关系问题
		
穷举（写出状态方程，暴力穷举）--->备忘录消除重叠子问题（自顶而下的递归）--->自底而上的迭代解法

	#初始化base case
	dp[0][0][...] = base

	#进行状态转移
	for 状态1  in 状态1的所有取值：
		for 状态2 in 状态2的所有取值：
			for ..
				dp[状态1][状态2][..] = 求最值（选择1，选择2...）

python 没有++运算符，只有 a+=1

not bool的结构

#### 20  表示数值的字符串


```python
class Solution:
    def isNumber(self, s: str) -> bool:
        
        n = len(s)
        index = 0
        has_num = has_e = has_dot = has_sign = False
        while index < n and  s[index]== ' ':
            index = index + 1
        while index < n:
            while (index < n and '0' <= s[index] <= '9'):
                index = index + 1
                has_num = True
            if index == n:
                break
            
            if s[index] == 'e' or s[index] == 'E':
                if has_e or not has_num:
                    return False
                has_e = True
                has_num = has_dot = has_sign = False
            elif s[index] == '+' or s[index] == '-':
                if has_num or has_dot or has_sign:
                    return False
                has_sign = True
            elif s[index] == '.':
                if has_dot or has_e:
                    return False
                has_dot = True
            elif s[index] == ' ':
                break
            else:
                return False
            index = index + 1
            
        while index < n and s[index] == ' ':
            index = index + 1
        return has_num and index == n 
```

bool_after_dot = (len(s[index+1:]) >= 1) and ('0' <= s[index + 1] <= '9') 

bool 条件，兼容判断长度

bool 标记法

#### 21 调整数组顺序使奇数位于偶数前面

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

#### 22 合并两个有序链表

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

#### 26 树的子结构

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

#### 27  二叉树的镜像

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

#### 28 对称的二叉树

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


#### 22 链表中倒数第k个节点

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


#### 23  反转链表

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


#### 24  复杂链表的复制


##### 方法1: 链表法  复制-调整-拆分

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

##### 方法2: 字典法

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
