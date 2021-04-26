
源码： https://github.com/zhedahht/CodingInterviewChinese2


## 目录：

2. 实现 Singleton

3. 数组中重复的数字

4. 二维数组中的查找

5. 替换空格

6. 从尾到头打印链表

7. 重建二叉树

8. 二叉树的下一个结点

9. 用两个栈实现队列

10.1 斐波那契数列

10.2 跳台阶

10.3 变态跳台阶

10.4 矩形覆盖

11. 旋转数组的最小数字

12. 矩阵中的路径

13. 机器人的运动范围

14. 剪绳子

15. 二进制中 1 的个数

16. 数值的整数次方

17. 打印从 1 到最大的 n 位数

18.1 在 O(1) 时间内删除链表节点

18.2 删除链表中重复的结点

19. 正则表达式匹配

20. 表示数值的字符串

21. 调整数组顺序使奇数位于偶数前面

22. 链表中倒数第 K 个结点

23. 链表中环的入口结点

24. 反转链表

25. 合并两个排序的链表

26. 树的子结构

27. 二叉树的镜像

28.1 对称的二叉树

28.2 平衡二叉树

29. 顺时针打印矩阵

30. 包含 min 函数的栈

31. 栈的压入、弹出序列

32.1 从上往下打印二叉树

32.2 把二叉树打印成多行

32.3 按之字形顺序打印二叉树

33. 二叉搜索树的后序遍历序列

34. 二叉树中和为某一值的路径

35. 复杂链表的复制

36. 二叉搜索树与双向链表

37. 序列化二叉树

38. 字符串的排列

39. 数组中出现次数超过一半的数字

40. 最小的 K 个数

41.1 数据流中的中位数

41.2 字符流中第一个不重复的字符

42. 连续子数组的最大和

43. 从 1 到 n 整数中 1 出现的次数

44. 数字序列中的某一位数字

45. 把数组排成最小的数

46. 把数字翻译成字符串

47. 礼物的最大价值

48. 最长不含重复字符的子字符串

49. 丑数

50. 第一个只出现一次的字符位置

51. 数组中的逆序对

52. 两个链表的第一个公共结点

53 数字在排序数组中出现的次数

54. 二叉搜索树的第 k 个结点

55 二叉树的深度

56. 数组中只出现一次的数字

57.1 和为 S 的两个数字

57.2 和为 S 的连续正数序列

58.1 翻转单词顺序列

58.2 左旋转字符串

59. 滑动窗口的最大值

60. n 个骰子的点数

61. 扑克牌顺子

62. 圆圈中最后剩下的数

63. 股票的最大利润

64. 求 1+2+3+...+n

65. 不用加减乘除做加法

66. 构建乘积数组

67. 把字符串转换成整数

68. 树中两个节点的最低公共祖先




## 1  Utilities

### Array

```c++
Array.h

#pragma once

__declspec( dllexport ) int Partition(int data[], int length, int start, int end);

Array.cpp


#include <stdlib.h>
#include "Array.h"
#include <exception>

// Random Partition
int RandomInRange(int min, int max)
{
    int random = rand() % (max - min + 1) + min;
    return random;
}

void Swap(int* num1, int* num2)
{
    int temp = *num1;
    *num1 = *num2;
    *num2 = temp;
}

int Partition(int data[], int length, int start, int end)
{
    if(data == nullptr || length <= 0 || start < 0 || end >= length)
        throw new std::exception("Invalid Parameters");

    int index = RandomInRange(start, end);
    Swap(&data[index], &data[end]);

    int small = start - 1;
    for(index = start; index < end; ++ index)
    {
        if(data[index] < data[end])
        {
            ++ small;
            if(small != index)
                Swap(&data[index], &data[small]);
        }
    }

    ++ small;
    Swap(&data[small], &data[end]);

    return small;
}

```

### list

```c++

list.h

struct ListNode
{
    int       m_nValue;
    ListNode* m_pNext;
};

__declspec( dllexport ) ListNode* CreateListNode(int value);
__declspec( dllexport ) void ConnectListNodes(ListNode* pCurrent, ListNode* pNext);
__declspec( dllexport ) void PrintListNode(ListNode* pNode);
__declspec( dllexport ) void PrintList(ListNode* pHead);
__declspec( dllexport ) void DestroyList(ListNode* pHead);
__declspec( dllexport ) void AddToTail(ListNode** pHead, int value);
__declspec( dllexport ) void RemoveNode(ListNode** pHead, int value);


list.cpp

#include "list.h"
#include <stdio.h>
#include <stdlib.h>

ListNode* CreateListNode(int value)
{
    ListNode* pNode = new ListNode();
    pNode->m_nValue = value;
    pNode->m_pNext = nullptr;

    return pNode;
}

void ConnectListNodes(ListNode* pCurrent, ListNode* pNext)
{
    if(pCurrent == nullptr)
    {
        printf("Error to connect two nodes.\n");
        exit(1);
    }

    pCurrent->m_pNext = pNext;
}

void PrintListNode(ListNode* pNode)
{ 
    if(pNode == nullptr)
    {
        printf("The node is nullptr\n");
    }
    else
    {
        printf("The key in node is %d.\n", pNode->m_nValue);
    }
}

void PrintList(ListNode* pHead)
{
    printf("PrintList starts.\n");
    
    ListNode* pNode = pHead;
    while(pNode != nullptr)
    {
        printf("%d\t", pNode->m_nValue);
        pNode = pNode->m_pNext;
    }

    printf("\nPrintList ends.\n");
}

void DestroyList(ListNode* pHead)
{
    ListNode* pNode = pHead;
    while(pNode != nullptr)
    {
        pHead = pHead->m_pNext;
        delete pNode;
        pNode = pHead;
    }
}

void AddToTail(ListNode** pHead, int value)
{
    ListNode* pNew = new ListNode();
    pNew->m_nValue = value;
    pNew->m_pNext = nullptr;

    if(*pHead == nullptr)
    {
        *pHead = pNew;
    }
    else
    {
        ListNode* pNode = *pHead;
        while(pNode->m_pNext != nullptr)
            pNode = pNode->m_pNext;

        pNode->m_pNext = pNew;
    }
}

void RemoveNode(ListNode** pHead, int value)
{
    if(pHead == nullptr || *pHead == nullptr)
        return;

    ListNode* pToBeDeleted = nullptr;
    if((*pHead)->m_nValue == value)
    {
        pToBeDeleted = *pHead;
        *pHead = (*pHead)->m_pNext;
    }
    else
    {
        ListNode* pNode = *pHead;
        while(pNode->m_pNext != nullptr && pNode->m_pNext->m_nValue != value)
            pNode = pNode->m_pNext;

        if(pNode->m_pNext != nullptr && pNode->m_pNext->m_nValue == value)
        {
            pToBeDeleted = pNode->m_pNext;
            pNode->m_pNext = pNode->m_pNext->m_pNext;
        }
    }

    if(pToBeDeleted != nullptr)
    {
        delete pToBeDeleted;
        pToBeDeleted = nullptr;
    }
}
```


### string

```c++

StringUtil.h

__declspec( dllexport ) void Reverse(char *pBegin, char *pEnd);

StringUtil.cpp

#include "StringUtil.h"

void Reverse(char *pBegin, char *pEnd)
{
    if(pBegin == nullptr || pEnd == nullptr)
        return;

    while(pBegin < pEnd)
    {
        char temp = *pBegin;
        *pBegin = *pEnd;
        *pEnd = temp;

        pBegin ++, pEnd --;
    }
}

```

### Tree

```c++

Tree.h

#pragma once

#include <vector>

struct TreeNode 
{
    int                       m_nValue;    
    std::vector<TreeNode*>    m_vChildren;    
};

__declspec( dllexport ) TreeNode* CreateTreeNode(int value);
__declspec( dllexport ) void ConnectTreeNodes(TreeNode* pParent, TreeNode* pChild);
__declspec( dllexport ) void PrintTreeNode(const TreeNode* pNode);
__declspec( dllexport ) void PrintTree(const TreeNode* pRoot);
__declspec( dllexport ) void DestroyTree(TreeNode* pRoot);

Tree.cpp

#include "Tree.h"

TreeNode* CreateTreeNode(int value)
{
    TreeNode* pNode = new TreeNode();
    pNode->m_nValue = value;

    return pNode;
}

void ConnectTreeNodes(TreeNode* pParent, TreeNode* pChild)
{
    if(pParent != nullptr)
    {
        pParent->m_vChildren.push_back(pChild);
    }
}

void PrintTreeNode(const TreeNode* pNode)
{
    if(pNode != nullptr)
    {
        printf("value of this node is: %d.\n", pNode->m_nValue);

        printf("its children is as the following:\n");
        std::vector<TreeNode*>::const_iterator i = pNode->m_vChildren.begin();
        while(i < pNode->m_vChildren.end())
        {
            if(*i != nullptr)
                printf("%d\t", (*i)->m_nValue);
        }

        printf("\n");
    }
    else
    {
        printf("this node is nullptr.\n");
    }

    printf("\n");
}

void PrintTree(const TreeNode* pRoot)
{
    PrintTreeNode(pRoot);

    if(pRoot != nullptr)
    {
        std::vector<TreeNode*>::const_iterator i = pRoot->m_vChildren.begin();
        while(i < pRoot->m_vChildren.end())
        {
            PrintTree(*i);
            ++i;
        }
    }
}

void DestroyTree(TreeNode* pRoot)
{
    if(pRoot != nullptr)
    {
        std::vector<TreeNode*>::iterator i = pRoot->m_vChildren.begin();
        while(i < pRoot->m_vChildren.end())
        {
            DestroyTree(*i);
            ++i;
        }

        delete pRoot;
    }
}
```

### BinaryTree

```c++

BinaryTree.h

#pragma once

struct BinaryTreeNode 
{
    int                    m_nValue; 
    BinaryTreeNode*        m_pLeft;  
    BinaryTreeNode*        m_pRight; 
};

__declspec( dllexport ) BinaryTreeNode* CreateBinaryTreeNode(int value);
__declspec( dllexport ) void ConnectTreeNodes(BinaryTreeNode* pParent, BinaryTreeNode* pLeft, BinaryTreeNode* pRight);
__declspec( dllexport ) void PrintTreeNode(const BinaryTreeNode* pNode);
__declspec( dllexport ) void PrintTree(const BinaryTreeNode* pRoot);
__declspec( dllexport ) void DestroyTree(BinaryTreeNode* pRoot);


BinaryTree.cpp

#include <cstdio>
#include "BinaryTree.h"

BinaryTreeNode* CreateBinaryTreeNode(int value)
{
    BinaryTreeNode* pNode = new BinaryTreeNode();
    pNode->m_nValue = value;
    pNode->m_pLeft = nullptr;
    pNode->m_pRight = nullptr;

    return pNode;
}

void ConnectTreeNodes(BinaryTreeNode* pParent, BinaryTreeNode* pLeft, BinaryTreeNode* pRight)
{
    if(pParent != nullptr)
    {
        pParent->m_pLeft = pLeft;
        pParent->m_pRight = pRight;
    }
}

void PrintTreeNode(const BinaryTreeNode* pNode)
{
    if(pNode != nullptr)
    {
        printf("value of this node is: %d\n", pNode->m_nValue);

        if(pNode->m_pLeft != nullptr)
            printf("value of its left child is: %d.\n", pNode->m_pLeft->m_nValue);
        else
            printf("left child is nullptr.\n");

        if(pNode->m_pRight != nullptr)
            printf("value of its right child is: %d.\n", pNode->m_pRight->m_nValue);
        else
            printf("right child is nullptr.\n");
    }
    else
    {
        printf("this node is nullptr.\n");
    }

    printf("\n");
}

void PrintTree(const BinaryTreeNode* pRoot)
{
    PrintTreeNode(pRoot);

    if(pRoot != nullptr)
    {
        if(pRoot->m_pLeft != nullptr)
            PrintTree(pRoot->m_pLeft);

        if(pRoot->m_pRight != nullptr)
            PrintTree(pRoot->m_pRight);
    }
}

void DestroyTree(BinaryTreeNode* pRoot)
{
    if(pRoot != nullptr)
    {
        BinaryTreeNode* pLeft = pRoot->m_pLeft;
        BinaryTreeNode* pRight = pRoot->m_pRight;

        delete pRoot;
        pRoot = nullptr;

        DestroyTree(pLeft);
        DestroyTree(pRight);
    }
}
```


## 2  题目

### 02_Singleton

// 面试题2：实现Singleton模式

// 题目：设计一个类，我们只能生成该类的一个实例。

```c++
using System;

namespace _02_Singleton
{
    public sealed class Singleton1
    {
        private Singleton1()
        {
        }

        private static Singleton1 instance = null;
        public static Singleton1 Instance
        {
            get
            {
                if (instance == null)
                    instance = new Singleton1();

                return instance;
            }
        }
    }

    public sealed class Singleton2
    {
        private Singleton2()
        {
        }

        private static readonly object syncObj = new object();

        private static Singleton2 instance = null;
        public static Singleton2 Instance
        {
            get
            {
                lock (syncObj)
                {
                    if (instance == null)
                        instance = new Singleton2();
                }

                return instance;
            }
        }
    }

    public sealed class Singleton3
    {
        private Singleton3()
        {
        }

        private static object syncObj = new object();

        private static Singleton3 instance = null;
        public static Singleton3 Instance
        {
            get
            {
                if (instance == null)
                {
                    lock (syncObj)
                    {
                        if (instance == null)
                            instance = new Singleton3();
                    }
                }

                return instance;
            }
        }
    }

    public sealed class Singleton4
    {
        private Singleton4()
        {
            Console.WriteLine("An instance of Singleton4 is created.");
        }

        public static void Print()
        {
            Console.WriteLine("Singleton4 Print");
        }

        private static Singleton4 instance = new Singleton4();
        public static Singleton4 Instance
        {
            get
            {
                return instance;
            }
        }
    }

    public sealed class Singleton5
    {
        Singleton5()
        {
            Console.WriteLine("An instance of Singleton5 is created.");
        }

        public static void Print()
        {
            Console.WriteLine("Singleton5 Print");
        }

        public static Singleton5 Instance
        {
            get
            {
                return Nested.instance;
            }
        }

        class Nested
        {
            static Nested()
            {
            }

            internal static readonly Singleton5 instance = new Singleton5();
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // 也会打印An instance of Singleton4 is created.
            Singleton4.Print();

            // 不会打印An instance of Singleton5 is created.
            Singleton5.Print();
        }
    }
}
```


### 03_01_DuplicationInArray

// 面试题3（一）：找出数组中重复的数字

// 题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，

// 也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组{2, 3, 1, 0, 2, 5, 3}，

// 那么对应的输出是重复的数字2或者3。


```c++
#include <cstdio>

// 参数:
//        numbers:     一个整数数组
//        length:      数组的长度
//        duplication: (输出) 数组中的一个重复的数字
// 返回值:             
//        true  - 输入有效，并且数组中存在重复的数字
//        false - 输入无效，或者数组中没有重复的数字
bool duplicate(int numbers[], int length, int* duplication)
{
    if(numbers == nullptr || length <= 0)
        return false;

    for(int i = 0; i < length; ++i)
    {
        if(numbers[i] < 0 || numbers[i] > length - 1)
            return false;
    }

    for(int i = 0; i < length; ++i)
    {
        while(numbers[i] != i)
        {
            if(numbers[i] == numbers[numbers[i]])
            {
                *duplication = numbers[i];
                return true;
            }

            // 交换numbers[i]和numbers[numbers[i]]             
            int temp = numbers[i];
            numbers[i] = numbers[temp];
            numbers[temp] = temp;
        }
    }

    return false;
}

// ====================测试代码====================
bool contains(int array[], int length, int number)
{
    for(int i = 0; i < length; ++i)
    {
        if(array[i] == number)
            return true;
    }

    return false;
}
```


### 03_02_DuplicationInArrayNoEdit

// 面试题3（二）：不修改数组找出重复的数字

// 题目：在一个长度为n+1的数组里的所有数字都在1到n的范围内，所以数组中至

// 少有一个数字是重复的。请找出数组中任意一个重复的数字，但不能修改输入的

// 数组。例如，如果输入长度为8的数组{2, 3, 5, 4, 3, 2, 6, 7}，那么对应的

// 输出是重复的数字2或者3。


```c++
#include <iostream>

int countRange(const int* numbers, int length, int start, int end);

// 参数:
//        numbers:     一个整数数组
//        length:      数组的长度
// 返回值:             
//        正数  - 输入有效，并且数组中存在重复的数字，返回值为重复的数字
//        负数  - 输入无效，或者数组中没有重复的数字
int getDuplication(const int* numbers, int length)
{
    if(numbers == nullptr || length <= 0)
        return -1;

    int start = 1;
    int end = length - 1;
    while(end >= start)
    {
        int middle = ((end - start) >> 1) + start;
        int count = countRange(numbers, length, start, middle);
        if(end == start)
        {
            if(count > 1)
                return start;
            else
                break;
        }

        if(count > (middle - start + 1))
            end = middle;
        else
            start = middle + 1;
    }
    return -1;
}

int countRange(const int* numbers, int length, int start, int end)
{
    if(numbers == nullptr)
        return 0;

    int count = 0;
    for(int i = 0; i < length; i++)
        if(numbers[i] >= start && numbers[i] <= end)
            ++count;
    return count;
}
```

### 04_FindInPartiallySortedMatrix


// 面试题4：二维数组中的查找

// 题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按

// 照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个

// 整数，判断数组中是否含有该整数。


```c++

#include <cstdio>

bool Find(int* matrix, int rows, int columns, int number)
{
    bool found = false;

    if(matrix != nullptr && rows > 0 && columns > 0)
    {
        int row = 0;
        int column = columns - 1;
        while(row < rows && column >=0)
        {
            if(matrix[row * columns + column] == number)
            {
                found = true;
                break;
            }
            else if(matrix[row * columns + column] > number)
                -- column;
            else
                ++ row;
        }
    }

    return found;
}

// ====================测试代码====================
void Test(char* testName, int* matrix, int rows, int columns, int number, bool expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    bool result = Find(matrix, rows, columns, number);
    if(result == expected)
        printf("Passed.\n");
    else
        printf("Failed.\n");
}
```



### 05_ReplaceSpaces

// 面试题5：替换空格

// 题目：请实现一个函数，把字符串中的每个空格替换成"%20"。例如输入“We are happy.”，

// 则输出“We%20are%20happy.”。


```c++
#include <cstdio>
#include <cstring>

/*length 为字符数组str的总容量，大于或等于字符串str的实际长度*/
void ReplaceBlank(char str[], int length)
{
    if(str == nullptr && length <= 0)
        return;

    /*originalLength 为字符串str的实际长度*/
    int originalLength = 0;
    int numberOfBlank = 0;
    int i = 0;
    while(str[i] != '\0')
    {
        ++ originalLength;

        if(str[i] == ' ')
            ++ numberOfBlank;

        ++ i;
    }

    /*newLength 为把空格替换成'%20'之后的长度*/
    int newLength = originalLength + numberOfBlank * 2;
    if(newLength > length)
        return;

    int indexOfOriginal = originalLength;
    int indexOfNew = newLength;
    while(indexOfOriginal >= 0 && indexOfNew > indexOfOriginal)
    {
        if(str[indexOfOriginal] == ' ')
        {
            str[indexOfNew --] = '0';
            str[indexOfNew --] = '2';
            str[indexOfNew --] = '%';
        }
        else
        {
            str[indexOfNew --] = str[indexOfOriginal];
        }

        -- indexOfOriginal;
    }
}

// ====================测试代码====================
void Test(char* testName, char str[], int length, char expected[])
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    ReplaceBlank(str, length);

    if(expected == nullptr && str == nullptr)
        printf("passed.\n");
    else if(expected == nullptr && str != nullptr)
        printf("failed.\n");
    else if(strcmp(str, expected) == 0)
        printf("passed.\n");
    else
        printf("failed.\n");
}

// 空格在句子中间
void Test1()
{
    const int length = 100;

    char str[length] = "hello world";
    Test("Test1", str, length, "hello%20world");
}

// 空格在句子开头
void Test2()
{
    const int length = 100;

    char str[length] = " helloworld";
    Test("Test2", str, length, "%20helloworld");
}
```


### 06_PrintListInReversedOrder

// 面试题6：从尾到头打印链表

// 题目：输入一个链表的头结点，从尾到头反过来打印出每个结点的值。


```c++

#include "..\Utilities\List.h"
#include <stack>

void PrintListReversingly_Iteratively(ListNode* pHead)
{
    std::stack<ListNode*> nodes;

    ListNode* pNode = pHead;
    while(pNode != nullptr)
    {
        nodes.push(pNode);
        pNode = pNode->m_pNext;
    }

    while(!nodes.empty())
    {
        pNode = nodes.top();
        printf("%d\t", pNode->m_nValue);
        nodes.pop();
    }
}

void PrintListReversingly_Recursively(ListNode* pHead)
{
    if(pHead != nullptr)
    {
        if (pHead->m_pNext != nullptr)
        {
            PrintListReversingly_Recursively(pHead->m_pNext);
        }
 
        printf("%d\t", pHead->m_nValue);
    }
}

// ====================测试代码====================
void Test(ListNode* pHead)
{
    PrintList(pHead);
    PrintListReversingly_Iteratively(pHead);
    printf("\n");
    PrintListReversingly_Recursively(pHead);
}

// 1->2->3->4->5
void Test1()
{
    printf("\nTest1 begins.\n");

    ListNode* pNode1 = CreateListNode(1);
    ListNode* pNode2 = CreateListNode(2);
    ListNode* pNode3 = CreateListNode(3);
    ListNode* pNode4 = CreateListNode(4);
    ListNode* pNode5 = CreateListNode(5);

    ConnectListNodes(pNode1, pNode2);
    ConnectListNodes(pNode2, pNode3);
    ConnectListNodes(pNode3, pNode4);
    ConnectListNodes(pNode4, pNode5);

    Test(pNode1);

    DestroyList(pNode1);
}
```


### 07_ConstructBinaryTree

// 面试题7：重建二叉树

// 题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输

// 入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,

// 2, 4, 7, 3, 5, 6, 8}和中序遍历序列{4, 7, 2, 1, 5, 3, 8, 6}，则重建出

// 图2.6所示的二叉树并输出它的头结点。


```c++

#include "..\Utilities\BinaryTree.h"
#include <exception>
#include <cstdio>

BinaryTreeNode* ConstructCore(int* startPreorder, int* endPreorder, int* startInorder, int* endInorder);

BinaryTreeNode* Construct(int* preorder, int* inorder, int length)
{
    if(preorder == nullptr || inorder == nullptr || length <= 0)
        return nullptr;

    return ConstructCore(preorder, preorder + length - 1,
        inorder, inorder + length - 1);
}

BinaryTreeNode* ConstructCore
(
    int* startPreorder, int* endPreorder, 
    int* startInorder, int* endInorder
)
{
    // 前序遍历序列的第一个数字是根结点的值
    int rootValue = startPreorder[0];
    BinaryTreeNode* root = new BinaryTreeNode();
    root->m_nValue = rootValue;
    root->m_pLeft = root->m_pRight = nullptr;

    if(startPreorder == endPreorder)
    {
        if(startInorder == endInorder && *startPreorder == *startInorder)
            return root;
        else
            throw std::exception("Invalid input.");
    }

    // 在中序遍历中找到根结点的值
    int* rootInorder = startInorder;
    while(rootInorder <= endInorder && *rootInorder != rootValue)
        ++ rootInorder;

    if(rootInorder == endInorder && *rootInorder != rootValue)
        throw std::exception("Invalid input.");

    int leftLength = rootInorder - startInorder;
    int* leftPreorderEnd = startPreorder + leftLength;
    if(leftLength > 0)
    {
        // 构建左子树
        root->m_pLeft = ConstructCore(startPreorder + 1, leftPreorderEnd, 
            startInorder, rootInorder - 1);
    }
    if(leftLength < endPreorder - startPreorder)
    {
        // 构建右子树
        root->m_pRight = ConstructCore(leftPreorderEnd + 1, endPreorder,
            rootInorder + 1, endInorder);
    }

    return root;
}

// ====================测试代码====================
void Test(char* testName, int* preorder, int* inorder, int length)
{
    if(testName != nullptr)
        printf("%s begins:\n", testName);

    printf("The preorder sequence is: ");
    for(int i = 0; i < length; ++ i)
        printf("%d ", preorder[i]);
    printf("\n");

    printf("The inorder sequence is: ");
    for(int i = 0; i < length; ++ i)
        printf("%d ", inorder[i]);
    printf("\n");

    try
    {
        BinaryTreeNode* root = Construct(preorder, inorder, length);
        PrintTree(root);

        DestroyTree(root);
    }
    catch(std::exception& exception)
    {
        printf("Invalid Input.\n");
    }
}

// 普通二叉树
//              1
//           /     \
//          2       3  
//         /       / \
//        4       5   6
//         \         /
//          7       8
void Test1()
{
    const int length = 8;
    int preorder[length] = {1, 2, 4, 7, 3, 5, 6, 8};
    int inorder[length] = {4, 7, 2, 1, 5, 3, 8, 6};

    Test("Test1", preorder, inorder, length);
}

// 所有结点都没有右子结点
//            1
//           / 
//          2   
//         / 
//        3 
//       /
//      4
//     /
//    5
void Test2()
{
    const int length = 5;
    int preorder[length] = {1, 2, 3, 4, 5};
    int inorder[length] = {5, 4, 3, 2, 1};

    Test("Test2", preorder, inorder, length);
}

// 所有结点都没有左子结点
//            1
//             \ 
//              2   
//               \ 
//                3 
//                 \
//                  4
//                   \
//                    5
void Test3()
{
    const int length = 5;
    int preorder[length] = {1, 2, 3, 4, 5};
    int inorder[length] = {1, 2, 3, 4, 5};

    Test("Test3", preorder, inorder, length);
}

// 树中只有一个结点
void Test4()
{
    const int length = 1;
    int preorder[length] = {1};
    int inorder[length] = {1};

    Test("Test4", preorder, inorder, length);
}

// 完全二叉树
//              1
//           /     \
//          2       3  
//         / \     / \
//        4   5   6   7
void Test5()
{
    const int length = 7;
    int preorder[length] = {1, 2, 4, 5, 3, 6, 7};
    int inorder[length] = {4, 2, 5, 1, 6, 3, 7};

    Test("Test5", preorder, inorder, length);
}

// 输入空指针
void Test6()
{
    Test("Test6", nullptr, nullptr, 0);
}

// 输入的两个序列不匹配
void Test7()
{
    const int length = 7;
    int preorder[length] = {1, 2, 4, 5, 3, 6, 7};
    int inorder[length] = {4, 2, 8, 1, 6, 3, 7};

    Test("Test7: for unmatched input", preorder, inorder, length);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
    Test5();
    Test6();
    Test7();

    return 0;
}

```

### 08_NextNodeInBinaryTrees

// 面试题8：二叉树的下一个结点

// 题目：给定一棵二叉树和其中的一个结点，如何找出中序遍历顺序的下一个结点？

// 树中的结点除了有两个分别指向左右子结点的指针以外，还有一个指向父结点的指针。

