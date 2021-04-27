## 第一章  动态规划系列

### 1 动态规划设计：最长递增子序列

300.最长上升子序列

给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

 
示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。


dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度。

#### 1.1 动态规划解法 


结合我们刚才说的 base case，下面我们看一下完整代码：

```java
public int lengthOfLIS(int[] nums) {
    int[] dp = new int[nums.length];
    // base case：dp 数组全都初始化为 1
    Arrays.fill(dp, 1);
    for (int i = 0; i < nums.length; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) 
                dp[i] = Math.max(dp[i], dp[j] + 1);
        }
    }
    
    int res = 0;
    for (int i = 0; i < dp.length; i++) {
        res = Math.max(res, dp[i]);
    }
    return res;
}
```


#### 1.2 二分查找解法

首先，给你一排扑克牌，我们像遍历数组那样从左到右一张一张处理这些扑克牌，最终要把这些牌分成若干堆。

只能把点数小的牌压到点数比它大的牌上；如果当前牌点数较大没有可以放置的堆，则新建一个堆，把这张牌放进去；如果当前牌有多个堆可供选择，则选择最左边的那一堆放置。

比如说上述的扑克牌最终会被分成这样 5 堆（我们认为纸牌 A 的牌面是最大的，纸牌 2 的牌面是最小的）。

**处理这些扑克牌要遵循以下规则**：

只能把点数小的牌压到点数比它大的牌上；如果当前牌点数较大没有可以放置的堆，则新建一个堆，把这张牌放进去；如果当前牌有多个堆可供选择，则选择最左边的那一堆放置。


```java
public int lengthOfLIS(int[] nums) {
    int[] top = new int[nums.length];
    // 牌堆数初始化为 0
    int piles = 0;
    for (int i = 0; i < nums.length; i++) {
        // 要处理的扑克牌
        int poker = nums[i];

        /***** 搜索左侧边界的二分查找 *****/
        int left = 0, right = piles;
        while (left < right) {
            int mid = (left + right) / 2;
            if (top[mid] > poker) {
                right = mid;
            } else if (top[mid] < poker) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        /*********************************/
        
        // 没找到合适的牌堆，新建一堆
        if (left == piles) piles++;
        // 把这张牌放到牌堆顶
        top[left] = poker;
    }
    // 牌堆数就是 LIS 长度
    return piles;
}
```

#### 1.3 其他语言

**python**

```python 动态规划
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1] * (n)

        for i in range(n):
            for j in range(i):
                if nums[j]  < nums[i]:
                    f[i] = max(f[i], f[j] + 1)
        
        res = 0
        for i in range(n):
            res = max(res, f[i])
        return res
```

```python 二分查找
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []

        def find_index(num):
            l, r = 0, len(stack)
            while l < r:
                mid = l + r >> 1
                if stack[mid] >= num:
                    r = mid 
                else:
                    l = mid + 1

            return r


        for num in nums:
            if not stack or num > stack[-1]:
                stack.append(num)
            else:
                position = find_index(num)
                stack[position] = num

        return len(stack)
```



**c++**

