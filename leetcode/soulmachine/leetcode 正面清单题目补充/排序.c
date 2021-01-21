
//直接插入排序

/** 数组元素的类型 */
typedef int elem_t;

/**
  * @brief 直接插入排序，时间复杂度O(n^2).
  *
  * @param[inout] a 待排序元素序列
  * @param[in] start 开始位置
  * @param[in] end 结束位置，最后一个元素后一个位置，即左闭右开区间
  * @return 无
  */
void straight_insertion_sort(elem_t a[], const int start, const int end) {
    elem_t tmp;
    int i, j;

    for (i = start + 1; i < end; i++) {
        tmp = a[i];
        for (j = i - 1; tmp < a[j] && j >= start; j--) {
            a[j + 1] = a[j];
        }
        a[j + 1] = tmp;
    }
}



/**
  * @brief 折半插入排序，时间复杂度O(nlog2n).
  *
  * @param[inout] a 待排序元素序列
  * @param[in] start 开始位置
  * @param[in] end 结束位置，最后一个元素后一个位置
  * @return 无
  */
void binary_insertion_sort(elem_t a[], const int start, const int end) {
    elem_t tmp;
    int i, j, left, right, mid;

    for (i = start + 1; i < end; i++) {
        tmp = a[i];
        left = start;
        right = i - 1;
        while (left <= right) {
            mid = (left + right) / 2;
            if (tmp < a[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        for (j = i - 1;j >= left; j--) {
            a[j + 1] = a[j];
        }
        a[left] = tmp;
    }
}



//希尔排序
/*
  * @brief 一趟希尔插入排序.
  *
  * 和一趟直接插入排序相比，仅有一点不同，就是前后元素的间距是gap而不是1
  *
  * @param[inout] a 待排序元素序列
  * @param[in] start 开始位置
  * @param[in] end 结束位置，最后一个元素后一个位置，即左闭右开区间
  * @param[in] gap 间隔
  * @return 无
  */
static void shell_insert(elem_t a[], const int start, const int end, const int gap) {
    elem_t tmp;
    int i, j;
    for (i = start + gap; i < end; i++) {
        tmp = a[i];
        for (j = i - gap; tmp < a[j] && j >= start; j -= gap) {
            a[j + gap] = a[j];
        }
        a[j + gap] = tmp;
    }
}


 /*
  * @brief 希尔排序.
  * @param[inout] a 待排序元素序列
  * @param[in] start 开始位置
  * @param[in] end 结束位置，最后一个元素后一个位置，即左闭右开区间
  * @return 无
  */
void shell_sort(elem_t a[], const int start, const int end) {
    int gap = end - start;
    while (gap > 1) {
        gap = gap / 3 + 1;
        shell_insert(a, start, end, gap);
    }
}




/** 数组元素的类型 */
typedef int elem_t;

/**
  * @brief 冒泡排序.
  * @param[inout] a 待排序元素序列
  * @param[in] start 开始位置
  * @param[in] end 结束位置，最后一个元素后一个位置，即左闭右开区间
  * @return 无
  * @note 无
  * @remarks 无
  */
void bubble_sort(elem_t a[], const int start, const int end) {
    int exchange; /* 是否发生交换*/
    elem_t tmp;
    int i, j;

    for (i = start; i < end - 1; i++) {
        exchange = 0;
        for (j = end - 1; j > i; j--) { /* 发生逆序，交换*/
            if (a[j - 1] > a[j]) {
                tmp = a[j - 1];
                a[j - 1] = a[j];
                a[j] = tmp;
                exchange = 1;
            }
        }
        if (exchange == 0) return; /* 本趟无逆序，停止处理*/
    }
}




//快速排序
/** 数组元素的类型 */
typedef int elem_t;
 /*
  * @brief 一趟划分.
  * @param[inout] a 待排序元素序列
  * @param[in] start 开始位置
  * @param[in] end 结束位置，最后一个元素后一个位置，即左闭右开区间
  * @return 基准元素的新位置
  */
int partition(elem_t a[], const int start, const int end) {
    int i = start;
    int j = end - 1;
    const elem_t pivot = a[i];

    while(i < j) {
        while(i < j && a[j] >= pivot) j--;
        a[i] = a[j];
        while(i < j && a[i] <= pivot) i++;
        a[j] = a[i];
    }
    a[i] = pivot;
    return i;
}

/**
  * @brief 快速排序.
  * @param[inout] a 待排序元素序列
  * @param[in] start 开始位置
  * @param[in] end 结束位置，最后一个元素后一个位置
  * @return 无
  */
void quick_sort(elem_t a[], const int start, const int end) {
    if(start < end - 1) { /* 至少两个元素*/
        const int pivot_pos = partition(a, start, end);
        quick_sort(a, start, pivot_pos);
        quick_sort(a, pivot_pos + 1, end);
    }
}



//简单选择排序
/** 数组元素的类型 */
typedef int elem_t;

/**
  * @brief 简单选择排序.
  * @param[inout] a 待排序元素序列
  * @param[in] start 开始位置
  * @param[in] end 结束位置，最后一个元素后一个位置，即左闭右开区间
  * @return 无
  */
void simple_selection_sort(elem_t a[], int start, int end) {
    elem_t tmp;
    int i, j, k;

    for (i = start; i < end; i++) {
        k = i;
        /* 在a[i]到a[end-1]中寻找最小元素*/
        for (j = i + 1; j < end; j++)
            if(a[j] < a[k]) k = j;
        /* 交换*/
        if (k != i) {
            tmp = a[i];
            a[i] = a[k];
            a[k]= tmp;
        }
    }
}




//归并排序
 /** 数组元素的类型 */
typedef int elem_t;

 /*
  * @brief 将两个有序表合并成一个新的有序表
  * @param[inout] a 待排序元素序列，包含两个有序表
  * @param[in] tmp 与a等长的辅助数组
  * @param[in] start a[start]~a[mid-1]为第一个有序表
  * @param[in] mid 分界点
  * @param[in] end a[mid]~a[end-1]为第二个有序表
  * @return 无
  */
static void merge(elem_t a[], elem_t tmp[], const int start, 
        const int mid, const int end) {
    int i, j, k;
    for (i = 0; i < end; i++) tmp[i] = a[i];

    /* i, j是检测指针，k是存放指针*/
    for (i = start, j = mid, k = start; i < mid && j < end; k++) {
        if (tmp[i] < tmp[j]) {
            a[k] = tmp[i++];
        } else {
            a[k] = tmp[j++];
        }
    }
    /* 若第一个表未检测完，复制*/
    while (i < mid) a[k++] = tmp[i++];
    /* 若第二个表未检测完，复制*/
    while (j < end) a[k++] = tmp[j++];
}

/**
  * @brief 归并排序.
  * @param[inout] a 待排序元素序列
  * @param[in] tmp 与a等长的辅助数组
  * @param[in] start 开始位置
  * @param[in] end 结束位置，最后一个元素后一个位置，即左闭右开区间
  * @return 无
  * @note 无
  * @remarks 无
  */
void merge_sort(elem_t a[], elem_t tmp[], const int start, const int end) {
    if (start < end - 1) {
        const int mid = (start + end) / 2;
        merge_sort(a, tmp, start, mid);
        merge_sort(a, tmp, mid, end);
        merge(a, tmp, start, mid, end);
    }
}