```c++
#include <stdio.h>

struct BinaryTreeNode
{
    int                    m_nValue;
    BinaryTreeNode*        m_pLeft;
    BinaryTreeNode*        m_pRight;
    BinaryTreeNode*        m_pParent;
};

BinaryTreeNode* GetNext(BinaryTreeNode* pNode)
{
    if(pNode == nullptr)
        return nullptr;

    BinaryTreeNode* pNext = nullptr;
    if(pNode->m_pRight != nullptr)
    {
        BinaryTreeNode* pRight = pNode->m_pRight;
        while(pRight->m_pLeft != nullptr)
            pRight = pRight->m_pLeft;

        pNext = pRight;
    }
    else if(pNode->m_pParent != nullptr)
    {
        BinaryTreeNode* pCurrent = pNode;
        BinaryTreeNode* pParent = pNode->m_pParent;
        while(pParent != nullptr && pCurrent == pParent->m_pRight)
        {
            pCurrent = pParent;
            pParent = pParent->m_pParent;
        }

        pNext = pParent;
    }

    return pNext;
}

// ==================== 辅助代码用来构建二叉树 ====================
BinaryTreeNode* CreateBinaryTreeNode(int value)
{
    BinaryTreeNode* pNode = new BinaryTreeNode();
    pNode->m_nValue = value;
    pNode->m_pLeft = nullptr;
    pNode->m_pRight = nullptr;
    pNode->m_pParent = nullptr;

    return pNode;
}

void ConnectTreeNodes(BinaryTreeNode* pParent, BinaryTreeNode* pLeft, BinaryTreeNode* pRight)
{
    if(pParent != nullptr)
    {
        pParent->m_pLeft = pLeft;
        pParent->m_pRight = pRight;

        if(pLeft != nullptr)
            pLeft->m_pParent = pParent;
        if(pRight != nullptr)
            pRight->m_pParent = pParent;
    }
}

void PrintTreeNode(BinaryTreeNode* pNode)
{
    if(pNode != nullptr)
    {
        printf("value of this node is: %d\n", pNode->m_nValue);

        if(pNode->m_pLeft != nullptr)
            printf("value of its left child is: %d.\n", pNode->m_pLeft->m_nValue);
        else
            printf("left child is null.\n");

        if(pNode->m_pRight != nullptr)
            printf("value of its right child is: %d.\n", pNode->m_pRight->m_nValue);
        else
            printf("right child is null.\n");
    }
    else
    {
        printf("this node is null.\n");
    }

    printf("\n");
}

void PrintTree(BinaryTreeNode* pRoot)
{
    PrintTreeNode(pRoot);

    if(pRoot != nullptr)
    {
        if(pRoot->m_pLeft != nullptr)
            PrintTree(pRoot->m_pLeft);

        if(pRoot->m_pRight != nullptr)
            PrintTree(pRoot->m_pRight);
    }
}

void DestroyTree(BinaryTreeNode* pRoot)
{
    if(pRoot != nullptr)
    {
        BinaryTreeNode* pLeft = pRoot->m_pLeft;
        BinaryTreeNode* pRight = pRoot->m_pRight;

        delete pRoot;
        pRoot = nullptr;

        DestroyTree(pLeft);
        DestroyTree(pRight);
    }
}

// ====================测试代码====================
void Test(char* testName, BinaryTreeNode* pNode, BinaryTreeNode* expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    BinaryTreeNode* pNext = GetNext(pNode);
    if(pNext == expected)
        printf("Passed.\n");
    else
        printf("FAILED.\n");
}

//            8
//        6      10
//       5 7    9  11
void Test1_7()
{
    BinaryTreeNode* pNode8 = CreateBinaryTreeNode(8);
    BinaryTreeNode* pNode6 = CreateBinaryTreeNode(6);
    BinaryTreeNode* pNode10 = CreateBinaryTreeNode(10);
    BinaryTreeNode* pNode5 = CreateBinaryTreeNode(5);
    BinaryTreeNode* pNode7 = CreateBinaryTreeNode(7);
    BinaryTreeNode* pNode9 = CreateBinaryTreeNode(9);
    BinaryTreeNode* pNode11 = CreateBinaryTreeNode(11);

    ConnectTreeNodes(pNode8, pNode6, pNode10);
    ConnectTreeNodes(pNode6, pNode5, pNode7);
    ConnectTreeNodes(pNode10, pNode9, pNode11);

    Test("Test1", pNode8, pNode9);
    Test("Test2", pNode6, pNode7);
    Test("Test3", pNode10, pNode11);
    Test("Test4", pNode5, pNode6);
    Test("Test5", pNode7, pNode8);
    Test("Test6", pNode9, pNode10);
    Test("Test7", pNode11, nullptr);

    DestroyTree(pNode8);
}

```

### 09_QueueWithTwoStacks

// 面试题9：用两个栈实现队列

// 题目：用两个栈实现一个队列。队列的声明如下，请实现它的两个函数appendTail

// 和deleteHead，分别完成在队列尾部插入结点和在队列头部删除结点的功能。


```c++

Queue.h

#pragma once
#include <stack>
#include <exception>

using namespace std;

template <typename T> class CQueue
{
public:
    CQueue(void);
    ~CQueue(void);
    
    // 在队列末尾添加一个结点
    void appendTail(const T& node);

    // 删除队列的头结点
    T deleteHead();

private:
    stack<T> stack1;
    stack<T> stack2;
};

template <typename T> CQueue<T>::CQueue(void)
{
}

template <typename T> CQueue<T>::~CQueue(void)
{
}

template<typename T> void CQueue<T>::appendTail(const T& element)
{
    stack1.push(element);
} 

template<typename T> T CQueue<T>::deleteHead()
{
    if(stack2.size()<= 0)
    {
        while(stack1.size()>0)
        {
            T& data = stack1.top();
            stack1.pop();
            stack2.push(data);
        }
    }

    if(stack2.size() == 0)
        throw new exception("queue is empty");

    T head = stack2.top();
    stack2.pop();

    return head;
}


QueueWithTwoStacks.cpp

#include "Queue.h"

// ====================测试代码====================
void Test(char actual, char expected)
{
    if(actual == expected)
        printf("Test passed.\n");
    else
        printf("Test failed.\n");
}

int main(int argc, char* argv[])
{
    CQueue<char> queue;

    queue.appendTail('a');
    queue.appendTail('b');
    queue.appendTail('c');

    char head = queue.deleteHead();
    Test(head, 'a');

    head = queue.deleteHead();
    Test(head, 'b');

    queue.appendTail('d');
    head = queue.deleteHead();
    Test(head, 'c');

    queue.appendTail('e');
    head = queue.deleteHead();
    Test(head, 'd');

    head = queue.deleteHead();
    Test(head, 'e');

    return 0;
}
```


### 10_Fibonacci

// 面试题10：斐波那契数列

// 题目：写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项。


```c++

Fibonacci.cpp

#include <cstdio>

// ====================方法1：递归====================
long long Fibonacci_Solution1(unsigned int n)
{
    if(n <= 0)
        return 0;

    if(n == 1)
        return 1;

    return Fibonacci_Solution1(n - 1) + Fibonacci_Solution1(n - 2);
}

// ====================方法2：循环====================
long long Fibonacci_Solution2(unsigned n)
{
    int result[2] = {0, 1};
    if(n < 2)
        return result[n];

    long long  fibNMinusOne = 1;
    long long  fibNMinusTwo = 0;
    long long  fibN = 0;
    for(unsigned int i = 2; i <= n; ++ i)
    {
        fibN = fibNMinusOne + fibNMinusTwo;

        fibNMinusTwo = fibNMinusOne;
        fibNMinusOne = fibN;
    }

     return fibN;
}

// ====================方法3：基于矩阵乘法====================
#include <cassert>

struct Matrix2By2
{
    Matrix2By2
    (
        long long m00 = 0, 
        long long m01 = 0, 
        long long m10 = 0, 
        long long m11 = 0
    )
    :m_00(m00), m_01(m01), m_10(m10), m_11(m11) 
    {
    }

    long long m_00;
    long long m_01;
    long long m_10;
    long long m_11;
};

Matrix2By2 MatrixMultiply
(
    const Matrix2By2& matrix1, 
    const Matrix2By2& matrix2
)
{
    return Matrix2By2(
        matrix1.m_00 * matrix2.m_00 + matrix1.m_01 * matrix2.m_10,
        matrix1.m_00 * matrix2.m_01 + matrix1.m_01 * matrix2.m_11,
        matrix1.m_10 * matrix2.m_00 + matrix1.m_11 * matrix2.m_10,
        matrix1.m_10 * matrix2.m_01 + matrix1.m_11 * matrix2.m_11);
}

Matrix2By2 MatrixPower(unsigned int n)
{
    assert(n > 0);

    Matrix2By2 matrix;
    if(n == 1)
    {
        matrix = Matrix2By2(1, 1, 1, 0);
    }
    else if(n % 2 == 0)
    {
        matrix = MatrixPower(n / 2);
        matrix = MatrixMultiply(matrix, matrix);
    }
    else if(n % 2 == 1)
    {
        matrix = MatrixPower((n - 1) / 2);
        matrix = MatrixMultiply(matrix, matrix);
        matrix = MatrixMultiply(matrix, Matrix2By2(1, 1, 1, 0));
    }

    return matrix;
}

long long Fibonacci_Solution3(unsigned int n)
{
    int result[2] = {0, 1};
    if(n < 2)
        return result[n];

    Matrix2By2 PowerNMinus2 = MatrixPower(n - 1);
    return PowerNMinus2.m_00;
}

// ====================测试代码====================
void Test(int n, int expected)
{
    if(Fibonacci_Solution1(n) == expected)
        printf("Test for %d in solution1 passed.\n", n);
    else
        printf("Test for %d in solution1 failed.\n", n);

    if(Fibonacci_Solution2(n) == expected)
        printf("Test for %d in solution2 passed.\n", n);
    else
        printf("Test for %d in solution2 failed.\n", n);

    if(Fibonacci_Solution3(n) == expected)
        printf("Test for %d in solution3 passed.\n", n);
    else
        printf("Test for %d in solution3 failed.\n", n);
}

int main(int argc, char* argv[])
{
    Test(0, 0);
    Test(1, 1);
}
```


### 11_MinNumberInRotatedArray

// 面试题11：旋转数组的最小数字

// 题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

// 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如数组

// {3, 4, 5, 1, 2}为{1, 2, 3, 4, 5}的一个旋转，该数组的最小值为1。


```c++
#include <cstdio>
#include <exception>

int MinInOrder(int* numbers, int index1, int index2);

int Min(int* numbers, int length)
{
    if(numbers == nullptr || length <= 0)
        throw new std::exception("Invalid parameters");
 
    int index1 = 0;
    int index2 = length - 1;
    int indexMid = index1;
    while(numbers[index1] >= numbers[index2])
    {
        // 如果index1和index2指向相邻的两个数，
        // 则index1指向第一个递增子数组的最后一个数字，
        // index2指向第二个子数组的第一个数字，也就是数组中的最小数字
        if(index2 - index1 == 1)
        {
            indexMid = index2;
            break;
        }
 
        // 如果下标为index1、index2和indexMid指向的三个数字相等，
        // 则只能顺序查找
        indexMid = (index1 + index2) / 2;
        if(numbers[index1] == numbers[index2] && numbers[indexMid] == numbers[index1])
            return MinInOrder(numbers, index1, index2);

        // 缩小查找范围
        if(numbers[indexMid] >= numbers[index1])
            index1 = indexMid;
        else if(numbers[indexMid] <= numbers[index2])
            index2 = indexMid;
    }
 
    return numbers[indexMid];
}

int MinInOrder(int* numbers, int index1, int index2)
{
    int result = numbers[index1];
    for(int i = index1 + 1; i <= index2; ++i)
    {
        if(result > numbers[i])
            result = numbers[i];
    }

    return result;
}

// ====================测试代码====================
void Test(int* numbers, int length, int expected)
{
    int result = 0;
    try
    {
        result = Min(numbers, length);

        for(int i = 0; i < length; ++i)
            printf("%d ", numbers[i]);

        if(result == expected)
            printf("\tpassed\n");
        else
            printf("\tfailed\n");
    }
    catch (...)
    {
        if(numbers == nullptr)
            printf("Test passed.\n");
        else
            printf("Test failed.\n");
    }
}

int main(int argc, char* argv[])
{
    // 典型输入，单调升序的数组的一个旋转
    int array1[] = { 3, 4, 5, 1, 2 };
    Test(array1, sizeof(array1) / sizeof(int), 1);

    // 有重复数字，并且重复的数字刚好的最小的数字
    int array2[] = { 3, 4, 5, 1, 1, 2 };
    Test(array2, sizeof(array2) / sizeof(int), 1);

    // 有重复数字，但重复的数字不是第一个数字和最后一个数字
    int array3[] = { 3, 4, 5, 1, 2, 2 };
    Test(array3, sizeof(array3) / sizeof(int), 1);

    // 有重复的数字，并且重复的数字刚好是第一个数字和最后一个数字
    int array4[] = { 1, 0, 1, 1, 1 };
    Test(array4, sizeof(array4) / sizeof(int), 0);

    // 单调升序数组，旋转0个元素，也就是单调升序数组本身
    int array5[] = { 1, 2, 3, 4, 5 };
    Test(array5, sizeof(array5) / sizeof(int), 1);

    // 数组中只有一个数字
    int array6[] = { 2 };
    Test(array6, sizeof(array6) / sizeof(int), 2);

    // 输入nullptr
    Test(nullptr, 0, 0);

    return 0;
}
```


### 12_StringPathInMatrix

// 面试题12：矩阵中的路径

// 题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有

// 字符的路径。路径可以从矩阵中任意一格开始，每一步可以在矩阵中向左、右、

// 上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入

// 该格子。例如在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字

// 母用下划线标出）。但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个

// 字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

// A B T G

// C F C S

// J D E H


```c++
#include <cstdio>
#include <string>
#include <stack>

using namespace std;

bool hasPathCore(const char* matrix, int rows, int cols, int row, int col, const char* str, int& pathLength, bool* visited);

bool hasPath(const char* matrix, int rows, int cols, const char* str)
{
    if(matrix == nullptr || rows < 1 || cols < 1 || str == nullptr)
        return false;

    bool *visited = new bool[rows * cols];
    memset(visited, 0, rows * cols);

    int pathLength = 0;
    for(int row = 0; row < rows; ++row)
    {
        for(int col = 0; col < cols; ++col)
        {
            if(hasPathCore(matrix, rows, cols, row, col, str,
                pathLength, visited))
            {
                return true;
            }
        }
    }

    delete[] visited;

    return false;
}

bool hasPathCore(const char* matrix, int rows, int cols, int row,
    int col, const char* str, int& pathLength, bool* visited)
{
    if(str[pathLength] == '\0')
        return true;

    bool hasPath = false;
    if(row >= 0 && row < rows && col >= 0 && col < cols
        && matrix[row * cols + col] == str[pathLength]
        && !visited[row * cols + col])
    {
        ++pathLength;
        visited[row * cols + col] = true;

        hasPath = hasPathCore(matrix, rows, cols, row, col - 1,
            str, pathLength, visited)
            || hasPathCore(matrix, rows, cols, row - 1, col,
                str, pathLength, visited)
            || hasPathCore(matrix, rows, cols, row, col + 1,
                str, pathLength, visited)
            || hasPathCore(matrix, rows, cols, row + 1, col,
                str, pathLength, visited);

        if(!hasPath)
        {
            --pathLength;
            visited[row * cols + col] = false;
        }
    }

    return hasPath;
}

// ====================测试代码====================
void Test(const char* testName, const char* matrix, int rows, int cols, const char* str, bool expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    if(hasPath(matrix, rows, cols, str) == expected)
        printf("Passed.\n");
    else
        printf("FAILED.\n");
}

//ABTG
//CFCS
//JDEH

//BFCE
void Test1()
{
    const char* matrix = "ABTGCFCSJDEH";
    const char* str = "BFCE";

    Test("Test1", (const char*) matrix, 3, 4, str, true);
}

//ABCE
//SFCS
//ADEE

//SEE
void Test2()
{
    const char* matrix = "ABCESFCSADEE";
    const char* str = "SEE";

    Test("Test2", (const char*) matrix, 3, 4, str, true);
}
```


### 13_RobotMove

// 面试题13：机器人的运动范围

// 题目：地上有一个m行n列的方格。一个机器人从坐标(0, 0)的格子开始移动，它

// 每一次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标的数位之和

// 大于k的格子。例如，当k为18时，机器人能够进入方格(35, 37)，因为3+5+3+7=18。

// 但它不能进入方格(35, 38)，因为3+5+3+8=19。请问该机器人能够到达多少个格子？


```c++
#include <cstdio>

int movingCountCore(int threshold, int rows, int cols, int row, int col, bool* visited);
bool check(int threshold, int rows, int cols, int row, int col, bool* visited);
int getDigitSum(int number);

int movingCount(int threshold, int rows, int cols)
{
    if(threshold < 0 || rows <= 0 || cols <= 0)
        return 0;

    bool *visited = new bool[rows * cols];
    for(int i = 0; i < rows * cols; ++i)
        visited[i] = false;

    int count = movingCountCore(threshold, rows, cols,
        0, 0, visited);

    delete[] visited;

    return count;
}

int movingCountCore(int threshold, int rows, int cols, int row,
    int col, bool* visited)
{
    int count = 0;
    if(check(threshold, rows, cols, row, col, visited))
    {
        visited[row * cols + col] = true;

        count = 1 + movingCountCore(threshold, rows, cols,
            row - 1, col, visited)
            + movingCountCore(threshold, rows, cols,
                row, col - 1, visited)
            + movingCountCore(threshold, rows, cols,
                row + 1, col, visited)
            + movingCountCore(threshold, rows, cols,
                row, col + 1, visited);
    }

    return count;
}

bool check(int threshold, int rows, int cols, int row, int col,
    bool* visited)
{
    if(row >= 0 && row < rows && col >= 0 && col < cols
        && getDigitSum(row) + getDigitSum(col) <= threshold
        && !visited[row* cols + col])
        return true;

    return false;
}

int getDigitSum(int number)
{
    int sum = 0;
    while(number > 0)
    {
        sum += number % 10;
        number /= 10;
    }

    return sum;
}

// ====================测试代码====================
void test(char* testName, int threshold, int rows, int cols, int expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    if(movingCount(threshold, rows, cols) == expected)
        printf("Passed.\n");
    else
        printf("FAILED.\n");
}

// 方格多行多列
void test1()
{
    test("Test1", 5, 10, 10, 21);
}

// 方格多行多列
void test2()
{
    test("Test2", 15, 20, 20, 359);
}
```

### 14_CuttingRope

// 面试题14：剪绳子

// 题目：给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m≥1）。

// 每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]*k[1]*…*k[m]可能的最大乘

// 积是多少？例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此

// 时得到最大的乘积18。


```
#include <iostream>
#include <cmath>

// ====================动态规划====================
int maxProductAfterCutting_solution1(int length)
{
    if(length < 2)
        return 0;
    if(length == 2)
        return 1;
    if(length == 3)
        return 2;

    int* products = new int[length + 1];
    products[0] = 0;
    products[1] = 1;
    products[2] = 2;
    products[3] = 3;

    int max = 0;
    for(int i = 4; i <= length; ++i)
    {
        max = 0;
        for(int j = 1; j <= i / 2; ++j)
        {
            int product = products[j] * products[i - j];
            if(max < product)
                max = product;

            products[i] = max;
        }
    }

    max = products[length];
    delete[] products;

    return max;
}

// ====================贪婪算法====================
int maxProductAfterCutting_solution2(int length)
{
    if(length < 2)
        return 0;
    if(length == 2)
        return 1;
    if(length == 3)
        return 2;

    // 尽可能多地减去长度为3的绳子段
    int timesOf3 = length / 3;

    // 当绳子最后剩下的长度为4的时候，不能再剪去长度为3的绳子段。
    // 此时更好的方法是把绳子剪成长度为2的两段，因为2*2 > 3*1。
    if(length - timesOf3 * 3 == 1)
        timesOf3 -= 1;

    int timesOf2 = (length - timesOf3 * 3) / 2;

    return (int) (pow(3, timesOf3)) * (int) (pow(2, timesOf2));
}

// ====================测试代码====================
void test(const char* testName, int length, int expected)
{
    int result1 = maxProductAfterCutting_solution1(length);
    if(result1 == expected)
        std::cout << "Solution1 for " << testName << " passed." << std::endl;
    else
        std::cout << "Solution1 for " << testName << " FAILED." << std::endl;

    int result2 = maxProductAfterCutting_solution2(length);
    if(result2 == expected)
        std::cout << "Solution2 for " << testName << " passed." << std::endl;
    else
        std::cout << "Solution2 for " << testName << " FAILED." << std::endl;
}

void test1()
{
    int length = 1;
    int expected = 0;
    test("test1", length, expected);
}
```


### 15_NumberOf1InBinary

// 面试题15：二进制中1的个数

// 题目：请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如

// 把9表示成二进制是1001，有2位是1。因此如果输入9，该函数输出2。


```c++
#include <cstdio>

int NumberOf1_Solution1(int n)
{
    int count = 0;
    unsigned int flag = 1;
    while (flag)
    {
        if (n & flag)
            count++;

        flag = flag << 1;
    }

    return count;
}

int NumberOf1_Solution2(int n)
{
    int count = 0;

    while (n)
    {
        ++count;
        n = (n - 1) & n;
    }

    return count;
}

// ====================测试代码====================
void Test(int number, unsigned int expected)
{
    int actual = NumberOf1_Solution1(number);
    if (actual == expected)
        printf("Solution1: Test for %p passed.\n", number);
    else
        printf("Solution1: Test for %p failed.\n", number);

    actual = NumberOf1_Solution2(number);
    if (actual == expected)
        printf("Solution2: Test for %p passed.\n", number);
    else
        printf("Solution2: Test for %p failed.\n", number);

    printf("\n");
}

int main(int argc, char* argv[])
{
    // 输入0，期待的输出是0
    Test(0, 0);

    // 输入1，期待的输出是1
    Test(1, 1);

    // 输入10，期待的输出是2
    Test(10, 2);

}

```


### 16_Power

// 面试题16：数值的整数次方

// 题目：实现函数double Power(double base, int exponent)，求base的exponent

// 次方。不得使用库函数，同时不需要考虑大数问题。

```c++

#include <iostream>
#include <cmath>

bool g_InvalidInput = false;
bool equal(double num1, double num2);
double PowerWithUnsignedExponent(double base, unsigned int exponent);

double Power(double base, int exponent)
{
    g_InvalidInput = false;

    if (equal(base, 0.0) && exponent < 0)
    {
        g_InvalidInput = true;
        return 0.0;
    }

    unsigned int absExponent = (unsigned int) (exponent);
    if (exponent < 0)
        absExponent = (unsigned int) (-exponent);

    double result = PowerWithUnsignedExponent(base, absExponent);
    if (exponent < 0)
        result = 1.0 / result;

    return result;
}

/*
double PowerWithUnsignedExponent(double base, unsigned int exponent)
{
    double result = 1.0;
    
    for (int i = 1; i <= exponent; ++i)
        result *= base;
    return result;
}
*/

double PowerWithUnsignedExponent(double base, unsigned int exponent)
{
    if (exponent == 0)
        return 1;
    if (exponent == 1)
        return base;

    double result = PowerWithUnsignedExponent(base, exponent >> 1);
    result *= result;
    if ((exponent & 0x1) == 1)
        result *= base;

    return result;
}

bool equal(double num1, double num2)
{
    if ((num1 - num2 > -0.0000001) && (num1 - num2 < 0.0000001))
        return true;
    else
        return false;
}

// ====================测试代码====================
void Test(const char* testName, double base, int exponent, double expectedResult, bool expectedFlag)
{
    double result = Power(base, exponent);
    if (equal(result, expectedResult) && g_InvalidInput == expectedFlag)
        std::cout << testName << " passed" << std::endl;
    else
        std::cout << testName << " FAILED" << std::endl;
}

int main(int argc, char* argv[])
{
    // 底数、指数都为正数
    Test("Test1", 2, 3, 8, false);

    // 底数为负数、指数为正数
    Test("Test2", -2, 3, -8, false);

}
```

###   17_Print1ToMaxOfNDigits

// 面试题17：打印1到最大的n位数

// 题目：输入数字n，按顺序打印出从1最大的n位十进制数。比如输入3，则

// 打印出1、2、3一直到最大的3位数即999


```c++
#include <cstdio>
#include <memory>

void PrintNumber(char* number);
bool Increment(char* number);
void Print1ToMaxOfNDigitsRecursively(char* number, int length, int index);

// ====================方法一====================
void Print1ToMaxOfNDigits_1(int n)
{
    if (n <= 0)
        return;

    char *number = new char[n + 1];
    memset(number, '0', n);
    number[n] = '\0';

    while (!Increment(number))
    {
        PrintNumber(number);
    }

    delete[]number;
}

// 字符串number表示一个数字，在 number上增加1
// 如果做加法溢出，则返回true；否则为false
bool Increment(char* number)
{
    bool isOverflow = false;
    int nTakeOver = 0;
    int nLength = strlen(number);

    for (int i = nLength - 1; i >= 0; i--)
    {
        int nSum = number[i] - '0' + nTakeOver;
        if (i == nLength - 1)
            nSum++;

        if (nSum >= 10)
        {
            if (i == 0)
                isOverflow = true;
            else
            {
                nSum -= 10;
                nTakeOver = 1;
                number[i] = '0' + nSum;
            }
        }
        else
        {
            number[i] = '0' + nSum;
            break;
        }
    }

    return isOverflow;
}

// ====================方法二====================
void Print1ToMaxOfNDigits_2(int n)
{
    if (n <= 0)
        return;

    char* number = new char[n + 1];
    number[n] = '\0';

    for (int i = 0; i < 10; ++i)
    {
        number[0] = i + '0';
        Print1ToMaxOfNDigitsRecursively(number, n, 0);
    }

    delete[] number;
}

void Print1ToMaxOfNDigitsRecursively(char* number, int length, int index)
{
    if (index == length - 1)
    {
        PrintNumber(number);
        return;
    }

    for (int i = 0; i < 10; ++i)
    {
        number[index + 1] = i + '0';
        Print1ToMaxOfNDigitsRecursively(number, length, index + 1);
    }
}

// ====================公共函数====================
// 字符串number表示一个数字，数字有若干个0开头
// 打印出这个数字，并忽略开头的0
void PrintNumber(char* number)
{
    bool isBeginning0 = true;
    int nLength = strlen(number);

    for (int i = 0; i < nLength; ++i)
    {
        if (isBeginning0 && number[i] != '0')
            isBeginning0 = false;

        if (!isBeginning0)
        {
            printf("%c", number[i]);
        }
    }

    printf("\t");
}

// ====================测试代码====================
void Test(int n)
{
    printf("Test for %d begins:\n", n);

    Print1ToMaxOfNDigits_1(n);
    Print1ToMaxOfNDigits_2(n);

    printf("\nTest for %d ends.\n", n);
}

int main(int argc, char* argv[])
{
    Test(1);
    Test(2);
    Test(3);
    Test(0);
    Test(-1);

    return 0;
}
```


###  18_01_DeleteNodeInList

// 面试题18（一）：在O(1)时间删除链表结点

// 题目：给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除该

// 结点。