[Kian](https://github.com/KianKw/) 提供 C++ 代码

```c++
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        /* len 为牌的数量 */
        int len = nums.size();
        vector<int> top(len, 0);
        /* 牌堆数初始化为0 */
        int piles = 0;
        for (int i = 0; i < len; i++) {
            /* nums[i] 为要处理的扑克牌 */
            int poker = nums[i];

            /***** 搜索左侧边界的二分查找 *****/
            int left = 0, right = piles;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (top[mid] > poker) {
                    right = mid;
                } else if (top[mid] < poker) {
                    left = mid + 1;
                } else if (top[mid] == poker) {
                    right = mid;
                }
            }
            /*********************************/

            /* 没找到合适的牌堆，新建一堆 */
            if (left == piles)
                piles++;
            /* 把这张牌放到牌堆顶 */
            top[left] = poker;
        }
        /* 牌堆数就是 LIS 长度 */
        return piles;
    }
};
```

### 2 编辑距离

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 
示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')


#### 2.1 base 

编辑距离问题就是给我们两个字符串 `s1` 和 `s2`，只能用三种操作，让我们把 `s1` 变成 `s2`，求最少的操作数。需要明确的是，不管是把 `s1` 变成 `s2` 还是反过来，结果都是一样的，所以后文就以 `s1` 变成 `s2` 举例。

前文「最长公共子序列」说过，**解决两个字符串的动态规划问题，一般都是用两个指针 `i,j` 分别指向两个字符串的最后，然后一步步往前走，缩小问题的规模**。

```python
def minDistance(s1, s2) -> int:

    def dp(i, j):
        # base case
        if i == -1: return j + 1
        if j == -1: return i + 1
        
        if s1[i] == s2[j]:
            return dp(i - 1, j - 1)  # 啥都不做
        else:
            return min(
                dp(i, j - 1) + 1,    # 插入
                dp(i - 1, j) + 1,    # 删除
                dp(i - 1, j - 1) + 1 # 替换
            )
    
    # i，j 初始化指向最后一个索引
    return dp(len(s1) - 1, len(s2) - 1)
```

#### 2.2 动态规划优化

```python
def minDistance(s1, s2) -> int:

    memo = dict() # 备忘录
    def dp(i, j):
        if (i, j) in memo: 
            return memo[(i, j)]
        ...
        
        if s1[i] == s2[j]:
            memo[(i, j)] = ...  
        else:
            memo[(i, j)] = ...
        return memo[(i, j)]
    
    return dp(len(s1) - 1, len(s2) - 1)
```

既然 dp 数组和递归 dp 函数含义一样，也就可以直接套用之前的思路写代码，**唯一不同的是，DP table 是自底向上求解，递归解法是自顶向下求解**：

```java
int minDistance(String s1, String s2) {
    int m = s1.length(), n = s2.length();
    int[][] dp = new int[m + 1][n + 1];
    // base case 
    for (int i = 1; i <= m; i++)
        dp[i][0] = i;
    for (int j = 1; j <= n; j++)
        dp[0][j] = j;
    // 自底向上求解
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++)
            if (s1.charAt(i-1) == s2.charAt(j-1))
                dp[i][j] = dp[i - 1][j - 1];
            else               
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i-1][j-1] + 1
                );
    // 储存着整个 s1 和 s2 的最小编辑距离
    return dp[m][n];
}

int min(int a, int b, int c) {
    return Math.min(a, Math.min(b, c));
}
```

####  2.3 扩展延伸

你可能还会问，**这里只求出了最小的编辑距离，那具体的操作是什么**？你之前举的修改公众号文章的例子，只有一个最小编辑距离肯定不够，还得知道具体怎么修改才行。

这个其实很简单，代码稍加修改，给 dp 数组增加额外的信息即可：

```java
// int[][] dp;
Node[][] dp;

class Node {
    int val;
    int choice;
    // 0 代表啥都不做
    // 1 代表插入
    // 2 代表删除
    // 3 代表替换
}
```

#### 2.4 其他语言

[ChenjieXu](https://github.com/ChenjieXu) 提供Python版本[72.编辑距离](https://leetcode-cn.com/problems/edit-distance)代码：  

```python
def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    # 创建 DP 数组
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # base case初始化
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # 自底向上求解
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 状态转移方程
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, 
                               dp[i][j - 1] + 1,
                               dp[i - 1][j - 1] + 1)
    # 储存着整个 word1 和 word2 的最小编辑距离
    return dp[m][n]
````

### 3 高楼扔鸡蛋问题

给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。

已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。

每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。

请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？

 
示例 1：

输入：k = 1, n = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。 
否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。 
如果它没碎，那么肯定能得出 f = 2 。 
因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。 


#### 3.1 base

*「状态」很明显，就是当前拥有的鸡蛋数 `K` 和需要测试的楼层数 `N`**。随着测试的进行，鸡蛋个数可能减少，楼层的搜索范围会减小，这就是状态的变化。

**「选择」其实就是去选择哪层楼扔鸡蛋**。回顾刚才的线性扫描和二分思路，二分查找每次选择到楼层区间的中间去扔鸡蛋，而线性扫描选择一层层向上测试。不同的选择会造成状态的转移。


```python
def superEggDrop(K: int, N: int):

    memo = dict()
    def dp(K, N) -> int:
        # base case
        if K == 1: return N
        if N == 0: return 0
        # 避免重复计算
        if (K, N) in memo:
            return memo[(K, N)]

        res = float('INF')
        # 穷举所有可能的选择
        for i in range(1, N + 1):
            res = min(res, 
                      max(
                            dp(K, N - i), 
                            dp(K - 1, i - 1)
                         ) + 1
                  )
        # 记入备忘录
        memo[(K, N)] = res
        return res
    
    return dp(K, N)
```

#### 3.2 优化

```python
def superEggDrop(self, K: int, N: int) -> int:
        
    memo = dict()
    def dp(K, N):
        if K == 1: return N
        if N == 0: return 0
        if (K, N) in memo:
            return memo[(K, N)]
                            
        # for 1 <= i <= N:
        #     res = min(res, 
        #             max( 
    #                     dp(K - 1, i - 1), 
    #                     dp(K, N - i)      
        #                 ) + 1 
        #             )

        res = float('INF')
        # 用二分搜索代替线性搜索
        lo, hi = 1, N
        while lo <= hi:
            mid = (lo + hi) // 2
            broken = dp(K - 1, mid - 1) # 碎
            not_broken = dp(K, N - mid) # 没碎
            # res = min(max(碎，没碎) + 1)
            if broken > not_broken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, not_broken + 1)

        memo[(K, N)] = res
        return res
    
    return dp(K, N)
```

### 4 高楼扔鸡蛋（进阶）


#### 4.1 优化

```python
def superEggDrop(self, K: int, N: int) -> int:
        
    memo = dict()
    def dp(K, N):
        if K == 1: return N
        if N == 0: return 0
        if (K, N) in memo:
            return memo[(K, N)]
                            
        # for 1 <= i <= N:
        #     res = min(res, 
        #             max( 
        #                 dp(K - 1, i - 1), 
        #                 dp(K, N - i)      
        #                 ) + 1 
        #             )

        res = float('INF')
        # 用二分搜索代替线性搜索
        lo, hi = 1, N
        while lo <= hi:
            mid = (lo + hi) // 2
            broken = dp(K - 1, mid - 1) # 碎
            not_broken = dp(K, N - mid) # 没碎
            # res = min(max(碎，没碎) + 1)
            if broken > not_broken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, not_broken + 1)

        memo[(K, N)] = res
        return res
    
    return dp(K, N)
