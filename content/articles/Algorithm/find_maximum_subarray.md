Title: 最大子数组问题
Category: 读书笔记
Date: 2018-10-27 22:26:28
Modified: 2018-10-28 13:02:31
Tags: 算法

[TOC]

寻找数组中和最大的非空连续子数组。

## 1. 暴力求解

先找出从第1个元素开始的最大子数组，而后再从第2个元素开始找出从第2个元素开始的最大子数组，依次类推，比较得出最大的子数组。

时间复杂度 $O(n^2)$。

```
#include <tuple>

typedef std::tuple<int, int, int> array_info_message;
array_info_message find_max_subarray(int a[], int len) {
        int i, j;
        int sum = 0;
        int max_left, max_right; //每次开始累加的起始位置的循环
        for (i = 0; i < len; i++) {
                max_left = i;
                int temp = 0;
                //向后累加的循环
                for (j = i; j < len; j++) {
                        temp += a[j];
                        if (temp > sum) {
                                sum = temp;
                                max_right = j;
                        }
                }
        }
        return std::make_tuple(max_left, max_right, sum);
}
```

## 2. 分治算法

时间复杂度 $O(nlgn)$。

```
#include <limits>
#include <tuple>

typedef std::tuple<int, int, int> array_info_message;

void find_max_cross_subarray(int a[], int low, int mid,
                                           int high) {
        int left_sum = std::numeric_limits<int>::min();
        int right_sum = std::numeric_limits<int>::min();
        int sum = 0;
        int max_left = mid;
        int max_right = mid;
        for (int i = mid; i >= low; --i) {
                sum += a[i];
                if (left_sum < sum) {
                        left_sum = sum;
                        max_left = i;
                }
        }
        sum = 0;
        for (int i = mid + 1; i <= high; ++i) {
                sum += a[i];
                if (right_sum < sum) {
                        right_sum = sum;
                        max_right = i;
                }
        }
        return std::make_tuple(max_left, max_right, left_sum + right_sum);
}

array_info_message find_max_subarray(int a[], int low, int high) {
        array_info_message r1, r2, r3;
        if (low == high)
                return std::make_tuple(low, high, a[low]);
        else {
                // 第一次这里处理成减号了，找了半天 bug
                int mid = static_cast<int>((high + low) / 2);
                r1 = find_max_subarray(a, low, mid);
                r2 = find_max_subarray(a, mid + 1, high);
                r3 = find_max_cross_subarray(a, low, mid, high);
                if (std::get<2>(r1) >= std::get<2>(r2) &&
                    std::get<2>(r1) >= std::get<2>(r3))
                        return r1;
                if ((std::get<2>(r2) >= std::get<2>(r1) &&
                     std::get<2>(r2) >= std::get<2>(r3)))
                        return r2;
                if ((std::get<2>(r3) >= std::get<2>(r1) &&
                     std::get<2>(r3) >= std::get<2>(r2)))
                        return r3;
        }
        return std::make_tuple(0, 0, 0);
}
```

## 3. 动态规划：Kadane 算法

Kadane 算法扫描一次整个数列的所有数值，在每一个扫描点计算以该点数值为结束点的子数列的最大和（正数和）。该子数列由两部分组成：以前一个位置为结束点的最大子数列、该位置的数值。因为该算法用到了“最佳子结构”（以每个位置为终点的最大子数列都是基于其前一位置的最大子数列计算得出）。

Kadane 算法时间复杂度为 $O(n)$，空间复杂度为 $O(1)$。

```
array_info_message find_max_subarray(int a[], int n) {
    void maxSubArray(int a[], int n) {
    int max = std::numeric_limits<int>::min();
    int sum = 0;
    int left = 0, right = 0, max_left = 0, max_right = 0;
    for (int i = 0; i < n; i++) {
            if (sum + a[i] > a[i]) {
                    sum = sum + a[i];
                    right = i;
            } else {
                    sum = a[i];
                    left = i;
                    right = i;
            }
            if (sum > max) {
                    max = sum;
                    max_left = left;
                    max_right = right;
            }
    }
    return std::make_tuple(max_left, max_right, max);
}
```

若我们只需要求最大和，则有如下简洁解法：

```
int find_max_subarray(int a[], int n) {
        int max = std::numeric_limits<int>::min();
        int sum = 0;
        for (int i = 0; i < n; i++) {
                sum = sum + a[i] > a[i] ? sum + a[i] : a[i];
                max = sum > max ? sum : max;
        }
        return max;
}
```