```c++
#include <cstdio>
#include "..\Utilities\List.h"

void DeleteNode(ListNode** pListHead, ListNode* pToBeDeleted)
{
    if(!pListHead || !pToBeDeleted)
        return;

    // 要删除的结点不是尾结点
    if(pToBeDeleted->m_pNext != nullptr)
    {
        ListNode* pNext = pToBeDeleted->m_pNext;
        pToBeDeleted->m_nValue = pNext->m_nValue;
        pToBeDeleted->m_pNext = pNext->m_pNext;
 
        delete pNext;
        pNext = nullptr;
    }
    // 链表只有一个结点，删除头结点（也是尾结点）
    else if(*pListHead == pToBeDeleted)
    {
        delete pToBeDeleted;
        pToBeDeleted = nullptr;
        *pListHead = nullptr;
    }
    // 链表中有多个结点，删除尾结点
    else
    {
        ListNode* pNode = *pListHead;
        while(pNode->m_pNext != pToBeDeleted)
        {
            pNode = pNode->m_pNext;            
        }
 
        pNode->m_pNext = nullptr;
        delete pToBeDeleted;
        pToBeDeleted = nullptr;
    }
}

// ====================测试代码====================
void Test(ListNode* pListHead, ListNode* pNode)
{
    printf("The original list is: \n");
    PrintList(pListHead);

    printf("The node to be deleted is: \n");
    PrintListNode(pNode);

    DeleteNode(&pListHead, pNode);
    
    printf("The result list is: \n");
    PrintList(pListHead);
}

// 链表中有多个结点，删除中间的结点
void Test1()
{
    ListNode* pNode1 = CreateListNode(1);
    ListNode* pNode2 = CreateListNode(2);
    ListNode* pNode3 = CreateListNode(3);
    ListNode* pNode4 = CreateListNode(4);
    ListNode* pNode5 = CreateListNode(5);

    ConnectListNodes(pNode1, pNode2);
    ConnectListNodes(pNode2, pNode3);
    ConnectListNodes(pNode3, pNode4);
    ConnectListNodes(pNode4, pNode5);

    Test(pNode1, pNode3);

    DestroyList(pNode1);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
}
```

### 18_02_DeleteDuplicatedNode

// 面试题18（二）：删除链表中重复的结点

// 题目：在一个排序的链表中，如何删除重复的结点？例如，在图3.4（a）中重复

// 结点被删除之后，链表如图3.4（b）所示。


```c++
#include <cstdio>
#include "../Utilities/list.h"

void DeleteDuplication(ListNode** pHead)
{
    if(pHead == nullptr || *pHead == nullptr)
        return;

    ListNode* pPreNode = nullptr;
    ListNode* pNode = *pHead;
    while(pNode != nullptr)
    {
        ListNode *pNext = pNode->m_pNext;
        bool needDelete = false;
        if(pNext != nullptr && pNext->m_nValue == pNode->m_nValue)
            needDelete = true;

        if(!needDelete)
        {
            pPreNode = pNode;
            pNode = pNode->m_pNext;
        }
        else
        {
            int value = pNode->m_nValue;
            ListNode* pToBeDel = pNode;
            while(pToBeDel != nullptr && pToBeDel->m_nValue == value)
            {
                pNext = pToBeDel->m_pNext;

                delete pToBeDel;
                pToBeDel = nullptr;

                pToBeDel = pNext;
            }

            if(pPreNode == nullptr)
                *pHead = pNext;
            else
                pPreNode->m_pNext = pNext;
            pNode = pNext;
        }
    }
}

// ====================测试代码====================
void Test(char* testName, ListNode** pHead, int* expectedValues, int expectedLength)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    DeleteDuplication(pHead);

    int index = 0;
    ListNode* pNode = *pHead;
    while(pNode != nullptr && index < expectedLength)
    {
        if(pNode->m_nValue != expectedValues[index])
            break;

        pNode = pNode->m_pNext;
        index++;
    }

    if(pNode == nullptr && index == expectedLength)
        printf("Passed.\n");
    else
        printf("FAILED.\n");
}

// 某些结点是重复的
void Test1()
{
    ListNode* pNode1 = CreateListNode(1);
    ListNode* pNode2 = CreateListNode(2);
}
```


### 19_RegularExpressionsMatching

// 面试题19：正则表达式匹配

// 题目：请实现一个函数用来匹配包含'.'和'*'的正则表达式。模式中的字符'.'

// 表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题

// 中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"

// 和"ab*ac*a"匹配，但与"aa.a"及"ab*a"均不匹配。


```c++
#include <cstdio>

bool matchCore(const char* str, const char* pattern);

bool match(const char* str, const char* pattern)
{
    if(str == nullptr || pattern == nullptr)
        return false;

    return matchCore(str, pattern);
}

bool matchCore(const char* str, const char* pattern)
{
    if(*str == '\0' && *pattern == '\0')
        return true;

    if(*str != '\0' && *pattern == '\0')
        return false;

    if(*(pattern + 1) == '*')
    {
        if(*pattern == *str || (*pattern == '.' && *str != '\0'))
            // 进入有限状态机的下一个状态
            return matchCore(str + 1, pattern + 2)
            // 继续留在有限状态机的当前状态 
            || matchCore(str + 1, pattern)
            // 略过一个'*' 
            || matchCore(str, pattern + 2);
        else
            // 略过一个'*'
            return matchCore(str, pattern + 2);
    }

    if(*str == *pattern || (*pattern == '.' && *str != '\0'))
        return matchCore(str + 1, pattern + 1);

    return false;
}

// ====================测试代码====================
void Test(const char* testName, const char* string, const char* pattern, bool expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    if(match(string, pattern) == expected)
        printf("Passed.\n");
    else
        printf("FAILED.\n");
}

int main(int argc, char* argv[])
{
    Test("Test01", "", "", true);
    Test("Test02", "", ".*", true);
    Test("Test03", "", ".", false);

}
```

### 20_NumericStrings

// 面试题20：表示数值的字符串

// 题目：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，

// 字符串“+100”、“5e2”、“-123”、“3.1416”及“-1E-16”都表示数值，但“12e”、

// “1a3.14”、“1.2.3”、“+-5”及“12e+5.4”都不是


```c++
#include <stdio.h>

bool scanUnsignedInteger(const char** str);
bool scanInteger(const char** str);

// 数字的格式可以用A[.[B]][e|EC]或者.B[e|EC]表示，其中A和C都是
// 整数（可以有正负号，也可以没有），而B是一个无符号整数
bool isNumeric(const char* str)
{
    if(str == nullptr)
        return false;

    bool numeric = scanInteger(&str);

    // 如果出现'.'，接下来是数字的小数部分
    if(*str == '.')
    {
        ++str;

        // 下面一行代码用||的原因：
        // 1. 小数可以没有整数部分，例如.123等于0.123；
        // 2. 小数点后面可以没有数字，例如233.等于233.0；
        // 3. 当然小数点前面和后面可以有数字，例如233.666
        numeric = scanUnsignedInteger(&str) || numeric;
    }

    // 如果出现'e'或者'E'，接下来跟着的是数字的指数部分
    if(*str == 'e' || *str == 'E')
    {
        ++str;

        // 下面一行代码用&&的原因：
        // 1. 当e或E前面没有数字时，整个字符串不能表示数字，例如.e1、e1；
        // 2. 当e或E后面没有整数时，整个字符串不能表示数字，例如12e、12e+5.4
        numeric = numeric && scanInteger(&str);
    }

    return numeric && *str == '\0';
}

bool scanUnsignedInteger(const char** str)
{
    const char* before = *str;
    while(**str != '\0' && **str >= '0' && **str <= '9')
        ++(*str);

    // 当str中存在若干0-9的数字时，返回true
    return *str > before;
}

// 整数的格式可以用[+|-]B表示, 其中B为无符号整数
bool scanInteger(const char** str)
{
    if(**str == '+' || **str == '-')
        ++(*str);
    return scanUnsignedInteger(str);
}

// ====================测试代码====================
void Test(const char* testName, const char* str, bool expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    if(isNumeric(str) == expected)
        printf("Passed.\n");
    else
        printf("FAILED.\n");
}


int main(int argc, char* argv[])
{
    Test("Test1", "100", true);
    Test("Test2", "123.45e+6", true);
    Test("Test3", "+500", true);
}
```

### 21_ReorderArray

// 面试题21：调整数组顺序使奇数位于偶数前面

// 题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有

// 奇数位于数组的前半部分，所有偶数位于数组的后半部分。



```c++
#include <cstdio>

void Reorder(int *pData, unsigned int length, bool (*func)(int));
bool isEven(int n);

// ====================方法一====================
void ReorderOddEven_1(int *pData, unsigned int length)
{
    if(pData == nullptr || length == 0)
        return;

    int *pBegin = pData;
    int *pEnd = pData + length - 1;

    while(pBegin < pEnd)
    {
        // 向后移动pBegin，直到它指向偶数
        while(pBegin < pEnd && (*pBegin & 0x1) != 0)
            pBegin ++;

        // 向前移动pEnd，直到它指向奇数
        while(pBegin < pEnd && (*pEnd & 0x1) == 0)
            pEnd --;

        if(pBegin < pEnd)
        {
            int temp = *pBegin;
            *pBegin = *pEnd;
            *pEnd = temp;
        }
    }
}

// ====================方法二====================
void ReorderOddEven_2(int *pData, unsigned int length)
{
    Reorder(pData, length, isEven);
}

void Reorder(int *pData, unsigned int length, bool (*func)(int))
{
    if(pData == nullptr || length == 0)
        return;

    int *pBegin = pData;
    int *pEnd = pData + length - 1;

    while(pBegin < pEnd) 
    {
        // 向后移动pBegin
        while(pBegin < pEnd && !func(*pBegin))
            pBegin ++;

        // 向前移动pEnd
        while(pBegin < pEnd && func(*pEnd))
            pEnd --;

        if(pBegin < pEnd)
        {
            int temp = *pBegin;
            *pBegin = *pEnd;
            *pEnd = temp;
        }
    }
}

bool isEven(int n)
{
    return (n & 1) == 0;
}

// ====================测试代码====================
void PrintArray(int numbers[], int length)
{
    if(length < 0)
        return;

    for(int i = 0; i < length; ++i)
        printf("%d\t", numbers[i]);

    printf("\n");
}

void Test(char* testName, int numbers[], int length)
{
    if(testName != nullptr)
        printf("%s begins:\n", testName);

    int* copy = new int[length];
    for(int i = 0; i < length; ++i)
    {
        copy[i] = numbers[i];
    }

    printf("Test for solution 1:\n");
    PrintArray(numbers, length);
    ReorderOddEven_1(numbers, length);
    PrintArray(numbers, length);

    printf("Test for solution 2:\n");
    PrintArray(copy, length);
    ReorderOddEven_2(copy, length);
    PrintArray(copy, length);

    delete[] copy;
}

void Test1()
{
    int numbers[] = {1, 2, 3, 4, 5, 6, 7};
    Test("Test1", numbers, sizeof(numbers)/sizeof(int));
}

void Test2()
{
    int numbers[] = {2, 4, 6, 1, 3, 5, 7};
    Test("Test2", numbers, sizeof(numbers)/sizeof(int));
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
}
```

### 22_KthNodeFromEnd

// 面试题22：链表中倒数第k个结点

// 题目：输入一个链表，输出该链表中倒数第k个结点。为了符合大多数人的习惯，

// 本题从1开始计数，即链表的尾结点是倒数第1个结点。例如一个链表有6个结点，

// 从头结点开始它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个结点是

// 值为4的结点。


```c++
#include <cstdio>
#include "..\Utilities\List.h"

ListNode* FindKthToTail(ListNode* pListHead, unsigned int k)
{
    if(pListHead == nullptr || k == 0)
        return nullptr;

    ListNode *pAhead = pListHead;
    ListNode *pBehind = nullptr;

    for(unsigned int i = 0; i < k - 1; ++ i)
    {
        if(pAhead->m_pNext != nullptr)
            pAhead = pAhead->m_pNext;
        else
        {
            return nullptr;
        }
    }

    pBehind = pListHead;
    while(pAhead->m_pNext != nullptr)
    {
        pAhead = pAhead->m_pNext;
        pBehind = pBehind->m_pNext;
    }

    return pBehind;
}

// ====================测试代码====================
// 测试要找的结点在链表中间
void Test1()
{
    printf("=====Test1 starts:=====\n");
    ListNode* pNode1 = CreateListNode(1);
    ListNode* pNode2 = CreateListNode(2);
    ListNode* pNode3 = CreateListNode(3);
    ListNode* pNode4 = CreateListNode(4);
    ListNode* pNode5 = CreateListNode(5);

    ConnectListNodes(pNode1, pNode2);
    ConnectListNodes(pNode2, pNode3);
    ConnectListNodes(pNode3, pNode4);
    ConnectListNodes(pNode4, pNode5);

    printf("expected result: 4.\n");
    ListNode* pNode = FindKthToTail(pNode1, 2);
    PrintListNode(pNode);

    DestroyList(pNode1);
}
```

### 23_EntryNodeInListLoop

// 面试题23：链表中环的入口结点

// 题目：一个链表中包含环，如何找出环的入口结点？例如，在图3.8的链表中，

// 环的入口结点是结点3。

```c++
#include <cstdio>
#include "../Utilities/list.h"

ListNode* MeetingNode(ListNode* pHead)
{
    if(pHead == nullptr)
        return nullptr;

    ListNode* pSlow = pHead->m_pNext;
    if(pSlow == nullptr)
        return nullptr;

    ListNode* pFast = pSlow->m_pNext;
    while(pFast != nullptr && pSlow != nullptr)
    {
        if(pFast == pSlow)
            return pFast;

        pSlow = pSlow->m_pNext;

        pFast = pFast->m_pNext;
        if(pFast != nullptr)
            pFast = pFast->m_pNext;
    }

    return nullptr;
}

ListNode* EntryNodeOfLoop(ListNode* pHead)
{
    ListNode* meetingNode = MeetingNode(pHead);
    if(meetingNode == nullptr)
        return nullptr;

    // 得到环中结点的数目
    int nodesInLoop = 1;
    ListNode* pNode1 = meetingNode;
    while(pNode1->m_pNext != meetingNode)
    {
        pNode1 = pNode1->m_pNext;
        ++nodesInLoop;
    }

    // 先移动pNode1，次数为环中结点的数目
    pNode1 = pHead;
    for(int i = 0; i < nodesInLoop; ++i)
        pNode1 = pNode1->m_pNext;

    // 再移动pNode1和pNode2
    ListNode* pNode2 = pHead;
    while(pNode1 != pNode2)
    {
        pNode1 = pNode1->m_pNext;
        pNode2 = pNode2->m_pNext;
    }

    return pNode1;
}

// ==================== Test Code ====================
void Test(char* testName, ListNode* pHead, ListNode* entryNode)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    if(EntryNodeOfLoop(pHead) == entryNode)
        printf("Passed.\n");
    else
        printf("FAILED.\n");
}

// A list has a node, without a loop
void Test1()
{
    ListNode* pNode1 = CreateListNode(1);

    Test("Test1", pNode1, nullptr);

    DestroyList(pNode1);
}

// A list has a node, with a loop
void Test2()
{
    ListNode* pNode1 = CreateListNode(1);
    ConnectListNodes(pNode1, pNode1);

    Test("Test2", pNode1, pNode1);

    delete pNode1;
    pNode1 = nullptr;
}
```

###   24_ReverseList

// 面试题24：反转链表

// 题目：定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的

// 头结点。

```c++
#include <cstdio>
#include "..\Utilities\List.h"

ListNode* ReverseList(ListNode* pHead)
{
    ListNode* pReversedHead = nullptr;
    ListNode* pNode = pHead;
    ListNode* pPrev = nullptr;
    while(pNode != nullptr)
    {
        ListNode* pNext = pNode->m_pNext;

        if(pNext == nullptr)
            pReversedHead = pNode;

        pNode->m_pNext = pPrev;

        pPrev = pNode;
        pNode = pNext;
    }

    return pReversedHead;
}

// ====================测试代码====================
ListNode* Test(ListNode* pHead)
{
    printf("The original list is: \n");
    PrintList(pHead);

    ListNode* pReversedHead = ReverseList(pHead);

    printf("The reversed list is: \n");
    PrintList(pReversedHead);

    return pReversedHead;
}

// 输入的链表有多个结点
void Test1()
{
    ListNode* pNode1 = CreateListNode(1);
    ListNode* pNode2 = CreateListNode(2);
    ListNode* pNode3 = CreateListNode(3);
    ListNode* pNode4 = CreateListNode(4);
    ListNode* pNode5 = CreateListNode(5);

    ConnectListNodes(pNode1, pNode2);
    ConnectListNodes(pNode2, pNode3);
    ConnectListNodes(pNode3, pNode4);
    ConnectListNodes(pNode4, pNode5);

    ListNode* pReversedHead = Test(pNode1);

    DestroyList(pReversedHead);
}


int main(int argc, char* argv[])
{
    Test1();
}
```


### 25_MergeSortedLists


// 面试题25：合并两个排序的链表

// 题目：输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按

// 照递增排序的。例如输入图3.11中的链表1和链表2，则合并之后的升序链表如链

// 表3所示。

```c++
#include <cstdio>
#include "..\Utilities\List.h"

ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
{
    if(pHead1 == nullptr)
        return pHead2;
    else if(pHead2 == nullptr)
        return pHead1;

    ListNode* pMergedHead = nullptr;

    if(pHead1->m_nValue < pHead2->m_nValue)
    {
        pMergedHead = pHead1;
        pMergedHead->m_pNext = Merge(pHead1->m_pNext, pHead2);
    }
    else
    {
        pMergedHead = pHead2;
        pMergedHead->m_pNext = Merge(pHead1, pHead2->m_pNext);
    }

    return pMergedHead;
}

// ====================测试代码====================
ListNode* Test(char* testName, ListNode* pHead1, ListNode* pHead2)
{
    if(testName != nullptr)
        printf("%s begins:\n", testName);

    printf("The first list is:\n");
    PrintList(pHead1);

    printf("The second list is:\n");
    PrintList(pHead2);

    printf("The merged list is:\n");
    ListNode* pMergedHead = Merge(pHead1, pHead2);
    PrintList(pMergedHead);
    
    printf("\n\n");

    return pMergedHead;
}

// list1: 1->3->5
// list2: 2->4->6
void Test1()
{
    ListNode* pNode1 = CreateListNode(1);
    ListNode* pNode3 = CreateListNode(3);
    ListNode* pNode5 = CreateListNode(5);

    ConnectListNodes(pNode1, pNode3);
    ConnectListNodes(pNode3, pNode5);

    ListNode* pNode2 = CreateListNode(2);
    ListNode* pNode4 = CreateListNode(4);
    ListNode* pNode6 = CreateListNode(6);

    ConnectListNodes(pNode2, pNode4);
    ConnectListNodes(pNode4, pNode6);

    ListNode* pMergedHead = Test("Test1", pNode1, pNode2);

    DestroyList(pMergedHead);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
}
```

### 26_SubstructureInTree

// 面试题26：树的子结构

// 题目：输入两棵二叉树A和B，判断B是不是A的子结构。

```c++
#include <cstdio>

struct BinaryTreeNode
{
    double                 m_dbValue;
    BinaryTreeNode*        m_pLeft;
    BinaryTreeNode*        m_pRight;
};

bool DoesTree1HaveTree2(BinaryTreeNode* pRoot1, BinaryTreeNode* pRoot2);
bool Equal(double num1, double num2);

bool HasSubtree(BinaryTreeNode* pRoot1, BinaryTreeNode* pRoot2)
{
    bool result = false;

    if(pRoot1 != nullptr && pRoot2 != nullptr)
    {
        if(Equal(pRoot1->m_dbValue, pRoot2->m_dbValue))
            result = DoesTree1HaveTree2(pRoot1, pRoot2);
        if(!result)
            result = HasSubtree(pRoot1->m_pLeft, pRoot2);
        if(!result)
            result = HasSubtree(pRoot1->m_pRight, pRoot2);
    }

    return result;
}

bool DoesTree1HaveTree2(BinaryTreeNode* pRoot1, BinaryTreeNode* pRoot2)
{
    if(pRoot2 == nullptr)
        return true;

    if(pRoot1 == nullptr)
        return false;

    if(!Equal(pRoot1->m_dbValue, pRoot2->m_dbValue))
        return false;

    return DoesTree1HaveTree2(pRoot1->m_pLeft, pRoot2->m_pLeft) &&
        DoesTree1HaveTree2(pRoot1->m_pRight, pRoot2->m_pRight);
}

bool Equal(double num1, double num2)
{
    if((num1 - num2 > -0.0000001) && (num1 - num2 < 0.0000001))
        return true;
    else
        return false;
}

// ====================辅助测试代码====================
BinaryTreeNode* CreateBinaryTreeNode(double dbValue)
{
    BinaryTreeNode* pNode = new BinaryTreeNode();
    pNode->m_dbValue = dbValue;
    pNode->m_pLeft = nullptr;
    pNode->m_pRight = nullptr;

    return pNode;
}

void ConnectTreeNodes(BinaryTreeNode* pParent, BinaryTreeNode* pLeft, BinaryTreeNode* pRight)
{
    if(pParent != nullptr)
    {
        pParent->m_pLeft = pLeft;
        pParent->m_pRight = pRight;
    }
}

void DestroyTree(BinaryTreeNode* pRoot)
{
    if(pRoot != nullptr)
    {
        BinaryTreeNode* pLeft = pRoot->m_pLeft;
        BinaryTreeNode* pRight = pRoot->m_pRight;

        delete pRoot;
        pRoot = nullptr;

        DestroyTree(pLeft);
        DestroyTree(pRight);
    }
}

// ====================测试代码====================
void Test(char* testName, BinaryTreeNode* pRoot1, BinaryTreeNode* pRoot2, bool expected)
{
    if(HasSubtree(pRoot1, pRoot2) == expected)
        printf("%s passed.\n", testName);
    else
        printf("%s failed.\n", testName);
}

// 树中结点含有分叉，树B是树A的子结构
//                  8                8
//              /       \           / \
//             8         7         9   2
//           /   \
//          9     2
//               / \
//              4   7
void Test1()
{
    BinaryTreeNode* pNodeA1 = CreateBinaryTreeNode(8);
    BinaryTreeNode* pNodeA2 = CreateBinaryTreeNode(8);
    BinaryTreeNode* pNodeA3 = CreateBinaryTreeNode(7);
    BinaryTreeNode* pNodeA4 = CreateBinaryTreeNode(9);
    BinaryTreeNode* pNodeA5 = CreateBinaryTreeNode(2);
    BinaryTreeNode* pNodeA6 = CreateBinaryTreeNode(4);
    BinaryTreeNode* pNodeA7 = CreateBinaryTreeNode(7);

    ConnectTreeNodes(pNodeA1, pNodeA2, pNodeA3);
    ConnectTreeNodes(pNodeA2, pNodeA4, pNodeA5);
    ConnectTreeNodes(pNodeA5, pNodeA6, pNodeA7);

    BinaryTreeNode* pNodeB1 = CreateBinaryTreeNode(8);
    BinaryTreeNode* pNodeB2 = CreateBinaryTreeNode(9);
    BinaryTreeNode* pNodeB3 = CreateBinaryTreeNode(2);

    ConnectTreeNodes(pNodeB1, pNodeB2, pNodeB3);

    Test("Test1", pNodeA1, pNodeB1, true);

    DestroyTree(pNodeA1);
    DestroyTree(pNodeB1);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
}
```

### 27_MirrorOfBinaryTree

// 面试题27：二叉树的镜像

// 题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像。

```c++
#include <cstdio>
#include "..\Utilities\BinaryTree.h"
#include <stack>

void MirrorRecursively(BinaryTreeNode *pNode)
{
    if((pNode == nullptr) || (pNode->m_pLeft == nullptr && pNode->m_pRight))
        return;

    BinaryTreeNode *pTemp = pNode->m_pLeft;
    pNode->m_pLeft = pNode->m_pRight;
    pNode->m_pRight = pTemp;
    
    if(pNode->m_pLeft)
        MirrorRecursively(pNode->m_pLeft);  

    if(pNode->m_pRight)
        MirrorRecursively(pNode->m_pRight); 
}

void MirrorIteratively(BinaryTreeNode* pRoot)
{
    if(pRoot == nullptr)
        return;

    std::stack<BinaryTreeNode*> stackTreeNode;
    stackTreeNode.push(pRoot);

    while(stackTreeNode.size() > 0)
    {
        BinaryTreeNode *pNode = stackTreeNode.top();
        stackTreeNode.pop();

        BinaryTreeNode *pTemp = pNode->m_pLeft;
        pNode->m_pLeft = pNode->m_pRight;
        pNode->m_pRight = pTemp;

        if(pNode->m_pLeft)
            stackTreeNode.push(pNode->m_pLeft);

        if(pNode->m_pRight)
            stackTreeNode.push(pNode->m_pRight);
    }
}

// ====================测试代码====================
// 测试完全二叉树：除了叶子节点，其他节点都有两个子节点
//            8
//        6      10
//       5 7    9  11
void Test1()
{
    printf("=====Test1 starts:=====\n");
    BinaryTreeNode* pNode8 = CreateBinaryTreeNode(8);
    BinaryTreeNode* pNode6 = CreateBinaryTreeNode(6);
    BinaryTreeNode* pNode10 = CreateBinaryTreeNode(10);
    BinaryTreeNode* pNode5 = CreateBinaryTreeNode(5);
    BinaryTreeNode* pNode7 = CreateBinaryTreeNode(7);
    BinaryTreeNode* pNode9 = CreateBinaryTreeNode(9);
    BinaryTreeNode* pNode11 = CreateBinaryTreeNode(11);

    ConnectTreeNodes(pNode8, pNode6, pNode10);
    ConnectTreeNodes(pNode6, pNode5, pNode7);
    ConnectTreeNodes(pNode10, pNode9, pNode11);

    PrintTree(pNode8);

}


int main(int argc, char* argv[])
{
    Test1();
    Test2();
 }
```

### 28_SymmetricalBinaryTree
 
// 面试题28：对称的二叉树

// 题目：请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和

// 它的镜像一样，那么它是对称的。 

```c++
#include <cstdio>
#include "../Utilities/BinaryTree.h"

bool isSymmetrical(BinaryTreeNode* pRoot1, BinaryTreeNode* pRoot2);

bool isSymmetrical(BinaryTreeNode* pRoot)
{
    return isSymmetrical(pRoot, pRoot);
}

bool isSymmetrical(BinaryTreeNode* pRoot1, BinaryTreeNode* pRoot2)
{
    if(pRoot1 == nullptr && pRoot2 == nullptr)
        return true;

    if(pRoot1 == nullptr || pRoot2 == nullptr)
        return false;

    if(pRoot1->m_nValue != pRoot2->m_nValue)
        return false;

    return isSymmetrical(pRoot1->m_pLeft, pRoot2->m_pRight)
        && isSymmetrical(pRoot1->m_pRight, pRoot2->m_pLeft);
}

// ====================测试代码====================
void Test(char* testName, BinaryTreeNode* pRoot, bool expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    if(isSymmetrical(pRoot) == expected)
        printf("Passed.\n");
    else
        printf("FAILED.\n");
}

//            8
//        6      6
//       5 7    7 5
void Test1()
{
    BinaryTreeNode* pNode8 = CreateBinaryTreeNode(8);
    BinaryTreeNode* pNode61 = CreateBinaryTreeNode(6);
    BinaryTreeNode* pNode62 = CreateBinaryTreeNode(6);
    BinaryTreeNode* pNode51 = CreateBinaryTreeNode(5);
    BinaryTreeNode* pNode71 = CreateBinaryTreeNode(7);
    BinaryTreeNode* pNode72 = CreateBinaryTreeNode(7);
    BinaryTreeNode* pNode52 = CreateBinaryTreeNode(5);

    ConnectTreeNodes(pNode8, pNode61, pNode62);
    ConnectTreeNodes(pNode61, pNode51, pNode71);
    ConnectTreeNodes(pNode62, pNode72, pNode52);

    Test("Test1", pNode8, true);

    DestroyTree(pNode8);
}

void main(int argc, char* argv[])
{
    Test1();
    Test2();
}
```

###  29_PrintMatrix


// 面试题29：顺时针打印矩阵

// 题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

