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



### 19 字符串匹配

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

### 20  表示数值的字符串


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

