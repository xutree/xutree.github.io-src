Title: 统计学习方法 第六章 逻辑回归与最大熵模型
Category: 读书笔记
Date: 2018-11-09 16:17:17
Modified: 2018-11-11 13:21:32
Tags: 统计学习, 机器学习

逻辑回归（logistic regression）是统计学习中的经典分类方法。最大熵是概率模型学习的一个准则，将其推广到分类问题得到最大熵模型（maximum entropy model）。

逻辑回归模型和最大熵模型都属于对数线性模型。

## 6.1 逻辑回归模型

### 6.1.1 逻辑分布

**
定义 6.1（逻辑分布）设 $X$ 是连续随机变量，$X$ 服从逻辑分布是指 $X$ 具有下列分布函数和密度函数：
$$\begin{eqnarray}
F(x) &=& P(X\leq x)=\frac{1}{1+\text{e}^{-(x-\mu)/\gamma}} \\
f(x) &=& F'(x)=\frac{\text{e}^{-(x-\mu)/\gamma}}{\gamma(1+\text{e}^{-(x-\mu)/\gamma})^2}
\end{eqnarray}$$
式中，$\mu$ 为位置参数，$\gamma>0$ 为形状参数。
**

下图中绘制了对于不用 $\gamma$ 逻辑分布函数和概率密度函数。分布函数是一条 S 形曲线（sigmoid curve）。该曲线以点 $\left(\mu,\frac{1}{2}\right)$ 为中心对称，即满足
$$F(-x+\mu)+F(x+\mu)=1$$

![逻辑分布]({static}/images/statistical_learning_6.1.png)

曲线在中心附近增长速度较快，在两端增长速度较慢。

### 6.1.2 二项逻辑回归模型

二项逻辑回归模型（binomial logistic regression model）是一种分类模型，由条件概率 $P(Y|X)$ 表示，形式为参数化的逻辑分布。这里，随机变量 $X$ 取值为实数，随机变量 $Y$ 取值为 1 或 0，我们通过监督学习的方法来估计模型参数。

**
定义 6.2 （逻辑回归模型）二项逻辑回归模型是如下的条件概率分布：
$$\begin{eqnarray}
P(Y=1|x) &=& \frac{\exp(w\cdot x+b)}{1+\exp(w\cdot x+b)} \\
P(Y=0|x) &=& \frac{1}{1+\exp(w\cdot x+b)}
\end{eqnarray}$$
这里，$x\in\mathbb{R}^n$ 是输入，$Y\in\{0,1\}$ 是输出，$w\in\mathbb{R}^n$ 和 $b\in\mathbb{R}$ 是参数（分别称为权重向量和偏置），$w\cdot x$ 是内积。
**

对于给定的输入实例 $x$，按照定义 6.2 可以求得 $P(Y=1|x)$ 和 $P(Y=0|x)$。逻辑回归比较两个概率值的大小，将实例 $x$ 分到概率值较大的那一类。

有时为了方便，将权重向量和输入向量加以扩充，即
$$w=\left(w^{(1)},w^{(2)},\cdots,w^{(n)},1\right)^\text{T}\\
x=\left(x^{(1)},x^{(2)},\cdots,x^{(n)},1\right)^\text{T}$$
这时，逻辑回归模型如下：
$$\begin{eqnarray}
P(Y=1|x) &=& \frac{\exp(w\cdot x)}{1+\exp(w\cdot x)} \\
P(Y=0|x) &=& \frac{1}{1+\exp(w\cdot x)}
\end{eqnarray}$$

一个事件的几率（odds）是指该事件发生的概率与该事件不发生的概率的比值，该事件的对数几率（log odds）或 logit 函数是
$$\text{logit}(p)=\log\frac{p}{1-p}$$

