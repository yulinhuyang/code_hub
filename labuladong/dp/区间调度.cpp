public int intervalSchedule(int[][] intvs) {
    if (intvs.length == 0) return 0;
    // 按 end 升序排序
    Arrays.sort(intvs, new Comparator<int[]>() {
        @Override
        public int compare(int[] a, int[] b) {
            // 这里不能使用 a[1] - b[1]，要注意溢出问题
            if (a[1] < b[1])
                return -1;
            else if (a[1] > b[1])
                return 1;
            else return 0;
        }
    });
    // 至少有一个区间不相交
    int count = 1;
    // 排序后，第一个区间就是 x
    int x_end = intvs[0][1];
    for (int[] interval : intvs) {
        int start = interval[0];
        if (start >= x_end) {
            // 找到下一个选择的区间了
            count++;
            x_end = interval[1];
        }
    }
    return count;
}
