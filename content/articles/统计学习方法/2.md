Title: 统计学习方法 第二章 感知机
Category: 读书笔记
Date: 2018-11-04 21:04:02
Modified: 2018-11-07 15:34:59
Tags: 统计学习, 机器学习

感知机（perceptron）是二分类的线性分类模型，其输入是实例的特征向量，输出为实例的类别，取 +1 和 -1 二值。感知机对应于输入空间（特征空间）中将实例划分为正负类别的分离超平面，属于判别模型。

## 2.1 感知机模型

**定义 2.1（感知机）假设输入空间（特征空间）是 ${\cal X}\subseteq\mathbb{R}^n$，输出空间是 ${\cal Y}=\{+1,-1\}$。输入 $x\in{\cal X}$ 表示实例的特征向量，对应于输入空间（特征空间）的点；输出 $y\in{\cal Y}$ 表示实例的类别。由输入空间到输出空间的如下函数：
$$f(x)=\text{sign}(w\cdot x+b)$$
称为感知机。其中，$w$ 和 $b$ 为感知机模型参数，$w\in\mathbb{R}^n$ 叫做权值（weight）或权值向量（weight vector），$b\in\mathbb{R}$ 叫做偏置（bias），$w\cdot x$ 表示 $w$ 和 $x$ 的内积。sign 是符号函数，即：
$$\text{sign}(x)=\begin{cases}+1, & x\geq0 \\ -1, & x<0\end{cases}$$**

感知机是一种线性分类模型。感知机模型的假设空间是定义在特征空间中的所有线性分类模型（linear classification model）或线性分类器（linear classifier），即函数集合：$\{f|f(x)=w\cdot x+b\}$。

感知机的几何解释：对于线性方程
$$w\cdot x+b=0$$
对应于特征空间 $\mathbb{R}^n$ 中的一个超平面 $S$，称为分离超平面（separating hyperplane），其中 $w$ 是超平面的法向量，$b$ 是超平面的截距。这个超平面将特征空间划分为两个部分。

## 2.2 感知机学习策略

### 2.2.1 数据集的线性可分性

**定义 2.2 （数据集的线性可分性）给定一个数据集
$$T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$$
其中，$x_i\in{\cal X}=\mathbb{R}^n$，$y_i\in{\cal Y}=\{+1,-1\}$，$i=1,2,\cdots,N$，如果存在某个超平面 $S$
$$w\cdot x+b=0$$
能够将数据集的正负实例完全正确的划分到超平面的两侧，则称数据集 $T$ 是线性可分数据集（linearly separable data set）；否则，则称数据集 $T$ 线性不可分。**

### 2.2.2 感知机学习策略

为了找出超平面，需要一个学习策略，即定义（经验）损失函数并将损失函数极小化。

损失函数的一个自然选择是误分类点的总数。但是，这样的损失函数不是参数 $w$、$b$ 的连续可导函数，不易优化。损失函数的另一个选择是误分类点到超平面 $S$ 的总距离，这是感知机所采用的。

首先，输入空间 $\mathbb{R}^n$ 中任一点 $x_0$ 到超平面 $S$ 的距离为：
$$\frac{1}{||w||}|w\cdot x+b|$$
这里，$||w||$ 是 $w$ 的 $L_2$ 范数。

其次，注意到对于误分类点数据 $(x_i,y_i)$，下式成立：
$$-y_i(w\cdot x_i+b)>0$$
因此，误分类点到超平面的总距离为：
$$-\frac{1}{||w||}\sum_{x_i\in M}y_i(w\cdot x_i+b)$$
其中，$M$ 是误分类点集合。不考虑 $\frac{1}{||w||}$，就得到感知机学习的损失函数。

给定训练数据集：
$$T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$$
感知机 $\text{sign}(w\cdot x+b)$ 学习的损失函数定义为：
$$L(w,b)=-\sum_{x_i\in M}y_i(w\cdot x_i+b)$$

感知机学习的策略是在假设空间中选取使上面的损失函数最小的模型参数 $w$，$b$，即感知机模型。

## 2.3 感知机学习算法

为最优化上节的损失函数，采取随机梯度下降法（stochastic gradient descent）。

### 2.3.1 感知机学习算法的原始形式

感知机学习算法是对以下最优化问题的算法。给定训练数据集：
$$T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$$
其中 $x_i\in{\cal X}=\mathbb{R}^n$，$y_i\in{\cal Y}=\{+1,-1\}$，$i=1,2,\cdots,N$，求参数 $w$，$b$，使其为以下损失函数极小化的一个解：
$$\min_{w,b} L(w,b)=-\sum_{x_i\in M}y_i(w\cdot x_i+b)$$
其中，$M$ 是误分类点集合。

