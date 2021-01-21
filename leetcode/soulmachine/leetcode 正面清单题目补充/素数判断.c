

/**
 * @brief 判断正整数n是否是素数
 * @param[in] n 正整数
 * @return 是，返回1，否，返回0
 */
int is_prime(unsigned int n) {
    int i;
    if (n < 2) return 0;
    for (i = 2; i < n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}


/**
 * @brief 判断正整数n是否是素数，上界改为sqrt(n)
 * @param[in] n 正整数
 * @return 是，返回1，否，返回0
 */
int is_prime(unsigned int n) {
    int i;
    if (n < 2) return 0;
    const int upper = sqrt(n);

    for (i = 2; i <= upper; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

/**
 * @brief 判断正整数n是否是素数，上界改为sqrt(n)，但不使用sqrt()函数
 * @param[in] n 正整数
 * @return 是，返回1，否，返回0
 */
int is_prime1(unsigned int n) {
    int i;
    if (n < 2) return 0;
    for (i = 2; i*i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}