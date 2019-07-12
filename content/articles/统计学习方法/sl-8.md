Title: 统计学习方法 第八章 提升方法
Category: 读书笔记
Date: 2019-03-23 21:42:33
Modified: 2019-03-25 10:34:40
Tags: 统计学习, 机器学习

[TOC]

提升（boosting）方法是一种常用的统计学习方法，应用广泛且有效。在分类问题中，它通过改变训练样本的权重，学习多个分类器，并将这些分类器进行线性组合，提高分类的性能。

## 8.1 提升方法 AdaBoost 算法

### 8.1.1 提升方法的基本思想

提升方法是一种可以用来减小监督式学习中偏差的机器学习元算法。面对的问题是迈可·肯斯（Michael Kearns）提出的：一组“弱学习者”的集合能否生成一个“强学习者”？弱学习者一般是指一个分类器，它的结果只比随机分类好一点点；强学习者指分类器的结果非常接近真值。

大多数的提升方法都是改变训练数据的概率分布（训练数据的权值分布），针对不同的训练数据分布调用弱学习算法学习一系列弱分类器。这样对于提升方法来说，有两个问题需要回答：

- 在每一轮如何改变训练数据的权值或概率分布
- 如何将弱分类器组合为一个强分类器

关于第一个问题，AdaBoost 的做法是，提高那些被前一轮分类器错误分类样本的权值，而降低那些被正确分类样本的权值。至于第二个问题，即弱分类器的组合，AdaBoost 采取加权多数表决的方法，具体的加大分类误差率小的弱分类器的权值，使其在表决中起较大的作用。

### 8.1.2 AdaBoost 算法

**
算法 8.1（AdaBoost）  
输入：训练数据集
$$T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$$
其中 $x_i\in{\cal X}\subseteq\mathbb{R}^n$，$y_i\inΥ=\{−1,+1\}$；弱学习算法  
输出：最终分类器 $G(x)$  
(1) 初始化训练数据的权值分布
$$D_1= (w_{11},\cdots,w_{1i},w_{1N}),\ w_{1i}=\frac{1}{N},\ i=1,2,\cdots,N$$
(2) 对 $m=1,2,\cdots,M$  
(2.a) 使用具有权值分布 $D_m$ 的训练数据集学习，得到基本分类器
$$G_m(x):{\cal X} \rightarrow \{-1,+1\}$$
(2.b) 计算 $G_m(x)$ 在训练数据集上的分类误差率
$$e_m = \sum_{i=1}^NP(G_m(x_i)\neq y_i)=\sum_{i=1}^Nw_{mi}\mathbb{I}(G_m(x_i)\neq y_i)$$
(2.c) 计算 $G_m(x)$ 的系数
$$\alpha_m=\frac{1}{2}\log\frac{1-e_m}{e_m}$$
这里的对数是自然对数  
(2.d) 更新训练数据集的权值分布
$$D_{m+1}=(w_{m+1,1},\cdots,w_{m+1,i},\cdots,w_{m+1,N}) \\
w_{m+1,i}=\frac{w_{mi}}{Z_m}\exp(-\alpha_my_iG_m(x_i)),\ i=1,2,\cdots,N$$
这里，$Z_m$ 是规范化因子
$$Z_m=\sum_{i=1}^{N}w_{mi}\exp\left(-\alpha_my_iG_m(x_i)\right)$$
它使 $D_{m+1}$ 成为一个概率分布  
(3) 构建基本分类器的线性组合
$$f(x)=\sum_{m=1}^{M}\alpha_mG_m(x)$$
得到最终分类器
$$G(x)=\text{sign}(f(x))=\text{sign}\left(\sum_{m=1}^M\alpha_mG_m(x)\right)$$
**

$\alpha_m$ 表示 $G_m(x)$ 在最终分类器中的重要性。当 $e_m\leq\frac{1}{2}$ 时，$\alpha_m\geq0$，并且 $\alpha_m$ 随着 $e_m$ 的减小而增大。

