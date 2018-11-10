Title: 拉格朗日对偶性
Category: 基础知识
Date: 2018-11-10 13:41:43
Modified: 2018-11-10 14:16:04
Tags: 数学

## 1. 原始问题

假设 $f(x)$，$c_i(x)$，$h_j(x)$ 是定义在 $\mathbb{R}^n$ 上的连续可微函数。考虑约束最优化问题：
$$\min_{x\in\mathbb{R}^n}f(x) \\
\text{s.t.}\ \ \ \ \
\begin{eqnarray}
c_i(x) &\leq& 0,i=1,2,\cdots,k \\
h_j(x) &=& 0,j=1,2,\cdots,l
\end{eqnarray}$$
称此优化约束问题为原始最优化问题或原始问题。

首先，引进广义拉格朗日函数：
$$L(x,\alpha,\beta)=f(x)+\sum_{i=1}^k\alpha_ic_i(x)+\sum_{j=1}^l\beta_jh_j(x)$$
这里，$x=\left(x^{(1)},x^{(2)},\cdots,x^{(n)}\right)^\text{T}\in\mathbb{R}^n$，$\alpha_i$，$\beta_j$ 是拉格朗日乘子，$\alpha_i\geq0$，考虑 $x$ 的函数：
$$\theta_P(x)=\max_{\alpha,\beta:\alpha\geq0}L(x,\alpha,\beta)$$
这里，下标 $P$ 表示原始问题。

易知：
$$\theta_P(x)=\begin{cases}
f(x), & x\ 满足原始问题约束 \\
+\infty, & 其他
\end{cases}$$
所以如果考虑极小化问题
$$\min_x\theta_P(x)=\min_x\max_{\alpha,\beta:\alpha_i\geq0}L(x,\alpha,\beta)$$
它是与原始最优化问题等价的问题。

为了方便，定义原始问题的最优值
$$p^{\star}=\min_x\theta_P(x)$$
称为原始问题的值。

## 2. 对偶问题

定义
$$\theta_D(\alpha,\beta)=\min_xL(x,\alpha,\beta)$$
再考虑极大化，即
$$\max_{\alpha,\beta:\alpha_i\geq0}\theta_D(\alpha,\beta)=\max_{\alpha,\beta:\alpha_i\geq0}\min_xL(x,\alpha,\beta)$$
上述问题称为广义拉格朗日函数的极大极小问题。

可以将广义拉格朗日函数的极大极小问题表示为约束最优化问题：
$$\max_{\alpha,\beta}\theta_D(\alpha,\beta)=\max_{\alpha,\beta}\min_xL(x,\alpha,\beta) \\
\text{s.t.}\ \ \ \alpha_i\geq0,i=1,2,\cdots,k$$
称为原始问题的对偶问题。定义对偶问题的最优值：
$$d^\star=\max_{\alpha,\beta:\alpha_i\geq0}\theta_D(\alpha,\beta)$$
称为对偶问题的值。

## 3. 原始问题和对偶问题的关系

> **定理 1** 若原始问题和对偶问题都有最优值，则
> $$d^\star=\max_{\alpha,\beta:\alpha_i\geq0}\min_xL(x,\alpha,\beta)\leq\min_x\max_{\alpha,\beta:\alpha_i\geq0}L(x,\alpha,\beta)=p^\star$$

> **推论 1** 设 $x^\star$ 是原始问题的可行解，$\alpha^\star$，$\beta^\star$ 是对偶问题的可行解，并且 $d^\star=p^\star$，则它们分别是原始问题和对偶问题的最优解。

> **定理 2** 考虑原始问题和对偶问题。假设函数 $f(x)$ 和 $c_i(x)$ 是凸函数，$h_j(x)$ 是仿射函数；并且假设不等式约束 $c_i(x)$ 是严格可行的，即存在 $x$，对所有 $i$，有 $c_i<0$，则存在 $x^\star$，$\alpha^\star$，$\beta^\star$，使 $x^\star$ 是原始问题的解，$\alpha^\star$，$\beta^\star$ 是对偶问题的解，并且
> $$p^\star=d^\star=L(x^\star,\alpha^\star,\beta^\star)$$

> **定理 3** 对原始问题和对偶问题，假设函数 $f(x)$ 和 $c_i(x)$ 是凸函数，$h_j(x)$ 是仿射函数，并且假设不等式约束 $c_i(x)$ 是严格可行的，则 $x^\star$，$\alpha^\star$，$\beta^\star$ 分别是原始问题和对偶问题的解的充要条件是 $x^\star$，$\alpha^\star$，$\beta^\star$ 满足下面的 Karush-Kuhn-Tucker（KKT）条件
> $$\nabla_xL(x^\star,\alpha^\star,\beta^\star)=0 \\
\alpha_i^\star c_i(x^\star)=0,i=1,2,\cdots,k \\
c_i(x^\star)\leq0,i=1,2,\cdots,k \\
\alpha_i^\star\geq0,i=1,2,\cdots,k \\
h_j(x^\star)=0,j=1,2,\cdots,l$$
