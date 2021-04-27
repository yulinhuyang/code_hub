### 前缀和技巧

#### 前缀和思路

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

#### 应用

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

### 字符串乘法

#### 描述

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"

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
#### 其他语言实现


### python

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

### java

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


### FloodFill算法详解及应用

#### 描述框架

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


### 区间调度之区间合并问题

[56.合并区间](https://leetcode-cn.com/problems/merge-intervals)

#### 区间合并

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

#### 其他语言实现

##### java

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

##### c++

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

### 区间调度之区间交集问题

[986.区间列表的交集](https://leetcode-cn.com/problems/interval-list-intersections)

#### 解法

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

#### java实现

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

### 信封嵌套问题

#### 描述

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

### 洗牌算法

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

#### 蒙特卡罗方法验证正确性

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

### 递归详解

#### 写递归的技巧

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

#### 分治算法

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


