
##  第零章、必读系列

### 1 动态规划解题框架


**明确 base case -> 明确「状态」-> 明确「选择」 -> 定义 dp 数组/函数的含义**。

按上面的套路走，最后的结果就可以套这个框架：

```python
# 初始化 base case
dp[0][0][...] = base
# 进行状态转移
for 状态1 in 状态1的所有取值：
    for 状态2 in 状态2的所有取值：
        for ...
            dp[状态1][状态2][...] = 求最值(选择1，选择2...)
```            
            
#### 1.1 斐波那契数列

**带备忘录的递归解法**

```cpp
int fib(int N) {
    if (N < 1) return 0;
    // 备忘录全初始化为 0
    vector<int> memo(N + 1, 0);
    // 进行带备忘录的递归
    return helper(memo, N);
}
 
int helper(vector<int>& memo, int n) {
    // base case 
    if (n == 1 || n == 2) return 1;
    // 已经计算过
    if (memo[n] != 0) return memo[n];
    memo[n] = helper(memo, n - 1) + helper(memo, n - 2);
    return memo[n];
}
```
**dp 数组的迭代解法**

```cpp
int fib(int N) {
    if (N == 0) return 0;
    if (N == 1) return 1;
    vector<int> dp(N + 1, 0);
    // base case
    dp[1] = dp[2] = 1;
    for (int i = 3; i <= N; i++)
        dp[i] = dp[i - 1] + dp[i - 2];
    return dp[N];
}
```

「**状态压缩**」

```cpp
int fib(int n) {
    if (n == 2 || n == 1) 
        return 1;
    int prev = 1, curr = 1;
    for (int i = 3; i <= n; i++) {
        int sum = prev + curr;
        prev = curr;
        curr = sum;
    }
    return curr;
}
```

#### 1.2 凑零钱问题


```python
def coinChange(coins: List[int], amount: int):

    def dp(n):
        # base case
        if n == 0: return 0
        if n < 0: return -1
        # 求最小值，所以初始化为正无穷
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            # 子问题无解，跳过
            if subproblem == -1: continue
            res = min(res, 1 + subproblem)

        return res if res != float('INF') else -1
    
    return dp(amount)

** 带备忘录的递归**

```python
def coinChange(coins: List[int], amount: int):
    # 备忘录
    memo = dict()
    def dp(n):
        # 查备忘录，避免重复计算
        if n in memo: return memo[n]
        # base case
        if n == 0: return 0
        if n < 0: return -1
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1: continue
            res = min(res, 1 + subproblem)
        
        # 记入备忘录
        memo[n] = res if res != float('INF') else -1
        return memo[n]
    
    return dp(amount)
```

**dp 数组的迭代解法**


```cpp
int coinChange(vector<int>& coins, int amount) {
    // 数组大小为 amount + 1，初始值也为 amount + 1
    vector<int> dp(amount + 1, amount + 1);
    // base case
    dp[0] = 0;
    // 外层 for 循环在遍历所有状态的所有取值
    for (int i = 0; i < dp.size(); i++) {
        // 内层 for 循环在求所有选择的最小值
        for (int coin : coins) {
            // 子问题无解，跳过
            if (i - coin < 0) continue;
            dp[i] = min(dp[i], 1 + dp[i - coin]);
        }
    }
    return (dp[amount] == amount + 1) ? -1 : dp[amount];
}
```


#### 1.3 其他语言实现

##### python

[DapangLiu](https://github.com/DapangLiu) 提供 509. 斐波那契数 Python3 解法代码：

递归写法

```python
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N-1) + self.fib(N-2)
```

动态规划写法

```python
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        # init
        result = [0 for i in range(N+1)]
        result[1] = 1

        # status transition
        for j in range(2, N+1):
            result[j] = result[j-1] + result[j-2]
        return result[-1]
```

动态规划写法 (状态压缩)

```python
class Solution:
    def fib(self, n: int) -> int:
        # current status only depends on two previous status
        dp_0, dp_1 = 0, 1
        for _ in range(n):
            dp_0, dp_1 = dp_1, dp_0 + dp_1
        return dp_0
```

#### dp 遍历方向

dp 数组的遍历方向

我相信读者做动态规问题时，肯定会对 `dp` 数组的遍历顺序有些头疼。我们拿二维 `dp` 数组来举例，有时候我们是正向遍历：

```java
int[][] dp = new int[m][n];
for (int i = 0; i < m; i++)
    for (int j = 0; j < n; j++)
        // 计算 dp[i][j]
```

有时候我们反向遍历：

```java
for (int i = m - 1; i >= 0; i--)
    for (int j = n - 1; j >= 0; j--)
        // 计算 dp[i][j]
```

有时候可能会斜向遍历：

```java
// 斜着遍历数组
for (int l = 2; l <= n; l++) {
    for (int i = 0; i <= n - l; i++) {
        int j = l + i - 1;
        // 计算 dp[i][j]
    }
}
```

### 2  回溯算法解题框架

```python
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```

#### 2.1 全排列问题

```python
for 选择 in 选择列表:
    # 做选择
    将该选择从选择列表移除
    路径.add(选择)
    backtrack(路径, 选择列表)
    # 撤销选择
    路径.remove(选择)
    将该选择再加入选择列表
```

全排列代码：

```java
List<List<Integer>> res = new LinkedList<>();

/* 主函数，输入一组不重复的数字，返回它们的全排列 */
List<List<Integer>> permute(int[] nums) {
    // 记录「路径」
    LinkedList<Integer> track = new LinkedList<>();
    backtrack(nums, track);
    return res;
}

// 路径：记录在 track 中
// 选择列表：nums 中不存在于 track 的那些元素
// 结束条件：nums 中的元素全都在 track 中出现
void backtrack(int[] nums, LinkedList<Integer> track) {
    // 触发结束条件
    if (track.size() == nums.length) {
        res.add(new LinkedList(track));
        return;
    }
    
    for (int i = 0; i < nums.length; i++) {
        // 排除不合法的选择
        if (track.contains(nums[i]))
            continue;
        // 做选择
        track.add(nums[i]);
        // 进入下一层决策树
        backtrack(nums, track);
        // 取消选择
        track.removeLast();
    }
}
```

#### 2.2  N 皇后问题

给你一个 N×N 的棋盘，让你放置 N 个皇后，使得它们不能互相攻击。

PS：皇后可以攻击同一行、同一列、左上左下右上右下四个方向的任意单位。

```cpp
vector<vector<string>> res;

/* 输入棋盘边长 n，返回所有合法的放置 */
vector<vector<string>> solveNQueens(int n) {
    // '.' 表示空，'Q' 表示皇后，初始化空棋盘。
    vector<string> board(n, string(n, '.'));
    backtrack(board, 0);
    return res;
}

// 路径：board 中小于 row 的那些行都已经成功放置了皇后
// 选择列表：第 row 行的所有列都是放置皇后的选择
// 结束条件：row 超过 board 的最后一行
void backtrack(vector<string>& board, int row) {
    // 触发结束条件
    if (row == board.size()) {
        res.push_back(board);
        return;
    }
    
    int n = board[row].size();
    for (int col = 0; col < n; col++) {
        // 排除不合法选择
        if (!isValid(board, row, col)) 
            continue;
        // 做选择
        board[row][col] = 'Q';
        // 进入下一行决策
        backtrack(board, row + 1);
        // 撤销选择
        board[row][col] = '.';
    }
}
```

```cpp
/* 是否可以在 board[row][col] 放置皇后？ */
bool isValid(vector<string>& board, int row, int col) {
    int n = board.size();
    // 检查列是否有皇后互相冲突
    for (int i = 0; i < n; i++) {
        if (board[i][col] == 'Q')
            return false;
    }
    // 检查右上方是否有皇后互相冲突
    for (int i = row - 1, j = col + 1; 
            i >= 0 && j < n; i--, j++) {
        if (board[i][j] == 'Q')
            return false;
    }
    // 检查左上方是否有皇后互相冲突
    for (int i = row - 1, j = col - 1;
            i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 'Q')
            return false;
    }
    return true;
}
```

```cpp
// 函数找到一个答案后就返回 true
bool backtrack(vector<string>& board, int row) {
    // 触发结束条件
    if (row == board.size()) {
        res.push_back(board);
        return true;
    }
    ...
    for (int col = 0; col < n; col++) {
        ...
        board[row][col] = 'Q';

        if (backtrack(board, row + 1))
            return true;
        
        board[row][col] = '.';
    }

    return false;
}
```

#### 2.3 其他语言

[46.全排列](https://leetcode-cn.com/problems/permutations)

```java
List<List<Integer>> res = new LinkedList<>();

/* 主函数，输入一组不重复的数字，返回它们的全排列 */
List<List<Integer>> permute(int[] nums) {
    // 记录「路径」
    LinkedList<Integer> track = new LinkedList<>();
    backtrack(nums, track);
    return res;
}

// 路径：记录在 track 中
// 选择列表：nums 中不存在于 track 的那些元素
// 结束条件：nums 中的元素全都在 track 中出现
void backtrack(int[] nums, LinkedList<Integer> track) {
    // 触发结束条件
    if (track.size() == nums.length) {
        res.add(new LinkedList(track));
        return;
    }
    
    for (int i = 0; i < nums.length; i++) {
        // 排除不合法的选择
        if (track.contains(nums[i]))
            continue;
        // 做选择
        track.add(nums[i]);
        // 进入下一层决策树
        backtrack(nums, track);
        // 取消选择
        track.removeLast();
    }
}
```



由[kepler-zc](https://github.com/kepler-zc) 提供 51.N皇后 Java 解法代码：
```java
class solution {
    private List<List<String>> res = new ArrayList<>();

    // 输入棋盘边长 n，返回所有合法的放置
    public List<List<String>> solveNQueens(int n){
        // '.'表示空，'Q'表示皇后，初始化空棋盘
        char[][] chess = new char[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(chess[i], '.');
        }
        // 已经不能放置皇后的列（被占用）
        boolean[] usedCol = new boolean[n];
        // 已经不能放置皇后的正斜线 , 按右上角到左下角排列 , 共2n-1条
        boolean[] usedSlash = new boolean[2*n-1];
        // 已经不能放置皇后的反斜线 , 按左上角到右下角排列 , 共2n-1条
        boolean[] usedBackSlash = new boolean[2*n-1];
        backtrack(chess, 0, usedCol, usedSlash, usedBackSlash);
        return res;
    }

    // 路径：chess 中小于 row 的那些行都已经成功放置了皇后
    // 选择列表：第 row 行的所有列都是放置皇后的选择
    // 结束条件：row 超过 棋盘最后一行
    private void backtrack(char[][] chess, int row, boolean[] usedCol, boolean[] usedSlash, boolean[] usedBackSlash) {
        // 触发结束条件
        if (row == chess.length){
            res.add(construct(chess));
            return;
        }
        for (int col = 0; col < chess.length; col++) {
            // 对合法选择进行回溯操作
            // 分别检查列，左上方， 右上方是否存在皇后冲突，都不冲突集为合法选择。
            if (!usedCol[col] && !usedSlash[row-col+usedCol.length-1] && !usedBackSlash[col+row]){
                // 做选择
                chess[row][col] = 'Q';
                usedCol[col] = true;
                // 对坐标为[i,j]的点对应的正斜线和反斜线的索引分别为：row-col+n-1; col+row
                usedSlash[row-col+chess.length-1] = true;
                usedBackSlash[col+row] = true;
                // 进入下一行
                backtrack(chess, row+1, usedCol,usedSlash, usedBackSlash);
                // 撤销选择
                chess[row][col] = '.';
                usedCol[col] = false;
                usedSlash[row-col+chess.length-1] = false;
                usedBackSlash[col+row] = false;
            }
        }
    }

    private List<String> construct(char[][] chess) {
        // 数组转List
        List<String> path = new ArrayList<>();
        for (char[] chars : chess) {
            path.add(new String(chars));
        }
        return path;
    }
}
```

### 3  二分查找详解

#### 3.1 二分查找框架

```java
int binarySearch(int[] nums, int target) {
    int left = 0, right = ...;

    while(...) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            ...
        } else if (nums[mid] < target) {
            left = ...
        } else if (nums[mid] > target) {
            right = ...
        }
    }
    return ...;
}
```

#### 3.2 寻找一个数（基本的二分搜索）

这个场景是最简单的，可能也是大家最熟悉的，即搜索一个数，如果存在，返回其索引，否则返回 -1。

```java
int binarySearch(int[] nums, int target) {
    int left = 0; 
    int right = nums.length - 1; // 注意

    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(nums[mid] == target)
            return mid; 
        else if (nums[mid] < target)
            left = mid + 1; // 注意
        else if (nums[mid] > target)
            right = mid - 1; // 注意
    }
    return -1;
}
```

#### 3.3 寻找左侧边界的二分搜索

以下是最常见的代码形式，其中的标记是需要注意的细节：

```java
int left_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    // 搜索区间为 [left, right]
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            // 搜索区间变为 [mid+1, right]
            left = mid + 1;
        } else if (nums[mid] > target) {
            // 搜索区间变为 [left, mid-1]
            right = mid - 1;
        } else if (nums[mid] == target) {
            // 收缩右侧边界
            right = mid - 1;
        }
    }
    // 检查出界情况
    if (left >= nums.length || nums[left] != target)
        return -1;
    return left;
}
```

#### 3.4 寻找右侧边界的二分查找

类似寻找左侧边界的算法，这里也会提供两种写法，还是先写常见的左闭右开的写法，只有两处和搜索左侧边界不同，已标注：

```java
int right_bound(int[] nums, int target) {
    if (nums.length == 0) return -1;
    int left = 0, right = nums.length;
    
    while (left < right) {
        int mid = (left + right) / 2;
        if (nums[mid] == target) {
            left = mid + 1; // 注意
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid;
        }
    }
    return left - 1; // 注意
}
```

是否也可以把这个算法的「搜索区间」也统一成两端都闭的形式呢？这样这三个写法就完全统一了，以后就可以闭着眼睛写出来了**。

答：当然可以，类似搜索左侧边界的统一写法，其实只要改两个地方就行了：

```java
int right_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else if (nums[mid] == target) {
            // 这里改成收缩左侧边界即可
            left = mid + 1;
        }
    }
    // 这里改为检查 right 越界的情况，见下图
    if (right < 0 || nums[right] != target)
        return -1;
    return right;
}
```


对于寻找左右边界的二分搜索，常见的手法是使用左闭右开的「搜索区间」，**我们还根据逻辑将「搜索区间」全都统一成了两端都闭，便于记忆，只要修改两处即可变化出三种写法**：

```java
int binary_search(int[] nums, int target) {
    int left = 0, right = nums.length - 1; 
    while(left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1; 
        } else if(nums[mid] == target) {
            // 直接返回
            return mid;
        }
    }
    // 直接返回
    return -1;
}

int left_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else if (nums[mid] == target) {
            // 别返回，锁定左侧边界
            right = mid - 1;
        }
    }
    // 最后要检查 left 越界的情况
    if (left >= nums.length || nums[left] != target)
        return -1;
    return left;
}


int right_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else if (nums[mid] == target) {
            // 别返回，锁定右侧边界
            left = mid + 1;
        }
    }
    // 最后要检查 right 越界的情况
    if (right < 0 || nums[right] != target)
        return -1;
    return right;
}
```


#### 3.5 python版本代码

[MarineJoker](https://github.com/MarineJoker) 提供 Python3 代码  

```python
# 基本二分搜索
def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 直接返回
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    # 直接返回
    return -1


# 寻找左侧边界的二分搜索，开区间写法
def left_bound(nums, target):
    left, right = 0, len(nums)
    if right == 0:
        return -1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 锁定左侧边界
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 检查left越界情况
    if left >= len(nums) or nums[left] != target:
        return -1
    return left


# 寻找右侧边界的二分搜索，开区间写法
def right_bound(nums, target):
    left, right = 0, len(nums)
    if right == 0:
        return -1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 锁定右侧边界
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 检查越界情况
    if left == 0 or nums[left - 1] != target:
        return -1
    return left - 1


# 寻找左侧边界的二分搜索，闭区间写法
def left_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 锁定左侧边界
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    # 检查left越界情况
    if left >= len(nums) or nums[left] != target:
        return -1
    return left

# 寻找右侧边界的二分搜索，闭区间写法
def right_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 锁定右侧边界
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    # 检查right越界情况
    if right < 0 or nums[right] != target:
        return -1
    return right
```


### 4  滑动窗口解题框架

#### 4.1 最小覆盖子串

```cpp
string minWindow(string s, string t) {
    // 记录最短子串的开始位置和长度
    int start = 0, minLen = INT_MAX;
    int left = 0, right = 0;
    
    unordered_map<char, int> window;
    unordered_map<char, int> needs;
    for (char c : t) needs[c]++;
    
    int match = 0;
    
    while (right < s.size()) {
        char c1 = s[right];
        if (needs.count(c1)) {
            window[c1]++;
            if (window[c1] == needs[c1]) 
                match++;
        }
        right++;
        
        while (match == needs.size()) {
            if (right - left < minLen) {
                // 更新最小子串的位置和长度
                start = left;
                minLen = right - left;
            }
            char c2 = s[left];
            if (needs.count(c2)) {
                window[c2]--;
                if (window[c2] < needs[c2])
                    match--;
            }
            left++;
        }
    }
    return minLen == INT_MAX ?
                "" : s.substr(start, minLen);
}
```

#### 4.2 找到字符串中所有字母异位词

实际上，这个 Easy 是属于了解双指针技巧的人的，只要把上一道题的代码改中更新 res 部分的代码稍加修改就成了这道题的解：

```cpp
vector<int> findAnagrams(string s, string t) {
    // 用数组记录答案
    vector<int> res;
    int left = 0, right = 0;
    unordered_map<char, int> needs;
    unordered_map<char, int> window;
    for (char c : t) needs[c]++;
    int match = 0;
    
    while (right < s.size()) {
        char c1 = s[right];
        if (needs.count(c1)) {
            window[c1]++;
            if (window[c1] == needs[c1])
                match++;
        }
        right++;

        while (match == needs.size()) {
            // 如果 window 的大小合适
            // 就把起始索引 left 加入结果
            if (right - left == t.size()) {
                res.push_back(left);
            }
            char c2 = s[left];
            if (needs.count(c2)) {
                window[c2]--;
                if (window[c2] < needs[c2])
                    match--;
            }
            left++;
        }
    }
    return res;
}
```
#### 4.3 无重复字符的最长子串

类似之前的思路，使用 window 作为计数器记录窗口中的字符出现次数，然后先向右移动 right，当 window 中出现重复字符时，开始移动 left 缩小窗口，如此往复：

```cpp
int lengthOfLongestSubstring(string s) {
    int left = 0, right = 0;
    unordered_map<char, int> window;
    int res = 0; // 记录最长长度

    while (right < s.size()) {
        char c1 = s[right];
        window[c1]++;
        right++;
        // 如果 window 中出现重复字符
        // 开始移动 left 缩小窗口
        while (window[c1] > 1) {
            char c2 = s[left];
            window[c2]--;
            left++;
        }
        res = max(res, right - left);
    }
    return res;
}
```

通过上面三道题，我们可以总结出滑动窗口算法的抽象思想：

```java
int left = 0, right = 0;

while (right < s.size()) {
    window.add(s[right]);
    right++;
    
    while (valid) {
        window.remove(s[left]);
        left++;
    }
}
```
#### 4.4 其他语言实现

[Jiajun](https://github.com/liujiajun) 提供最小覆盖子串 Python3 代码：
```python3
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 最短子串开始位置和长度
        start, min_len = 0, float('Inf')
        left, right = 0, 0
        res = s
        
        # 两个计数器
        needs = Counter(t)
        window = collections.defaultdict(int) 
        # defaultdict在访问的key不存在的时候返回默认值0, 可以减少一次逻辑判断
        
        match = 0
        
        while right < len(s):
            c1 = s[right]
            if needs[c1] > 0:
                window[c1] += 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1
            
            while match == len(needs):
                if right - left < min_len:
                    # 更新最小子串长度
                    min_len = right - left
                    start = left
                c2 = s[left]
                if needs[c2] > 0:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        
        return s[start:start+min_len] if min_len != float("Inf") else ""
```

第3题 Python3 代码（提供: [FaDrYL](https://github.com/FaDrYL) ）：
```python
def lengthOfLongestSubstring(self, s: str) -> int:
    # 子字符串
    sub = ""
    largest = 0
    
    # 循环字符串，将当前字符加入子字符串，并检查长度
    for i in range(len(s)):
        if s[i] not in sub:
            # 当前字符不存在于子字符串中，加入当前字符
            sub += s[i]
        else:
            # 如果当前子字符串的长度超过了之前的记录
            if len(sub) > largest:
                largest = len(sub)
            # 将子字符串从当前字符处+1切片至最后，并加入当前字符
            sub = sub[sub.find(s[i])+1:] + s[i]
            
    # 如果最后的子字符串长度超过了之前的记录
    if len(sub) > largest:
        return len(sub)
    return largest
