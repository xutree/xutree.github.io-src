Title: 剑指 offer (1)
Category: 读书笔记
Date: 2018-10-07 15:32:21
Modified: 2018-11-26 19:56:59
Tags: 剑指offer, 面试, 算法

[TOC]

## 1. 二维数组中的查找

在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

```
class Solution {
public:
    bool Find(int target, vector<vector<int> > array) {
        // 注意 size 是成员函数，要加括号
        if (array.size() == 0) return false; // 为空，返回
        int row = array.size();
        int col = array[0].size();
        // 从右上角开始查找
        for (int i = 0, j = n - 1; i < m && j >= 0;) {
            if (array[i][j] == target) {
                return true;
            } else if (array[i][j] > target) {
                j--;
            } else {
                i++;
            }
        }
        return false;
    }
};
```

**思路**：如我们从右上角的数据开始出发，比他小的数必定在它的左侧，就往左找；比他大的数必定在它的下侧，就往下找。

## 2. 替换空格

请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

```
class Solution {
public:
	void replaceSpace(char *str,int length) {
        // 先统计总共有多少空格
        int count_space = 0;
        for (int i = 0; i < length; i++) {
            if (str[i] == ' ') count_space++;
        }
        int new_length = length + 2 * count_space;
        // 从后开始移位
        for (int i = length - 1, j = new_length - 1; i >= 0 && j >=0; ) {
            if (str[i] == ' ') {
                str[j--] = '0';
                str[j--] = '2';
                str[j--] = '%';
                i--;
            } else {
                str[j--] = str[i--];
            }
        }
        // 字符串结束标志
        str[new_length] = '\0';
	}
};
```

**思路**：从后往前移位可避免重复移位。

## 3. 从尾到头打印链表

输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

```
/**
*  struct ListNode {
*        int val;
*        struct ListNode *next;
*        ListNode(int x) :
*              val(x), next(NULL) {
*        }
*  };
*/
class Solution {
public:
    vector<int> printListFromTailToHead(ListNode* head) {
        ListNode* node = head;
        stack<int> st;
        int count = 0;
        while (node != NULL) {
            // 用 ->
            st.push(node->val);
            count++;
            node = node->next;
        }
        // 为了效率我们静态 vector 开辟空间
        vector<int> res(count);
        for(int i = 0; i < count && st.empty() != true; i++)
        {
            // 如果静态开辟 vector 不能使用push_back
            // 否则会在原来数据的基础上增加
            // res.push_back(st.top());
            // 注意栈的三个主要函数
            res[i] = st.top();
            st.pop();
        }
        return res;
    }
};
```

**思路**：首先我们想到的就是反转链表了,如果把链表反转了，然后再返回头，这样再次遍历的时候就相当于从尾到头打印了。但是在面试时候，如果我们打算修改输入的数据，最好先问问面试官是不是允许修改。通常打印只是一个只读操作，我们肯定不希望输入时候修改链表的内容。

**利用栈的后进先出特性**：单链表的遍历只能从前往后，但是需要从尾往头输出，这不是典型的“先进后出”么，那么我们可以用栈模拟输出。每经过一个结点的时候，把该结点放到一个栈中。当遍历完整个链表后，再从栈顶开始逐个输出结点的值，此时输出的结点的顺序已经反转过来了。注意包含 **stack** 头文件。

**递归实现**

```
/**
*  struct ListNode {
*        int val;
*        struct ListNode *next;
*        ListNode(int x) :
*              val(x), next(NULL) {
*        }
*  };
*/
class Solution {
public:
    vector<int> res; // 保存结果
    vector<int> printListFromTailToHead(ListNode* head) {
        if (head != NULL) {
            printListFromTailToHead(head->next);
            res.push_back(head->val);
        }
        return res;
    }
};
```

## 4. 重建二叉树

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