```

### 5 最长回文子序列问题 解题模板

给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。


示例 1:
输入:

"bbbab"
输出:

4


#### 5.1 思路 

**1、第一种思路模板是一个一维的 dp 数组**：

```java
int n = array.length;
int[] dp = new int[n];

for (int i = 1; i < n; i++) {
    for (int j = 0; j < i; j++) {
        dp[i] = 最值(dp[i], dp[j] + ...)
    }
}
```

举个我们写过的例子「最长递增子序列」，在这个思路中 dp 数组的定义是：

**在子数组 `array[0..i]` 中，我们要求的子序列（最长递增子序列）的长度是 `dp[i]`**。

为啥最长递增子序列需要这种思路呢？前文说得很清楚了，因为这样符合归纳法，可以找到状态转移的关系，这里就不具体展开了。

**2、第二种思路模板是一个二维的 dp 数组**：

```java
int n = arr.length;
int[][] dp = new dp[n][n];

for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        if (arr[i] == arr[j]) 
            dp[i][j] = dp[i][j] + ...
        else
            dp[i][j] = 最值(...)
    }
}
```

**2.1 涉及两个字符串/数组时**（比如最长公共子序列），dp 数组的含义如下：

**在子数组 `arr1[0..i]` 和子数组 `arr2[0..j]` 中，我们要求的子序列（最长公共子序列）长度为 `dp[i][j]`**。

**2.2 只涉及一个字符串/数组时**（比如本文要讲的最长回文子序列），dp 数组的含义如下：

**在子数组 `array[i..j]` 中，我们要求的子序列（最长回文子序列）的长度为 `dp[i][j]`**。

第一种情况可以参考这两篇旧文：「编辑距离」「公共子序列」

下面就借最长回文子序列这个问题，详解一下第二种情况下如何使用动态规划。

#### 5.2 实现

这类问题都是让你求一个最长子序列，因为最短子序列就是一个字符嘛，没啥可问的。一旦涉及到子序列和最值，那几乎可以肯定，考察的是动态规划技巧，时间复杂度一般都是 O(n^2)。

```cpp
int longestPalindromeSubseq(string s) {
    int n = s.size();
    // dp 数组全部初始化为 0
    vector<vector<int>> dp(n, vector<int>(n, 0));
    // base case
    for (int i = 0; i < n; i++)
        dp[i][i] = 1;
    // 反着遍历保证正确的状态转移
    for (int i = n - 1; i >= 0; i--) {
        for (int j = i + 1; j < n; j++) {
            // 状态转移方程
            if (s[i] == s[j])
                dp[i][j] = dp[i + 1][j - 1] + 2;
            else
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
        }
    }
    // 整个 s 的最长回文子串长度
    return dp[0][n - 1];
}
```


### 6 动态规划之博弈问题

亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。

游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。

亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。

假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。


示例：

	输入：[5,3,4,5]
	输出：true
	解释：
	亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
	假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
	如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
	如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
	这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。


#### 6.1 博弈问题

可以注意一下斜着遍历数组的技巧

```java
/* 返回游戏最后先手和后手的得分之差 */
int stoneGame(int[] piles) {
    int n = piles.length;
    // 初始化 dp 数组
    Pair[][] dp = new Pair[n][n];
    for (int i = 0; i < n; i++) 
        for (int j = i; j < n; j++)
            dp[i][j] = new Pair(0, 0);
    // 填入 base case
    for (int i = 0; i < n; i++) {
        dp[i][i].fir = piles[i];
        dp[i][i].sec = 0;
    }
    // 斜着遍历数组
    for (int l = 2; l <= n; l++) {
        for (int i = 0; i <= n - l; i++) {
            int j = l + i - 1;
            // 先手选择最左边或最右边的分数
            int left = piles[i] + dp[i+1][j].sec;
            int right = piles[j] + dp[i][j-1].sec;
            // 套用状态转移方程
            if (left > right) {
                dp[i][j].fir = left;
                dp[i][j].sec = dp[i+1][j].fir;
            } else {
                dp[i][j].fir = right;
                dp[i][j].sec = dp[i][j-1].fir;
            }
        }
    }
    Pair res = dp[0][n-1];
    return res.fir - res.sec;
}
```

#### 6.2 其他语言实现

**python实现**

由[SCUHZS](https://github.com/brucecat)提供

这里采取的是三维的做法

```python
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        # 初始化一个n*n的矩阵 dp数组
        dp = [[None] * n for i in range(0, n)]

        # 在三角区域填充
        for i in range(n):
            for j in range(i, n):
                dp[i][j] = [0, 0]

        # 填入base case
        for i in range(0, n):
            dp[i][i][0] = piles[i]
            dp[i][i][1] = 0

        # 斜着遍历数组
        for l in range(2, n + 1):
            for i in range(0, n-l+1):
                j = l + i - 1


                # 先手选择最左边或最右边的分数
                left = piles[i] + dp[i + 1][j][1]
                right = piles[j] + dp[i][j - 1][1]

                # 套用状态转移方程
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j - 1][0]

        res = dp[0][n - 1]

        return res[0] - res[1] > 0

