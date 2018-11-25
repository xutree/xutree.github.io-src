Title: 排序算法
Category: 读书笔记
Date: 2018-10-26 23:08:38
Modified: 2018-11-01 22:21:00
Tags: 算法

[TOC]

## 1. 插入排序

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

## 2. 归并排序

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

## 3. 堆排序

堆排序（英语：Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

### 3.1 堆节点的访问

通常堆是通过一维数组来实现的。在数组起始位置为0的情形中：

- 父节点 $i$ 的左子节点在位置 $2i+1$
- 父节点 $i$ 的右子节点在位置 $2i+2$
- 子节点 $i$ 的父节点在位置 $\text{floor}((i-1)/2)$

### 3.2 堆的操作

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

## 4. 快速排序

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

## 5. 计数排序

计数排序（Counting sort）是一种稳定的线性时间排序算法。计数排序使用一个额外的数组 $C$ ，其中第 $i$ 个元素是待排序数组 $A$ 中值等于 $i$ 的元素的个数。然后根据数组 $C$ 来将 $A$ 中的元素排到正确的位置。

当输入的元素是 $n$ 个 $[0,k]$ 之间的整数时，它的运行时间是 $\Theta (n+k)$。计数排序不是比较排序，排序的速度快于任何比较排序算法。

由于用来计数的数组 $C$ 的长度取决于待排序数组中数据的范围（等于待排序数组的最大值与最小值的差加上1），这使得计数排序对于数据范围很大的数组，需要大量时间和内存。例如：计数排序是用来排序0到100之间的数字的最好的算法，但是它不适合按字母顺序排序人名。但是，计数排序可以用在基数排序算法中，能够更有效的排序数据范围很大的数组。

当原数组有重复数据时，为保证稳定排序，最后要反向填充目标数组，以及将每个数字的统计减去1。

### 步骤

- 找出待排序的数组中最大和最小的元素
- 统计数组中每个值为 $i$ 的元素出现的次数，存入数组 $C$ 的第 $i$ 项
- 对所有的计数累加（从 $C$ 中的第一个元素开始，每一项和前一项相加）
- 反向填充目标数组：将每个元素 $i$ 放在新数组的第 $C[i]$ 项，每放一个元素就将 $C[i]$ 减去1

```
#include <iostream>
#include <time.h>
#include <vector>
using namespace std;

void Counting_sort(int A[], size_t n, int k) {
        //申请额外空间
        int *B = new int[n];
        int *C = new int[k + 1];
        for (int i = 0; i <= k; ++i) {
                C[i] = 0; //将 C 指向的数组所有元素置0
        }
        //保存数组 A 中每个元素出现的个数
        for (int j = 0; j < n; ++j) {
                C[A[j]]++;
        }
        //将所有计数次数累加
        for (int i = 1; i <= k; ++i) {
                C[i] = C[i] + C[i - 1];
        }
        //将元素重新输入
        for (int i = n - 1; i >= 0; --i) {
                //次数大小最小为1、数组开始为0
                B[C[A[i]] - 1] = A[i];
                C[A[i]]--;
        }

        for (int j = 0; j < n; ++j) {
                A[j] = B[j];
        }
        //不要忘了释放分配的空间
        delete[] B;
        delete[] C;
}

int main(int argc, char **argv) {
        int a[10] = {2, 56, 4, 2, 9, 56, 3, 59, 9, 16};
        int max = a[0];
        for (int i = 1; i < 10; ++i) {
                if (a[i] > max) {
                        max = a[i];
                }
        }
        Counting_sort(a, 10, max);
        for (int i = 0; i < 10; ++i) {
                cout << a[i] << " ";
        }
        return 0;
}
```

- 最坏时间复杂度 $O(n+k)$
- 最优时间复杂度 $O(n+k)$
- 平均时间复杂度 $O(n+k)$
- 最坏空间复杂度 $O(n+k)$
- 稳定排序

## 6. 基数排序

基数排序（英语：Radix sort）是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。

它是这样实现的：将所有待比较数值（正整数）统一为同样的数字长度，数字较短的数前面补零。然后，从最低位开始，依次进行一次排序。这样从最低位排序一直到最高位排序完成以后，数列就变成一个有序序列。

基数排序的时间复杂度是 $O(k\cdot n)$，其中 $n$ 是排序元素个数，$k$ 是数字位数。