对逻辑回归而言，由扩充后的回归模型得
$$\text{logit}\left(P(Y=1|x)\right)=\log\frac{P(Y=1|x)}{1-P(Y=1|x)}=w\cdot x$$
也就是说，输出 $Y=1$ 的对数几率是输入 $x$ 的线性函数，或者说，输出 $Y=1$ 的对数几率是由输入 $x$ 的线性函数表示的模型，即逻辑回归模型。

换一个角度看，考虑对输入 $x$ 进行分类的线性函数 $w\cdot x$（扩充后的），其值域为实数域。通过逻辑回归模型定义式可以将线性函数 $w\cdot x$ 转换为概率
$$P(Y=1|x)=\frac{\exp(w\cdot x)}{1+\exp(w\cdot x)}$$
上面的分布实际上是逻辑分布。这是，线性函数的值越接近 $+\infty$，概率值就越接近 1；线性函数的值越接近 $-\infty$，概率在就越接近 0。这样的模型就是逻辑回归模型。

### 6.1.3 模型参数估计

逻辑回归模型学习时，对于给定的训练数据集
$$T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$$
其中 $x_i\in\mathbb{R}^n$，$y_i\in\{0,1\}$，可以应用极大似然估计法估计模型参数，从而得到逻辑回归模型。

设
$$P(Y=1|x) = \pi(x) \\
P(Y=0|x) = 1-\pi(x)$$
似然函数为
$$\prod_{i=1}^N\left[\pi(x_i)\right]^{y_i}\left[1-\pi(x_i)\right]^{1-y_i}$$
对数似然函数为
$$\begin{eqnarray}
L(w) &=& \sum_{i=1}^N\left[y_i\log\pi(x_i)+(1-y_i)\log(1-\pi(x_i))\right] \\
&=& \sum_{i=1}^N\left[y_i\log\frac{\pi(x_i)}{1-\pi(x_i)}+\log(1-\pi(x_i))\right] \\
&=& \sum_{i=1}^N[y_i(w\cdot x_i)-\log(1+\exp(w\cdot x_i))]
\end{eqnarray}$$
对 $L(w)$ 求极大值，得到 $w$ 的估计值。

这样，问题就变成以对数似然函数为目标函数的最优化问题。逻辑回归学习中通常采用的方法是梯度下降法和拟牛顿法。

假设 $w$ 的极大似然估计值是 $\hat{w}$，那么学到的逻辑回归模型为
$$P(Y=1|x)=\frac{\exp(\hat{w}\cdot x)}{1+\exp(\hat{w}\cdot x)} \\
P(Y=0|x)=\frac{1}{1+\exp(\hat{w}\cdot x)}$$

### 6.1.4 多项逻辑回归

可以将二项回归模型推广到多项逻辑回归模型（multi-nominal logistic regression model），用于多类分类。

假设离散型随机变量 $Y$ 的取值集合是 $\{1,2,\cdots,K\}$，那么多项逻辑回归模型是
$$P(Y=k|x)=\frac{\exp(w_k\cdot x)}{1+\sum_{k=1}^{K-1}\exp(w_k\cdot x)},k=1,2,\cdots,K-1 \\
P(Y=K|x)=\frac{1}{1+\sum_{k=1}^{K-1}\exp(w_k\cdot x)}$$
这里，$x\in\mathbb{R}^{n+1}$，$w_k\in\mathbb{R}^{n+1}$
二项逻辑回归的参数估计法也可以推广到多项逻辑回归。

## 6.2 最大熵模型

最大熵模型（maximum entropy model）由最大熵原理推导实现。

### 6.2.1 最大熵原理

最大熵原理是概率模型学习的一个准则。最大熵原理认为：学习概率模型时，在所有可能的概率模型（分布）中，熵最大的模型时最好的模型。

通常用约束条件来确定概率模型的集合，所以，最大熵原理也可以表述为在满足约束条件的模型集合中选取熵最大的模型。

假设离散随机变量 $X$ 的概率分布是 $P(X)$，则其熵是
$$H(P)=-\sum_xP(x)\log P(x)$$
熵满足下列不等式
$$0\leq H(P)\leq\log |X|$$
式中，$|X|$ 是 $X$ 取值个数，当且仅当 $X$ 的分布是均匀分布时右边的等号成立。也就是说，当 $X$ 服从均匀分布时，熵最大。

