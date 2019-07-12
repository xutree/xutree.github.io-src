Title: 剑指 offer (2)
Category: 读书笔记
Date: 2018-10-08 19:37:12
Modified: 2018-11-26 22:42:52
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

## 2. 把数组排成最小的数

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组 {3，32，321}，则打印出这三个数字能排成的最小数字为 321323。

```
// #include <sstream>
template<class T>
string ToString(const T& t) {

    ostringstream oss;  //  创建一个流
    oss << t;            //  把值传递如流中
    return oss.str();  //  获取转换后的字符转并将其写入 result
}

class Solution {
public:
    ///  比较函数
    //  我们比较的不是两个字符串本身的大小，而是他们拼接后的两个数字的大小
    static bool Compare(const string &left, const string &right) {
        string leftright = left + right;
        string rightleft = right + left;
        return leftright < rightleft;
    }

    string PrintMinNumber(vector<int> numbers) {
        string res = "";
        string str;

        vector<string> strNum;

        ///  将整数转换成字符串
        for(unsigned int i = 0; i < numbers.size(); i++) {
            str = ToString(numbers[i]);
            strNum.push_back(str);
        }

        ///  对字符串按照拼接后的大小进行排序
        // #include <algorithm>
        sort(strNum.begin(), strNum.end(), Compare);

        ///  拼接结果
        for(unsigned int i = 0; i < strNum.size(); i++)
            res += strNum[i];
        return res;
    }
};
```

## 3. 丑数

把只包含质因子 2、3 和 5的数称作丑数（Ugly Number）。例如 6、8 都是丑数，但 14 不是，因为它包含质因子 7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第 $N$ 个丑数。

```
class Solution {
// 自己添加
protected:
    int ugly[10000];
    int min(int a, int b, int c) {
        int temp = (a < b ? a : b);
        return (temp < c ? temp : c);
    }
public:
    int GetUglyNumber_Solution(int index) {
        ugly[0] = 1;
        int index2 = 0;
        int index3 = 0;
        int index5 = 0;
        int n = 1;
        while (n < index)
        {
            //竞争产生下一个丑数
            int val = min(ugly[index2]*2, ugly[index3]*3, ugly[index5]*5);

            if (val == ugly[index2] * 2) //将产生这个丑数的index*向后挪一位；
                ++index2;
            if (val == ugly[index3] * 3)   //这里不能用elseif，因为可能有两个最小值，这时都要挪动；
                ++index3;
            if (val == ugly[index5] * 5)
                ++index5;
            ugly[n++] = val;
        }
        int result = ugly[index - 1];
        return result;
    }
};
```

## 4. 第一个只出现一次的字符

在一个字符串（0<= 字符串长度 <= 10000，全部由字母组成）中找到第一个只出现一次的字符，并返回它的位置，如果没有则返回 -1（需要区分大小写）。

```
class Solution {
public:
    int FirstNotRepeatingChar(string str) {
        int x[26] = {0}, y[26] = {0};

        for(unsigned int i = 0; i < str.size(); i++)
        {
            //  小写字母
            if('a' <= str[i] && str[i] <= 'z') {
                if(x[str[i] - 'a'] == 0) {
                    //  首次出现保存出现位置
                    x[str[i] - 'a'] = i + 1;
                } else {
                    //  出现多次, 就置标识-1
                    x[str[i] - 'a'] = -1;
                }
            } else if('A' <= str[i] && str[i] <= 'Z') {
                if(y[str[i] - 'A'] == 0) {
                     //  首次出现保存出现位置
                     y[str[i] - 'A']= i + 1;
                } else {
                    //  出现多次, 就置标识-1
                    y[str[i] - 'A'] = -1;
                }
            }
        }

        //  由于标识数组中
        //  只出现一次的字符会存储出现的位置
        //  出现多次的字符就存储标识-1
        //  因此查找数组中非-1的最小值即可
        int res = INT_MAX;
        for(int i = 0; i < 26; ++i)
        {
            if(x[i] != 0 && x[i] != -1)
            {
                res = min(res, x[i]);
            }
            if(y[i] != 0 && y[i] != -1)
            {
                res = min(res, y[i]);
            }
        }
        return res > str.size() ? -1 : res - 1;
    }
};
```

## 5. 数组中的逆序对


在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数 $P$。并将 $P$ 对 1000000007 取模的结果输出。 即输出 `P % 1000000007`。

```
class Solution {
public:
    int InversePairs(vector<int> data) {
        if(data.size() == 0) return 0;
        vector<int> temp(data.size());
        long long sum = CountMergePairs(data, 0, data.size() - 1, temp);
        return sum % 1000000007;
    }

    long long CountMergePairs(vector<int> &data, int start, int end, vector<int> &temp)
    {
	    long long PairsNum = 0;
	    if (start < end) {
		    int mid = (start + end) / 2;
		    PairsNum += CountMergePairs(data, start, mid, temp);	//统计左边子数组的逆序对
		    PairsNum += CountMergePairs(data, mid + 1, end, temp);	//统计右边子数组的逆序对
		    PairsNum += MergePairsBetweenArray(data, start, mid, end, temp); //统计左右子数组间的逆序对
	    }
	    return PairsNum;
    }

    long long MergePairsBetweenArray(vector<int> &data, int start, int mid, int end, vector<int> &temp)
    {
	    int i = start;
    	int j = mid + 1;
    	int k = 0;  //辅助数组的最后一位
	    long long count = 0;

    	//设置两个指针i,j分别从右往左依次比较，
	    //将较大的依次放入辅助数组的右边
    	while(i <= mid && j <= end) {
		    if(data[i] > data[j]) {
	    		count += mid - i + 1;
		    	temp[k++] = data[j++];
    		} else
		    	temp[k++] = data[i++];
	    }

	    //将其中一个数组中还剩下的元素拷贝到辅助数组中，
    	//两个循环只会执行其中的一个
	    while(i <= mid)
		    temp[k++] = data[i++];
	    while(j <= end)
		    temp[k++] = data[j++];

	    //从辅助数组中将元素拷贝到原数组中，使其有序排列
	    for(i = 0; i < k; i++)
		    data[start + i] = temp[i];

    	return count;
    }
};
```