更新数据的权值方案也可以写为
$$w_{m+1,i}=\begin{cases}
\frac{w_{mi}}{Z_m}\text{e}^{-\alpha_m}, & G_m(x_i)=y_i \\
\frac{w_{mi}}{Z_m}\text{e}^{\alpha_m}, & G_m(x_i)\neq y_i
\end{cases}$$
显然，正确分类样本的权值在缩小，错误分类样本的权值在增大，误分类样本的权值被放大
$$\text{e}^{2\alpha_m}=\frac{1-e_m}{e_m}$$

## 8.2 AdaBoost  算法的训练误差分析

**
定理 8.1（AdaBoost 的训练误差界）AdaBoost 算法最终分类器的训练误差界为
$$\frac{1}{N}\sum_{i=1}^N\mathbb{I}\left(G(x_i)\neq y_i\right)\leq\frac{1}{N}\sum_{i=1}^N\exp(-y_if(x_i))=\prod_{m=1}^MZ_m$$
其中
$$G(x)=\text{sign}(f(x))=\text{sign}\left(\sum_{m=1}^M\alpha_mG_m(x)\right) \\
f(x)=\sum_{m=1}^{M}\alpha_mG_m(x) \\
Z_m=\sum_{i=1}^{N}w_{mi}\exp\left(-\alpha_my_iG_m(x_i)\right)$$
**

**证明**：当 $G(x_i)\neq y_i$ 时，$y_if(x_i)<0$，因而 $\exp(-y_if(x_i))\geq1$，前半部分成立。

对于后半部分，注意到
$$w_{mi}\exp(-\alpha_my_iG_m(x_i))=Z_mw_{m+1,i}$$
则
$$\begin{eqnarray}
\frac{1}{N} &\sum_i& \exp(-y_if(x_i)) \\
&=& \frac{1}{N}\sum_i\exp\left(-y_i\sum_{m=1}^{M}\alpha_mG_m(x_i)\right) \\
&=& \frac{1}{N}\sum_i\prod_{m=1}^M\exp\left(-y_i\alpha_mG_m(x_i)\right) \\
&=& \sum_iw_{1i}\prod_{m=1}^M\exp\left(-y_i\alpha_mG_m(x_i)\right) \\
&=& Z_1\sum_iw_{2i}\prod_{m=2}^M\exp\left(-y_i\alpha_mG_m(x_i)\right) \\
&=& Z_1Z_2\sum_iw_{3i}\prod_{m=3}^M\exp\left(-y_i\alpha_mG_m(x_i)\right) \\
&=& \cdots \\
&=& \prod_{m=1}^MZ_m
\end{eqnarray}$$

这一定理说明，可以在每一轮选取适当的 $G_m$ 使得 $Z_m$ 最小，从而使训练误差下降最快。

**
定理 8.2（二类分类问题 AdaBoost 的训练误差界）
$$\prod_{m=1}^MZ_m=\prod_{m=1}^M\left[2\sqrt{e_m(1-e_m)}\right]=\prod_{m=1}^M\sqrt{(1-4\gamma_m^2)}\leq\exp\left(-2\sum_{m=1}^M\gamma_m^2\right)$$
这里，$\gamma_m=\frac{1}{2}-e_m$
**

**证明**：对二类分类问题
$$\begin{eqnarray}
Z_m &=& \sum_{i=1}^Nw_{mi}\exp(-\alpha_my_iG_m(x_i)) \\
&=& \sum_{y_i=G_m(x_i)}w_{mi}\text{e}^{-\alpha_m}+\sum_{y_i\neq G_m(x_i)}w_{mi}\text{e}^{\alpha_m} \\
&=& (1-e_m)\text{e}^{-\alpha_m}+e_m\text{e}^{\alpha_m} \\
&=& 2\sqrt{e_m(1-e_m)}=\sqrt{1-4\gamma_m^2}
\end{eqnarray}$$
后半部分证明可以由 $\text{e}^x$ 和 $\sqrt{1-x}$ 在点 $x=0$ 的泰勒展开式推出不等式
$$\sqrt{1-4\gamma_m^2}\leq\exp(-2\gamma_m^2)$$
进而得到。

