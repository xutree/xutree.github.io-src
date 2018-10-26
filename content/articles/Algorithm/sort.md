Title: 排序算法
Category: 读书笔记
Date: 2018-10-26 23:08:38
Modified: 2018-10-26 23:08:38
Tags: 算法

## 插入排序

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