```


### 5  双指针技巧

#### 5.1 常见用法

**1、判定链表中是否含有环**

如果链表中不含环，那么这个指针最终会遇到空指针 null 表示链表到头了，这还好说，可以判断该链表不含环。
```java
boolean hasCycle(ListNode head) {
    ListNode fast, slow;
    fast = slow = head;
    while (fast != null && fast.next != null) {
        fast = fast.next.next;
        slow = slow.next;
        
        if (fast == slow) return true;
    }
    return false;
}
```

**2、已知链表中含有环，返回这个环的起始位置**

```java
ListNode detectCycle(ListNode head) {
    ListNode fast, slow;
    fast = slow = head;
    while (fast != null && fast.next != null) {
        fast = fast.next.next;
        slow = slow.next;
        if (fast == slow) break;
    }
    // 上面的代码类似 hasCycle 函数
    if (fast == null || fast.next == null) {
        // fast 遇到空指针说明没有环
        return null;
    }

    slow = head;
    while (slow != fast) {
        fast = fast.next;
        slow = slow.next;
    }
    return slow;
}
```

**3、寻找链表的中点**

```java
while (fast != null && fast.next != null) {
    fast = fast.next.next;
    slow = slow.next;
}
// slow 就在中间位置
return slow;
```


**4、寻找链表的倒数第 k 个元素**

我们的思路还是使用快慢指针，让快指针先走 k 步，然后快慢指针开始同速前进。这样当快指针走到链表末尾 null 时，慢指针所在的位置就是倒数第 k 个链表节点（为了简化，假设 k 不会超过链表长度）：

```java
ListNode slow, fast;
slow = fast = head;
while (k-- > 0) 
    fast = fast.next;

while (fast != null) {
    slow = slow.next;
    fast = fast.next;
}
return slow;
```

#### 5.2 左右指针的常用算法

左右指针在数组中实际是指两个索引值，一般初始化为 left = 0, right = nums.length - 1 。

**1、二分查找**

前文「二分查找」有详细讲解，这里只写最简单的二分算法，旨在突出它的双指针特性：

```java
int binarySearch(int[] nums, int target) {
    int left = 0; 
    int right = nums.length - 1;
    while(left <= right) {
        int mid = (right + left) / 2;
        if(nums[mid] == target)
            return mid; 
        else if (nums[mid] < target)
            left = mid + 1; 
        else if (nums[mid] > target)
            right = mid - 1;
    }
    return -1;
}
```

**2、两数之和**

直接看一道 LeetCode 题目吧：

只要数组有序，就应该想到双指针技巧。这道题的解法有点类似二分查找，通过调节 left 和 right 可以调整 sum 的大小：

```java
int[] twoSum(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left < right) {
        int sum = nums[left] + nums[right];
        if (sum == target) {
            // 题目要求的索引是从 1 开始的
            return new int[]{left + 1, right + 1};
        } else if (sum < target) {
            left++; // 让 sum 大一点
        } else if (sum > target) {
            right--; // 让 sum 小一点
        }
    }
    return new int[]{-1, -1};
}
```

**3、反转数组**

```java
void reverse(int[] nums) {
    int left = 0;
    int right = nums.length - 1;
    while (left < right) {
        // swap(nums[left], nums[right])
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
        left++; right--;
    }
}
```
**4、滑动窗口算法**

这也许是双指针技巧的最高境界了，如果掌握了此算法，可以解决一大类子字符串匹配的问题，不过「滑动窗口」稍微比上述的这些算法复杂些。

#### 5.3 其他语言实现  

**C++**

```cpp
class Solution {
public:
    bool hasCycle(ListNode *head) {
        // 链表为空或有一个元素，则无环
        if(!head || !head->next) return false; 
        
        ListNode* slow = head;
        ListNode* fast = head->next;

        while(fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
            // 快慢指针相遇，则有环
            if(fast == slow) return true;
        }
        return false; // 链表走完，快慢指针未相遇，则无环
    }
};
```


> 其实快慢指针问题，也就是著名的 *[Floyd's cycle detection algorithm](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare)* 问题。

```c++
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        // 如果链表为空或者第一个结点的指针为空，则无环
        if (!head || !head->next) {
            return NULL;
        }

        // 快慢指针找相遇点
        ListNode *fast = head, *slow = head;
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow) {
                break;
            }
        }
        // 如果没有相遇点，表示没有环，直接返回即可
        // 此时，快慢指针要么指向同一个结点，要么快指针指向空（偶数个结点）或者倒数第一个结点（奇数个结点）
        if (fast != slow) {
            return NULL;
        }
        //让慢指针回到第一个结点，然后快慢指针重新同步前进，两指针相遇时就是环的起点位置
        slow = head;
        while (fast != slow) {
            fast = fast->next;
            slow = slow->next;
        }
        return fast;
    }
};
```


**python**

[MarineJoker](https://github.com/MarineJoker) 提供 167.两数之和 II - 输入有序数组 Python 代码
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum > target:
                right -= 1 # 使得two_sum变小
            elif two_sum < target:
                left += 1 # 使得two_sum变大
            elif two_sum == target:
                return [left+1, right+1] # 由于索引由1开始
        return [-1, -1]
```

[ryandeng32](https://github.com/ryandeng32/) 提供 Python 代码
```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 检查链表头是否为None，是的话则不可能为环形
        if head is None: 
            return False 
        # 快慢指针初始化
        slow = fast = head 
        # 若链表非环形则快指针终究会遇到None，然后退出循环
        while fast.next and fast.next.next: 
            # 更新快慢指针
            slow = slow.next
            fast = fast.next.next
            # 快指针追上慢指针则链表为环形
            if slow == fast: 
                return True 
        # 退出循环，则链表有结束，不可能为环形
        return False 
```

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


## 第二章、数据结构系列

### 1 学习算法和刷题的思路指南

数据结构的基本操作

数组遍历框架，典型的线性迭代结构：

```java
void traverse(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        // 迭代访问 arr[i]
    }
}
```

链表遍历框架，兼具迭代和递归结构：

```java
/* 基本的单链表节点 */
class ListNode {
    int val;
    ListNode next;
}

void traverse(ListNode head) {
    for (ListNode p = head; p != null; p = p.next) {
        // 迭代访问 p.val
    }
}

void traverse(ListNode head) {
    // 递归访问 head.val
    traverse(head.next)
}
```

二叉树遍历框架，典型的非线性递归遍历结构：

```java
/* 基本的二叉树节点 */
class TreeNode {
    int val;
    TreeNode left, right;
}

void traverse(TreeNode root) {
    traverse(root.left)
    traverse(root.right)
}
```

你看二叉树的递归遍历方式和链表的递归遍历方式，相似不？再看看二叉树结构和单链表结构，相似不？如果再多几条叉，N 叉树你会不会遍历？

二叉树框架可以扩展为 N 叉树的遍历框架：

```java
/* 基本的 N 叉树节点 */
class TreeNode {
    int val;
    TreeNode[] children;
}

void traverse(TreeNode root) {
    for (TreeNode child : root.children)
        traverse(child);
}
```

N 叉树的遍历又可以扩展为图的遍历，因为图就是好几 N 叉棵树的结合体。你说图是可能出现环的？这个很好办，用个布尔数组 visited 做标记就行了，这里就不写代码了。

### 2 二叉堆详解实现优先级队列

因为，二叉堆其实就是一种特殊的二叉树（完全二叉树），只不过存储在数组里。一般的链表二叉树，我们操作节点的指针，而在数组里，我们把数组索引作为指针：

```java
// 父节点的索引
int parent(int root) {
    return root / 2;
}
// 左孩子的索引
int left(int root) {
    return root * 2;
}
// 右孩子的索引
int right(int root) {
    return root * 2 + 1;
}
```
数据结构的功能无非增删查该，优先级队列有两个主要 API，分别是 `insert` 插入一个元素和 `delMax` 删除最大元素（如果底层用最小堆，那么就是 `delMin`）。

```java
public class MaxPQ
    <Key extends Comparable<Key>> {
    // 存储元素的数组
    private Key[] pq;
    // 当前 Priority Queue 中的元素个数
    private int N = 0;

    public MaxPQ(int cap) {
        // 索引 0 不用，所以多分配一个空间
        pq = (Key[]) new Comparable[cap + 1];
    }

    /* 返回当前队列中最大元素 */
    public Key max() {
        return pq[1];
    }

    /* 插入元素 e */
    public void insert(Key e) {...}

    /* 删除并返回当前队列中最大元素 */
    public Key delMax() {...}

    /* 上浮第 k 个元素，以维护最大堆性质 */
    private void swim(int k) {...}

    /* 下沉第 k 个元素，以维护最大堆性质 */
    private void sink(int k) {...}

    /* 交换数组的两个元素 */
    private void exch(int i, int j) {
        Key temp = pq[i];
        pq[i] = pq[j];
        pq[j] = temp;
    }

    /* pq[i] 是否比 pq[j] 小？ */
    private boolean less(int i, int j) {
        return pq[i].compareTo(pq[j]) < 0;
    }

    /* 还有 left, right, parent 三个方法 */
}
```


**上浮的代码实现：**

```java
private void swim(int k) {
    // 如果浮到堆顶，就不能再上浮了
    while (k > 1 && less(parent(k), k)) {
        // 如果第 k 个元素比上层大
        // 将 k 换上去
        exch(parent(k), k);
        k = parent(k);
    }
}
```

```java
private void sink(int k) {
    // 如果沉到堆底，就沉不下去了
    while (left(k) <= N) {
        // 先假设左边节点较大
        int older = left(k);
        // 如果右边节点存在，比一下大小
        if (right(k) <= N && less(older, right(k)))
            older = right(k);
        // 结点 k 比俩孩子都大，就不必下沉了
        if (less(older, k)) break;
        // 否则，不符合最大堆的结构，下沉 k 结点
        exch(k, older);
        k = older;
    }
}
```


```java
public void insert(Key e) {
    N++;
    // 先把新元素加到最后
    pq[N] = e;
    // 然后让它上浮到正确的位置
    swim(N);
}
```


```java
public Key delMax() {
    // 最大堆的堆顶就是最大元素
    Key max = pq[1];
    // 把这个最大元素换到最后，删除之
    exch(1, N);
    pq[N] = null;
    N--;
    // 让 pq[1] 下沉到正确位置
    sink(1);
    return max;
}
```


###  3 LRU算法

LRU 缓存淘汰算法就是一种常用策略。LRU 的全称是 Least Recently Used，也就是说我们认为最近使用过的数据应该是是「有用的」，很久都没用过的数据应该是无用的，内存满了就优先删那些很久没用过的数据。

[146.LRU缓存机制](https://leetcode-cn.com/problems/lru-cache/)

#### 3.1 实现

```java
class LRUCache {
    int cap;
    LinkedHashMap<Integer, Integer> cache = new LinkedHashMap<>();
    public LRUCache(int capacity) { 
        this.cap = capacity;
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }
        // 将 key 变为最近使用
        makeRecently(key);
        return cache.get(key);
    }
    
    public void put(int key, int val) {
        if (cache.containsKey(key)) {
            // 修改 key 的值
            cache.put(key, val);
            // 将 key 变为最近使用
            makeRecently(key);
            return;
        }
        
        if (cache.size() >= this.cap) {
            // 链表头部就是最久未使用的 key
            int oldestKey = cache.keySet().iterator().next();
            cache.remove(oldestKey);
        }
        // 将新的 key 添加链表尾部
        cache.put(key, val);
    }
    
    private void makeRecently(int key) {
        int val = cache.get(key);
        // 删除 key，重新插入到队尾
        cache.remove(key);
        cache.put(key, val);
    }
}
```

#### 3.2 其他语言实现

**c++**

[gowufang](https://github.com/gowufang)提供第146题C++代码：
```cpp
class LRUCache {
        public:
        struct node {
            int val;
            int key;
            node* pre;//当前节点的前一个节点
            node* next;//当前节点的后一个节点
            node(){}
            node(int key, int val):key(key), val(val), pre(NULL), next(NULL){}
        };

        LRUCache(int size) {
            this->size = size;
            head = new node();
            tail = new node();
            head->next = tail;
            tail->pre = head;
        }


        void movetohead(node* cur)//相当于一个insert操作，在head 和 head的next之间插入一个节点
        {
            node* next = head->next;//head的next先保存起来
            head->next = cur;//将当前节点移动到head的后面
            cur->pre = head;//当前节点cur的pre指向head
            next->pre = cur;
            cur->next = next;
        }

        node* deletecurrentnode(node* cur)//移除当前节点
        {
            cur->pre->next = cur->next;
            cur->next->pre = cur->pre;
            return cur;
        }
        void makerecently(node* cur)
        {
            node* temp = deletecurrentnode(cur);// 删除 cur，要重新插入到对头
            movetohead(temp);//cur放到队头去
        }
        int get(int key)
        {
            int ret = -1;
            if ( map.count(key))
            {
                node* temp = map[key];
                makerecently(temp);// 将 key 变为最近使用
                ret = temp->val;
            }
            return ret;
        }

        void put(int key, int value) {
            if ( map.count(key))
            {
                // 修改 key 的值
                node* temp = map[key];
                temp->val = value;
                // 将 key 变为最近使用
                makerecently(temp);
            }
            else
            {
                node* cur = new node(key, value);
                if( map.size()== size )
                {
                    // 链表头部就是最久未使用的 key
                    node *temp = deletecurrentnode(tail->pre);
                    map.erase(temp->key);
                }
                movetohead(cur);
                map[key] = cur;

            }
        
        }

        unordered_map<int, node*> map;
        int size;
        node* head, *tail;

    };
```



**python**

```python
"""
所谓LRU缓存，根本的难点在于记录最久被使用的键值对，这就设计到排序的问题，
在python中，天生具备排序功能的字典就是OrderDict。
注意到，记录最久未被使用的键值对的充要条件是将每一次put/get的键值对都定义为
最近访问，那么最久未被使用的键值对自然就会排到最后。
如果你深入python OrderDict的底层实现，就会知道它的本质是个双向链表+字典。
它内置支持了
1. move_to_end来重排链表顺序，它可以让我们将最近访问的键值对放到最后面
2. popitem来弹出键值对，它既可以弹出最近的，也可以弹出最远的，弹出最远的就是我们要的操作。
"""
from collections import OrderedDict
class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity  # cache的容量
    self.visited = OrderedDict()  # python内置的OrderDict具备排序的功能
    
  def get(self, key: int) -> int:
    if key not in self.visited:
      return -1
    self.visited.move_to_end(key)  # 最近访问的放到链表最后，维护好顺序
    return self.visited[key]

  def put(self, key: int, value: int) -> None:
    if key not in self.visited and len(self.visited) == self.capacity:
      # last=False时，按照FIFO顺序弹出键值对
      # 因为我们将最近访问的放到最后，所以最远访问的就是最前的，也就是最first的，故要用FIFO顺序
      self.visited.popitem(last=False)
      self.visited[key]=value
      self.visited.move_to_end(key)    # 最近访问的放到链表最后，维护好顺序


```

### 4 二叉搜索树操作集锦

#### 4.1 设计思路

100.相同的树

450.删除二叉搜索树中的节点

701.二叉搜索树中的插入操作

700.二叉搜索树中的搜索

98.验证二叉搜索树

二叉树算法的设计的总路线：明确一个节点要做的事情，然后剩下的事抛给框架。

void traverse(TreeNode root) {
    // root 需要做什么？在这做。
    // 其他的不用 root 操心，抛给框架
    traverse(root.left);
    traverse(root.right);
}

举两个简单的例子体会一下这个思路，热热身。

**1. 如何把二叉树所有的节点中的值加一？**

```java
void plusOne(TreeNode root) {
    if (root == null) return;
    root.val += 1;

    plusOne(root.left);
    plusOne(root.right);
}
```

**2. 如何判断两棵二叉树是否完全相同？**

```java
boolean isSameTree(TreeNode root1, TreeNode root2) {
    // 都为空的话，显然相同
    if (root1 == null && root2 == null) return true;
    // 一个为空，一个非空，显然不同
    if (root1 == null || root2 == null) return false;
    // 两个都非空，但 val 不一样也不行
    if (root1.val != root2.val) return false;

    // root1 和 root2 该比的都比完了
    return isSameTree(root1.left, root2.left)
        && isSameTree(root1.right, root2.right);
}
```

**在 BST 中查找一个数是否存在**

```java
boolean isInBST(TreeNode root, int target) {
    if (root == null) return false;
    if (root.val == target) return true;

    return isInBST(root.left, target)
        || isInBST(root.right, target);
}
```


**零、判断 BST 的合法性**

```java
boolean isValidBST(TreeNode root) {
    return isValidBST(root, null, null);
}

boolean isValidBST(TreeNode root, TreeNode min, TreeNode max) {
    if (root == null) return true;
    if (min != null && root.val <= min.val) return false;
    if (max != null && root.val >= max.val) return false;
    return isValidBST(root.left, min, root) 
        && isValidBST(root.right, root, max);
}
```

**针对 BST 的遍历框架**：

```java
void BST(TreeNode root, int target) {
    if (root.val == target)
        // 找到目标，做点什么
    if (root.val < target) 
        BST(root.right, target);
    if (root.val > target)
        BST(root.left, target);
}
```

**在 BST 中插入一个数**

```java
TreeNode insertIntoBST(TreeNode root, int val) {
    // 找到空位置插入新节点
    if (root == null) return new TreeNode(val);
    // if (root.val == val)
    //     BST 中一般不会插入已存在元素
    if (root.val < val) 
        root.right = insertIntoBST(root.right, val);
    if (root.val > val) 
        root.left = insertIntoBST(root.left, val);
    return root;
}
```

**在 BST 中删除一个数**

```java
TreeNode deleteNode(TreeNode root, int key) {
    if (root == null) return null;
    if (root.val == key) {
        // 这两个 if 把情况 1 和 2 都正确处理了
        if (root.left == null) return root.right;
        if (root.right == null) return root.left;
        // 处理情况 3
        TreeNode minNode = getMin(root.right);
        root.val = minNode.val;
        root.right = deleteNode(root.right, minNode.val);
    } else if (root.val > key) {
        root.left = deleteNode(root.left, key);
    } else if (root.val < key) {
        root.right = deleteNode(root.right, key);
    }
    return root;
}

TreeNode getMin(TreeNode node) {
    // BST 最左边的就是最小的
    while (node.left != null) node = node.left;
    return node;
} 
```

#### 4.2 其他语言实现


[100.相同的树](https://leetcode-cn.com/problems/same-tree)

[450.删除二叉搜索树中的节点](https://leetcode-cn.com/problems/delete-node-in-a-bst)

[701.二叉搜索树中的插入操作](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree)

[700.二叉搜索树中的搜索](https://leetcode-cn.com/problems/search-in-a-binary-search-tree)

[98.验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree)


**c++实现**

[dekunma](https://www.linkedin.com/in/dekun-ma-036a9b198/)提供第98题C++代码：

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        // 用helper method求解
        return isValidBST(root, nullptr, nullptr);
    }

    bool isValidBST(TreeNode* root, TreeNode* min, TreeNode* max) {
        // base case, root为nullptr
        if (!root) return true;

        // 不符合BST的条件
        if (min && root->val <= min->val) return false;
        if (max && root->val >= max->val) return false;

        // 向左右子树分别递归求解
        return isValidBST(root->left, min, root) 
            && isValidBST(root->right, root, max);
    }
};
```


[yanggg1997](https://github.com/yanggg1997)提供第100题C++代码：

``` c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
		// 若当前节点均为空，则此处相同
        if(!p && !q) return true;	
        // 若当前节点在一棵树上有而另一棵树上为空，则两棵树不同
        if(!p && q) return false;	
        if(p && !q) return false;
        // 若当前节点在两棵树上均存在。
        if(p->val != q->val)
        {
            return false;
        }
        else
        {
            // 向左右子树分别递归判断
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        }
    }
};
```

**python实现**

[ChenjieXu](https://github.com/ChenjieXu)提供第98题Python3代码：

```python
def isValidBST(self, root):
        # 递归函数
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False
            # 右节点
            if not helper(node.right, val, upper):
                return False
            # 左节点
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
        
```

[lixiandea](https://github.com/lixiandea)提供第100题Python3代码：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    '''
    当前节点值相等且树的子树相等，则树相等。
    递归退出条件：两个节点存在一个节点为空
    '''
        if p == None:
            if q == None:
                return True
            else:
                return False
        if q == None:
            return False
        # 当前节点相同且左子树和右子树分别相同
        return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```


[Edwenc](https://github.com/Edwenc) 提供 leetcode第450题的python3 代码：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        #  如果没有树  直接返回None
        if root == None:
            return None

        #  如果要删除的结点  就是当前结点
        if root.val == key:
            #  左子树为空  只有右子树需要被更新  直接返回
            if root.left == None:
                return root.right
            #  右子树为空  只有左子树需要被更新  直接返回
            if root.right== None:
                return root.left

            #  找出此结点左子树的最大值
            #  用这个最大值  来代替当前结点
            #  再在左子树中递归地删除这个最大值结点
            big = self.getMax( root.left )
            root.val = big.val
            root.left = self.deleteNode( root.left , big.val )
        
        #  当前结点较大  它的左子树中需要删除节点  递归到左子树
        elif root.val > key:
            root.left = self.deleteNode( root.left , key)
        #  当前结点较小  它的右子树中需要删除节点  递归到右子树
        else:
            root.right= self.deleteNode( root.right, key)

        return root

    #  辅助函数
    #  功能是找出此二叉搜索树中最大元素的结点  并返回此结点
    def getMax( self , node ):
        #  一直找它的右子树  直到为空
        while node.right:
            node = node.right
        return node
```

**java实现**


```
/**
* 第【98】题的扩展解法：
* 对于BST，有一个重要的性质，即“BST的中序遍历是单调递增的”。抓住这个性质，我们可以通过中序遍历来判断该二叉树是不是BST。
* 我们定义preNode节点表示上一个遍历的节点，在中序遍历的时候，比较当前节点和preNode节点的大小，一旦有节点小于或等于前一个节点，则不满足BST的规则，直接返回false，否则遍历结束，返回true。
*/
TreeNode preNode = null;
public boolean isValidBST(TreeNode root) {
    if (root == null) return true;

    boolean leftRes = isValidBST(root.left);

    if (preNode != null && root.val <= preNode.val) {
        return false;
    }
    preNode = root;

    boolean rightRes = isValidBST(root.right);

    return leftRes && rightRes;
}
```

###  5 特殊数据结构：单调栈

单调栈实际上就是栈，只是利用了一些巧妙的逻辑，使得每次新元素入栈后，栈内的元素都保持有序（单调递增或单调递减）。

Next Greater Number 的原始问题，这是力扣第 496 题「下一个更大元素 I」：

给你一个数组，返回一个等长的数组，对应索引存储着下一个更大元素，如果没有更大的元素，就存 -1。

函数签名如下：

	vector<int> nextGreaterElement(vector<int>& nums);
	比如说，输入一个数组 nums = [2,1,2,4,3]，你返回数组 [4,2,4,-1,-1]。


#### 5.1 单调栈模板

```cpp
vector<int> nextGreaterElement(vector<int>& nums) {
    vector<int> res(nums.size()); // 存放答案的数组
    stack<int> s;
    // 倒着往栈里放
    for (int i = nums.size() - 1; i >= 0; i--) {
        // 判定个子高矮
        while (!s.empty() && s.top() <= nums[i]) {
            // 矮个起开，反正也被挡着了。。。
            s.pop();
        }
        // nums[i] 身后的 next great number
        res[i] = s.empty() ? -1 : s.top();
        // 
        s.push(nums[i]);
    }
    return res;
}
```

这就是单调队列解决问题的模板。for 循环要从后往前扫描元素，因为我们借助的是栈的结构，倒着入栈，其实是正着出栈。while 循环是把两个「个子高」元素之间的元素排除，因为他们的存在没有意义，前面挡着个「更高」的元素，所以他们不可能被作为后续进来的元素的 Next Great Number 了。


环形数组： 通过 % 运算符求模（余数），来获得环形特效：


```java
int[] arr = {1,2,3,4,5};
int n = arr.length, index = 0;
while (true) {
    print(arr[index % n]);
    index++;
}
```


#### 5.2 实现

```java
// 496.下一个更大元素
// 单调栈解法
public int[] nextGreaterElement(int[] nums1, int[] nums2) {
    Stack<Integer> stack = new Stack <>();
    HashMap<Integer, Integer> map = new HashMap <>();
    int[] result = new int[nums1.length];
    for (int value : nums2) {
        while (!stack.empty() && value > stack.peek()) {
            map.put(stack.pop(), value);
        }
        stack.push(value);
    }
    while (!stack.empty()) {
        map.put(stack.pop(), -1);
    }
    for (int i = 0; i < nums1.length; i++) {
        result[i] = map.get(nums1[i]);
    }
    return result;
}
```

[ZakAnun](https://github.com/ZakAnun) 提供代码

```java
// 739. Daily Temperatures
class Solution {
    public int[] dailyTemperatures(int[] T) {
        Stack<Integer> stack = new Stack<>();
        int[] ans = new int[T.length];
        for (int i = 0; i < T.length; i++) {
            // 如果压栈之后不满足单调递减，弹出元素，直至保持单调性
            while (!stack.isEmpty() && T[i] > T[stack.peek()]) {
                int index = stack.pop();
                // 被弹出的元素（T[index]）都是小于当前的元素(T[i])，由于栈内元素单调递减，大于被弹出元素（index）的最近的就是当前元素(i)
                ans[index] = i - index;
            }
            stack.push(i);
        }
        return ans;
    }
}
```

[JiangangZhao](https://github.com/JiangangZhao)提供【503.下一个更大元素II】【java】

```java
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        //数组长度
        int n = nums.length;
        //逻辑拼接，数组长度翻倍
        int len = n*2 - 1;
        //存储结果数组
        int[] res = new int[n];
        //存放索引，不是元素
        LinkedList<Integer> s = new LinkedList<>();
        //从前往后遍历
        for (int i = 0; i < len; ++i) {
            //索引要取模
            int val = nums[i % n];
            //当前元素比栈顶元素大，即是栈顶元素的下一个更大的元素
            while (!s.isEmpty() && val > nums[s.peek()]) {
                res[s.pop()] = val;
            }
            //i<n时入栈
            if (i < n) {
                s.push(i);
            }
        }
        //栈中剩余的索引不存在下一个更大的元素，赋值-1
        while (!s.isEmpty()) {
            res[s.pop()] = -1;
        }
        return res;
    }
}
```

### 6 特殊数据结构：单调队列

239.滑动窗口最大值

给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

示例 1：

	输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
	输出：[3,3,5,5,6,7]
	解释：
	滑动窗口的位置                最大值
	---------------               -----
	[1  3  -1] -3  5  3  6  7       3
	 1 [3  -1  -3] 5  3  6  7       3
	 1  3 [-1  -3  5] 3  6  7       5
	 1  3  -1 [-3  5  3] 6  7       5
	 1  3  -1  -3 [5  3  6] 7       6
	 1  3  -1  -3  5 [3  6  7]      7


#### 6.1 单调队列模板

```cpp
class MonotonicQueue {
private:
    deque<int> data;
public:
    void push(int n) {
        while (!data.empty() && data.back() < n) 
            data.pop_back();
        data.push_back(n);
    }
    
    int max() { return data.front(); }
    
    void pop(int n) {
        if (!data.empty() && data.front() == n)
            data.pop_front();
    }
};

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    MonotonicQueue window;
    vector<int> res;
    for (int i = 0; i < nums.size(); i++) {
        if (i < k - 1) { //先填满窗口的前 k - 1
            window.push(nums[i]);
        } else { // 窗口向前滑动
            window.push(nums[i]);
            res.push_back(window.max());
            window.pop(nums[i - k + 1]);
        }
    }
    return res;
}
```


#### 6.2 其他语言实现

**python**

由[SCUHZS](ttps://github.com/brucecat)提供


```python
from collections import deque

class MonotonicQueue(object):
    def __init__(self):
        # 双端队列
        self.data = deque()

    def push(self, n):
        # 实现单调队列的push方法
        while self.data and self.data[-1] < n:
            self.data.pop()
        self.data.append(n)

    def max(self):
        # 取得单调队列中的最大值
        return self.data[0]

    def pop(self, n):
        # 实现单调队列的pop方法
        if self.data and self.data[0] == n:
            self.data.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调队列实现的窗口
        window = MonotonicQueue()

        # 结果
        res = []
        
        for i in range(0, len(nums)):
            
            if i < k-1:
                # 先填满窗口前k-1
                window.push(nums[i])
            else:
                # 窗口向前滑动
                window.push(nums[i])
                res.append(window.max())
                window.pop(nums[i-k+1])
        return res

```

**java**


```java
class Twitter {
    private static int timestamp = 0;
    private static class Tweet {}
    private static class User {}

    /* 还有那几个 API 方法 */
    public void postTweet(int userId, int tweetId) {}
    public List<Integer> getNewsFeed(int userId) {}
    public void follow(int followerId, int followeeId) {}
    public void unfollow(int followerId, int followeeId) {}
}
```


```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int len = nums.length;
        // 判断数组或者窗口长度为0的情况
        if (len * k == 0) {
            return new int[0];
        }

        /*
        采用两端扫描的方法
        将数组分成大小为 k 的若干个窗口, 对每个窗口分别从左往右和从右往左扫描, 记录扫描的最大值
        left[] 记录从左往右扫描的最大值
        right[] 记录从右往左扫描的最大值
         */
        int[] left = new int[len];
        int[] right = new int[len];

        for (int i = 0; i < len; i = i + k) {
            // 每个窗口中的第一个值
            left[i] = nums[i];
            // 窗口的最后边界
            int index = i + k - 1 >= len ? len - 1 : i + k - 1;
            // 每个窗口的最后一个值
            right[index] = nums[index];
            // 对该窗口从左往右扫描
            for (int j = i + 1; j <= index; j++) {
                left[j] = Math.max(left[j - 1], nums[j]);
            }
            // 对该窗口从右往左扫描
            for (int j = index - 1; j >= i; j--) {
                right[j] = Math.max(right[j + 1], nums[j]);
            }
        }

        int[] arr = new int[len - k + 1];

        // 对于第 i 个位置, 它一定是该窗口从右往左扫描数组中的最后一个值, 相对的 i + k - 1 是该窗口从左向右扫描数组中的最后一个位置
        // 对两者取最大值即可
        for (int i = 0; i < len - k + 1; i++) {
            arr[i] = Math.max(right[i], left[i + k - 1]);
        }

        return arr;
    }
}
```

### 7 设计Twitter

355.设计推特

#### 题目

Twitter 和微博功能差不多，我们主要要实现这样几个 API：

```java
class Twitter {