```
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
        // 遍历长度应该相同
        if (pre.size() != vin.size()) return NULL;
        // 非空
        if (pre.size() == 0) return NULL;
        int length = pre.size();
        // 前序遍历的第一个节点是根节点
        int value = pre[0];
        TreeNode* root = new TreeNode(value);
        // 在中序遍历中查找根的位置
        int rootIndex = 0;
        for (rootIndex = 0; rootIndex < length; rootIndex++) {
            if(vin[rootIndex] == value) break;
        }
        if (rootIndex >= length) return NULL;
        // 区分左子树和右子树
        // 中序遍历中，根左边的就是左子数，右边的就是右子树
        // 前序遍历中，根后面是先遍历左子树，然后是右子树
        // 首先确定左右子树的长度，从中序遍历 vin 中确定
        int leftLength = rootIndex;
        int rightLength = length - 1 - rootIndex;
        vector<int> preLeft(leftLength), vinLeft(leftLength);
        vector<int> preRight(rightLength), vinRight(rightLength);
        for (int i = 0; i < length; i++) {
            if (i < rootIndex) {
                preLeft[i] = pre[i + 1];
                vinLeft[i] = vin[i];
            } else if (i > rootIndex) {
                preRight[i - rootIndex - 1] = pre[i];
                vinRight[i - rootIndex - 1] = vin[i];
            }
        }
        root->left = reConstructBinaryTree(preLeft, vinLeft);
        root->right = reConstructBinaryTree(preRight, vinRight);

        return root;
    }
};
```

## 5. 用两个栈实现队列

用两个栈来实现一个队列，完成队列的 Push 和 Pop 操作。 队列中的元素为 int 类型。

```
class Solution
{
public:
    void push(int node) {
        stack1.push(node);
    }

    int pop() {
        if (stack2.empty()) {
            // 空队列，返回 -1
            if (stack1.empty()) return -1;
            while (!stack1.empty()) {
                int temp = stack1.top();
                stack2.push(temp);
                stack1.pop();
            }
        }
        int res = stack2.top();
        stack2.pop();
        return res;
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};
```

**思路**：始终维护 s1 作为输入栈，以 s2 作为输出栈：

- 入队时，将元素压入 s1
- 出队时，判断 s2 是否为空，如不为空，则直接弹出顶元素；如为空，则将 s1 的元素逐个“倒入” s2，把最后一个元素弹出并出队。这个思路，避免了反复“倒”栈，仅在需要时才“倒”一次。

## 6. 旋转数组的最小数字

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组 {3,4,5,1,2} 为 {1,2,3,4,5} 的一个旋转，该数组的最小值为 1。 NOTE：给出的所有元素都大于 0，若数组大小为 0，请返回 0。

```
class Solution {
public:
    int minNumberInRotateArray(vector<int> rotateArray) {
        if (rotateArray.size() == 0) return 0;
        //  如果把排序数组前面 0 个元素搬到后面，也就是说其实没有旋转，
        //  那么第 0 个元素就是最小的元素
        //  因此我们将 mid 初始化为 0
        int mid = 0;
        int low = 0, high = rotateArray.size() - 1;
        while (rotateArray[low] >= rotateArray[high]) {
            //  如果前一个元素与后一个元素差一位
            //  说明找到了最大最小的元素
            if(high - low == 1) {
                mid = high;
                break;
            }
            mid = (low + high) / 2;
            // rotateArray[low] rotateArray[mid] rotateArray[high]三者相等
            // 无法确定中间元素是属于前面还是后面的递增子数组
            // 只能顺序查找
            if (rotateArray[low] == rotateArray[mid] && rotateArray[mid] == rotateArray[high]) {
               return MinOrder(rotateArray, low, high);
            }
            //  如果该中间元素位于前面的递增子数组，那么它应该大于或者等于第一个指针指向的元素
            if (rotateArray[mid] >= rotateArray[low]) {
                low = mid;          //  此时最小的元素位于中间元素的后面
            }
            // 如果中间元素位于后面的递增子数组，那么它应该小于或者等于第二个指针指 向的元素
            else if (rotateArray[mid] <= rotateArray[high]) {
                high = mid;         //  此时最小的元素位于中间元素的前面
            }
        }
        return rotateArray[mid];
    }

private:
    // 顺序寻找最小值
    int MinOrder(vector<int> &num, int low, int high)
    {
        int result = num[low];
        for (int i = low + 1; i < high; i++) {
            if(num[i] < result) result = num[i];
        }
        return result;
    }
};
```

**思路**：和二分查找法一样，用两个指针分别指向数组的第一个元素和最后一个元素。我们注意到旋转之后的数组实际上可以划分为两个排序的子数组，而且前面的子数组的元素都大于或者等于后面子数组的元素。我们还可以注意到最小的元素刚好是这两个子数组的分界线。