```c++
#include <cstdio>

void PrintMatrixInCircle(int** numbers, int columns, int rows, int start);
void printNumber(int number);

void PrintMatrixClockwisely(int** numbers, int columns, int rows)
{
    if(numbers == nullptr || columns <= 0 || rows <= 0)
        return;

    int start = 0;

    while(columns > start * 2 && rows > start * 2)
    {
        PrintMatrixInCircle(numbers, columns, rows, start);

        ++start;
    }
}

void PrintMatrixInCircle(int** numbers, int columns, int rows, int start)
{
    int endX = columns - 1 - start;
    int endY = rows - 1 - start;

    // 从左到右打印一行
    for(int i = start; i <= endX; ++i)
    {
        int number = numbers[start][i];
        printNumber(number);
    }

    // 从上到下打印一列
    if(start < endY)
    {
        for(int i = start + 1; i <= endY; ++i)
        {
            int number = numbers[i][endX];
            printNumber(number);
        }
    }

    // 从右到左打印一行
    if(start < endX && start < endY)
    {
        for(int i = endX - 1; i >= start; --i)
        {
            int number = numbers[endY][i];
            printNumber(number);
        }
    }

    // 从下到上打印一行
    if(start < endX && start < endY - 1)
    {
        for(int i = endY - 1; i >= start + 1; --i)
        {
            int number = numbers[i][start];
            printNumber(number);
        }
    }
}

void printNumber(int number)
{
    printf("%d\t", number);
}

// ====================测试代码====================
void Test(int columns, int rows)
{
    printf("Test Begin: %d columns, %d rows.\n", columns, rows);

    if(columns < 1 || rows < 1)
        return;

    int** numbers = new int*[rows];
    for(int i = 0; i < rows; ++i)
    {
        numbers[i] = new int[columns];
        for(int j = 0; j < columns; ++j)
        {
            numbers[i][j] = i * columns + j + 1;
        }
    }

    PrintMatrixClockwisely(numbers, columns, rows);
    printf("\n");

    for(int i = 0; i < rows; ++i)
        delete[] (int*)numbers[i];

    delete[] numbers;
}

int main(int argc, char* argv[])
{
    /*
    1    
    */
    Test(1, 1);

    /*
    1    2
    3    4
    */
    Test(2, 2);

}
```

### 30_MinInStack

// 面试题30：包含min函数的栈

// 题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min

// 函数。在该栈中，调用min、push及pop的时间复杂度都是O(1)。

```c++
StackWithMin.h

#pragma once

#include <stack>
#include <assert.h>

template <typename T> class StackWithMin
{
public:
    StackWithMin() {}
    virtual ~StackWithMin() {}

    T& top();
    const T& top() const;

    void push(const T& value);
    void pop();

    const T& min() const;

    bool empty() const;
    size_t size() const;

private:
    std::stack<T>   m_data;     // 数据栈，存放栈的所有元素
    std::stack<T>   m_min;      // 辅助栈，存放栈的最小元素
};

template <typename T> void StackWithMin<T>::push(const T& value)
{
    // 把新元素添加到辅助栈
    m_data.push(value);

    // 当新元素比之前的最小元素小时，把新元素插入辅助栈里；
    // 否则把之前的最小元素重复插入辅助栈里
    if(m_min.size() == 0 || value < m_min.top())
        m_min.push(value);
    else
        m_min.push(m_min.top());
}

template <typename T> void StackWithMin<T>::pop()
{
    assert(m_data.size() > 0 && m_min.size() > 0);

    m_data.pop();
    m_min.pop();
}


template <typename T> const T& StackWithMin<T>::min() const
{
    assert(m_data.size() > 0 && m_min.size() > 0);

    return m_min.top();
}

template <typename T> T& StackWithMin<T>::top()
{
    return m_data.top();
}

template <typename T> const T& StackWithMin<T>::top() const
{
    return m_data.top();
}

template <typename T> bool StackWithMin<T>::empty() const
{
    return m_data.empty();
}

template <typename T> size_t StackWithMin<T>::size() const
{
    return m_data.size();
}



MinInStack.cpp


#include <cstdio>
#include "StackWithMin.h"

void Test(const char* testName, const StackWithMin<int>& stack, int expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    if(stack.min() == expected)
        printf("Passed.\n");
    else
        printf("Failed.\n");
}



int main(int argc, char* argv[])
{
    StackWithMin<int> stack;

    stack.push(3);
    Test("Test1", stack, 3);

    stack.push(4);
    Test("Test2", stack, 3);

    stack.push(2);
    Test("Test3", stack, 2);

    stack.push(3);
    Test("Test4", stack, 2);

    stack.pop();
    Test("Test5", stack, 2);

    stack.pop();
    Test("Test6", stack, 3);

    stack.pop();
    Test("Test7", stack, 3);

    stack.push(0);
    Test("Test8", stack, 0);

    return 0;
}
```

### 31_StackPushPopOrder

// 面试题31：栈的压入、弹出序列

// 题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是

// 否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1、2、3、4、

// 5是某栈的压栈序列，序列4、5、3、2、1是该压栈序列对应的一个弹出序列，但

// 4、3、5、1、2就不可能是该压栈序列的弹出序列。

```c++
StackPushPopOrder.cpp

#include <cstdio>
#include <stack>

bool IsPopOrder(const int* pPush, const int* pPop, int nLength)
{
    bool bPossible = false;

    if(pPush != nullptr && pPop != nullptr && nLength > 0)
    {
        const int* pNextPush = pPush;
        const int* pNextPop = pPop;

        std::stack<int> stackData;

        while(pNextPop - pPop < nLength)
        {
            // 当辅助栈的栈顶元素不是要弹出的元素
            // 先压入一些数字入栈
            while(stackData.empty() || stackData.top() != *pNextPop)
            {
                // 如果所有数字都压入辅助栈了，退出循环
                if(pNextPush - pPush == nLength)
                    break;

                stackData.push(*pNextPush);

                pNextPush ++;
            }

            if(stackData.top() != *pNextPop)
                break;

            stackData.pop();
            pNextPop ++;
        }

        if(stackData.empty() && pNextPop - pPop == nLength)
            bPossible = true;
    }

    return bPossible;
}

// ====================测试代码====================
void Test(const char* testName, const int* pPush, const int* pPop, int nLength, bool expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    if(IsPopOrder(pPush, pPop, nLength) == expected)
        printf("Passed.\n");
    else
        printf("failed.\n");
}

void Test1()
{
    const int nLength = 5;
    int push[nLength] = {1, 2, 3, 4, 5};
    int pop[nLength] = {4, 5, 3, 2, 1};
    
    Test("Test1", push, pop, nLength, true);
}

void Test2()
{
    const int nLength = 5;
    int push[nLength] = {1, 2, 3, 4, 5};
    int pop[nLength] = {3, 5, 4, 2, 1};
    
    Test("Test2", push, pop, nLength, true);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
}
```


### 32_01_PrintTreeFromTopToBottom

// 面试题32（一）：不分行从上往下打印二叉树

// 题目：从上往下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印。


```c++
#include <cstdio>
#include "..\Utilities\BinaryTree.h"
#include <deque>

void PrintFromTopToBottom(BinaryTreeNode* pRoot)
{
    if(pRoot == nullptr)
        return;

    std::deque<BinaryTreeNode *> dequeTreeNode;

    dequeTreeNode.push_back(pRoot);

    while(dequeTreeNode.size())
    {
        BinaryTreeNode *pNode = dequeTreeNode.front();
        dequeTreeNode.pop_front();

        printf("%d ", pNode->m_nValue);

        if(pNode->m_pLeft)
            dequeTreeNode.push_back(pNode->m_pLeft);

        if(pNode->m_pRight)
            dequeTreeNode.push_back(pNode->m_pRight);
    }
}

// ====================测试代码====================
void Test(char* testName, BinaryTreeNode* pRoot)
{
    if(testName != nullptr)
        printf("%s begins: \n", testName);

    PrintTree(pRoot);

    printf("The nodes from top to bottom, from left to right are: \n");
    PrintFromTopToBottom(pRoot);

    printf("\n\n");
}

//            10
//         /      \
//        6        14
//       /\        /\
//      4  8     12  16
void Test1()
{
    BinaryTreeNode* pNode10 = CreateBinaryTreeNode(10);
    BinaryTreeNode* pNode6 = CreateBinaryTreeNode(6);
    BinaryTreeNode* pNode14 = CreateBinaryTreeNode(14);
    BinaryTreeNode* pNode4 = CreateBinaryTreeNode(4);
    BinaryTreeNode* pNode8 = CreateBinaryTreeNode(8);
    BinaryTreeNode* pNode12 = CreateBinaryTreeNode(12);
    BinaryTreeNode* pNode16 = CreateBinaryTreeNode(16);

    ConnectTreeNodes(pNode10, pNode6, pNode14);
    ConnectTreeNodes(pNode6, pNode4, pNode8);
    ConnectTreeNodes(pNode14, pNode12, pNode16);

    Test("Test1", pNode10);

    DestroyTree(pNode10);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
}
```


### 32_02_PrintTreesInLines

// 面试题32（二）：分行从上到下打印二叉树

// 题目：从上到下按层打印二叉树，同一层的结点按从左到右的顺序打印，每一层

// 打印到一行。

```c++
#include <cstdio>
#include "..\Utilities\BinaryTree.h"
#include <queue>

void Print(BinaryTreeNode* pRoot)
{
    if(pRoot == nullptr)
        return;

    std::queue<BinaryTreeNode*> nodes;
    nodes.push(pRoot);
    int nextLevel = 0;
    int toBePrinted = 1;
    while(!nodes.empty())
    {
        BinaryTreeNode* pNode = nodes.front();
        printf("%d ", pNode->m_nValue);

        if(pNode->m_pLeft != nullptr)
        {
            nodes.push(pNode->m_pLeft);
            ++nextLevel;
        }
        if(pNode->m_pRight != nullptr)
        {
            nodes.push(pNode->m_pRight);
            ++nextLevel;
        }

        nodes.pop();
        --toBePrinted;
        if(toBePrinted == 0)
        {
            printf("\n");
            toBePrinted = nextLevel;
            nextLevel = 0;
        }
    }
}

// ====================测试代码====================
//            8
//        6      10
//       5 7    9  11
void Test1()
{
    BinaryTreeNode* pNode8 = CreateBinaryTreeNode(8);
    BinaryTreeNode* pNode6 = CreateBinaryTreeNode(6);
    BinaryTreeNode* pNode10 = CreateBinaryTreeNode(10);
    BinaryTreeNode* pNode5 = CreateBinaryTreeNode(5);
    BinaryTreeNode* pNode7 = CreateBinaryTreeNode(7);
    BinaryTreeNode* pNode9 = CreateBinaryTreeNode(9);
    BinaryTreeNode* pNode11 = CreateBinaryTreeNode(11);

    ConnectTreeNodes(pNode8, pNode6, pNode10);
    ConnectTreeNodes(pNode6, pNode5, pNode7);
    ConnectTreeNodes(pNode10, pNode9, pNode11);

    printf("====Test1 Begins: ====\n");
    printf("Expected Result is:\n");
    printf("8 \n");
    printf("6 10 \n");
    printf("5 7 9 11 \n\n");

    printf("Actual Result is: \n");
    Print(pNode8);
    printf("\n");

    DestroyTree(pNode8);
}
```


### 32_03_PrintTreesInZigzag


// 面试题32（三）：之字形打印二叉树

// 题目：请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺

// 序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，

// 其他行以此类推。

```c++
#include <cstdio>
#include "..\Utilities\BinaryTree.h"
#include <stack>

void Print(BinaryTreeNode* pRoot)
{
    if(pRoot == nullptr)
        return;

    std::stack<BinaryTreeNode*> levels[2];
    int current = 0;
    int next = 1;

    levels[current].push(pRoot);
    while(!levels[0].empty() || !levels[1].empty())
    {
        BinaryTreeNode* pNode = levels[current].top();
        levels[current].pop();

        printf("%d ", pNode->m_nValue);

        if(current == 0)
        {
            if(pNode->m_pLeft != nullptr)
                levels[next].push(pNode->m_pLeft);
            if(pNode->m_pRight != nullptr)
                levels[next].push(pNode->m_pRight);
        }
        else
        {
            if(pNode->m_pRight != nullptr)
                levels[next].push(pNode->m_pRight);
            if(pNode->m_pLeft != nullptr)
                levels[next].push(pNode->m_pLeft);
        }

        if(levels[current].empty())
        {
            printf("\n");
            current = 1 - current;
            next = 1 - next;
        }
    }
}

// ====================测试代码====================
//            8
//        6      10
//       5 7    9  11
void Test1()
{
    BinaryTreeNode* pNode8 = CreateBinaryTreeNode(8);
    BinaryTreeNode* pNode6 = CreateBinaryTreeNode(6);
    BinaryTreeNode* pNode10 = CreateBinaryTreeNode(10);
    BinaryTreeNode* pNode5 = CreateBinaryTreeNode(5);
    BinaryTreeNode* pNode7 = CreateBinaryTreeNode(7);
    BinaryTreeNode* pNode9 = CreateBinaryTreeNode(9);
    BinaryTreeNode* pNode11 = CreateBinaryTreeNode(11);

    ConnectTreeNodes(pNode8, pNode6, pNode10);
    ConnectTreeNodes(pNode6, pNode5, pNode7);
    ConnectTreeNodes(pNode10, pNode9, pNode11);

    printf("====Test1 Begins: ====\n");
    printf("Expected Result is:\n");
    printf("8 \n");
    printf("10 6 \n");
    printf("5 7 9 11 \n\n");

    printf("Actual Result is: \n");
    Print(pNode8);
    printf("\n");

    DestroyTree(pNode8);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
}
```

#### 33_SquenceOfBST


// 面试题33：二叉搜索树的后序遍历序列

// 题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。

// 如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同。

```c++

SquenceOfBST.cpp

#include <cstdio>

// BST：Binary Search Tree，二叉搜索树
bool VerifySquenceOfBST(int sequence[], int length)
{
    if(sequence == nullptr || length <= 0)
        return false;

    int root = sequence[length - 1];

    // 在二叉搜索树中左子树的结点小于根结点
    int i = 0;
    for(; i < length - 1; ++ i)
    {
        if(sequence[i] > root)
            break;
    }

    // 在二叉搜索树中右子树的结点大于根结点
    int j = i;
    for(; j < length - 1; ++ j)
    {
        if(sequence[j] < root)
            return false;
    }

    // 判断左子树是不是二叉搜索树
    bool left = true;
    if(i > 0)
        left = VerifySquenceOfBST(sequence, i);

    // 判断右子树是不是二叉搜索树
    bool right = true;
    if(i < length - 1)
        right = VerifySquenceOfBST(sequence + i, length - i - 1);

    return (left && right);
}

// ====================测试代码====================
void Test(const char* testName, int sequence[], int length, bool expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    if(VerifySquenceOfBST(sequence, length) == expected)
        printf("passed.\n");
    else
        printf("failed.\n");
}

//            10
//         /      \
//        6        14
//       /\        /\
//      4  8     12  16
void Test1()
{
    int data[] = {4, 8, 6, 12, 16, 14, 10};
    Test("Test1", data, sizeof(data)/sizeof(int), true);
}
```

### 34_PathInTree

// 面试题34：二叉树中和为某一值的路径

// 题目：输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所

// 有路径。从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。


```c++
#include <cstdio>
#include "..\Utilities\BinaryTree.h"
#include <vector>

void FindPath(BinaryTreeNode* pRoot, int expectedSum, std::vector<int>& path, int& currentSum);

void FindPath(BinaryTreeNode* pRoot, int expectedSum)
{
    if(pRoot == nullptr)
        return;

    std::vector<int> path;
    int currentSum = 0;
    FindPath(pRoot, expectedSum, path, currentSum);
}

void FindPath
(
    BinaryTreeNode*   pRoot,        
    int               expectedSum,  
    std::vector<int>& path,         
    int&              currentSum
)
{
    currentSum += pRoot->m_nValue;
    path.push_back(pRoot->m_nValue);

    // 如果是叶结点，并且路径上结点的和等于输入的值
    // 打印出这条路径
    bool isLeaf = pRoot->m_pLeft == nullptr && pRoot->m_pRight == nullptr;
    if(currentSum == expectedSum && isLeaf)
    {
        printf("A path is found: ");
        std::vector<int>::iterator iter = path.begin();
        for(; iter != path.end(); ++ iter)
            printf("%d\t", *iter);
        
        printf("\n");
    }

    // 如果不是叶结点，则遍历它的子结点
    if(pRoot->m_pLeft != nullptr)
        FindPath(pRoot->m_pLeft, expectedSum, path, currentSum);
    if(pRoot->m_pRight != nullptr)
        FindPath(pRoot->m_pRight, expectedSum, path, currentSum);

    // 在返回到父结点之前，在路径上删除当前结点，
    // 并在currentSum中减去当前结点的值
    currentSum -= pRoot->m_nValue;
    path.pop_back();
} 

// ====================测试代码====================
void Test(char* testName, BinaryTreeNode* pRoot, int expectedSum)
{
    if(testName != nullptr)
        printf("%s begins:\n", testName);

    FindPath(pRoot, expectedSum);

    printf("\n");
}

//            10
//         /      \
//        5        12
//       /\        
//      4  7     
// 有两条路径上的结点和为22
void Test1()
{
    BinaryTreeNode* pNode10 = CreateBinaryTreeNode(10);
    BinaryTreeNode* pNode5 = CreateBinaryTreeNode(5);
    BinaryTreeNode* pNode12 = CreateBinaryTreeNode(12);
    BinaryTreeNode* pNode4 = CreateBinaryTreeNode(4);
    BinaryTreeNode* pNode7 = CreateBinaryTreeNode(7);

    ConnectTreeNodes(pNode10, pNode5, pNode12);
    ConnectTreeNodes(pNode5, pNode4, pNode7);

    printf("Two paths should be found in Test1.\n");
    Test("Test1", pNode10, 22);

    DestroyTree(pNode10);
}


int main(int argc, char* argv[])
{
    Test1();
    Test2();

}
```

### 35_CopyComplexList

// 面试题35：复杂链表的复制

// 题目：请实现函数ComplexListNode* Clone(ComplexListNode* pHead)，复

// 制一个复杂链表。在复杂链表中，每个结点除了有一个m_pNext指针指向下一个

// 结点外，还有一个m_pSibling 指向链表中的任意结点或者nullptr。


```c++

ComplexList.h

#pragma once

struct ComplexListNode
{
    int                 m_nValue;
    ComplexListNode*    m_pNext;
    ComplexListNode*    m_pSibling;
};

ComplexListNode* CreateNode(int nValue);
void BuildNodes(ComplexListNode* pNode, ComplexListNode* pNext, ComplexListNode* pSibling);
void PrintList(ComplexListNode* pHead);


ComplexList.cpp

#include <cstdio>
#include "ComplexList.h"

ComplexListNode* CreateNode(int nValue)
{
    ComplexListNode* pNode = new ComplexListNode();
    
    pNode->m_nValue = nValue;
    pNode->m_pNext = nullptr;
    pNode->m_pSibling = nullptr;

    return pNode;
}

void BuildNodes(ComplexListNode* pNode, ComplexListNode* pNext, ComplexListNode* pSibling)
{
    if(pNode != nullptr)
    {
        pNode->m_pNext = pNext;
        pNode->m_pSibling = pSibling;
    }
}

void PrintList(ComplexListNode* pHead)
{
    ComplexListNode* pNode = pHead;
    while(pNode != nullptr)
    {
        printf("The value of this node is: %d.\n", pNode->m_nValue);

        if(pNode->m_pSibling != nullptr)
            printf("The value of its sibling is: %d.\n", pNode->m_pSibling->m_nValue);
        else
            printf("This node does not have a sibling.\n");

        printf("\n");

        pNode = pNode->m_pNext;
    }
}


CopyComplexList.cpp

#include <cstdio>
#include "ComplexList.h"

void CloneNodes(ComplexListNode* pHead);
void ConnectSiblingNodes(ComplexListNode* pHead);
ComplexListNode* ReconnectNodes(ComplexListNode* pHead);

ComplexListNode* Clone(ComplexListNode* pHead)
{
    CloneNodes(pHead);
    ConnectSiblingNodes(pHead);
    return ReconnectNodes(pHead);
}

void CloneNodes(ComplexListNode* pHead)
{
    ComplexListNode* pNode = pHead;
    while(pNode != nullptr)
    {
        ComplexListNode* pCloned = new ComplexListNode();
        pCloned->m_nValue = pNode->m_nValue;
        pCloned->m_pNext = pNode->m_pNext;
        pCloned->m_pSibling = nullptr;
 
        pNode->m_pNext = pCloned;
 
        pNode = pCloned->m_pNext;
    }
}

void ConnectSiblingNodes(ComplexListNode* pHead)
{
    ComplexListNode* pNode = pHead;
    while(pNode != nullptr)
    {
        ComplexListNode* pCloned = pNode->m_pNext;
        if(pNode->m_pSibling != nullptr)
        {
            pCloned->m_pSibling = pNode->m_pSibling->m_pNext;
        }
 
        pNode = pCloned->m_pNext;
    }
}

ComplexListNode* ReconnectNodes(ComplexListNode* pHead)
{
    ComplexListNode* pNode = pHead;
    ComplexListNode* pClonedHead = nullptr;
    ComplexListNode* pClonedNode = nullptr;
 
    if(pNode != nullptr)
    {
        pClonedHead = pClonedNode = pNode->m_pNext;
        pNode->m_pNext = pClonedNode->m_pNext;
        pNode = pNode->m_pNext;
    }
 
    while(pNode != nullptr)
    {
        pClonedNode->m_pNext = pNode->m_pNext;
        pClonedNode = pClonedNode->m_pNext;
 
        pNode->m_pNext = pClonedNode->m_pNext;
        pNode = pNode->m_pNext;
    }
 
    return pClonedHead;
}

// ====================测试代码====================
void Test(const char* testName, ComplexListNode* pHead)
{
    if(testName != nullptr)
        printf("%s begins:\n", testName);

    printf("The original list is:\n");
    PrintList(pHead);

    ComplexListNode* pClonedHead = Clone(pHead);

    printf("The cloned list is:\n");
    PrintList(pClonedHead);
}

//          -----------------
//         \|/              |
//  1-------2-------3-------4-------5
//  |       |      /|\             /|\
//  --------+--------               |
//          -------------------------
void Test1()
{
    ComplexListNode* pNode1 = CreateNode(1);
    ComplexListNode* pNode2 = CreateNode(2);
    ComplexListNode* pNode3 = CreateNode(3);
    ComplexListNode* pNode4 = CreateNode(4);
    ComplexListNode* pNode5 = CreateNode(5);

    BuildNodes(pNode1, pNode2, pNode3);
    BuildNodes(pNode2, pNode3, pNode5);
    BuildNodes(pNode3, pNode4, nullptr);
    BuildNodes(pNode4, pNode5, pNode2);

    Test("Test1", pNode1);
}
```

### 36_ConvertBinarySearchTree

// 面试题36：二叉搜索树与双向链表

// 题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求

// 不能创建任何新的结点，只能调整树中结点指针的指向。


```c++
#include <cstdio>
#include "..\Utilities\BinaryTree.h"

void ConvertNode(BinaryTreeNode* pNode, BinaryTreeNode** pLastNodeInList);

BinaryTreeNode* Convert(BinaryTreeNode* pRootOfTree)
{
	BinaryTreeNode *pLastNodeInList = nullptr;
	ConvertNode(pRootOfTree, &pLastNodeInList);

	// pLastNodeInList指向双向链表的尾结点，
	// 我们需要返回头结点
	BinaryTreeNode *pHeadOfList = pLastNodeInList;
	while(pHeadOfList != nullptr && pHeadOfList->m_pLeft != nullptr)
		pHeadOfList = pHeadOfList->m_pLeft;

	return pHeadOfList;
}

void ConvertNode(BinaryTreeNode* pNode, BinaryTreeNode** pLastNodeInList)
{
	if(pNode == nullptr)
		return;

	BinaryTreeNode *pCurrent = pNode;

	if (pCurrent->m_pLeft != nullptr)
		ConvertNode(pCurrent->m_pLeft, pLastNodeInList);

	pCurrent->m_pLeft = *pLastNodeInList; 
	if(*pLastNodeInList != nullptr)
		(*pLastNodeInList)->m_pRight = pCurrent;

	*pLastNodeInList = pCurrent;

	if (pCurrent->m_pRight != nullptr)
		ConvertNode(pCurrent->m_pRight, pLastNodeInList);
}

// ====================测试代码====================
void PrintDoubleLinkedList(BinaryTreeNode* pHeadOfList)
{
	BinaryTreeNode* pNode = pHeadOfList;

	printf("The nodes from left to right are:\n");
	while(pNode != nullptr)
	{
		printf("%d\t", pNode->m_nValue);

		if(pNode->m_pRight == nullptr)
			break;
		pNode = pNode->m_pRight;
	}

	printf("\nThe nodes from right to left are:\n");
	while(pNode != nullptr)
	{
		printf("%d\t", pNode->m_nValue);

		if(pNode->m_pLeft == nullptr)
			break;
		pNode = pNode->m_pLeft;
	}

	printf("\n");
}

void DestroyList(BinaryTreeNode* pHeadOfList)
{
	BinaryTreeNode* pNode = pHeadOfList;
	while(pNode != nullptr)
	{
		BinaryTreeNode* pNext = pNode->m_pRight;

		delete pNode;
		pNode = pNext;
	}
}

void Test(char* testName, BinaryTreeNode* pRootOfTree)
{
	if(testName != nullptr)
		printf("%s begins:\n", testName);

	PrintTree(pRootOfTree);

	BinaryTreeNode* pHeadOfList = Convert(pRootOfTree);

	PrintDoubleLinkedList(pHeadOfList);
}


//            10
//         /      \
//        6        14
//       /\        /\
//      4  8     12  16
void Test1()
{
	BinaryTreeNode* pNode10 = CreateBinaryTreeNode(10);
	BinaryTreeNode* pNode6 = CreateBinaryTreeNode(6);
	BinaryTreeNode* pNode14 = CreateBinaryTreeNode(14);
	BinaryTreeNode* pNode4 = CreateBinaryTreeNode(4);
	BinaryTreeNode* pNode8 = CreateBinaryTreeNode(8);
	BinaryTreeNode* pNode12 = CreateBinaryTreeNode(12);
	BinaryTreeNode* pNode16 = CreateBinaryTreeNode(16);

	ConnectTreeNodes(pNode10, pNode6, pNode14);
	ConnectTreeNodes(pNode6, pNode4, pNode8);
	ConnectTreeNodes(pNode14, pNode12, pNode16);

	Test("Test1", pNode10);

	DestroyList(pNode4);
}

int main(int argc, char* argv[])
{
	Test1();
	Test2();
}

```


###  37_SerializeBinaryTrees

// 面试题37：序列化二叉树

// 题目：请实现两个函数，分别用来序列化和反序列化二叉树。



