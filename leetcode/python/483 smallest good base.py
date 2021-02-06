
## 题目描述

```
对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。

以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。

 

示例 1：

输入："13"
输出："3"
解释：13 的 3 进制是 111。
示例 2：

输入："4681"
输出："8"
解释：4681 的 8 进制是 11111。
示例 3：

输入："1000000000000000000"
输出："999999999999999999"
解释：1000000000000000000 的 999999999999999999 进制是 11。
 

提示：

n的取值范围是 [3, 10^18]。
输入总是有效且没有前导 0。

```

## 前置知识

- 二分法
- 进制转换


## 关键点解析

- 利用等比数列求和公式可降低时间复杂度
- 从进制转换入手发现单调性，从而使用二分解决

## 代码

代码支持：Python3

Python3 Code:

```python
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        # 上面提到的 base 进制转十进制公式。
        # 使用等比数列求和公式可简化时间复杂度
        def sum_with(base, N):
            return (1 - base ** N) // (1 - base)
            # return sum(1 * base ** i for i in range(N))
        # bin(n) 会计算出 n 的二进制表示， 其会返回形如 '0b10111' 的字符串，因此需要减去 2。
        for N in range(len(bin(n)) - 2, 0, -1):
            l = 2
            r = n - 1
            while l <= r:
                mid = (l + r) // 2
                v = sum_with(mid, N)

                if v < n:
                    l = mid + 1
                elif v > n:
                    r = mid - 1
                else:
                    return str(mid)
