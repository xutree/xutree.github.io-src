Title: 排序算法
Category: 读书笔记
Date: 2018-10-26 23:08:38
Modified: 2018-10-27 14:11:21
Tags: 算法

## 插入排序

插入排序思想：

假设对数组 A[p...r] 排序：

- 维持不变式：设当前排序的元素是 A[q]，则保持 A[p...q-1] 为排好的，A[q] 在 A[p...q-1] 中找到它的位置坐下
- 时间复杂度 $O(n^2)$
- 原地排序


```
#include <functional>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

template <typename Iterator,
          typename CompareType =
              std::less<typename std::iterator_traits<Iterator>::value_type>>
void insert_sort(Iterator begin, Iterator end,
                 CompareType compare = CompareType()) {
  auto size = std::distance(begin, end);
  if (size <= 1)
    return;
  Iterator current = begin;
  while (++current != end) {
    auto small_next = current;
    while (small_next != begin && compare(*current, *(small_next - 1))) {
      small_next--;
    }

    auto key = *current;
    auto iter = current;
    while (iter != small_next) {
      *iter = *(iter - 1);
      iter--;
    }
    *iter = key;
  }
}

template <typename Iterator> void print(Iterator begin, Iterator end) {
  while (begin != end) {
    std::cout << *begin << '\t';
    begin++;
  }
}

int main(int argc, char *argv[]) {
  std::istream_iterator<double> inc(std::cin), eof;
  std::vector<double> vec(inc, eof);
  insert_sort(vec.begin(), vec.end());
  print(vec.begin(), vec.end());
  return 0;
}
```

## 分治排序

归并思想，假设对数组 A[p...q...r] 归并：

- 拷贝：将数组 A[p...q] 拷贝到数组 L，将数组 A[q...r] 拷贝到数组 R
- 归并：从左到右依次取 L、R 中的较小的元素，存放到 A 中
- 时间复杂度 $O(n)$
- 归并时需要额外的空间 $O(n)$

```
template <typename Iterator,
          typename CompareType =
              std::less<typename std::iterator_traits<Iterator>::value_type>>
void merge(Iterator begin, Iterator middle, Iterator end,
           CompareType compare = CompareType()) {
  typedef typename std::iterator_traits<Iterator>::value_type T;
  if (std::distance(begin, middle) <= 0 || std::distance(middle, end) <= 0)
    return;
  std::vector<T> result(begin, end);
  auto current = result.begin();
  auto left_current = begin;
  auto right_current = middle;
  while (left_current != middle && right_current != end) {
    if (compare(*left_current, *right_current)) {
      *current++ = *left_current++;
    } else {
      *current++ = *right_current++;
    }
  }
  if (left_current == middle && right_current != end)
    std::copy(right_current, end, current);
  if (left_current != middle && right_current == end)
    std::copy(left_current, middle, current);

  std::copy(result.begin(), result.end(), begin);
}
```

归并排序思想，假设对数组 A[p...r] 排序：

- 分解：将数组 A[p...r] 平均划分为2子数组 A[p...q-1] 和 A[q...r]，一直划分直到每个子数组只有1个元素
- 归并： 对 A[p...q-1] 和 A[q...r] 这两个已排序好的数组进行合并
- 时间复杂度 $O(nlgn)$
- 非原地排序，归并时需要额外的空间 $O(n)$

```
template <typename Iterator,
          typename CompareType =
              std::less<typename std::iterator_traits<Iterator>::value_type>>
void merge_sort(Iterator begin, Iterator end,
                CompareType compare = CompareType()) {
  auto size = std::distance(begin, end);
  if (size > 1) {
    Iterator middle = begin + size / 2;
    merge_sort(begin, middle, compare);
    merge_sort(middle, end, compare);
    merge(begin, middle, end, compare);
  }
}
```
