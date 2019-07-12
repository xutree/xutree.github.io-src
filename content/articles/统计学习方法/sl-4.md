Title: 统计学习方法 第四章 朴素贝叶斯法
Category: 读书笔记
Date: 2019-01-29 16:42:01
Modified: 2019-01-29 16:42:01
Tags: 统计学习, 机器学习

[TOC]

朴素贝叶斯（naive Bayes）法是基于贝叶斯定理与特征条件独立假设的分类方法。朴素贝叶斯法实现简单，学习和预测效率都很高，是一种常用的方法。

## 4.1 朴素贝叶斯法的学习与分类

### 4.1.1 基本方法

设输入特征向量
$$x\in{\cal X}\subseteq\mathbb{R}^n$$
输出类标记
$$y\in{\cal Y}=\{c_1,c_2,\cdots,c_K\}$$
$X$ 是定义在输入空间 ${\cal X}$ 上的随机变量，$Y$ 是定义在输出空间 ${\cal Y}$ 上的随机变量，$P(X,Y)$ 是 $X$ 和 $Y$ 的联合概率分布。训练数据集
$$T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$$
由 $P(X,Y)$ 独立同分布产生。

朴素贝叶斯法通过训练数据集学习联合概率分布 $P(X,Y)$。具体地，学习以下先验概率分布及条件概率分布。先验概率分布
$$P(Y=c_k),k=1,2,\cdots,K$$
条件概率分布
$$P(X=x|Y=c_k)=P(X^{(1)}=x^{(1)},\cdots,X^{(n)}=x^{(n)}|Y=c_k),k=1,2,\cdots,K$$
于是学习到联合概率分布
$$P(X,Y)=P(X=x|Y=c_k)P(Y=c_k)$$

条件概率分布 $P(X=x|Y=c_k)$ 由指数级数量的参数，其估计实际是不可行的。事实上，假设 $x^{(i)}$ 可取值有 $S_j$ 个，$Y$ 可取值有 $K$ 个，那么参数个数为 $K\prod_{j=1}^nS_j$。

朴素贝叶斯法对条件概率分布作了条件独立性的假设。这是一个较强的假设，朴素贝叶斯法也由此得名。具体的，条件独立性假设是
$$\begin{eqnarray}
P(X=x|Y=c_k) &=& P(X^{(1)}=x^{(1)},\cdots,X^{(n)}=x^{(n)})|Y=c_k)\\
&=& \prod_{j=1}^nP(X^{(j)}=x^{(j)}|Y=c_k)
\end{eqnarray}$$

朴素贝叶斯法实际上学习到生成数据的机制，所以属于生成模型。条件独立假设等于是说分类的特征在类确定的条件下都是条件独立的。这一假设使朴素贝叶斯法变得简单，但有时会牺牲一定的分类准确率。

利用朴素贝叶斯法对给定输入 $x$分类是，将后验概率最大的类作为 $x$ 的类输出，后验概率根据贝叶斯定理计算
$$P(Y=c_k|X=x)=\frac{P(X=x|Y=c_k)P(Y=c_k)}{\sum_kP(X=x|Y=c_k)P(Y=c_k)}$$
利用条件独立假设
$$P(Y=c_k|X=x)=\frac{P(Y=c_k)\prod_jP(X^{(j)}=x^{(j)}|Y=c_k)}{\sum_kP(Y=c_k)\prod_jP(X^{(j)}=x^{(j)}|Y=c_k)}$$
这是朴素贝叶斯法的基本公式，于是朴素贝叶斯分类器可表示为
$$y=f(x)=\arg\max_{c_k}\frac{P(Y=c_k)\prod_jP(X^{(j)}=x^{(j)}|Y=c_k)}{\sum_kP(Y=c_k)\prod_jP(X^{(j)}=x^{(j)}|Y=c_k)}$$
注意到上式中分母对所有 $c_k$ 都为 $P(X=x)$，所以
$$y=f(x)=\arg\max_{c_k}P(Y=c_k)\prod_jP(X^{(j)}=x^{(j)}|Y=c_k)$$

### 4.1.2 后验概率最大化的含义

朴素贝叶斯法将实例分类到后验概率最大的类中，这等价于期望风险最小化。假设 0-1 损失函数
$$L(Y,f(X))=\begin{cases}1,&Y\neq f(X)\\0,& Y=f(X)\end{cases}$$
式中 $f(X)$ 是分类决策函数。这时期望风险函数为
$$\begin{eqnarray}
R_\text{exp}(f) &=& \text{E}[L(Y,f(X))]=\int_{{\cal X}\times{\cal Y}}L(y,f(x))P(x,y)dxdy\\
&=& \int_{\cal X}\int_{\cal Y}L(y,f(x))P(y|x)P(x)dxdy\\
&=& \int_{\cal X} \left[\int_{\cal Y}L(y,f(x))P(y|x)dy\right] P(x)dx
\end{eqnarray}$$
期望是对联合概率分布 $P(X,Y)$ 取的。由此取条件期望
$$R_\text{exp}(f)=\text{E}_X\sum_{k=1}^K[L(c_k,f(X))]P(c_k|X)$$
为了使期望风险最小化，只需对 $X=x$ 逐个极小化，得
$$\begin{eqnarray}f(x) &=& \arg\min_{y\in{\cal Y}}\sum_{k=1}^KL(c_k,y)P(c_k|X=x)\\&=&\arg\min_{y\in\cal Y}\sum_{k=1}^KP(y\neq c_k|X=x)\\&=&\arg\min_{y\in{\cal Y}}(1-P(y=c_k|X=x))\\&=&\arg\max_{y\in\cal Y}P(y=c_k|X=x)\end{eqnarray}$$
这样一来，根据期望风险最小化准则就得到了后验概率最大化准则
$$f(x)=\arg\max_{c_k}P(c_k|X=x)$$
即朴素贝叶斯法采用的原理。