### 6.2.2 最大熵模型的定义

最大熵原理是统计学习的一般原理，将它应用到分类得到最大熵模型。

假设分类模型是一个条件概率分布 $P(Y|X)$，给定一个训练数据集
$$T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$$
学习的目标是用最大熵原理选择最好的分类模型。

首先考虑模型应该满足的条件。给定训练数据集，可以确定联合概率分布 $P(X,Y)$ 和边缘分布 $P(X)$ 的经验分布，分别用 $\tilde{P}(X,Y)$ 和 $\tilde{P}(X)$ 表示
$$\tilde{P}(X=x,Y=y)=\frac{v(X=x,Y=y)}{N} \\
\tilde{P}(X=x)=\frac{v(X=x)}{N}$$
其中，$v(\cdot)$ 表示频数，$N$ 是训练样本容量。

用特征函数（feature function）$f(x,y)$ 描述输入 $x$ 和输出 $y$ 之间的某一个事实。其定义是
$$f(x,y)=\begin{cases}
1, & x\ 与\ y\ 满足某一事实 \\
0, & 否则
\end{cases}$$
它是一个二值函数（一般的，特征函数可以是任意的实值函数）。

特征函数 $f(x,y)$ 关于经验分布 $\tilde{P}(X,Y)$ 的期望值，用 $\text{E}_{\tilde{P}}(f)$ 表示
$$\text{E}_{\tilde{P}}(f)=\sum_{x,y}\tilde{P}(x,y)f(x,y)$$

特征函数 $f(x,y)$ 关于模型 $P(Y|X)$ 与经验分布 $\tilde{P}(X)$ 的期望值，用 $\text{E}_P(f)$ 表示
$$\text{E}_P(f)=\sum_{x,y}\tilde{P}(x)P(y|x)f(x,y)$$

如果模型能够获取训练数据中的信息，那么就可以假设这两个期望值相等，即
$$\text{E}_P(f)=\text{E}_{\tilde{P}}(f)$$
即
$$\sum_{x,y}\tilde{P}(x)P(y|x)f(x,y)=\sum_{x,y}\tilde{P}(x,y)f(x,y)$$
我们将上式作为模型学习的约束条件。假如有 $n$ 个特征函数 $f_i(x,y)$，$i=1,2,\cdots,n$，那么就有 $n$ 个约束条件。

**
定义 6.3（最大熵模型）假设满足所有约束条件的模型集合为
$${\cal C}\equiv\left\{P\in{\cal P}|\text{E}_P(f_i)=\text{E}_{\tilde{P}}(f_i),i=1,2,\cdots,n\right\}$$
定义在条件概率分布 $P(Y|X)$ 上的条件熵为
$$H(P)=-\sum_{x,y}\tilde{P}(x)P(y|x)\log P(y|x)$$
则模型集合 ${\cal C}$ 中条件熵 $H(P)$ 最大的模型称为最大熵模型。式中的对数为自然对数。
**

### 6.2.3 最大熵模型的学习

最大熵模型的学习过程就是求解最大熵模型的过程。最大熵模型的学习可以形式化为约束最优化问题。

对于给定的训练数据集
$$T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$$
以及特征函数
$$f_i(x,y),\ i=1,2,\cdots,n$$
最大熵模型的学习等价于约束优化问题：
$$\max_{P\in{\cal C}}\ \ \ \ \ H(P)=-\sum_{x,y}\tilde{P}(x)P(y|x)\log P(y|x) \\
\text{s.t.}\ \ \ \ \ \text{E}_P(f_i)=\text{E}_{\tilde{P}}(f_i),\ i=1,2,\cdots,n \\
\sum_{y}P(y|x)=1$$