```



压缩成一维数组，以减小空间复杂度，做法如下。

```python
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = piles.copy()

        for i in range(len(piles) - 1, -1, -1):  # 从下往上遍历
            for j in range(i, len(piles)):       # 从前往后遍历
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])  # 计算之后覆盖一维数组的对应位置

        return dp[len(piles) - 1] > 0
        

```


**C++ 版本实现**

由 [TCeason](https://github.com/TCeason) 提供

这里采用 hash map 来解决问题

```cpp
class Solution {
public:
    unordered_map<int, int> memo;

    int dfs(vector<int> &piles, int index) {
        // 从两边向中间获取
        // index 值为 1/2 piles.size() 时可以停止算法
        if (index == piles.size() / 2)
            return 0;

        // 减少计算，快速返回已有结果
        if (memo.count(index))
            return memo[index];

        // 防止第一次取最右时越界
        int n = piles.size() - 1;

        // 先手选择最左边或最右边后的分数
        int l = piles[index] + dfs(piles, index + 1);
        int r = piles[n - index] + dfs(piles, index + 1);

        // 返回先手左或右边的最高分
        return memo[index] = max(l, r);
    }

   bool stoneGame(vector<int>& piles) {
        // 最佳发挥时：
        // 先手得分 * 2 > 总大小 则先手者胜利
        return dfs(piles, 0) * 2 > accumulate(begin(piles), end(piles), 0);
    }
};

```


### 7 贪心算法之区间调度问题

很经典的贪心算法问题 Interval Scheduling（区间调度问题）。给你很多形如 [start, end] 的闭区间，请你设计一个算法，算出这些区间中最多有几个互不相交的区间。

int intervalSchedule(int[][] intvs) {}

举个例子，intvs = [[1,3], [2,4], [3,6]]，这些区间最多有 2 个区间互不相交，即 [[1,3], [3,6]]，你的算法应该返回 2。注意边界相同并不算相交。

#### 7.1 区间调度实现


```java
int findMinArrowShots(int[][] intvs) {
    // ...

    for (int[] interval : intvs) {
        int start = interval[0];
        // 把 >= 改成 > 就行了
        if (start > x_end) {
            count++;
            x_end = interval[1];
        }
    }
    return count;
}
```

#### 7.2 python实现

Edwenc 提供 第435题的python3 代码：

```python  
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ###  思路是首先找到不重叠的区间的个数
        ###  然后再用总个数减去不重叠个数  
        ###  获得的就是  需要移除的个数

        #  首先获得区间的个数  为0的话就不用移除
        n = len(intervals)
        if n==0:
            return 0

        #  按照每个区间的右端点值进行排序
        sorted_list = sorted( intervals , key=lambda x: x[1] )

        #  不重叠区间个数至少是1
        count = 1

        #  end是所有不重叠的区间中  最大的右端点
        #  end的初始值即是sorted_list[0]的右端点
        end = sorted_list[0][1]

        #  从1开始往后找  因为0在上面已经取过了
        for i in range(1,n):
            #  start是当前区间左端点值
            start = sorted_list[i][0] 
            #  如果当前左端点比最大右端点都大了（可能相等）  
            #  说明两区间不重叠  count+1  再更新end     
            if start>=end:
                count += 1
                end = sorted_list[i][1]

        #  最后返回的是  需要移除的区间个数
        return n-count
```

### 8 动态规划之KMP字符匹配算法

#### 8.1 kmp 与 状态机概述

KMP 算法的完整代码吧：

```java
public class KMP {
    private int[][] dp;
    private String pat;