我们试着用二元查找法的思路在寻找这个最小的元素。

首先我们用两个指针，分别指向数组的第一个元素和最后一个元素。按照题目旋转的规则，第一个元素应该是大于或者等于最后一个元素的（这其实不完全对，还有特例。后面再讨论特例）。

接着我们得到处在数组中间的元素。

如果该中间元素位于前面的递增子数组，那么它应该大于或者等于第一个指针指向的元素。
此时数组中最小的元素应该位于该中间 元素的后面。我们可以把第一指针指向该中间元素，这样可以缩小寻找的范围。

同样，如果中间元素位于后面的递增子数组，那么它应该小于或者等于第二个指针指 向的元素。此时该数组中最小的元素应该位于该中间元素的前面。我们可以把第二个指针指向该中间元素，这样同样可以缩小寻找的范围。我们接着再用更新之后的 两个指针，去得到和比较新的中间元素，循环下去。

按照上述的思路，我们的第一个指针总是指向前面递增数组的元素，而第二个指针总是指向后面递增数组的元素。最后第一个指针将指向前面子数组的最后一个元素， 而第二个指针会指向后面子数组的第一个元素。也就是它们最终会指向两个相邻的元素，而第二个指针指向的刚好是最小的元素。这就是循环结束的条件。

我们考虑下特殊情况，我们的循环判断是以 `rotateArray[low] >= rotateArray[high]` 为条件的，不满足这个的特殊情况有那些呢？

由于是把递增排序数组前面的若干个数据搬到后面去，因此第一个数字总是大于或者等于最后一个数字，但按照定义还有一个

特例：开始时就 `rotateArray[low] < rotateArray[high]`，那么循环不会执行.如果数组旋转后仍然有序，即 `rotateArray[low] < rotateArray[high]` 如果把排序数组前面 0 个元素搬到后面，也就是说其实没有旋转。那么第 0 个元素就是最小的元素，因此我们将 mid 初始化为 0。

如果 `rotateArray[low] = rotateArray[high]`

测试用例: [2, 3, 4, 2, 2, 2, 2]，此时 `rotateArray[low] rotateArray[mid] rotateArray[high]` 三者相等，无法确定中间元素是属于前面还是后面的递增子数组，只能顺序查找。

## 7. 斐波那契数列

大家都知道斐波那契数列，现在要求输入一个整数 $n$，请你输出斐波那契数列的第 $n$ 项（从 0 开始，第 0 项为 0），$n \leq 39$。

```
class Solution {
public:
    int Fibonacci(int n) {
        if (n < 2) {
            return n;
        }
        int f1 = 0, f2 = 1, res = 0;
        for (int i = 2; i <= n; i++) {
            res = f1 + f2;
            f1 = f2;
            f2 = res;
        }
        return res;
    }
};
```

**思路**：不可递归，会超时，需展开。

## 8. 跳台阶

一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级。求该青蛙跳上一个 $n$ 级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

```
class Solution {
public:
    int jumpFloor(int number) {
        if (number <= 2) return number;
        int f1 = 1, f2 = 2, res;
        for (int i = 3; i <= number; i++) {
            res = f1 + f2;
            f1 = f2;
            f2 = res;
        }
        return res;
    }
};
```

**思路**：$f(n)=f(n-1)+f(n-2)$

## 9. 变态跳台阶

一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级...它也可以跳上 $n$ 级。求该青蛙跳上一个 $n$ 级的台阶总共有多少种跳法。

```
class Solution {
public:
    int jumpFloorII(int number) {
        return pow(2, number - 1);
    }
};
```

**思路**：$f(n)=f(n-1)+f(n-2)+\cdots+f(1)=2f(n-1)$
$$f(n)=\begin{cases}
1, & n=0 \\
1, & n=1 \\
2f(n-1), & n\geq 2
\end{cases}$$

## 10. 矩形覆盖

我们可以用 $2\times1$ 的小矩形横着或者竖着去覆盖更大的矩形。请问用 $n$ 个 $2\times1$ 的小矩形无重叠地覆盖一个 $2\times n$ 的大矩形，总共有多少种方法？

```
class Solution {
public:
    int rectCover(int number) {
        if (number <= 2) return number;
        int f1 = 1, f2 = 2, res;
        for (int i = 3; i <= number; i++) {
            res = f1 + f2;
            f1 = f2;
            f2 = res;
        }
        return res;
    }
};
```