## 6. 两个链表的第一个公共结点

输入两个链表，找出它们的第一个公共结点。

```
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* FindFirstCommonNode( ListNode* pHead1, ListNode* pHead2) {
        unordered_map<ListNode*, bool> umap;

        ListNode* left = pHead1;
        while (left != NULL)
        {
            umap.insert(make_pair(left, 1 ));
            left = left->next;
        }

        ListNode* right = pHead2;
        while (right)
        {
            if (umap.count(right)>0)
            {
                return right;
            }
            right = right->next;
        }
        return NULL;
    }
};
```

## 7. 数字在排序数组中出现的次数

统计一个数字在排序数组中出现的次数。

```
class Solution {
public:
    int GetNumberOfK(vector<int> data ,int k) {
        if (data.size() == 0) return 0;
        int index = BinarySearch(data, 0, data.size() - 1, k);
        int i, res = 0;
        if (index != -1) {
            for (i = index; i < data.size(); i++) {
                if (data[i] == k)
                    res++;
                else
                    break;
            }
            for (i = index - 1; i >= 0; i--) {
                if (data[i] == k)
                    res++;
                else
                    break;
            }
        }
        return res;
    }

    int BinarySearch(vector<int> &data, int low, int high, int k) {
        int mid;
        while (low <= high) {
            mid = (low + high) / 2;
            if (data[mid] > k)
                high = mid - 1;
            else if (data[mid] < k)
                low = mid + 1;
            else
                return mid;
        }
        return -1;
    }
};
```

## 8. 二叉树的深度

输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

```
/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
public:
    int TreeDepth(TreeNode* pRoot)
    {
        return TreeDepthRecursion(pRoot);
    }
    int TreeDepthRecursion(TreeNode *root)
    {
        if(root == NULL)
        {
            return 0;
        }
        else
        {
            int leftDepth = TreeDepthRecursion(root->left);
            int rightDepth = TreeDepthRecursion(root->right);

            return max(leftDepth, rightDepth) + 1;
        }
    }

};
```

## 9. 平衡二叉树

输入一棵二叉树，判断该二叉树是否是平衡二叉树。

```
class Solution {
public:
    bool IsBalanced_Solution(TreeNode* pRoot) {
        if(pRoot == NULL)
            return true;
        //int leftDepth = TreeDepth(pRoot->left);
        //int rightDepth = TreeDepth(pRoot->right);

        //if(fabs(leftDepth - rightDepth) <= 1)
        //    return IsBalanced_Solution(pRoot->left) && IsBalanced_Solution(pRoot->right);
        //else
        //    return false;
        int depth = 0;
        return IsVALWithDepth(pRoot, &depth);
    }

    int TreeDepth(TreeNode *root) {
    if(root == NULL)
        return 0;

    int leftDepth = TreeDepth(root->left);
    int rightDepth = TreeDepth(root->right);

    //  返回左右子树中深度最深的
    return max(leftDepth, rightDepth) + 1;
    }

    bool IsVALWithDepth(TreeNode *root, int *depth) {
        if(root == NULL) {
            *depth = 0;
            return true;
        }

        int leftDepth, rightDepth;

        bool left = IsVALWithDepth(root->left, &leftDepth);
        bool right = IsVALWithDepth(root->right, &rightDepth);

        if(left == true && right == true) {
            if(fabs(leftDepth - rightDepth) <= 1) {
                *depth = max(leftDepth, rightDepth) + 1;
                return true;
            }
        }
        return false;
    }
};
```

**思路**：1. 首先得到二叉树的深度，然后递归的判断每个节点的左右子树是否满足平衡条件；2. 这个递归法有很大缺陷，在求该结点的的左右子树深度时遍历一遍树，再次判断子树的平衡性时又遍历一遍树结构，造成遍历多次。我们在递归的过程中用 depth 来保存层数，然后递归的过程中同步遍历。

## 10. 只出现一次的数字

一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。

```
class Solution {
public:
    void FindNumsAppearOnce(vector<int> data,int* num1,int *num2) {
        // 注意星号！！！
        *num1 = *num2 = 0;
        if (data.size() < 2)
            return;
        int i, len = data.size();
        int XOR = data[0];
        for (i = 1; i < len; i++)
            XOR ^= data[i];
        int flag = XOR & (-XOR);
        for (i = 0; i < len; i++) {
            // 注意加括号，先算术运算，后移位运算，最后位运算。
            if ((data[i] & flag) == flag)
                *num1 ^= data[i];
            else
                *num2 ^= data[i];
        }
        return;
    }
};
```

## 11. 和为 $S$ 的连续正数序列

小明很喜欢数学,有一天他在做数学作业时,要求计算出 9~16 的和,他马上就写出了正确答案是 100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为 100（至少包括两个数）。没多久,他就得到另一组连续正数和为 100 的序列：18，19，20，21，22。现在把问题交给你,你能不能也很快的找出所有和为 $S$ 的连续正数序列? Good Luck!