```c++

#include <cstdio>
#include "..\Utilities\BinaryTree.h"
#include <iostream>
#include <fstream>

using namespace std;

void Serialize(const BinaryTreeNode* pRoot, ostream& stream)
{
	if(pRoot == nullptr)
	{
		stream << "$,";
		return;
	}

	stream << pRoot->m_nValue << ',';
	Serialize(pRoot->m_pLeft, stream);
	Serialize(pRoot->m_pRight, stream);
}

bool ReadStream(istream& stream, int* number)
{
	if(stream.eof())
		return false;

	char buffer[32];
	buffer[0] = '\0';

	char ch;
	stream >> ch;
	int i = 0;
	while(!stream.eof() && ch != ',')
	{
		buffer[i++] = ch;
		stream >> ch;
	}

	bool isNumeric = false;
	if(i > 0 && buffer[0] != '$')
	{
		*number = atoi(buffer);
		isNumeric = true;
	}

	return isNumeric;
}

void Deserialize(BinaryTreeNode** pRoot, istream& stream)
{
	int number;
	if(ReadStream(stream, &number))
	{
		*pRoot = new BinaryTreeNode();
		(*pRoot)->m_nValue = number;
		(*pRoot)->m_pLeft = nullptr;
		(*pRoot)->m_pRight = nullptr;

		Deserialize(&((*pRoot)->m_pLeft), stream);
		Deserialize(&((*pRoot)->m_pRight), stream);
	}
}

// ==================== Test Code ====================
bool isSameTree(const BinaryTreeNode* pRoot1, const BinaryTreeNode* pRoot2)
{
	if(pRoot1 == nullptr && pRoot2 == nullptr)
		return true;

	if(pRoot1 == nullptr || pRoot2 == nullptr)
		return false;

	if(pRoot1->m_nValue != pRoot2->m_nValue)
		return false;

	return isSameTree(pRoot1->m_pLeft, pRoot2->m_pLeft) &&
		isSameTree(pRoot1->m_pRight, pRoot2->m_pRight);
}

void Test(const char* testName, const BinaryTreeNode* pRoot)
{
	if(testName != nullptr)
		printf("%s begins: \n", testName);

	PrintTree(pRoot);

	char* fileName = "test.txt";
	ofstream fileOut;
	fileOut.open(fileName);

	Serialize(pRoot, fileOut);
	fileOut.close();

	// print the serialized file
	ifstream fileIn1;
	char ch;
	fileIn1.open(fileName);
	while(!fileIn1.eof())
	{
		fileIn1 >> ch;
		cout << ch;
	}
	fileIn1.close();
	cout << endl;

	ifstream fileIn2;
	fileIn2.open(fileName);
	BinaryTreeNode* pNewRoot = nullptr;
	Deserialize(&pNewRoot, fileIn2);
	fileIn2.close();

	PrintTree(pNewRoot);

	if(isSameTree(pRoot, pNewRoot))
		printf("The deserialized tree is same as the oritinal tree.\n\n");
	else
		printf("The deserialized tree is NOT same as the oritinal tree.\n\n");

	DestroyTree(pNewRoot);
}

//            8
//        6      10
//       5 7    9  11
void Test1()
{
	BinaryTreeNode* pNode8 = CreateBinaryTreeNode(8);
	BinaryTreeNode* pNode6 = CreateBinaryTreeNode(6);
	BinaryTreeNode* pNode10 = CreateBinaryTreeNode(10);
	BinaryTreeNode* pNode5 = CreateBinaryTreeNode(5);
	BinaryTreeNode* pNode7 = CreateBinaryTreeNode(7);
	BinaryTreeNode* pNode9 = CreateBinaryTreeNode(9);
	BinaryTreeNode* pNode11 = CreateBinaryTreeNode(11);

	ConnectTreeNodes(pNode8, pNode6, pNode10);
	ConnectTreeNodes(pNode6, pNode5, pNode7);
	ConnectTreeNodes(pNode10, pNode9, pNode11);

	Test("Test1", pNode8);

	DestroyTree(pNode8);
}

//            5
//          4
//        3
//      2
void Test2()
{
	BinaryTreeNode* pNode5 = CreateBinaryTreeNode(5);
	BinaryTreeNode* pNode4 = CreateBinaryTreeNode(4);
	BinaryTreeNode* pNode3 = CreateBinaryTreeNode(3);
	BinaryTreeNode* pNode2 = CreateBinaryTreeNode(2);

	ConnectTreeNodes(pNode5, pNode4, nullptr);
	ConnectTreeNodes(pNode4, pNode3, nullptr);
	ConnectTreeNodes(pNode3, pNode2, nullptr);

	Test("Test2", pNode5);

	DestroyTree(pNode5);
}

int main(int argc, char* argv[])
{
	Test1();
	Test2();

}
```



###  38_StringPermutation

// 面试题38：字符串的排列

// 题目：输入一个字符串，打印出该字符串中字符的所有排列。例如输入字符串abc，

// 则打印出由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。


```c++

#include <cstdio>

void Permutation(char* pStr, char* pBegin);

void Permutation(char* pStr)
{
	if(pStr == nullptr)
		return;

	Permutation(pStr, pStr);
}

void Permutation(char* pStr, char* pBegin)
{
	if(*pBegin == '\0')
	{
		printf("%s\n", pStr);
	}
	else
	{
		for(char* pCh = pBegin; *pCh != '\0'; ++ pCh)
		{
			char temp = *pCh;
			*pCh = *pBegin;
			*pBegin = temp;

			Permutation(pStr, pBegin + 1);

			temp = *pCh;
			*pCh = *pBegin;
			*pBegin = temp;
		}
	}
}

// ====================测试代码====================
void Test(char* pStr)
{
	if(pStr == nullptr)
		printf("Test for nullptr begins:\n");
	else
		printf("Test for %s begins:\n", pStr);

	Permutation(pStr);

	printf("\n");
}

int main(int argc, char* argv[])
{
	Test(nullptr);

	char string1[] = "";
	Test(string1);

	char string2[] = "a";
	Test(string2);

	char string3[] = "ab";
	Test(string3);

	char string4[] = "abc";
	Test(string4);

	return 0;
}
```



###  39_MoreThanHalfNumber

// 面试题39：数组中出现次数超过一半的数字

// 题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例

// 如输入一个长度为9的数组{1, 2, 3, 2, 2, 2, 5, 4, 2}。由于数字2在数组中

// 出现了5次，超过数组长度的一半，因此输出2。



```c++

#include <cstdio>
#include "..\Utilities\Array.h"

bool g_bInputInvalid = false;

bool CheckInvalidArray(int* numbers, int length)
{
    g_bInputInvalid = false;
    if(numbers == nullptr && length <= 0)
        g_bInputInvalid = true;

    return g_bInputInvalid;
}

bool CheckMoreThanHalf(int* numbers, int length, int number)
{
    int times = 0;
    for(int i = 0; i < length; ++i)
    {
        if(numbers[i] == number)
            times++;
    }
 
    bool isMoreThanHalf = true;
    if(times * 2 <= length)
    {
        g_bInputInvalid = true;
        isMoreThanHalf = false;
    }

    return isMoreThanHalf;
}

// ====================方法1====================
int MoreThanHalfNum_Solution1(int* numbers, int length)
{
    if(CheckInvalidArray(numbers, length))
        return 0;
 
    int middle = length >> 1;
    int start = 0;
    int end = length - 1;
    int index = Partition(numbers, length, start, end);
    while(index != middle)
    {
        if(index > middle)
        {
            end = index - 1;
            index = Partition(numbers, length, start, end);
        }
        else
        {
            start = index + 1;
            index = Partition(numbers, length, start, end);
        }
    }
 
    int result = numbers[middle];
    if(!CheckMoreThanHalf(numbers, length, result))
        result = 0;

    return result;
}

// ====================方法2====================
int MoreThanHalfNum_Solution2(int* numbers, int length)
{
    if(CheckInvalidArray(numbers, length))
        return 0;
 
    int result = numbers[0];
    int times = 1;
    for(int i = 1; i < length; ++i)
    {
        if(times == 0)
        {
            result = numbers[i];
            times = 1;
        }
        else if(numbers[i] == result)
            times++;
        else
            times--;
    }
 
    if(!CheckMoreThanHalf(numbers, length, result))
        result = 0;
 
    return result;
}

// ====================测试代码====================
void Test(char* testName, int* numbers, int length, int expectedValue, bool expectedFlag)
{
    if(testName != nullptr)
        printf("%s begins: \n", testName);

    int* copy = new int[length];
    for(int i = 0; i < length; ++i)
        copy[i] = numbers[i];

    printf("Test for solution1: ");
    int result = MoreThanHalfNum_Solution1(numbers, length);
    if(result == expectedValue && g_bInputInvalid == expectedFlag)
        printf("Passed.\n");
    else
        printf("Failed.\n");

    printf("Test for solution2: ");
    result = MoreThanHalfNum_Solution2(copy, length);
    if(result == expectedValue && g_bInputInvalid == expectedFlag)
        printf("Passed.\n");
    else
        printf("Failed.\n");

    delete[] copy;
}

// 存在出现次数超过数组长度一半的数字
void Test1()
{
    int numbers[] = {1, 2, 3, 2, 2, 2, 5, 4, 2};
    Test("Test1", numbers, sizeof(numbers) / sizeof(int), 2, false);
}

// 不存在出现次数超过数组长度一半的数字
void Test2()
{
    int numbers[] = {1, 2, 3, 2, 4, 2, 5, 2, 3};
    Test("Test2", numbers, sizeof(numbers) / sizeof(int), 0, true);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
}

```



### 40_KLeastNumbers

// 面试题40：最小的k个数

// 题目：输入n个整数，找出其中最小的k个数。例如输入4、5、1、6、2、7、3、8

// 这8个数字，则最小的4个数字是1、2、3、4。

```c++
#include <cstdio>
#include "..\Utilities\Array.h"

#include <set>
#include <vector>
#include <iostream>
#include <functional>

using namespace std;

// ====================方法1====================
void GetLeastNumbers_Solution1(int* input, int n, int* output, int k)
{
    if(input == nullptr || output == nullptr || k > n || n <= 0 || k <= 0)
        return;

    int start = 0;
    int end = n - 1;
    int index = Partition(input, n, start, end);
    while(index != k - 1)
    {
        if(index > k - 1)
        {
            end = index - 1;
            index = Partition(input, n, start, end);
        }
        else
        {
            start = index + 1;
            index = Partition(input, n, start, end);
        }
    }

    for(int i = 0; i < k; ++i)
        output[i] = input[i];
}

// ====================方法2====================
typedef multiset<int, std::greater<int> >            intSet;
typedef multiset<int, std::greater<int> >::iterator  setIterator;

void GetLeastNumbers_Solution2(const vector<int>& data, intSet& leastNumbers, int k)
{
    leastNumbers.clear();

    if(k < 1 || data.size() < k)
        return;

    vector<int>::const_iterator iter = data.begin();
    for(; iter != data.end(); ++ iter)
    {
        if((leastNumbers.size()) < k)
            leastNumbers.insert(*iter);

        else
        {
            setIterator iterGreatest = leastNumbers.begin();

            if(*iter < *(leastNumbers.begin()))
            {
                leastNumbers.erase(iterGreatest);
                leastNumbers.insert(*iter);
            }
        }
    }
}

// ====================测试代码====================
void Test(char* testName, int* data, int n, int* expectedResult, int k)
{
    if(testName != nullptr)
        printf("%s begins: \n", testName);

    vector<int> vectorData;
    for(int i = 0; i < n; ++ i)
        vectorData.push_back(data[i]);

    if(expectedResult == nullptr)
        printf("The input is invalid, we don't expect any result.\n");
    else
    {
        printf("Expected result: \n");
        for(int i = 0; i < k; ++ i)
            printf("%d\t", expectedResult[i]);
        printf("\n");
    }

    printf("Result for solution1:\n");
    int* output = new int[k];
    GetLeastNumbers_Solution1(data, n, output, k);
    if(expectedResult != nullptr)
    {
        for(int i = 0; i < k; ++ i)
            printf("%d\t", output[i]);
        printf("\n");
    }

    delete[] output;

    printf("Result for solution2:\n");
    intSet leastNumbers;
    GetLeastNumbers_Solution2(vectorData, leastNumbers, k);
    printf("The actual output numbers are:\n");
    for(setIterator iter = leastNumbers.begin(); iter != leastNumbers.end(); ++iter)
        printf("%d\t", *iter);
    printf("\n\n");
}

// k小于数组的长度
void Test1()
{
    int data[] = {4, 5, 1, 6, 2, 7, 3, 8};
    int expected[] = {1, 2, 3, 4};
    Test("Test1", data, sizeof(data) / sizeof(int), expected, sizeof(expected) / sizeof(int));
}

// k等于数组的长度
void Test2()
{
    int data[] = {4, 5, 1, 6, 2, 7, 3, 8};
    int expected[] = {1, 2, 3, 4, 5, 6, 7, 8};
    Test("Test2", data, sizeof(data) / sizeof(int), expected, sizeof(expected) / sizeof(int));
}

// k等于1
void Test4()
{
    int data[] = {4, 5, 1, 6, 2, 7, 3, 8};
    int expected[] = {1};
    Test("Test4", data, sizeof(data) / sizeof(int), expected, sizeof(expected) / sizeof(int));
}

// k等于0
void Test5()
{
    int data[] = {4, 5, 1, 6, 2, 7, 3, 8};
    int* expected = nullptr;
    Test("Test5", data, sizeof(data) / sizeof(int), expected, 0);
}

// 数组中有相同的数字
void Test6()
{
    int data[] = {4, 5, 1, 6, 2, 7, 2, 8};
    int expected[] = {1, 2};
    Test("Test6", data, sizeof(data) / sizeof(int), expected, sizeof(expected) / sizeof(int));
}

// 输入空指针
void Test7()
{
    int* expected = nullptr;
    Test("Test7", nullptr, 0, expected, 0);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();

}
```


### 41_StreamMedian

// 面试题41：数据流中的中位数

// 题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么

// 中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，

// 那么中位数就是所有数值排序之后中间两个数的平均值。



```c++

#include <cstdio>
#include <algorithm>
#include <vector>
#include <functional>

using namespace std;

template<typename T> class DynamicArray
{
public:
    void Insert(T num)
    {
        if(((min.size() + max.size()) & 1) == 0)
        {
            if(max.size() > 0 && num < max[0])
            {
                max.push_back(num);
                push_heap(max.begin(), max.end(), less<T>());

                num = max[0];

                pop_heap(max.begin(), max.end(), less<T>());
                max.pop_back();
            }

            min.push_back(num);
            push_heap(min.begin(), min.end(), greater<T>());
        }
        else
        {
            if(min.size() > 0 && min[0] < num)
            {
                min.push_back(num);
                push_heap(min.begin(), min.end(), greater<T>());

                num = min[0];

                pop_heap(min.begin(), min.end(), greater<T>());
                min.pop_back();
            }

            max.push_back(num);
            push_heap(max.begin(), max.end(), less<T>());
        }
    }

    T GetMedian()
    {
        int size = min.size() + max.size();
        if(size == 0)
            throw exception("No numbers are available");

        T median = 0;
        if((size & 1) == 1)
            median = min[0];
        else
            median = (min[0] + max[0]) / 2;

        return median;
    }

private:
    vector<T> min;
    vector<T> max;
};

// ====================测试代码====================
void Test(char* testName, DynamicArray<double>& numbers, double expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    if(abs(numbers.GetMedian() - expected) < 0.0000001)
        printf("Passed.\n");
    else
        printf("FAILED.\n");
}

int main(int argc, char* argv[])
{
    DynamicArray<double> numbers;

    printf("Test1 begins: ");
    try
    {
        numbers.GetMedian();
        printf("FAILED.\n");
    }
    catch(const exception&)
    {
        printf("Passed.\n");
    }

    numbers.Insert(5);
    Test("Test2", numbers, 5);

    numbers.Insert(2);
    Test("Test3", numbers, 3.5);

    numbers.Insert(3);
    Test("Test4", numbers, 3);
    
    numbers.Insert(4);
    Test("Test6", numbers, 3.5);

    numbers.Insert(1);
    Test("Test5", numbers, 3);
}
```



### 42_GreatestSumOfSubarrays

// 面试题42：连续子数组的最大和

// 题目：输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整

// 数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)。



```c++
#include <cstdio>

bool g_InvalidInput = false;

int FindGreatestSumOfSubArray(int *pData, int nLength)
{
    if((pData == nullptr) || (nLength <= 0))
    {
        g_InvalidInput = true;
        return 0;
    }

    g_InvalidInput = false;

    int nCurSum = 0;
    int nGreatestSum = 0x80000000;
    for(int i = 0; i < nLength; ++i)
    {
        if(nCurSum <= 0)
            nCurSum = pData[i];
        else
            nCurSum += pData[i];

        if(nCurSum > nGreatestSum)
            nGreatestSum = nCurSum;
    }

    return nGreatestSum;
} 

// ====================测试代码====================
void Test(char* testName, int* pData, int nLength, int expected, bool expectedFlag)
{
    if(testName != nullptr)
        printf("%s begins: \n", testName);

    int result = FindGreatestSumOfSubArray(pData, nLength);
    if(result == expected && expectedFlag == g_InvalidInput)
        printf("Passed.\n");
    else
        printf("Failed.\n");
}

// 1, -2, 3, 10, -4, 7, 2, -5
void Test1()
{
    int data[] = {1, -2, 3, 10, -4, 7, 2, -5};
    Test("Test1", data, sizeof(data) / sizeof(int), 18, false);
}

// 所有数字都是负数
// -2, -8, -1, -5, -9
void Test2()
{
    int data[] = {-2, -8, -1, -5, -9};
    Test("Test2", data, sizeof(data) / sizeof(int), -1, false);
}
// 所有数字都是正数
// 2, 8, 1, 5, 9
void Test3()
{
    int data[] = {2, 8, 1, 5, 9};
    Test("Test3", data, sizeof(data) / sizeof(int), 25, false);
}

// 无效输入
void Test4()
{
    Test("Test4", nullptr, 0, 0, true);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();

    return 0;
}
```


### 43_NumberOf1

// 面试题43：从1到n整数中1出现的次数

// 题目：输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数。例如

// 输入12，从1到12这些整数中包含1 的数字有1，10，11和12，1一共出现了5次。



```c++
#include <cstdio>
#include <cstring>
#include <cstdlib>

// ====================方法一====================
int NumberOf1(unsigned int n);

int NumberOf1Between1AndN_Solution1(unsigned int n)
{
    int number = 0;

    for(unsigned int i = 1; i <= n; ++ i)
        number += NumberOf1(i);

    return number;
}

int NumberOf1(unsigned int n)
{
    int number = 0;
    while(n)
    {
        if(n % 10 == 1)
            number ++;

        n = n / 10;
    }

    return number;
}

// ====================方法二====================
int NumberOf1(const char* strN);
int PowerBase10(unsigned int n);

int NumberOf1Between1AndN_Solution2(int n)
{
    if(n <= 0)
        return 0;

    char strN[50];
    sprintf(strN, "%d", n);

    return NumberOf1(strN);
}

int NumberOf1(const char* strN)
{
    if(!strN || *strN < '0' || *strN > '9' || *strN == '\0')
        return 0;

    int first = *strN - '0';
    unsigned int length = static_cast<unsigned int>(strlen(strN));

    if(length == 1 && first == 0)
        return 0;

    if(length == 1 && first > 0)
        return 1;

    // 假设strN是"21345"
    // numFirstDigit是数字10000-19999的第一个位中1的数目
    int numFirstDigit = 0;
    if(first > 1)
        numFirstDigit = PowerBase10(length - 1);
    else if(first == 1)
        numFirstDigit = atoi(strN + 1) + 1;

    // numOtherDigits是01346-21345除了第一位之外的数位中1的数目
    int numOtherDigits = first * (length - 1) * PowerBase10(length - 2);
    // numRecursive是1-1345中1的数目
    int numRecursive = NumberOf1(strN + 1);

    return numFirstDigit + numOtherDigits + numRecursive;
}

int PowerBase10(unsigned int n)
{
    int result = 1;
    for(unsigned int i = 0; i < n; ++ i)
        result *= 10;

    return result;
}

// ====================测试代码====================
void Test(const char* testName, int n, int expected)
{
    if(testName != nullptr)
        printf("%s begins: \n", testName);
    
    if(NumberOf1Between1AndN_Solution1(n) == expected)
        printf("Solution1 passed.\n");
    else
        printf("Solution1 failed.\n"); 
    
    if(NumberOf1Between1AndN_Solution2(n) == expected)
        printf("Solution2 passed.\n");
    else
        printf("Solution2 failed.\n"); 

    printf("\n");
}

void Test()
{
    Test("Test1", 1, 1);
    Test("Test2", 5, 1);
    Test("Test3", 10, 2);
    Test("Test4", 55, 16);
    Test("Test5", 99, 20);
    Test("Test6", 10000, 4001);
    Test("Test7", 21345, 18821);
    Test("Test8", 0, 0);
}

int main(int argc, char* argv[])
{
    Test();

    return 0;
}
```

### 44_DigitsInSequence

// 面试题44：数字序列中某一位的数字

// 题目：数字以0123456789101112131415…的格式序列化到一个字符序列中。在这

// 个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。请写一

// 个函数求任意位对应的数字。


```c++
#include <iostream>
#include <algorithm>

using namespace std;

int countOfIntegers(int digits);
int digitAtIndex(int index, int digits);
int beginNumber(int digits);

int digitAtIndex(int index)
{
	if(index < 0)
		return -1;

	int digits = 1;
	while(true)
	{
		int numbers = countOfIntegers(digits);
		if(index < numbers * digits)
			return digitAtIndex(index, digits);

		index -= digits * numbers;
		digits++;
	}

	return -1;
}

int countOfIntegers(int digits)
{
	if(digits == 1)
		return 10;

	int count = (int) std::pow(10, digits - 1);
	return 9 * count;
}

int digitAtIndex(int index, int digits)
{
	int number = beginNumber(digits) + index / digits;
	int indexFromRight = digits - index % digits;
	for(int i = 1; i < indexFromRight; ++i)
		number /= 10;
	return number % 10;
}

int beginNumber(int digits)
{
	if(digits == 1)
		return 0;

	return (int) std::pow(10, digits - 1);
}

// ====================测试代码====================
void test(const char* testName, int inputIndex, int expectedOutput)
{
	if(digitAtIndex(inputIndex) == expectedOutput)
		cout << testName << " passed." << endl;
	else
		cout << testName << " FAILED." << endl;
}


int main()
{
	test("Test1", 0, 0);
	test("Test2", 1, 1);
	test("Test3", 9, 9);
	test("Test4", 10, 1);
	test("Test5", 189, 9);  // 数字99的最后一位，9
	test("Test6", 190, 1);  // 数字100的第一位，1
	test("Test7", 1000, 3); // 数字370的第一位，3
	test("Test8", 1001, 7); // 数字370的第二位，7
	test("Test9", 1002, 0); // 数字370的第三位，0
	return 0;
}

### 45_SortArrayForMinNumber

// 面试题45：把数组排成最小的数

// 题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼

// 接出的所有数字中最小的一个。例如输入数组{3, 32, 321}，则打印出这3个数

// 字能排成的最小数字321323。

#include "cstdio"
#include <string>
#include <algorithm>

int compare(const void* strNumber1, const void* strNumber2);

// int型整数用十进制表示最多只有10位
const int g_MaxNumberLength = 10;
 
char* g_StrCombine1 = new char[g_MaxNumberLength * 2 + 1];
char* g_StrCombine2 = new char[g_MaxNumberLength * 2 + 1];
 
void PrintMinNumber(const int* numbers, int length)
{
    if(numbers == nullptr || length <= 0)
        return;
 
    char** strNumbers = (char**)(new int[length]);
    for(int i = 0; i < length; ++i)
    {
        strNumbers[i] = new char[g_MaxNumberLength + 1];
        sprintf(strNumbers[i], "%d", numbers[i]);
    }
 
    qsort(strNumbers, length, sizeof(char*), compare);
 
    for(int i = 0; i < length; ++i)
        printf("%s", strNumbers[i]);
    printf("\n");
 
    for(int i = 0; i < length; ++i)
        delete[] strNumbers[i];
    delete[] strNumbers;
}
 
// 如果[strNumber1][strNumber2] > [strNumber2][strNumber1], 返回值大于0
// 如果[strNumber1][strNumber2] = [strNumber2][strNumber1], 返回值等于0
// 如果[strNumber1][strNumber2] < [strNumber2][strNumber1], 返回值小于0
int compare(const void* strNumber1, const void* strNumber2)
{
    // [strNumber1][strNumber2]
    strcpy(g_StrCombine1, *(const char**)strNumber1);
    strcat(g_StrCombine1, *(const char**)strNumber2);
 
    // [strNumber2][strNumber1]
    strcpy(g_StrCombine2, *(const char**)strNumber2);
    strcat(g_StrCombine2, *(const char**)strNumber1);
 
    return strcmp(g_StrCombine1, g_StrCombine2);
}

// ====================测试代码====================
void Test(const char* testName, int* numbers, int length, const char* expectedResult)
{
    if(testName != nullptr)
        printf("%s begins:\n", testName);

    if(expectedResult != nullptr)
        printf("Expected result is: \t%s\n", expectedResult);

    printf("Actual result is: \t");
    PrintMinNumber(numbers, length);

    printf("\n");
}

void Test1()
{
    int numbers[] = {3, 5, 1, 4, 2};
    Test("Test1", numbers, sizeof(numbers)/sizeof(int), "12345");
}

void Test2()
{
    int numbers[] = {3, 32, 321};
    Test("Test2", numbers, sizeof(numbers)/sizeof(int), "321323");
}

void Test3()
{
    int numbers[] = {3, 323, 32123};
    Test("Test3", numbers, sizeof(numbers)/sizeof(int), "321233233");
}

void Test4()
{
    int numbers[] = {1, 11, 111};
    Test("Test4", numbers, sizeof(numbers)/sizeof(int), "111111");
}

// 数组中只有一个数字
void Test5()
{
    int numbers[] = {321};
    Test("Test5", numbers, sizeof(numbers)/sizeof(int), "321");
}

void Test6()
{
    Test("Test6", nullptr, 0, "Don't print anything.");
}


int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
    Test5();
    Test6();

    return 0;
}
```

### 46_TranslateNumbersToStrings


// 面试题46：把数字翻译成字符串

// 题目：给定一个数字，我们按照如下规则把它翻译为字符串：0翻译成"a"，1翻

// 译成"b"，……，11翻译成"l"，……，25翻译成"z"。一个数字可能有多个翻译。例

// 如12258有5种不同的翻译，它们分别是"bccfi"、"bwfi"、"bczi"、"mcfi"和

// "mzi"。请编程实现一个函数用来计算一个数字有多少种不同的翻译方法。


```c++
#include <string>
#include <iostream>

using namespace std;

int GetTranslationCount(const string& number);

int GetTranslationCount(int number)
{
    if(number < 0)
        return 0;

    string numberInString = to_string(number);
    return GetTranslationCount(numberInString);
}

int GetTranslationCount(const string& number)
{
    int length = number.length();
    int* counts = new int[length];
    int count = 0;

    for(int i = length - 1; i >= 0; --i)
    {
        count = 0;
         if(i < length - 1)
               count = counts[i + 1];
         else
               count = 1;

        if(i < length - 1)
        {
            int digit1 = number[i] - '0';
            int digit2 = number[i + 1] - '0';
            int converted = digit1 * 10 + digit2;
            if(converted >= 10 && converted <= 25)
            {
                if(i < length - 2)
                    count += counts[i + 2];
                else
                    count += 1;
            }
        }

        counts[i] = count;
    }

    count = counts[0];
    delete[] counts;

    return count;
}

// ====================测试代码====================
void Test(const string& testName, int number, int expected)
{
    if(GetTranslationCount(number) == expected)
        cout << testName << " passed." << endl;
    else
        cout << testName << " FAILED." << endl;
}

void Test1()
{
    int number = 0;
    int expected = 1;
    Test("Test1", number, expected);
}

void Test2()
{
    int number = 10;
    int expected = 2;
    Test("Test2", number, expected);
}

void Test3()
{
    int number = 125;
    int expected = 3;
    Test("Test3", number, expected);
}

void Test4()
{
    int number = 126;
    int expected = 2;
    Test("Test4", number, expected);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
}
```