    /** user 发表一条 tweet 动态 */
    public void postTweet(int userId, int tweetId) {}
    
    /** 返回该 user 关注的人（包括他自己）最近的动态 id，
    最多 10 条，而且这些动态必须按从新到旧的时间线顺序排列。*/
    public List<Integer> getNewsFeed(int userId) {}
    
    /** follower 关注 followee，如果 Id 不存在则新建 */
    public void follow(int followerId, int followeeId) {}
    
    /** follower 取关 followee，如果 Id 不存在则什么都不做 */
    public void unfollow(int followerId, int followeeId) {}
}
```

举个具体的例子，方便大家理解 API 的具体用法：

```java
Twitter twitter = new Twitter();

twitter.postTweet(1, 5);
// 用户 1 发送了一条新推文 5

twitter.getNewsFeed(1);
// return [5]，因为自己是关注自己的

twitter.follow(1, 2);
// 用户 1 关注了用户 2

twitter.postTweet(2, 6);
// 用户2发送了一个新推文 (id = 6)

twitter.getNewsFeed(1);
// return [6, 5]
// 解释：用户 1 关注了自己和用户 2，所以返回他们的最近推文
// 而且 6 必须在 5 之前，因为 6 是最近发送的

twitter.unfollow(1, 2);
// 用户 1 取消关注了用户 2

twitter.getNewsFeed(1);
// return [5]
```

这个场景在我们的现实生活中非常常见。拿朋友圈举例，比如我刚加到女神的微信，然后我去刷新一下我的朋友圈动态，那么女神的动态就会出现在我的动态列表，而且会和其他动态按时间排好序。只不过 Twitter 是单向关注，微信好友相当于双向关注。除非，被屏蔽...

这几个 API 中大部分都很好实现，最核心的功能难点应该是 `getNewsFeed`，因为返回的结果必须在时间上有序，但问题是用户的关注是动态变化的，怎么办？

**这里就涉及到算法了**：如果我们把每个用户各自的推文存储在链表里，每个链表节点存储文章 id 和一个时间戳 time（记录发帖时间以便比较），而且这个链表是按 time 有序的，那么如果某个用户关注了 k 个用户，我们就可以用合并 k 个有序链表的算法合并出有序的推文列表，正确地 `getNewsFeed` 了！

具体的算法等会讲解。不过，就算我们掌握了算法，应该如何编程表示用户 user 和推文动态 tweet 才能把算法流畅地用出来呢？**这就涉及简单的面向对象设计了**，下面我们来由浅入深，一步一步进行设计。

```java
class Tweet {
    private int id;
    private int time;
    private Tweet next;

    // 需要传入推文内容（id）和发文时间
    public Tweet(int id, int time) {
        this.id = id;
        this.time = time;
        this.next = null;
    }
}
```


```java
// static int timestamp = 0
class User {
    private int id;
    public Set<Integer> followed;
    // 用户发表的推文链表头结点
    public Tweet head;

    public User(int userId) {
        followed = new HashSet<>();
        this.id = userId;
        this.head = null;
        // 关注一下自己
        follow(id);
    }

    public void follow(int userId) {
        followed.add(userId);
    }

    public void unfollow(int userId) {
        // 不可以取关自己
        if (userId != this.id)
            followed.remove(userId);
    }

    public void post(int tweetId) {
        Tweet twt = new Tweet(tweetId, timestamp);
        timestamp++;
        // 将新建的推文插入链表头
        // 越靠前的推文 time 值越大
        twt.next = head;
        head = twt;
    }
}
```

```java
class Twitter {
    private static int timestamp = 0;
    private static class Tweet {...}
    private static class User {...}

    // 我们需要一个映射将 userId 和 User 对象对应起来
    private HashMap<Integer, User> userMap = new HashMap<>();

    /** user 发表一条 tweet 动态 */
    public void postTweet(int userId, int tweetId) {
        // 若 userId 不存在，则新建
        if (!userMap.containsKey(userId))
            userMap.put(userId, new User(userId));
        User u = userMap.get(userId);
        u.post(tweetId);
    }
    
    /** follower 关注 followee */
    public void follow(int followerId, int followeeId) {
        // 若 follower 不存在，则新建
		if(!userMap.containsKey(followerId)){
			User u = new User(followerId);
			userMap.put(followerId, u);
		}
        // 若 followee 不存在，则新建
		if(!userMap.containsKey(followeeId)){
			User u = new User(followeeId);
			userMap.put(followeeId, u);
		}
		userMap.get(followerId).follow(followeeId);
    }
    
    /** follower 取关 followee，如果 Id 不存在则什么都不做 */
    public void unfollow(int followerId, int followeeId) {
        if (userMap.containsKey(followerId)) {
            User flwer = userMap.get(followerId);
            flwer.unfollow(followeeId);
        }
    }

    /** 返回该 user 关注的人（包括他自己）最近的动态 id，
    最多 10 条，而且这些动态必须按从新到旧的时间线顺序排列。*/
    public List<Integer> getNewsFeed(int userId) {
        // 需要理解算法，见下文
    }
}
```


```java
public List<Integer> getNewsFeed(int userId) {
    List<Integer> res = new ArrayList<>();
    if (!userMap.containsKey(userId)) return res;
    // 关注列表的用户 Id
    Set<Integer> users = userMap.get(userId).followed;
    // 自动通过 time 属性从大到小排序，容量为 users 的大小
    PriorityQueue<Tweet> pq = 
        new PriorityQueue<>(users.size(), (a, b)->(b.time - a.time));

    // 先将所有链表头节点插入优先级队列
    for (int id : users) {
        Tweet twt = userMap.get(id).head;
        if (twt == null) continue;
        pq.add(twt);
    }

    while (!pq.isEmpty()) {
        // 最多返回 10 条就够了
        if (res.size() == 10) break;
        // 弹出 time 值最大的（最近发表的）
        Tweet twt = pq.poll();
        res.add(twt.id);
        // 将下一篇 Tweet 插入进行排序
        if (twt.next != null) 
            pq.add(twt.next);
    }
    return res;
}
```


#### 7.2 其他语言实现

**C++**

[happy-yuxuan](https://github.com/happy-yuxuan) 提供 C++ 代码：

```c++
static int timestamp = 0;
class Tweet {
private:
    int id;
    int time;
public:
    Tweet *next;
    // id为推文内容，time为发文时间
    Tweet(int id, int time) {
        this->id = id;
        this->time = time;
        next = nullptr;
    }
    int getId() const {
        return this->id;
    }
    int getTime() const {
        return this->time;
    }
};
class User {
private:
    int id;
public:
    Tweet *head;  // 发布的Twitter，用链表表示
    unordered_set<int> followed;  // 用户关注了那些人
    User(int userId) {
        this->id = userId;
        head = nullptr;
        // 要先把自己关注了
        followed.insert(id);
    }
    void follow(int userId) {
        followed.insert(userId);
    }
    void unfollow(int userId) {
        // 不可以取关自己
        if (userId != this->id)
            followed.erase(userId);
    }
    void post(int contentId) {
        Tweet *twt = new Tweet(contentId, timestamp);
        timestamp++;
        // 将新建的推文插入链表头
        // 越靠前的推文 timestamp 值越大
        twt->next = head;
        head = twt;
    }
};
class Twitter {
private:
    // 映射将 userId 和 User 对象对应起来
    unordered_map<int, User*> userMap;
    // 判断该用户存不存在系统中,即userMap中存不存在id
    inline bool contain(int id) {
        return userMap.find(id) != userMap.end();
    }
public:
    Twitter() {
        userMap.clear();
    }
    /* user 发表一条 tweet 动态 */
    void postTweet(int userId, int tweetId) {
        if (!contain(userId))
            userMap[userId] = new User(userId);
        userMap[userId]->post(tweetId);
    }
    /* 返回该 user 关注的人（包括他自己）最近的动态 id，
    最多 10 条，而且这些动态必须按从新到旧的时间线顺序排列。*/
    vector<int> getNewsFeed(int userId) {
        vector<int> ret;
        if (!contain(userId)) return ret;
        // 构造一个自动通过Tweet发布的time属性从大到小排序的二叉堆
        typedef function<bool(const Tweet*, const Tweet*)> Compare;
        Compare cmp = [](const Tweet *a, const Tweet *b) {
            return a->getTime() < b->getTime();
        };
        priority_queue<Tweet*, vector<Tweet*>, Compare> q(cmp);
        // 关注列表的用户Id
        unordered_set<int> &users = userMap[userId]->followed;
        // 先将所有链表头节点插入优先级队列
        for (int id : users) {
            if (!contain(id)) continue;
            Tweet *twt = userMap[id]->head;
            if (twt == nullptr) continue;
            q.push(twt);
        }
        while (!q.empty()) {
            Tweet *t = q.top(); q.pop();
            ret.push_back(t->getId());
            if (ret.size() == 10) return ret;  // 最多返回 10 条就够了
            if (t->next)
                q.push(t->next);
        }
        return ret;
    }
    /* follower 关注 followee */
    void follow(int followerId, int followeeId) {
        // 若 follower 不存在，则新建
        if (!contain(followerId))
            userMap[followerId] = new User(followerId);
        // 若 followee 不存在，则新建
        if (!contain(followeeId))
            userMap[followeeId] = new User(followeeId);
        userMap[followerId]->follow(followeeId);
    }
    /* follower 取关 followee，如果 Id 不存在则什么都不做 */
    void unfollow(int followerId, int followeeId) {
        if (contain(followerId))
            userMap[followerId]->unfollow(followeeId);
    }
};
```



**python**

```python
import heapq

class Tweet:
    def __init__(self, tid: int, time: int) -> None:
        self.tid = tid
        self.time = time
        self.next = None

class User:
    def __init__(self, uid: int):
        self.uid = uid
        self.following = set()
        self.tweetlst = None
        self.follow(uid)

    def post(self, tid: int, time: int) -> None:
        tweet = Tweet(tid, time)
        tweet.next = self.tweetlst
        self.tweetlst = tweet

    def follow(self, uid: int) -> None:
        if uid not in self.following:
            self.following.add(uid)

    def unfollow(self, uid: int) -> None:
        # one cannot unfollow itself
        if uid != self.uid and uid in self.following:
            self.following.remove(uid)