```
class Solution {
public:
    vector<vector<int> > FindContinuousSequence(int sum) {
        int l, r, s;
        vector<vector<int>> res;

        for (l = 1, r = 2; l < (sum + 1) / 2 && r < sum; ) {
            s = (r - l + 1) / 2.0 * (l + r);
            if (s < sum)
                r++;
            else if (s > sum)
                l++;
            else {
                vector<int> temp;
                for (int i = l; i <= r; i++) {
                    temp.push_back(i);
                }
                res.push_back(temp);
                l++;
            }  
        }
        return res;
    }
};
```

**思路**：滑动窗口法。

## 12. 和为 $S$ 的两个数字

输入一个递增排序的数组和一个数字 $S$，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于 $S$，输出两个数的乘积最小的。

```
class Solution {
public:
    vector<int> FindNumbersWithSum(vector<int> array,int sum) {
        vector<int> res;
        if (array.size() < 2) return res;
        int l = 0, r = array.size() - 1;
        for (; l < (sum + 1) / 2 && l < r; ) {
            if (array[l] + array[r] == sum) {
                res.push_back(array[l]);
                res.push_back(array[r]);
                return res;
            } else if (array[l] + array[r] > sum) {
                r--;
            } else {
                l++;
            }
        }
        return res;
    }
};
```

**思路**：从两端开始查找，距离越远积越小。

## 13. 左旋转字符串

汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列 $S$，请你把其循环左移 $K$ 位后的序列输出。例如，字符序列 $S=abcXYZdef$，要求输出循环左移 3 位后的结果，即 $XYZdefabc$。是不是很简单？OK，搞定它。

```
class Solution {
public:
    string LeftRotateString(string str, int n) {
        if(str.size() == 0) return "";
        // 不修改原字符串
        string res(str);
        if(n > str.size())
             n %= str.size();
        for(int i = 0; i < str.size(); i++)
            res[i] = str[(i + n) % str.size()];
        return res;
    }
};
```

## 14. 翻转单词顺序列

牛客最近来了一个新员工 Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事 Cat 对 Fish 写的内容颇感兴趣，有一天他向 Fish 借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是 “I am a student.”。Cat 对一一的翻转这些单词顺序可不在行，你能帮助他么？

```
class Solution {
public:
    string ReverseSentence(string str) {
        if(str.size() == 0)
            return str;
        string res = "", tmp = "";
        for(unsigned int i = 0; i < str.size(); i++) {
            if(str[i] == ' ')       //  发现一个单词
            {
                res = " " + tmp + res;      //  顺序的拼接, 前面需要一个空格
                tmp = "";
            }
            else
            {
                tmp += str[i];
            }
        }
        if(tmp.size() != 0)     //  拼接最后一个单子, 前面无需空格
        {
            res = tmp + res;
        }
        return res;
    }
};
```

**思路**：从后向前重新组装字符串。

## 15. 扑克牌顺子

LL 今天心情特别好，因为他去买了一副扑克牌，发现里面居然有 2 个大王，2 个小王（一副牌原本是 54 张）...他随机从中抽出了 5 张牌，想测测自己的手气，看看能不能抽到顺子，如果抽到的话，他决定去买体育彩票,嘿嘿！！他想了想，决定大小王可以看成任何数字，并且 A 看作 1，J 为 11，Q 为 12 K 为 13。现在，要求你使用这幅牌模拟上面的过程，然后告诉我们 LL 的运气如何，如果牌能组成顺子就输出 true，否则就输出 false。为了方便起见，你可以认为大小王是0。

```
#define BIT_GET(number, pos) ((number) >> (pos) & 1)     /// 用宏得到某数的某位

#define BIT_SET(number, pos) ((number) |= 1 << (pos))    /// 把某位置1

#define BIT_CLR(number, pos) ((number) &= ~(1 << (pos))) /// 把某位清0

#define BIT_CPL(number, pos) ((number) ^= 1 << (pos))    /// 把number的POS位取反

class Solution {
public:
    bool IsContinuous( vector<int> numbers ) {
        if(numbers.size() != 5)
            return false;
        int min = INT_MAX;
        int max = INT_MIN;
        int flag = 0;
        for(int i = 0; i < numbers.size(); i++) {
            int num = numbers[i];
            if(num < 0 || num > 13) //  牌只能在0~13之间
                return false;
            else if(num == 0)       //  0用来答题任何牌，因此不能参与最大最小牌的比对
                continue;
            //  非0元素不能重复
            if(BIT_GET(flag, num) == 1)     //  如果flag的第num位为1, 说明num重复
                return false;
            else
                BIT_SET(flag, num);     //  将标识flag的第num位置为1
            //  寻找最大最小的牌
            if(num > max)
                max = num;
            if(num < min)
                min = num;
            //  如果最大值和最小值的差值大于4, 那么必应不能补齐
            if(max - min > 4)
                return false;
        }
        return true;
    }
};
```

**思路**：条件： 5张牌，顺子，除 0 之外不能重复。

结论： 非 0 元素的极差（最大值最小值的差）不超过 4， 非 0 元素不重复。

也可以排序后看 0 能不能填补空缺。


