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





