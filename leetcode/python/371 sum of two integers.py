
## 题目描述

```
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1

```

## 前置知识

- [位运算]



## 关键点解析

- 位运算
- 异或是一种不进位的加减法
- 求与之后左移一位来可以表示进位


Python Code:
```python
# python整数类型为Unifying Long Integers, 即无限长整数类型.
# 模拟 32bit 有符号整型加法
class Solution:
    def getSum(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            carry = a & b
            a ^= b
            b = ((carry) << 1) & 0xFFFFFFFF
            # print((a, b))
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)