按照最优化问题的习惯，将求最大值问题改写为等价的求最小值问题：
$$\min_{P\in{\cal C}}\ \ \ \ \ -H(P)=\sum_{x,y}\tilde{P}(x)P(y|x)\log P(y|x) \\
\text{s.t.}\ \ \ \ \ \text{E}_P(f_i)-\text{E}_{\tilde{P}}(f_i)=0,\ i=1,2,\cdots,n \\
\sum_{y}P(y|x)=1$$

这里，将约束最优化问题的原始问题转换为无约束最优化的对偶问题，通过求解对偶问题求解原始问题。

首先，引进拉格朗日乘子 $w_0,w_1,w_2,\cdots,w_n$，定义拉格朗日函数
$$\begin{eqnarray}
L(P,w) &\equiv& -H(P)+w_0\left(1-\sum_yP(y|x)\right)+\sum_{i=1}^nw_i\left(\text{E}_P(f_i)-\text{E}_{\tilde{P}}(f_i)\right) \\
&=& \sum_{x,y}\tilde{P}(x)P(y|x)\log P(y|x)+w_0\left(1-\sum_yP(y|x)\right) \\
&+& \sum_{i=1}^nw_i\left(\sum_{x,y}\tilde{P}(x,y)f_i(x,y)-\sum_{x,y}\tilde{P}(x)P(y|x)f_i(x,y)\right)
\end{eqnarray}$$
最优化的原始问题是
$$\min_{P\in{\cal C}}\max_wL(P,w)$$
对偶问题是
$$\max_w\min_{P\in{\cal C}}L(P,w)$$
由于拉格朗日函数 $L(P,w)$ 是 $P$ 的凸函数，原始问题的解和对偶问题的解是等价的。

首先，求解对偶问题内部的极小化问题，记作
$$\Psi(w)=\min_{P\in{\cal C}}L(P,w)=L(P_w,w)$$
$\Psi(w)$ 称为对偶函数，同时，将其解记作
$$P_w=\arg\min_{P\in{\cal C}}L(P,w)=P_w(y|x)$$
通过令偏导数等于 0
$$\begin{eqnarray}
\frac{\partial L(P,w)}{\partial P(y|x)} &=& \sum_{x,y}\tilde{P}(x)\left(\log P(y|x)+1\right)-\sum_yw_0-\sum_{x,y}\left(\tilde{P}(x)\sum_{i=1}^nw_if_i(x,y)\right) \\
&=& \sum_{x,y}\tilde{P}(x)\left(\log P(y|x)+1-w_0-\sum_{i=1}^nw_if_i(x,y)\right)
\end{eqnarray}$$
在 $\tilde{P}(x)>0$ 的情况下，解得
$$\begin{eqnarray}
P(y|x) &=& \exp\left(\sum_{i=1}^nw_if_i(x,y)+w_0-1\right) \\
&=& \frac{\exp\left(\sum_{i=1}^nw_if_i(x,y)\right)}{\exp(1-w_0)}
\end{eqnarray}$$
由于 $\sum_yP(y|x)=1$，得
$$P_w(y|x)=\frac{1}{Z_w(x)}\exp\left(\sum_{i=1}^nw_if_i(x,y)\right)$$
其中
$$Z_w(x)=\sum_y\exp\left(\sum_{i=1}^nw_if_i(x,y)\right)$$
称为规范化因子；$f_i(x,y)$ 是特征函数，$w_i$ 是特征函数的权值。由以上两式表示的 $P_w(y|x)$ 就是最大熵模型，$w$ 是最大熵模型中的参数向量。

之后，求解对偶问题外部的极大化问题
$$\max_w\Psi(w)$$
将其解记为 $w^\star$，即
$$w^\star=\arg\max_w\Psi(w)$$
故最终的最大熵模型是
$$P^\star=P_{w^\star}=P_{w^\star}(y|x)$$

### 6.2.4 极大似然估计

