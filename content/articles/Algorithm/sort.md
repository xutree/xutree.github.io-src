Title: 排序算法
Category: 读书笔记
Date: 2018-10-26 23:08:38
Modified: 2018-10-27 22:28:38
Tags: 算法

## 插入排序

插入排序（英语：Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在实现上，通常采用 in-place 排序（即只需用到 $O(1)$ 的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。


```
void insertion_sort(int arr[], int len) {
        for (int i = 1; i < len; i++) {
                int key = arr[i];
                int j;
                for (j = i - 1; j >= 0 && key < arr[j]; j--) {
                        arr[j + 1] = arr[j];
                        arr[j] = key;
                }
        }
}
```

如果目标是把 $n$ 个元素的序列升序排列，那么采用插入排序存在最好情况和最坏情况。最好情况就是，序列已经是升序排列了，在这种情况下，需要进行的比较操作需 $n-1$ 次即可。最坏情况就是，序列是降序排列，那么此时需要进行的比较共有 $\frac {1}{2}n(n-1)$ 次。插入排序的赋值操作是比较操作的次数减去 $n-1$ 次，（因为 $n-1$ 次循环中，每一次循环的比较都比赋值多一个，多在最后那一次比较并不带来赋值）。平均来说插入排序算法复杂度为 $O(n^{2})$。因而，插入排序不适合对于数据量比较大的排序应用。但是，如果需要排序的数据量很小，例如，量级小于千；或者若已知输入元素大致上按照顺序排列，那么插入排序还是一个不错的选择。 插入排序在工业级库中也有着广泛的应用，在 STL 的 sort 算法和 stdlib 的 qsort 算法中，都将插入排序作为快速排序的补充，用于少量元素的排序（通常为8个或以下）。

## 归并排序

归并排序（英语：Merge sort，或 mergesort），是创建在归并操作上的一种有效的排序算法，效率为 $O(n\log n)$。1945年由约翰·冯·诺伊曼首次提出。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用，且各层分治递归可以同时进行。

```
template <typename Iterator>
void merge(Iterator begin, Iterator end, Iterator middle) {
        typedef typename std::iterator_traits<Iterator>::value_type
                T; // 迭代器指向对象的值类型
        if (std::distance(begin, middle) <= 0 || std::distance(middle, end) <= 0)
                return;
        std::vector<T> result(begin, end); //暂存结果
        auto current = result.begin();
        auto left_current = begin; //左侧序列当前比较位置
        auto right_current = middle; //右序列当前比较位置
        while (left_current != middle && right_current != end) {
                if (*left_current < *right_current) {
                        *current++ = *left_current++; //左侧较小

                } else {
                        *current++ = *right_current++; //左侧较小
                }
        }
        if (left_current == middle && right_current != end) //当左侧序列为搬空
        {
                std::copy(right_current, end, current);
        }
        if (right_current == end && left_current != middle) //当右侧序列搬空
        {
                std::copy(left_current, middle, current);
        }
        std::copy(result.begin(), result.end(),
                  begin); //复制回原序列，因此是非原地的
}

template <typename Iterator> void merge_sort(Iterator begin, Iterator end) {
        auto size = std::distance(begin, end);
        if (size > 1) {
                Iterator middle = begin + size / 2;
                merge_sort(begin, middle);
                merge_sort(middle, end);
                merge(begin, end, middle);
        }
}
```

比较操作的次数介于 $\frac{1}{2}n\log n$ 和 $n\log n-n+1$ 之间。 赋值操作的次数是 $2n\log n$。归并算法的空间复杂度为：$\Theta (n)$。