    public KMP(String pat) {
        this.pat = pat;
        int M = pat.length();
        // dp[状态][字符] = 下个状态
        dp = new int[M][256];
        // base case
        dp[0][pat.charAt(0)] = 1;
        // 影子状态 X 初始为 0
        int X = 0;
        // 构建状态转移图（稍改的更紧凑了）
        for (int j = 1; j < M; j++) {
            for (int c = 0; c < 256; c++)
                dp[j][c] = dp[X][c];
            dp[j][pat.charAt(j)] = j + 1;
            // 更新影子状态
            X = dp[X][pat.charAt(j)];
        }
    }

    public int search(String txt) {
        int M = pat.length();
        int N = txt.length();
        // pat 的初始态为 0
        int j = 0;
        for (int i = 0; i < N; i++) {
            // 计算 pat 的下一个状态
            j = dp[j][txt.charAt(i)];
            // 到达终止态，返回结果
            if (j == M) return i - M + 1;
        }
        // 没到达终止态，匹配失败
        return -1;
    }
}
```


#### 8.2 python实现

[MoguCloud](https://github.com/MoguCloud) 提供 实现 strStr() 的 Python 完整代码：

```python
class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    # 边界条件判断
    if not needle:
      return 0
    pat = needle
    txt = haystack

    M = len(pat)
    # dp[状态][字符] = 下个状态
    dp = [[0 for _ in range(256)] for _ in pat]
    # base case
    dp[0][ord(pat[0])] = 1
    # 影子状态 X 初始化为 0
    X = 0
    for j in range(1, M):
      for c in range(256):
        dp[j][c] = dp[X][c]
        dp[j][ord(pat[j])] = j + 1
        # 更新影子状态
        X = dp[X][ord(pat[j])]

        N = len(txt)
        # pat 初始状态为 0 
        j = 0
        for i in range(N):
          # 计算 pat 的下一个状态
          j = dp[j][ord(txt[i])]
          # 到达终止态，返回结果
          if j == M:
            return i - M + 1
          # 没到达终止态，匹配失败
          return -1
```

### 9 团灭 LeetCode 股票买卖问题

买卖股票的最佳时机

买卖股票的最佳时机 II

买卖股票的最佳时机 III

买卖股票的最佳时机 IV

最佳买卖股票时机含冷冻期

买卖股票的最佳时机含手续费

#### 分析

**k == 1**

```java

// k == 1
int maxProfit_k_1(int[] prices) {
    int n = prices.length;
    // base case: dp[-1][0] = 0, dp[-1][1] = -infinity
    int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
        // dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        // dp[i][1] = max(dp[i-1][1], -prices[i])
        dp_i_1 = Math.max(dp_i_1, -prices[i]);
    }
    return dp_i_0;
}
```

**第二题，k = +infinity**

```java
int maxProfit_k_inf(int[] prices) {
    int n = prices.length;
    int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
        int temp = dp_i_0;
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        dp_i_1 = Math.max(dp_i_1, temp - prices[i]);
    }
    return dp_i_0;
}
```
**第三题，k = +infinity with cooldown**

每次 sell 之后要等一天才能继续交易。只要把这个特点融入上一题的状态转移方程即可：

```
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
解释：第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 。
```

翻译成代码：

```java
int maxProfit_with_cool(int[] prices) {
    int n = prices.length;
    int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
    int dp_pre_0 = 0; // 代表 dp[i-2][0]
    for (int i = 0; i < n; i++) {
        int temp = dp_i_0;
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        dp_i_1 = Math.max(dp_i_1, dp_pre_0 - prices[i]);
        dp_pre_0 = temp;
    }
    return dp_i_0;
}
```

**第四题，k = +infinity with fee**

每次交易要支付手续费，只要把手续费从利润中减去即可。改写方程：

```
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
解释：相当于买入股票的价格升高了。
在第一个式子里减也是一样的，相当于卖出股票的价格减小了。
```

直接翻译成代码：

```java
int maxProfit_with_fee(int[] prices, int fee) {
    int n = prices.length;
    int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
        int temp = dp_i_0;
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        dp_i_1 = Math.max(dp_i_1, temp - prices[i] - fee);
    }
    return dp_i_0;
}
```

**第五题，k = 2**

```java
dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
dp[i][1][1] = max(dp[i-1][1][1], -prices[i])