随机梯度下降法步骤如下：首先，任意选取一个超平面 $w_0$，$b_0$，然后用梯度下降法不断地极小化目标函数。极小化过程不是一次使 $M$ 中所有误分类法的梯度下降，而是一次随机选取一个误分类点使其梯度下降。

假设误分类点集合 $M$ 是固定的，那么损失函数 $L(w,b)$ 的梯度为：
$$\begin{eqnarray}
\nabla_wL(w,b) &=& -\sum_{x_i\in M}y_ix_i \\
\nabla_bL(w,b) &=& -\sum_{x_i\in M}y_i
\end{eqnarray}$$

随机选取一个误分类点 $(x_i,y_i)$ 对 $w$，$b$ 进行更新：
$$\begin{eqnarray}
w &\longleftarrow& w+\eta y_ix_i \\
b &\longleftarrow& b+\eta y_i
\end{eqnarray}$$
式中 $\eta\ (0<\eta\leq 1)$ 是步长，也称学习率（learning rate）。

**算法 2.1 （感知机学习算法的原始形式)  
输入：训练数据集
$$T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$$
其中
$$x_i\in{\cal X}=\mathbb{R}^n,y_i\in{\cal Y}=\{+1,-1\},i=1,2,\cdots,N$$
学习率
$$\eta\ (0<\eta\leq 1)$$
输出：$w$，$b$；
感知机模型
$$f(x)=\text{sign}(w\cdot x+b)$$
(1) 选取初值 $w_0$，$b_0$  
(2) 在训练集中选取数据 $(x_i,y_i)$  
(3) 如果 $y_i(w\cdot x_i+b)\leq 0$
$$\begin{eqnarray}
w &\longleftarrow& w+\eta y_ix_i \\
b &\longleftarrow& b+\eta y_i
\end{eqnarray}$$
(4) 转至 (2)，直至训练集中没有误分类点**

### 2.3.2 算法的收敛性

为便于推导，将偏置并入权重向量，记为 $\hat{w}=(w^\text{T},b)^\text{T}$，同样也将输入向量加以扩充，加进常数 1，记作 $\hat{x}=(x^\text{T},1)^\text{T}$。这样，$\hat{x}\in\mathbb{R}^{n+1}$，$\hat{w}\in\mathbb{R}^{n+1}$，显然 $\hat{w}\cdot\hat{x}=w\cdot x+b$。

**定理 2.1 （Novikoff）设训练集
$$T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$$
线性可分，则  
(1). 存在满足条件 $||\hat{w}_\text{opt}||=1$ 的超平面
$$\hat{w}_\text{opt}\cdot\hat{x}=w_\text{opt}\cdot x_+b_\text{opt}=0$$
将训练数据集完全正确分开；切存在 $\gamma>0$，对所有 $i=1,2,\cdots,N$
$$y_i(\hat{w}_\text{opt}\cdot\hat{x}_i)=y_i(w_\text{opt}\cdot x_i+b_\text{opt})\geq\gamma$$
(2). 令
$$R=\max_{1\leq i\leq N}||\hat{x}_i||$$，则感知机算法 2.1 在训练数据集上的误分类次数 $k$ 满足不等式
$$k\leq\left(\frac{R}{\gamma}\right)^2$$**

证明：（1）由线性可分性的定义即可证明，其中：
$$\gamma=\min_i\{y_i(w_\text{opt}\cdot x_i+b_\text{opt})\}$$
（2）感知机算法从 $\hat{w}_0$ 开始，如果实例被误分类，则更新权重。令 $\hat{w}_{k-1}$ 是第 $k$ 个误分类实例之前的扩充权重向量，即：
$$\hat{w}_{k-1}=(w_{k-1}^\text{T},b_{k-1})^\text{T}$$
则第 $k$ 个被误分类实例的条件是
$$y_i(\hat{w}_{k-1}\cdot\hat{x}_i)=y_i(w_{k-1}\cdot x_i+b_{k-1})\leq0$$
若 $(x_i,y_i)$ 是被 $\hat{w}_{k-1}$ 误分类的数据，则 $w$ 和 $b$ 的更新为
$$\begin{eqnarray}
w_k &\longleftarrow& w_{k-1}+\eta y_ix_i \\
b_k &\longleftarrow& b_{k-1}+\eta y_i
\end{eqnarray}$$
即
$$\hat{w}_k\longleftarrow \hat{w}_{k-1}+\eta y_i\hat{x}_i$$

下面推导两个不等式：