### 47_MaxValueOfGifts

// 面试题47：礼物的最大价值

// 题目：在一个m×n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值

// （价值大于0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向左或

// 者向下移动一格直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计

// 算你最多能拿到多少价值的礼物？


```c++
#include <algorithm>
#include <iostream>

int getMaxValue_solution1(const int* values, int rows, int cols)
{
    if(values == nullptr || rows <= 0 || cols <= 0)
        return 0;

    int** maxValues = new int*[rows];
    for(int i = 0; i < rows; ++i)
        maxValues[i] = new int[cols];

    for(int i = 0; i < rows; ++i)
    {
        for(int j = 0; j < cols; ++j)
        {
            int left = 0;
            int up = 0;

            if(i > 0)
                up = maxValues[i - 1][j];

            if(j > 0)
                left = maxValues[i][j - 1];

            maxValues[i][j] = std::max(left, up) + values[i * cols + j];
        }
    }

    int maxValue = maxValues[rows - 1][cols - 1];

    for(int i = 0; i < rows; ++i)
        delete[] maxValues[i];
    delete[] maxValues;

    return maxValue;
}

int getMaxValue_solution2(const int* values, int rows, int cols)
{
    if(values == nullptr || rows <= 0 || cols <= 0)
        return 0;

    int* maxValues = new int[cols];
    for(int i = 0; i < rows; ++i)
    {
        for(int j = 0; j < cols; ++j)
        {
            int left = 0;
            int up = 0;

            if(i > 0)
                up = maxValues[j];

            if(j > 0)
                left = maxValues[j - 1];

            maxValues[j] = std::max(left, up) + values[i * cols + j];
        }
    }

    int maxValue = maxValues[cols - 1];

    delete[] maxValues;

    return maxValue;
}

// ====================测试代码====================
void test(const char* testName, const int* values, int rows, int cols, int expected)
{
    if(getMaxValue_solution1(values, rows, cols) == expected)
        std::cout << testName << ": solution1 passed." << std::endl;
    else
        std::cout << testName << ": solution1 FAILED." << std::endl;

    if(getMaxValue_solution2(values, rows, cols) == expected)
        std::cout << testName << ": solution2 passed." << std::endl;
    else
        std::cout << testName << ": solution2 FAILED." << std::endl;
}

void test1()
{
    // 三行三列
    int values[][3] = {
        { 1, 2, 3 },
        { 4, 5, 6 },
        { 7, 8, 9 }
    };
    int expected = 29;
    test("test1", (const int*) values, 3, 3, expected);
}

void test2()
{
    //四行四列
    int values[][4] = {
        { 1, 10, 3, 8 },
        { 12, 2, 9, 6 },
        { 5, 7, 4, 11 },
        { 3, 7, 16, 5 }
    };
    int expected = 53;
    test("test2", (const int*) values, 4, 4, expected);
}

void test3()
{
    // 一行四列
    int values[][4] = {
        { 1, 10, 3, 8 }
    };
    int expected = 22;
    test("test3", (const int*) values, 1, 4, expected);
}

void test4()
{
    int values[4][1] = {
        { 1 },
        { 12 },
        { 5 },
        { 3 }
    };
    int expected = 21;
    test("test4", (const int*) values, 4, 1, expected);
}

void test5()
{
    // 一行一列
    int values[][1] = {
        { 3 }
    };
    int expected = 3;
    test("test5", (const int*) values, 1, 1, expected);
}

void test6()
{
    // 空指针
    int expected = 0;
    test("test6", nullptr, 0, 0, expected);
}

int main(int argc, char* argv[])
{
    test1();
    test2();
    test3();
    test4();
    test5();

    return 0;
}
```

### 48_LongestSubstringWithoutDup

// 面试题48：最长不含重复字符的子字符串

// 题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子

// 字符串的长度。假设字符串中只包含从'a'到'z'的字符。

```c++
#include <string>
#include <iostream>

// 方法一：蛮力法
bool hasDuplication(const std::string& str, int position[]);

int longestSubstringWithoutDuplication_1(const std::string& str)
{
    int longest = 0;
    int* position = new int[26];
    for(int start = 0; start < str.length(); ++start)
    {
        for(int end = start; end < str.length(); ++end)
        {
            int count = end - start + 1;
            const std::string& substring = str.substr(start, count);
            if(!hasDuplication(substring, position))
            {
                if(count > longest)
                    longest = count;
            }
            else
                break;

        }
    }

    delete[] position;
    return longest;
}

bool hasDuplication(const std::string& str, int position[])
{
    for(int i = 0; i < 26; ++i)
        position[i] = -1;

    for(int i = 0; i < str.length(); ++i)
    {
        int indexInPosition = str[i] - 'a';
        if(position[indexInPosition] >= 0)
            return true;

        position[indexInPosition] = indexInPosition;
    }

    return false;
}

// 方法一：动态规划
int longestSubstringWithoutDuplication_2(const std::string& str)
{
    int curLength = 0;
    int maxLength = 0;

    int* position = new int[26];
    for(int i = 0; i < 26; ++i)
        position[i] = -1;

    for(int i = 0; i < str.length(); ++i)
    {
        int prevIndex = position[str[i] - 'a'];
        if(prevIndex < 0 || i - prevIndex > curLength)
            ++curLength;
        else
        {
            if(curLength > maxLength)
                maxLength = curLength;

            curLength = i - prevIndex;
        }
        position[str[i] - 'a'] = i;
    }

    if(curLength > maxLength)
        maxLength = curLength;

    delete[] position;
    return maxLength;
}

// ====================测试代码====================
void testSolution1(const std::string& input, int expected)
{
    int output = longestSubstringWithoutDuplication_1(input);
    if(output == expected)
        std::cout << "Solution 1 passed, with input: " << input << std::endl;
    else
        std::cout << "Solution 1 FAILED, with input: " << input << std::endl;
}

void testSolution2(const std::string& input, int expected)
{
    int output = longestSubstringWithoutDuplication_2(input);
    if(output == expected)
        std::cout << "Solution 2 passed, with input: " << input << std::endl;
    else
        std::cout << "Solution 2 FAILED, with input: " << input << std::endl;
}

void test(const std::string& input, int expected)
{
    testSolution1(input, expected);
    testSolution2(input, expected);
}

void test1()
{
    const std::string input = "abcacfrar";
    int expected = 4;
    test(input, expected);
}

void test2()
{
    const std::string input = "acfrarabc";
    int expected = 4;
    test(input, expected);
}

void test3()
{
    const std::string input = "arabcacfr";
    int expected = 4;
    test(input, expected);
}

void test4()
{
    const std::string input = "aaaa";
    int expected = 1;
    test(input, expected);
}

void test5()
{
    const std::string input = "abcdefg";
    int expected = 7;
    test(input, expected);
}

int main(int argc, char* argv[])
{
    test1();
    test2();
    test3();
    test4();
    test5();

}
```

### 49_UglyNumber

// 面试题49：丑数

// 题目：我们把只包含因子2、3和5的数称作丑数（Ugly Number）。求按从小到

// 大的顺序的第1500个丑数。例如6、8都是丑数，但14不是，因为它包含因子7。

// 习惯上我们把1当做第一个丑数。


```c++
#include <cstdio>

// ====================算法1的代码====================
bool IsUgly(int number)
{
    while(number % 2 == 0)
        number /= 2;
    while(number % 3 == 0)
        number /= 3;
    while(number % 5 == 0)
        number /= 5;

    return (number == 1) ? true : false;
}

int GetUglyNumber_Solution1(int index)
{
    if(index <= 0)
        return 0;

    int number = 0;
    int uglyFound = 0;
    while(uglyFound < index)
    {
        ++number;

        if(IsUgly(number))
            ++uglyFound;
    }

    return number;
}

// ====================算法2的代码====================
int Min(int number1, int number2, int number3);

int GetUglyNumber_Solution2(int index)
{
    if(index <= 0)
        return 0;

    int *pUglyNumbers = new int[index];
    pUglyNumbers[0] = 1;
    int nextUglyIndex = 1;

    int *pMultiply2 = pUglyNumbers;
    int *pMultiply3 = pUglyNumbers;
    int *pMultiply5 = pUglyNumbers;

    while(nextUglyIndex < index)
    {
        int min = Min(*pMultiply2 * 2, *pMultiply3 * 3, *pMultiply5 * 5);
        pUglyNumbers[nextUglyIndex] = min;

        while(*pMultiply2 * 2 <= pUglyNumbers[nextUglyIndex])
            ++pMultiply2;
        while(*pMultiply3 * 3 <= pUglyNumbers[nextUglyIndex])
            ++pMultiply3;
        while(*pMultiply5 * 5 <= pUglyNumbers[nextUglyIndex])
            ++pMultiply5;

        ++nextUglyIndex;
    }

    int ugly = pUglyNumbers[nextUglyIndex - 1];
    delete[] pUglyNumbers;
    return ugly;
}

int Min(int number1, int number2, int number3)
{
    int min = (number1 < number2) ? number1 : number2;
    min = (min < number3) ? min : number3;

    return min;
}

// ====================测试代码====================
void Test(int index, int expected)
{
    if(GetUglyNumber_Solution1(index) == expected)
        printf("solution1 passed\n");
    else
        printf("solution1 failed\n");

    if(GetUglyNumber_Solution2(index) == expected)
        printf("solution2 passed\n");
    else
        printf("solution2 failed\n");
}

int main(int argc, char* argv[])
{
    Test(1, 1);

    Test(2, 2);
    Test(3, 3);
    Test(4, 4);
    Test(10, 12);
    Test(11, 15);

    Test(1500, 859963392);

}
```

### 50_01_FirstNotRepeatingChar

// 面试题50（一）：字符串中第一个只出现一次的字符

// 题目：在字符串中找出第一个只出现一次的字符。如输入"abaccdeff"，则输出

// 'b'。


```c++
#include <cstdio>
#include <string>

char FirstNotRepeatingChar(const char* pString)
{
    if(pString == nullptr)
        return '\0';

    const int tableSize = 256;
    unsigned int hashTable[tableSize];
    for(unsigned int i = 0; i < tableSize; ++i)
        hashTable[i] = 0;

    const char* pHashKey = pString;
    while(*(pHashKey) != '\0')
        hashTable[*(pHashKey++)] ++;

    pHashKey = pString;
    while(*pHashKey != '\0')
    {
        if(hashTable[*pHashKey] == 1)
            return *pHashKey;

        pHashKey++;
    }

    return '\0';
}

// ====================测试代码====================
void Test(const char* pString, char expected)
{
    if(FirstNotRepeatingChar(pString) == expected)
        printf("Test passed.\n");
    else
        printf("Test failed.\n");
}

int main(int argc, char* argv[])
{
    // 常规输入测试，存在只出现一次的字符
    Test("google", 'l');

    // 常规输入测试，不存在只出现一次的字符
    Test("aabccdbd", '\0');

    // 常规输入测试，所有字符都只出现一次
    Test("abcdefg", 'a');

    // 鲁棒性测试，输入nullptr
    Test(nullptr, '\0');

    return 0;
}
```

###  50_02_FirstCharacterInStream

// 面试题50（二）：字符流中第一个只出现一次的字符

// 题目：请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从

// 字符流中只读出前两个字符"go"时，第一个只出现一次的字符是'g'。当从该字

// 符流中读出前六个字符"google"时，第一个只出现一次的字符是'l'。

```c++
#include <cstdio>
#include <vector>
#include <limits>

using namespace std;

class CharStatistics
{
public:
    CharStatistics() : index(0)
    {
        for(int i = 0; i < 256; ++i)
            occurrence[i] = -1;
    }

    void Insert(char ch)
    {
        if(occurrence[ch] == -1)
            occurrence[ch] = index;
        else if(occurrence[ch] >= 0)
            occurrence[ch] = -2;

        index++;
    }

    char FirstAppearingOnce()
    {
        char ch = '\0';
        int minIndex = numeric_limits<int>::max();
        for(int i = 0; i < 256; ++i)
        {
            if(occurrence[i] >= 0 && occurrence[i] < minIndex)
            {
                ch = (char) i;
                minIndex = occurrence[i];
            }
        }

        return ch;
    }

private:
    // occurrence[i]: A character with ASCII value i;
    // occurrence[i] = -1: The character has not found;
    // occurrence[i] = -2: The character has been found for mutlple times
    // occurrence[i] >= 0: The character has been found only once
    int occurrence[256];
    int index;
};

// ====================测试代码====================
void Test(const char* testName, CharStatistics chars, char expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    if(chars.FirstAppearingOnce() == expected)
        printf("Passed.\n");
    else
        printf("FAILED.\n");
}

int main(int argc, char* argv[])
{
    CharStatistics chars;

    Test("Test1", chars, '\0');

    chars.Insert('g');
    Test("Test2", chars, 'g');

    chars.Insert('o');
    Test("Test3", chars, 'g');

    chars.Insert('o');
    Test("Test4", chars, 'g');

}
```


### 51_InversePairs

// 面试题51：数组中的逆序对

// 题目：在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组

// 成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

```c++
#include <cstdio>

int InversePairsCore(int* data, int* copy, int start, int end);

int InversePairs(int* data, int length)
{
    if(data == nullptr || length < 0)
        return 0;

    int* copy = new int[length];
    for(int i = 0; i < length; ++i)
        copy[i] = data[i];

    int count = InversePairsCore(data, copy, 0, length - 1);
    delete[] copy;

    return count;
}

int InversePairsCore(int* data, int* copy, int start, int end)
{
    if(start == end)
    {
        copy[start] = data[start];
        return 0;
    }

    int length = (end - start) / 2;

    int left = InversePairsCore(copy, data, start, start + length);
    int right = InversePairsCore(copy, data, start + length + 1, end);

    // i初始化为前半段最后一个数字的下标
    int i = start + length;
    // j初始化为后半段最后一个数字的下标
    int j = end;
    int indexCopy = end;
    int count = 0;
    while(i >= start && j >= start + length + 1)
    {
        if(data[i] > data[j])
        {
            copy[indexCopy--] = data[i--];
            count += j - start - length;
        }
        else
        {
            copy[indexCopy--] = data[j--];
        }
    }

    for(; i >= start; --i)
        copy[indexCopy--] = data[i];

    for(; j >= start + length + 1; --j)
        copy[indexCopy--] = data[j];

    return left + right + count;
}

// ====================测试代码====================
void Test(char* testName, int* data, int length, int expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    if(InversePairs(data, length) == expected)
        printf("Passed.\n");
    else
        printf("Failed.\n");
}

void Test1()
{
    int data[] = { 1, 2, 3, 4, 7, 6, 5 };
    int expected = 3;

    Test("Test1", data, sizeof(data) / sizeof(int), expected);
}

// 递减排序数组
void Test2()
{
    int data[] = { 6, 5, 4, 3, 2, 1 };
    int expected = 15;

    Test("Test2", data, sizeof(data) / sizeof(int), expected);
}

// 递增排序数组
void Test3()
{
    int data[] = { 1, 2, 3, 4, 5, 6 };
    int expected = 0;

    Test("Test3", data, sizeof(data) / sizeof(int), expected);
}


int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
}
```



###  52_FirstCommonNodesInLists

// 面试题52：两个链表的第一个公共结点

// 题目：输入两个链表，找出它们的第一个公共结点。

```c++
#include <cstdio>
#include "..\Utilities\List.h"

unsigned int GetListLength(ListNode* pHead);

ListNode* FindFirstCommonNode(ListNode *pHead1, ListNode *pHead2)
{
    // 得到两个链表的长度
    unsigned int nLength1 = GetListLength(pHead1);
    unsigned int nLength2 = GetListLength(pHead2);
    int nLengthDif = nLength1 - nLength2;

    ListNode* pListHeadLong = pHead1;
    ListNode* pListHeadShort = pHead2;
    if(nLength2 > nLength1)
    {
        pListHeadLong = pHead2;
        pListHeadShort = pHead1;
        nLengthDif = nLength2 - nLength1;
    }

    // 先在长链表上走几步，再同时在两个链表上遍历
    for(int i = 0; i < nLengthDif; ++i)
        pListHeadLong = pListHeadLong->m_pNext;

    while((pListHeadLong != nullptr) &&
        (pListHeadShort != nullptr) &&
        (pListHeadLong != pListHeadShort))
    {
        pListHeadLong = pListHeadLong->m_pNext;
        pListHeadShort = pListHeadShort->m_pNext;
    }

    // 得到第一个公共结点
    ListNode* pFisrtCommonNode = pListHeadLong;

    return pFisrtCommonNode;
}

unsigned int GetListLength(ListNode* pHead)
{
    unsigned int nLength = 0;
    ListNode* pNode = pHead;
    while(pNode != nullptr)
    {
        ++nLength;
        pNode = pNode->m_pNext;
    }

    return nLength;
}

// ====================测试代码====================
void DestroyNode(ListNode* pNode);

void Test(char* testName, ListNode* pHead1, ListNode* pHead2, ListNode* pExpected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    ListNode* pResult = FindFirstCommonNode(pHead1, pHead2);
    if(pResult == pExpected)
        printf("Passed.\n");
    else
        printf("Failed.\n");
}

// 第一个公共结点在链表中间
// 1 - 2 - 3 \
//            6 - 7
//     4 - 5 /
void Test1()
{
    ListNode* pNode1 = CreateListNode(1);
    ListNode* pNode2 = CreateListNode(2);
    ListNode* pNode3 = CreateListNode(3);
    ListNode* pNode4 = CreateListNode(4);
    ListNode* pNode5 = CreateListNode(5);
    ListNode* pNode6 = CreateListNode(6);
    ListNode* pNode7 = CreateListNode(7);

    ConnectListNodes(pNode1, pNode2);
    ConnectListNodes(pNode2, pNode3);
    ConnectListNodes(pNode3, pNode6);
    ConnectListNodes(pNode4, pNode5);
    ConnectListNodes(pNode5, pNode6);
    ConnectListNodes(pNode6, pNode7);

    Test("Test1", pNode1, pNode4, pNode6);

    DestroyNode(pNode1);
    DestroyNode(pNode2);
    DestroyNode(pNode3);
    DestroyNode(pNode4);
    DestroyNode(pNode5);
    DestroyNode(pNode6);
    DestroyNode(pNode7);
}

void DestroyNode(ListNode* pNode)
{
    delete pNode;
    pNode = nullptr;
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
}
```

###  53_01_NumberOfK

// 面试题53（一）：数字在排序数组中出现的次数
// 题目：统计一个数字在排序数组中出现的次数。例如输入排序数组{1, 2, 3, 3,
// 3, 3, 4, 5}和数字3，由于3在这个数组中出现了4次，因此输出4。


```c++
#include <cstdio>

int GetFirstK(const int* data, int length, int k, int start, int end);
int GetLastK(const int* data, int length, int k, int start, int end);

int GetNumberOfK(const int* data, int length, int k)
{
    int number = 0;

    if(data != nullptr && length > 0)
    {
        int first = GetFirstK(data, length, k, 0, length - 1);
        int last = GetLastK(data, length, k, 0, length - 1);
        
        if(first > -1 && last > -1)
            number = last - first + 1;
    }

    return number;
}

// 找到数组中第一个k的下标。如果数组中不存在k，返回-1
int GetFirstK(const int* data, int length, int k, int start, int end)
{
    if(start > end)
        return -1;

    int middleIndex = (start + end) / 2;
    int middleData = data[middleIndex];

    if(middleData == k)
    {
        if((middleIndex > 0 && data[middleIndex - 1] != k) 
            || middleIndex == 0)
            return middleIndex;
        else
            end  = middleIndex - 1;
    }
    else if(middleData > k)
        end = middleIndex - 1;
    else
        start = middleIndex + 1;

    return GetFirstK(data, length, k, start, end);
}

// 找到数组中最后一个k的下标。如果数组中不存在k，返回-1
int GetLastK(const int* data, int length, int k, int start, int end)
{
    if(start > end)
        return -1;

    int middleIndex = (start + end) / 2;
    int middleData = data[middleIndex];

    if(middleData == k)
    {
        if((middleIndex < length - 1 && data[middleIndex + 1] != k) 
            || middleIndex == length - 1)
            return middleIndex;
        else
            start  = middleIndex + 1;
    }
    else if(middleData < k)
        start = middleIndex + 1;
    else
        end = middleIndex - 1;

    return GetLastK(data, length, k, start, end);
}

// ====================测试代码====================
void Test(const char* testName, int data[], int length, int k, int expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    int result = GetNumberOfK(data, length, k);
    if(result == expected)
        printf("Passed.\n");
    else
        printf("Failed.\n");
}

// 查找的数字出现在数组的中间
void Test1()
{
    int data[] = {1, 2, 3, 3, 3, 3, 4, 5};
    Test("Test1", data, sizeof(data) / sizeof(int), 3, 4);
}

// 查找的数组出现在数组的开头
void Test2()
{
    int data[] = {3, 3, 3, 3, 4, 5};
    Test("Test2", data, sizeof(data) / sizeof(int), 3, 4);
}

// 查找的数组出现在数组的结尾
void Test3()
{
    int data[] = {1, 2, 3, 3, 3, 3};
    Test("Test3", data, sizeof(data) / sizeof(int), 3, 4);
}

// 数组中的数字从头到尾都是查找的数字
void Test7()
{
    int data[] = {3, 3, 3, 3};
    Test("Test7", data, sizeof(data) / sizeof(int), 3, 4);
}

// 数组中的数字从头到尾只有一个重复的数字，不是查找的数字
void Test8()
{
    int data[] = {3, 3, 3, 3};
    Test("Test8", data, sizeof(data) / sizeof(int), 4, 0);
}
// 鲁棒性测试，数组空指针
void Test11()
{
    Test("Test11", nullptr, 0, 0, 0);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
    Test5();
}
```


###  53_02_MissingNumber

// 面试题53（二）：0到n-1中缺失的数字

// 题目：一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字

// 都在范围0到n-1之内。在范围0到n-1的n个数字中有且只有一个数字不在该数组

// 中，请找出这个数字。

```c++
#include <cstdio>

int GetMissingNumber(const int* numbers, int length)
{
    if(numbers == nullptr || length <= 0)
        return -1;

    int left = 0;
    int right = length - 1;
    while(left <= right)
    {
        int middle = (right + left) >> 1;
        if(numbers[middle] != middle)
        {
            if(middle == 0 || numbers[middle - 1] == middle - 1)
                return middle;
            right = middle - 1;
        }
        else
            left = middle + 1;
    }

    if(left == length)
        return length;

    // 无效的输入，比如数组不是按要求排序的，
    // 或者有数字不在0到n-1范围之内
    return -1;
}

// ====================测试代码====================
void Test(const char* testName, int numbers[], int length, int expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    int result = GetMissingNumber(numbers, length);
    if(result == expected)
        printf("Passed.\n");
    else
        printf("Failed.\n");
}

// 缺失的是第一个数字0
void Test1()
{
    int numbers[] = { 1, 2, 3, 4, 5 };
    int expected = 0;
    Test("Test1", numbers, sizeof(numbers) / sizeof(int), expected);
}

// 缺失的是最后一个数字
void Test2()
{
    int numbers[] = { 0, 1, 2, 3, 4 };
    int expected = 5;
    Test("Test2", numbers, sizeof(numbers) / sizeof(int), expected);
}

// 缺失的是中间某个数字0
void Test3()
{
    int numbers[] = { 0, 1, 2, 4, 5 };
    int expected = 3;
    Test("Test3", numbers, sizeof(numbers) / sizeof(int), expected);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
}
```


### 53_03_IntegerIdenticalToIndex

// 面试题53（三）：数组中数值和下标相等的元素

// 题目：假设一个单调递增的数组里的每个元素都是整数并且是唯一的。请编程实

// 现一个函数找出数组中任意一个数值等于其下标的元素。例如，在数组{-3, -1,

// 1, 3, 5}中，数字3和它的下标相等。

```c++
#include <cstdio>

int GetNumberSameAsIndex(const int* numbers, int length)
{
    if(numbers == nullptr || length <= 0)
        return -1;

    int left = 0;
    int right = length - 1;
    while(left <= right)
    {
        int middle = left + ((right - left) >> 1);
        if(numbers[middle] == middle)
            return middle;

        if(numbers[middle] > middle)
            right = middle - 1;
        else
            left = middle + 1;
    }

    return -1;
}

// ====================测试代码====================
void Test(const char* testName, int numbers[], int length, int expected)
{
    if(GetNumberSameAsIndex(numbers, length) == expected)
        printf("%s passed.\n", testName);
    else
        printf("%s FAILED.\n", testName);
}

void Test1()
{
    int numbers[] = { -3, -1, 1, 3, 5 };
    int expected = 3;
    Test("Test1", numbers, sizeof(numbers) / sizeof(int), expected);
}

void Test2()
{
    int numbers[] = { 0, 1, 3, 5, 6 };
    int expected = 0;
    Test("Test2", numbers, sizeof(numbers) / sizeof(int), expected);
}

void Test3()
{
    int numbers[] = { -1, 0, 1, 2, 4 };
    int expected = 4;
    Test("Test3", numbers, sizeof(numbers) / sizeof(int), expected);
}

void Test4()
{
    int numbers[] = { -1, 0, 1, 2, 5 };
    int expected = -1;
    Test("Test4", numbers, sizeof(numbers) / sizeof(int), expected);
}

void Test5()
{
    int numbers[] = { 0 };
    int expected = 0;
    Test("Test5", numbers, sizeof(numbers) / sizeof(int), expected);
}

void Test6()
{
    int numbers[] = { 10 };
    int expected = -1;
    Test("Test6", numbers, sizeof(numbers) / sizeof(int), expected);
}

void Test7()
{
    Test("Test7", nullptr, 0, -1);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
    Test5();
    Test6();
    Test7();

    return 0;
}
```


### 54_KthNodeInBST


// 面试题54：二叉搜索树的第k个结点

// 题目：给定一棵二叉搜索树，请找出其中的第k大的结点。