从最大熵模型学习中可以看出，最大熵模型是由下面两个式子表示的条件概率分布：
$$P_w(y|x)=\frac{1}{Z_w(x)}\exp\left(\sum_{i=1}^nw_if_i(x,y)\right) \\
Z_w(x)=\sum_y\exp\left(\sum_{i=1}^nw_if_i(x,y)\right)$$
下面证明，对偶函数的极大化等价于最大熵模型的极大似然估计。

最大似然函数的一般形式是样本集中各个样本的联合概率：
$$L(x_1,x_2,\cdots,x_N;\theta)=\prod_{i=1}^{N} p(x_i;\theta)$$
其中利用了数据是独立同分布产生的假设。$x_1,x_2,\cdots,x_N$ 是样本具体观测值。随机变量 $X$ 是离散的，所以它的取值范围是一个集合，假设样本集的大小为 $N$，$X$ 的取值有 $K$ 个，分别是 $c_1,c_2,\cdots,c_K$。用 $v(X=c_i)$表示在观测值中样本 $c_i$ 出现的频数。则：
$$L(x_1,x_2,\cdots,x_N;\theta)=\prod_{i=1}^{k}p(v_i;\theta)^{v(X=c_i)}$$
对等式两边同时开 $N$ 次方，可得：
$$L(x_1,x_2,\cdots,x_N;\theta)^{\frac{1}{N}}=\prod_{i=1}^{k}p(v_i;\theta)^{\frac{v(X=c_i)}{N}}$$
因为经验概率 $\tilde{p}(x)=\frac{v(X=c_i)}{N}$，所以：
$$L(x_1,x_2,\cdots,x_N;\theta)^{\frac{1}{N}}=\prod_{x}p(x;\theta)^{\tilde{p}(x)}$$
很明显对 $L(x_1,x_2,\cdots,x_N;\theta)$ 求最大值和对 $L(x_1,x_2,\cdots,x_N;\theta)^{\frac{1}{N}}$求最大值的优化的结果是一样的。整理上式所以最终的最大似然函数可以表示为：
$$L(x;\theta)=\prod_{x} p(x;\theta)^{\tilde{p}(x)}$$

已知训练数据的经验概率分布 $\tilde{P}(X,Y)$，条件概率分布 $P(Y|X)$ 的对数似然函数表示为：
$$L_{\tilde{P}}(P_w)=\log\prod_{x,y}P(y|x)^{\tilde{P}(x,y)}=\sum_{x,y}\tilde{P}(x,y)\log P(y|x)$$
当条件概率分布 $P(y|x)$ 是最大熵模型时，对数似然函数为
$$\begin{eqnarray}
L_{\tilde{P}}(P_w) &=& \sum_{x,y}\tilde{P}(x,y)\log P(y|x) \\
&=& \sum_{x,y}\tilde{P}(x,y)\sum_{i=1}^nw_if_i(x,y)-\sum_{x,y}\tilde{P}(x,y)\log Z_w(x) \\
&=& \sum_{x,y}\tilde{P}(x,y)\sum_{i=1}^nw_if_i(x,y)-\sum_x\tilde{P}(x)\log Z_w(x)
\end{eqnarray}$$
再看对偶函数 $\Psi(w)$:
$$\begin{eqnarray}
\Psi(w) &=& \sum_{x,y}\tilde{P}(x)P_w(y|x)\log P_w(y|x)+w_0\left(1-\sum_yP_w(y|x)\right) \\
&+& \sum_{i=1}^nw_i\left(\sum_{x,y}\tilde{P}(x,y)f_i(x,y)-\sum_{x,y}\tilde{P}(x)P_w(y|x)f_i(x,y)\right) \\
&=& \sum_{x,y}\tilde{P}(x,y)\sum_{i=1}^nw_if_i(x,y) \\
&+& \sum_{x,y}\tilde{P}(x)P_w(y|x)\left(\log P_w(y|x)-\sum_{i=1}^nw_if_i(x,y)\right) \\
&=& \sum_{x,y}\tilde{P}(x,y)\sum_{i=1}^nw_if_i(x,y)-\sum_{x,y}\tilde{P}(x)P_w(y|x)\log Z_w(x) \\
&=& \sum_{x,y}\tilde{P}(x,y)\sum_{i=1}^nw_if_i(x,y)-\sum_{x}\tilde{P}(x)\log Z_w(x)
\end{eqnarray}$$
其中利用了 $\sum_yP(y|x)=1$。

