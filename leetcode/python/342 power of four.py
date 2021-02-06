## 题目描述

```
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:

输入: 16
输出: true
示例 2:

输入: 5
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？

```


如果一个数字是 4 的幂次方，那么只需要满足：

1. 是二的倍数
2. 减去 1 是三的倍数

代码如下：

```js
return num > 0 && (num & (num - 1)) === 0 && (num - 1) % 3 === 0;
```

## 关键点

- 数论
- 2的幂次方特点（数学性质以及二进制表示）
- 4的幂次方特点（数学性质以及二进制表示）

#azl


Python Code:

```python
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        elif num < 4:
            return False
        else:
            if not num & (num-1) == 0:
                return False
            else:
                return num & 0x55555555 == num

    # 另一种解法：将数字转化为二进制表示的字符串，利用字符串的相关操作进行判断
    def isPowerOfFour(self, num: int) -> bool:
        binary_num = bin(num)[2:]
        return binary_num.strip('0') == '1' and len(binary_num) % 2 == 1
```