**思路**：$f(n)=f(n-1)+f(n-2)$

## 11. 二进制中 1 的个数

输入一个整数，输出该数二进制表示中 1 的个数。其中负数用补码表示。

```
class Solution {
public:
     int  NumberOf1(int n) {
         int count = 0;
         while (n) {
             count++;
             n = n & (n - 1);
         }
         return count;
     }
};
```

**逻辑右移与算术右移**：比如一个有符号位的 8 位二进制数 11001101，逻辑右移就不管符号位，如果移一位就变成 01100110。算术右移要管符号位，右移一位变成 10100110。

- 逻辑左移=算数左移，右边统一添 0
- 逻辑右移，左边统一添 0
- 算数右移，左边添加的数和符号有关

因此如果输入负数，那么我们的算法简单的判断是不是 0 来终结，岂不是要死循环。

**避免负数移位的死循环**：为了负数时候避免死循环，我们可以不右移数字 $n$，转而去移动测试位。

那么思考我们的循环结束条件，flag 一直左移（乘以 2），当超出表示标识范围的时候，我们就可以终止了，但是这样子的话，最高位的符号位没有测试，因此要单独测试，同时由于会溢出，我们的 flag 需要用 long 来标识。

**整数中有几个 1 就循环几次 --- lowbit 优化**：把一个整数 $n$ 减去 1，再和原来的整数做与运算，会把该整数最右边一个 1 变成 0，那么该整数有多少个 1，就会进行多少次与运算。

## 12. 数值的正数次方

给定一个 `double` 类型的浮点数 `base` 和 `int` 类型的整数 `exponent`。求 `base` 的 `exponent` 次方。

```
class Solution {
public:
    double Power(double base, int exponent) {
        // 注意不可声明为int
        double res = 1, curr = base;
        // 只有正数支持位运算
        int n;
        if (exponent > 0) {
            n = exponent;
        } else if (exponent < 0) {
            // 由于精度原因，double 类型的变量不能用等号判断两个数是否相等
            if (base > -0.000001 && base < 0.000001 ) {
                // 抛出异常
                throw new runtime_error("分母不能为0");
            }
            n = - exponent;
        } else {
            return 1;
        }
        while (n != 0) {
            // 不确定的地方加括号
            if ((n & 1) == 1)
                res *= curr;
            curr *= curr;
            n >>= 1;
        }
        return exponent >= 0 ? res : (1 / res);
    }
};
```

## 13. 调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

```
class Solution {
public:
    void reOrderArray(vector<int> &array) {
        if (array.size() <= 1) return;
        vector<int> temp;
        auto ib1 = array.begin();
        //  删除元素，尾后迭代器失效
        for (; ib1 != array.end(); ) {
            if (*ib1 % 2 == 0) {
                temp.push_back(*ib1);
                array.erase(ib1);
            } else {
                ib1++;
            }
        }
        /*
        Summary:
           1. For observing the elements, use the following syntax:
                 for (const auto& elem : container)    // capture by const reference
           2. If the objects are cheap to copy (like ints, doubles, etc.),
           it's possible to use a slightly simplified form:
                 for (auto elem : container)    // capture by value
           3. For modifying the elements in place, use:
                 for (auto& elem : container)    // capture by (non-const) reference
           4. If the container uses "proxy iterators" (like std::vector<bool>), use:
                 for (auto&& elem : container)    // capture by &&
           5. Of course, if there is a need to make a local copy of the element inside the loop body,
           capturing by value (for (auto elem : container)) is a good choice.
        */
        for (auto elem : temp) {
            array.push_back(elem);
        }
    }
};
```

## 14. 链表中倒数第 $k$ 个结点

输入一个链表，输出该链表中倒数第 $k$ 个结点。

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
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
        if (pListHead == NULL) return NULL;
        ListNode* left = pListHead, *right = left;
        unsigned int i = 0;
        while (i < k && right != NULL) {
            right = right->next;
            i++;
        }
        // 注意条件
        if (i < k && right == NULL) return NULL;
        // 注意条件
        while (right != NULL) {
            right = right->next;
            left = left->next;
        }
        return left;
    }
};
```

**思路**：双指针法

## 15. 反转链表

输入一个链表，反转链表后，输出新链表的表头。

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
    ListNode* ReverseList(ListNode* pHead) {
        if (pHead == NULL) return NULL;
        ListNode *pPrev = NULL, *pNext = NULL, *pNode = pHead;
        while (pNode) {
            pNext = pNode->next;
            pNode->next = pPrev;
            pPrev = pNode;
            pNode = pNext;
        }
        return pPrev;
    }
};
```

