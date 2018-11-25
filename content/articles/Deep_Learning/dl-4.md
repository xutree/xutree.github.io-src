Title: 深度学习 第四章 数值计算
Category: 读书笔记
Date: 2018-11-24 21:02:36
Modified: 2018-11-25 16:08:25
Tags: 机器学习, 深度学习

## 4.1 上溢和下溢

数值**上溢**（overflow）：大量级的数被近似为正无穷或负无穷时发生上溢，进一步运算导致无限值变为非数字。

数值**下溢**（underflow）：接近零的数被四舍五入为0时发生下溢。被零除，取零的对数，进一步运算会变为非数字。

必须对上溢和下溢进行数值稳定的一个例子是 softmax 函数。

在数学，尤其是概率论和相关领域中，softmax 函数或称归一化指数函数，是逻辑函数的一种推广。它能将一个含任意实数的 $K$ 维向量 $\boldsymbol {z}$ “压缩”到另一个 $K$ 维实向量 $\sigma(\boldsymbol z)$ 中，使得每一个元素的范围都在 $(0,1)$ 之间，并且所有元素的和为 1。该函数的形式通常按下面的式子给出：
$$\text{softmax}(\boldsymbol x)_i=\frac{\text{e}^{x_i}}{\sum_{j=1}^K\text{e}^{x_j}}$$

Softmax 函数实际上是有限项离散概率分布的梯度对数归一化。因此，softmax函数在包括 多项逻辑回归，多项线性判别分析，朴素贝叶斯分类器和人工神经网络等的多种基于概率的多分类问题方法中都有着广泛应用。

Softmax 函数可以通过执行下面的替换进行稳定：
$$\boldsymbol z=\boldsymbol x-\max_{i}x_i$$

在实现深度学习算法时，底层库的开发者应该牢记数值问题。

## 4.2 病态条件

考虑函数 $f(\boldsymbol x)=\boldsymbol A^{-1}\boldsymbol x$。当 $\boldsymbol A\in\mathbb{R}^{n\times n}$ 具有特征分解时，其条件数为：
$$\max_{i,j}\left\lvert\frac{\lambda_i}{\lambda_j}\right\rvert$$
是最大和最小特征值的模之比。当条件数很大时，矩阵求逆对输入的误差特别敏感。

## 4.3 基于导数的优化方法

### 4.3.1 梯度、方向导数、Jacobian 和 Hessian 矩阵

- 梯度向量：由多维输入一维输出的一阶导数构成
- 雅克比矩阵：由多维输入多维输出的一阶导数构成
- 海森矩阵：由多维输入一维输出的二阶导数构成

#### 4.3.1.1 梯度

在向量微积分中，**标量场**的**梯度**（gradient）是一个**向量场**。标量场中某一点的梯度指向在这点标量场增长最快的方向（当然要比较的话必须固定方向的长度），梯度的绝对值是长度为 1 的方向中函数最大的增加率

多维函数的梯度是相对于一个向量求导的导数，记作
$$\nabla_{\boldsymbol x}f(\boldsymbol x)$$
此结果是一个列向量，第 $i$ 个元素是 $f$ 关于 $x_i$ 的偏导数（partial derivation）。

#### 4.3.1.2 方向导数

**方向导数**（directional derivation）是函数 $f$ 在 $\boldsymbol u$ 方向上的斜率。是函数 $f(\boldsymbol x+\alpha\boldsymbol u)$ 关于 $\alpha$ 的导数（在 $\alpha=0$ 时取得），根据链式法则：
$$\begin{eqnarray}
\frac{\partial f(\boldsymbol x+\alpha\boldsymbol u)}{\partial\alpha} &=& \frac{\partial f(\boldsymbol x+\alpha\boldsymbol u)}{\partial(\boldsymbol x+\alpha\boldsymbol u)}\frac{\partial(\boldsymbol x+\alpha\boldsymbol u)}{\partial \alpha} \\
&=& \nabla_{{\boldsymbol x}^\text{T}}f(\boldsymbol x)\boldsymbol u
\end{eqnarray}$$
注意等号右边第一项为标量对向量的导数，需要转置。再利用 $\alpha=0$，并注意等式左边为标量，对等式两边同时转置，得方向导数为：
$$\boldsymbol u^\text{T}\nabla_{\boldsymbol x}f(\boldsymbol x)$$

如果函数 $f(\boldsymbol x)$ 在点 $\boldsymbol x$ 处可微，则沿着任意非零向量 $\boldsymbol u$ 的方向导数都存在。对赋范向量空间或内积空间有：
$$\nabla_{\boldsymbol u}f(\boldsymbol x)=\boldsymbol u\cdot \nabla_{\boldsymbol x}f(\boldsymbol x)=\boldsymbol u^\text{T}\nabla_{\boldsymbol x}f(\boldsymbol x)$$
其中，$\cdot$ 是内积运算。

