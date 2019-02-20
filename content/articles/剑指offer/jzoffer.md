Title: 剑指offer
Category: 读书笔记
Date: 2019-02-19 15:32:21
Modified: 2019-02-20 17:14:54
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

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

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
