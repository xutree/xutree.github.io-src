Title: 剑指 offer (2)
Category: 读书笔记
Date: 2019-02-23 19:37:12
Modified: 2019-02-23 19:37:12
Tags: 剑指offer, 面试, 算法

[TOC]

## 1. 整数中 1 出现的次数

求出 1~13 的整数中 1 出现的次数，并算出 100~1300 的整数中 1 出现的次数？为此他特别数了一下 1~13 中包含 1 的数字有 1、10、11、12、13 因此共出现 6 次，但是对于后面问题他就没辙了。ACMer 希望你们帮帮他，并把问题更加普遍化，可以很快的求出任意非负整数区间中 1 出现的次数（从 1 到 $n$ 中 1 出现的次数）。

```
class Solution {
public:
    int NumberOf1Between1AndN_Solution(int n)
    {
        long count = 0, i = 1;
        long before = 0, current = 0, after = 0;
        while (n / i != 0) {
            before = n / (i * 10);
            current = (n / i) % 10;
            after = n - (n / i) * i;
            if (current > 1)
                count += before * i + i;
            else if (current == 0)
                count += before * i;
            else if (current == 1)
                count += before * i + after + 1;
            i *= 10;
        }
        return count;
    }
};
```