int maxProfit_k_2(int[] prices) {
    int dp_i10 = 0, dp_i11 = Integer.MIN_VALUE;
    int dp_i20 = 0, dp_i21 = Integer.MIN_VALUE;
    for (int price : prices) {
        dp_i20 = Math.max(dp_i20, dp_i21 + price);
        dp_i21 = Math.max(dp_i21, dp_i10 - price);
        dp_i10 = Math.max(dp_i10, dp_i11 + price);
        dp_i11 = Math.max(dp_i11, -price);
    }
    return dp_i20;
}
```

**第六题，k = any integer**

有了上一题 k = 2 的铺垫，这题应该和上一题的第一个解法没啥区别。但是出现了一个超内存的错误，原来是传入的 k 值会非常大，dp 数组太大了。现在想想，交易次数 k 最多有多大呢？

一次交易由买入和卖出构成，至少需要两天。所以说有效的限制 k 应该不超过 n/2，如果超过，就没有约束作用了，相当于 k = +infinity。这种情况是之前解决过的。

直接把之前的代码重用：

```java
int maxProfit_k_any(int max_k, int[] prices) {
    int n = prices.length;
    if (max_k > n / 2) 
        return maxProfit_k_inf(prices);

    int[][][] dp = new int[n][max_k + 1][2];
    for (int i = 0; i < n; i++) 
        for (int k = max_k; k >= 1; k--) {
            if (i - 1 == -1) { /* 处理 base case */ }
            dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
            dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]);     
        }
    return dp[n - 1][max_k][0];
}
```


### 10 团灭 LeetCode 打家劫舍问题

198.打家劫舍


你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。


示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。


213.打家劫舍II

337.打家劫舍III

#### 10.1 实现

House Robber I

```java
int rob(int[] nums) {
    int n = nums.length;
    // 记录 dp[i+1] 和 dp[i+2]
    int dp_i_1 = 0, dp_i_2 = 0;
    // 记录 dp[i]
    int dp_i = 0; 
    for (int i = n - 1; i >= 0; i--) {
        dp_i = Math.max(dp_i_1, nums[i] + dp_i_2);
        dp_i_2 = dp_i_1;
        dp_i_1 = dp_i;
    }
    return dp_i;
}
```


House Robber II

```java
public int rob(int[] nums) {
    int n = nums.length;
    if (n == 1) return nums[0];
    return Math.max(robRange(nums, 0, n - 2), 
                    robRange(nums, 1, n - 1));
}

// 仅计算闭区间 [start,end] 的最优结果
int robRange(int[] nums, int start, int end) {
    int n = nums.length;
    int dp_i_1 = 0, dp_i_2 = 0;
    int dp_i = 0;
    for (int i = end; i >= start; i--) {
        dp_i = Math.max(dp_i_1, nums[i] + dp_i_2);
        dp_i_2 = dp_i_1;
        dp_i_1 = dp_i;
    }
    return dp_i;
}
```

House Robber III

```java
Map<TreeNode, Integer> memo = new HashMap<>();
public int rob(TreeNode root) {
    if (root == null) return 0;
    // 利用备忘录消除重叠子问题
    if (memo.containsKey(root)) 
        return memo.get(root);
    // 抢，然后去下下家
    int do_it = root.val
        + (root.left == null ? 
            0 : rob(root.left.left) + rob(root.left.right))
        + (root.right == null ? 
            0 : rob(root.right.left) + rob(root.right.right));
    // 不抢，然后去下家
    int not_do = rob(root.left) + rob(root.right);
    
    int res = Math.max(do_it, not_do);
    memo.put(root, res);
    return res;
}
```

这道题就解决了，时间复杂度 O(N)，`N` 为数的节点数。

但是这道题让我觉得巧妙的点在于，还有更漂亮的解法。比如下面是我在评论区看到的一个解法：

```java
int rob(TreeNode root) {
    int[] res = dp(root);
    return Math.max(res[0], res[1]);
}

/* 返回一个大小为 2 的数组 arr
arr[0] 表示不抢 root 的话，得到的最大钱数
arr[1] 表示抢 root 的话，得到的最大钱数 */
int[] dp(TreeNode root) {
    if (root == null)
        return new int[]{0, 0};
    int[] left = dp(root.left);
    int[] right = dp(root.right);
    // 抢，下家就不能抢了
    int rob = root.val + left[0] + right[0];
    // 不抢，下家可抢可不抢，取决于收益大小
    int not_rob = Math.max(left[0], left[1])
                + Math.max(right[0], right[1]);
    
    return new int[]{not_rob, rob};
}
```

#### 10.2 python实现

[Shantom](https://github.com/Shantom) 提供 198. House Robber I Python3 解法代码：

```Python
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 当前，上一间，上上间
        cur, pre1, pre2 = 0, 0, 0  

        for num in nums:
            # 当前 = max(上上间+（抢当前），上间（放弃当前）)
            cur = max(pre2 + num, pre1)
            pre2 = pre1
            pre1 = cur

        return cur
```
[Shantom](https://github.com/Shantom) 提供 213. House Robber II Python3 解法代码：

```Python
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 只有一间时不成环
        if len(nums) == 1:
            return nums[0]

        # 该函数同198题
        def subRob(nums: List[int]) -> int:
            # 当前，上一间，上上间
            cur, pre1, pre2 = 0, 0, 0  
            for num in nums:
                # 当前 = max(上上间+（抢当前），上间（放弃当前）)
                cur = max(pre2 + num, pre1)
                pre2 = pre1
                pre1 = cur
            return cur
        
        # 不考虑第一间或者不考虑最后一间
        return max(subRob(nums[:-1]), subRob(nums[1:]))
