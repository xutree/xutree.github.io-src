Title: 统计学习方法 第九章 EM 算法及其推广
Category: 读书笔记
Date: 2018-11-17 19:32:10
Modified: 2018-11-17 19:32:59
Tags: 统计学习, 机器学习

EM 算法是一种迭代算法，用于含有隐变量（hidden varibale）的概率模型参数的极大似然估计，或极大后验概率估计。EM 算法每次的迭代分两步：E 步，求期望（expectation）；M 步，求极大（maximization）。所以这一算法被称为期望极大算法（expectation maximization）。

## 9.1 EM 算法的引入

概率模型有时既含有观测变量（observable variable），又含有隐变量或潜在变量（latent variable）。如果概率模型的变量都是观测变量，那么给定数据，可以直接用极大似然估计法，或贝叶斯估计法估计模型参数。但是，当模型含有隐变量时，就不能简单的使用这些估计方法。EM 算法就是含有隐变量的概率模型参数的极大似然估计法，或极大后验概率估计法。

### 9.1.1 EM 算法

一般的，用 $Y$ 表示观测随机变量的数据，$Z$ 表示隐随机变量的数据。$Y$ 和 $Z$ 连在一起称为完全数据（complete-data），观测数据 $Y$ 又称为不完全数据（incomplete-data）。假设给定观测数据 $Y$，其概率分布是 $P(Y|\theta)$，其中 $\Theta$ 是需要估计的模型参数，那么不完全数据了 $Y$ 的似然函数是 $P(Y|\theta)$，对数似然函数是 $L(\theta)=\log P(Y|\theta)$；假设 $Y$ 和 $Z$ 的联合概率分布是 $P(Y,Z|\theta)$，那么完全数据的对数似然函数是 $\log P(Y,Z|\theta)$。

EM 算法通过迭代求 $L(\theta)=\log P(Y|\theta)$ 的极大似然估计。

**
算法 9.1（EM 算法）  
输入：观测变量数据 $Y$，隐变量数据 $Z$，联合分布 $P(Y,Z|\theta)$，条件分布 $P(Z|Y,\theta)$  
输出：模型参数 $\theta$  
(1) 选择参数的初值 $\theta^{(0)}$，开始迭代  
(2) E 步：记 $\theta^{(i)}$ 为第 $i$ 次迭代参数 $\theta$ 的估计值。在第 $i+1$ 次迭代的 E 步，计算
$$\begin{eqnarray}
Q\left(\theta,\theta^{(i)}\right) &=& \text{E}_Z\left[\log P(Y,Z|\theta)|Y,\theta^{(i)}\right] \\
&=& \sum_{Z}\log P(Y,Z|\theta)P(Z|Y,\theta^{(i)})
\end{eqnarray}$$
这里，$P(Z|Y,\theta^{(i)})$ 是在给定观测数据 $Y$ 和当前的参数估计 $\theta^{(i)}$ 下隐变量数据 $Z$ 的条件概率分布  
(3) M 步：求极大，更新 $\theta$  
$$\theta^{(i+1)}=\arg\max_{\theta}Q\left(\theta,\theta^{(i)}\right)$$
(4) 重复 (2)，(3)，直到收敛
**

$Q$ 函数是 EM 算法的核心。

**
定义 9.1（$Q$ 函数）玩去数据的对数似然函数 $\log P(Y,Z|\theta)$ 关于在给定观测数据 $Y$ 的当前参数 $\theta^{(i)}$ 下对未观测数据 $Z$ 的条件概率分布 $P\left(Z|Y,\theta^{(i)}\right)$ 的期望称为 $Q$ 函数，即
$$Q\left(\theta,\theta^{(i)}\right)=\text{E}_Z\left[\log P(Y,Z|\theta)|Y,\theta^{(i)}\right]$$
**

关于 EM 算法需要注意：参数的初值可以任意选择，但需注意 EM 算法对初值是敏感的；给出停止迭代的条件，一般是对较小的正数 $\epsilon_1$，$\epsilon_2$，若满足
$$\|\theta^{(i+1)}-\theta^{(i)}\|<\epsilon_1 $$
或
$$\left\|Q\left(\theta^{(i+1)},\theta^{(i)}\right)-Q\left(\theta^{(i)},\theta^{(i)}\right)\right\|<\epsilon_2$$
则迭代停止。