**
推论 8.1 如果存在 $\gamma>0$，对所有的 $m$ 有 $\gamma_m\geq\gamma$，则
$$\frac{1}{N}\sum_{i=1}^N\mathbb{I}\left(G(x_i)\neq y_i\right)\leq\exp(-2M\gamma^2)$$
**
这表明在此条件下，AdaBoost 训练误差关于训练次数 $M$ 以指数速率下降。

## 8.3 AdaBoost 算法的解释

AdaBoost 算法还有另外一个解释，即可以认为 AdaBoost 算法是模型为加法模型，损失函数为指数函数，学习算法为前向分步算法时的二类分类学习方法。

### 8.3.1 前向分步算法

考虑加法模型（additive model）
$$f(x)=\sum_{m=1}^M\beta_mb(x;\gamma_m)$$
其中，$b\left(x;\gamma_{m}\right)$ 为基函数，$\beta_{m}$ 为基函数系数，$\gamma_{m}$ 为基函数参数。

在给定训练数据及损失函数 $L\left(y,f\left(x\right)\right)$ 的条件下，学习加法模型 $f\left(x\right)$ 成为经验风险极小化问题
$$\begin{align*} \\ & \min_{\beta_{m},\gamma_{m}} \sum_{i=1}^{N} L \left( y_{i}, \sum_{m=1}^{M} \beta_{m} b\left(x_{i};\gamma_{m}\right) \right) \end{align*}$$

通常这是一个复杂的优化问题。前向分步算法（forward stagewise algorithm）求解这一问题的想法是：因为学习是加法模型，如果能够从前向后，每一步只学习一个基函数及其系数，逐步逼近优化目标函数式，那么就可以简化优化的复杂度。具体的，每步只需优化如下损失函数
$$\begin{align*} \\ & \min_{\beta,\gamma} \sum_{i=1}^{N} L \left( y_{i}, \beta b\left(x_{i};\gamma\right) \right) \end{align*}$$

**
算法 8.2（前向分步算法）  
输入：训练数据集
$$T=\left\{(x_{1},y_{1}),(x_{2},y_{2}),\cdots,(x_{N},y_{N})\right\}$$
损失函数 $L\left(y,f\left(x\right)\right)$；基函数集 $\left\{b\left(x;\gamma\right)\right\}$  
输出：加法模型 $f\left(x\right)$  
(1) 初始化 $f_{0}\left(x\right)=0$  
(2) 对 $m=1,2,\cdots,M$  
(2.a) 极小化损失函数
$$\begin{align*} \\ & \left(\beta_{m},\gamma_{m}\right) = \arg \min_{\beta,\gamma} \sum_{i=1}^{N} L \left( y_{i},f_{m-1} \left(x_{i}\right) + \beta b\left(x_{i};\gamma \right)\right) \end{align*}$$
得到参数 $\beta_{m}$，$\gamma_{m}$  
(2.b) 更新
$$\begin{align*} \\& f_{m} \left(x\right) = f_{m-1} \left(x\right) + \beta_{m} b\left(x;\gamma_{m}\right) \end{align*}$$
(3) 得到加法模型
$$\begin{align*} \\ & f \left( x \right) = f_{M} \left( x \right) = \sum_{m=1}^{M} \beta_{m} b \left( x; \gamma_{m} \right) \end{align*}$$
**

### 8.3.2 前向分布算法与 AdaBoost

**
定理 8.3 AdaBoost 算法是前向分布加法算法的特例。这时模型是由基本分类器组成的加法模型，损失函数是指数函数。
**