比较易得 $\Psi(w)=L_{\tilde{P}}(P_w)$，于是证明了最大熵学习中的对偶函数极大化等价于最大熵模型的极大似然估计这一事实。这样，最大熵模型的学习问题就转换为具体求解对数似然函数极大化或对偶函数极大化的问题。

可以将最大熵模型写成更一般的形式：
$$P_w(y|x)=\frac{1}{Z_w(x)}\exp\left(\sum_{i=1}^nw_if_i(x,y)\right) \\
Z_w(x)=\sum_y\exp\left(\sum_{i=1}^nw_if_i(x,y)\right)$$
这里，$x\in\mathbb{R}^n$ 为输入，$y\in\{1,2,\cdots,K\}$ 为输出，$w\in\mathbb{R}^n$ 为权值向量，$f_i(x,y)$，$i=1,2,\cdots,n$ 为任意实值特征函数。

最大熵模型与逻辑回归模型有着类似的形式，它们又称为对数线性模型（log linear model）。模型学习就是在给定的训练数据条件下对模型进行极大似然估计或正则化的极大似然估计。

## 6.3 模型学习的最优化算法

### 6.3.1 改进的迭代尺度法

改进的迭代尺度法（improved iterative scaling，IIS）是一种最大熵模型学习的最优化算法。

已知最大熵模型：
$$P_w(y|x)=\frac{1}{Z_w(x)}\exp\left(\sum_{i=1}^nw_if_i(x,y)\right) \\
Z_w(x)=\sum_y\exp\left(\sum_{i=1}^nw_if_i(x,y)\right)$$

对数似然函数为：
$$L(w)=\sum_{x,y}\tilde{P}(x,y)\sum_{i=1}^nw_if_i(x,y)-\sum_x\tilde{P}(x)\log Z_w(x)
$$
目标是通过极大似然估计学习模型参数，即求对数似然函数的极大值 $w^\star$。

首先建立对数似然函数改变量的下界
$$\begin{eqnarray}
L(w+\delta)-L(w) &=& \sum_{x,y}\tilde{P}(x,y)\log P_{w+\delta}(y|x)-\sum_{x,y}\tilde{P}(x,y)\log P_{w}(y|x) \\
&=& \sum_{x,y}\tilde{P}(x,y)\sum_{i=1}^n\delta_if_i(x,y)-\sum_x\tilde{P}(x)\log \frac{Z_{w+\delta}(x)}{Z_w(x)}
\end{eqnarray}$$
利用不等式
$$-\log\alpha\geq1-\alpha,\alpha>0$$
得
$$\begin{eqnarray}
L(w+\delta)-L(w) &\geq& \sum_{x,y}\tilde{P}(x,y)\sum_{i=1}^n\delta_if_i(x,y)+1-\sum_x\tilde{P}(x)\frac{Z_{w+\delta}(x)}{Z_w(x)} \\
&=& \sum_{x,y}\tilde{P}(x,y)\sum_{i=1}^n\delta_if_i(x,y)+1 \\
&-& \sum_x\tilde{P}(x)\sum_yP_w(y|x)\exp\left(\sum_{i=1}^n\delta_if_i(x,y)\right)
\end{eqnarray}$$
将右端记为
$$A(\delta|w)=\sum_{x,y}\tilde{P}(x,y)\sum_{i=1}^n\delta_if_i(x,y)+1-\sum_x\tilde{P}(x)\sum_yP_w(y|x)\exp\left(\sum_{i=1}^n\delta_if_i(x,y)\right)$$
于是有
$$L(w+\delta)-L(w)\geq A(\delta|w)$$

