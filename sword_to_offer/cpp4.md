### 36_ConvertBinarySearchTree

// 面试题36：二叉搜索树与双向链表

// 题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求

// 不能创建任何新的结点，只能调整树中结点指针的指向。



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


###  37_SerializeBinaryTrees

// 面试题37：序列化二叉树
// 题目：请实现两个函数，分别用来序列化和反序列化二叉树。


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


    ###  38_StringPermutation

    // 面试题38：字符串的排列
    // 题目：输入一个字符串，打印出该字符串中字符的所有排列。例如输入字符串abc，
    // 则打印出由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。

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


###  39_MoreThanHalfNumber

// 面试题39：数组中出现次数超过一半的数字

// 题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例

// 如输入一个长度为9的数组{1, 2, 3, 2, 2, 2, 5, 4, 2}。由于数字2在数组中

// 出现了5次，超过数组长度的一半，因此输出2。

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


### 40_KLeastNumbers

// 面试题40：最小的k个数
// 题目：输入n个整数，找出其中最小的k个数。例如输入4、5、1、6、2、7、3、8
// 这8个数字，则最小的4个数字是1、2、3、4。


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


### 41_StreamMedian

// 面试题41：数据流中的中位数

// 题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么

// 中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，

// 那么中位数就是所有数值排序之后中间两个数的平均值。

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


### 42_GreatestSumOfSubarrays

// 面试题42：连续子数组的最大和

// 题目：输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整

// 数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)。

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


### 43_NumberOf1

// 面试题43：从1到n整数中1出现的次数

// 题目：输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数。例如

// 输入12，从1到12这些整数中包含1 的数字有1，10，11和12，1一共出现了5次。

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