```
// 左移、右移 > 位运算 > 逻辑运算

#define BIT_GET(number, pos) ((number) >> (pos) & 1)     
/// 用宏得到某数的某位

#define BIT_SET(number, pos) ((number) |= 1 << (pos))    
/// 把某位置1

#define BIT_CLR(number, pos) ((number) &= ~(1 << (pos)))
/// 把某位清0

#define BIT_CPL(number, pos) ((number) ^= 1 << (pos))    
/// 把number的POS位取反
```

## 16. 孩子们的游戏（圆圈中最后剩下的数）

每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友，今年亦是如此。HF 作为牛客的资深元老，自然也准备了一些小游戏。其中，有个游戏是这样的：首先，让小朋友们围成一个大圈。然后，他随机指定一个数 $m$，让编号为 0 的小朋友开始报数。每次喊到 $m-1$ 的那个小朋友要出列唱首歌，然后可以在礼品箱中任意的挑选礼物，并且不再回到圈中，从他的下一个小朋友开始,继续 0...$m-1$ 报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!)。请你试着想下，哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从 0 到 $n-1$)。

```
class Solution {
public:
    int LastRemaining_Solution(int n, int m)
    {
        if(n < 1 || m < 1)
            return -1;
        int last = 0;
        for(int step = 2; step <= n; step++)
            last = (last + m) % step;
        return last;
    }
};
```