如果能找到适当的 $\delta$ 使下界 $A(\delta|w)$ 提高，那么对数似然函数也会提高，然而 $A(\delta|w)$ 中的 $\delta$ 是个向量，不易同时优化，IIS 试图一次只优化其中一个变量 $\delta_i$，而固定其他变量 $\delta_j$，$i\neq j$。

为达到这一目的，IIS 进一步降低下界 $A(\delta|w)$。引入一个量
$$f^\sharp(x,y)=\sum_if_i(x,y)$$
因为 $f_i$ 是二值函数，故 $f^\sharp(x,y)$ 表示所有特征在 $(x,y)$ 出现的次数，这样 $A(\delta|w)$ 可改写为
$$\begin{eqnarray}
A(\delta|w) &=& \sum_{x,y}\tilde{P}(x,y)\sum_{i=1}^n\delta_if_i(x,y)+1 \\
&-& \sum_x\tilde{P}(x)\sum_yP_w(y|x)\exp\left(f^\sharp(x,y)\sum_{i=1}^n\frac{\delta_if_i(x,y)}{f^\sharp(x,y)}\right)
\end{eqnarray}$$
利用指数函数的凸性以及对任意 $i$，有
$$\frac{f_i(x,y)}{f^\sharp(x,y)}\geq0\ 且\ \sum_{i=1}^n\frac{f_i(x,y)}{f^\sharp(x,y)}=1$$
根据琴生不等式（Jensen's inequality），得到
$$\exp\left(\sum_{i=1}^n\frac{f_i(x,y)}{f^\sharp(x,y)}\delta_if^\sharp(x,y)\right)\leq\sum_{i=1}^n\frac{f_i(x,y)}{f^\sharp(x,y)}\exp\left(\delta_if^\sharp(x,y)\right)$$
于是得到对数似然函数改变量的一个新的（相对不紧的）下界
$$\begin{eqnarray}
B(\delta|w) &=& \sum_{x,y}\tilde{P}(x,y)\sum_{i=1}^n\delta_if_i(x,y)+1 \\
&-& \sum_x\tilde{P}(x)\sum_yP_w(y|x)\sum_{i=1}^n\left(\frac{f_i(x,y)}{f^\sharp(x,y)}\right)\exp\left(\delta_if^\sharp(x,y)\right)
\end{eqnarray}$$
求 $B(\delta|w)$ 对 $\delta_i$ 的偏导数
$$\begin{eqnarray}
\frac{\partial B(\delta|w)}{\partial \delta_i} &=& \sum_{x,y}\tilde{P}(x,y)f_i(x,y) \\ &-& \sum_x\tilde{P}(x)\sum_yP_w(y|x)f_i(x,y)\exp\left(\delta_if^\sharp(x,y)\right)
\end{eqnarray}$$
上式只含有 $\delta_i$，令偏导数等于 0 得到
$$\sum_x\tilde{P}(x)\sum_yP_w(y|x)f_i(x,y)\exp\left(\delta_if^\sharp(x,y)\right)=\text{E}_{\tilde{P}}(f_i)$$
于是，依次对 $\delta_i$ 求解上述方程就可以求出 $\delta$。

**
算法 6.1（改进的迭代尺度算法 IIS）  
输入：特征函数 $f_1,f_2,\cdots,f_n$；经验分布函数 $\tilde{P}(X,Y)$，模型 $P_w(y|x)$  
输出：最优参数值 $w_i^\star$；最优模型 $P_{w^\star}$  
(1) 对所有 $i\in\{1,2,\cdots,n\}$，取初值 $w_i=0$  
(2) 对每一 $i\in\{1,2,\cdots,n\}$：  
(2.a) 令 $\delta_i$ 是方程
$$\sum_x\tilde{P}(x)\sum_yP_w(y|x)f_i(x,y)\exp\left(\delta_if^\sharp(x,y)\right)=\text{E}_{\tilde{P}}(f_i)$$
的解，这里
$$f^\sharp(x,y)=\sum_{i=1}^nf_i(x,y)$$  
(2.b) 更新：$w_i\leftarrow w_i+\delta_i$  
(3) 如果不是所有 $w_i$ 都收敛，重复步骤 (2)
**