### 9.1.2 EM 算法的推导

首先
$$\begin{eqnarray}
L(\theta) &=& \log P(Y|\theta)=\log\sum_ZP(Y,Z|\theta) \\
&=& \log\left(\sum_ZP(Y|Z,\theta)P(Z|\theta)\right)
\end{eqnarray}$$
则
$$\begin{eqnarray}
L\left(\theta\right)-L(\theta^{(i)}) &=& \log\left(\sum_ZP(Y|Z,\theta)P(Z|\theta)\right)-\log P(Y|\theta^{(i)}) \\
&=& \log\left(\sum_ZP(Z|Y,\theta^{(i)})\frac{P(Y|Z,\theta)P(Z|\theta)}{P(Z|Y,\theta^{(i)})}\right)-\log P(Y|\theta^{(i)}) \\
&\geq& \sum_Z P(Z|Y,\theta^{(i)})\log\frac{P(Y|Z,\theta)P(Z|\theta)}{P(Z|Y,\theta^{(i)})}-\log P(Y|\theta^{(i)}) \\
&=& \sum_ZP(Z|Y,\theta^{(i)})\log\frac{P(Y|Z,\theta)P(Z|\theta)}{P(Z|Y,\theta^{(i)})P(Y|\theta^{(i)})}
\end{eqnarray}$$
令
$$B(\theta,\theta^{(i)})\equiv L(\theta^{(i)})+\sum_ZP(Z|Y,\theta^{(i)})\log\frac{P(Y|Z,\theta)P(Z|\theta)}{P(Z|Y,\theta^{(i)})P(Y|\theta^{(i)})}$$
则只需要最大化 $B(\theta,\theta^{(i)})$，故
$$\begin{eqnarray}
\theta^{(i+1)} &=& \arg\max_\theta\left(L(\theta^{(i)})+\sum_ZP(Z|Y,\theta^{(i)})\log\frac{P(Y|Z,\theta)P(Z|\theta)}{P(Z|Y,\theta^{(i)})P(Y|\theta^{(i)})}\right) \\
&=& \arg\max_\theta\left(\sum_ZP(Z|Y,\theta^{(i)})\log\left(P(Y|Z,\theta)P(Z|\theta)\right)\right) \\
&=& \arg\max_\theta\left(\sum_ZP(Z|Y,\theta^{(i)})\log P(Y,Z|\theta)\right) \\
&=& \arg\max_\theta Q(\theta,\theta^{(i)})
\end{eqnarray}$$

EM 算法不能保证全局最优。

## 9.2 EM 算法的收敛性

**
定理 9.1 设 $P(Y|\theta)$ 为观测数据的似然函数，$\theta^{(i)}$ 为 EM 算法得到的参数估计序列，$P(Y|\theta^{(i)})$ 为对应的似然函数序列，则 $P(Y|\theta^{(i)})$ 是单调递增的，即
$$P(Y|\theta^{(i+1)})\geq P(Y|\theta^{(i)})$$
**