```c++
#include <cstdio>
#include "../Utilities/BinaryTree.h"

const BinaryTreeNode* KthNodeCore(const BinaryTreeNode* pRoot, unsigned int& k);

const BinaryTreeNode* KthNode(const BinaryTreeNode* pRoot, unsigned int k)
{
    if(pRoot == nullptr || k == 0)
        return nullptr;

    return KthNodeCore(pRoot, k);
}

const BinaryTreeNode* KthNodeCore(const BinaryTreeNode* pRoot, unsigned int& k)
{
    const BinaryTreeNode* target = nullptr;

    if(pRoot->m_pLeft != nullptr)
        target = KthNodeCore(pRoot->m_pLeft, k);

    if(target == nullptr)
    {
        if(k == 1)
            target = pRoot;

        k--;
    }

    if(target == nullptr && pRoot->m_pRight != nullptr)
        target = KthNodeCore(pRoot->m_pRight, k);

    return target;
}

// ====================测试代码====================
void Test(const char* testName, const BinaryTreeNode* pRoot, unsigned int k, bool isNull, int expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    const BinaryTreeNode* pTarget = KthNode(pRoot, k);
    if((isNull && pTarget == nullptr) || (!isNull && pTarget->m_nValue == expected))
        printf("Passed.\n");
    else
        printf("FAILED.\n");
}

//            8
//        6      10
//       5 7    9  11
void TestA()
{
    BinaryTreeNode* pNode8 = CreateBinaryTreeNode(8);
    BinaryTreeNode* pNode6 = CreateBinaryTreeNode(6);
    BinaryTreeNode* pNode10 = CreateBinaryTreeNode(10);
    BinaryTreeNode* pNode5 = CreateBinaryTreeNode(5);
    BinaryTreeNode* pNode7 = CreateBinaryTreeNode(7);
    BinaryTreeNode* pNode9 = CreateBinaryTreeNode(9);
    BinaryTreeNode* pNode11 = CreateBinaryTreeNode(11);

    ConnectTreeNodes(pNode8, pNode6, pNode10);
    ConnectTreeNodes(pNode6, pNode5, pNode7);
    ConnectTreeNodes(pNode10, pNode9, pNode11);

    Test("TestA0", pNode8, 0, true, -1);
    Test("TestA1", pNode8, 1, false, 5);
    Test("TestA2", pNode8, 2, false, 6);
    Test("TestA3", pNode8, 3, false, 7);
    Test("TestA4", pNode8, 4, false, 8);
    Test("TestA5", pNode8, 5, false, 9);
    Test("TestA6", pNode8, 6, false, 10);
    Test("TestA7", pNode8, 7, false, 11);
    Test("TestA8", pNode8, 8, true, -1);

    DestroyTree(pNode8);

    printf("\n\n");
}

// There is only one node in a tree
void TestD()
{
    BinaryTreeNode* pNode1 = CreateBinaryTreeNode(1);

    Test("TestD0", pNode1, 0, true, -1);
    Test("TestD1", pNode1, 1, false, 1);
    Test("TestD2", pNode1, 2, true, -1);

    DestroyTree(pNode1);

    printf("\n\n");
}

// empty tree
void TestE()
{
    Test("TestE0", nullptr, 0, true, -1);
    Test("TestE1", nullptr, 1, true, -1);

    printf("\n\n");
}

int main(int argc, char* argv[])
{
    TestA();
    TestB();
    TestC();
    TestD();
    TestE();
}
```


###  55_01_TreeDepth

// 面试题55（一）：二叉树的深度

// 题目：输入一棵二叉树的根结点，求该树的深度。从根结点到叶结点依次经过的

// 结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。


```c++
#include <cstdio>
#include "..\Utilities\BinaryTree.h"

int TreeDepth(const BinaryTreeNode* pRoot)
{
    if(pRoot == nullptr)
        return 0;

    int nLeft = TreeDepth(pRoot->m_pLeft);
    int nRight = TreeDepth(pRoot->m_pRight);

    return (nLeft > nRight) ? (nLeft + 1) : (nRight + 1);
}

// ====================测试代码====================
void Test(const char* testName, const BinaryTreeNode* pRoot, int expected)
{
    int result = TreeDepth(pRoot);
    if(expected == result)
        printf("%s passed.\n", testName);
    else
        printf("%s FAILED.\n", testName);
}

//            1
//         /      \
//        2        3
//       /\         \
//      4  5         6
//        /
//       7
void Test1()
{
    BinaryTreeNode* pNode1 = CreateBinaryTreeNode(1);
    BinaryTreeNode* pNode2 = CreateBinaryTreeNode(2);
    BinaryTreeNode* pNode3 = CreateBinaryTreeNode(3);
    BinaryTreeNode* pNode4 = CreateBinaryTreeNode(4);
    BinaryTreeNode* pNode5 = CreateBinaryTreeNode(5);
    BinaryTreeNode* pNode6 = CreateBinaryTreeNode(6);
    BinaryTreeNode* pNode7 = CreateBinaryTreeNode(7);

    ConnectTreeNodes(pNode1, pNode2, pNode3);
    ConnectTreeNodes(pNode2, pNode4, pNode5);
    ConnectTreeNodes(pNode3, nullptr, pNode6);
    ConnectTreeNodes(pNode5, pNode7, nullptr);

    Test("Test1", pNode1, 4);

    DestroyTree(pNode1);
}


// 树中只有1个结点
void Test4()
{
    BinaryTreeNode* pNode1 = CreateBinaryTreeNode(1);
    Test("Test4", pNode1, 1);

    DestroyTree(pNode1);
}

// 树中没有结点
void Test5()
{
    Test("Test5", nullptr, 0);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
    Test5();

    return 0;
}
```


### 55_02_BalancedBinaryTree

// 面试题55（二）：平衡二叉树

// 题目：输入一棵二叉树的根结点，判断该树是不是平衡二叉树。如果某二叉树中

// 任意结点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。


```c++
#include <cstdio>
#include "..\Utilities\BinaryTree.h"

// ====================方法1====================
int TreeDepth(const BinaryTreeNode* pRoot)
{
    if(pRoot == nullptr)
        return 0;

    int nLeft = TreeDepth(pRoot->m_pLeft);
    int nRight = TreeDepth(pRoot->m_pRight);

    return (nLeft > nRight) ? (nLeft + 1) : (nRight + 1);
}

bool IsBalanced_Solution1(const BinaryTreeNode* pRoot)
{
    if(pRoot == nullptr)
        return true;

    int left = TreeDepth(pRoot->m_pLeft);
    int right = TreeDepth(pRoot->m_pRight);
    int diff = left - right;
    if(diff > 1 || diff < -1)
        return false;

    return IsBalanced_Solution1(pRoot->m_pLeft) 
        && IsBalanced_Solution1(pRoot->m_pRight);
}

// ====================方法2====================
bool IsBalanced(const BinaryTreeNode* pRoot, int* pDepth);

bool IsBalanced_Solution2(const BinaryTreeNode* pRoot)
{
    int depth = 0;
    return IsBalanced(pRoot, &depth);
}

bool IsBalanced(const BinaryTreeNode* pRoot, int* pDepth)
{
    if(pRoot == nullptr)
    {
        *pDepth = 0;
        return true;
    }

    int left, right;
    if(IsBalanced(pRoot->m_pLeft, &left) 
        && IsBalanced(pRoot->m_pRight, &right))
    {
        int diff = left - right;
        if(diff <= 1 && diff >= -1)
        {
            *pDepth = 1 + (left > right ? left : right);
            return true;
        }
    }

    return false;
}

// ====================测试代码====================
void Test(const char* testName, const BinaryTreeNode* pRoot, bool expected)
{
    if(testName != nullptr)
        printf("%s begins:\n", testName);

    printf("Solution1 begins: ");
    if(IsBalanced_Solution1(pRoot) == expected)
        printf("Passed.\n");
    else
        printf("Failed.\n");

    printf("Solution2 begins: ");
    if(IsBalanced_Solution2(pRoot) == expected)
        printf("Passed.\n");
    else
        printf("Failed.\n");
}

// 完全二叉树
//             1
//         /      \
//        2        3
//       /\       / \
//      4  5     6   7
void Test1()
{
    BinaryTreeNode* pNode1 = CreateBinaryTreeNode(1);
    BinaryTreeNode* pNode2 = CreateBinaryTreeNode(2);
    BinaryTreeNode* pNode3 = CreateBinaryTreeNode(3);
    BinaryTreeNode* pNode4 = CreateBinaryTreeNode(4);
    BinaryTreeNode* pNode5 = CreateBinaryTreeNode(5);
    BinaryTreeNode* pNode6 = CreateBinaryTreeNode(6);
    BinaryTreeNode* pNode7 = CreateBinaryTreeNode(7);

    ConnectTreeNodes(pNode1, pNode2, pNode3);
    ConnectTreeNodes(pNode2, pNode4, pNode5);
    ConnectTreeNodes(pNode3, pNode6, pNode7);

    Test("Test1", pNode1, true);

    DestroyTree(pNode1);
}

// 1
//  \
//   2
//    \
//     3
//      \
//       4
//        \
//         5
void Test5()
{
    BinaryTreeNode* pNode1 = CreateBinaryTreeNode(1);
    BinaryTreeNode* pNode2 = CreateBinaryTreeNode(2);
    BinaryTreeNode* pNode3 = CreateBinaryTreeNode(3);
    BinaryTreeNode* pNode4 = CreateBinaryTreeNode(4);
    BinaryTreeNode* pNode5 = CreateBinaryTreeNode(5);

    ConnectTreeNodes(pNode1, nullptr, pNode2);
    ConnectTreeNodes(pNode2, nullptr, pNode3);
    ConnectTreeNodes(pNode3, nullptr, pNode4);
    ConnectTreeNodes(pNode4, nullptr, pNode5);

    Test("Test5", pNode1, false);

    DestroyTree(pNode1);
}

// 树中只有1个结点
void Test6()
{
    BinaryTreeNode* pNode1 = CreateBinaryTreeNode(1);
    Test("Test6", pNode1, true);

    DestroyTree(pNode1);
}

// 树中没有结点
void Test7()
{
    Test("Test7", nullptr, true);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
    Test5();
    Test6();
    Test7();

    return 0;
}
```


### 56_01_NumbersAppearOnce

// 面试题56（一）：数组中只出现一次的两个数字

// 题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序

// 找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。


```c++
#include <cstdio>

unsigned int FindFirstBitIs1(int num);
bool IsBit1(int num, unsigned int indexBit);

void FindNumsAppearOnce(int data[], int length, int* num1, int* num2)
{
    if(data == nullptr || length < 2)
        return;

    int resultExclusiveOR = 0;
    for(int i = 0; i < length; ++i)
        resultExclusiveOR ^= data[i];

    unsigned int indexOf1 = FindFirstBitIs1(resultExclusiveOR);

    *num1 = *num2 = 0;
    for(int j = 0; j < length; ++j)
    {
        if(IsBit1(data[j], indexOf1))
            *num1 ^= data[j];
        else
            *num2 ^= data[j];
    }
}

// 找到num从右边数起第一个是1的位
unsigned int FindFirstBitIs1(int num)
{
    int indexBit = 0;
    while(((num & 1) == 0) && (indexBit < 8 * sizeof(int)))
    {
        num = num >> 1;
        ++indexBit;
    }

    return indexBit;
}

// 判断数字num的第indexBit位是不是1
bool IsBit1(int num, unsigned int indexBit)
{
    num = num >> indexBit;
    return (num & 1);
}

// ====================测试代码====================
void Test(const char* testName, int data[], int length, int expected1, int expected2)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    int result1, result2;
    FindNumsAppearOnce(data, length, &result1, &result2);

    if((expected1 == result1 && expected2 == result2) ||
        (expected2 == result1 && expected1 == result2))
        printf("Passed.\n\n");
    else
        printf("Failed.\n\n");
}

void Test1()
{
    int data[] = { 2, 4, 3, 6, 3, 2, 5, 5 };
    Test("Test1", data, sizeof(data) / sizeof(int), 4, 6);
}

void Test2()
{
    int data[] = { 4, 6 };
    Test("Test2", data, sizeof(data) / sizeof(int), 4, 6);
}

void Test3()
{
    int data[] = { 4, 6, 1, 1, 1, 1 };
    Test("Test3", data, sizeof(data) / sizeof(int), 4, 6);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();

    return 0;
}
```


### 56_02_NumberAppearingOnce

// 面试题56（二）：数组中唯一只出现一次的数字

// 题目：在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。请

// 找出那个吃出现一次的数字。


```c++
#include <cstdio>
#include <exception>

int FindNumberAppearingOnce(int numbers[], int length)
{
    if(numbers == nullptr || length <= 0)
        throw new std::exception("Invalid input.");

    int bitSum[32] = {0};
    for(int i = 0; i < length; ++i)
    {
        int bitMask = 1;
        for(int j = 31; j >= 0; --j)
        {
            int bit = numbers[i] & bitMask;
            if(bit != 0)
                bitSum[j] += 1;

            bitMask = bitMask << 1;
        }
    }

    int result = 0;
    for(int i = 0; i < 32; ++i)
    {
        result = result << 1;
        result += bitSum[i] % 3;
    }

    return result;
}

// ====================测试代码====================
void Test(const char* testName, int numbers[], int length, int expected)
{
    int result = FindNumberAppearingOnce(numbers, length);
    if(result == expected)
        printf("%s passed.\n", testName);
    else
        printf("%s FAILED.\n", testName);
}

// 所有数字都是正数，唯一的数字是最小的
void Test1()
{
    int numbers[] = { 1, 1, 2, 2, 2, 1, 3 };
    int expected = 3;
    Test("Test1", numbers, sizeof(numbers) / sizeof(int), expected);
}

// 所有数字都是正数，唯一的数字的大小位于中间
void Test2()
{
    int numbers[] = { 4, 3, 3, 2, 2, 2, 3 };
    int expected = 4;
    Test("Test2", numbers, sizeof(numbers) / sizeof(int), expected);
}

// 所有数字都是正数，唯一的数字是最大的
void Test3()
{
    int numbers[] = { 4, 4, 1, 1, 1, 7, 4 };
    int expected = 7;
    Test("Test3", numbers, sizeof(numbers) / sizeof(int), expected);
}

// 唯一的数字是负数
void Test4()
{
    int numbers[] = { -10, 214, 214, 214 };
    int expected = -10;
    Test("Test4", numbers, sizeof(numbers) / sizeof(int), expected);
}

// 除了唯一的数字，其他数字都是负数
void Test5()
{
    int numbers[] = { -209, 3467, -209, -209 };
    int expected = 3467;
    Test("Test5", numbers, sizeof(numbers) / sizeof(int), expected);
}

// 重复的数字有正数也有负数
void Test6()
{
    int numbers[] = { 1024, -1025, 1024, -1025, 1024, -1025, 1023 };
    int expected = 1023;
    Test("Test6", numbers, sizeof(numbers) / sizeof(int), expected);
}

// 所有数字都是负数
void Test7()
{
    int numbers[] = { -1024, -1024, -1024, -1023 };
    int expected = -1023;
    Test("Test7", numbers, sizeof(numbers) / sizeof(int), expected);
}

// 唯一的数字是0
void Test8()
{
    int numbers[] = { -23, 0, 214, -23, 214, -23, 214 };
    int expected = 0;
    Test("Test8", numbers, sizeof(numbers) / sizeof(int), expected);
}

// 除了唯一的数字，其他数字都是0
void Test9()
{
    int numbers[] = { 0, 3467, 0, 0, 0, 0, 0, 0 };
    int expected = 3467;
    Test("Test9", numbers, sizeof(numbers) / sizeof(int), expected);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
    Test5();
    Test6();
    Test7();
    Test8();
    Test9();

    return 0;
}
```


###  57_01_TwoNumbersWithSum


// 面试题57（一）：和为s的两个数字

// 题目：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们

// 的和正好是s。如果有多对数字的和等于s，输出任意一对即可。


```c++
#include <cstdio>

bool FindNumbersWithSum(int data[], int length, int sum, 
                        int* num1, int* num2)
{
    bool found = false;
    if(length < 1 || num1 == nullptr || num2 == nullptr)
        return found;

    int ahead = length - 1;
    int behind = 0;

    while(ahead > behind)
    {
        long long curSum = data[ahead] + data[behind];

        if(curSum == sum)
        {
            *num1 = data[behind];
            *num2 = data[ahead];
            found = true;
            break;
        }
        else if(curSum > sum)
            ahead --;
        else
            behind ++;
    }

    return found;
}

// ====================测试代码====================
void Test(const char* testName, int data[], int length, int sum, bool expectedReturn)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);
    
    int num1, num2;
    int result = FindNumbersWithSum(data, length, sum, &num1, &num2);
    if(result == expectedReturn)
    {
        if(result)
        {
            if(num1 + num2 == sum)
                printf("Passed. \n");
            else
                printf("FAILED. \n");
        }
        else
            printf("Passed. \n");
    }
    else
        printf("FAILED. \n");
}

// 存在和为s的两个数字，这两个数字位于数组的中间
void Test1()
{
    int data[] = {1, 2, 4, 7, 11, 15};
    Test("Test1", data, sizeof(data) / sizeof(int), 15, true);
}

// 存在和为s的两个数字，这两个数字位于数组的两段
void Test2()
{
    int data[] = {1, 2, 4, 7, 11, 16};
    Test("Test2", data, sizeof(data) / sizeof(int), 17, true);
}

// 不存在和为s的两个数字
void Test3()
{
    int data[] = {1, 2, 4, 7, 11, 16};
    Test("Test3", data, sizeof(data) / sizeof(int), 10, false);
}

// 鲁棒性测试
void Test4()
{
    Test("Test4", nullptr, 0, 0, false);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();

    return 0;
}
```


###  57_02_ContinuousSquenceWithSum

// 面试题57（二）：为s的连续正数序列

// 题目：输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。

// 例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以结果打印出3个连续序列1～5、

// 4～6和7～8。


```c++
#include <cstdio>

void PrintContinuousSequence(int small, int big);

void FindContinuousSequence(int sum)
{
    if(sum < 3)
        return;

    int small = 1; 
    int big = 2;
    int middle = (1 + sum) / 2;
    int curSum = small + big;

    while(small < middle)
    {
        if(curSum == sum)
            PrintContinuousSequence(small, big);

        while(curSum > sum && small < middle)
        {
            curSum -= small;
            small ++;

            if(curSum == sum)
                PrintContinuousSequence(small, big);
        }

        big ++;
        curSum += big;
    }
}

void PrintContinuousSequence(int small, int big)
{
    for(int i = small; i <= big; ++ i)
        printf("%d ", i);

    printf("\n");
}

// ====================测试代码====================
void Test(const char* testName, int sum)
{
    if(testName != nullptr)
        printf("%s for %d begins: \n", testName, sum);

    FindContinuousSequence(sum);
}

int main(int argc, char* argv[])
{
    Test("test1", 1);
    Test("test2", 3);
    Test("test3", 4);
    Test("test4", 9);
    Test("test5", 15);
    Test("test6", 100);

    return 0;
}
```


### 58_01_ReverseWordsInSentence

// 面试题58（一）：翻转单词顺序

// 题目：输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。

// 为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，

// 则输出"student. a am I"。


```c++
#include <cstdio>
#include "..\Utilities\StringUtil.h"
#include <string>

char* ReverseSentence(char *pData)
{
    if(pData == nullptr)
        return nullptr;

    char *pBegin = pData;

    char *pEnd = pData;
    while(*pEnd != '\0')
        pEnd ++;
    pEnd--;

    // 翻转整个句子
    Reverse(pBegin, pEnd);

    // 翻转句子中的每个单词
    pBegin = pEnd = pData;
    while(*pBegin != '\0')
    {
        if(*pBegin == ' ')
        {
            pBegin ++;
            pEnd ++;
        }
        else if(*pEnd == ' ' || *pEnd == '\0')
        {
            Reverse(pBegin, --pEnd);
            pBegin = ++pEnd;
        }
        else
            pEnd ++;
    }

    return pData;
}

// ====================测试代码====================
void Test(const char* testName, char* input, const char* expectedResult)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    ReverseSentence(input);

    if((input == nullptr && expectedResult == nullptr)
        || (input != nullptr && strcmp(input, expectedResult) == 0))
        printf("Passed.\n\n");
    else
        printf("Failed.\n\n");
}

// 功能测试，句子中有多个单词
void Test1()
{
    char input[] = "I am a student.";
    char expected[] = "student. a am I";

    Test("Test1", input, expected);
}

// 功能测试，句子中只有一个单词
void Test2()
{
    char input[] = "Wonderful";
    char expected[] = "Wonderful";

    Test("Test2", input, expected);
}

// 鲁棒性测试
void Test3()
{
    Test("Test3", nullptr, nullptr);
}

// 边界值测试，测试空字符串
void Test4()
{
    Test("Test4", "", "");
}

// 边界值测试，字符串中只有空格
void Test5()
{
    char input[] = "   ";
    char expected[] = "   ";
    Test("Test5", input, expected);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
    Test5();

    return 0;
}
```


### 58_02_LeftRotateString

// 面试题58（二）：左旋转字符串

// 题目：字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。

// 请定义一个函数实现字符串左旋转操作的功能。比如输入字符串"abcdefg"和数

// 字2，该函数将返回左旋转2位得到的结果"cdefgab"。


```c++
#include <cstdio>
#include "..\Utilities\StringUtil.h"
#include <string.h>

char* LeftRotateString(char* pStr, int n)
{
    if(pStr != nullptr)
    {
        int nLength = static_cast<int>(strlen(pStr));
        if(nLength > 0 && n > 0 && n < nLength)
        {
            char* pFirstStart = pStr;
            char* pFirstEnd = pStr + n - 1;
            char* pSecondStart = pStr + n;
            char* pSecondEnd = pStr + nLength - 1;

            // 翻转字符串的前面n个字符
            Reverse(pFirstStart, pFirstEnd);
            // 翻转字符串的后面部分
            Reverse(pSecondStart, pSecondEnd);
            // 翻转整个字符串
            Reverse(pFirstStart, pSecondEnd);
        }
    }

    return pStr;
}

// ====================测试代码====================
void Test(const char* testName, char* input, int num, const char* expectedResult)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    char* result = LeftRotateString(input, num);

    if((input == nullptr && expectedResult == nullptr)
        || (input != nullptr && strcmp(result, expectedResult) == 0))
        printf("Passed.\n\n");
    else
        printf("Failed.\n\n");
}

// 功能测试
void Test1()
{
    char input[] = "abcdefg";
    char expected[] = "cdefgab";

    Test("Test1", input, 2, expected);
}

// 边界值测试
void Test2()
{
    char input[] = "abcdefg";
    char expected[] = "bcdefga";

    Test("Test2", input, 1, expected);
}

// 边界值测试
void Test3()
{
    char input[] = "abcdefg";
    char expected[] = "gabcdef";

    Test("Test3", input, 6, expected);
}

// 鲁棒性测试
void Test4()
{
    Test("Test4", nullptr, 6, nullptr);
}

// 鲁棒性测试
void Test5()
{
    char input[] = "abcdefg";
    char expected[] = "abcdefg";

    Test("Test5", input, 0, expected);
}

// 鲁棒性测试
void Test6()
{
    char input[] = "abcdefg";
    char expected[] = "abcdefg";

    Test("Test6", input, 7, expected);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
    Test5();
    Test6();

    return 0;
}
```


###  59_01_MaxInSlidingWindow

// 面试题59（一）：滑动窗口的最大值

// 题目：给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。例如，

// 如果输入数组{2, 3, 4, 2, 6, 2, 5, 1}及滑动窗口的大小3，那么一共存在6个

// 滑动窗口，它们的最大值分别为{4, 4, 6, 6, 6, 5}，


```c++
#include <cstdio>
#include <vector>
#include <deque>

using namespace std;

vector<int> maxInWindows(const vector<int>& num, unsigned int size)
{
    vector<int> maxInWindows;
    if(num.size() >= size && size >= 1)
    {
        deque<int> index;

        for(unsigned int i = 0; i < size; ++i)
        {
            while(!index.empty() && num[i] >= num[index.back()])
                index.pop_back();

            index.push_back(i);
        }

        for(unsigned int i = size; i < num.size(); ++i)
        {
            maxInWindows.push_back(num[index.front()]);

            while(!index.empty() && num[i] >= num[index.back()])
                index.pop_back();
            if(!index.empty() && index.front() <= (int) (i - size))
                index.pop_front();

            index.push_back(i);
        }
        maxInWindows.push_back(num[index.front()]);
    }

    return maxInWindows;
}

// ====================测试代码====================
void Test(const char* testName, const vector<int>& num, unsigned int size, const vector<int>& expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    vector<int> result = maxInWindows(num, size);

    vector<int>::const_iterator iterResult = result.begin();
    vector<int>::const_iterator iterExpected = expected.begin();
    while(iterResult < result.end() && iterExpected < expected.end())
    {
        if(*iterResult != *iterExpected)
            break;

        ++iterResult;
        ++iterExpected;
    }

    if(iterResult == result.end() && iterExpected == expected.end())
        printf("Passed.\n");
    else
        printf("FAILED.\n");
}

void Test1()
{
    int num[] = { 2, 3, 4, 2, 6, 2, 5, 1 };
    vector<int> vecNumbers(num, num + sizeof(num) / sizeof(int));

    int expected[] = { 4, 4, 6, 6, 6, 5 };
    vector<int> vecExpected(expected, expected + sizeof(expected) / sizeof(int));

    unsigned int size = 3;

    Test("Test1", vecNumbers, size, vecExpected);
}

void Test2()
{
    int num[] = { 1, 3, -1, -3, 5, 3, 6, 7 };
    vector<int> vecNumbers(num, num + sizeof(num) / sizeof(int));

    int expected[] = { 3, 3, 5, 5, 6, 7 };
    vector<int> vecExpected(expected, expected + sizeof(expected) / sizeof(int));

    unsigned int size = 3;

    Test("Test2", vecNumbers, size, vecExpected);
}

// 输入数组单调递增
void Test3()
{
    int num[] = { 1, 3, 5, 7, 9, 11, 13, 15 };
    vector<int> vecNumbers(num, num + sizeof(num) / sizeof(int));

    int expected[] = { 7, 9, 11, 13, 15 };
    vector<int> vecExpected(expected, expected + sizeof(expected) / sizeof(int));

    unsigned int size = 4;

    Test("Test3", vecNumbers, size, vecExpected);
}

// 输入数组单调递减
void Test4()
{
    int num[] = { 16, 14, 12, 10, 8, 6, 4 };
    vector<int> vecNumbers(num, num + sizeof(num) / sizeof(int));

    int expected[] = { 16, 14, 12 };
    vector<int> vecExpected(expected, expected + sizeof(expected) / sizeof(int));

    unsigned int size = 5;

    Test("Test4", vecNumbers, size, vecExpected);
}

// 滑动窗口的大小为1
void Test5()
{
    int num[] = { 10, 14, 12, 11 };
    vector<int> vecNumbers(num, num + sizeof(num) / sizeof(int));

    int expected[] = { 10, 14, 12, 11 };
    vector<int> vecExpected(expected, expected + sizeof(expected) / sizeof(int));

    unsigned int size = 1;

    Test("Test5", vecNumbers, size, vecExpected);
}

// 滑动窗口的大小等于数组的长度
void Test6()
{
    int num[] = { 10, 14, 12, 11 };
    vector<int> vecNumbers(num, num + sizeof(num) / sizeof(int));

    int expected[] = { 14 };
    vector<int> vecExpected(expected, expected + sizeof(expected) / sizeof(int));

    unsigned int size = 4;

    Test("Test6", vecNumbers, size, vecExpected);
}

// 滑动窗口的大小为0
void Test7()
{
    int num[] = { 10, 14, 12, 11 };
    vector<int> vecNumbers(num, num + sizeof(num) / sizeof(int));

    vector<int> vecExpected;

    unsigned int size = 0;

    Test("Test7", vecNumbers, size, vecExpected);
}

// 滑动窗口的大小大于输入数组的长度
void Test8()
{
    int num[] = { 10, 14, 12, 11 };
    vector<int> vecNumbers(num, num + sizeof(num) / sizeof(int));

    vector<int> vecExpected;

    unsigned int size = 5;

    Test("Test8", vecNumbers, size, vecExpected);
}

// 输入数组为空
void Test9()
{
    vector<int> vecNumbers;
    vector<int> vecExpected;

    unsigned int size = 5;

    Test("Test9", vecNumbers, size, vecExpected);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
    Test5();
    Test6();
    Test7();
    Test8();
    Test9();

    return 0;
}
```


###  59_02_QueueWithMax

// 面试题59（二）：队列的最大值

// 题目：给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。例如，

// 如果输入数组{2, 3, 4, 2, 6, 2, 5, 1}及滑动窗口的大小3，那么一共存在6个

// 滑动窗口，它们的最大值分别为{4, 4, 6, 6, 6, 5}，