这一算法关键步骤是 (2.a)，如果 $f^\sharp(x,y)$ 是常数，即对任意的 $x$，$y$，有 $f^\sharp(x,y)=M$，那么 $\delta_i$ 可以显示的表示为
$$\delta_i=\frac{1}{M}\log\frac{\text{E}_\tilde{P}(f_i)}{\text{E}_P(f_i)}$$
如果 $f^\sharp(x,y)$ 不是常数，就必须数值计算求 $\delta_i$，简单有效的方法是牛顿法，由于方程有单根，因此牛顿法恒收敛，且收敛速度很快。

### 6.3.2 拟牛顿法

最大熵模型学习还可以应用牛顿法或拟牛顿法。

对于最大熵模型
$$P_w(y|x)=\frac{\exp\left(\sum_{i=1}^nw_if_i(x,y)\right)}{\sum_y\exp\left(\sum_{i=1}^nw_if_i(x,y)\right)}$$

目标函数为：
$$\min_{w\in\mathbb{R}^n}\ \ f(w)=\sum_x\tilde{P}(x)\log\sum_y\exp\left(\sum_{i=1}^nw_if_i(x,y)\right)-\sum_{x,y}\tilde{P}(x,y)\sum_{i=1}^nw_if_i(x,y)
$$
梯度：
$$g(w)=\left(\frac{\partial f(w)}{\partial w_1},\frac{\partial f(w)}{\partial w_2},\cdots,\frac{\partial f(w)}{\partial w_n}\right)^\text{T}$$
其中
$$\frac{\partial f(w)}{\partial w_i}=\sum_{x,y}\tilde{P}(x)P_w(y|x)f_i(x,y)-\text{E}_{\tilde{P}}(f_i),i=1,2,\cdots,n$$

**
算法 6.2（最大熵模型学习的 BFGS）算法  
输入：特征函数 $f_1,f_2,\cdots,f_n$；经验分布 $\tilde{P}(x,y)$，目标函数 $f(w)$，梯度 $g(w)=\nabla f(w)$，精度要求 $\epsilon$  
输出：最优化参数值 $w^\star$；最优模型 $P_{w^\star}(y|x)$  
(1) 选定初始点 $w^{(0)}$，取 ${\bf B_0}$ 为正定对称矩阵，置 $k=0$  
(2) 计算 $g_k=g(w^{(k)})$，若 $\|g_k\|<\epsilon$，则停止计算，得 $w^\star=w^{(k)}$；否则，转到 (3)  
(3) 由 ${\bf B_k}p_k=-g_k$ 求出 $p_k$  
(4) 一维搜索：求 $\lambda_k$ 使得
$$f(w^{(k)}+\lambda_kp_k)=\min_{\lambda\geq0}f(w^{(k)}+\lambda p_k)$$
(5) 置 $w^{(k+1)}=w^{(k)}+\lambda_k p_k$  
(6) 计算 $g_{k+1}=g(w^{(k+1)})$，若 $\|g_{k+1}\|<\epsilon$，则停止计算，得 $w^\star=w^{(k+1)}$；否则，按照下式求出 ${\bf B_{k+1}}$
$${\bf B_{k+1}}={\bf B_k}+\frac{y_ky_k^\text{T}}{y_k^\text{T}\delta_k}-\frac{{\bf B_k}\delta_k\delta_k^\text{T}{\bf B_k}}{\delta_k^\text{T}{\bf B_k}\delta_k}$$
其中，
$$y_k=g_{k+1}-g_k,\delta_k=w^{(k+1)}-w^{(k)}$$
(7) 置 $k=k+1$，转到 (3)
**