#### 4.3.1.3 雅克比矩阵

有时我们需要计算**输入和输出都是向量**的函数的所有偏导数。包含所有这样的偏导数的矩阵被称为**雅可比矩阵**（Jacobian matrix）。

具体来说，对于函数 $f:\mathbb{R}^m\to\mathbb{R}^n$，$f$ 的雅克比矩阵 $\boldsymbol J\in\mathbb{R}^{n\times m}$ 定义为：
$$J_{i,j}=\frac{\partial}{\partial x_j}f(\boldsymbol x)_i$$
即
$$\boldsymbol J=\begin{bmatrix}
\frac{\partial f(\boldsymbol x)_1}{\partial x_1} & \frac{\partial f(\boldsymbol x)_1}{\partial x_2} & \cdots & \frac{\partial f(\boldsymbol x)_1}{\partial x_m} \\
\frac{\partial f(\boldsymbol x)_2}{\partial x_1} & \frac{\partial f(\boldsymbol x)_2}{\partial x_2} & \cdots & \frac{\partial f(\boldsymbol x)_2}{\partial x_m} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f(\boldsymbol x)_n}{\partial x_1} & \frac{\partial f(\boldsymbol x)_n}{\partial x_2} & \cdots & \frac{\partial f(\boldsymbol x)_n}{\partial x_m} \\
\end{bmatrix}
=\begin{bmatrix}
\left(\nabla_{\boldsymbol x}f(\boldsymbol x)_1\right)^\text{T} \\
\left(\nabla_{\boldsymbol x}f(\boldsymbol x)_2\right)^\text{T} \\
\vdots \\
\left(\nabla_{\boldsymbol x}f(\boldsymbol x)_n\right)^\text{T}
\end{bmatrix}$$
它的每一行都是由相应的函数的梯度向量的转置构成的。当目标函数为标量函数时，Jacobi 矩阵就是梯度向量。雅克比矩阵也记为：
$$J_f(x_1,x_2,\cdots,x_m)\ \ 或\ \  \frac{\partial (f(\boldsymbol x)_1,f(\boldsymbol x)_2,\cdots,f(\boldsymbol x_n)}{\partial (x_1,x_2,\cdots,x_m)}$$

如果 $\boldsymbol x_0$ 是 $\mathbb{R}^m$ 中的一点，$f$ 在 $\boldsymbol x_0$ 点可微分，根据数学分析，$J_{f}(\boldsymbol x_0)$ 是在这点的导数。在此情况下，$J_{f}(\boldsymbol x_0)$ 这个线性映射即 $f$ 在点 $\boldsymbol x_0$ 附近的**最优线性逼近**，也就是说当 $\boldsymbol x$ 足够靠近点 $\boldsymbol x_0$ 时，我们有
$$f(\boldsymbol x)=f(\boldsymbol x_0)+J_f(\boldsymbol x_0)(\boldsymbol x-\boldsymbol x_0)$$

如果 $m=n$，那么 $f$ 是从 $n$ 维空间到 $n$ 维空间的函数，且它的雅可比矩阵是一个方块矩阵。于是我们可以取它的行列式，称为**雅可比行列式**。

在某个给定点的雅可比行列式提供了 $f$ 在接近该点时的表现的重要信息。例如，如果连续可微函数 $f$ 在 $\boldsymbol x$ 点的雅可比行列式不是零，那么它在该点附近具有反函数。这称为**反函数定理**。

更进一步，如果 $\boldsymbol x$ 点的雅可比行列式是正数，则 $f$ 在 $\boldsymbol x$ 点的取向不变；如果是负数，则 $f$ 的取向相反。而从雅可比行列式的绝对值，就可以知道函数 $f$ 在 $\boldsymbol x$ 点的缩放因子；这就是它出现在换元积分法中的原因。

#### 4.3.1.4 海森矩阵

**海森矩阵**（Hessian matrix）是一个**多变量实值函数**的二阶偏导数组成的方块矩阵。假如有一实函数 $f(\boldsymbol x)$，如果 $f$ 所有的二阶偏导数都存在，那么 $f$ 的海森矩阵的第 $ij$ 项即：
$$H(f)(\boldsymbol x)_{ij}=\frac{\partial^2}{\partial x_i\partial x_j}f(\boldsymbol x)$$
即
$$\boldsymbol H(f)=\begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1\partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1\partial x_m} \\
\frac{\partial^2 f}{\partial x_2\partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2\partial x_m} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_m\partial x_1} & \frac{\partial^2 f}{\partial x_m\partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_m^2} \\
\end{bmatrix}=\boldsymbol J_{\nabla_f(\boldsymbol x)}(\boldsymbol x)$$

