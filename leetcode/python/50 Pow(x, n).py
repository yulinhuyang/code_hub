## 题目描述

```
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。


## 解法零 - 遍历法

语言支持: Python3

Python3 Code:

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        res = 1
        for _ in range(n):
            res *= x
        return res
```

## 解法一 - 普通递归（超时法）

### 代码

语言支持: Python3

Python3 Code:

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)
        return self.myPow(x, n // 2) * self.myPow(x, n - n // 2)
```


## 解法二 - 优化递归

Python3 Code:

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)
        return self.myPow(x _ x, n // 2) if n % 2 == 0 else x _ self.myPow(x, n - 1)
```

## 解法三 - 位运算

语言支持: Python3

Python3 Code:

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        res = 1
        while n:
            if n & 1 == 1:
                res *= x
            x *= x
            n >>= 1
        return res
```