**证明**：加法模型等价于 AdaBoost 的最终分类器
$$f(x)=\sum_{m=1}^{M}\alpha_{m}G_{m}(x)$$
由基本分类器 $G_{m}(x)$ 及其系数 $\alpha_{m}$ 组成，$m=1,2,\cdots,M$。前向分布算法逐一学习基本函数，这一过程与 AdaBoost 算法逐一学习基本分类器的过程一致。下面证明前向分布算法的损失函数是指数损失函数（exponential loss function）
$$L(y,f(x))=exp[-yf(x)]$$
时，其学习的具体操作等价于 AdaBoost 算法学习的具体操作。

假设经过 $m-1$ 轮迭代前向分布算法已经得到 $f_{m-1}(x)$：
$$\begin{eqnarray}
f_{m-1}(x) &=& f_{m-2}(x)+\alpha_{m-1}G_{m-1}(x) \\
&=& \alpha_{1}G_{1}(x)+\cdots +\alpha_{m-1}G_{m-1}(x)
\end{eqnarray}$$
在第 $m$ 轮得到 $\alpha_{m}$，$G_{m}(x)$ 和 $f_{m}(x)$
$$f_{m}(x)=f_{m-1}(x)+\alpha_{m}G_{m}(x)$$
目标是使前向算法得到的 $\alpha_{m}$ 和 $G_{m}$ 使 $f_{m}(x)$ 在训练数据集 $T$ 上的指数损失最小，即：
$$\left(\alpha_{m},G_{m}(x)\right)=\arg\underset{\alpha,G}{\min}\sum_{i=1}^{N}\exp\left[-y_{i}(f_{m-1}(x_{i})+\alpha G(x_{i}))\right]$$
可以表示成：
$$(\alpha_{m},G_{m}(x))=\arg\underset{\alpha,G}{\min}\sum_{i=1}^{N}\overline{w}_{mi}\exp[-y_{i}\alpha G(x_{i})]$$
其中
$$\overline{w}_{mi}=\exp[-y_{i}f_{m-1}(x_{i})]$$ $\overline{w}_{mi}$ 不依赖于 $\alpha$，也不依赖于 $G$，但依赖于 $f_{m-1}(x)$，随着每一轮迭代而发生改变。

首先求 $G_{m}^{\star}(x)$，进一步展开：
$$\begin{eqnarray}
\sum_{i=1}^{N}\overline{w}_{mi}\exp[-y_{i}\alpha G(x_{i})] &=& \sum_{i=1}^{N}\overline{w}_{mi}\text{e}^{-\alpha}\mathbb{I}(y_{i}=G(x_{i}))+\sum_{i=1}^{N}\overline{w}_{mi}\text{e}^{\alpha}\mathbb{I}(y_{i}\neq G(x_{i})) \\
&=& \text{e}^{-\alpha}\sum_{i=1}^{N}\overline{w}_{mi}\mathbb{I}(y_{i}=G(x_{i}))+\text{e}^{\alpha}\sum_{i=1}^{N}\overline{w}_{mi}\mathbb{I}(y_{i}\neq G(x_{i})) \\
&+& \text{e}^{-\alpha}\sum_{i=1}^{N}\overline{w}_{mi}\mathbb{I}(y_{i}\neq G(x_{i}))-e^{-\alpha}\sum_{i=1}^{N}\overline{w}_{mi}\mathbb{I}(y_{i}\neq G(x_{i})) \\
&=& \text{e}^{-\alpha}\sum_{i=1}^{N}\overline{w}_{mi}+(\text{e}^{\alpha}-\text{e}^{-\alpha})\sum_{i=1}^{N}\overline{w}_{mi}\mathbb{I}(y_{i}\neq G(x_{i}))
\end{eqnarray}$$
所以最小化 $G(x)$ 由下式得到：
$$G_{m}^{\star}(x)=\arg\underset{G}{\min}\sum_{i=1}^{N}\overline{w}_{mi}\mathbb{I}(y_{i}\neq G(x_{i}))$$