```c++
#include <cstdio>
#include <deque>
#include <exception>

using namespace std;

template<typename T> class QueueWithMax
{
public:
    QueueWithMax() : currentIndex(0)
    {
    }

    void push_back(T number)
    {
        while(!maximums.empty() && number >= maximums.back().number)
            maximums.pop_back();

        InternalData internalData = { number, currentIndex };
        data.push_back(internalData);
        maximums.push_back(internalData);

        ++currentIndex;
    }

    void pop_front()
    {
        if(maximums.empty())
            throw new exception("queue is empty");

        if(maximums.front().index == data.front().index)
            maximums.pop_front();

        data.pop_front();
    }

    T max() const
    {
        if(maximums.empty())
            throw new exception("queue is empty");

        return maximums.front().number;
    }

private:
    struct InternalData
    {
        T number;
        int index;
    };

    deque<InternalData> data;
    deque<InternalData> maximums;
    int currentIndex;
};

// ====================测试代码====================
void Test(const char* testName, const QueueWithMax<int>& queue, int expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    if(queue.max() == expected)
        printf("Passed.\n");
    else
        printf("FAILED.\n");
}

int main(int argc, char* argv[])
{
    QueueWithMax<int> queue;
    // {2}
    queue.push_back(2);
    Test("Test1", queue, 2);

    // {2, 3}
    queue.push_back(3);
    Test("Test2", queue, 3);

    // {2, 3, 4}
    queue.push_back(4);
    Test("Test3", queue, 4);

    // {2, 3, 4, 2}
    queue.push_back(2);
    Test("Test4", queue, 4);

    // {3, 4, 2}
    queue.pop_front();
    Test("Test5", queue, 4);

    // {4, 2}
    queue.pop_front();
    Test("Test6", queue, 4);

    // {2}
    queue.pop_front();
    Test("Test7", queue, 2);

    // {2, 6}
    queue.push_back(6);
    Test("Test8", queue, 6);

    // {2, 6, 2}
    queue.push_back(2);
    Test("Test9", queue, 6);

    // {2, 6, 2, 5}
    queue.push_back(5);
    Test("Test9", queue, 6);

    // {6, 2, 5}
    queue.pop_front();
    Test("Test10", queue, 6);

    // {2, 5}
    queue.pop_front();
    Test("Test11", queue, 5);

    // {5}
    queue.pop_front();
    Test("Test12", queue, 5);

    // {5, 1}
    queue.push_back(1);
    Test("Test13", queue, 5);

    return 0;
}
```


### 60_DicesProbability

// 面试题60：n个骰子的点数

// 题目：把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s

// 的所有可能的值出现的概率。


```c++
#include <cstdio>
#include <math.h>

int g_maxValue = 6;
 
// ====================方法一====================
void Probability(int number, int* pProbabilities);
void Probability(int original, int current, int sum, int* pProbabilities);

void PrintProbability_Solution1(int number)
{
    if(number < 1)
        return;
 
    int maxSum = number * g_maxValue;
    int* pProbabilities = new int[maxSum - number + 1];
    for(int i = number; i <= maxSum; ++i)
        pProbabilities[i - number] = 0;
 
    Probability(number, pProbabilities);
 
    int total = pow((double)g_maxValue, number);
    for(int i = number; i <= maxSum; ++i)
    {
        double ratio = (double)pProbabilities[i - number] / total;
        printf("%d: %e\n", i, ratio);
    }
 
    delete[] pProbabilities;
}
 
void Probability(int number, int* pProbabilities)
{
    for(int i = 1; i <= g_maxValue; ++i)
        Probability(number, number, i, pProbabilities);
}
 
void Probability(int original, int current, int sum, 
                 int* pProbabilities)
{
    if(current == 1)
    {
        pProbabilities[sum - original]++;
    }
    else
    {
        for(int i = 1; i <= g_maxValue; ++i)
        {
            Probability(original, current - 1, i + sum, pProbabilities);
        }
    }
} 

// ====================方法二====================
void PrintProbability_Solution2(int number)
{
    if(number < 1)
        return;

    int* pProbabilities[2];
    pProbabilities[0] = new int[g_maxValue * number + 1];
    pProbabilities[1] = new int[g_maxValue * number + 1];
    for(int i = 0; i < g_maxValue * number + 1; ++i)
    {
        pProbabilities[0][i] = 0;
        pProbabilities[1][i] = 0;
    }
 
    int flag = 0;
    for (int i = 1; i <= g_maxValue; ++i) 
        pProbabilities[flag][i] = 1; 
    
    for (int k = 2; k <= number; ++k) 
    {
        for(int i = 0; i < k; ++i)
            pProbabilities[1 - flag][i] = 0;

        for (int i = k; i <= g_maxValue * k; ++i) 
        {
            pProbabilities[1 - flag][i] = 0;
            for(int j = 1; j <= i && j <= g_maxValue; ++j) 
                pProbabilities[1 - flag][i] += pProbabilities[flag][i - j];
        }
 
        flag = 1 - flag;
    }
 
    double total = pow((double)g_maxValue, number);
    for(int i = number; i <= g_maxValue * number; ++i)
    {
        double ratio = (double)pProbabilities[flag][i] / total;
        printf("%d: %e\n", i, ratio);
    }
 
    delete[] pProbabilities[0];
    delete[] pProbabilities[1];
}

// ====================测试代码====================
void Test(int n)
{
    printf("Test for %d begins:\n", n);
    
    printf("Test for solution1\n");
    PrintProbability_Solution1(n);

    printf("Test for solution2\n");
    PrintProbability_Solution2(n);

    printf("\n");
}

int main(int argc, char* argv[])
{
    Test(1);
    Test(2);
    Test(3);
    Test(4);
    
    Test(11);

    Test(0);

    return 0;
}
```


###  61_ContinousCards

// 面试题61：扑克牌的顺子

// 题目：从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。

// 2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王可以看成任意数字。


```c++
#include <cstdio>
#include <cstdlib>

int Compare(const void *arg1, const void *arg2);

bool IsContinuous(int* numbers, int length)
{
    if(numbers == nullptr || length < 1)
        return false;

    qsort(numbers, length, sizeof(int), Compare);

    int numberOfZero = 0;
    int numberOfGap = 0;

    // 统计数组中0的个数
    for(int i = 0; i < length && numbers[i] == 0; ++i)
        ++numberOfZero;

    // 统计数组中的间隔数目
    int small = numberOfZero;
    int big = small + 1;
    while(big < length)
    {
        // 两个数相等，有对子，不可能是顺子
        if(numbers[small] == numbers[big])
            return false;

        numberOfGap += numbers[big] - numbers[small] - 1;
        small = big;
        ++big;
    }

    return (numberOfGap > numberOfZero) ? false : true;
}

int Compare(const void *arg1, const void *arg2)
{
    return *(int*) arg1 - *(int*) arg2;
}

// ====================测试代码====================
void Test(const char* testName, int* numbers, int length, bool expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    if(IsContinuous(numbers, length) == expected)
        printf("Passed.\n");
    else
        printf("Failed.\n");
}

void Test1()
{
    int numbers[] = { 1, 3, 2, 5, 4 };
    Test("Test1", numbers, sizeof(numbers) / sizeof(int), true);
}

void Test2()
{
    int numbers[] = { 1, 3, 2, 6, 4 };
    Test("Test2", numbers, sizeof(numbers) / sizeof(int), false);
}

void Test3()
{
    int numbers[] = { 0, 3, 2, 6, 4 };
    Test("Test3", numbers, sizeof(numbers) / sizeof(int), true);
}

void Test4()
{
    int numbers[] = { 0, 3, 1, 6, 4 };
    Test("Test4", numbers, sizeof(numbers) / sizeof(int), false);
}

void Test5()
{
    int numbers[] = { 1, 3, 0, 5, 0 };
    Test("Test5", numbers, sizeof(numbers) / sizeof(int), true);
}

void Test6()
{
    int numbers[] = { 1, 3, 0, 7, 0 };
    Test("Test6", numbers, sizeof(numbers) / sizeof(int), false);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
    Test5();
    Test6();

}
```

### 62_LastNumberInCircle

// 面试题62：圆圈中最后剩下的数字

// 题目：0, 1, …, n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈里

// 删除第m个数字。求出这个圆圈里剩下的最后一个数字。


```c++
#include <cstdio>
#include <list>

using namespace std;

// ====================方法1====================
int LastRemaining_Solution1(unsigned int n, unsigned int m)
{
    if(n < 1 || m < 1)
        return -1;

    unsigned int i = 0;

    list<int> numbers;
    for(i = 0; i < n; ++ i)
        numbers.push_back(i);

    list<int>::iterator current = numbers.begin();
    while(numbers.size() > 1)
    {
        for(int i = 1; i < m; ++ i)
        {
            current ++;
            if(current == numbers.end())
                current = numbers.begin();
        }

        list<int>::iterator next = ++ current;
        if(next == numbers.end())
            next = numbers.begin();

        -- current;
        numbers.erase(current);
        current = next;
    }

    return *(current);
}

// ====================方法2====================
int LastRemaining_Solution2(unsigned int n, unsigned int m)
{
    if(n < 1 || m < 1)
        return -1;

    int last = 0;
    for (int i = 2; i <= n; i ++) 
        last = (last + m) % i;

    return last;
}

// ====================测试代码====================
void Test(const char* testName, unsigned int n, unsigned int m, int expected)
{
    if(testName != nullptr)
        printf("%s begins: \n", testName);

    if(LastRemaining_Solution1(n, m) == expected)
        printf("Solution1 passed.\n");
    else
        printf("Solution1 failed.\n");

    if(LastRemaining_Solution2(n, m) == expected)
        printf("Solution2 passed.\n");
    else
        printf("Solution2 failed.\n");

    printf("\n");
}

void Test1()
{
    Test("Test1", 5, 3, 3);
}

void Test2()
{
    Test("Test2", 5, 2, 2);
}

void Test3()
{
    Test("Test3", 6, 7, 4);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
}
```



###  63_MaximalProfit


// 面试题63：股票的最大利润

// 题目：假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖交易该股

// 票可能获得的利润是多少？例如一只股票在某些时间节点的价格为{9, 11, 8, 5,

// 7, 12, 16, 14}。如果我们能在价格为5的时候买入并在价格为16时卖出，则能

// 收获最大的利润11。


```c++
#include <cstdio>

int MaxDiff(const int* numbers, unsigned length)
{
    if(numbers == nullptr && length < 2)
        return 0;

    int min = numbers[0];
    int maxDiff = numbers[1] - min;

    for(int i = 2; i < length; ++i)
    {
        if(numbers[i - 1] < min)
            min = numbers[i - 1];

        int currentDiff = numbers[i] - min;
        if(currentDiff > maxDiff)
            maxDiff = currentDiff;
    }

    return maxDiff;
}

// ==================== Test Code ====================
void Test(const char* testName, const int* numbers, unsigned int length, int expected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    if(MaxDiff(numbers, length) == expected)
        printf("Passed.\n");
    else
        printf("FAILED.\n");
}

void Test1()
{
    int numbers[] = { 4, 1, 3, 2, 5 };
    Test("Test1", numbers, sizeof(numbers) / sizeof(int), 4);
}

// 价格递增
void Test2()
{
    int numbers[] = { 1, 2, 4, 7, 11, 16 };
    Test("Test2", numbers, sizeof(numbers) / sizeof(int), 15);
}

// 价格递减
void Test3()
{
    int numbers[] = { 16, 11, 7, 4, 2, 1 };
    Test("Test3", numbers, sizeof(numbers) / sizeof(int), -1);
}

// 价格全部相同
void Test4()
{
	int numbers[] = { 16, 16, 16, 16, 16 };
	Test("Test4", numbers, sizeof(numbers) / sizeof(int), 0);
}

void Test5()
{
    int numbers[] = { 9, 11, 5, 7, 16, 1, 4, 2 };
    Test("Test5", numbers, sizeof(numbers) / sizeof(int), 11);
}

void Test6()
{
    int numbers[] = { 2, 4 };
    Test("Test6", numbers, sizeof(numbers) / sizeof(int), 2);
}

void Test7()
{
    int numbers[] = { 4, 2 };
    Test("Test7", numbers, sizeof(numbers) / sizeof(int), -2);
}

void Test8()
{
	Test("Test8", nullptr, 0, 0);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
    Test5();
    Test6();
	 Test7();
	 Test8();

    return 0;
}
```


### 64_Accumulate

// 面试题64：求1+2+…+n

// 题目：求1+2+…+n，要求不能使用乘除法、for、while、if、else、switch、case

// 等关键字及条件判断语句（A?B:C）。

```c++
#include <cstdio>

// ====================方法一====================
class Temp
{
public:
    Temp() { ++ N; Sum += N; }

    static void Reset() { N = 0; Sum = 0; }
    static unsigned int GetSum() { return Sum; }

private:
    static unsigned int N;
    static unsigned int Sum;
};

unsigned int Temp::N = 0;
unsigned int Temp::Sum = 0;

unsigned int Sum_Solution1(unsigned int n)
{
    Temp::Reset();

    Temp *a = new Temp[n];
    delete []a;
    a = NULL;

    return Temp::GetSum();
}

// ====================方法二====================
class A;
A* Array[2];

class A
{
public:
    virtual unsigned int Sum (unsigned int n) 
    { 
        return 0; 
    }
};

class B: public A
{
public:
    virtual unsigned int Sum (unsigned int n) 
    { 
        return Array[!!n]->Sum(n-1) + n; 
    }
};

int Sum_Solution2(int n)
{
    A a;
    B b;
    Array[0] = &a;
    Array[1] = &b;

    int value = Array[1]->Sum(n);

    return value;
}

// ====================方法三====================
typedef unsigned int (*fun)(unsigned int);

unsigned int Solution3_Teminator(unsigned int n) 
{
    return 0;
}

unsigned int Sum_Solution3(unsigned int n)
{
    static fun f[2] = {Solution3_Teminator, Sum_Solution3}; 
    return n + f[!!n](n - 1);
}

// ====================方法四====================
template <unsigned int n> struct Sum_Solution4
{
    enum Value { N = Sum_Solution4<n - 1>::N + n};
};

template <> struct Sum_Solution4<1>
{
    enum Value { N = 1};
};

template <> struct Sum_Solution4<0>
{
    enum Value { N = 0};
};

// ====================测试代码====================
void Test(int n, int expected)
{
    printf("Test for %d begins:\n", n);

    if(Sum_Solution1(n) == expected)
        printf("Solution1 passed.\n");
    else
        printf("Solution1 failed.\n");

    if(Sum_Solution2(n) == expected)
        printf("Solution2 passed.\n");
    else
        printf("Solution2 failed.\n");

    if(Sum_Solution3(n) == expected)
        printf("Solution3 passed.\n");
    else
        printf("Solution3 failed.\n");
}

void Test1()
{
    const unsigned int number = 1;
    int expected = 1;
    Test(number, expected);
    if(Sum_Solution4<number>::N == expected)
        printf("Solution4 passed.\n");
    else
        printf("Solution4 failed.\n");
}

void Test2()
{
    const unsigned int number = 5;
    int expected = 15;
    Test(number, expected);
    if(Sum_Solution4<number>::N == expected)
        printf("Solution4 passed.\n");
    else
        printf("Solution4 failed.\n");
}

void Test3()
{
    const unsigned int number = 10;
    int expected = 55;
    Test(number, expected);
    if(Sum_Solution4<number>::N == expected)
        printf("Solution4 passed.\n");
    else
        printf("Solution4 failed.\n");
}

void Test4()
{
    const unsigned int number = 0;
    int expected = 0;
    Test(number, expected);
    if(Sum_Solution4<number>::N == expected)
        printf("Solution4 passed.\n");
    else
        printf("Solution4 failed.\n");
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();

    return 0;
}
```


### 65_AddTwoNumbers

// 面试题65：不用加减乘除做加法

// 题目：写一个函数，求两个整数之和，要求在函数体内不得使用＋、－、×、÷

// 四则运算符号。


```c++
#include <cstdio>

int Add(int num1, int num2)
{
    int sum, carry;
    do
    {
        sum = num1 ^ num2;
        carry = (num1 & num2) << 1;

        num1 = sum;
        num2 = carry;
    }
    while(num2 != 0);

    return num1;
}

// ====================测试代码====================
void Test(int num1, int num2, int expected)
{
    int result = Add(num1, num2);
    if(result == expected)
        printf("%d + %d is %d. Passed\n", num1, num2, result);
    else
        printf("%d + %d is %d. FAILED\n", num1, num2, result);
}

int main(int argc, char* argv[])
{
    Test(1, 2, 3);
    Test(111, 899, 1010);

    Test(-1, 2, 1);
    Test(1, -2, -1);

    Test(3, 0, 3);
    Test(0, -4, -4);

    Test(-2, -8, -10);

    return 0;
}
```


###  66_ConstuctArray

// 面试题66：构建乘积数组

// 题目：给定一个数组A[0, 1, …, n-1]，请构建一个数组B[0, 1, …, n-1]，其

// 中B中的元素B[i] =A[0]×A[1]×… ×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。


```c++
#include <cstdio>
#include <vector>

using namespace std;

void BuildProductionArray(const vector<double>& input, vector<double>& output)
{
    int length1 = input.size();
    int length2 = output.size();

    if(length1 == length2 && length2 > 1)
    {
        output[0] = 1;
        for(int i = 1; i < length1; ++i)
        {
            output[i] = output[i - 1] * input[i - 1];
        }

        double temp = 1;
        for(int i = length1 - 2; i >= 0; --i)
        {
            temp *= input[i + 1];
            output[i] *= temp;
        }
    }
}

//================= Test Code =================
static bool EqualArrays(const vector<double>& input, const vector<double>& output)
{
    int length1 = input.size();
    int length2 = output.size();

    if(length1 != length2)
        return false;

    for(int i = 0; i < length1; ++i)
    {
        if(abs(input[i] - output[i]) > 0.0000001)
            return false;
    }

    return true;
}

static void test(char* testName, const vector<double>& input, vector<double>& output, const vector<double>& expected)
{
    printf("%s Begins: ", testName);

    BuildProductionArray(input, output);
    if(EqualArrays(output, expected))
        printf("Passed.\n");
    else
        printf("FAILED.\n");
}

static void test1()
{
    // 输入数组中没有0
    double input[] = { 1, 2, 3, 4, 5 };
    double output[] = { 0, 0, 0, 0, 0 };
    double expected[] = { 120, 60, 40, 30, 24 };

    test("Test1", vector<double>(input, input + sizeof(input) / sizeof(double)),
        vector<double>(output, output + sizeof(output) / sizeof(double)),
        vector<double>(expected, expected + sizeof(expected) / sizeof(double)));
}

static void test2()
{
    // 输入数组中有一个0
    double input[] = { 1, 2, 0, 4, 5 };
    double output[] = { 0, 0, 0, 0, 0 };
    double expected[] = { 0, 0, 40, 0, 0 };

    test("Test2", vector<double>(input, input + sizeof(input) / sizeof(double)),
        vector<double>(output, output + sizeof(output) / sizeof(double)),
        vector<double>(expected, expected + sizeof(expected) / sizeof(double)));
}

static void test3()
{
    // 输入数组中有两个0
    double input[] = { 1, 2, 0, 4, 0 };
    double output[] = { 0, 0, 0, 0, 0 };
    double expected[] = { 0, 0, 0, 0, 0 };

    test("Test3", vector<double>(input, input + sizeof(input) / sizeof(double)),
        vector<double>(output, output + sizeof(output) / sizeof(double)),
        vector<double>(expected, expected + sizeof(expected) / sizeof(double)));
}

static void test4()
{
    // 输入数组中有正、负数
    double input[] = { 1, -2, 3, -4, 5 };
    double output[] = { 0, 0, 0, 0, 0 };
    double expected[] = { 120, -60, 40, -30, 24 };

    test("Test4", vector<double>(input, input + sizeof(input) / sizeof(double)),
        vector<double>(output, output + sizeof(output) / sizeof(double)),
        vector<double>(expected, expected + sizeof(expected) / sizeof(double)));
}

static void test5()
{
    // 输入输入中只有两个数字
    double input[] = { 1, -2 };
    double output[] = { 0, 0 };
    double expected[] = { -2, 1 };

    test("Test5", vector<double>(input, input + sizeof(input) / sizeof(double)),
        vector<double>(output, output + sizeof(output) / sizeof(double)),
        vector<double>(expected, expected + sizeof(expected) / sizeof(double)));
}

int main(int argc, char* argv[])
{
    test1();
    test2();
    test3();
    test4();
    test5();

    return 0;
}
```


### 67_StringToInt


// 面试题67：把字符串转换成整数

// 题目：请你写一个函数StrToInt，实现把字符串转换成整数这个功能。当然，不

// 能使用atoi或者其他类似的库函数


```c++
#include <cstdio>

long long StrToIntCore(const char* str, bool minus);

enum Status {kValid = 0, kInvalid};
int g_nStatus = kValid;

int StrToInt(const char* str)
{
    g_nStatus = kInvalid;
    long long num = 0;

    if(str != nullptr && *str != '\0') 
    {
        bool minus = false;
        if(*str == '+')
            str ++;
        else if(*str == '-') 
        {
            str ++;
            minus = true;
        }

        if(*str != '\0') 
            num = StrToIntCore(str, minus);
    }

    return (int)num;
}

long long StrToIntCore(const char* digit, bool minus)
{
    long long num = 0;

    while(*digit != '\0') 
    {
        if(*digit >= '0' && *digit <= '9') 
        {
            int flag = minus ? -1 : 1;
            num = num * 10 + flag * (*digit - '0');

            if((!minus && num > 0x7FFFFFFF) 
                || (minus && num < (signed int)0x80000000))
            {
                num = 0;
                break;
            }

            digit++;
        }
        else 
        {
            num = 0;
            break;
        }
    }

    if(*digit == '\0') 
        g_nStatus = kValid;

    return num;
}

// ====================测试代码====================
void Test(const char* string)
{
    int result = StrToInt(string);
    if(result == 0 && g_nStatus == kInvalid)
        printf("the input %s is invalid.\n", string);
    else
        printf("number for %s is: %d.\n", string, result);
}

int main(int argc, char* argv[])
{
    Test(nullptr);

    Test("");

    Test("123");

    Test("+123");
    
    Test("-123");

    Test("1a33");

    Test("+0");

    Test("-0");

    //有效的最大正整数, 0x7FFFFFFF
    Test("+2147483647");    

    Test("-2147483647");

    Test("+2147483648");

    //有效的最小负整数, 0x80000000
    Test("-2147483648");    

    Test("+2147483649");

    Test("-2147483649");

    Test("+");

    Test("-");

    return 0;
}
```


### 68_CommonParentInTree

// 面试题68：树中两个结点的最低公共祖先

// 题目：输入两个树结点，求它们的最低公共祖先。


```c++
#include <cstdio>
#include "..\Utilities\Tree.h"
#include <list>

using namespace std;

bool GetNodePath(const TreeNode* pRoot, const TreeNode* pNode, list<const TreeNode*>& path)
{
    if(pRoot == pNode)
        return true;
 
    path.push_back(pRoot);
 
    bool found = false;

    vector<TreeNode*>::const_iterator i = pRoot->m_vChildren.begin();
    while(!found && i < pRoot->m_vChildren.end())
    {
        found = GetNodePath(*i, pNode, path);
        ++i;
    }
 
    if(!found)
        path.pop_back();
 
    return found;
}

const TreeNode* GetLastCommonNode
(
    const list<const TreeNode*>& path1, 
    const list<const TreeNode*>& path2
)
{
    list<const TreeNode*>::const_iterator iterator1 = path1.begin();
    list<const TreeNode*>::const_iterator iterator2 = path2.begin();
    
    const TreeNode* pLast = nullptr;
 
    while(iterator1 != path1.end() && iterator2 != path2.end())
    {
        if(*iterator1 == *iterator2)
            pLast = *iterator1;
 
        iterator1++;
        iterator2++;
    }
 
    return pLast;
}

const TreeNode* GetLastCommonParent(const TreeNode* pRoot, const TreeNode* pNode1, const TreeNode* pNode2)
{
    if(pRoot == nullptr || pNode1 == nullptr || pNode2 == nullptr)
        return nullptr;
 
    list<const TreeNode*> path1;
    GetNodePath(pRoot, pNode1, path1);
 
    list<const TreeNode*> path2;
    GetNodePath(pRoot, pNode2, path2);
 
    return GetLastCommonNode(path1, path2);
}

// ====================测试代码====================
void Test(const char* testName, const TreeNode* pRoot, const TreeNode* pNode1, const TreeNode* pNode2, TreeNode* pExpected)
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    const TreeNode* pResult = GetLastCommonParent(pRoot, pNode1, pNode2);

    if((pExpected == nullptr && pResult == nullptr) || 
        (pExpected != nullptr && pResult != nullptr && pResult->m_nValue == pExpected->m_nValue))
        printf("Passed.\n");
    else
        printf("Failed.\n");
}

// 形状普通的树
//              1
//            /   \
//           2     3
//       /       \
//      4         5
//     / \      / |  \
//    6   7    8  9  10
void Test1()
{
    TreeNode* pNode1 = CreateTreeNode(1);
    TreeNode* pNode2 = CreateTreeNode(2);
    TreeNode* pNode3 = CreateTreeNode(3);
    TreeNode* pNode4 = CreateTreeNode(4);
    TreeNode* pNode5 = CreateTreeNode(5);
    TreeNode* pNode6 = CreateTreeNode(6);
    TreeNode* pNode7 = CreateTreeNode(7);
    TreeNode* pNode8 = CreateTreeNode(8);
    TreeNode* pNode9 = CreateTreeNode(9);
    TreeNode* pNode10 = CreateTreeNode(10);

    ConnectTreeNodes(pNode1, pNode2);
    ConnectTreeNodes(pNode1, pNode3);

    ConnectTreeNodes(pNode2, pNode4);
    ConnectTreeNodes(pNode2, pNode5);

    ConnectTreeNodes(pNode4, pNode6);
    ConnectTreeNodes(pNode4, pNode7);

    ConnectTreeNodes(pNode5, pNode8);
    ConnectTreeNodes(pNode5, pNode9);
    ConnectTreeNodes(pNode5, pNode10);

    Test("Test1", pNode1, pNode6, pNode8, pNode2);
}

// 树退化成一个链表
//               1
//              /
//             2
//            /
//           3
//          /
//         4
//        /
//       5
void Test2()
{
    TreeNode* pNode1 = CreateTreeNode(1);
    TreeNode* pNode2 = CreateTreeNode(2);
    TreeNode* pNode3 = CreateTreeNode(3);
    TreeNode* pNode4 = CreateTreeNode(4);
    TreeNode* pNode5 = CreateTreeNode(5);

    ConnectTreeNodes(pNode1, pNode2);
    ConnectTreeNodes(pNode2, pNode3);
    ConnectTreeNodes(pNode3, pNode4);
    ConnectTreeNodes(pNode4, pNode5);

    Test("Test2", pNode1, pNode5, pNode4, pNode3);
}

// 树退化成一个链表，一个结点不在树中
//               1
//              /
//             2
//            /
//           3
//          /
//         4
//        /
//       5
void Test3()
{
    TreeNode* pNode1 = CreateTreeNode(1);
    TreeNode* pNode2 = CreateTreeNode(2);
    TreeNode* pNode3 = CreateTreeNode(3);
    TreeNode* pNode4 = CreateTreeNode(4);
    TreeNode* pNode5 = CreateTreeNode(5);

    ConnectTreeNodes(pNode1, pNode2);
    ConnectTreeNodes(pNode2, pNode3);
    ConnectTreeNodes(pNode3, pNode4);
    ConnectTreeNodes(pNode4, pNode5);

    TreeNode* pNode6 = CreateTreeNode(6);

    Test("Test3", pNode1, pNode5, pNode6, nullptr);
}

// 输入nullptr
void Test4()
{
    Test("Test4", nullptr, nullptr, nullptr, nullptr);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();

    return 0;
}
```