## 16. 合并两个排序的链表

输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

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
    ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
    {
        if (pHead1 == NULL ) {
            return pHead2;
        } else if (pHead2 == NULL) {
            return pHead1;
        }

        ListNode *phead1 = pHead1;
        ListNode *phead2 = pHead2;
        //  先生成头结点
        ListNode *head = NULL;
        if(phead1->val < phead2->val) {
            head = phead1;
            phead1 = phead1->next;
        } else {
            head = phead2;
            phead2 = phead2->next;
        }
        //  遍历两个链表，另用一个指针以保存头指针
        ListNode *curr = head;

        while (phead1 && phead2) {
            if (phead1->val > phead2->val) {
                curr->next = phead2;
                curr = curr->next;
                phead2 = phead2->next;
            } else {
                curr->next = phead1;
                curr = curr->next;
                phead1 = phead1->next;
            }
        }
        // 直接附加上去
        if (phead1 == NULL) {
            curr->next = phead2;
        } else {
            curr->next = phead1;
        }
        return head;
    }
};
```

## 17. 树的子结构

输入两棵二叉树 $A$，$B$，判断 $B$ 是不是 $A$ 的子结构。（ps：我们约定空树不是任意一个树的子结构）。

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
    bool HasSubtree(TreeNode* pRoot1, TreeNode* pRoot2)
    {
        bool res = false;
        // 判断非空
        if (pRoot1 != NULL && pRoot2 != NULL) {
            if (pRoot1->val == pRoot2->val) {
                res = DoesTree1HaveTree2(pRoot1, pRoot2);
            }
            if (!res) {
                res = HasSubtree(pRoot1->left, pRoot2);
            }
            if (!res) {
                res = HasSubtree(pRoot1->right, pRoot2);
            }
        }
        return res;
    }

    bool DoesTree1HaveTree2(TreeNode* pRoot1, TreeNode* pRoot2)
    {
        if (pRoot2 == NULL) return true;
        if (pRoot1 == NULL) return false;
        if (pRoot1->val != pRoot2->val) return false;
        return DoesTree1HaveTree2(pRoot1->left, pRoot2->left) &&
            DoesTree1HaveTree2(pRoot1->right, pRoot2->right);
    }
};
```

## 18. 二叉树的镜像