海森矩阵的混合偏导数是海森矩阵非主对角线上的元素。假如他们是连续的，那么求导顺序没有区别，即
$${\frac  {\partial }{\partial x_1}}\left({\frac  {\partial f}{\partial x_2}}\right)={\frac  {\partial }{\partial x_2}}\left({\frac  {\partial f}{\partial x_1}}\right)$$
上式也可写为
$$f_{x_1x_2}=f_{x_2x_1}$$
也就是说，如果 $f$ 函数在区域 $D$ 内的每个二阶导数都是连续函数，那么 $f$ 的海森矩阵在 $D$ 区域内为对称矩阵。

**二阶导数测试**（second derivation test）：当函数 $f:\mathbb{R}^n\to\mathbb{R}$ 二阶连续可导时，Hessian 矩阵 $\boldsymbol H$ 在临界点 $\boldsymbol x_{0}$ (即，所有一阶偏导数都为零)上是一个 $n\times n$ 阶的对称矩阵。计算在 临界点 $\boldsymbol x_{0}$ 的海森矩阵：

- 当 $\boldsymbol H$ 是正定矩阵时（所有特征值都是正的），临界点 $x_{0}$ 是一个局部的极小值
- 当 $\boldsymbol H$ 是负定矩阵时（所有特征值都是正的），临界点 $x_{0}$ 是一个局部的极大值
- $\boldsymbol H=0$，需要更高阶的导数来帮助判断
- 在其余情况下，临界点 $x_{0}$ 不是局部极值

实值函数 $f$ 在特定方向 $\boldsymbol d$ 上的二阶导数为：
$$\nabla_{\boldsymbol d}(\nabla_{\boldsymbol d}f)=\nabla_{\boldsymbol d}(\boldsymbol d^\text{T}\nabla f)=\nabla(\boldsymbol d^\text{T}\nabla f)\boldsymbol d=\boldsymbol d^\text{T}\nabla(\nabla f)\boldsymbol d=\boldsymbol d^\text{T}\boldsymbol {Hd}$$
当 $\boldsymbol d$ 是 $\boldsymbol H$ 的一个特征向量时，这个方向的二阶导数就是对应的特征值。对于其他的方向 $\boldsymbol d$，方向二阶导数是所有特征值的加权平均，权重在 0 和 1 之间。最大特征值确定最大二阶导数，最小特征确定最下二阶导数。

### 4.3.2 梯度下降法

我们经常最小化具有多维输入的函数：$f:\mathbb{R}^n\to\mathbb{R}$。为了使“最小化”的概念有意义，输出必须是一维的（标量）。

为最小化 $f$，我们希望找到使 $f$ 下降得最快的方向。计算方向导数：
$$\min_{\boldsymbol u,\boldsymbol u^\text{T}\boldsymbol u=1}\boldsymbol u^\text{T}\nabla_{\boldsymbol x}f(\boldsymbol x) \\
=\min_{\boldsymbol u,\boldsymbol u^\text{T}\boldsymbol u=1}\|\boldsymbol u\|_2\|\nabla_{\boldsymbol x}f(\boldsymbol x)\|_2\cos\theta \\
=\min_{\boldsymbol u}\cos\theta$$
其中 $\theta$ 是 $\boldsymbol u$ 与梯度的夹角。这表明当 $\boldsymbol u$ 与梯度方向相反时，函数下降最快。即梯度向量指向上坡，负梯度向量指向下坡。我们在负梯度方向上移动可以减小 $f$，这被称为**最速下降法**（method of steepest descent）或**梯度下降**（gradient descent）。

最速下降建议新的点为：
$$\boldsymbol x'=\boldsymbol x-\epsilon\nabla_{\boldsymbol x}f(\boldsymbol x)$$
其中 $\epsilon$ 为**学习率**（learning rate），是一个确定步长大小的正标量。我们可以通过几种不同的方式选择 $\epsilon$。普遍的方式是选择一个小常数。有时我们通过计算，选择使方向导数消失的步长。还有一种方法是根据几个 $\epsilon$ 计算 $f(\boldsymbol x-\epsilon\nabla_{\boldsymbol x}f(\boldsymbol x))$，并选择其中能产生最小目标函数值的 $\epsilon$。这种策略称为线搜索。