[https://blog.csdn.net/fuxuemingzhu/article/details/79702974](https://blog.csdn.net/fuxuemingzhu/article/details/79702974)

## 17. 求 $1+2+3+...+n$

要求不能使用乘除法、for、while、if、else、switch、case 等关键字及条件判断语句（A?B:C）。

```
class Solution {
public:
    int Sum_Solution(int n) {
        int ans = n;
        n && (ans += Sum_Solution(n - 1));
        return ans;
    }
};
```

## 18. 不用加减乘除做加法

写一个函数，求两个整数之和，要求在函数体内不得使用 +、-、\*、/ 四则运算符号。

```
class Solution {
public:
    int Add(int num1, int num2)
    {
        int temp;
        while(num2 != 0)
        {
            temp = num1 ^ num2;         //  计算不带进位的情况
            num2 = (num1 & num2) <<1;   //  计算带进位的情况
            num1 = temp;
            //  now num1 = 不带进位的情况, num2 = 带进位的情况
        }

        return num1;
    }
};
```

## 19. 将一个字符串转换成一个整数

将一个字符串转换成一个整数（实现 Integer.valueOf(string) 的功能，但是 string 不符合数字要求时返回 0），要求不能使用字符串转换整数的库函数。 数值为 0 或者字符串不是一个合法的数值则返回 0。

```
class Solution {
public:
    int StrToInt(string str) {
        string::iterator pstr = str.begin();
        //  排除前导的空格
        while (*pstr == ' ')  //  排除前导的空格
            pstr++;
        bool minus = false;
        //  判断符号位+ -
        if (*pstr == '+')
            pstr++;
        else if (*pstr == '-') {
            pstr++;
            minus = true;
        }
        long long int value = 0;
        for ( ; pstr != str.end(); pstr++) {
            if ('0' <= *pstr && *pstr <= '9') {
                value *= 10;
                value += *pstr - '0';
            }
            else
                break;
            //  解决OVER_FLOW的问题
            //  INT_MAX     2147483647
            //  INT_MIN     -2147483648  minus = true
            //  负数绝对值最大为INT_MAX + 1
            //  正数最大值为INT_MAX
            if((minus == true  && value > (unsigned long)(INT_MAX) + 1)
            || (minus == false && value > INT_MAX))
                break;
        }
        if(pstr != str.end())
            return 0;
        else {
            if (minus == true)
                value = -value;
            if (value >= INT_MAX)
                value = INT_MAX;
            else if (value <= INT_MIN)
                value = INT_MIN;
            return (int)value;
        }
    }
};
```

## 20. 数组中重复的数字

在一个长度为 $n$ 的数组里的所有数字都在 0 到 $n-1$ 的范围内。数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为 7 的数组 {2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字 2。

```
#define SET_SYMBOL_BIT(num)  ((num) |= (1 << 31))		/*  设置符号位为1 */
#define GET_ORIGIN_NUM(num)  ((num) & (~(1 << 31)))		/*	获取到源数据  */
#define GET_SYMBOL_BIT(num)  (((num) >> 31) & 1)		/*  获取符号位(标识)*/
class Solution {
public:
    // Parameters:
    //        numbers:     an array of integers
    //        length:      the length of array numbers
    //        duplication: (Output) the duplicated number in the array number
    // Return value:       true if the input is valid, and there are some duplications in the array number
    //                     otherwise false
    bool duplicate(int numbers[], int length, int* duplication) {
        *duplication = -1;
        if(CheckValidity(numbers, length) == false)
            return false;
        for(int i = 0; i < length; i++) {
            //  当前数字numbers[i]的标识即是numbers[numbers[i]]的符号位
            //  检查numbers[i]
            if(GET_SYMBOL_BIT(numbers[GET_ORIGIN_NUM(numbers[i])]) == 1) {
                *duplication = GET_ORIGIN_NUM(numbers[i]);
                return true;
            } else {
                SET_SYMBOL_BIT(numbers[GET_ORIGIN_NUM(numbers[i])]);
            }
        }
        return false;
    }

    bool CheckValidity(int *numbers, int length) {
        //  输入数据不合法
        if(numbers == NULL || length <= 0)
            return false;
        //  元素必须在[0, n-1]的范围
        for(int i = 0; i < length; i++)
            if(numbers[i] < 0 || numbers[i] > length - 1)
                return false;
        return true;
    }
};
```

**思路**：1. 排序后判断重复；2. 符号位标识法；3. 固定偏移法；4. 将元素放在自己该在的位置。

## 21. 构建乘积数组

给定一个数组 A[0,1,...,n-1]，请构建一个数组 B[0,1,...,n-1]，其中 B 中的元素 B[i]=A[0]\*A[1]\*...\*A[i-1]\*A[i+1]\*...\*A[n-1]。不能使用除法。

```
class Solution {
public:
    vector<int> multiply(const vector<int>& A) {
        vector<int> B(A.size());
        if (A.size() == 0) return B;
        for (int i = 0, temp = 1; i < A.size(); i++){
            B[i] = temp;
            temp *= A[i];
        }
        for (int i = A.size() - 1, temp = 1; i >= 0; i--) {
            B[i] *= temp;
            temp *= A[i];
        }
        return B;
    }
};
```

## 22. 正则表达式匹配

请实现一个函数用来匹配包括'.'和'\*'的正则表达式。模式中的字符'.'表示任意一个字符，而'\*'表示它前面的字符可以出现任意次（包含 0 次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串 "aaa" 与模式 "a.a" 和 "ab*ac*a" 匹配，但是与 "aa.a" 和 "ab*a" 均不匹配。

```
class Solution {
public:
    bool match(char* str, char* pattern)
    {
        /**
         * f[i][j]: if s[0..i-1] matches p[0..j-1]
         * if p[j - 1] != '*'
         *      f[i][j] = f[i - 1][j - 1] && s[i - 1] == p[j - 1]
         * if p[j - 1] == '*', denote p[j - 2] with x
         *      f[i][j] is true iff any of the following is true
         *      1) "x*" repeats 0 time and matches empty: f[i][j - 2]
         *      2) "x*" repeats >= 1 times and matches "x*x": s[i - 1] == x && f[i - 1][j]
         * '.' matches any single character
         */
        int m = strlen(str), n = strlen(pattern);
        vector<vector<bool>> f(m + 1, vector<bool>(n + 1, false));
        f[0][0] = true;
        for (int i = 1; i <= m; i++)
            f[i][0] = false;
        // p[0.., j - 3, j - 2, j - 1] matches empty iff p[j - 1] // is '*' and p[0..j - 3] matches empty
        for (int j = 1; j <= n; j++)
            f[0][j] = j > 1 && '*' == pattern[j - 1] && f[0][j - 2];

        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++)
                if (pattern[j - 1] != '*')
                    f[i][j] = f[i - 1][j - 1] && (str[i - 1] == pattern[j - 1] || '.' == pattern[j - 1]);
                else
        // p[0] cannot be '*' so no need to check "j > 1" here
                    f[i][j] = f[i][j - 2] || (str[i - 1] == pattern[j - 2] || '.' == pattern[j - 2]) && f[i - 1][j];

        return f[m][n];
    }
};
```

## 23. 表示数值的字符串

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串 "+100"，"5e2"，"-123"，"3.1416" 和 "-1E-16" 都表示数值。 但是 "12e"，"1a3.14"，"1.2.3"，"+-5" 和 "12e+4.3" 都不是。

```
class Solution {
public:
    bool isNumeric(char* string) {
        if (string == NULL) return false;
        if (*string == '+' || *string == '-')
             ++string;
        if (*string == '\0') return false;
        bool res = true;
        ScanDigits(&string);
        if (*string != '\0') {
            if (*string == '.') {
                ++string;
                ScanDigits(&string);
                if (*string == 'e' || *string =='E') {
                    res = IsExponential(&string);
                }
            } else if(*string == 'e' || *string == 'E') {
                res = IsExponential(&string);
            } else {
                res = false;
            }
        }
        return res && *string == '\0';
    }
    void ScanDigits(char** string) {
        while (**string != '\0' && (**string >= '0' && **string <= '9')) {
            ++(*string);
        }
    }
     bool IsExponential(char** string) {
         ++(*string);
         if (**string == '+' || **string == '-')
             ++(*string);
         if (**string == '\0')
             return false;
         ScanDigits(string);
         return (**string == '\0') ? true : false;
     }

};
```

**思路**：

1) 首先看第一个字符是不是正负号。
2) 如果是，在字符串上移动一个字符，继续扫描剩余的字符串中0到9的数位。
3) 如果是一个小数，则将遇到小数点。
4) 另外，如果是用科学计数法表示的数值，在整数或者小数的后面还有可能遇到“e”或者“E”。

## 24. 字符流中第一个只出现一次的字符

请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

```
class Solution
{
public:
    Solution(){
        str="";
        // #include <cstring>
        memset(count,0,sizeof(count));
    }
  //Insert one char from stringstream
    void Insert(char ch) {
        str += ch;
        count[(int)ch]++;
    }
  //return the first appearence once char in current stringstream
    char FirstAppearingOnce() {
        int len = str.size();
        for(int i = 0; i < len; i++)
            if (count[(int)str[i]] == 1)
                return str[i];
        return '#';
    }
private:
    string str;
    int count[256];
};
```

## 25. 链表中环入口

给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出 null。

```
/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
class Solution {
public:
    ListNode* EntryNodeOfLoop(ListNode* pHead)
    {
        if (pHead == NULL) return NULL;
        ListNode *p1 = pHead, *p2 = pHead;
        while (p1 != NULL && p2 != NULL) {
            p1 = p1->next;
            p2 = p2->next;
            if (p2 == NULL)
                return NULL;
            p2 = p2->next;
            if (p1 == p2)
                break;
        }
        p1 = pHead;
        while (p1 != p2) {
            p1 = p1->next;
            p2 = p2->next;
        }
        return p1;
    }
};
```

