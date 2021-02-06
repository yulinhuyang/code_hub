## 题目描述

```
机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：

-2：向左转 90 度
-1：向右转 90 度
1 <= x <= 9：向前移动 x 个单位长度
在网格上有一些格子被视为障碍物。

第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])

如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。

返回从原点到机器人的最大欧式距离的平方。

 

示例 1：

输入: commands = [4,-1,3], obstacles = []
输出: 25
解释: 机器人将会到达 (3, 4)
示例 2：

输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
输出: 65
解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
 

提示：

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
答案保证小于 2 ^ 31


```

## 前置知识

- hashtable


## 关键点解析

- 理解题意，这道题容易理解错题意，求解为`最终位置距离原点的距离`
- 建立坐标系
- 空间换时间

## 代码

代码支持： Python3

Python3 Code:

```python
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pos = [0, 0]
        deg = 90
        ans = 0
        obstaclesSet = set(map(tuple, obstacles))

        for command in commands:
            if command == -1:
                deg = (deg + 270) % 360
            elif command == -2:
                deg = (deg + 90) % 360
            else:
                if deg == 0:
                    i = 0
                    while i < command and not (pos[0] + 1, pos[1]) in obstaclesSet:
                        pos[0] += 1
                        i += 1
                if deg == 90:
                    i = 0
                    while i < command and not (pos[0], pos[1] + 1) in obstaclesSet:
                        pos[1] += 1
                        i += 1
                if deg == 180:
                    i = 0
                    while i < command and not (pos[0] - 1, pos[1]) in obstaclesSet:
                        pos[0] -= 1
                        i += 1
                if deg == 270:
                    i = 0
                    while i < command and not (pos[0], pos[1] - 1) in obstaclesSet:
                        pos[1] -= 1
                        i += 1
                ans = max(ans, pos[0] ** 2 + pos[1] ** 2)
        return ans
```