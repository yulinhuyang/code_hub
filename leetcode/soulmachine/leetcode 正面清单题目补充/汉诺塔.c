#include <stdio.h>
/*
    * @brief 将塔座 x 上按直径有小到大且自上而下编号
    * 为 1 至 n 的 n 个圆盘按规则搬到塔座 z 上，y 可用做辅助塔座.
    * @param[in] n 圆盘个数
    * @param[in] x 源塔座
    * @param[in] y 辅助塔座
    * @param[in] z 目标塔座
    * @return 无
*/
void hanoi(int n, char x, char y, char z) {
    if(n == 1) {
        /* 将编号为 n 的圆盘从 x 移到 z */
        printf("%d from %c to %c\n", n, x, z);
        return;
    } else {
        /* 将 x 上编号 1 至 n-1 的圆盘移到 y，z 作辅助塔 */
        hanoi(n-1, x, z, y);
        /* 将编号为 n 的圆盘从 x 移到 z */
        printf("%d from %c to %c\n", n, x, z);
        /* 将 y 上编号 1 至 n-1 的圆盘移到 z，x 作辅助塔 */
        hanoi(n-1, y, x, z);
    } 
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", (1 << n) - 1); /* 总次数 */
    hanoi(n, 'A', 'B', 'C');
    return 0;
}