**思路**：双指针，第二个指针比第一个指针多走环节点整数倍。

## 26. 删除链表中重复的结点

在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表 1->2->3->3->4->4->5 处理后为 1->2->5

```
/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
class Solution {
public:
    ListNode* deleteDuplication(ListNode* pHead)
    {
        if (pHead == NULL) return NULL;
        ListNode *phony = new ListNode(-1);
        phony->next = pHead;
        ListNode *p = pHead, *last = phony;
        while (p != NULL && p->next != NULL) {
            if (p->val == p->next->val) {
                int val = p->val;
                while (p != NULL && p->val == val)
                    p = p->next;
                last->next = p;
            } else {
                last = p;
                p = p->next;
            }
        }
        return phony->next;
    }
};
```

**思路**：

1) 我们每次都判断当前结点的值与下一个节点的值是否重复
2) 如果重复就循环寻找下一个不重复的节点，将他们链接新新链表的尾部（其实就是删除重复的节点）

## 27. 二叉树的下一个结点

给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

```
/*
struct TreeLinkNode {
    int val;
    struct TreeLinkNode *left;
    struct TreeLinkNode *right;
    struct TreeLinkNode *next;
    TreeLinkNode(int x) :val(x), left(NULL), right(NULL), next(NULL) {

    }
};
*/
class Solution {
public:
    TreeLinkNode* GetNext(TreeLinkNode* pNode)
    {
        if (pNode == NULL) return NULL;
        // 不要在局部函数内定义需要返回的变量，局部函数执行完就销毁了。
        TreeLinkNode *Next = NULL;
        if (pNode->right != NULL) {
            TreeLinkNode *temp = pNode->right;
            while (temp->left != NULL) {
                temp = temp->left;
            }
            Next = temp;
        } else {
            TreeLinkNode *parent = pNode->next;
            TreeLinkNode *current = pNode;
            while (parent != NULL && current == parent->right) {
                current = parent;
                parent = parent->next;
            }
            Next = parent;
        }
        return Next;
    }
};
```

**思路**：

1) 如果当前结点有右子树, 那么其中序遍历的下一个结点就是其右子树的最左结点
2) 如果当前结点没有右子树, 而它是其父结点的左子结点那么其中序遍历的下一个结点就是他的父亲结点
3) 如果当前结点没有右子树，而它还是其父结点的右子结点，这种情况下其下一个结点应该是当前结点所在的左子树的根, 因此我们可以顺着其父节点一直向上遍历, 直到找到一个是它父结点的左子结点的结点

## 28. 对称的二叉树

请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

```
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    bool isSymmetrical(TreeNode* pRoot)
    {
        if(pRoot == NULL)
            return true;   
        return isSymmetricalRecursion(pRoot->left, pRoot->right);
    }
    bool isSymmetricalRecursion(TreeNode *pLeft, TreeNode *pRight) {
        if(pLeft == NULL && pRight == NULL)
            return true;
        if(pLeft == NULL || pRight == NULL)
            return false;
        if(pLeft->val != pRight->val)
            return false;
        //  左子树的左与右子树的右对称
        //  左子树的右与右子树的左对称
        return isSymmetricalRecursion(pLeft->left, pRight->right)
            && isSymmetricalRecursion(pLeft->right, pRight->left);
    }
};
```

```
class Solution
{
public:
    bool isSymmetrical(TreeNode *root)
    {
        if(root == NULL)
        {
            return true;
        }

        if(root->left == NULL
        && root->right == NULL)
        {
            return true;
        }
        if((root->left == NULL && root->right != NULL)
        || (root->left != NULL && root->right == NULL))
        {
            return false;
        }

        deque< TreeNode * > dq;
        dq.push_front(root->left);
        dq.push_back(root->right);

        while(dq.empty( ) != true)
        {
            TreeNode* lroot = dq.front();
            TreeNode* rroot = dq.back();
            dq.pop_front();
            dq.pop_back();

            if(lroot -> val != rroot -> val)
            {
                return false;
            }

            if((lroot->right == NULL && rroot->left != NULL)
            || (lroot->right != NULL && rroot->left == NULL))
            {
                return false;
            }

            if(lroot->right != NULL)
            {
                dq.push_front(lroot->right);
                dq.push_back(rroot->left);
            }

            if((lroot->left == NULL && rroot->right != NULL)
            || (lroot->left != NULL && rroot->right == NULL))
            {
                return false;
            }

            if(lroot->left != NULL)
            {
                dq.push_front(lroot->left);
                dq.push_back(rroot->right);
            }
        }
        return true;
    }
};
```

## 29. 按照之字形打印二叉树

请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

```
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    vector<vector<int> > Print(TreeNode* pRoot) {
        vector<vector<int>> ret;
        if(pRoot == NULL) return ret;
        vector<int> curr;
        deque<TreeNode*> deq;
        deq.push_back(NULL);//层分隔符
        deq.push_back(pRoot);
        bool leftToRight = true;
        while (deq.size() != 1){
            TreeNode* node = deq.front();
            deq.pop_front();
            if(node == NULL)    //  到达每层分隔符
            {
                if (leftToRight == true)    //  从前完后遍历
                {
                    deque<TreeNode*>::iterator iter;
                    for(iter = deq.begin(); iter != deq.end(); iter++)
                        curr.push_back((*iter)->val);
                } else                        //  从后往前遍历
                {
                    deque<TreeNode*>::reverse_iterator riter;
                    for(riter = deq.rbegin(); riter < deq.rend(); riter++)
                        curr.push_back((*riter)->val);
                }
                leftToRight = !leftToRight;
                ret.push_back(curr);
                curr.clear();
                deq.push_back(NULL);//添加层分隔符
                continue;//一定要continue
            }
            if (node->left != NULL)
                deq.push_back(node->left);
            if (node->right != NULL)
                deq.push_back(node->right);
        }
        return ret;
    }
};
```

