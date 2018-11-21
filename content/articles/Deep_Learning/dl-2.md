Title: 深度学习 第二章 线性代数
Category: 读书笔记
Date: 2018-11-21 14:02:59
Modified: 2018-11-21 14:31:12
Tags: 机器学习, 深度学习

## 2.1 标量、向量、矩阵和张量

**标量**（scalar）：一个单独的数，用斜体小写字母表示，如 $n\in\mathbb{R}$ 中的 $n$

**向量**（vector）：一列数，用粗斜体小写字母表示
$$\boldsymbol x=\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix}$$
$\boldsymbol x_{-1}$ 表示 $\boldsymbol x$ 中除 $x_1$ 外的所有元素构成的向量。$\boldsymbol x_{-S}$ 表示 $\boldsymbol x$ 中除 $S$ 中指定的索引外的所有元素构成的向量。

**矩阵**（matrix）：二位数组，用粗斜体大写字母表示
$$\boldsymbol A=\begin{bmatrix}
A_{1,1} & A_{1,2} \\
A_{2,1} & A_{2,2}
\end{bmatrix}$$

**张量**（tensor）：坐标超过两维的数组，用粗体大写字母表示。张量 $\bf A$ 中坐标为 $(i,j,k)$ 的元素记为 ${\bf A}_{i,j,k}$

**转置**（transpose）是矩阵以其主对角线（main diagonal）为轴的镜像。
$$({\boldsymbol A}^\text{T})_{i,j}=A_{j,i}$$
标量的转置等于它本身。

**广播**（broadcasting）是矩阵和向量采取下面的规则相加
$${\boldsymbol C}={\boldsymbol A}+{\boldsymbol b}\Longleftrightarrow C_{i,j}=A_{i,j}+b_j$$
也就是向量 ${\boldsymbol b}$ 和矩阵 ${\boldsymbol A}$ 的每一行相加。

## 2.2 矩阵和向量相乘

**矩阵相乘**（matrix product）：要求第一个矩阵的列数等于第二个矩阵的行数。满足分配律、结合律，一般不满足交换律。
$${\boldsymbol C}=\boldsymbol {AB}\Longleftrightarrow C_{i,j}=\sum_kA_{i,k}B_{k,j}$$

**Hadamard 乘积**：要求两个矩阵形状一样，为对应元素乘积。满足交换律。
$${\boldsymbol C}={\boldsymbol A}\odot{\boldsymbol B}\Longleftrightarrow C_{i,j}=A_{i,j}B_{i,j}$$

**向量点积**（vector dot product）：要求两个向量维度相同。满足交换律。
$${\boldsymbol z}=\boldsymbol {xy}\Longleftrightarrow z_i=x_iy_i$$
也可写作矩阵乘积的形式
$${\boldsymbol z}={\boldsymbol x}^\text{T}{\boldsymbol y}$$
和 Hadamard 乘积形式
$${\boldsymbol z}={\boldsymbol x}\odot{\boldsymbol y}$$

## 2.3 范数

有时我们需要衡量一个向量的大小。在机器学习中，我们经常使用**范数**（norm）来衡量向量的大小。形式上，$L^p$ 范数定义如下：
$$\|{\boldsymbol x}\|_p=\left(\sum_i|x_i|^p\right)^{\frac{1}{p}}$$
其中，$p\in\mathbb{R}$，$p\geq1$。

更严格的，范数是满足下列性质的任意函数：

- $f({\boldsymbol x})=0\Rightarrow{\boldsymbol x}={\boldsymbol 0}$
- $f({\boldsymbol x}+{\boldsymbol y})\leq f({\boldsymbol x})+f({\boldsymbol y})$
- $\forall\alpha\in\mathbb{R},\ f(\alpha{\boldsymbol x})=|\alpha|f({\boldsymbol x})$

当 $p=2$ 时，$L^2$ 范数称为**欧几里得范数**（Euclidean norm），经常简化表示为 $\|\boldsymbol x\|$，略去下标 2。平方 $L^2$ 范数也经常用来衡量向量的大小，可以简单的通过点积 ${\boldsymbol x}^\text{T}{\boldsymbol x}$ 计算。