- 最坏时间复杂度 $O(k\cdot n)$
- 最坏时间复杂度 $O(n^2)$
- 最坏空间复杂度 $O(k+n)$
- 稳定排序

```
int maxbit(int data[], int n) //辅助函数，求数据的最大位数
{
        int maxData = data[0]; ///< 最大数
        /// 先求出最大数，再求其位数
        for (int i = 1; i < n; ++i) {
                if (maxData < data[i])
                        maxData = data[i];
        }
        int d = 1;
        int p = 10;
        while (maxData >= p) {
                maxData /= 10;
                ++d;
        }
        return d;
}
void radixsort(int data[], int n) //基数排序
{
        int d = maxbit(data, n);
        int *tmp = new int[n];
        int *count = new int[10]; //计数器
        int i, j, k;
        int radix = 1;
        for (i = 1; i <= d; i++) //进行 d 次排序
        {
                //每一次都是计数排序
                for (j = 0; j < 10; j++)
                        count[j] = 0; //每次分配前清空计数器
                for (j = 0; j < n; j++) {
                        k = (data[j] / radix) % 10; //统计每个桶中的记录数
                        count[k]++;
                }
                for (j = 1; j < 10; j++)
                        count[j] = count[j - 1] + count[j]; //将tmp中的位置依次分配给每个桶
                for (j = n - 1; j >= 0; j--) //将所有桶中记录依次收集到tmp中
                {
                        k = (data[j] / radix) % 10;
                        tmp[count[k] - 1] = data[j];
                        count[k]--;
                }
                for (j = 0; j < n; j++) //将临时数组的内容复制到data中
                        data[j] = tmp[j];
                radix = radix * 10;
        }
        delete[] tmp;
        delete[] count;
}
```

## 7. 桶排序

桶排序（Bucket sort）或所谓的箱排序，是一个排序算法，工作的原理是将数组分到有限数量的桶里。每个桶再个别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排序）。桶排序是鸽巢排序的一种归纳结果。当要被排序的数组内的数值是均匀分配的时候，桶排序使用线性时间 $\Theta (n)$。桶排序不是比较排序。

### 7.1 步骤

- 设置一个定量的数组当作空桶子
- 寻访序列，并且把项目一个一个放到对应的桶子去
- 对每个不是空的桶子进行排序
- 从不是空的桶子里把项目再放回原来的序列中

### 7.2 实现

转自：[https://blog.csdn.net/misayaaaaa/article/details/66969486](https://blog.csdn.net/misayaaaaa/article/details/66969486)

```
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

void Bucket_sort(double a[], size_t n) {
        double **p = new double *[10]; // p数组存放十个double指针，分为10个桶
        for (int i = 0; i < 10; ++i) {
                p[i] = new double
                       [100]; //每个指针都指向一块10个double的数组，每个桶都可以包含100个元素
        }

        int count[10] = {0}; //元素全为0的数组
        for (int i = 0; i < n; ++i) {
                double temp = a[i];
                int flag = (int)(temp * 10); //判断每个元素属于哪个桶
                p[flag][count[flag]] = temp; //将每个元素放入到对应的桶中，从0开始
                int j = count[flag]++; //将对应桶的计数加1

                //在本桶之中与之前的元素做比较，比较替换（插入排序）
                for (; j > 0 && temp < p[flag][j - 1]; --j) {
                        p[flag][j] = p[flag][j - 1];
                }
                p[flag][j] = temp;
        }

        //元素全部放完之后，需要进行重新链接的过程
        int k = 0;
        for (int i = 0; i < 10; ++i) {
                for (int j = 0; j < count[i]; ++j) //桶中元素的个数count[i]
                {
                        a[k++] = p[i][j];
                }
        }

        //申请内存的释放
        for (int i = 0; i < 10; i++) {
                delete p[i];
                p[i] = NULL;
        }
        delete[] p;
        p = NULL;
}

//随机初始化数组[0,1)
void Initial_array(double a[], size_t n) {
        for (size_t i = 0; i < n; ++i) {
                a[i] = rand() / (static_cast<double>(RAND_MAX) + 1);
        }
}

int main(int argc, char **argv) {
        double a[100];
        Initial_array(a, 100);

        Bucket_sort(a, 100);
        for (int i = 0; i < 100; ++i) {
                cout << a[i] << " ";
        }
        return 0;
}
```

- 时间复杂度为 $O(n)$
- 空间复杂度为 $O(n+M)$
- 稳定排序