## 30. 把二叉树打印出多行

从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

```
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
        vector<vector<int> > Print(TreeNode* pRoot) {
            vector<vector<int>> res;
            if (pRoot == NULL) return res;
            vector<int> temp;
            TreeNode* curr;
            queue<TreeNode*> node;
            node.push(pRoot);
            node.push(NULL);
            while (node.empty() != true) {
                curr = node.front();
                node.pop();
                if (curr != NULL) {
                    temp.push_back(curr->val);
                    if (curr->left != NULL) node.push(curr->left);
                    if (curr->right != NULL) node.push(curr->right);
                } else if (node.empty() != true) {
                    res.push_back(temp);
                    temp.clear();
                    node.push(NULL);
                }
            }
            if (temp.size() != 0) res.push_back(temp);
            return res;
        }

};
```

## 31. 序列化二叉树

请实现两个函数，分别用来序列化和反序列化二叉树。


```
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    /*  序列化二叉树  */
    char* Serialize(TreeNode *root){
        if(root == NULL){
            char *serial = new char[3];
            strcpy(serial, "#,");
            return serial;
        }
        string str;
        Serialize(root, str);
        const char  *c_str = str.c_str();
        char *serial = new char[str.length() + 1];
        strcpy(serial, c_str);
        return serial;
    }

    TreeNode* Deserialize(char *str) {
        if(str == NULL|| *str == '\0')
            return NULL;
        int index = 0;
        return Deserialize(str, index);
    }
private:
    void Serialize(TreeNode *root, string &str) {
        if(root == NULL) {
            str += "#,";
            return;
        }
        /*  先序遍历的方式, 序列化二叉树  */
        str += (toString(root->val) + ",");
        Serialize(root->left, str);
        Serialize(root->right, str);
    }
    /*  反序列化二叉树
     *  将一个序列化的字符串转换成二叉树  */
    TreeNode* Deserialize(char *str, int &index) {
        if(str[index] == '#') {
            index += 2;
            return NULL;
        }
        /*  获取到节点的数字权值  */
        int num = 0;
        while(str[index] != ',' && str[index] != '\0'){
            num = num * 10 + (str[index] - '0');
            index++;
        }
        index++;
        TreeNode *root = new TreeNode(num);
        root->left = Deserialize(str, index);
        root->right = Deserialize(str, index);
        return root;
    }

    string toString(int num) {
        stringstream ss;
        ss << num;
        return ss.str();
    }
};
```

## 32. 二叉搜索树的第 $k$ 个结点

给定一棵二叉搜索树，请找出其中的第 $k$ 小的结点。例如，（5，3，7，2，4，6，8） 中，按结点数值大小顺序第三小结点的值为 4。

```
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
private:
    unsigned int count = 0;
public:
    TreeNode* KthNode(TreeNode* pRoot, int k)
    {
        if(pRoot == NULL)
            return NULL;
        TreeNode *ret = NULL;
        if((ret = KthNode(pRoot->left, k)) != NULL)
            return ret;
        ++count;
        if(count == k)
            return pRoot;
        if((ret = KthNode(pRoot->right, k)) != NULL)
            return ret;
        return NULL;
    }  
};
```

## 33. 数据流中的中位数

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用 Insert() 方法读取数据流，使用 GetMedian() 方法获取当前读取数据的中位数。

```
class Solution {
private:
    vector<int> m_min; // 后半部分数据
    vector<int> m_max; // 前半部分数据
protected:
    void MakeHeapify(vector<int> &a, int start, int end, int flag) {
        int dad = start;
        int son = 2 * dad + 1;
        // 最大堆
        if (flag == 1) {
            while (son <= end) {
                if (son + 1 <= end && a[son + 1] > a[son])
                    son++;
                if (a[dad] >= a[son]) return;
                else {
                    swap(a[dad], a[son]);
                    dad = son;
                    son = dad * 2 + 1;
                }
            }
        } // 最小堆
        if (flag == 0) {
            while (son <= end) {
                if (son + 1 <= end && a[son + 1] < a[son])
                    son++;
                if (a[dad] < a[son]) return;
                else {
                    swap(a[dad], a[son]);
                    dad = son;
                    son = dad * 2 + 1;
                }
            }
        }
    }
    void swap(int &a, int &b) {
        if (a != b) {
            a ^= b;
            b ^= a;
            a ^= b;
        }
    }
public:
    void Insert(int num) {
        int temp = num;
        // 偶数时，假设最大堆比最小堆少1 关系 > 逐位运算
        if (((m_min.size() + m_max.size()) & 1) == 0) {
            if (m_max.size() > 0 && num < m_max[0]) {
                swap(m_max[0], temp);
                MakeHeapify(m_max, 0, m_max.size() - 1, 1);
            }
            m_min.push_back(temp);
            MakeHeapify(m_min, 0, m_min.size() - 1, 0);
        } else {
            if (m_min.size() > 0 && num > m_min[0]) {
                swap(m_min[0], temp);
                MakeHeapify(m_min, 0, m_min.size() - 1, 0);
            }
            m_max.push_back(temp);
            MakeHeapify(m_max, 0, m_max.size() - 1, 1);
        }
    }

    double GetMedian() {
        int size = m_min.size() + m_max.size();
        if (size == 0) return -1;
        double median = 0;
        if((size & 1) != 0)
            median = (double) m_min[0];
        else
            median = (double) (m_max[0] + m_min[0]) / 2;
        return median;
    }
};
```

