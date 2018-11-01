Title: 排序算法
Category: 读书笔记
Date: 2018-10-26 23:08:38
Modified: 2018-11-01 16:47:24
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

- 最坏时间复杂度：$O(n^2)$
- 最优时间复杂度：$O(n)$
- 平均时间复杂度：$\Theta (n^2)$
- 最坏空间复杂度：$O(1)$
- 稳定排序

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

- 最坏时间复杂度：$O(n\log n)$
- 最优时间复杂度：$\Omega(n \log n)$
- 平均时间复杂度：$\Theta (n\log n)$
- 最坏空间复杂度：$O(n)$
- 稳定排序

## 堆排序

堆排序（英语：Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

### 堆节点的访问

通常堆是通过一维数组来实现的。在数组起始位置为0的情形中：

- 父节点 $i$ 的左子节点在位置 $2i+1$
- 父节点 $i$ 的右子节点在位置 $2i+2$
- 子节点 $i$ 的父节点在位置 $\text{floor}((i-1)/2)$

### 堆的操作

堆中定义以下几种操作：

- 最大堆调整（Max Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
- 创建最大堆（Build Max Heap）：将堆中的所有数据重新排序
- 堆排序（HeapSort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算

```
#include <iostream>
using namespace std;

//最大堆调整，i 为要调整节点，n 为最大堆尺寸
void max_heapify(int arr[], int n, int i) {
        int largest = i;
        int l = 2 * i + 1; //左孩子
        int r = 2 * i + 2; //右孩子
        if (l < n && arr[l] > arr[largest])
                largest = l;
        if (r < n && arr[r] > arr[largest])
                largest = r;
        if (largest != i) {
                swap(arr[i], arr[largest]);
                heapify(arr, n, largest);
        }
}

//堆排序
void heapSort(int arr[], int n) {
        //建堆
        for (int i = n / 2 - 1; i >= 0; i--)
                max_heapify(arr, n, i);
        //排序
        for (int i = n - 1; i >= 0; i--) {
                //交换堆顶和尾元素
                swap(arr[0], arr[i]);
                max_heapify(arr, i, 0);
        }
}

void printArray(int arr[], int n) {
        for (int i = 0; i < n; ++i)
                cout << arr[i] << " ";
        cout << "\n";
}

int main() {
        int arr[] = {12, 11, 13, 5, 6, 7};
        int n = sizeof(arr) / sizeof(arr[0]);
        heapSort(arr, n);
        cout << "Sorted array is \n";
        printArray(arr, n);
}
```

- 最坏时间复杂度：$O(n\log n)$
- 最优时间复杂度：$O(n\log n)$
- 平均时间复杂度：$\Theta (n\log n)$
- 最坏空间复杂度：$O(1)$
- 不稳定排序

## 快速排序

快速排序（英语：Quicksort），又称划分交换排序（partition-exchange sort），简称快排，一种排序算法，最早由东尼·霍尔提出。在平均状况下，排序 $n$ 个项目要 $O(n\log n)$ 次比较。在最坏状况下则需要 $O(n^{2})$ 次比较，但这种状况并不常见。事实上，快速排序 $\Theta (n\log n)$ 通常明显比其他算法更快，因为它的内部循环（inner loop）可以在大部分的架构上很有效率地达成。

快速排序是二叉查找树（二叉搜索树）的一个空间最优化版本。不是循序地把数据项插入到一个明确的树中，而是由快速排序组织这些数据项到一个由递归调用所隐含的树中。这两个算法完全地产生相同的比较次数，但是顺序不同。对于排序算法的稳定性指标，原地分割版本的快速排序算法是不稳定的。其他变种是可以通过牺牲性能和空间来维护稳定性的。

```
template <typename T>
void quick_sort_recursive(T arr[], int start, int end) {
    if (start >= end)
        return;
    T mid = arr[end];
    int left = start, right = end - 1;
    while (left < right) { //在整个范围内搜寻比枢纽元值小或大的元素，然后将左侧元素与右侧元素交换
        while (arr[left] < mid && left < right) //试图在左侧找到一个比枢纽元更大的元素
            left++;
        while (arr[right] >= mid && left < right) //试图在右侧找到一个比枢纽元更小的元素
            right--;
        std::swap(arr[left], arr[right]); //交换元素
    }
    if (arr[left] >= arr[end])
        std::swap(arr[left], arr[end]);
    else
        left++;
    quick_sort_recursive(arr, start, left - 1);
    quick_sort_recursive(arr, left + 1, end);
}
template <typename T> //整数或浮点数皆可使用,若要使用类时必須定义"小于"(<)、"大于"(>)、"不小于"(>=)操作
void quick_sort(T arr[], int len) {
    quick_sort_recursive(arr, 0, len - 1);
}
```

### 随机算法

当划分产生的两个子问题分别包含 $n-1$ 和0个元素时，最坏情况发生。划分操作的时间复杂度为 $\Theta(n)$，$T(0)=\Theta(1)$，这时算法运行时间的递归式为：$T(n) = T(n-1) + T(0) + \Theta(n) = T(n-1) + \Theta(n)$，解为 $T(n) = \Theta(n^2)$。

当划分产生的两个子问题分别包含 $\lfloor n/2 \rfloor$ 和 $\lceil n/2 \rceil-1$ 个元素时，最好情况发生。算法运行时间递归式为：$T(n) = 2T(n/2) + \Theta(n)$，解为 $T(n) = \Theta(n\lg n)$。


可以通过在算法中引入随机性，使得算法对所有输入都能获得较好的期望性能。随机算法保证了对任何的输入而言，都可以保证 $\Theta (n\lg n)$ 的时间复杂度。

```
void rand_quick_sort(T arr[], int begin, int end){
    if (end-begin <= 1)
        return;

    int pindex = rand() % (end-begin) + begin;
    std::swap(arr[end-1], arr[pindex]);

    quick_sort(arr, end - begin + 1);
}
```

- 最坏时间复杂度：$\Theta(n^2)$
- 最优时间复杂度：$\Theta(n\log n)$
- 平均时间复杂度：$\Theta (n\log n)$
- 空间复杂度：$O(\log n)$
- 不稳定排序