平方 $L^2$ 范数在数学和计算上都比 $L^2$ 范数本身更方便。例如，平方 $L^2$ 范数对每个元素的导数只取决于对应的元素。

但在某些情况下，平方 $L^2$ 范数也可能不受欢迎，因为它在原点附近增长得十分缓慢。在某些机器学习应用中，区分恰好是零元素和非零但值很小的元素是很重要的。在这些情况下，我们转而使用在各个位置斜率相同，同时保持简单的数学形式的函数：$L^1$ 范数：
$$\|{\boldsymbol x}\|_1=\sum_i|x_i|$$

另外一个常用的范数是**最大范数**（max norm）：
$$\|{\boldsymbol x}\|_{\infty}=\max_i|x_i|$$

有时候我们可能也希望衡量矩阵的大小。在深度学习中，最常见的做法是使用 **弗洛宾尼斯范数**（Frobenius norm）：
$$\|{\boldsymbol A}\|_F=\sqrt{\sum_{i,j}A_{i,j}^2}$$
其类似于向量的 $L^2$ 范数。

## 2.4 特征分解

**特征分解**（eigendecomposition）是使用最广泛的矩阵分解之一，它将矩阵分解为一组特征值和特征向量。

设方阵 ${\boldsymbol A}$ 的特征值为 $\lambda$，特征向量为 ${\boldsymbol v}$，即
$$\boldsymbol {Av}=\lambda{\boldsymbol v}$$
假设矩阵 $\boldsymbol A$ 有 $n$ 个线性无关的特征向量 $\left\{\boldsymbol v^{(1)},\cdots,\boldsymbol v^{(n)}\right\}$，对应和特征值 $\left\{\lambda_1,\cdots,\lambda_n\right\}$。取矩阵 $\boldsymbol V=\left[\boldsymbol v^{(1)},\cdots,\boldsymbol v^{(n)}\right]$，$\boldsymbol\lambda=[\lambda_1,\cdots,\lambda_n]^\text{T}$，则 $\boldsymbol A$ 的特征分解可记作
$$\boldsymbol A=\boldsymbol V\ \text{diag}(\boldsymbol\lambda){\boldsymbol V}^{\text{-}1}$$

实对称矩阵都可以分解成实特征值和实特征向量：
$$\boldsymbol A=\boldsymbol {Q\Lambda}{\boldsymbol Q}^{-1}$$
其中，$\boldsymbol Q$ 是正交矩阵。

矩阵的特征分解提供了许多有用的信息。例如，矩阵是奇异的，当且仅当含有零特征值。

考虑下面的二次方程
$$f(\boldsymbol x)=\boldsymbol x^\text{T}\boldsymbol {Ax}$$
其中限制 $\|\boldsymbol x\|_2=1$，则当 $\boldsymbol x$ 等于 $\boldsymbol A$ 的某个特征向量时，$f$ 将返回对应的特征值。在限制条件下，$f$ 的最大值是最大特征值，最小值是最小特征值。证明方法是将任意的 $\boldsymbol x$ 展开为 $\boldsymbol A$ 特征向量的线性组合。

**正定矩阵**（positive definite）：所有特征值都是正数的矩阵。

**半正定矩阵**（positive semidefinite）：所有特征值都是非负数的矩阵。

**负定矩阵**（negative definite）：所有特征值都是负数的矩阵。

**半负定矩阵**（negative semidefinite）：所有特征值都是非正数的矩阵。

对半正定矩阵 $\boldsymbol A$，$\forall \boldsymbol x,\ \boldsymbol x^\text{T}\boldsymbol{Ax}\geq0$。

此外，正定矩阵还保证 $\boldsymbol x^\text{T}\boldsymbol{Ax}=0\Rightarrow\boldsymbol x=\boldsymbol 0$。

## 2.5 奇异值分解

**奇异值分解**（singular value decomposition，SVD）是另一种矩阵分解方法。

$$\boldsymbol A=\boldsymbol {UD}{\boldsymbol V}^\text{T}$$
其中，$\boldsymbol A$ 是 $m\times n$ 的矩阵，$\boldsymbol U$ 是 $m\times m$ 的正交矩阵，$\boldsymbol V$ 是 $n\times n$ 的正交矩阵，$\boldsymbol D$ 是 $m\times n$ 的对角矩阵。

