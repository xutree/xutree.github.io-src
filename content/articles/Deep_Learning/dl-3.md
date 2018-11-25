Title: 深度学习 第三章 概率与信息论
Category: 读书笔记
Date: 2018-11-21 20:09:05
Modified: 2018-11-22 11:36:17
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
$$\mathbb{E}_{\text{x}\sim P}\left[\text{x}\right]=\sum_xxP(x)\ 或\ \mathbb{E}_{\text{x}\sim p}\left[\text{x}\right]=\int_xxP(x)dx$$
约定 $\mathbb{E}[\cdot]$ 表示对方括号内的所有随机变量的值求平均。如随机变量明确，则可以省略下标。

性质：
$$\mathbb{E}[a\text{x}+b\text{y}]=a\mathbb{E}[\text{x}]+b\mathbb{E}[\text{y}]$$

**方差**（variance）
$$\text{Var}\left(\text{x}\right)=\mathbb{E}\left[\left(\text{x}-\mathbb{E}[\text{x}]\right)^2\right]=\mathbb{E}\left[\text{x}^2\right]-\left(\mathbb{E}[\text{x}]\right)^2$$
方差的平方根称为**标准差**（standard deviation）。

性质：
$$\text{Var}(\text{x})\geq0 \\
\text{Var}(\text{x}+\text{const})=\text{Var}(\text{x}) \\
\text{Var}(a\text{x})=a^2\text{Var}(\text{x}) \\
\text{Var}(a\text{x}+b\text{y})=a^2\text{Var}(\text{x})+b^2\text{Var}(\text{y})+2ab\ \text{Cov}(\text{x},\text{y}) \\
\text{Var}(\text{x}-\text{y})=\text{Var}(\text{x})+\text{Var}(\text{y})-2\ \text{Cov}(\text{x},\text{y}) \\
\text{Var}\left(\sum_{i=1}^N\text{x}_i\right)=\sum_{i,j=1}^N\text{Cov}(\text{x}_i,\text{x}_j)=\sum_{i=1}^N\text{Var}(\text{x}_i)+\sum_{i\neq j}\text{Cov}(\text{x}_i,\text{x}_j)$$
最后一式为随机向量的方差。

**协方差**（covariance）在概率论和统计学中用于衡量两个变量的总体误差。而方差是协方差的一种特殊情况，即当两个变量是相同的情况。期望值分别为 $\mathbb{E}(\text{x})=\mu$ 和 $\mathbb{E}(y)=\nu$ 的两个具有有限二阶矩的实数随机变量 x 与 y 之间的协方差定义为：
$$\text{Cov}(\text{x},\text{y})=\mathbb{E}\left[(\text{x}-\mu)(\text{y}-\nu)\right]=\mathbb{E}[\text{x}\cdot y]-\mu\nu$$
协方差表示的是两个变量的总体的误差，这与只表示一个变量误差的方差不同。 如果两个变量的变化趋势一致，也就是说如果其中一个大于自身的期望值，另外一个也大于自身的期望值，那么两个变量之间的协方差就是正值。 如果两个变量的变化趋势相反，即其中一个大于自身的期望值，另外一个却小于自身的期望值，那么两个变量之间的协方差就是负值。

如果 x 与 y 是统计独立的，那么二者之间的协方差就是 0。

取决于协方差的**相关性**（correlation）定义为
$$\eta=\frac{\text{cov}(\text{x},\text{y})}{\sqrt{\text{Var}(\text{x})\cdot\text{Var}(\text{y})}}$$
更准确地说是线性相关性，是一个衡量线性独立的无量纲数，其取值在 $[－1,1]$ 之间。相关性 $\eta=1$ 时称为“完全线性相关”（相关性 $\eta=-1$ 时称为“完全线性负相关”）。

相关性为 0（因而协方差也为 0）的两个随机变量又被称为是不相关的，或者更准确地说叫作“线性无关”、“线性不相关”，这仅仅表明 x 与 y 两随机变量之间没有线性相关性，并非表示它们之间一定没有任何内在的（非线性）函数关系。

性质：
$$\text{Cov}(\text{x},\text{x})=\text{Var}(\text{x}) \\
\text{Cov}(\text{x},\text{y})=\text{Cov}(\text{y},\text{x}) \\
\text{Cov}(a\text{x},b\text{y})=ab\ \text{Cov}(\text{x},\text{y}) \\
\text{Cov}\left(\sum_{i=1}^n\text{x}_i\sum_{j=1}^m\text{y}_j\right)=\sum_{i=1}^n\sum_{j=1}^m\text{Cov}(\text{x}_i,\text{y}_j)$$