## 4.2 朴素贝叶斯法的参数估计

### 4.2.1 极大似然估计

对于
$$y=f(x)=\arg\max_{c_k}P(Y=c_k)\prod_jP(X^{(j)}=x^{(j)}|Y=c_k)$$
朴素贝叶斯学习意味着估计 $P(Y=c_k)$ 和 $P(X^{(j)}=x^{(j)}|Y=c_k)$。可以应用极大似然估计法估计相应的概率。

先验概率 $P(Y=c_k)$ 的极大似然估计是
$$P(Y=c_k)=\frac{\sum_{i=1}^N\mathbb{I}(y_i=c_k)}{N},k=1,2,\cdots,K$$
设第 $j$ 个特征 $x^{(j)}$ 可能的取值集合为 $\{a_{j1},a_{j2},\cdots,a_{jS_j}\}$，条件概率的极大似然估计是
$$P(X^{(j)}=a_{jl}|Y=c_k)=\frac{\sum_{i=1}^N\mathbb{I}(x_i^{(j)}=a_{jl},y_i=c_k)}{\sum_{i=1}^N\mathbb{I}(y_i=c_k)}\\
j=1,2,\cdots,n; l=1,2,\cdots,S_j; k=1,2,\cdots,K$$

### 4.2.2 学习与分类算法

**
算法 4.1 朴素贝叶斯法（naive Bayes algorithm）  
输入：  
(a) 训练数据集
$$T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$$
其中
$$x_i=\left(x_i^{(1)},x_i^{(2)},\cdots,x_i^{(n)}\right)^\text{T}$$
$x_i^{(j)}$ 是第 $i$ 个样本的第 $j$ 个特征，且
$$x_i^{(j)}\in\{a_{j1},a_{j2},\cdots,a_{jS_j}\}$$
$$y_i\in\{c_1,c_2,\cdots,c_K\}$$
(b) 实例 $x$  
输出：实例 $x$ 的分类  
(1) 计算先验概率及条件概率
$$\begin{eqnarray}
P(Y=c_k) &=& \frac{\sum_{i=1}^N\mathbb{I}(y_i=c_k)}{N} \\
P(X^{(j)}=a_{jl}|Y=c_k) &=& \frac{\sum_{i=1}^N\mathbb{I}(x_i^{(j)}=a_{jl},y_i=c_k)}{\sum_{i=1}^N\mathbb{I}(y_i=c_k)}
\end{eqnarray}\\
j=1,2,\cdots,n; l=1,2,\cdots,S_j; k=1,2,\cdots,K$$
(2) 对于给定的实例 $x=\left(x^{(1)},x^{(2)},\cdots,x^{(n)}\right)^\text{T}$，计算
$$P(Y=c_k)\prod_{j=1}P(X^{(j)}=x^{(j)}|Y=c_k),k=1,2,\cdots,K$$
(3) 确定实例 $x$ 的类
$$y=f(x)=\arg\max_{c_k}P(Y=c_k)\prod_jP(X^{(j)}=x^{(j)}|Y=c_k)$$
**

### 4.2.3 贝叶斯估计

用极大似然估计可能会出现所要估计的概率值为 0 的情况。这时会影响到后验概率的计算结果，使分类产生偏差。解决这一问题的方法是采用贝叶斯估计。

先验概率的贝叶斯估计是
$$P_\lambda(Y=c_k)=\frac{\sum_{i=1}^N\mathbb{I}(y_i=c_k)+\lambda}{N+K\lambda},k=1,2,\cdots,K$$

条件概率的贝叶斯估计是
$$P_\lambda(X^{(j)}=a_{jl}|Y=c_k)=\frac{\sum_{i=1}^N\mathbb{I}(x_i^{(j)}=a_{jl},y_i=c_k)+\lambda}{\sum_{i=1}^N\mathbb{I}(y_i=c_k)+S_j\lambda}\\
j=1,2,\cdots,n; l=1,2,\cdots,S_j; k=1,2,\cdots,K$$
式中 $\lambda\geq0$，等价于在随机变量各个取值的频数上赋予一个非负数。当 $\lambda=0$ 时，就是极大似然估计。常取 $\lambda=1$，这是称为拉普拉斯平滑（Laplace smoothing）。

显然
$$\begin{eqnarray}
P_\lambda(X^{(j)}=a_{jl}|Y=c_k) &\geq& 0 \\
\sum_{l=1}^{S_j}P_\lambda(X^{(j)}=a_{jl}|Y=c_k) &=& 1
\end{eqnarray}$$
表明这的确是一种概率分布。