class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.id2user = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.id2user: self.id2user[userId] = User(userId)
        user = self.id2user[userId]
        user.post(tweetId, self.timestamp)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        heap, user = [], self.id2user.get(userId)

        if user:
            for uid in user.following:
                tweets = self.id2user[uid].tweetlst
                while tweets:
                    heap.append(tweets)
                    tweets = tweets.next
            return [twt.tid for twt in heapq.nlargest(10, heap, key= lambda twt: twt.time)]
        else: return []

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.id2user:
            self.id2user[followerId] = User(followerId)
        if followeeId not in self.id2user:
            self.id2user[followeeId] = User(followeeId)
        self.id2user[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.id2user:
            self.id2user[followerId].unfollow(followeeId)
```


### 8 递归反转链表的一部分

#### 8.1 递归反转整个链表

```java
ListNode reverse(ListNode head) {
    if (head.next == null) return head;
    ListNode last = reverse(head.next);
    head.next.next = head;
    head.next = null;
    return last;
}
```

#### 8.2 反转链表前 N 个节点

```java
ListNode successor = null; // 后驱节点

// 反转以 head 为起点的 n 个节点，返回新的头结点
ListNode reverseN(ListNode head, int n) {
    if (n == 1) { 
        // 记录第 n + 1 个节点
        successor = head.next;
        return head;
    }
    // 以 head.next 为起点，需要反转前 n - 1 个节点
    ListNode last = reverseN(head.next, n - 1);

    head.next.next = head;
    // 让反转之后的 head 节点和后面的节点连起来
    head.next = successor;
    return last;
}    
```

#### 8.3 反转链表的一部分

```java
ListNode reverseBetween(ListNode head, int m, int n) {
    // base case
    if (m == 1) {
        return reverseN(head, n);
    }
    // 前进到反转的起点触发 base case
    head.next = reverseBetween(head.next, m - 1, n - 1);
    return head;
}
```

#### 8.4 其他语言实现


**c++** 

[shilei](https://github.com/ShileiGuo) 提供C++解法代码:

思想:

   1.head表示需要反转的头节点，pre表示需要反转头节点的前驱节点

   2.对于从m到n的节点反转，需要反转n-m次，将head的next节点移动到需要反转链表部分的首部，需要反转链表部分剩余节点依旧保持相对顺序即可

   3.示例 当m=2, n=5时 

   第一次反转：1(pre) 2(head) 3(next) 4 5 反转为 1 3 2 4 5

   第二次反转：1(pre) 3 2(head) 4(next) 5 反转为 1 4 3 2 5

   第三次发转：1(pre) 4 3 2(head) 5(next) 反转为 1 5 4 3 2

```CPP
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        //初始化哨兵节点
        ListNode* dummy=new ListNode(-1);
        //初始化待反转区间的前一个节点
        ListNode* pre=dummy;
        //哨兵节点下一个节点指向head头节点
        dummy->next=head;
        
        //获取待反转节点的前一个节点
        for(int i=0;i<m-1;i++)
            pre=pre->next;        
        //获取待反转节点的第一个节点
        head=pre->next;  
        //迭代反转n-m次，将head的next节点移动到需要反转链表部分的首部
        for(int i=m;i<n;i++){
            ListNode* t=head->next;       
            head->next=t->next;          
            t->next=pre->next;         
            pre->next=t;                
        }
        //返回哨兵节点
        return dummy->next;
    }
};
```

**python**

[DiamondI](https://github.com/DiamondI) 提供python3版本代码：

思路：递归。时间复杂度为O(n)，由于递归调用需要借助栈的空间，因此空间复杂度亦为O(n)。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def __init__(self):
    self.__successor = None

    def __reverseN(self, head: ListNode, n: int) -> ListNode:
      if n == 1:  
        # 记录第 n + 1 个节点
        self.__successor = head.next;
        return head;
      # 以 head.next 为起点，需要反转前 n - 1 个节点
      last = self.__reverseN(head.next, n - 1);

      head.next.next = head;
      # 让反转之后的 head 节点和后面的节点连起来
      head.next = self.__successor;
      return last;

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
      # base case
      if m == 1:
        return self.__reverseN(head, n);
      # 前进到反转的起点触发 base case
      head.next = self.reverseBetween(head.next, m - 1, n - 1);
      return head;
```


### 9 队列实现栈|栈实现队列 

[232.用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks)


请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：

    void push(int x) 将元素 x 推到队列的末尾
    int pop() 从队列的开头移除并返回元素
    int peek() 返回队列开头的元素
    boolean empty() 如果队列为空，返回 true ；否则，返回 false


    说明：

    你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
    你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。


[225.用队列实现栈](https://leetcode-cn.com/problems/implement-stack-using-queues)

请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通队列的全部四种操作（push、top、pop 和 empty）。

    实现 MyStack 类：

    void push(int x) 将元素 x 压入栈顶。
    int pop() 移除并返回栈顶元素。
    int top() 返回栈顶元素。
    boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。

    注意：

    你只能使用队列的基本操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
    你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。


#### 9.1 用栈实现队列

```java
class MyQueue {
    private Stack<Integer> s1, s2;
    
    public MyQueue() {
        s1 = new Stack<>();
        s2 = new Stack<>();
    }
    // ...
}
```

```java
/** 添加元素到队尾 */
public void push(int x) {
    s1.push(x);
}
```

```java
/** 返回队头元素 */
public int peek() {
    if (s2.isEmpty())
        // 把 s1 元素压入 s2
        while (!s1.isEmpty())
            s2.push(s1.pop());
    return s2.peek();
}
```

```java
/** 删除队头的元素并返回 */
public int pop() {
    // 先调用 peek 保证 s2 非空
    peek();
    return s2.pop();
}
```
```java
/** 判断队列是否为空 */
public boolean empty() {
    return s1.isEmpty() && s2.isEmpty();
}
```


#### 9.2 用队列实现栈

```java
class MyStack {
    Queue<Integer> q = new LinkedList<>();
    int top_elem = 0;

    /** 添加元素到栈顶 */
    public void push(int x) {
        // x 是队列的队尾，是栈的栈顶
        q.offer(x);
        top_elem = x;
    }
    
    /** 返回栈顶元素 */
    public int top() {
        return top_elem;
    }
}
```
```java
/** 删除栈顶的元素并返回 */
public int pop() {
    int size = q.size();
    while (size > 1) {
        q.offer(q.poll());
        size--;
    }
    // 之前的队尾元素已经到了队头
    return q.poll();
}
```

```java
/** 删除栈顶的元素并返回 */
public int pop() {
    int size = q.size();
    // 留下队尾 2 个元素
    while (size > 2) {
        q.offer(q.poll());
        size--;
    }
    // 记录新的队尾元素
    top_elem = q.peek();
    q.offer(q.poll());
    // 删除之前的队尾元素
    return q.poll();
}
```
```java
/** 判断栈是否为空 */
public boolean empty() {
    return q.isEmpty();
}
```


## 第三章 算法思维系列

### 1 回溯算法详解

#### 1.1 题目

[46.全排列](https://leetcode-cn.com/problems/permutations)

给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

    输入: [1,2,3]
    输出:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]

[51.N皇后](https://leetcode-cn.com/problems/n-queens)

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。


代码方面，回溯算法的框架：

```python
for 选择 in 选择列表:
    # 做选择
    将该选择从选择列表移除
    路径.add(选择)
    backtrack(路径, 选择列表)
    # 撤销选择
    路径.remove(选择)
    将该选择再加入选择列表
```

#### 1.2 全排列问题


**我们只要在递归之前做出选择，在递归之后撤销刚才的选择**，就能正确得到每个节点的选择列表和路径。

下面，直接看全排列代码：

```java
List<List<Integer>> res = new LinkedList<>();

/* 主函数，输入一组不重复的数字，返回它们的全排列 */
List<List<Integer>> permute(int[] nums) {
    // 记录「路径」
    LinkedList<Integer> track = new LinkedList<>();
    backtrack(nums, track);
    return res;
}

// 路径：记录在 track 中
// 选择列表：nums 中不存在于 track 的那些元素
// 结束条件：nums 中的元素全都在 track 中出现
void backtrack(int[] nums, LinkedList<Integer> track) {
    // 触发结束条件
    if (track.size() == nums.length) {
        res.add(new LinkedList(track));
        return;
    }
    
    for (int i = 0; i < nums.length; i++) {
        // 排除不合法的选择
        if (track.contains(nums[i]))
            continue;
        // 做选择
        track.add(nums[i]);
        // 进入下一层决策树
        backtrack(nums, track);
        // 取消选择
        track.removeLast();
    }
}
```


#### 1.3 N 皇后问题

给你一个 N×N 的棋盘，让你放置 N 个皇后，使得它们不能互相攻击。

PS：皇后可以攻击同一行、同一列、左上左下右上右下四个方向的任意单位。

这个问题本质上跟全排列问题差不多，决策树的每一层表示棋盘上的每一行；每个节点可以做出的选择是，在该行的任意一列放置一个皇后。

直接套用框架:

```cpp
vector<vector<string>> res;

/* 输入棋盘边长 n，返回所有合法的放置 */
vector<vector<string>> solveNQueens(int n) {
    // '.' 表示空，'Q' 表示皇后，初始化空棋盘。
    vector<string> board(n, string(n, '.'));
    backtrack(board, 0);
    return res;
}

// 路径：board 中小于 row 的那些行都已经成功放置了皇后
// 选择列表：第 row 行的所有列都是放置皇后的选择
// 结束条件：row 超过 board 的最后一行
void backtrack(vector<string>& board, int row) {
    // 触发结束条件
    if (row == board.size()) {
        res.push_back(board);
        return;
    }
    
    int n = board[row].size();
    for (int col = 0; col < n; col++) {
        // 排除不合法选择
        if (!isValid(board, row, col)) 
            continue;
        // 做选择
        board[row][col] = 'Q';
        // 进入下一行决策
        backtrack(board, row + 1);
        // 撤销选择
        board[row][col] = '.';
    }
}
```

这部分主要代码，其实跟全排列问题差不多，`isValid` 函数的实现也很简单：

```cpp
/* 是否可以在 board[row][col] 放置皇后？ */
bool isValid(vector<string>& board, int row, int col) {
    int n = board.size();
    // 检查列是否有皇后互相冲突
    for (int i = 0; i < n; i++) {
        if (board[i][col] == 'Q')
            return false;
    }
    // 检查右上方是否有皇后互相冲突
    for (int i = row - 1, j = col + 1; 
            i >= 0 && j < n; i--, j++) {
        if (board[i][j] == 'Q')
            return false;
    }
    // 检查左上方是否有皇后互相冲突
    for (int i = row - 1, j = col - 1;
            i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 'Q')
            return false;
    }
    return true;
}
```

**有的时候，我们并不想得到所有合法的答案，只想要一个答案，怎么办呢**？比如解数独的算法，找所有解法复杂度太高，只要找到一种解法就可以。

其实特别简单，只要稍微修改一下回溯算法的代码即可：

```cpp
// 函数找到一个答案后就返回 true
bool backtrack(vector<string>& board, int row) {
    // 触发结束条件
    if (row == board.size()) {
        res.push_back(board);
        return true;
    }
    ...
    for (int col = 0; col < n; col++) {
        ...
        board[row][col] = 'Q';

        if (backtrack(board, row + 1))
            return true;
        
        board[row][col] = '.';
    }

    return false;
}
```


#### 1.4 其他语言实现


[46.全排列](https://leetcode-cn.com/problems/permutations)

```java
List<List<Integer>> res = new LinkedList<>();

/* 主函数，输入一组不重复的数字，返回它们的全排列 */
List<List<Integer>> permute(int[] nums) {
    // 记录「路径」
    LinkedList<Integer> track = new LinkedList<>();
    backtrack(nums, track);
    return res;
}

// 路径：记录在 track 中
// 选择列表：nums 中不存在于 track 的那些元素
// 结束条件：nums 中的元素全都在 track 中出现
void backtrack(int[] nums, LinkedList<Integer> track) {
    // 触发结束条件
    if (track.size() == nums.length) {
        res.add(new LinkedList(track));
        return;
    }
    
    for (int i = 0; i < nums.length; i++) {
        // 排除不合法的选择
        if (track.contains(nums[i]))
            continue;
        // 做选择
        track.add(nums[i]);
        // 进入下一层决策树
        backtrack(nums, track);
        // 取消选择
        track.removeLast();
    }
}
```

### 2 回溯算法团灭子集、排列、组合问题

#### 2.1 子集

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。


    示例 1：

    输入：nums = [1,2,3]
    输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


```cpp
vector<vector<int>> res;

vector<vector<int>> subsets(vector<int>& nums) {
    // 记录走过的路径
    vector<int> track;
    backtrack(nums, 0, track);
    return res;
}

void backtrack(vector<int>& nums, int start, vector<int>& track) {
    res.push_back(track);
    for (int i = start; i < nums.size(); i++) {
        // 做选择
        track.push_back(nums[i]);
        // 回溯
        backtrack(nums, i + 1, track);
        // 撤销选择
        track.pop_back();
    }
}
```

#### 2.2 组合

输入两个数字 `n, k`，算法输出 `[1..n]` 中 k 个数字的所有组合。

```cpp
vector<vector<int>> combine(int n, int k);
```

比如输入 `n = 4, k = 2`，输出如下结果，顺序无所谓，但是不能包含重复（按照组合的定义，`[1,2]` 和 `[2,1]` 也算重复）：

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4]
]



```cpp
vector<vector<int>>res;

vector<vector<int>> combine(int n, int k) {
    if (k <= 0 || n <= 0) return res;
    vector<int> track;
    backtrack(n, k, 1, track);
    return res;
}

void backtrack(int n, int k, int start, vector<int>& track) {
    // 到达树的底部
    if (k == track.size()) {
        res.push_back(track);
        return;
    }
    // 注意 i 从 start 开始递增
    for (int i = start; i <= n; i++) {
        // 做选择
        track.push_back(i);
        backtrack(n, k, i + 1, track);
        // 撤销选择
        track.pop_back();
    }
}
```

#### 2.3 排列

输入一个**不包含重复数字**的数组 `nums`，返回这些数字的全部排列。

```cpp
vector<vector<int>> permute(vector<int>& nums);
```

比如说输入数组 `[1,2,3]`，输出结果应该如下，顺序无所谓，不能有重复：

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

```java
List<List<Integer>> res = new LinkedList<>();

/* 主函数，输入一组不重复的数字，返回它们的全排列 */
List<List<Integer>> permute(int[] nums) {
    // 记录「路径」
    LinkedList<Integer> track = new LinkedList<>();
    backtrack(nums, track);
    return res;
}

void backtrack(int[] nums, LinkedList<Integer> track) {
    // 触发结束条件
    if (track.size() == nums.length) {
        res.add(new LinkedList(track));
        return;
    }
    
    for (int i = 0; i < nums.length; i++) {
        // 排除不合法的选择
        if (track.contains(nums[i]))
            continue;
        // 做选择
        track.add(nums[i]);
        // 进入下一层决策树
        backtrack(nums, track);
        // 取消选择
        track.removeLast();
    }
}
```

#### 2.4 其他实现

[userLF](https://github.com/userLF)提供全排列的java代码：

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
  List<List<Integer>> res = new ArrayList<>();
  public List<List<Integer>> permute(int[] nums) {
    res.clear();
    dfs(nums, 0);//
    return res;
  }

  public void dfs(int[] n, int start) {//start表示要被替换元素的位置
    if( start >= n.length) {
      List<Integer> list = new ArrayList<Integer>();
      for(int i : n) {
        list.add(i);
      }
      res.add(list);
      return;
    }

    for(int i = start; i< n.length; i++) {//i从start开始，如果从start+1开始的话，会把当前序列遗漏掉直接保存了下一个序列
      int temp= n[i];
      n[i] = n[start];
      n[start] = temp;
      dfs(n, start + 1);//递归下一个位置
      //回到上一个状态
      n[start] = n[i];
      n[i] = temp;
    }
  }
}

```


### 3 二分查找详解


#### 3.1 二分查找框架

```java
int binarySearch(int[] nums, int target) {
    int left = 0, right = ...;

    while(...) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            ...
        } else if (nums[mid] < target) {
            left = ...
        } else if (nums[mid] > target) {
            right = ...
        }
    }
    return ...;
}
```

#### 3.2 寻找一个数（基本的二分搜索）

```java
int binarySearch(int[] nums, int target) {
    int left = 0; 
    int right = nums.length - 1; // 注意

    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(nums[mid] == target)
            return mid; 
        else if (nums[mid] < target)
            left = mid + 1; // 注意
        else if (nums[mid] > target)
            right = mid - 1; // 注意
    }
    return -1;
}
```

#### 3.3 寻找左侧边界的二分搜索

以下是最常见的代码形式，其中的标记是需要注意的细节：

```java
int left_bound(int[] nums, int target) {
    if (nums.length == 0) return -1;
    int left = 0;
    int right = nums.length; // 注意
    
    while (left < right) { // 注意
        int mid = (left + right) / 2;
        if (nums[mid] == target) {
            right = mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid; // 注意
        }
    }
    return left;
}
```

#### 3.4 寻找右侧边界的二分查找

类似寻找左侧边界的算法，这里也会提供两种写法，还是先写常见的左闭右开的写法，只有两处和搜索左侧边界不同，已标注：

```java
int right_bound(int[] nums, int target) {
    if (nums.length == 0) return -1;
    int left = 0, right = nums.length;
    
    while (left < right) {
        int mid = (left + right) / 2;
        if (nums[mid] == target) {
            left = mid + 1; // 注意
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid;
        }
    }
    return left - 1; // 注意
}
```


#### 3.5 逻辑统一

```java
int binary_search(int[] nums, int target) {
    int left = 0, right = nums.length - 1; 
    while(left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1; 
        } else if(nums[mid] == target) {
            // 直接返回
            return mid;
        }
    }
    // 直接返回
    return -1;
}

int left_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else if (nums[mid] == target) {
            // 别返回，锁定左侧边界
            right = mid - 1;
        }
    }
    // 最后要检查 left 越界的情况
    if (left >= nums.length || nums[left] != target)
        return -1;
    return left;
}


int right_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else if (nums[mid] == target) {
            // 别返回，锁定右侧边界
            left = mid + 1;
        }
    }
    // 最后要检查 right 越界的情况
    if (right < 0 || nums[right] != target)
        return -1;
    return right;
}
```

#### 3.6 其他语言实现

**python**

[MarineJoker](https://github.com/MarineJoker) 提供 Python3 代码  

```python
# 基本二分搜索
def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 直接返回
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    # 直接返回
    return -1


# 寻找左侧边界的二分搜索，开区间写法
def left_bound(nums, target):
    left, right = 0, len(nums)
    if right == 0:
        return -1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 锁定左侧边界
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 检查left越界情况
    if left >= len(nums) or nums[left] != target:
        return -1
    return left


# 寻找右侧边界的二分搜索，开区间写法
def right_bound(nums, target):
    left, right = 0, len(nums)
    if right == 0:
        return -1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 锁定右侧边界
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 检查越界情况
    if left == 0 or nums[left - 1] != target:
        return -1
    return left - 1


# 寻找左侧边界的二分搜索，闭区间写法
def left_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 锁定左侧边界
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    # 检查left越界情况
    if left >= len(nums) or nums[left] != target:
        return -1
    return left

# 寻找右侧边界的二分搜索，闭区间写法
def right_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 锁定右侧边界
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    # 检查right越界情况
    if right < 0 or nums[right] != target:
        return -1
    return right
```



### 4 双指针技巧总结

#### 4.1 滑动窗口技巧

[76.最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring)

给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。


    示例 1：

    输入：s = "ADOBECODEBANC", t = "ABC"
    输出："BANC"



[567.字符串的排列](https://leetcode-cn.com/problems/permutation-in-string)

给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的 子串 。


    示例 1：

    输入: s1 = "ab" s2 = "eidbaooo"
    输出: True
    解释: s2 包含 s1 的排列之一 ("ba").


[438.找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string)

给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

    说明：

    字母异位词指字母相同，但排列不同的字符串。
    不考虑答案输出的顺序。
    示例 1:

    输入:
    s: "cbaebabacd" p: "abc"

    输出:
    [0, 6]

    解释:
    起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。


[3.无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters)

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

    示例 1:

    输入: s = "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

#### 4.2 最小覆盖子串

```cpp
string minWindow(string s, string t) {
    // 记录最短子串的开始位置和长度
    int start = 0, minLen = INT_MAX;
    int left = 0, right = 0;
    
    unordered_map<char, int> window;
    unordered_map<char, int> needs;
    for (char c : t) needs[c]++;
    
    int match = 0;
    
    while (right < s.size()) {
        char c1 = s[right];
        if (needs.count(c1)) {
            window[c1]++;
            if (window[c1] == needs[c1]) 
                match++;
        }
        right++;
        
        while (match == needs.size()) {
            if (right - left < minLen) {
                // 更新最小子串的位置和长度
                start = left;
                minLen = right - left;
            }
            char c2 = s[left];
            if (needs.count(c2)) {
                window[c2]--;
                if (window[c2] < needs[c2])
                    match--;
            }
            left++;
        }
    }
    return minLen == INT_MAX ?
                "" : s.substr(start, minLen);
}
```

#### 4.3 找到字符串中所有字母异位词

```cpp
vector<int> findAnagrams(string s, string t) {
    // 用数组记录答案
    vector<int> res;
    int left = 0, right = 0;
    unordered_map<char, int> needs;
    unordered_map<char, int> window;
    for (char c : t) needs[c]++;
    int match = 0;
    
    while (right < s.size()) {
        char c1 = s[right];
        if (needs.count(c1)) {
            window[c1]++;
            if (window[c1] == needs[c1])
                match++;
        }
        right++;

        while (match == needs.size()) {
            // 如果 window 的大小合适
            // 就把起始索引 left 加入结果
            if (right - left == t.size()) {
                res.push_back(left);
            }
            char c2 = s[left];
            if (needs.count(c2)) {
                window[c2]--;
                if (window[c2] < needs[c2])
                    match--;
            }
            left++;
        }
    }
    return res;
}
```
#### 4.4 无重复字符的最长子串

类似之前的思路，使用 window 作为计数器记录窗口中的字符出现次数，然后先向右移动 right，当 window 中出现重复字符时，开始移动 left 缩小窗口，如此往复：

```cpp
int lengthOfLongestSubstring(string s) {
    int left = 0, right = 0;
    unordered_map<char, int> window;
    int res = 0; // 记录最长长度

    while (right < s.size()) {
        char c1 = s[right];
        window[c1]++;
        right++;
        // 如果 window 中出现重复字符
        // 开始移动 left 缩小窗口
        while (window[c1] > 1) {
            char c2 = s[left];
            window[c2]--;
            left++;
        }
        res = max(res, right - left);
    }
    return res;
}
```
#### 4.5 其他语言实现


[Jiajun](https://github.com/liujiajun) 提供最小覆盖子串 Python3 代码：
```python3
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 最短子串开始位置和长度
        start, min_len = 0, float('Inf')
        left, right = 0, 0
        res = s
        
        # 两个计数器
        needs = Counter(t)
        window = collections.defaultdict(int) 
        # defaultdict在访问的key不存在的时候返回默认值0, 可以减少一次逻辑判断
        
        match = 0
        
        while right < len(s):
            c1 = s[right]
            if needs[c1] > 0:
                window[c1] += 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1
            
            while match == len(needs):
                if right - left < min_len:
                    # 更新最小子串长度
                    min_len = right - left
                    start = left
                c2 = s[left]
                if needs[c2] > 0:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        
        return s[start:start+min_len] if min_len != float("Inf") else ""
