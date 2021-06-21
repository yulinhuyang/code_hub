### 12 矩阵中的路径

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


### 13  机器人的运动范围

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

### 14 减绳子

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


### 15 二进制中1的个数

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

### 16 数值的整数次方

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

### 17 打印从1到最大的n位数

```python
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10 ** n):
            res.append(i)
        return res
```

**  乘方

### 18  删除链表的节点

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

