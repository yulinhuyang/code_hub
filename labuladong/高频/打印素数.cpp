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