之后我们求解 $\alpha_{m}^{\star}$：
$$\sum_{i=1}^{N}\overline{w}_{mi}\exp[-y_{i}\alpha G(x_{i})]=\sum_{y_{i}=G_{m}(x_{i})}\overline{w}_{mi}\text{e}^{-\alpha}+\sum_{y_{i}\neq G_{m}(x_{i})}\overline{w}_{mi}\text{e}^{\alpha}\\
=\text{e}^{-\alpha}\sum_{i=1}^{N}\overline{w}_{mi}+(\text{e}^{\alpha}-\text{e}^{-\alpha})\sum_{i=1}^{N}\overline{w}_{mi}\mathbb{I}(y_{i}\neq G(x_{i}))$$

对 $\alpha$ 求导：
$$\frac{\partial }{\partial \alpha}\left(\text{e}^{-\alpha}\sum_{i=1}^{N}\overline{w}_{mi}+(\text{e}^{\alpha}-\text{e}^{-\alpha})\sum_{i=1}^{N}\overline{w}_{mi}\mathbb{I}(y_{i}\neq G(x_{i}))\right)\\
=-\text{e}^{-\alpha}\sum_{i=1}^{N}\overline{w}_{mi}+(\text{e}^{\alpha}+\text{e}^{-\alpha})\sum_{i=1}^{N}\overline{w}_{mi}\mathbb{I}(y_{i}\neq G(x_{i}))=0$$
即得：
$$\frac{\text{e}^{\alpha}+\text{e}^{-\alpha}}{\text{e}^{-\alpha}}=\frac {\sum_{i=1}^{N}\overline{w}_{mi}}{\sum_{i=1}^{N}\overline{w}_{mi}\mathbb{I}(y_{i}\neq G(x_{i}))} \\
\alpha_{m}^{\star}=\frac{1}{2}\log\frac{1-e_{m}}{e_{m}}$$
其中 $e_{m}$ 是分类错误率：
$$e_{m}=\frac {\sum_{i=1}^{N}\overline{w}_{mi}\mathbb{I}(y_{i}\neq G(x_{i}))}{\sum_{i=1}^{N}\overline{w}_{mi}}=\sum_{i=1}^{N}w_{mi}\mathbb{I}(y_{i}\neq G(x_{i}))$$

这里的 $\alpha_{m}^{\star}$ 与 AdaBoost 算法的 $\alpha_{m}$ 完全一致。

再看一下每一轮的权值更新，由：
$$f_{m}(x)=f_{m-1}(x)+\alpha_{m}G_{m}(x)$$
以及
$$\overline{w}_{mi}=\exp[-y_{i}f_{m-1}(x_{i})]$$
可得：
$$\overline{w}_{m+1,i}=\overline{w}_{m,i}\exp[-y_{i}\alpha_{m}G_{m}(x)]$$
这与 AdaBoost 算法的样本权值的更新，只相差规范会因子，因此等价。

## 8.4 提升树

提升树是以分类或回归树为基本分类器的提升方法。提升树被认为是统计学习中性能最好的方法之一。

### 8.4.1 提升树模型

提升方法实际采用加法模型（即基函数的线性组合）与前向分布算法。以决策树为基函数的提升方法称为提升树（boosting tree）。对分类问题决策树是二叉分类树，对回归问题决策树是二叉回归树。只有一个条件的基本分类器可以看做是由一个根结点直接连接两个叶结点简单决策树，即所谓的决策树桩（decision stump）。提升树模型可以表示为决策树的加法模型：
$$f_{M}(x)=\sum_{m=1}^{M}T(x;\Theta_{m})$$
其中，$T(x;\Theta_{m})$ 表示决策树；$\Theta_{m}$ 为决策树的参数；$M$ 为树的个数。提升树中树之间没有权重，或者说它们的权重都是一样的，树之间是独立的，训练样本之间也没有权重的概念，这是提升树和随机森林、AdaBoost 之间的区别。