i. $\hat{w}_k\cdot\hat{w}_\text{opt}\geq k\eta\gamma$
$$\hat{w}_k\cdot\hat{w}_\text{opt}=(\hat{w}_{k-1}+\eta y_i\hat{x}_i)\cdot\hat{w}_\text{opt}\geq\hat{w}_{k-1}\cdot\hat{w}_\text{opt}+\eta\gamma\geq\cdots\geq k\eta\gamma$$
ii. $||\hat{w}_k||^2\leq k\eta^2R^2$
$$
\begin{eqnarray}
||\hat{w}_k||^2 &=& ||\hat{w}_{k-1}+\eta y_i\hat{x}_i||^2 \\
&=& ||\hat{w}_{k-1}||^2+2\eta y_i\hat{w}_{k-1}\cdot\hat{x}_i+\eta^2||\hat{x}_i||^2 \\
&\leq& ||\hat{w}_{k-1}||^2+\eta^2||\hat{x}_i||^2 \\
&\leq& ||\hat{w}_{k-1}||^2+\eta^2R^2\leq\cdots\leq k\eta^2R^2
\end{eqnarray}$$

由上述两个不等式
$$k\eta\gamma\leq\hat{w}_k\cdot\hat{w}_\text{opt}\leq||\hat{w}_k||\ ||\hat{w}_\text{opt}||\leq\sqrt{k}\eta R$$
于是
$$k\leq\left(\frac{R}{\gamma}\right)^2$$

定理表明，误分类次数是有上界的，经过有限次搜索可以找到将训练数据完全正确分开的分离超平面。

感知机学习算法存在许多解，这些解既依赖于初值的选择，也依赖于迭代过程中误分类点的选择顺序。

当训练集线性不可分时，感知机学习算法不收敛，迭代结果会发生震荡。

### 2.3.3 感知机学习算法的对偶形式

对偶形式的基本想法是，将 $w$ 和 $b$ 表示为实例 $x_i$ 和标记 $y_i$ 的线性组合的形式，通过求解其系数而求得 $w$ 和 $b$。不失一般性，在算法 2.1 中可以假设初始值 $w_0$ 和 $b_0$ 均为 0，对误分类点 $(x_i,y_i)$ 通过
$$\begin{eqnarray}
w &\longleftarrow& w+\eta y_ix_i \\
b &\longleftarrow& b+\eta y_i
\end{eqnarray}$$
逐步修改 $w$，$b$，设修改 $n$次（随机梯度下降，一个点可能被选择多次），则 $w$ 和 $b$ 关于 $(x_i,y_i)$  的增量分别是 $\alpha_iy_ix_i$ 和 $\alpha_iy_i$ 这里
$$\alpha_i=n_i\eta$$
这样，从学习过程不难看出，最后学习到的 $w$ 和 $b$ 可以分别表示为
$$\begin{eqnarray}
w &=& \sum_{i=1}^N\alpha_iy_ix_i \\
b &=& \sum_{i=1}^N\alpha_iy_i
\end{eqnarray}$$
这里，$\alpha_i\geq0$，$i=1,2,\cdots,N$，当 $\eta=1$ 时，表示第 $i$ 个实例点由于误分类而进行更新的次数。实例点更新次数越多，意味着它距离分离超平面越近，也就越难正确分类。换句话说，这样的实例对学习结果影响很大。

**算法 2.2 （感知机学习算法的对偶形式）  
输入：训练数据集
$$T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$$
其中
$$x_i\in{\cal X}=\mathbb{R}^n,y_i\in{\cal Y}=\{+1,-1\},i=1,2,\cdots,N$$
学习率
$$\eta\ (0<\eta\leq 1)$$
输出：$\alpha$，$b$；
感知机模型
$$f(x)=\text{sign}(\sum_{j=1}^N\alpha_jy_jx_j\cdot x+b)$$
其中 $\alpha=(\alpha_1,\alpha_2,\cdots,\alpha_N)^\text{T}$  
(1) $\alpha\longleftarrow0$， $b\longleftarrow0$  
(2) 在训练集中选取数据 $(x_i,y_i)$  
(3) 如果 $y_i\left(\sum_{j=1}^N\alpha_jy_jx_j\cdot x_i+b\right)\leq 0$
$$\begin{eqnarray}
\alpha_i &\longleftarrow& \alpha_i+\eta \\
b &\longleftarrow& b+\eta y_i
\end{eqnarray}$$
(4) 转至 (2)，直至训练集中没有误分类点**

对偶形式中训练实例仅以内积的形式出现。为了方便，可以预先将训练集中实例间的内积计算出来并以矩阵的形式存储，这个矩阵就是所谓的 Gram 矩阵（Gram matrix）
$$G=[x_i\cdot x_j]_{N\times N}$$