对角矩阵 $\boldsymbol D$ 对角线上的元素称为矩阵 $\boldsymbol A$ 的奇异值（singular value）。矩阵 $\boldsymbol U$ 的列向量称为左奇异向量（left singular vector），它是 $\boldsymbol {AA}^\text{T}$ 的特征向量。矩阵 $\boldsymbol V$ 的列向量称为右奇异向量（right singular vector），它是 $\boldsymbol A^\text{T}\boldsymbol A$ 的特征向量。$\boldsymbol A$ 的非零奇异值是 $\boldsymbol {AA}^\text{T}$ 和 $\boldsymbol A^\text{T}\boldsymbol A$ 特征值的平方根。

每个实数矩阵都有奇异值分解。

## 2.6 摩尔－彭若斯伪逆

矩阵 $\boldsymbol A$ 的摩尔－彭若斯伪逆（Moore-Penrose pseudoinverse）定义为：
$$\boldsymbol A^+=\lim_{\alpha\to0^+}\left(\boldsymbol A^\text{T}\boldsymbol A+\alpha \boldsymbol I\right)^{-1}\boldsymbol A^\text{T}$$
一般计算使用下面的公式：
$$\boldsymbol A^+=\boldsymbol {V}{\boldsymbol D}^+\boldsymbol U^\text{T}$$
其中，矩阵 $\boldsymbol U$、$\boldsymbol D$ 和 $\boldsymbol V$ 是矩阵 $\boldsymbol A$ 奇异值分解后得到的矩阵。对角矩阵 $\boldsymbol D$ 的伪逆 $\boldsymbol D^+$ 是其非零元素取倒数之后再转置得到的。

对于线性方程：
$$\boldsymbol {Ax}=\boldsymbol y$$
当矩阵 $\boldsymbol A$ 的列数多于行数时，使用伪逆求解线性方程是众多可能解法中的一种，$\boldsymbol x=\boldsymbol A^+\boldsymbol y$ 是所有可行解中欧几里得范数 $\|\boldsymbol x\|_2$ 最小的那一个。

当矩阵 $\boldsymbol A$ 的列数多于行数时，可能没有解，通过伪逆求得的 $\boldsymbol x$ 是使得 $\|\boldsymbol {Ax}-\boldsymbol y\|_2$ 最小的那一个。

## 2.7 迹运算

迹运算返回的是矩阵对角元素的和：
$$\text{Tr}(\boldsymbol A)=\sum_iA_{i,i}$$

利用迹运算可以重写矩阵弗洛宾尼斯范数：
$$\|{\boldsymbol A}\|_F=\sqrt{\sum_{i,j}A_{i,j}^2}=\sqrt{\text{Tr}(\boldsymbol {AA}^\text{T})}$$

迹运算性质：

- $\text{Tr}(\boldsymbol A)=\text{Tr}\left(\boldsymbol A^\text{T}\right)$
- $\text{Tr}(\boldsymbol{ABC})=\text{Tr}(\boldsymbol{CAB})=\text{Tr}(\boldsymbol{BCA})$
- $\text{Tr}(a)=a$

## 2.8 行列式

记作 $\text{det}(\boldsymbol A)$，等于矩阵特征值的乘积。

行列式的绝对值可以用来衡量矩阵参与矩阵乘法后空间扩大或缩小了多少。如果行列式是 0，那么空间至少沿着某一维完全收缩了，使其失去了所有的体积；如果行列式是 1，那么这个转换保持空间体积不变。

## 2.9 实例：主成分分析

**主成分分析**（principal components analysis，PCA）是一个简单的机器学习算法。

**问题**：假设在 $\mathbb{R}^n$ 空间中有 $m$ 个点 $\left\{\boldsymbol x^{(1)},\cdots,\boldsymbol x^{(m)}\right\}$，我们希望对这些点进行有损压缩。有损压缩表示我们使用更少的内存，但损失一些精度去存储这些点。我们希望损失的精度尽可能少。

**分析**：编码这些点的一种方式是用低维表示。对于