```
[Shantom](https://github.com/Shantom) 提供 337. House Robber III Python3 解法代码：

```Python
class Solution:
    def rob(self, root: TreeNode) -> int:
        # 返回值0项为不抢该节点，1项为抢该节点
        def dp(root):
            if not root:
                return 0, 0

            left = dp(root.left)
            right = dp(root.right)
            
            # 抢当前，则两个下家不抢
            do = root.val + left[0] + right[0]
            # 不抢当前，则下家随意
            do_not = max(left) + max(right)

            return do_not, do
        
        return max(dp(root))
```


### 11 动态规划之四键键盘

651.四键键盘

假设你有一个特殊的键盘包含下面的按键：

Key 1: (A)：在屏幕上打印一个 'A'。

Key 2: (Ctrl-A)：选中整个屏幕。

Key 3: (Ctrl-C)：复制选中区域到缓冲区。

Key 4: (Ctrl-V)：将缓冲区内容输出到上次输入的结束位置，并显示在屏幕上。

现在，你只可以按键 N 次（使用上述四种按键），请问屏幕上最多可以显示几个 'A’呢？

	样例 1:
	输入: N = 3
	输出: 3
	解释: 
	我们最多可以在屏幕上显示三个'A'通过如下顺序按键：
	A, A, A


#### 11.1 实现

第一种思路：

```python
def maxA(N: int) -> int:
    # 备忘录
    memo = dict()
    def dp(n, a_num, copy):
        if n <= 0: return a_num;
        # 避免计算重叠子问题
        if (n, a_num, copy) in memo:
            return memo[(n, a_num, copy)]

        memo[(n, a_num, copy)] = max(
                # 几种选择还是一样的
            )
        return memo[(n, a_num, copy)]

    return dp(N, 0, 0)
```

第二种思路：

```java
public int maxA(int N) {
    int[] dp = new int[N + 1];
    dp[0] = 0;
    for (int i = 1; i <= N; i++) {
        // 按 A 键
        dp[i] = dp[i - 1] + 1;
        for (int j = 2; j < i; j++) {
            // 全选 & 复制 dp[j-2]，连续粘贴 i - j 次
            // 屏幕上共 dp[j - 2] * (i - j + 1) 个 A
            dp[i] = Math.max(dp[i], dp[j - 2] * (i - j + 1));
        }
    }
    // N 次按键之后最多有几个 A？
    return dp[N];
}
```


### 12 动态规划之正则表达


[10.正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/)

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

	'.' 匹配任意单个字符
	'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

 
	示例 1：

	输入：s = "aa" p = "a"
	输出：false
	解释："a" 无法匹配 "aa" 整个字符串。

 
#### 12.1 正则表达

比如说模式串 ".a*b" 就可以匹配文本 "zaaab"，也可以匹配 "cb"；模式串 "a..b" 可以匹配文本 "amnb"；而模式串 ".*" 就比较牛逼了，它可以匹配任何文本。

题目会给我们输入两个字符串 s 和 p，s 代表文本，p 代表模式串，请你判断模式串 p 是否可以匹配文本 s。我们可以假设模式串只包含小写字母和上述两种通配符且一定合法，不会出现 *a 或者 b** 这种不合法的模式串，

函数签名如下：

bool isMatch(string s, string p);

动态规划解法：

```cpp
/* 计算 p[j..] 是否匹配 s[i..] */
bool dp(string& s, int i, string& p, int j) {
    int m = s.size(), n = p.size();
    // base case
    if (j == n) {
        return i == m;
    }
    if (i == m) {
        if ((n - j) % 2 == 1) {
            return false;
        }
        for (; j + 1 < n; j += 2) {
            if (p[j + 1] != '*') {
                return false;
            }
        }
        return true;
    }

    // 记录状态 (i, j)，消除重叠子问题
    string key = to_string(i) + "," + to_string(j);
    if (memo.count(key)) return memo[key];
    
    bool res = false;
    
    if (s[i] == p[j] || p[j] == '.') {
        if (j < n - 1 && p[j + 1] == '*') {
            res = dp(s, i, p, j + 2)
               || dp(s, i + 1, p, j);
        } else {
            res = dp(s, i + 1, p, j + 1);
        }
    } else {
        if (j < n - 1 && p[j + 1] == '*') {
            res = dp(s, i, p, j + 2);
        } else {
            res = false;
        }
    }
    // 将当前结果记入备忘录
    memo[key] = res;
    
    return res;
}
```

#### 12.2 C++ 实现

```c++
class Solution {
public:
    map<string, bool> memo;
    bool isMatch(string s, string p) {
        // 指针 i，j 从索引 0 开始移动
        return dp(s, 0, p, 0);
    }