```


### 5 twoSum问题的核心思想

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 
示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。


[1.两数之和](https://leetcode-cn.com/problems/two-sum)

[170.两数之和 III - 数据结构设计](https://leetcode-cn.com/problems/two-sum-iii-data-structure-design)

#### 5.1 TwoSum I

这个问题的**最基本形式**是这样：给你一个数组和一个整数 `target`，可以保证数组中**存在**两个数的和为 `target`，请你返回这两个数的索引。

比如输入 `nums = [3,1,3,6], target = 6`，算法应该返回数组 `[0,2]`，因为 3 + 3 = 6。

这个问题如何解决呢？首先最简单粗暴的办法当然是穷举了：

```java
int[] twoSum(int[] nums, int target) {

    for (int i = 0; i < nums.length; i++) 
        for (int j = i + 1; j < nums.length; j++) 
            if (nums[j] == target - nums[i]) 
                return new int[] { i, j };

    // 不存在这么两个数
    return new int[] {-1, -1};
}
```

这个解法非常直接，时间复杂度 O(N^2)，空间复杂度 O(1)。

可以通过一个哈希表减少时间复杂度：

```java
int[] twoSum(int[] nums, int target) {
    int n = nums.length;
    index<Integer, Integer> index = new HashMap<>();
    // 构造一个哈希表：元素映射到相应的索引
    for (int i = 0; i < n; i++)
        index.put(nums[i], i);
    
    for (int i = 0; i < n; i++) {
        int other = target - nums[i];
        // 如果 other 存在且不是 nums[i] 本身
        if (index.containsKey(other) && index.get(other) != i)
            return new int[] {i, index.get(other)};
    }
    
    return new int[] {-1, -1};
}
```

#### 5.2 TwoSum II

优化：借助**哈希集合**来针对性优化 `find` 方法

```java
class TwoSum {
    Set<Integer> sum = new HashSet<>();
    List<Integer> nums = new ArrayList<>();

    public void add(int number) {
        // 记录所有可能组成的和
        for (int n : nums)
            sum.add(n + number);
        nums.add(number);
    }
    
    public boolean find(int value) {
        return sum.contains(value);
    }
}
```

#### 5.3 python实现

由[JodyZ0203](https://github.com/JodyZ0203)提供 1. Two Sums Python3 解法代码:

只用一个哈希表

```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 提前构造一个哈希表
        hashTable = {}
        # 寻找两个目标数值
        for i, n in enumerate(nums):
            other_num = target - n
            # 如果存在这个余数 other_num
            if other_num in hashTable.keys():
                # 查看是否存在哈希表里，如果存在的话就返回数组
                return [i, hashTable[other_num]]
            # 如果不存在的话继续处理剩余的数
            hashTable[n] = i
```


### 6 常用的位操作

#### 6.1 几个有趣的位操作

1. **利用或操作 `|` 和空格将英文字符转换为小写**

```c
('a' | ' ') = 'a'
('A' | ' ') = 'a'
```

2. **利用与操作 `&` 和下划线将英文字符转换为大写**

```c
('b' & '_') = 'B'
('B' & '_') = 'B'
```

3. **利用异或操作 `^` 和空格进行英文字符大小写互换**

```c
('d' ^ ' ') = 'D'
('D' ^ ' ') = 'd'
```

以上操作能够产生奇特效果的原因在于 ASCII 编码。字符其实就是数字，恰巧这些字符对应的数字通过位运算就能得到正确的结果，有兴趣的读者可以查 ASCII 码表自己算算，本文就不展开讲了。

4. **判断两个数是否异号**

```cpp
int x = -1, y = 2;
bool f = ((x ^ y) < 0); // true

int x = 3, y = 2;
bool f = ((x ^ y) < 0); // false
```

这个技巧还是很实用的，利用的是补码编码的符号位。如果不用位运算来判断是否异号，需要使用 if else 分支，还挺麻烦的。读者可能想利用乘积或者商来判断两个数是否异号，但是这种处理方式可能造成溢出，从而出现错误。

5. **不用临时变量交换两个数**

```c
int a = 1, b = 2;
a ^= b;
b ^= a;
a ^= b;
// 现在 a = 2, b = 1
```

6. **加一**

```c
int n = 1;
n = -~n;
// 现在 n = 2
```

7. **减一**

```c
int n = 2;
n = ~-n;
// 现在 n = 1
```

PS：上面这三个操作就纯属装逼用的，没啥实际用处，大家了解了解乐呵一下就行。

**算法常用操作**

 `n&(n-1)` 这个操作是算法中常见的，作用是消除数字 `n` 的二进制表示中的最后一个 1。



1. **计算汉明权重（Hamming Weight）**

就是让你返回 n 的二进制表示中有几个 1。因为 n & (n - 1) 可以消除最后一个 1，所以可以用一个循环不停地消除 1 同时计数，直到 n 变成 0 为止。

```cpp
int hammingWeight(uint32_t n) {
    int res = 0;
    while (n != 0) {
        n = n & (n - 1);
        res++;
    }
    return res;
}
```

2. **判断一个数是不是 2 的指数**

一个数如果是 2 的指数，那么它的二进制表示一定只含有一个 1：

```cpp
2^0 = 1 = 0b0001
2^1 = 2 = 0b0010
2^2 = 4 = 0b0100
```

如果使用  `n&(n-1)` 的技巧就很简单了（注意运算符优先级，括号不可以省略）：

```cpp
bool isPowerOfTwo(int n) {
    if (n <= 0) return false;
    return (n & (n - 1)) == 0;
}
```

**3、查找只出现一次的元素**


这里就可以运用异或运算的性质：

一个数和它本身做异或运算结果为 0，即 `a ^ a = 0`；一个数和 0 做异或运算的结果为它本身，即 `a ^ 0 = a`。

对于这道题目，我们只要把所有数字进行异或，成对儿的数字就会变成 0，落单的数字和 0 做异或还是它本身，所以最后异或的结果就是只出现一次的元素：

```cpp
int singleNumber(vector<int>& nums) {
    int res = 0;
    for (int n : nums) {
        res ^= n;
    }
    return res;
}
```

### 7 烧饼排序

给你一个整数数组 arr ，请使用 煎饼翻转 完成对数组的排序。

一次煎饼翻转的执行过程如下：

选择一个整数 k ，1 <= k <= arr.length
反转子数组 arr[0...k-1]（下标从 0 开始）
例如，arr = [3,2,1,4] ，选择 k = 3 进行一次煎饼翻转，反转子数组 [3,2,1] ，得到 arr = [1,2,3,4] 。

以数组形式返回能使 arr 有序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 10 * arr.length 范围内的有效答案都将被判断为正确。

#### 7.1 题目

烧饼排序是个很有意思的实际问题：假设盘子上有 `n` 块**面积大小不一**的烧饼，你如何用一把锅铲进行若干次翻转，让这些烧饼的大小有序（小的在上，大的在下）


```java
// 记录反转操作序列
LinkedList<Integer> res = new LinkedList<>();

List<Integer> pancakeSort(int[] cakes) {
    sort(cakes, cakes.length);
    return res;
}

void sort(int[] cakes, int n) {
    // base case
    if (n == 1) return;
    
    // 寻找最大饼的索引
    int maxCake = 0;
    int maxCakeIndex = 0;
    for (int i = 0; i < n; i++)
        if (cakes[i] > maxCake) {
            maxCakeIndex = i;
            maxCake = cakes[i];
        }
    
    // 第一次翻转，将最大饼翻到最上面
    reverse(cakes, 0, maxCakeIndex);
    res.add(maxCakeIndex + 1);
    // 第二次翻转，将最大饼翻到最下面
    reverse(cakes, 0, n - 1);
    res.add(n);

    // 递归调用
    sort(cakes, n - 1);
}

void reverse(int[] arr, int i, int j) {
    while (i < j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        i++; j--;
    }
}
```


#### 7.2 其他语言实现

**python**

[fengshuu](https://github.com/fengshuu) 提供 Python3 解法代码：

```python
class Solution:
    # 记录反转操作序列
    def __init__(self):
        self.res = []

    def pancakeSort(self, arr: List[int]) -> List[int]:

        self.sort(arr, len(arr))
        return self.res

    def sort(self, cakes: List[int], n: int):
        # base case
        if 1 == n:
            return

        # 寻找最大饼的索引
        max_cake_index = cakes[:n].index(n)

        # 下面进行把最大的饼放到最后的两次翻转
        # 如果最后一个饼就是最大的, 就不需要翻转, 直接进行下次递归
        if max_cake_index != n - 1:
            # 第一次翻转, 将最大饼翻到最上面
            # 如果第一个饼本来就是最大的, 就不需要第一次翻转.
            if max_cake_index != 0:
                cakes[:max_cake_index + 1] = cakes[:max_cake_index + 1][::-1]
                self.res.append(max_cake_index + 1)

            # 第二次翻转，将最大饼翻到最下面
            cakes[:n] = cakes[:n][::-1]
            self.res.append(n)

        # 递归调用
        self.sort(cakes, n - 1)
```


**c++**

[fengshuu](https://github.com/fengshuu) 提供 C++ 解法代码：

```cpp
class Solution {
public:
    vector<int> pancakeSort(vector<int>& arr) {
        sort(arr, arr.size());
        return res;
    }
    
private:
    // 记录反转操作序列
    vector<int> res;
    void sort(vector<int>& cakes, int n){
        // base case
        if(n == 1) return;
        
        // 寻找最大饼的索引
        int maxCakeIndex = max_element(cakes.begin(), cakes.begin() + n) - cakes.begin();
        
        // 下面进行把最大的饼放到最后的两次翻转
        // 如果最后一个饼就是最大的, 就不需要翻转, 直接进行下次递归
        if (maxCakeIndex == n-1){
            sort(cakes, n - 1);
            return;
        }
            
        // 第一次翻转, 将最大饼翻到最上面
        // 如果第一个饼本来就是最大的, 就不需要第一次翻转.
        if (maxCakeIndex != 0) {
            reverse(cakes.begin(), cakes.begin() + maxCakeIndex + 1);
            res.push_back(maxCakeIndex + 1);
        }
        
        // 第二次翻转，将最大饼翻到最下面
        reverse(cakes.begin(), cakes.begin() + n);
        res.push_back(n);
        
        // 递归调用
        sort(cakes, n - 1);
    }
};
```

**java**

[L-WEIWEI](https://github.com/L-WWEEII) 提供 第969题的 Java 代码：

```java
class Solution {
    public List<Integer> pancakeSort(int[] A) {
        List<Integer> ans = new ArrayList<Integer>();
        int len = A.length;
        if(len == 0){
            return ans;
        }
        // maxIndex[0] == 当前轮次的最大元素， maxIndex[1] == 最大元素下标
        int[] maxIndex = new int[2];
        maxIndex[0] = Integer.MIN_VALUE;
        int maxCount = 0;
        // maxCount == len 时，说明完成了整个数组的最大值沉底操作，
        while(maxCount < len - 1){
            maxCount = maxValueDown(A, maxIndex, maxCount, ans);
            // 每做完一次最大值沉底操作，初始化最大元素值
            maxIndex[0] = Integer.MIN_VALUE;
        }
        return ans;
    }
    public int maxValueDown(int[] A, int[] maxIndex, int maxCount, List<Integer> ans){
        // 遍历条件为 i < A.length - maxCount ， 每次最大值沉底时，maxCount + 1，因此下次遍历即可不对最后 maxCount 个元素做操作
        for(int i = 0; i < A.length - maxCount; i++){
            // 元素大于当前储存的元素时，将值与下标 copy 到 maxIndex 数组中
            if(A[i] > maxIndex[0]){
                maxIndex[0] = A[i];
                maxIndex[1] = i;
            }
        }
        // 如果当前轮次最大元素的下标的下一位是上一轮次的最大下标，则不做翻转操作，直接返回 maxCount + 1 
        if(maxIndex[1] + 1 == A.length - maxCount){
            return maxCount + 1;
        }
        // 使用最大值沉底时，当本轮最大值在首位时，不需要再将其先翻转至首位，所以不添加
        if(maxIndex[1] > 0){
            // 将该轮次要翻转的下标添加到结果集中，结果集中需要的是翻转的位置而不是下标，所以添加时下标得 + 1
            ans.add(maxIndex[1] + 1);
        }
        // 双指针原地交换数组中的值
        // 左指针指0
        int left = 0;
        // 右指针指向当前轮次最大元素的下标
        int right = maxIndex[1];
        while(left < right){
            // 交换元素值
            A[left] += A[right];
            A[right] = A[left] - A[right];
            A[left] -= A[right];
            left++;
            right--;
        }
        // 上面交换玩元素值后，当前轮次最大元素排在首位，再从上一轮次最大元素 - 1 的位置翻转
        //     则当前轮次的最大元素成功沉底
        ans.add(A.length - maxCount);
        left = 0;
        right = A.length - 1 - maxCount;
        while(left < right){
            A[left] += A[right];
            A[right] = A[left] - A[right];
            A[left] -= A[right];
            left++;
            right--;
        }
        return maxCount + 1;
    }
}
```



### 8 前缀和技巧

560. 和为K的子数组

给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。


#### 8.1 前缀和思路

前缀和的思路是这样的，对于一个给定的数组 `nums`，我们额外开辟一个前缀和数组进行预处理：

```java
int n = nums.length;
// 前缀和数组
int[] preSum = new int[n + 1];
preSum[0] = 0;
for (int i = 0; i < n; i++)
    preSum[i + 1] = preSum[i] + nums[i];
```

求有多少个子数组的和为 k，借助前缀和技巧很容易写出一个解法：

以用哈希表，在记录前缀和的同时记录该前缀和出现的次数。

```java
int subarraySum(int[] nums, int k) {
    int n = nums.length;
    // map：前缀和 -> 该前缀和出现的次数
    HashMap<Integer, Integer> 
        preSum = new HashMap<>();
    // base case
    preSum.put(0, 1);

    int ans = 0, sum0_i = 0;
    for (int i = 0; i < n; i++) {
        sum0_i += nums[i];
        // 这是我们想找的前缀和 nums[0..j]
        int sum0_j = sum0_i - k;
        // 如果前面有这个前缀和，则直接更新答案
        if (preSum.containsKey(sum0_j))
            ans += preSum.get(sum0_j);
        // 把前缀和 nums[0..i] 加入并记录出现次数
        preSum.put(sum0_i, 
            preSum.getOrDefault(sum0_i, 0) + 1);
    }
    return ans;
}
```

#### 8.2 应用

前缀和不难，却很有用，主要用于处理数组区间的问题。

比如说，让你统计班上同学考试成绩在不同分数段的百分比，也可以利用前缀和技巧：

```java
int[] scores; // 存储着所有同学的分数
// 试卷满分 150 分
int[] count = new int[150 + 1]
// 记录每个分数有几个同学
for (int score : scores)
    count[score]++
// 构造前缀和
for (int i = 1; i < count.length; i++)
    count[i] = count[i] + count[i-1];
```

### 9 字符串乘法

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"

#### 9.1 实现

```java
string multiply(string num1, string num2) {
    int m = num1.size(), n = num2.size();
    // 结果最多为 m + n 位数
    vector<int> res(m + n, 0);
    // 从个位数开始逐位相乘
    for (int i = m - 1; i >= 0; i--)
        for (int j = n - 1; j >= 0; j--) {
            int mul = (num1[i]-'0') * (num2[j]-'0');
            // 乘积在 res 对应的索引位置
            int p1 = i + j, p2 = i + j + 1;
            // 叠加到 res 上
            int sum = mul + res[p2];
            res[p2] = sum % 10;
            res[p1] += sum / 10;
        }
    // 结果前缀可能存的 0（未使用的位）
    int i = 0;
    while (i < res.size() && res[i] == 0)
        i++;
    // 将计算结果转化成字符串
    string str;
    for (; i < res.size(); i++)
        str.push_back('0' + res[i]);
    
    return str.size() == 0 ? "0" : str;
}
```
#### 9.2 其他语言实现


**python**

[fengshuu](https://github.com/fengshuu) 提供 Python 解法代码：
```python
def multiply(num1: str, num2: str) -> str:
    m, n = len(num1), len(num2)
    # 结果最多为 m + n 位数
    res = [0] * (m + n)
    # 从个位数开始逐位相乘
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            # 乘积在 res 对应的索引位置
            p1 = i + j
            p2 = i + j + 1
            # 叠加到 res 上
            digit_sum = mul + res[p2]
            res[p2] = digit_sum % 10
            res[p1] += digit_sum // 10

    # 结果前缀可能存的 0（未使用的位）
    i = 0
    while i < len(res) and res[i] == 0:
        i += 1

    # 将计算结果转化成字符串
    result_str = "".join(str(x) for x in res[i:])

    return "0" if len(result_str) == 0 else result_str
```

**java**

[Zane Wang](https://github.com/zanecat) 提供 Java 解法代码：
```java
public String multiply(String num1, String num2) {
    // 初始化字符数组
    char[] s1 = num1.toCharArray();
    char[] s2 = num2.toCharArray();

    // 结果长度最多为两字符串长度之和
    int[] res = new int[s1.length + s2.length];

    // 从个位开始遍历，把两数字中每一位相乘
    for (int i = s1.length - 1; i >= 0; i--) {
        for (int j = s2.length - 1; j >= 0; j--) {
            // 计算乘积，并把乘积放在 res 对应的位置， 暂时不考虑进位
            res[i + j + 1] += (s1[i] - '0') * (s2[j] - '0');
        }
    }

    // 从个位再次遍历，如果上一次遍历中两数乘积为两位数，进位并叠加到前面一位
    int carry = 0;
    for (int i = res.length - 1; i >= 0; i--) {
        int sum = res[i] + carry;
        res[i] = sum % 10;
        carry = sum / 10;
    }

    //遍历res数组，构造最终答案字符串
    StringBuilder ans = new StringBuilder();
    int i = 0;

    // 首先找到不为0的第一位
    while (i < res.length - 1 && res[i] == 0) {
        i++;
    }

    // 将后面的数字附加到ans后面
    while (i < res.length) {
        ans.append(res[i++]);
    }
    return ans.toString();
}
```


### 10 FloodFill算法详解及应用

#### 10.1 描述框架

[733.图像渲染](https://leetcode-cn.com/problems/flood-fill)

矩阵，可以抽象为一幅「图」，这就是一个图的遍历问题，也就类似一个 N 叉树遍历的问题。几行代码就能解决，直接上框架吧：

```java
// (x, y) 为坐标位置
void fill(int x, int y) {
    fill(x - 1, y); // 上
    fill(x + 1, y); // 下
    fill(x, y - 1); // 左
    fill(x, y + 1); // 右
}
```

待填充的图像用二维数组 image 表示，元素为初始颜色值。初始坐标点的行坐标为 sr 列坐标为 sc。需要填充的新颜色为 newColor 。

「周围区域」是指颜色相同且在上、下、左、右四个方向上存在相连情况的若干元素。

请用新颜色填充初始坐标点的周围区域，并返回填充后的图像。

```java
int[][] floodFill(int[][] image,
        int sr, int sc, int newColor) {

    int origColor = image[sr][sc];
    fill(image, sr, sc, origColor, newColor);
    return image;
}


void fill(int[][] image, int x, int y,
        int origColor, int newColor) {
    // 出界：超出数组边界
    if (!inArea(image, x, y)) return;
    // 碰壁：遇到其他颜色，超出 origColor 区域
    if (image[x][y] != origColor) return;
    // 已探索过的 origColor 区域
    if (image[x][y] == -1) return;
    
    // choose：打标记，以免重复
    image[x][y] = -1;
    fill(image, x, y + 1, origColor, newColor);
    fill(image, x, y - 1, origColor, newColor);
    fill(image, x - 1, y, origColor, newColor);
    fill(image, x + 1, y, origColor, newColor);
    // unchoose：将标记替换为 newColor
    image[x][y] = newColor;
}


boolean inArea(int[][] image, int x, int y) {
    return x >= 0 && x < image.length
        && y >= 0 && y < image[0].length;
}
```


### 11 区间调度之区间合并问题

[56.合并区间](https://leetcode-cn.com/problems/merge-intervals)

以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

    示例 1：

    输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
    输出：[[1,6],[8,10],[15,18]]
    解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

 

#### 11.1 区间合并

一个区间可以表示为 `[start, end]`，前文聊的区间调度问题，需要按 `end` 排序，以便满足贪心选择性质。而对于区间合并问题，其实按 `end` 和 `start` 排序都可以，不过为了清晰起见，我们选择按 `start` 排序。

**显然，对于几个相交区间合并后的结果区间 `x`，`x.start` 一定是这些相交区间中 `start` 最小的，`x.end` 一定是这些相交区间中 `end` 最大的。**

```python
# intervals 形如 [[1,3],[2,6]...]
def merge(intervals):
    if not intervals: return []
    # 按区间的 start 升序排列
    intervals.sort(key=lambda intv: intv[0])
    res = []
    res.append(intervals[0])
    
    for i in range(1, len(intervals)):
        curr = intervals[i]
        # res 中最后一个元素的引用
        last = res[-1]
        if curr[0] <= last[1]:
            # 找到最大的 end
            last[1] = max(last[1], curr[1])
        else:
            # 处理下一个待合并区间
            res.append(curr)
    return res