**
定理 9.2 设 $L(\theta)=\log P(Y|\theta)$ 为观测数据的对数似然函数，$\theta^{(i)}$ 为 EM 算法得到的参数估计序列，$L(\theta^{(i)})$ 为对应的对数似然函数序列。  
(1) 如果 $P(Y|\theta)$ 有界，则 $L(\theta^{(i)})=\log P(Y|\theta^{(i)})$ 收敛到某一值 $L^\star$  
(2) 在函数 $Q(\theta,\theta')$ 与 $L(\theta)$ 满足一定条件下，由 EM 算法得到的参数估计序列 $\theta^{(i)}$ 的收敛值 $\theta^\star$ 是 $L(\theta)$ 的稳定点
**

在应用中，初始值的选择很重要，常用的办法是选取几个不同的初值进行迭代，然后对得到的各个估计值加以比较，从中选择最好的。

## 9.3 EM 算法在高斯混合模型学习中的应用

EM 算法的一个重要应用是高斯混合模型的参数估计。高斯混合模型应用广泛，在许多情况下，EM 算法是学习高斯混合模型（Gaussian misture model）的有效方法。

### 9.3.1 高斯混合模型

**
定义 9.2（高斯混合模型）高斯混合模型是指具有如下形式的概率分布模型：
$$P(y|\theta)=\sum_{k=1}^K\alpha_k\phi(y|\theta_k)$$
其中，$\alpha_k$ 是系数，$\alpha_k\geq0$，$\sum_{k=1}^K\alpha_k=1$；$\phi(y|\theta_k)$ 是高斯分布密度，$\theta_k=(\mu_k,\sigma_k^2)$
$$\phi(y|\theta_k)=\frac{1}{\sqrt{2\pi}\sigma_k}\exp\left(-\frac{(y-\mu_k)^2}{2\sigma_k^2}\right)$$
称为第 $k$ 个分模型。
**

一般混合模式可以由任意概率分布密度函数代替高斯分布密度。

### 9.3.2 高斯混合模型参数估计的 EM 算法

假设观测数据 $y_1,y_2,\cdots,y_N$ 由高斯混合模型生成
$$P(y|\theta)=\sum_{k=1}^K\alpha_k\phi(y|\theta_k)$$
其中 $\theta=(\alpha_1,\alpha_2,\cdots,\alpha_K;\theta_1,\theta_2,\cdots,\alpha_K)$。我们用 EM 算法估计高斯混合模型的参数 $\theta$。

$\blacksquare$ 明确隐变量，写成完全数据的对数似然函数

引入隐变量 $\gamma_{jk}$
$$\gamma_{jk}=\begin{cases}
1, & 第\ j\ 个观测来自第\ k\ 个分模型 \\
0, & 否则
\end{cases} \\
j=1,2,\cdots,N;\ k=1,2,\cdots,K$$
于是，完全数据似然函数可以写成：
$$\begin{eqnarray}
P(y,\gamma|\theta) &=& \prod_{j=1}^NP(y_j,\gamma_{j1},\gamma_{j2},\cdots,\gamma_{jK}|\theta) \\
&=& \prod_{k=1}^K\prod_{j=1}^N\left[\alpha_k\phi(y_j|\theta_k)\right]^{\gamma_{jk}} \\
&=& \prod_{k=1}^K\alpha_k^{n_k}\prod_{j=1}^N\left[\phi(y_j|\theta_k)\right]^{\gamma_{jk}} \\
&=& \prod_{k=1}^K\alpha_k^{n_k}\prod_{j=1}^N\left[\frac{1}{\sqrt{2\pi}\sigma_k}\exp\left(-\frac{(y_j-\mu_k)^2}{2\sigma_k^2}\right)\right]^{\gamma_{jk}}
\end{eqnarray}$$
其中
$$n_k=\sum_{j=1}^N\gamma_{jk},\ \sum_{k=1}^Kn_k=N$$
那么，完全数据的对数似然函数为
$$\log P(y,\gamma|\theta)=\sum_{k=1}^K\left\{n_k\log\alpha_k+\sum_{j=1}^N\gamma_{jk}\left[\log\left(\frac{1}{\sqrt{2\pi}}\right)-\log\sigma_k-\frac{1}{2\sigma_k^2}(y_j-\mu_k)^2\right]\right\}$$

$\blacksquare$ EM 算法的 E 步：确定 $Q$ 函数
$$\begin{eqnarray}
Q\left(\theta,\theta^{(i)}\right) &=& \text{E}\left[\log P(y,\gamma|\theta)|y,\theta^{(i)}\right] \\
&=& \text{E}\left\{\sum_{k=1}^K\left\{n_k\log\alpha_k+\sum_{j=1}^N\gamma_{jk}\left[\log\left(\frac{1}{\sqrt{2\pi}}\right)-\log\sigma_k-\frac{1}{2\sigma_k^2}(y_j-\mu_k)^2\right]\right\}\right\} \\
&=& \sum_{k=1}^K\left\{\sum_{j=1}^N\text{E}[\gamma_{jk}]\log\alpha_k+\sum_{j=1}^N\text{E}[\gamma_{jk}]\left[\log\left(\frac{1}{\sqrt{2\pi}}\right)-\log\sigma_k-\frac{1}{2\sigma_k^2}(y_j-\mu_k)^2\right]\right\}
\end{eqnarray}$$
这里需要计算 $\text{E}[\gamma_{jk}|y,\theta]$，记为 $\hat{\gamma}_{jk}$
$$\begin{eqnarray}
\hat{\gamma}_{jk} &=& \text{E}[\gamma_{jk}|y,\theta]=P(\gamma_{jk}=1|y,\theta) \\
&=& \frac{P(\gamma_{jk}=1,y_j|\theta)}{\sum_{k=1}^KP(\gamma_{jk}=1,y_j|\theta)} \\
&=& \frac{P(y_j|\gamma_{jk}=1,\theta)P(\gamma_{jk}=1|\theta)}{\sum_{k=1}^KP(y_j|\gamma_{jk}=1,\theta)P(\gamma_{jk}=1|\theta)} \\
&=& \frac{\alpha_k\phi(y_j|\theta_k)}{\sum_{k=1}^K\alpha_k\phi(y_j|\theta_k)}
\end{eqnarray}$$
其中
$$j=1,2,\cdots,N;\ k=1,2,\cdots,K$$
$\hat{\gamma_{jk}}$ 是在当前模型参数下第 $j$ 个观测数据来及第 $k$ 分模型的概率，称为分模型 $k$ 对观测数据 $y_j$ 的响应度。

将 $\hat{\gamma_{jk}}=\text{E}[\gamma_{jk}]$ 及 $n_k=\sum_{j=1}^N\text{E}[\gamma_{jk}]$ 带入上式，得
$$Q\left(\theta,\theta^{(i)}\right)=\sum_{k=1}^K\left\{n_k\log\alpha_k+\sum_{j=1}^N\gamma_{jk}\left[\log\left(\frac{1}{\sqrt{2\pi}}\right)-\log\sigma_k-\frac{1}{2\sigma_k^2}(y_j-\mu_k)^2\right]\right\}$$

$\blacksquare$ 确定 EM 算法的 M 步

即令各偏导为零，得：
$$\hat{\mu}_k\equiv\frac{\partial Q}{\partial \mu_k}=\frac{\sum_{j=1}^N\hat{\gamma}_{jk}y_j}{\sum_{j=1}^N\hat{\gamma}_{jk}} \\
\hat{\sigma_k}^2\equiv\frac{\partial Q}{\partial \sigma_k^2}=\frac{\sum_{j=1}^N\hat{\gamma}_{jk}(y_j-\mu_k)^2}{\sum_{j=1}^N\hat{\gamma}_{jk}} \\
\hat{\alpha}_k\equiv\frac{\partial Q}{\partial \alpha_k}=\frac{n_k}{N}=\frac{\sum_{j=1}^N\hat{\gamma}_{jk}}{N} \\
k=1,2,\cdots,K$$

**
算法 9.2（高斯混合模型参数估计的 EM 算法）  
输入：观测数据 $y_1,y_2,\cdots,y_N$，高斯混合模型  
输出：高斯混合模型参数  
(1) 取参数的初始值开始迭代  
(2) E 步：根据当前模型参数，计算分模型 $k$ 对观测数据 $y_j$ 的响应度
$$\hat{\gamma}_{jk}=\frac{\alpha_k\phi(y_j|\theta_k)}{\sum_{k=1}^K\alpha_k\phi(y_j|\theta_k)},\ j=1,2,\cdots,N;\ k=1,2,\cdots,K$$
(3) M 步：计算新一轮迭代的模型参数
$$\hat{\mu}_k=\frac{\sum_{j=1}^N\hat{\gamma}_{jk}y_j}{\sum_{j=1}^N\hat{\gamma}_{jk}} \\
\hat{\sigma_k}^2=\frac{\sum_{j=1}^N\hat{\gamma}_{jk}(y_j-\mu_k)^2}{\sum_{j=1}^N\hat{\gamma}_{jk}} \\
\hat{\alpha}_k=\frac{n_k}{N}=\frac{\sum_{j=1}^N\hat{\gamma}_{jk}}{N} \\
k=1,2,\cdots,K$$
(4) 重复 (2)，(3)，直到收敛
**