操作给定的二叉树，将其变换为源二叉树的镜像。

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
    void Mirror(TreeNode *pRoot) {
       if(pRoot == NULL) {
            return;
        }
        swap(pRoot->left, pRoot->right);
        Mirror(pRoot->left);
        Mirror(pRoot->right);
    }
};
```

## 19. 顺序打印矩阵

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10。

```
class Solution {
private:
    int row, col;
    vector<vector<bool>> flag;
    bool judge(int i, int j) {
        return 0 <= i && i < row && 0<= j && j <col && flag[i][j] == true;
    }
public:
    vector<int> printMatrix(vector<vector<int> > matrix) {
        vector<int> res;
        if (matrix.size() == 0) return res;
        row = matrix.size();
        col = matrix[0].size();
        flag = vector<vector<bool>> (row, vector<bool> (col, true));
        const int D[4][2] = {{0,1}, {1,0}, {0,-1}, {-1,0}};
        int i = 0, j = 0, d = 0, count = row * col;
        while (count--) {
            res.push_back(matrix[i][j]);
            flag[i][j] = false;
            if (judge(i + D[d][0],j + D[d][1]) == false) {
                (++d) %= 4;
            }
            i += D[d][0];
            j += D[d][1];
        }
        return res;
    }
};
```

## 20. 包含 `min` 函数的栈

定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的 `min` 函数（时间复杂度应为 $O(1)$）。

```
class Solution {
public:
    void push(int value) {
        m_data.push(value);
        if (m_min.empty()) {
            m_min.push(value);
        } else {
            int temp = value < m_min.top() ? value : m_min.top();
            m_min.push(temp);
        }
    }
    void pop() {
        m_data.pop();
        m_min.pop();
    }
    int top() {
        return m_data.top();
    }
    int min() {
        // 注意空
        if (m_min.empty()) return 0;
        return m_min.top();
    }
// 自己添加成员变量
protected:
    stack<int> m_data;
    stack<int> m_min;
};
```

**思路**：我们维持两个栈

- 数据栈 m_data，存储栈的数据用于常规的栈操作
- 最小栈 m_min，保存每次 `push` 和 `pop` 时候的最小值，

在 push-data 栈的时候，将当前最小数据压入，在 pop-data 栈的时候，将 min 栈栈顶的最小数据弹出，这样保证 min 栈中存储着当前现场的最小值，并随着数据栈的更新而更新。

## 21. 栈的压入、弹出序列

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）。

```
class Solution {
public:
    bool IsPopOrder(vector<int> pushV,vector<int> popV) {
        if (pushV.empty()) return false;
        vector<int> stack;
        for (int i = 0, j = 0; i < pushV.size(); ) {
            stack.push_back(pushV[i++]);
            // 注意为 while
            while (j < popV.size() && stack.back() == popV[j]) {
                stack.pop_back();
                j++;
            }
        }
        return stack.empty();
    }
};
```

## 22. 从上往下打印二叉树

从上往下打印出二叉树的每个节点，同层节点从左至右打印。

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
    vector<int> PrintFromTopToBottom(TreeNode* root) {
        vector<int> res;
        if (root == NULL) return res;

        vector<TreeNode*> vec;
        vec.push_back(root);

        int cur = 0;
        int end = 1;

        while (cur < vec.size()) {
            // 新的一行访问开始，重新定位 end 于当前行最后一个节点的下一个位置
            end = vec.size();

            while (cur < end) {
                res.push_back(vec[cur]->val);
                if (vec[cur]->left != NULL) ///  压入左节点
                {
                    vec.push_back(vec[cur]->left);
                }
                if (vec[cur]->right != NULL)    ///  压入右节点
                {
                    vec.push_back(vec[cur]->right);
                }
                cur++;
            }
        }
        return res;
    }
};
```

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
    vector<int> PrintFromTopToBottom(TreeNode* root) {
        vector<int> res;
        if (root == NULL) return res;
        queue<TreeNode*> node;
        node.push(root);
        node.push(NULL);
        TreeNode *curr = root;
        while (node.size() != 0) {
            // front 函数记住
            curr = node.front();
            node.pop();
            if (curr) {
                res.push_back(curr->val);
                if (curr->left) node.push(curr->left);
                if (curr->right) node.push(curr->right);
            } else if (node.size() != 0) {
                node.push(NULL);
            }
        }
        return res;
    }
};
```

## 23. 二叉搜索树的后序遍历序列

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

```
class Solution {
public:
    bool VerifySquenceOfBST(vector<int> sequence) {
        if (sequence.empty()) return false;
        return judge(sequence, 0, sequence.size() - 1);
    }
    bool judge(vector<int> &sequence, int left, int right) {
        if(left >= right) return true;
        /// 后一半的元素都比根元素大
        int mid = right - 1;
        // mid >= left
        while (mid >= left && sequence[mid] > sequence[right]) mid--;
        /// 那么前面的元素都应该比根小
        int i = left;
        while (i < mid && sequence[i] < sequence[right]) i++;
        if (i < mid) return false;
        return judge(sequence, left, mid) && judge(sequence, mid + 1, right - 1);
    }
};
```

**思路**：如果按照后序遍历，先左后右最后自己的顺序来遍历树，数组的最后一个元素肯定是自己（父节点），然后剩余的部分分成两个部分，第一部分都比自己小（左子树部分），第二部分都比自己大（右子树部分），因此套用这个关系就可以循环检验出是否是二叉搜索树的后序遍历了。

## 24. 二叉树中和为某一值的路径

输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的 list 中，数组长度大的数组靠前)。

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
    // 自己添加
private:
    vector<vector<int> >allRes;
    vector<int> tmp;
    void dfsFind(TreeNode * node , int expectNumber){
        tmp.push_back(node->val);
        if(expectNumber == node->val && node->left == NULL && node->right == NULL)
            allRes.push_back(tmp);
        else {
            if(node->left) dfsFind(node->left, expectNumber - node->val);
            if(node->right) dfsFind(node->right, expectNumber - node->val);
        }
        tmp.pop_back(); 
    }
public:
    vector<vector<int> > FindPath(TreeNode* root,int expectNumber) {
        if(root) dfsFind(root, expectNumber);
        return allRes;
    }
};
```