```

#### 11.2 其他语言实现

**java**

```java
class Solution {
    /**
     *  1. 先对区间集合进行排序（根据开始位置）
     *  2. 合并的情况一共有三种
     *    a.                        b.                   c.
     *          |---------|             |--------|             |--------|
     *              |---------|              |--|                            |--------|
     *      a和b两种情况，合并取右边界大的值，c情况不合并
     *  
     */

    private int[][] tmp;
    
    public int[][] merge(int[][] intervals) {
        if(intervals == null ||intervals.length == 0)return new int[0][0];
        int length = intervals.length;
        //将列表中的区间按照左端点升序排序
        // Arrays.sort(intervals,(v1,v2) -> v1[0]-v2[0]);
        
        this.tmp = new int[length][2];
        sort(intervals,0,length-1);

        int[][] ans = new int[length][2];
        int index = -1;
        for(int[] interval:intervals){
            // 当结果数组是空是，或者当前区间的起始位置 > 结果数组中最后区间的终止位置（即上图情况c）；
            // 则不合并，直接将当前区间加入结果数组。
            if(index == -1 || interval[0] > ans[index][1]){
                ans[++index] = interval;
            }else{
                // 反之将当前区间合并至结果数组的最后区间（即上图情况a,b）
                ans[index][1] = Math.max(ans[index][1],interval[1]);
            }
        }
        return Arrays.copyOf(ans, index + 1);
    }

    //归并排序
    public void sort(int[][] intervals,int l,int r){
        if(l >= r)return;

        int mid = l + (r-l)/2;
        sort(intervals,l,mid);
        sort(intervals,mid+1,r);

        //合并
        int i=l,j=mid+1;
        for(int k=l;k<=r;k++){
            if(i>mid)tmp[k]=intervals[j++];
            else if(j>r)tmp[k]=intervals[i++];
            else if(intervals[i][0]>intervals[j][0])tmp[k] = intervals[j++];
            else tmp[k] = intervals[i++];
        }

        System.arraycopy(tmp,l,intervals,l,r-l+1);
    }

}
```

**c++**

[Kian](https://github.com/KianKw/) 提供第 56 题 C++ 代码

```c++
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // len 为 intervals 的长度
        int len = intervals.size();
        if (len < 1)
            return {};

        // 按区间的 start 升序排列
        sort(intervals.begin(), intervals.end());

        // 初始化 res 数组
        vector<vector<int>> res;
        res.push_back(intervals[0]);

        for (int i = 1; i < len; i++) {
            vector<int> curr = intervals[i];
            // res.back() 为 res 中最后一个元素的索引
            if (curr[0] <= res.back()[1]) {
                // 找到最大的 end
                res.back()[1] = max(res.back()[1], curr[1]);
            } else {
                // 处理下一个待合并区间
                res.push_back(curr);
            }
        }
        return res;
    }
};
```

### 12 区间调度之区间交集问题

[986.区间列表的交集](https://leetcode-cn.com/problems/interval-list-intersections)

给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。

返回这 两个区间列表的交集 。

形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b 。

两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。

 
    输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
    输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
 


#### 12.1 解法

解决区间问题的思路一般是先排序

已经排好序了，那么可以用两个索引指针在 `A` 和 `B` 中游走，把交集找出来

```python
# A, B 形如 [[0,2],[5,10]...]
def intervalIntersection(A, B):
    i, j = 0, 0 # 双指针
    res = []
    while i < len(A) and j < len(B):
        a1, a2 = A[i][0], A[i][1]
        b1, b2 = B[j][0], B[j][1]
        # 两个区间存在交集
        if b2 >= a1 and a2 >= b1:
            # 计算出交集，加入 res
            res.append([max(a1, b1), min(a2, b2)])
        # 指针前进
        if b2 < a2: j += 1
        else:       i += 1
    return res
```

#### 12.2 java实现

[KiraZh](https://github.com/KiraZh)提供第986题Java代码

```java
class Solution {
    public int[][] intervalIntersection(int[][] A, int[][] B) {
        List<int[]> res = new ArrayList<>();
        int a = 0, b = 0;
        while(a < A.length && b < B.length) {
            // 确定左边界，两个区间左边界的最大值
            int left = Math.max(A[a][0], B[b][0]);
            // 确定右边界，两个区间右边界的最小值
            int right = Math.min(A[a][1], B[b][1]);
            // 左边界小于右边界则加入结果集
            if (left <= right) 
                res.add(new int[] {left, right});
            // 右边界更大的保持不动，另一个指针移动，继续比较
            if(A[a][1] < B[b][1]) a++;
            else b++;
        }
        // 将结果转为数组
        return res.toArray(new int[0][]);
    }
}
```

### 13 信封嵌套问题

给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。

当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

注意：不允许旋转信封。

 
    示例 1：

    输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
    输出：3
    解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

#### 13.1 描述

**先对宽度 `w` 进行升序排序，如果遇到 `w` 相同的情况，则按照高度 `h` 降序排序。之后把所有的 `h` 作为一个数组，在这个数组上计算 LIS 的长度就是答案。**

```java
// envelopes = [[w, h], [w, h]...]
public int maxEnvelopes(int[][] envelopes) {
    int n = envelopes.length;
    // 按宽度升序排列，如果宽度一样，则按高度降序排列
    Arrays.sort(envelopes, new Comparator<int[]>() 
    {
        public int compare(int[] a, int[] b) {
            return a[0] == b[0] ? 
                b[1] - a[1] : a[0] - b[0];
        }
    });
    // 对高度数组寻找 LIS
    int[] height = new int[n];
    for (int i = 0; i < n; i++)
        height[i] = envelopes[i][1];

    return lengthOfLIS(height);
}
```

```java
/* 返回 nums 中 LIS 的长度 */
public int lengthOfLIS(int[] nums) {
    int piles = 0, n = nums.length;
    int[] top = new int[n];
    for (int i = 0; i < n; i++) {
        // 要处理的扑克牌
        int poker = nums[i];
        int left = 0, right = piles;
        // 二分查找插入位置
        while (left < right) {
            int mid = (left + right) / 2;
            if (top[mid] >= poker)
                right = mid;
            else
                left = mid + 1;
        }
        if (left == piles) piles++;
        // 把这张牌放到牌堆顶
        top[left] = poker;
    }
    // 牌堆数就是 LIS 长度
    return piles;
}
```

### 14 洗牌算法

#### 14.1 原理

靠随机选取元素交换来获取随机性

```java
// 得到一个在闭区间 [min, max] 内的随机整数
int randInt(int min, int max);

// 第一种写法
void shuffle(int[] arr) {
    int n = arr.length();
    /******** 区别只有这两行 ********/
    for (int i = 0 ; i < n; i++) {
        // 从 i 到最后随机选一个元素
        int rand = randInt(i, n - 1);
        /*************************/
        swap(arr[i], arr[rand]);
    }
}

// 第二种写法
    for (int i = 0 ; i < n - 1; i++)
        int rand = randInt(i, n - 1);

// 第三种写法
    for (int i = n - 1 ; i >= 0; i--)
        int rand = randInt(0, i);

// 第四种写法
    for (int i = n - 1 ; i > 0; i--)
        int rand = randInt(0, i);
```

#### 14.2 蒙特卡罗方法验证正确性

洗牌算法，或者说随机乱置算法的**正确性衡量标准是：对于每种可能的结果出现的概率必须相等，也就是说要足够随机。**

**第二种思路**，可以这样想，arr 数组中全都是 0，只有一个 1。我们对 arr 进行 100 万次打乱，记录每个索引位置出现 1 的次数，如果每个索引出现的次数差不多，也可以说明每种打乱结果的概率是相等的。

```java
void shuffle(int[] arr);

// 蒙特卡罗方法
int N = 1000000;    
int[] arr = {1,0,0,0,0};
int[] count = new int[arr.length];
for (int i = 0; i < N; i++) {
    shuffle(arr); // 打乱 arr
    for (int j = 0; j < arr.length; j++) 
        if (arr[j] == 1) {
            count[j]++;
            break;
        }
}
for (int feq : count) 
    print(feq / N + " "); // 频率
```

### 15 递归详解

#### 15.1 写递归的技巧

**明白一个函数的作用并相信它能完成这个任务，千万不要试图跳进细节。**

以下**详解 LeetCode 的一道题来说明**：给一课二叉树，和一个目标值，节点上的值有正有负，返回树中和等于目标值的路径条数，让你编写 pathSum 函数：

```
/* 来源于 LeetCode PathSum III： https://leetcode.com/problems/path-sum-iii/ */
root = [10,5,-3,3,2,null,11,3,-2,null,1],
sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
```

```cpp
/* 看不懂没关系，底下有更详细的分析版本，这里突出体现递归的简洁优美 */
int pathSum(TreeNode root, int sum) {
    if (root == null) return 0;
    return count(root, sum) + 
        pathSum(root.left, sum) + pathSum(root.right, sum);
}
int count(TreeNode node, int sum) {
    if (node == null) return 0;
    return (node.val == sum) + 
        count(node.left, sum - node.val) + count(node.right, sum - node.val);
}
```

PathSum 函数：给他一个节点和一个目标值，他返回以这个节点为根的树中，和为目标值的路径总数。

count 函数：给他一个节点和一个目标值，他返回以这个节点为根的树中，能凑出几个以该节点为路径开头，和为目标值的路径总数。

```cpp
/* 有了以上铺垫，详细注释一下代码 */
int pathSum(TreeNode root, int sum) {
    if (root == null) return 0;
    int pathImLeading = count(root, sum); // 自己为开头的路径数
    int leftPathSum = pathSum(root.left, sum); // 左边路径总数（相信他能算出来）
    int rightPathSum = pathSum(root.right, sum); // 右边路径总数（相信他能算出来）
    return leftPathSum + rightPathSum + pathImLeading;
}
int count(TreeNode node, int sum) {
    if (node == null) return 0;
    // 我自己能不能独当一面，作为一条单独的路径呢？
    int isMe = (node.val == sum) ? 1 : 0;
    // 左边的小老弟，你那边能凑几个 sum - node.val 呀？
    int leftBrother = count(node.left, sum - node.val); 
    // 右边的小老弟，你那边能凑几个 sum - node.val 呀？
    int rightBrother = count(node.right, sum - node.val);
    return  isMe + leftBrother + rightBrother; // 我这能凑这么多个
}
```

#### 15.2 分治算法

**归并排序**，典型的分治算法；分治，典型的递归结构。

分治算法可以分三步走：分解 -> 解决 -> 合并

1. 分解原问题为结构相同的子问题。
2. 分解到某个容易求解的边界之后，进行第归求解。
3. 将子问题的解合并成原问题的解。

归并排序，我们就叫这个函数`merge_sort`吧，按照我们上面说的，要明确该函数的职责，即**对传入的一个数组排序**。OK，那么这个问题能不能分解呢？当然可以！给一个数组排序，不就等于给该数组的两半分别排序，然后合并就完事了。

```cpp
void merge_sort(一个数组) {
    if (可以很容易处理) return;
    merge_sort(左半个数组);
    merge_sort(右半个数组);
    merge(左半个数组, 右半个数组);
}
```

好了，这个算法也就这样了，完全没有任何难度。记住之前说的，相信函数的能力，传给他半个数组，那么这半个数组就已经被排好了。而且你会发现这不就是个二叉树遍历模板吗？为什么是后序遍历？因为我们分治算法的套路是 **分解 -> 解决（触底） -> 合并（回溯）** 啊，先左右分解，再处理合并，回溯就是在退栈，就相当于后序遍历了。至于`merge`函数，参考两个有序链表的合并，简直一模一样，下面直接贴代码吧。

下面参考《算法4》的 Java 代码，很漂亮。由此可见，不仅算法思想思想重要，编码技巧也是挺重要的吧！多思考，多模仿。

```java
public class Merge {
    // 不要在 merge 函数里构造新数组了，因为 merge 函数会被多次调用，影响性能
    // 直接一次性构造一个足够大的数组，简洁，高效
    private static Comparable[] aux;

     public static void sort(Comparable[] a) {
        aux = new Comparable[a.length];
        sort(a, 0, a.length - 1);
    }

    private static void sort(Comparable[] a, int lo, int hi) {
        if (lo >= hi) return;
        int mid = lo + (hi - lo) / 2;
        sort(a, lo, mid);
        sort(a, mid + 1, hi);
        merge(a, lo, mid, hi);
    }

    private static void merge(Comparable[] a, int lo, int mid, int hi) {
        int i = lo, j = mid + 1;
        for (int k = lo; k <= hi; k++)
            aux[k] = a[k];
        for (int k = lo; k <= hi; k++) {
            if      (i > mid)              { a[k] = aux[j++]; }
            else if (j > hi)               { a[k] = aux[i++]; }
            else if (less(aux[j], aux[i])) { a[k] = aux[j++]; }
            else                           { a[k] = aux[i++]; }
        }
    }

    private static boolean less(Comparable v, Comparable w) {
        return v.compareTo(w) < 0;
    }
}
```


## 第四章、高频面试系列

### 1 如何实现LRU算法

计算机的缓存容量有限，如果缓存满了就要删除一些内容，给新内容腾位置。但问题是，删除哪些内容呢？我们肯定希望删掉哪些没什么用的缓存，而把有用的数据继续留在缓存里，方便之后继续使用。那么，什么样的数据，我们判定为「有用的」的数据呢？

LRU 缓存淘汰算法就是一种常用策略。LRU 的全称是 Least Recently Used，也就是说我们认为最近使用过的数据应该是是「有用的」，很久都没用过的数据应该是无用的，内存满了就优先删那些很久没用过的数据。

设计：

1、显然 `cache` 中的元素必须有时序，以区分最近使用的和久未使用的数据，当容量满了之后要删除最久未使用的那个元素腾位置。

2、我们要在 `cache` 中快速找某个 `key` 是否已存在并得到对应的 `val`；

3、每次访问 `cache` 中的某个 `key`，需要将这个元素变为最近使用的，也就是说 `cache` 要支持在任意位置快速插入和删除元素。


#### 1.1 实现

```java
class Node {
    public int key, val;
    public Node next, prev;
    public Node(int k, int v) {
        this.key = k;
        this.val = v;
    }
}
```

```java
class DoubleList {  
    // 头尾虚节点
    private Node head, tail;  
    // 链表元素数
    private int size;
    
    public DoubleList() {
        // 初始化双向链表的数据
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
        size = 0;
    }

    // 在链表尾部添加节点 x，时间 O(1)
    public void addLast(Node x) {
        x.prev = tail.prev;
        x.next = tail;
        tail.prev.next = x;
        tail.prev = x;
        size++;
    }

    // 删除链表中的 x 节点（x 一定存在）
    // 由于是双链表且给的是目标 Node 节点，时间 O(1)
    public void remove(Node x) {
        x.prev.next = x.next;
        x.next.prev = x.prev;
        size--;
    }
    
    // 删除链表中第一个节点，并返回该节点，时间 O(1)
    public Node removeFirst() {
        if (head.next == tail)
            return null;
        Node first = head.next;
        remove(first);
        return first;
    }

    // 返回链表长度，时间 O(1)
    public int size() { return size; }

}
```
**注意我们实现的双链表 API 只能从尾部插入，也就是说靠尾部的数据是最近使用的，靠头部的数据是最久为使用的**。

```java
class LRUCache {
    // key -> Node(key, val)
    private HashMap<Integer, Node> map;
    // Node(k1, v1) <-> Node(k2, v2)...
    private DoubleList cache;
    // 最大容量
    private int cap;
    
    public LRUCache(int capacity) {
        this.cap = capacity;
        map = new HashMap<>();
        cache = new DoubleList();
    }
```

```java
/* 将某个 key 提升为最近使用的 */
private void makeRecently(int key) {
    Node x = map.get(key);
    // 先从链表中删除这个节点
    cache.remove(x);
    // 重新插到队尾
    cache.addLast(x);
}

/* 添加最近使用的元素 */
private void addRecently(int key, int val) {
    Node x = new Node(key, val);
    // 链表尾部就是最近使用的元素
    cache.addLast(x);
    // 别忘了在 map 中添加 key 的映射
    map.put(key, x);
}

/* 删除某一个 key */
private void deleteKey(int key) {
    Node x = map.get(key);
    // 从链表中删除
    cache.remove(x);
    // 从 map 中删除
    map.remove(key);
}

/* 删除最久未使用的元素 */
private void removeLeastRecently() {
    // 链表头部的第一个元素就是最久未使用的
    Node deletedNode = cache.removeFirst();
    // 同时别忘了从 map 中删除它的 key
    int deletedKey = deletedNode.key;
    map.remove(deletedKey);
}
```

```java
public int get(int key) {
    if (!map.containsKey(key)) {
        return -1;
    }
    // 将该数据提升为最近使用的
    makeRecently(key);
    return map.get(key).val;
}
```

```java
public void put(int key, int val) {
    if (map.containsKey(key)) {
        // 删除旧的数据
        deleteKey(key);
        // 新插入的数据为最近使用的数据
        addRecently(key, val);
        return;
    }
    
    if (cap == cache.size()) {
        // 删除最久未使用的元素
        removeLeastRecently();
    }
    // 添加为最近使用的元素
    addRecently(key, val);
}
```

#### 1.2 用 Java 的内置类型 `LinkedHashMap` 来实现 LRU 算法


```java
class LRUCache {
    int cap;
    LinkedHashMap<Integer, Integer> cache = new LinkedHashMap<>();
    public LRUCache(int capacity) { 
        this.cap = capacity;
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }
        // 将 key 变为最近使用
        makeRecently(key);
        return cache.get(key);
    }
    
    public void put(int key, int val) {
        if (cache.containsKey(key)) {
            // 修改 key 的值
            cache.put(key, val);
            // 将 key 变为最近使用
            makeRecently(key);
            return;
        }
        
        if (cache.size() >= this.cap) {
            // 链表头部就是最久未使用的 key
            int oldestKey = cache.keySet().iterator().next();
            cache.remove(oldestKey);
        }
        // 将新的 key 添加链表尾部
        cache.put(key, val);
    }
    
    private void makeRecently(int key) {
        int val = cache.get(key);
        // 删除 key，重新插入到队尾
        cache.remove(key);
        cache.put(key, val);
    }
}
```

#### 1.3 其他语言实现

[146.LRU缓存机制](https://leetcode-cn.com/problems/lru-cache/)

**c++**

[gowufang](https://github.com/gowufang)提供第146题C++代码：
```cpp
class LRUCache {
        public:
        struct node {
            int val;
            int key;
            node* pre;//当前节点的前一个节点
            node* next;//当前节点的后一个节点
            node(){}
            node(int key, int val):key(key), val(val), pre(NULL), next(NULL){}
        };

        LRUCache(int size) {
            this->size = size;
            head = new node();
            tail = new node();
            head->next = tail;
            tail->pre = head;
        }


        void movetohead(node* cur)//相当于一个insert操作，在head 和 head的next之间插入一个节点
        {
            node* next = head->next;//head的next先保存起来
            head->next = cur;//将当前节点移动到head的后面
            cur->pre = head;//当前节点cur的pre指向head
            next->pre = cur;
            cur->next = next;
        }

        node* deletecurrentnode(node* cur)//移除当前节点
        {
            cur->pre->next = cur->next;
            cur->next->pre = cur->pre;
            return cur;
        }
        void makerecently(node* cur)
        {
            node* temp = deletecurrentnode(cur);// 删除 cur，要重新插入到对头
            movetohead(temp);//cur放到队头去
        }
        int get(int key)
        {
            int ret = -1;
            if ( map.count(key))
            {
                node* temp = map[key];
                makerecently(temp);// 将 key 变为最近使用
                ret = temp->val;
            }
            return ret;
        }

        void put(int key, int value) {
            if ( map.count(key))
            {
                // 修改 key 的值
                node* temp = map[key];
                temp->val = value;
                // 将 key 变为最近使用
                makerecently(temp);
            }
            else
            {
                node* cur = new node(key, value);
                if( map.size()== size )
                {
                    // 链表头部就是最久未使用的 key
                    node *temp = deletecurrentnode(tail->pre);
                    map.erase(temp->key);
                }
                movetohead(cur);
                map[key] = cur;

            }
        
        }

        unordered_map<int, node*> map;
        int size;
        node* head, *tail;

    };
