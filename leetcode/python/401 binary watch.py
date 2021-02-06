## 题目描述

```
二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。
```
![](https://tva1.sinaimg.cn/large/0081Kckwly1gm5szmnbinj31400u0tra.jpg)

```
例如，上面的二进制手表读取 “3:25”。

给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

 

示例：

输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
 

提示：

输出的顺序没有要求。
小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。
超过表示范围（小时 0-11，分钟 0-59）的数据将会被舍弃，也就是说不会出现 "13:00", "0:61" 等时间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-watch
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```

## 前置知识

- 笛卡尔积
- [回溯


## 代码

```py
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        def possible_number(count, minute=False):
            if count == 0: return [0]
            if minute:
                return filter(lambda a: a < 60, map(sum, combinations([1, 2, 4, 8, 16, 32], count)))
            return filter(lambda a: a < 12, map(sum, combinations([1, 2, 4, 8], count)))
        ans = set()
        for i in range(min(4, num + 1)):
            for a in possible_number(i):
                for b in possible_number(num - i, True):
                    ans.add(str(a) + ":" + str(b).rjust(2, '0'))
        return list(ans)
```


进一步思考，实际上，我们要找的就是 a 和 b 相加等于 num，并且 a 和 b 就是二进制表示中 1 的个数。 因此可以将逻辑简化为：


```py
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        return [str(a) + ":" + str(b).rjust(2, '0') for a in range(12) for b in range(60) if (bin(a)+bin(b)).count('1') == num]