## 25. 复杂链表的复制

输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

```
/*
struct RandomListNode {
    int label;
    struct RandomListNode *next, *random;
    RandomListNode(int x) :
            label(x), next(NULL), random(NULL) {
    }
};
*/
class Solution {
public:
    RandomListNode* Clone(RandomListNode* pHead)
    {
        if (pHead == NULL) return NULL;
        RandomListNode *currNode = pHead;
        RandomListNode *newHead = NULL, *newNode = NULL;
        // 复制常规节点
        while (currNode != NULL) {
            if ((newNode = new RandomListNode(currNode->label)) == NULL) {
                // cstdio 用来将上一个函数发生错误的原因输出到标准设备(stderr)
                perror("new error: ");
                // cstdlib 退出当前运行的程序，并将参数返回给主调进程
                exit(-1);
            }

            newNode->next = currNode->next;
            currNode->next = newNode;
            currNode = newNode->next;
        }
        // 随机指针
        currNode = pHead;
        newNode = pHead->next;

        while (currNode != NULL) {
            RandomListNode *randNode = currNode->random;
            RandomListNode *newNode = currNode->next;
            if (randNode != NULL) {
                newNode->random = randNode->next;
            } else{
                newNode->random = NULL;
            }
            currNode = newNode->next;
        }
        // 断开
        currNode = pHead;
        newNode = newHead = pHead->next;
        while (currNode != NULL) {
            currNode->next = newNode->next;
            if (newNode->next != NULL) {
                newNode->next = newNode->next->next;
            } else {
                newNode->next = NULL;
            }
            currNode = currNode->next;
            newNode = newNode->next;
        }
        return newHead;
    }
};
```

**思路**：用 next 指针域关联新旧结点。将新节点直接插入到原结点的后面。