```



**python**

```python
"""
所谓LRU缓存，根本的难点在于记录最久被使用的键值对，这就设计到排序的问题，
在python中，天生具备排序功能的字典就是OrderDict。
注意到，记录最久未被使用的键值对的充要条件是将每一次put/get的键值对都定义为
最近访问，那么最久未被使用的键值对自然就会排到最后。
如果你深入python OrderDict的底层实现，就会知道它的本质是个双向链表+字典。
它内置支持了
1. move_to_end来重排链表顺序，它可以让我们将最近访问的键值对放到最后面
2. popitem来弹出键值对，它既可以弹出最近的，也可以弹出最远的，弹出最远的就是我们要的操作。
"""
from collections import OrderedDict
class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity  # cache的容量
    self.visited = OrderedDict()  # python内置的OrderDict具备排序的功能
    
  def get(self, key: int) -> int:
    if key not in self.visited:
      return -1
    self.visited.move_to_end(key)  # 最近访问的放到链表最后，维护好顺序
    return self.visited[key]

  def put(self, key: int, value: int) -> None:
    if key not in self.visited and len(self.visited) == self.capacity:
      # last=False时，按照FIFO顺序弹出键值对
      # 因为我们将最近访问的放到最后，所以最远访问的就是最前的，也就是最first的，故要用FIFO顺序
      self.visited.popitem(last=False)
      self.visited[key]=value
      self.visited.move_to_end(key)    # 最近访问的放到链表最后，维护好顺序


