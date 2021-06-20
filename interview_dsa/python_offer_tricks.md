### 1 主要参考：

刷题顺序： 剑指offer --> labuladong --> 头条腾讯 高频面试题

剑指offer:

https://github.com/JushuangQiao/Python-Offer

https://zhuanlan.zhihu.com/p/75864673

leetcode:

https://blog.csdn.net/qq_32424059/article/details/88855423


### 2 notes 

#### python使用基础

**创建一维、二维数组**

    array = [0 for i in range(3)]

    two_array = [[0 for i in range(3)] for i in range(3)]


**循环:**

    python反向循环：

    for i in range(len(a)-1,-1,-1):

    while循环，非+1情况

**list 和str互相转换：**
  
    str->list
    
    str1 = "12345"
    list1 = list(str1)
    
    
    list2 = str2.split( ) 或者  list3 = str3.split(".")
    
    list->str
    
    str4 = "".join(list3)  或者 str4 = " ".join(list3)
    
 
**list常用操作**

    insert(index)  pop(-1)

    反转链表： res[::-1]  reverse(res)


fib 循环法: a,b = b, a+b

**for range**
    
    指定 start stop step

 
 **简单数据结构**
 
     class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
   
 **注意点**
    
    return None 和return []

    判等 ==

    self 使用

    
 **set**

用set来表示一个无序不重复元素的序列。set的只要作用就是用来给数据去重。 

可以使用大括号 { } 或者 set() 函数创建集合

eg: 

添加一对数：

vis = set([(0, 0)])

vis.add((i, j))


/ 除以，带小数

//整除

**dict**

创建字典：

d = {key1 : value1, key2 : value2 }

eg；

dict = {'a': 1, 'b': 2, 'b': '3'}

**tuple**

tup1 = ('physics', 'chemistry', 1997, 2000)   
    
    
    
### 3 思路专题

**动态规划**

动态规划的特点：重叠子问题、状态转移方程、最优子结构

核心是穷举

套路: 明确 状态 --->明确 选择 ---> 明确dp函数/数组的定义---->明确base case 


暴力递归--->memo 解法--->pre cur for循环解法 ————>dp 数组


memo: 初始化为N+1

暴力递归：

	自顶向下的递归：f(20)————>f(19)————>.....f(0)

	其实，dp数组里面存的内容和memo是完全一样的，只不过把递归改成了for循环迭代了而已。

自底向上的迭代:
	
	f(0)--->f(1) ....f（20）

	pre-cur for循环解法

    
    
    
    
    


    