我们可以通过（方向）二阶导数预期一个梯度下降步骤能表现得多好。函数 $f(\boldsymbol x)$ 在当前点 $\boldsymbol x^{(0)}$ 的二阶泰勒近似为：
$$\begin{eqnarray}
f(\boldsymbol x) &\approx& f(\boldsymbol x^{(0)})+(\boldsymbol x-\boldsymbol x^{(0)})^\text{T}\nabla_{\boldsymbol x}f(\boldsymbol x^{(0)}) \\
&+& \frac{1}{2}(\boldsymbol x-\boldsymbol x^{(0)})^\text{T}\boldsymbol H(f)(\boldsymbol x^{(0)})(\boldsymbol x-\boldsymbol x^{(0)})
\end{eqnarray}$$
如果我们使用学习率 $\epsilon$，那么新的点 $\boldsymbol x$ 将会是 $\boldsymbol x^{(0)}-\epsilon\nabla_{\boldsymbol x}f(\boldsymbol x^{(0)})$，带入上式，令 $\boldsymbol g=\nabla_{\boldsymbol x}f(\boldsymbol x^{(0)})$，$\boldsymbol H=\boldsymbol H(f)(\boldsymbol x^{(0)})$ 得：
$$f(\boldsymbol x^{(0)}-\epsilon\boldsymbol g) \approx f(\boldsymbol x^{(0)})-\epsilon\boldsymbol g^\text{T}\boldsymbol g+\frac{1}{2}\epsilon^2\boldsymbol g^\text{T}\boldsymbol H\boldsymbol g$$
上式是关于 $\epsilon$ 的二次函数，所以，当 $\boldsymbol g^\text{T}\boldsymbol H\boldsymbol g$ 为零或负时，增加 $\epsilon$ 将永远使得 $f$ 下降；当 $\boldsymbol g^\text{T}\boldsymbol H\boldsymbol g$ 为正时，则使近似泰勒级数下降最多的最优步长为：
$$\epsilon^\ast=\frac{\boldsymbol g^\text{T}\boldsymbol g}{\boldsymbol g^\text{T}\boldsymbol H\boldsymbol g}$$
最坏的情况下，$\boldsymbol d$ 与 $\boldsymbol H$ 最大特征值 $\lambda_{\max}$ 对应的特征向量对齐，则最优步长是 $\frac{1}{\lambda_\max}$。当我们要最小化的函数能用二次函数很好的近似的情况下，海森矩阵的特征值决定了学习率的量级。

最速下降在梯度的每一个元素为零时收敛（或在实践中，近似为零）。在某些情况下，我们也许能够避免运行该迭代算法，并通过解方程 $\nabla_{\boldsymbol x}f(\boldsymbol x)=0$ 直接跳到临界点。

虽然梯度下降被限制在连续空间中的优化问题，但不断向更好的情况移动一小步的一般概念可以推广到离散空间。递增带有离散参数的目标函数称为**爬山**（hill climbing）算法。

### 4.3.3 牛顿法

梯度下降法利用函数一阶导数的信息，在局部位置用一阶方程（一维对应直线，二维对应平面，高维对应超平面）拟合函数，然后沿着拟合函数函数值减小方向下降。

牛顿法则利用函数一阶和二阶导数的信息，在局部位置用二阶方程（一维对应二次曲线，二维对应二次曲面，高维对应超二次曲面）拟合函数，然后沿着拟合函数函数值减小方向下降。

梯度下降法和牛顿法相比，两者都是迭代求解，不过梯度下降法是梯度求解，而牛顿法是用二阶的海森矩阵的逆矩阵求解。相对而言，使用牛顿法收敛更快（迭代更少次数）。但是每次迭代的时间比梯度下降法长。

目标函数 $f(\boldsymbol x)$ 在 $\boldsymbol x^{(0)}$ 处的二阶泰勒展开式为：
$$f(\boldsymbol x+\boldsymbol x^{(0)})=f(\boldsymbol x^{(0)})+\boldsymbol x^\text{T}\nabla_{\boldsymbol x}f(\boldsymbol x^{(0)})+\frac{1}{2}\boldsymbol x^\text{T}\boldsymbol H(f)(\boldsymbol x^{(0)})\boldsymbol x$$
当 $\boldsymbol x^{(0)}$ 固定时，$\boldsymbol x$ 取多少可以使 $f(\boldsymbol {x+x}^{(0)})$ 最小呢，由于上式是 $\boldsymbol x$ 的二次函数，对 $\boldsymbol x$ 求偏导得临界点：
$$\boldsymbol x^\ast=\boldsymbol x^{(0)}-\boldsymbol H(f)(\boldsymbol x^{(0)})^{-1}\nabla_{\boldsymbol x}f(\boldsymbol x^{(0)})$$
如果 $f$ 是一个正定二次函数，牛顿法只要使用上式一次就可以跳到函数的最小点。如果 $f$ 不是一个真正的二次但能在局部近似为正定二次，牛顿法则需要多次迭代应用上式。

仅使用梯度信息的优化算法称为**一阶优化算法**（first-order optimization algorithms），如梯度下降。使用 Hessian 矩阵的优化算法称为**二阶优化算法**（second-order optimization algorithms），如牛顿法。