**协方差矩阵**（covariance matrix）对随机向量 ${\bf x}\in\mathbb{R}^n$，协方差矩阵为
$$\text{Cov}({\bf x})_{i,j}=\text{Cov}(\text{x}_i,\text{y}_j)$$
其对角元是方差。

## 3.7 常用概率分布

### 3.7.1 伯努利分布

**伯努利分布**（Bernoulli distribution），又称两点分布或 0-1 分布。
$$P(\text{x}=1)=\phi \\
P(\text{x}=0)=1-\phi \\
P(\text{x}=x)=\phi^x(1-\phi)^{1-x} \\
\text{E}_{\text{x}}[\text{x}]=\phi \\
\text{Var}_{\text{x}}(\text{x})=\phi(1-\phi)$$

### 3.7.2 高斯分布

实数上最常用的分布就是**正态分布**（normal distribution），也称高斯分布（Gaussian distribution）。
$${\cal N}(x;\mu,\sigma^2)=\sqrt{\frac{1}{2\pi\sigma^2}}\exp\left(-\frac{1}{2\sigma^2}(x-\mu)^2\right) \\
\mathbb{E}_{\text{x}\sim{\cal N}}[\text{x}]=\mu \\
\text{Var}_{\text{x}\sim{\cal N}}[\text{x}]=\sigma^2$$
函数拐点在 $x=\mu\pm\sigma$ 处。

当我们由于缺乏关于某个实数上分布的先验知识而不知道该选择怎样的形式时，正态分布是默认较好的选择，有两个原因：

- 我们想要建模的很多分布的真实情况是比较接近正态分布的。中心极限定理（central limit theorem）说明很多独立随机变量的和近似服从正态分布
- 在具有相同方差的所有可能的概率分布中，正态分布在实数上具有最大的不确定性。因此，我们可以认为正态分布是对模型加入的先验知识量最少的分布

正态分布可以推广到 $\mathbb{R}^n$ 空间，这种情况下称为**多维正态分布**（multivariate normal distribution）。它的参数是一个正定对称矩阵 $\boldsymbol \Sigma$（协方差矩阵）：
$${\cal N}(\boldsymbol x;\boldsymbol\mu,\boldsymbol\Sigma)=\sqrt{\frac{1}{(2\pi)^n\text{det}(\boldsymbol \Sigma)}}\exp\left(-\frac{1}{2}(\boldsymbol x-\boldsymbol \mu)^\text{T}\boldsymbol\Sigma^{-1}(\boldsymbol x-\boldsymbol \mu)\right)$$

### 3.7.3 指数分布和 Laplace 分布

**指数分布**（exponential distribution）在 $x=0$ 处取得边界点（sharp point）的分布。
$$p(x;\lambda)=\lambda\boldsymbol 1_{x\geq0}\exp(-\lambda x)$$
指示函数（indicator function）$\boldsymbol 1_{x\geq0}$ 来使得当 $x$ 取负值时的概率为零。

**拉普拉斯分布**（Laplace distribution）可以在任意一点 $\mu$ 处设置概率质量的峰值。
$$\text{Laplace}(x;\mu,\gamma)=\frac{1}{2\gamma}\exp\left(-\frac{|x-\mu|}{\gamma}\right)$$

### 3.7.4 Dirac 分布和经验分布

Dirac delta 函数可以用于定义狄拉克分布：
$$p(x)=\delta(x-\mu)$$

Dirac 分布常作为**经验分布**（empirical distribution）的一个组成部分出现：
$$\hat{p}(\boldsymbol x)=\frac{1}{m}\sum_{i=1}^m\delta(\boldsymbol x-\boldsymbol x^{(i)})$$
经验分布将概率密度 $\frac{1}{m}$ 赋给 $m$ 个点 $\boldsymbol x^{(1)},\cdots,\boldsymbol x^{(m)}$ 中的每一个，这些点是给定的数据集或者采样的集合。

只有在定义连续型随机变量的经验分布时，狄拉克 delta 函数才是必要的。对于离散型随机变量，对于每一个可能的输入，其概率可以简单的设为训练集上那个输入值的**经验频率**（empirical frequency）。

当我们在训练集上训练模型时，可以认为从这个训练集上得到的经验分布指明了采样来源的分布。关于经验分布另外一个重要的观点是，它是训练数据的似然最大的那个概率密度函数。

### 3.7.5 分布的混合

**混合分布**（mixture distribution）是由一些组件（component）分布构成：
$$P(\text{x})=\sum_iP(\text{c}=i)P(\text{x}|\text{c}=i)$$
这里 $P(\text{c})$ 是各个组件被选中的概率，决定每一次试验样本从哪个组件分布生成。

## 3.8 常用函数的性质

### 3.8.1 逻辑函数