    /* 计算 p[j..] 是否匹配 s[i..] */
    bool dp(string& s, int i, string& p, int j) {
        int m = s.size(), n = p.size();
        // base case
        if (j == n) {
            return i == m;
        }
        if (i == m) {
            if ((n - j) % 2 == 1) {
                return false;
            }
            for (; j + 1 < n; j += 2) {
                if (p[j + 1] != '*') {
                    return false;
                }
            }
            return true;
        }

        // 记录状态 (i, j)，消除重叠子问题
        string key = to_string(i) + "," + to_string(j);
        if (memo.count(key)) return memo[key];
        
        bool res = false;
        
        if (s[i] == p[j] || p[j] == '.') {
            if (j < n - 1 && p[j + 1] == '*') {
                res = dp(s, i, p, j + 2)
                || dp(s, i + 1, p, j);
            } else {
                res = dp(s, i + 1, p, j + 1);
            }
        } else {
            if (j < n - 1 && p[j + 1] == '*') {
                res = dp(s, i, p, j + 2);
            } else {
                res = false;
            }
        }
        // 将当前结果记入备忘录
        memo[key] = res;
        
        return res;
    }
};
```

### 13 最长公共子序列

#### 13.1 描述

最长公共子序列（Longest Common Subsequence，简称 LCS）是一道非常经典的面试题目，因为它的解法是典型的二维动态规划，大部分比较困难的字符串问题都和这个问题一个套路，比如说编辑距离。而且，这个算法稍加改造就可以用于解决其他问题，所以说 LCS 算法是值得掌握的。

题目就是让我们求两个字符串的 LCS 长度：

```
输入: str1 = "abcde", str2 = "ace" 
输出: 3  
解释: 最长公共子序列是 "ace"，它的长度是 3
```

#### 13.2 其他语言实现

**c++**

[Edwenc](https://github.com/Edwenc) 提供 C++ 代码：

```C++
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        //  先计算两条字符串的长度
        int m = text1.size();
        int n = text2.size();

        //  构建dp矩阵  默认初始值0
	//  这里会多扩建一边和一列  
 	//  因为dp[i][j]的含义是：对于 s1[1..i] 和 s2[1..j]，它们的LCS长度是 dp[i][j]。
	//  所以当i或者j为零时  LCS的长度默认为0
        vector< vector<int> > dp ( m+1 , vector<int> ( n+1 , 0 ) );

        //  状态转移
	//  i、j都从1开始遍历  因为下面的操作中都会-1  相当于从0开始  
        for ( int i=1 ; i<m+1 ; i++ ){
            for ( int j=1 ; j<n+1 ; j++ ){
                //  如果text1和text2相同
                //  就在它们的前一位基础上加一
                //  如果不同  只能在之前的两者中去最大
                dp[i][j] = (text1[i-1] == text2[j-1]) ? dp[i-1][j-1] + 1 : max( dp[i-1][j] , dp[i][j-1] );
            }
        }

        //  返回最终右下角的值
        return dp[m][n];
    }
};
```



**java**

[Shawn](https://github.com/Shawn-Hx) 提供 Java 代码：

```java
public int longestCommonSubsequence(String text1, String text2) {
	// 字符串转为char数组以加快访问速度
	char[] str1 = text1.toCharArray();
	char[] str2 = text2.toCharArray();

	int m = str1.length, n = str2.length;
	// 构建dp table，初始值默认为0
	int[][] dp = new int[m + 1][n + 1];
	// 状态转移
	for (int i = 1; i <= m; i++)
		for (int j = 1; j <= n; j++)
			if (str1[i - 1] == str2[j - 1])
				// 找到LCS中的字符
				dp[i][j] = dp[i-1][j-1] + 1;
			else
				dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
	
	return dp[m][n];
}
```

**python**

[lo-tp](http://blog.lotp.xyz/) 提供 Python 代码：

```python
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
         # calculate the size of the first and second string
        sz1, sz2 = len(text1), len(text2)
        # since to calculate dp(i,j) we only need dp(i-1,j-1), dp(i-1,j), dp(i,j-1)
        # we don't have to save data before i-1
        # we use dp to save dp(i-1, 0), dp(i-1, 1)....dp(i-1, sz2)
        # we use tmp to save dp(i, 0), dp(i,1)....(dpi-1, sz2)
        tmp, dp = [0]*(sz2+1), [0]*(sz2+1)
        for i in range(0, sz1):
            for j in range(0,  sz2):
                tmp[j+1] = dp[j] + \
                    1 if text1[i] == text2[j] else max(tmp[j], dp[j+1])
        # In the next iteration, we will calculate dp(i+1,0),dp(i+1, 1)....dp(i+1,sz2)
        # So we exchange dp and tmp
            tmp, dp = dp, tmp
        return dp[-1]
```







