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


