Title: 剑指offer
Category: 读书笔记
Date: 2019-02-19 15:32:21
Modified: 2019-02-20 16:44:05
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
- 出队时，判断 s2 是否为空，如不为空，则直接弹出顶元素；如为空，则将 s1 的元素逐个“倒入” s2，把最后一个元素弹出并出队。这个思路，避免了反复“倒”栈，仅在需要时才“倒”一次。
