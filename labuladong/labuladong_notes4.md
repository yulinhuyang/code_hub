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

