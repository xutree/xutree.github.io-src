Title: 深度学习 第三章 概率与信息论
Category: 读书笔记
Date: 2018-11-21 20:09:05
Modified: 2018-11-21 20:09:05
Tags: 机器学习, 深度学习

## 3.1 随机变量

**随机变量**（random variable）是可以随机的取不同值的变量。通常用无格式字体（plain typeface）中的小写字母来表示随机变量本身，而用手写体中的小写字母来表示随机变量能够取到的值。例如，$x_1$ 和 $x_2$ 都是随机变量 x 的可能取值。

## 3.2 概率分布

**概率分布**（probability distribution）用来描述随机变量每一个可能取到的状态的可能性的大小。

**概率质量函数**（probability mass function，PMF）离散型变量的概率分布。

**概率密度函数**（probability density function，PDF）连续型变量的概率分布。

## 3.3 边缘概率

**边缘概率分布**（marginal probability distribution）是一种定义在子集上的概率分布。
$$p(x)=\int p(x,y)dy$$

## 3.4 条件概率

**条件概率**（conditional probability）就是事件在另外一个事件已经发生条件下的发生概率。
$$P(\text{y}=y|\text{x}=x)=\frac{P(\text{y}=y,\text{x}=x)}{P(\text{x}=x)}$$

## 3.5 独立性和条件独立性

**独立性**（independent）
$$\forall x\in\text{x},y\in\text{y} \\ p(\text{x}=x,\text{y}=y)=p(\text{x}=x)p(\text{y}=y)$$
记为 x$\perp$y。

**条件独立**（conditionally independent）
$$\forall x\in\text{x},y\in\text{y},z\in\text{z} \\ p(\text{x}=x,\text{y}=y|\text{z}=z)=p(\text{x}=x|\text{z}=z)p(\text{y}=y|\text{z}=z)$$
记为 x$\perp$y $\mid$ z。

## 3.6 期望、方差和协方差

**期望**（expectation）
$$\mathbb{E}_{\text{x}\sim P}\left[x\right]=\sum_xxP(x)\ 或\ \mathbb{E}_{\text{x}\sim p}\left[x\right]=\int_xxP(x)dx$$
约定 $\mathbb{E}[\cdot]$ 表示对方括号内的所有随机变量的值求平均。如随机变量明确，则可以省略下标。

性质：
$$\mathbb{E}[a{x}+b{y}]=a\mathbb{E}[{x}]+b\mathbb{E}[{y}]$$

**方差**（variance）
$$\text{Var}\left(x\right)=\mathbb{E}\left[\left(x-\mathbb{E}[x]\right)^2\right]=\mathbb{E}\left[x^2\right]-\left(\mathbb{E}[x]\right)^2$$
方差的平方根称为**标准差**（standard deviation）。

性质：
$$\text{Var}(x)\geq0 \\
\text{Var}(x+\text{const})=\text{Var}(x) \\
\text{Var}(ax)=a^2\text{Var}(x) \\
\text{Var}(ax+by)=a^2\text{Var}(x)+b^2\text{Var}(y)+2ab\ \text{Cov}(x,y) \\
\text{Var}(x-y)=\text{Var}(x)+\text{Var}(y)-2\ \text{Cov}(x,y) \\
\text{Var}\left(\sum_{i=1}^Nx_i\right)=\sum_{i,j=1}^N\text{Cov}(x_i,x_j)=\sum_{i=1}^N\text{Var}(x_i)+\sum_{i\neq j}\text{Cov}(x_i,x_j)$$
最后一式为随机向量的方差。

**协方差**（covariance）在概率论和统计学中用于衡量两个变量的总体误差。而方差是协方差的一种特殊情况，即当两个变量是相同的情况。期望值分别为 $\mathbb{E}(x)=\mu$ 和 $\mathbb{E}(y)=\nu$ 的两个具有有限二阶矩的实数随机变量 x 与 y 之间的协方差定义为：
$$\text{Cov}(x,y)=\mathbb{E}\left[(x-\mu)(y-\nu)\right]=\mathbb{E}[x\cdot y]-\mu\nu$$
协方差表示的是两个变量的总体的误差，这与只表示一个变量误差的方差不同。 如果两个变量的变化趋势一致，也就是说如果其中一个大于自身的期望值，另外一个也大于自身的期望值，那么两个变量之间的协方差就是正值。 如果两个变量的变化趋势相反，即其中一个大于自身的期望值，另外一个却小于自身的期望值，那么两个变量之间的协方差就是负值。

如果 x 与 y 是统计独立的，那么二者之间的协方差就是 0。

取决于协方差的**相关性**（correlation）定义为
$$\eta=\frac{\text{cov}(x,y)}{\sqrt{\text{Var}(x)\cdot\text{Var}(y)}}$$
更准确地说是线性相关性，是一个衡量线性独立的无量纲数，其取值在 $[－1,1]$ 之间。相关性 $\eta=1$ 时称为“完全线性相关”（相关性 $\eta=-1$ 时称为“完全线性负相关”）。

相关性为 0（因而协方差也为 0）的两个随机变量又被称为是不相关的，或者更准确地说叫作“线性无关”、“线性不相关”，这仅仅表明 x 与 y 两随机变量之间没有线性相关性，并非表示它们之间一定没有任何内在的（非线性）函数关系。

性质：
$$\text{Cov}(x,x)=\text{Var}(x) \\
\text{Cov}(x,y)=\text{Cov}(y,x) \\
\text{Cov}(ax,by)=ab\ \text{Cov}(x,y) \\
\text{Cov}\left(\sum_{i=1}^nx_i\sum_{j=1}^my_j\right)=\sum_{i=1}^n\sum_{j=1}^m\text{Cov}(x_i,y_j)$$

**协方差矩阵**（covariance matrix）对随机向量 $\boldsymbol x\in\mathbb{R}^n$，协方差矩阵为
$$\text{Cov}(\boldsymbol x)_{i,j}=\text{Cov}(x_i,y_j)$$
其对角元是方差。

## 3.7 常用概率分布