**逻辑函数**（logistic function），也被称为 **S 函数**（sigmoid function），通常用来产生伯努利分布中的参数 $\phi$，因为它的范围是 $(0,1)$。sigmoid 函数在变量取绝对值非常大的时候会出现饱和（saturate）现象，意味着对输入的微小变化变得不敏感。
$$\sigma(x)=\frac{1}{1+\text{e}^{-x}}$$
一些性质：
$$\sigma(x)=\frac{\text{e}^{x}}{\text{e}^{x}+1} \\
\frac{d}{dx}\sigma(x)=\sigma(x)\sigma(-x) \\
1-\sigma(x)=\sigma(-x) \\
\forall x\in(0,1),\ \sigma^{-1}(x)=\ln\left(\frac{x}{1-x}\right)$$

### 3.8.2 softplus 函数

$$\zeta(x)=\ln(1+\text{e}^{x})$$

softplus 函数可以用来产生正态分布的 $\beta$ 和 $\sigma$ 参数，因为它的范围是 $(0,\infty)$。softplus 函数名来源于它是另外一个函数的平滑（或“软化”）形式，这个函数是：
$$x^+=\max(0,x)$$

一些性质：
$$\zeta(x)=-\ln\sigma(-x) \\
\frac{d}{dx}\zeta(x)=\sigma(x) \\
\forall x\geq0,\ \zeta^{-1}(x)=\ln\left(\text{e}^x-1\right) \\
\zeta(x)=\int_{-\infty}^x\sigma(y)dy \\
\zeta(x)-\zeta(-x)=x$$

**正部函数**（positive part function）：$x^+=\max(0,x)$

**负部函数**（negative part function）：$x^-=\max(0,-x)$

$$x^+-x^-=x$$

## 3.9 贝叶斯规则

**贝叶斯规则**（Bayes' rule）：
$$P(\text{x}|\text{y})=\frac{P(\text{x})P(\text{y}|\text{x})}{P(\text{y})}=\frac{P(\text{x})P(\text{y}|\text{x})}{\sum_xP(\text{y}|x)P(x)}$$

## 3.10 连续型变量的技术细节

假设有两个随机变量 $\bf x$ 和 $\bf y$ 满足 $\boldsymbol y=g(\boldsymbol x)$，其中 $g$ 是可逆、连续可微的函数。

我们需要保持下面的性质：
$$|p_y(g(x))dy|=|p_x(x)dx|$$
即
$$p_y(y)=p_x(g^{-1}(y))\left\lvert\frac{\partial x}{\partial y}\right\rvert$$
即
$$p_x(x)=p_y(g(x))\left\lvert\frac{\partial g(x)}{\partial x}\right\rvert$$
在高维空间中，微分运算扩展为 **Jacobian 矩阵**的行列式，矩阵的每个元素为 $J_{i,j}=\frac{\partial x_i}{\partial y_j}$。因此，对实值向量 $\boldsymbol x$ 和 $\boldsymbol y$：
$$p_x(\boldsymbol x)=p_y(g(\boldsymbol x))\left\lvert\text{det}\left(\frac{\partial g(\boldsymbol x)}{\partial \boldsymbol x}\right)\right\rvert \\$$

## 3.11 信息论

### 3.11.1 自信息

一个事件 $\text{x}=x$ 的**自信息**（self-information）为
$$I(x)=-\log P(x)$$
当底数是 e 时，自信息的单位是**奈特**（nats）。当底数是 2 时，自信息的单位是**比特**（bit）或**香农**（shannons）。

### 3.11.2 香农熵

**香农熵**（Shannon entropy）对整个概率分布中的不确定性总量进行量化：
$$H(x)=\mathbb{E}_{\text{x}\sim P}[I(x)]=-\mathbb{E}_{\text{x}\sim P}[\log P(x)]$$
也记作 $H(P)$。当 x 是连续的，香农熵被称为**微分熵**（differential entropy）。

### 3.11.3 相对熵

如果对于同一个随机变量 x 有两个单独的概率分布 $P(\text{x})$ 和 $Q(\text{x})$，可以使用**相对熵**（relative entropy）来衡量两个分布的差异：
$$D_{KL}(P\|Q)=\mathbb{E}_{\text{x}\sim P}\left[\log\frac{P(x)}{Q(x)}\right]=\mathbb{E}_{\text{x}\sim P}[\log P(x)-\log Q(x)]$$
又称为 **KL 散度**（Kullback–Leibler divergence，简称KLD），**信息散度**（information divergence），**信息增益**（information gain）。

KL 散度是非负的。当且仅当分布相同 KL 散度为 0。

尽管从直觉上 KL 散度是个度量或距离函数, 但是它实际上并不是一个真正的度量或距离。因为 KL 散度不具有对称性。

> 按照惯例，在信息论中，$\lim_{x\to0}x\ln x=0$