```

### 2 如何高效寻找素数

#### 2.1 设计

```java
int countPrimes(int n) {
    boolean[] isPrim = new boolean[n];
    Arrays.fill(isPrim, true);
    for (int i = 2; i * i < n; i++) 
        if (isPrim[i]) 
            for (int j = i * i; j < n; j += i) 
                isPrim[j] = false;
    
    int count = 0;
    for (int i = 2; i < n; i++)
        if (isPrim[i]) count++;
    
    return count;
}
```




#### 2.2 其他实现

**C++实现**

[204.计数质数](https://leetcode-cn.com/problems/count-primes)

统计所有小于非负整数 n 的质数的数量。

 

	示例 1：

	输入：n = 10
	输出：4
	解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。


	采用的算法是埃拉托斯特尼筛法
	埃拉托斯特尼筛法的具体内容就是：**要得到自然数n以内的全部素数，必须把不大于根号n的所有素数的倍数剔除，剩下的就是素数。**
	同时考虑到大于2的偶数都不是素数，所以可以进一步优化成：**要得到自然数n以内的全部素数，必须把不大于根号n的所有素数的奇数倍剔除，剩下的奇数就是素数。**
	此算法其实就是上面的Java解法所采用的。

这里提供C++的代码：
```C++
class Solution {
  public:
  int countPrimes(int n) {
    int res = 0;
    bool prime[n+1];
    for(int i = 0; i < n; ++i)
      prime[i] = true;

    for(int i = 2; i <= sqrt(n); ++i)   //计数过程 
    {                                   //外循环优化，因为判断一个数是否为质数只需要整除到sqrt(n)，反推亦然
      if(prime[i])
      {
        for(int j = i * i; j < n; j += i)   //内循环优化，i*i之前的比如i*2，i*3等，在之前的循环中已经验证了
        {
          prime[j] = false;
        }
      }      
    }
    for (int i = 2; i < n; ++i)
      if (prime[i])  res++;     //最后遍历统计一遍，存入res

    return res;    
  }
};
```

### 3 二分查找应用

[875.爱吃香蕉的珂珂](https://leetcode-cn.com/problems/koko-eating-bananas)

珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。


	示例 1：

	输入: piles = [3,6,7,11], H = 8
	输出: 4


[1011.在D天内送达包裹的能力](https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days)

传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

示例 2：

输入：weights = [3,2,2,4,1,4], D = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4

 

#### 3.1  koko偷香蕉

珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

示例 1：

输入: piles = [3,6,7,11], H = 8

输出: 4

```java
int minEatingSpeed(int[] piles, int H) {
    // 套用搜索左侧边界的算法框架
    int left = 1, right = getMax(piles) + 1;
    while (left < right) {
        // 防止溢出
        int mid = left + (right - left) / 2;
        if (canFinish(piles, mid, H)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}

```java
// 时间复杂度 O(N)
boolean canFinish(int[] piles, int speed, int H) {
    int time = 0;
    for (int n : piles) {
        time += timeOf(n, speed);
    }
    return time <= H;
}

int timeOf(int n, int speed) {
    return (n / speed) + ((n % speed > 0) ? 1 : 0);
}

int getMax(int[] piles) {
    int max = 0;
    for (int n : piles)
        max = Math.max(n, max);
    return max;
}
```


#### 3.2 运输问题：

要在 `D` 天内运输完所有货物，货物不可分割，如何确定运输的最小载重呢（下文称为 `cap`）？

其实本质上和 Koko 吃香蕉的问题一样的，首先确定 `cap` 的最小值和最大值分别为 `max(weights)` 和 `sum(weights)`。

我们要求**最小载重**，所以可以用搜索左侧边界的二分查找算法优化线性搜索：

```java
// 寻找左侧边界的二分查找
int shipWithinDays(int[] weights, int D) {
	// 载重可能的最小值
    int left = getMax(weights);
	// 载重可能的最大值 + 1
    int right = getSum(weights) + 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (canFinish(weights, D, mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}

// 如果载重为 cap，是否能在 D 天内运完货物？
boolean canFinish(int[] w, int D, int cap) {
    int i = 0;
    for (int day = 0; day < D; day++) {
        int maxCap = cap;
        while ((maxCap -= w[i]) >= 0) {
            i++;
            if (i == w.length)
                return true;
        }
    }
    return false;
}
```

#### 3.3 其他语言实现

**c++**

[cchroot](https://github.com/cchroot) 提供 C++ 代码：

```c++
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int H) {
        // 二分法查找最小速度
        // 初始化最小速度为 1，最大速度为题目设定的最大值 10^9
        // 这里也可以遍历 piles 数组，获取数组中的最大值，设置 right 为数组中的最大值即可(因为每堆香蕉1小时吃完是最快的)
        // log2(10^9) 约等于30，次数不多，所以这里暂时就不采取遍历获取最大值了
        int left = 1, right = pow(10, 9);
        while (left < right) { // 二分法基本的防止溢出
            int mid = left + (right - left) / 2;
            // 以 mid 的速度吃香蕉，是否能在 H 小时内吃完香蕉
            if (!canFinish(piles, mid, H))
                left = mid + 1;
            else
                right = mid;
        }
        return left;
    }

    // 以 speed 的速度是否能把香蕉吃完
    bool canFinish(vector<int>& piles, int speed, int H) {
        int time = 0;
        // 遍历累加时间 time
        for (int p: piles)
            time += (p - 1) / speed + 1;
        return time <= H; // time 小于等于 H 说明能在 H 小时吃完返回 true, 否则返回 false
    }
};
```

**python**

[tonytang731](https://https://github.com/tonytang731) 提供 Python3 代码：

```python
import math

class Solution:
    def minEatingSpeed(self, piles, H):
        # 初始化起点和终点， 最快的速度可以一次拿完最大的一堆
        start = 1
        end = max(piles)
        
        # while loop进行二分查找
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            # 如果中点所需时间大于H, 我们需要加速， 将起点设为中点
            if self.timeH(piles, mid) > H:
                start = mid
            # 如果中点所需时间小于H, 我们需要减速， 将终点设为中点
            else:
                end = mid
                
        # 提交前确认起点是否满足条件，我们要尽量慢拿
        if self.timeH(piles, start) <= H:
            return start
        
        # 若起点不符合， 则中点是答案
        return end
            
        
        
    def timeH(self, piles, K):
        # 初始化时间
        H = 0
        
        #求拿每一堆需要多长时间
        for pile in piles:
            H += math.ceil(pile / K)
            
        return H
```


### 4 如何高效解决接雨水问题

[42.接雨水](https://leetcode-cn.com/problems/trapping-rain-water)

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
 
#### 4.1 暴力

```cpp
int trap(vector<int>& height) {
    int n = height.size();
    int res = 0;
    for (int i = 1; i < n - 1; i++) {
        int l_max = 0, r_max = 0;
        // 找右边最高的柱子
        for (int j = i; j < n; j++)
            r_max = max(r_max, height[j]);
        // 找左边最高的柱子
        for (int j = i; j >= 0; j--)
            l_max = max(l_max, height[j]);
        // 如果自己就是最高的话，
        // l_max == r_max == height[i]
        res += min(l_max, r_max) - height[i];
    }
    return res;
}
```


#### 4.2 备忘录优化


```cpp
int trap(vector<int>& height) {
    if (height.empty()) return 0;
    int n = height.size();
    int res = 0;
    // 数组充当备忘录
    vector<int> l_max(n), r_max(n);
    // 初始化 base case
    l_max[0] = height[0];
    r_max[n - 1] = height[n - 1];
    // 从左向右计算 l_max
    for (int i = 1; i < n; i++)
        l_max[i] = max(height[i], l_max[i - 1]);
    // 从右向左计算 r_max
    for (int i = n - 2; i >= 0; i--) 
        r_max[i] = max(height[i], r_max[i + 1]);
    // 计算答案
    for (int i = 1; i < n - 1; i++) 
        res += min(l_max[i], r_max[i]) - height[i];
    return res;
}
```

#### 4.3 双指针解法

```cpp
int trap(vector<int>& height) {
    if (height.empty()) return 0;
    int n = height.size();
    int left = 0, right = n - 1;
    int res = 0;
    
    int l_max = height[0];
    int r_max = height[n - 1];
    
    while (left <= right) {
        l_max = max(l_max, height[left]);
        r_max = max(r_max, height[right]);
        
        // res += min(l_max, r_max) - height[i]
        if (l_max < r_max) {
            res += l_max - height[left];
            left++; 
        } else {
            res += r_max - height[right];
            right--;
        }
    }
    return res;
}
```

#### 4.4 其他语言


[Yifan Zhang](https://github.com/FanFan0919) 提供 java 代码

**双指针解法**：时间复杂度 O(N)，空间复杂度 O(1)

对cpp版本的解法有非常微小的优化。  
因为我们每次循环只会选 left 或者 right 处的柱子来计算，因此我们并不需要在每次循环中同时更新`maxLeft`和`maxRight`。  
我们可以先比较 `maxLeft` 和 `maxRight`，决定这次选择计算的柱子是 `height[left]` 或者 `height[right]` 后再更新对应的 `maxLeft` 或 `maxRight`。  
当然这并不会在时间上带来什么优化，只是提供一种思路。

```java
class Solution {
    public int trap(int[] height) {
        if (height == null || height.length == 0) return 0;
        int left = 0, right = height.length - 1;
        int maxLeft = height[left], maxRight = height[right];
        int res = 0;
        
        while (left < right) {
            // 比较 maxLeft 和 maxRight，决定这次计算 left 还是 right 处的柱子
            if (maxLeft < maxRight) {
                left++;
                maxLeft = Math.max(maxLeft, height[left]);  // update maxLeft
                res += maxLeft - height[left];
            } else {
                right--;
                maxRight = Math.max(maxRight, height[right]);   // update maxRight
                res += maxRight - height[right];
            }
        }
        
        return res;
    }
}
```


### 5 如何去除有序数组的重复元素

#### 5.1 描述

**对于数组相关的算法问题，有一个通用的技巧：要尽量避免在中间删除元素，那我就先想办法把这个元素换到最后去**。这样的话，最终待删除的元素都拖在数组尾部，一个一个 pop 掉就行了，每次操作的时间复杂度也就降低到 O(1) 了。

**双指针**

我们让慢指针 `slow` 走左后面，快指针 `fast` 走在前面探路，找到一个不重复的元素就告诉 `slow` 并让 `slow` 前进一步。这样当 `fast` 指针遍历完整个数组 `nums` 后，**`nums[0..slow]` 就是不重复元素，之后的所有元素都是重复元素**。

```java
int removeDuplicates(int[] nums) {
    int n = nums.length;
    if (n == 0) return 0;
    int slow = 0, fast = 1;
    while (fast < n) {
        if (nums[fast] != nums[slow]) {
            slow++;
            // 维护 nums[0..slow] 无重复
            nums[slow] = nums[fast];
        }
        fast++;
    }
    // 长度为索引 + 1
    return slow + 1;
}
```

**一个有序链表去重**

```java
ListNode deleteDuplicates(ListNode head) {
    if (head == null) return null;
    ListNode slow = head, fast = head.next;
    while (fast != null) {
        if (fast.val != slow.val) {
            // nums[slow] = nums[fast];
            slow.next = fast;
            // slow++;
            slow = slow.next;
        }
        // fast++
        fast = fast.next;
    }
    // 断开与后面重复元素的连接
    slow.next = null;
    return head;
}
```


##### 5.2 python实现

[eric wang](https://www.github.com/eric496) 提供有序数组 Python3 代码 

```python
def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    
    if n == 0:
        return 0
    
    slow, fast = 0, 1
    
    while fast < n:
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
            
        fast += 1
        
    return slow + 1
```

[eric wang](https://www.github.com/eric496) 提供有序链表 Python3 代码 

```python
def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head:
        return head
    
    slow, fast = head, head.next
    
    while fast:
        if fast.val != slow.val:
            slow.next = fast
            slow = slow.next
            
        fast = fast.next

    # 断开与后面重复元素的连接   
    slow.next = None
    return head
```

### 6 如何寻找最长回文子串

[5.最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring)

给你一个字符串 s，找到 s 中最长的回文子串。

	示例 1：

	输入：s = "babad"
	输出："bab"
	解释："aba" 同样是符合题意的答案。



下面，就来说一下正确的思路，如何使用双指针。

**寻找回文串的问题核心思想是：从中间开始向两边扩散来判断回文串**。对于最长回文子串，就是这个意思：

```python
for 0 <= i < len(s):
    找到以 s[i] 为中心的回文串
    更新答案
```

但是呢，我们刚才也说了，回文串的长度可能是奇数也可能是偶数，如果是 `abba`这种情况，没有一个中心字符，上面的算法就没辙了。所以我们可以修改一下：

```python
for 0 <= i < len(s):
    找到以 s[i] 为中心的回文串
    找到以 s[i] 和 s[i+1] 为中心的回文串
    更新答案
```

#### 6.1 实现

要传入两个指针 `l` 和 `r` 呢？**因为这样实现可以同时处理回文串长度为奇数和偶数的情况**：

```python
for 0 <= i < len(s):
    # 找到以 s[i] 为中心的回文串
    palindrome(s, i, i)
    # 找到以 s[i] 和 s[i+1] 为中心的回文串
    palindrome(s, i, i + 1)
    更新答案
```

下面看下 `longestPalindrome` 的完整代码：

```cpp
string longestPalindrome(string s) {
    string res;
    for (int i = 0; i < s.size(); i++) {
        // 以 s[i] 为中心的最长回文子串
        string s1 = palindrome(s, i, i);
        // 以 s[i] 和 s[i+1] 为中心的最长回文子串
        string s2 = palindrome(s, i, i + 1);
        // res = longest(res, s1, s2)
        res = res.size() > s1.size() ? res : s1;
        res = res.size() > s2.size() ? res : s2;
    }
    return res;
}
```

#### 6.2 其他语言实现

[5.最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring)

**java**

[cchromt](https://github.com/cchroot) 提供 Java 代码：

```java
// 中心扩展算法
class Solution {
    public String longestPalindrome(String s) {
        // 如果字符串长度小于2，则直接返回其本身
        if (s.length() < 2) {
            return s;
        }
        String res = "";
        for (int i = 0; i < s.length() - 1; i++) {
            // 以 s.charAt(i) 为中心的最长回文子串
            String s1 = palindrome(s, i, i);
            // 以 s.charAt(i) 和 s.charAt(i+1) 为中心的最长回文子串
            String s2 = palindrome(s, i, i + 1);
            res = res.length() > s1.length() ? res : s1;
            res = res.length() > s2.length() ? res : s2;
        }
        return res;
    }

    public String palindrome(String s, int left, int right) {
        // 索引未越界的情况下，s.charAt(left) == s.charAt(right) 则继续向两边拓展
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        // 这里要注意，跳出 while 循环时，恰好满足 s.charAt(i) != s.charAt(j)，因此截取的的字符串为[left+1, right-1]
        return s.substring(left + 1, right);
    }
}
```


[enrilwang](https://github.com/enrilwang) 提供 Python 代码：

```python
# 中心扩展算法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #用n来装字符串长度，res来装答案
        n = len(s)  
        res = str()
        #字符串长度小于2，就返回本身
        if n < 2: return s
        for i in range(n-1):
            #oddstr是以i为中心的最长回文子串
            oddstr = self.centerExtend(s,i,i)
            #evenstr是以i和i+1为中心的最长回文子串
            evenstr = self.centerExtend(s,i,i+1)
            temp = oddstr if len(oddstr)>len(evenstr) else evenstr
            if len(temp)>len(res):res=temp
        
        return res

    def centerExtend(self,s:str,left,right)->str:
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        #这里要注意，跳出while循环时，恰好s[left] != s[right]
        return s[left+1:right]


```


### 7  如何k个一组反转链表

25.K个一组翻转链表

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：

你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。


#### 7.1 实现

```java
ListNode reverseKGroup(ListNode head, int k) {
    if (head == null) return null;
    // 区间 [a, b) 包含 k 个待反转元素
    ListNode a, b;
    a = b = head;
    for (int i = 0; i < k; i++) {
        // 不足 k 个，不需要反转，base case
        if (b == null) return head;
        b = b.next;
    }
    // 反转前 k 个元素
    ListNode newHead = reverse(a, b);
    // 递归反转后续链表并连接起来
    a.next = reverseKGroup(b, k);
    return newHead;
}
```


### 8 如何判定括号合法性

题目很简单，输入一个字符串，其中包含 [](){} 六种括号，请你判断这个字符串组成的括号是否合法。

Input: "()[]{}"
Output: true

Input: "([)]"
Output: false

Input: "{[]}"
Output: true

#### 8.1 实现

栈是一种先进后出的数据结构，处理括号问题的时候尤其有用。

我们这道题就用一个名为 `left` 的栈代替之前思路中的 `left` 变量，**遇到左括号就入栈，遇到右括号就去栈中寻找最近的左括号，看是否匹配**。

```cpp
bool isValid(string str) {
    stack<char> left;
    for (char c : str) {
        if (c == '(' || c == '{' || c == '[')
            left.push(c);
        else // 字符 c 是右括号
            if (!left.empty() && leftOf(c) == left.top())
                left.pop();
            else
                // 和最近的左括号不匹配
                return false;
    }
    // 是否所有的左括号都被匹配了
    return left.empty();
}

char leftOf(char c) {
    if (c == '}') return '{';
    if (c == ')') return '(';
    return '[';
}
```

#### 8.2 其他语言实现

[20.有效的括号](https://leetcode-cn.com/problems/valid-parentheses)

**python**

```python
def isValid(self, s: str) -> bool:
    left = []
    leftOf = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for c in s:
        if c in '([{':
            left.append(c)
        elif left and leftOf[c]==left[-1]: # 右括号 + left不为空 + 和最近左括号能匹配
            left.pop()
        else: # 右括号 + （left为空 / 和堆顶括号不匹配）
            return False
        
    # left中所有左括号都被匹配则return True 反之False
    return not left
```



**java**

```java
//基本思想：每次遇到左括号时都将相对应的右括号'）'，']'或'}'推入堆栈
//如果在字符串中出现右括号，则需要检查堆栈是否为空，以及顶部元素是否与该右括号相同。如果不是，则该字符串无效。
//最后，我们还需要检查堆栈是否为空
public boolean isValid(String s) {
  Deque<Character> stack = new ArrayDeque<>();
  for(char c : s.toCharArray()){
    //是左括号就将相对应的右括号入栈
    if(c=='(') {
      stack.offerLast(')');
    }else if(c=='{'){
      stack.offerLast('}');
    }else if(c=='['){
      stack.offerLast(']');   
    }else if(stack.isEmpty() || stack.pollLast()!=c){//出现右括号，检查堆栈是否为空，以及顶部元素是否与该右括号相同
      return false;
    }
  }
  return stack.isEmpty();
}


```

### 9 如何寻找消失的元素

448. 找到所有数组中消失的数字

给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]


#### 9.1 实现

刚才我们的思路是把两个和都加出来然后相减，为了避免溢出，干脆一边求和一边减算了。很类似刚才位运算解法的思路，仍然假设 `nums = [0,3,1,4]`，先补一位索引再让元素跟索引配对：


我们让每个索引减去其对应的元素，再把相减的结果加起来，不就是那个缺失的元素吗？

```java
public int missingNumber(int[] nums) {
    int n = nums.length;
    int res = 0;
    // 新补的索引
    res += n - 0;
    // 剩下索引和元素的差加起来
    for (int i = 0; i < n; i++) 
        res += i - nums[i];
    return res;
}
```

#### 9.1 其他语言实现

**python**

```python
def missingNumber(self, nums: List[int]) -> int:
    #思路1，位运算
    res = len(nums)
    for i,num in enumerate(nums):
        res ^= i^num
        return res
```

```python
def missingNumber(self, nums: List[int]) -> int:
    #思路2，求和
    n = len(nums)
    return n*(n+1)//2-sum(nums)
```

```python
def missingNumber(self, nums: List[int]) -> int:
    #思路3，防止整形溢出的优化
    res = len(nums)
    for i,num in enumerate(nums):
        res+=i-num
        return res
```

事实上，在python3中不存在整数溢出的问题（只要内存放得下），思路3的优化提升并不大，不过看上去有内味了哈...

**c++**

[happy-yuxuan](https://github.com/happy-yuxuan) 提供 三种方法的 C++ 代码：

```c++
// 方法：异或元素和索引
int missingNumber(vector<int>& nums) {
    int n = nums.size();
    int res = 0;
    // 先和新补的索引异或一下
    res ^= n;
    // 和其他的元素、索引做异或
    for (int i = 0; i < n; i++)
        res ^= i ^ nums[i];
    return res;
}
```

```c++
// 方法：等差数列求和
int missingNumber(vector<int>& nums) {
    int n = nums.size();
    // 公式：(首项 + 末项) * 项数 / 2
    int expect = (0 + n) * (n + 1) / 2;
    int sum = 0;
    for (int x : nums) 
        sum += x;
    return expect - sum;
}
```

```c++
// 方法：防止整型溢出
int missingNumber(vector<int>& nums) {
    int n = nums.size();
    int res = 0;
    // 新补的索引
    res += n - 0;
    // 剩下索引和元素的差加起来
    for (int i = 0; i < n; i++) 
        res += i - nums[i];
    return res;
}
```


### 10 如何寻找缺失和重复的元素

[645.错误的集合](https://leetcode-cn.com/problems/set-mismatch)


给一个长度为 N 的数组 nums，其中本来装着 [1..N] 这 N 个元素，无序。但是现在出现了一些错误，nums 中的一个元素出现了重复，也就同时导致了另一个元素的缺失。请你写一个算法，找到 nums 中的重复元素和缺失元素的值。

	// 返回两个数字，分别是 {dup, missing}
	vector<int> findErrorNums(vector<int>& nums);
	
比如说输入：nums = [1,2,2,4]，算法返回 [2,3]。

对于这种数组问题，**关键点在于元素和索引是成对儿出现的，常用的方法是排序、异或、映射**。

映射的思路就是我们刚才的分析，将每个索引和元素映射起来，通过正负号记录某个元素是否被映射。

排序的方法也很好理解，对于这个问题，可以想象如果元素都被从小到大排序，如果发现索引对应的元素如果不相符，就可以找到重复和缺失的元素。

异或运算也是常用的，因为异或性质 `a ^ a = 0, a ^ 0 = a`，如果将索引和元素同时异或，就可以消除成对儿的索引和元素，留下的就是重复或者缺失的元素。可以看看前文「寻找缺失元素」，介绍过这种方法。


#### 10.1 实现

```cpp
vector<int> findErrorNums(vector<int>& nums) {
    int n = nums.size();
    int dup = -1;
    for (int i = 0; i < n; i++) {
        // 现在的元素是从 1 开始的
        int index = abs(nums[i]) - 1;
        if (nums[index] < 0)
            dup = abs(nums[i]);
        else
            nums[index] *= -1;
    }

    int missing = -1;
    for (int i = 0; i < n; i++)
        if (nums[i] > 0)
            // 将索引转换成元素
            missing = i + 1;
    
    return {dup, missing};
}
```

#### 10.2 其他实现

[zhuli](https://github.com/1097452462 "zhuli")提供的Java代码：
```java
class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        int dup = -1;
        for (int i = 0; i < n; i++) {
	    // 元素是从 1 开始的
            int index = Math.abs(nums[i]) - 1;
            // nums[index] 小于 0 则说明重复访问
            if (nums[index] < 0)
                dup = Math.abs(nums[i]);
            else
                nums[index] *= -1;
        }
        int missing = -1;
        for (int i = 0; i < n; i++)
            // nums[i] 大于 0 则说明没有访问
            if (nums[i] > 0)
		// 将索引转换成元素
                missing = i + 1;
        return new int[]{dup, missing};
    }
}
```




### 11 如何判断回文链表

234.回文链表

请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true

**寻找**回文串的核心思想是从中心向两端扩展：

```cpp
string palindrome(string& s, int l, int r) {
    // 防止索引越界
    while (l >= 0 && r < s.size()
            && s[l] == s[r]) {
        // 向两边展开
        l--; r++;
    }
    // 返回以 s[l] 和 s[r] 为中心的最长回文串
    return s.substr(l + 1, r - l - 1);
}
```

因为回文串长度可能为奇数也可能是偶数，长度为奇数时只存在一个中心点，而长度为偶数时存在两个中心点，所以上面这个函数需要传入`l`和`r`。

而**判断**一个字符串是不是回文串就简单很多，不需要考虑奇偶情况，只需要「双指针技巧」，从两端向中间逼近即可：

```cpp
bool isPalindrome(string s) {
    int left = 0, right = s.length - 1;
    while (left < right) {
        if (s[left] != s[right])
            return false;
        left++; right--;
    }
    return true;
}
```

#### 11.1 实现

**判断回文单链表**

模仿双指针实现回文判断的功能：

```java
// 左侧指针
ListNode left;

boolean isPalindrome(ListNode head) {
    left = head;
    return traverse(head);
}

boolean traverse(ListNode right) {
    if (right == null) return true;
    boolean res = traverse(right.next);
    // 后序遍历代码
    res = res && (right.val == left.val);
    left = left.next;
    return res;
}
```

**实际上就是把链表节点放入一个栈，然后再拿出来，这时候元素顺序就是反的**

**优化空间复杂度**

更好的思路是这样的：

**1、先通过「双指针技巧」中的快慢指针来找到链表的中点**：

```java
ListNode slow, fast;
slow = fast = head;
while (fast != null && fast.next != null) {
    slow = slow.next;
    fast = fast.next.next;
}
// slow 指针现在指向链表中点
```



**2、如果`fast`指针没有指向`null`，说明链表长度为奇数，`slow`还要再前进一步**：

```java
if (fast != null)
    slow = slow.next;
```

![](../pictures/回文链表/2.jpg)

**3、从`slow`开始反转后面的链表，现在就可以开始比较回文串了**：

```java
ListNode left = head;
ListNode right = reverse(slow);

while (right != null) {
    if (left.val != right.val)
        return false;
    left = left.next;
    right = right.next;
}
return true;
```

#### 11.2 其他语言实现

**C++**

```cpp
bool isPalindrome(ListNode* head) {
  if (head == nullptr || head->next == nullptr) //为空或者只有一个节点时，直接判断为true
    return true;
  ListNode* slow = head, * fast = head;
  while (fast != nullptr) {//首先找到中间节点
    slow = slow->next;
    fast = fast->next == nullptr? fast->next:fast->next->next; //因为链表长度可能是奇数或偶数，所以需要进行判断
  }

  ListNode* temp = nullptr,* pre = nullptr;//pre始终保持后续链表的头部，temp节点则作为中间零时替换的节点
  while (slow != nullptr) {//利用头插法，将当前节点与后续链表断链处理，反转后半部分的链表
    temp = slow->next;
    slow->next = pre;//建立连接
    pre = slow;//pre始终作为后续链表的头部
    slow = temp;
  }

  while (head !=nullptr && pre != nullptr) {//同步进行比较
    if (head->val != pre->val) {//值有不一样的，说明不是回文联表，直接返回false了
      return false;
    }
    head = head->next;//head向下走，直到走到空
    pre = pre->next;//pre节点也向下走，直到走到空
  }
  return true;//到此说明当前链表是回文链表返回true即可
}

```


### 12 如何在无限序列中随机抽取元素

随机算法之水塘抽样算法

给你一个**未知长度**的链表，请你设计一个算法，**只能遍历一次**，随机地返回链表中的一个节点。

这里说的随机是均匀随机（uniform random），也就是说，如果有 `n` 个元素，每个元素被选中的概率都是 `1/n`，不可以有统计意义上的偏差。

#### 12.1 实现

**先解决只抽取一个元素的问题**，这个问题的难点在于，随机选择是「动态」的，比如说你现在你有 5 个元素，你已经随机选取了其中的某个元素 `a` 作为结果，但是现在再给你一个新元素 `b`，你应该留着 `a` 还是将 `b` 作为结果呢，以什么逻辑选择 `a` 和 `b` 呢，怎么证明你的选择方法在概率上是公平的呢？

**先说结论，当你遇到第 `i` 个元素时，应该有 `1/i` 的概率选择该元素，`1 - 1/i` 的概率保持原有的选择**。看代码容易理解这个思路：

```java
/* 返回链表中一个随机节点的值 */
int getRandom(ListNode head) {
    Random r = new Random();
    int i = 0, res = 0;
    ListNode p = head;
    // while 循环遍历链表
    while (p != null) {
        // 生成一个 [0, i) 之间的整数
        // 这个整数等于 0 的概率就是 1/i
        if (r.nextInt(++i) == 0) {
            res = p.val;
        }
        p = p.next;
    }
    return res;
}
```


### 13 座位调度

[855.考场就座](https://leetcode-cn.com/problems/exam-room)

假设有一个考场，考场有一排共 `N` 个座位，索引分别是 `[0..N-1]`，考生会**陆续**进入考场考试，并且可能在**任何时候**离开考场。

你作为考官，要安排考生们的座位，满足：**每当一个学生进入时，你需要最大化他和最近其他人的距离；如果有多个这样的座位，安排到他到索引最小的那个座位**

也就是请你实现下面这样一个类：

```java
class ExamRoom {
    // 构造函数，传入座位总数 N
    public ExamRoom(int N);
    // 来了一名考生，返回你给他分配的座位
    public int seat();
    // 坐在 p 位置的考生离开了
    // 可以认为 p 位置一定坐有考生
    public void leave(int p);
}
```

比方说考场有 5 个座位，分别是 `[0..4]`：

第一名考生进入时（调用 `seat()`），坐在任何位置都行，但是要给他安排索引最小的位置，也就是返回位置 0。

第二名学生进入时（再调用 `seat()`），要和旁边的人距离最远，也就是返回位置 4。

第三名学生进入时，要和旁边的人距离最远，应该做到中间，也就是座位 2。

如果再进一名学生，他可以坐在座位 1 或者 3，取较小的索引 1。

#### 13.1 实现

这个问题还用到一个常用的编程技巧，就是使用一个「虚拟线段」让算法正确启动，这就和链表相关的算法需要「虚拟头结点」一个道理。

```java
// 将端点 p 映射到以 p 为左端点的线段
private Map<Integer, int[]> startMap;
// 将端点 p 映射到以 p 为右端点的线段
private Map<Integer, int[]> endMap;
// 根据线段长度从小到大存放所有线段
private TreeSet<int[]> pq;
private int N;

public ExamRoom(int N) {
    this.N = N;
    startMap = new HashMap<>();
    endMap = new HashMap<>();
    pq = new TreeSet<>((a, b) -> {
        // 算出两个线段的长度
        int distA = distance(a);
        int distB = distance(b);
        // 长度更长的更大，排后面
        return distA - distB;
    });
    // 在有序集合中先放一个虚拟线段
    addInterval(new int[] {-1, N});
}

/* 去除一个线段 */
private void removeInterval(int[] intv) {
    pq.remove(intv);
    startMap.remove(intv[0]);
    endMap.remove(intv[1]);
}

/* 增加一个线段 */
private void addInterval(int[] intv) {
    pq.add(intv);
    startMap.put(intv[0], intv);
    endMap.put(intv[1], intv);
}

/* 计算一个线段的长度 */
private int distance(int[] intv) {
    return intv[1] - intv[0] - 1;
}
```

「虚拟线段」其实就是为了将所有座位表示为一个线段：


```java
public int seat() {
    // 从有序集合拿出最长的线段
    int[] longest = pq.last();
    int x = longest[0];
    int y = longest[1];
    int seat;
    if (x == -1) { // 情况一
        seat = 0;
    } else if (y == N) { // 情况二
        seat = N - 1;
    } else { // 情况三
        seat = (y - x) / 2 + x;
    }
    // 将最长的线段分成两段
    int[] left = new int[] {x, seat};
    int[] right = new int[] {seat, y};
    removeInterval(longest);
    addInterval(left);
    addInterval(right);
    return seat;
}

public void leave(int p) {
    // 将 p 左右的线段找出来
    int[] right = startMap.get(p);
    int[] left = endMap.get(p);
    // 合并两个线段成为一个线段
    int[] merged = new int[] {left[0], right[1]};
    removeInterval(left);
    removeInterval(right);
    addInterval(merged);
}
```

### 14 Union-Find算法详解

```java
class UF {
    // 连通分量个数
    private int count;
    // 存储一棵树
    private int[] parent;
    // 记录树的“重量”
    private int[] size;

    public UF(int n) {
        this.count = n;
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }
    
    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        if (rootP == rootQ)
            return;
        
        // 小树接到大树下面，较平衡
        if (size[rootP] > size[rootQ]) {
            parent[rootQ] = rootP;
            size[rootP] += size[rootQ];
        } else {
            parent[rootP] = rootQ;
            size[rootQ] += size[rootP];
        }
        count--;
    }

    public boolean connected(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        return rootP == rootQ;
    }

    private int find(int x) {
        while (parent[x] != x) {
            // 进行路径压缩
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public int count() {
        return count;
    }
}
```
Union-Find 算法的复杂度可以这样分析：构造函数初始化数据结构需要 O(N) 的时间和空间复杂度；连通两个节点`union`、判断两个节点的连通性`connected`、计算连通分量`count`所需的时间复杂度均为 O(1)。

### 15 Union-Find算法应用

算法的关键点有 3 个：

1、用 `parent` 数组记录每个节点的父节点，相当于指向父节点的指针，所以 `parent` 数组内实际存储着一个森林（若干棵多叉树）。

2、用 `size` 数组记录着每棵树的重量，目的是让 `union` 后树依然拥有平衡性，而不会退化成链表，影响操作效率。

3、在 `find` 函数中进行路径压缩，保证任意树的高度保持在常数，使得 `union` 和 `connected` API 时间复杂度为 O(1)。

有的读者问，**既然有了路径压缩，`size` 数组的重量平衡还需要吗**？这个问题很有意思，因为路径压缩保证了树高为常数（不超过 3），那么树就算不平衡，高度也是常数，基本没什么影响。

我认为，论时间复杂度的话，确实，不需要重量平衡也是 O(1)。但是如果加上 `size` 数组辅助，效率还是略微高一些，比如下面这种情况：

#### 15.1 DFS 的替代方案

很多使用 DFS 深度优先算法解决的问题，也可以用 Union-Find 算法解决。

比如第 130 题，被围绕的区域：给你一个 M×N 的二维矩阵，其中包含字符 `X` 和 `O`，让你找到矩阵中**四面**被 `X` 围住的 `O`，并且把它们替换成 `X`。

```java
void solve(char[][] board);
```

注意哦，必须是四面被围的 `O` 才能被换成 `X`，也就是说边角上的 `O` 一定不会被围，进一步，与边角上的 `O` 相连的 `O` 也不会被 `X` 围四面，也不会被替换。



#### 15.2 判定合法等式

给你一个数组 `equations`，装着若干字符串表示的算式。每个算式 `equations[i]` 长度都是 4，而且只有这两种情况：`a==b` 或者 `a!=b`，其中 `a,b` 可以是任意小写字母。你写一个算法，如果 `equations` 中所有算式都不会互相冲突，返回 true，否则返回 false。

比如说，输入 `["a==b","b!=c","c==a"]`，算法返回 false，因为这三个算式不可能同时正确。

再比如，输入 `["c==c","b==d","x!=z"]`，算法返回 true，因为这三个算式并不会造成逻辑冲突。

我们前文说过，动态连通性其实就是一种等价关系，具有「自反性」「传递性」和「对称性」，其实 `==` 关系也是一种等价关系，具有这些性质。所以这个问题用 Union-Find 算法就很自然。

核心思想是，**将 `equations` 中的算式根据 `==` 和 `!=` 分成两部分，先处理 `==` 算式，使得他们通过相等关系各自勾结成门派；然后处理 `!=` 算式，检查不等关系是否破坏了相等关系的连通性**。

```java    
boolean equationsPossible(String[] equations) {
    // 26 个英文字母
    UF uf = new UF(26);
    // 先让相等的字母形成连通分量
    for (String eq : equations) {
        if (eq.charAt(1) == '=') {
            char x = eq.charAt(0);
            char y = eq.charAt(3);
            uf.union(x - 'a', y - 'a');
        }
    }
    // 检查不等关系是否打破相等关系的连通性
    for (String eq : equations) {
        if (eq.charAt(1) == '!') {
            char x = eq.charAt(0);
            char y = eq.charAt(3);
            // 如果相等关系成立，就是逻辑冲突
            if (uf.connected(x - 'a', y - 'a'))
                return false;
        }
    }
    return true;
}
```

#### 15.3 其他语言实现

**java**

第261题的Java代码（提供：[LEODPEN](https://github.com/LEODPEN)）

```java
class Solution {

    class DisjointSet {

        int count; // 连通分量的总个数
        int[] parent; // 每个节点的头节点（不一定是连通分量的最终头节点）
        int[] size; // 每个连通分量的大小

        public DisjointSet(int n) {
            parent = new int[n];
            size = new int[n];
            // 初为n个连通分量，期望最后为1
            count = n;
            for (int i = 0; i < n; i++) {
                // 初始的连通分量只有该节点本身
                parent[i] = i;
                size[i] = 1;
            }
        }

        /**
         * @param first  节点1
         * @param second 节点2
         * @return 未连通 && 连通成功
         */
        public boolean union(int first, int second) {
            // 分别找到包含first 和 second 的最终根节点
            int firstParent = findRootParent(first), secondParent = findRootParent(second);
            // 相等说明已经处于一个连通分量，即说明有环
            if (firstParent == secondParent) return false;
            // 将较小的连通分量融入较大的连通分量
            if (size[firstParent] >= size[secondParent]) {
                parent[secondParent] = firstParent;
                size[firstParent] += size[secondParent];
            } else {
                parent[firstParent] = secondParent;
                size[secondParent] += size[firstParent];
            }
            // 连通分量已合并，count减少
            count--;
            return true;
        }

        /**
         * @param node 某节点
         * @return 包含该节点的连通分量的最终根节点
         */
        private int findRootParent(int node) {
            while (node != parent[node]) {
                // 压缩路径
                parent[node] = parent[parent[node]];
                node = parent[node];
            }
            return node;
        }
    }

    public boolean validTree(int n, int[][] edges) {
        // 树的特性：节点数 = 边数 + 1
        if (edges.length != n - 1) return false;
        DisjointSet djs = new DisjointSet(n);
        for (int[] edg : edges) {
            // 判断连通情况（如果合并的两个点在一个连通分量里，说明有环）
            if (!djs.union(edg[0], edg[1])) return false;
        }
        // 是否全部节点均已相连
        return djs.count == 1;
    }
}
```

### 16 二分查找高效判定子序列

如何判定字符串 `s` 是否是字符串 `t` 的子序列（可以假定 `s` 长度比较小，且 `t` 的长度非常大）。举两个例子：


s = "abc", t = "**a**h**b**gd**c**", return true.


s = "axc", t = "ahbgdc", return false.

#### 16.1 实现

这里以单个字符串 `s` 为例，对于多个字符串 `s`，可以把预处理部分抽出来。

```java
boolean isSubsequence(String s, String t) {
    int m = s.length(), n = t.length();
    // 对 t 进行预处理
    ArrayList<Integer>[] index = new ArrayList[256];
    for (int i = 0; i < n; i++) {
        char c = t.charAt(i);
        if (index[c] == null) 
            index[c] = new ArrayList<>();
        index[c].add(i);
    }
    
    // 串 t 上的指针
    int j = 0;
    // 借助 index 查找 s[i]
    for (int i = 0; i < m; i++) {
        char c = s.charAt(i);
        // 整个 t 压根儿没有字符 c
        if (index[c] == null) return false;
        int pos = left_bound(index[c], j);
        // 二分搜索区间中没有找到字符 c
        if (pos == index[c].size()) return false;
        // 向前移动指针 j
        j = index[c].get(pos) + 1;
    }
    return true;
}
```


#### 16.2 其他语言实现

**c++**

[dekunma](https://www.linkedin.com/in/dekun-ma-036a9b198/) 提供C++代码 

**解法一：遍历（也可以用双指针）：**  

```C++
class Solution {
public:
    bool isSubsequence(string s, string t) {
        // 遍历s
        for(int i = 0; i < s.size(); i++) {
            // 找到s[i]字符在t中的位置
            size_t pos = t.find(s[i]);
            
            // 如果s[i]字符不在t中，返回false
            if(pos == std::string::npos) return false;
            // 如果s[i]在t中，后面就只看pos以后的字串，防止重复查找
            else t = t.substr(pos + 1);
        }
        return true;
    }
};
```

**解法二：二分查找：**  
```C++
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int m = s.size(), n = t.size();
        // 对 t 进行预处理
        vector<int> index[256];
        for (int i = 0; i < n; i++) {
            char c = t[i];
            index[c].push_back(i);
        }
        // 串 t 上的指针
        int j = 0;
        // 借助 index 查找 s[i]
        for (int i = 0; i < m; i++) {
            char c = s[i];
            // 整个 t 压根儿没有字符 c
            if (index[c].empty()) return false;
            int pos = left_bound(index[c], j);
            // 二分搜索区间中没有找到字符 c
            if (pos == index[c].size()) return false;
            // 向前移动指针 j
            j = index[c][pos] + 1;
        }
        return true;
    }
    // 查找左侧边界的二分查找
    int left_bound(vector<int> arr, int tar) {
        int lo = 0, hi = arr.size();
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (tar > arr[mid]) {
                lo = mid + 1;
            } else {
                hi = mid;
            } 
        }
        return lo;
    }
};
```