## 34. 滑动窗口的最大值

给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。

```
class Solution {
public:
    vector<int> maxInWindows(const vector<int>& num, unsigned int size)
    {
        vector<int> res;
        deque<int> index;
        for(unsigned int i = 0; i < num.size(); i++) {
            /*  从后面依次弹出队列中比当前num值小的元素，
             *  同时也能保证队列首元素为当前窗口最大值下标  */
            while(index.size() != 0 && num[index.back()] <= num[i])
                index.pop_back();
            /*  当前窗口移出队首元素所在的位置
                即队首元素坐标对应的num不在窗口中，需要弹出  */
            while(index.size() && i - index.front() + 1 > size)
                index.pop_front( );
            /*  把每次滑动的num下标加入队列  */
            index.push_back(i);
            /*  当滑动窗口首地址i大于等于size时才开始写入窗口最大值  */
            if(size != 0 && i + 1 >= size)
                res.push_back(num[index.front()]);
        }
        return res;
    }
};
```

## 35. 矩阵中的路径

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

```
class Solution {
public:
    bool hasPath(char* matrix, int rows, int cols, char* str) {
        if (matrix == NULL || rows < 1 || cols < 1 || str == NULL)
			return false;
		//定义一个辅助矩阵，用来标记路径是否已经进入了每个格子
        bool* visited = new bool[rows * cols];
		memset(visited, 0, rows * cols);
		int pathLength = 0;
        //该循环是为了实现从任何一个位置出发，寻找路径
		for (int row = 0; row < rows; ++row) {
			for (int col = 0; col < cols; ++col) {
				if (hasPathCore(matrix, rows, cols, row,
                                col, str, pathLength, visited))
					return true;
			}
		}
		delete[] visited;
		return false;
    }
    /*此函数用来判断在当前路径满足条件下，相邻格子中是否存在一个格子满足条件*/
	bool hasPathCore(char* matrix, int rows, int cols, int row,
                     int col, char* str, int& pathLength, bool* visited) {
		if (str[pathLength] == '\0')
			return true;
		bool hasPath = false;
		if (row >= 0 && row < rows && col >= 0 && col < cols
            && matrix[row * cols + col] == str[pathLength]
            && !visited[row * cols + col]) {
			++pathLength;
			visited[row * cols + col] = true;
			/*如果矩阵格子(row,col)与路径字符串中下标为pathLength的字符一样时，
			从它的4个相邻格子中寻找与路径字符串下标为pathLength+1的字符相等的格子*/
			hasPath = hasPathCore(matrix, rows, cols, row, col - 1, str, pathLength, visited) ||
				hasPathCore(matrix, rows, cols, row - 1, col, str, pathLength, visited) ||
				hasPathCore(matrix, rows, cols, row, col + 1, str, pathLength, visited) ||
				hasPathCore(matrix, rows, cols, row + 1, col, str, pathLength, visited);
			if (!hasPath) {
                //如果没找到，则说明当前第pathLength个字符定位不正确，返回上一个位置重新定位
				--pathLength;
				visited[row * cols + col] = false;
			}
		}
		return hasPath;
	}
};
```

## 37. 机器人的运动范围

地上有一个 $m$ 行和 $n$ 列的方格。一个机器人从坐标 (0,0) 的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于 $k$ 的格子。 例如，当 $k$ 为 18 时，机器人能够进入方格（35,37），因为 3+5+3+7 = 18。但是，它不能进入方格（35,38），因为 3+5+3+8 = 19。请问该机器人能够达到多少个格子？

```
class Solution {
public:
    int movingCount(int threshold, int rows, int cols) {
        bool* visited = new bool[rows * cols];
		memset(visited, 0, rows * cols);
		int count = movingCountCore(threshold, rows, cols, 0, 0, visited);
		delete[] visited;
		return count;
    }
    int movingCountCore(int threshold, int rows, int cols,
                        int row, int col, bool* visited) {
		int count = 0;
		if (check(threshold, rows, cols, row, col, visited)) {
			visited[row * cols + col] = true;
			count = 1 +
                movingCountCore(threshold, rows, cols, row, col - 1, visited) +
				movingCountCore(threshold, rows, cols, row - 1, col, visited) +
				movingCountCore(threshold, rows, cols, row, col + 1, visited) +
				movingCountCore(threshold, rows, cols, row + 1, col, visited);
		}
		return count;
	}
	/*该函数检查坐标为(row,col)的方格能够进入*/
	bool check(int threshold, int rows, int cols, int row, int col, bool*visited) {
		if (row >= 0 && row < rows && col >= 0 && col < cols
			&& getDigitSum(row) + getDigitSum(col) <= threshold
			&& !visited[row*cols + col])
			return true;
		return false;
	}
	/*计算一个数的所有位数之和*/
	int getDigitSum(int number) {
		int sum = 0;
		while (number > 0)
		{
			sum += number % 10;
			number = number / 10;
		}
		return sum;
	}
};
```