### 8.4.2 提升树算法

提升树算法采用前向分步算法。首先确定初始提升树 $f_{0}(x)=0$，第 $m$ 步的模型是：
$$f_{m}(x)=f_{m-1}(x)+T(x;\Theta_{m})$$

其中，$f_{m-1}(x)$ 为当前模型，通过经验风险最小化确定下一决策树的参数 $\Theta_{m}$：
$$\hat {\Theta}_{m}=\arg\underset{\Theta_{m}}{\min}\sum_{i=1}^{N}L(y_{i},f_{m-1}(x_{i})+T(x_{i};\Theta_{m})$$

不同问题的提升树有不同的学习算法，其主要区别在于使用的损失函数不同。包含用平凡误差损失函数的回归问题，用指数损失函数的分类问题，以及用一般损失函数的一般决策问题。对于二分类问题，提升树只需将 Adaboost 算法的基本分类器限制为二分类即可，可以说这时的提升树算法是 Adaboost 算法的特殊情况。下面主要讨论下回归问题。

已知训练数据集
$$\begin{align*} \\& T = \left\{ \left( x_{1}, y_{1} \right), \left( x_{2}, y_{2} \right), \cdots, \left( x_{N}, y_{N} \right) \right\} \end{align*} \\ $$
其中，$x_{i} \in \mathcal{X} \subseteq \mathbb{R}^{n}$，$y_{i} \in \mathcal{Y} \subseteq \mathbb{R}$，$i = 1, 2,\cdots, N$。

将输入空间 $\mathcal{X}$ 划分为 $J$ 个互不相交的区域 $R_{1},R_{2},\cdots,R_{J}$，且在每个区域上确定输出的常量 $c_{j}$，则回归树
$$\begin{align*} \\& T \left(x; \varTheta\right) = \sum_{j=1}^{J} c_{j} \mathbb{I} \left(x \in R_{j}\right) \end{align*} \\$$
其中，参数
$$\varTheta = \left\{ \left(R_{1}, c_{1}\right),\left(R_{2}, c_{2}\right),\cdots,\left(R_{J}, c_{J}\right) \right\}$$
表示树的区域划分和各区域上的常数。$J$ 是回归树的复杂度即叶结点个数。

回归提升树使用前向分布算法
$$\begin{align*} \\& f_{0}=0 \\ & f_{m}\left(x\right) = f_{m-1}\left(x\right) + T \left(x; \varTheta_{m}\right),\ m=1,2,\cdots,M\\ & f_{M} = \sum_{m=1}^{M} T \left(x; \varTheta_{m}\right) \end{align*} \\$$

在前向分布算法的第 $m$ 步给定当前模型 $f_{m-1}\left(x\right)$，模型参数
$$\begin{align*} \\& \hat \varTheta_{m} = \arg \min_{\varTheta_{m}} \sum_{i=1}^{N} L \left( y_{i}, f_{m-1}\left(x_{i}\right) + T \left( x_{i}; \varTheta_{m} \right) \right) \end{align*} \\ $$
得到第 $m$ 棵树的参数 $\hat \varTheta_{m}$

当采用平方误差损失函数
$$\begin{align*} \\& L \left( y, f_{m-1}\left(x\right)+T\left(x;\varTheta_{m}\right)\right) \\ & = \left[y-f_{m-1}\left(x\right)-T\left(x;\varTheta_{m}\right)\right]^{2} \\ & = \left[r-T\left(x;\varTheta_{m}\right)\right]^{2}\end{align*} \\ $$
其中，$r=y-f_{m-1}\left(x\right)$ 是当前模型拟合数据的残差。

**
算法 8.3（回归问题的提升树方法）  
输入：训练数据集
$$T = \left\{ \left( x_{1}, y_{1} \right), \left( x_{2}, y_{2} \right), \cdots, \left( x_{N}, y_{N} \right) \right\}$$
$x_{i} \in \mathcal{X} \subseteq R^{n}$，$y_{i} \in \mathcal{Y} \subseteq R$，$i = 1, 2, \cdots, N$  
输出：回归提升树 $f_{M}\left(x\right)$  
(1) 初始化 $f_{0}\left(x\right)=0$  
(2) 对 $m=1,2,\cdots,M$  
(2.) 计算残差
$$\begin{align*} \\ & r_{mi}=y_{i}-f_{m-1}\left(x_{i}\right),\quad i=1,2,\cdots,N \end{align*}$$
(2.b) 拟合残差 $r_{mi}$ 学习一个回归树，得到 $T\left(x;\varTheta_{m}\right)$  
(2.c) 更新 $$f_{m}=f_{m-1}\left(x\right)+T\left(x;\varTheta_{m}\right)$$
(3) 得到回归提升树
$$\begin{align*} \\ & f_{M} \left( x \right) = \sum_{m=1}^{M} T \left(x;\varTheta_{m}\right) \end{align*}$$
**

### 8.4.3 梯度提升

提升树用加法模型与前向分布算法实现学习的优化过程。当损失函数是平方损失函数时，每一步优化是很简单的，但是对一般损失函数而言，往往每一步优化并不那么容易。因此Freidman提过了梯度提升（gradient boosting）。这是利用最速下降法的近似方法，其关键是利用损失函数的负梯度在当前模型的值：
$$-\left [ \frac{\partial L(y_{i},f(x_{i}))}{\partial f(x_{i})} \right]_{f(x)=f_{m-1}(x)}$$
作为回归问题提升树算法中的残差近似值，拟合一个回归树。

**
算法 8.4（梯度提升算法）  
输入：训练数据集
$$T = \left\{ \left( x_{1}, y_{1} \right), \left( x_{2}, y_{2} \right), \cdots, \left( x_{N}, y_{N} \right) \right\}$$
$x_{i} \in \mathcal{X} \subseteq \mathbb{R}^{n}$，$y_{i} \in \mathcal{Y} \subseteq \mathbb{R}$，$i = 1, 2, \cdots, N$，最大迭代次数 $M$ ，损失函数 $L\left(y,f\left(x\right)\right)$  
输出：回归树 $\hat f\left(x\right)$  
(1) 初始化
$$\begin{align*} \\ & f_{0}\left(x\right) = \arg \min_{c} \sum_{i=1}^{N} L \left(y_{i},c\right) \end{align*}$$
(2) 对 $m=1,2,\cdots,M$  
(2.a) 对 $i=1,2,\cdots,N$ 计算
$$\begin{align*} \\ & r_{mi}=- \left[ \dfrac {\partial L \left(y_{i},f\left(x_{i}\right) \right)}{\partial f \left(x_{i} \right)}\right]_{f\left(x\right)=f_{m-1}\left(x\right)} \end{align*}$$
(2.b) 对 $r_{mi}$ 拟合回归树，得到第 $m$ 棵树的叶结点区域 $R_{mj}$，$j=1,2,\cdots,J$   
(2.c) 对 $j=1,2,\cdots,J$，计算  
$$\begin{align*} \\ & c_{mj}=\arg \min_{c} \sum_{x_{i} \in R_{mj}} L \left( y_{i},f_{m-1} \left(x_{i}\right)+c \right) \end{align*}$$
(2.d) 更新 $f_{m}\left(x\right)= f_{m-1}\left(x\right) + \sum_{j=1}^{J} c_{mj} \mathbb{I} \left(x \in R_{mj} \right)$  
(3) 得到回归树
$$\begin{align*} \\ & \hat f \left( x \right) = f_{M} \left( x \right) = \sum_{m=1}^{M} \sum_{j=1}^{J} c_{mj} \mathbb{I} \left( x \in R_{mj} \right) \end{align*}$$
**