## 26. 二叉搜索树与双向链表

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

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
    TreeNode* Convert(TreeNode* pRootOfTree)
    {
        if (pRootOfTree == NULL) return NULL;
        TreeNode *pLastNode = NULL;
        ConvertRecursion(pRootOfTree, &pLastNode);

        // 当递归结束后,*pLastNode 指向了双向链表的尾结点
        TreeNode *node = pLastNode;
        while(node != NULL && node->left != NULL) {
           node = node->left;
        }
        return node;
    }
    void ConvertRecursion(TreeNode* root, TreeNode** pLastNode)
    {
        if (root == NULL) return;
        TreeNode *currNode = root;
        if (currNode->left != NULL) {
            ConvertRecursion(currNode->left, pLastNode);
        }
        currNode->left = *pLastNode;
        // 注意两层指针解引用
        if (*pLastNode != NULL) (*pLastNode)->right = currNode;
        *pLastNode = currNode;
        if (currNode->right != NULL) {
            ConvertRecursion(currNode->right, pLastNode);
        }
    }
};
```

## 27. 字符串的排列

输入一个字符串，按字典序打印出该字符串中字符的所有排列。例如输入字符串 abc，则打印出由字符 a、b、c 所能排列出来的所有字符串 abc、acb、bac、bca、cab 和 cba。

```
class Solution {
// 自己添加
protected:
    vector<string> m_res;
public:
    vector<string> Permutation(string str) {
        m_res.clear();

        if(str.empty() == true)
        {
            return m_res;
        }
        PermutationRecursion(str, 0);

        sort(m_res.begin(), m_res.end());
        return m_res;
    }
    void PermutationRecursion(string str, int begin)
    {
        if(str[begin] == '\0')
        {
            m_res.push_back(str);
        }
        else
        {
            for(int i = begin; str[i] != '\0'; i++)
            {
                if(!HasDuplicate(str, begin, i))
                {
                    swap(str[i], str[begin]);
                    PermutationRecursion(str, begin + 1);
                    swap(str[i], str[begin]);
                }
            }
        }
    }
private:
    //find duplicate of str[i] in str[k,i)
    bool HasDuplicate(string& str, int k, int i) const {
		for (int p = k; p < i; p++)
			if (str[p] == str[i]) return true;
		return false;
	}
};
```

**思路**：全排列中去掉重复的规则： 去重的全排列就是从第一个数字起，每个数分别与它后面非重复出现的数字交换。

## 28. 数组中出现次数超过一半的数字

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为 9 的数组 {1，2，3，2，2，2，5，4，2}。由于数字 2 在数组中出现了 5 次，超过数组长度的一半，因此输出 2。如果不存在则输出 0。

```
class Solution {
public:
    int MoreThanHalfNum_Solution(vector<int> numbers) {
        int len = numbers.size();
        if (len == 0) return 0;
        if (len == 1) return numbers[0];
        int k_val = FindKth(numbers, 0, len - 1, len / 2);
        int count = 0;
        for (auto &ele : numbers) {
            if (ele == k_val) count++;
        }
        return count > len / 2 ? k_val : 0;
    }
    int Partition(vector<int> &numbers, int low, int high) {
        if (low < high) {
            int i = low, j = high, x = numbers[i];
            while (i < j) {
                while (i < j && numbers[j] >= x) j--;
                numbers[i++] = numbers[j];
                while (i < j && numbers[i] < x) i++;
                numbers[j--] = numbers[i];
            }
            numbers[i] = x;
            return i;
        }
        return low;
    }
    int FindKth(vector<int> &numbers, int low, int high, int k) {
        if (low == high) return numbers[low];
        int index;
        index = Partition(numbers, low, high);
        // 递归 FindKth
        if (index < k)
            return FindKth(numbers, index + 1, high, k);
        else if (index > k)
            return FindKth(numbers, low, index - 1, k);
        else
            return numbers[index];
    }
};
```

## 29. 最小的 $K$ 个数

输入 $n$ 个整数，找出其中最小的 $K$ 个数。例如输入 4，5，6，2，7，3，8 这 8 个数字，则最小的 4 个数字是 1，2，3，4。

```
class Solution {
public:
    vector<int> GetLeastNumbers_Solution(vector<int> input, int k) {
        vector<int> res;
        if (input.size() == 0 || input.size() < k) return res;
        // 快排
        // quick_sort(input, 0, input.size() - 1);

        // 最大堆
        // make_maxheap(input, k);
        //for (int i = k; i < input.size(); i++) {
        //    if (input[0] > input[i]) {
        //        swap(input[0], input[i]);
        //        make_maxheap(input, k);
        //    }
        //}

        for (int i = 0; i < k; i++)
            res.push_back(input[i]);
        return res;
    }
    // 快排
    void quick_sort(vector<int> &input, int low, int high) {
        if (low < high) {
            int i = low, j = high, x = input[i];
            while (i < j) {
                while (i < j && input[j] >= x) j--;
                if (i < j) input[i++] = input[j];
                while (i < j && input[i] < x) i++;
                if (i < j) input[j--] = input[i];
            }
            input[i] = x;
            quick_sort(input, low, i - 1);
            quick_sort(input,i + 1, high);
        }
    }
    // 最大堆
    void make_maxheap(vector<int> &input, int k) {
        int dad = 0, son = 2 * dad + 1;
        while (son < k) {
            if (son + 1 < k && input[son + 1] > input[son])
                son++;
            if (input[son] <= input[dad])
                return;
            else {
                swap(input[son], input[dad]);
                dad = son;
                son = 2 * dad + 1;
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
};
```

## 30. 最大连续子序列的和

HZ 偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后，他又发话了：在古老的一维模式识别中，常常需要计算连续子向量的最大和，当向量全为正数的时候，问题很好解决。但是，如果向量中包含负数，是否应该包含某个负数，并期望旁边的正数会弥补它呢？例如：{6，-3，-2，7，-15，1，2，2}，连续子向量的最大和为 8（从第 0 个开始，到第 3 个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是 1)。

```
class Solution {
public:
    int FindGreatestSumOfSubArray(vector<int> array) {
        if (array.size() == 0) return 0;
        // #include <climits>
        int sum = 0, max_sum = INT_MIN;
        for (int i = 0; i < array.size(); i++) {
            if (sum <= 0) {
                sum = array[i];
            } else {
                sum += array[i];
            }
            if (sum > max_sum) {
                max_sum = sum;
            }
        }
        return max_sum;
    }
};
```
