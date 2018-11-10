Title: 方向导数和梯度
Category: 基础知识
Date: 2018-11-10 15:44:43
Modified: 2018-11-10 15:44:43
Tags: 数学

## 1. 方向导数

多元函数的偏导数反映了函数值沿着坐标轴方向的变化率，方向导数（directional derivative）则表示多元函数沿着某一方向的变化率。

**
定义 1.1（方向导数）设 $f$ 是定义于 $\mathbb{R}^n$ 中某区域 $D$ 上的函数，点 $P_0\in D$，$l$ 为一给定的非零向量，$P$ 为一动点，向量 $\vec{P_0P}$ 与 $l$ 的方向始终一致。如果极限
$$\lim_{\|P_0P\|\to0}\frac{f(P)-f(P_0}{\|\vec{P_0P}\|}$$
存在，则称此极限为函数 $f$ 在 $P_0$ 处沿 $l$ 方向的方向导数，记作 $\frac{\partial f}{\partial l}$。
**

**
定义 1.2（方向余弦）设 $l$ 是一个 $n$ 维非零向量，$l_0=\frac{l}{\|l\|}，即 $l_0$ 是与 $l$ 同向的单位向量。取 $0\leq\alpha_i\leq\pi$，使
$$l_0=(\cos\alpha_1,\cos\alpha_2,\cdots,\cos\alpha_n)$$
称
$$\cos\alpha_1,\cos\alpha_2,\cdots,\cos\alpha_n$$
为向量 $l$ 的方向余弦。
**

**
定理 1.1（方向导数计算公式）若函数 $f$ 在点 $P_0$ 处可微，向量 $l$ 的方向余弦为 $\cos\alpha_1,\cos\alpha_2,\cdots,\cos\alpha_n$，则函数 $f$ 在点 $P_0$ 处沿 $l$ 方向的方向导数存在，且
$$\frac{\partial f}{\partial l}\bigg\rvert_{P_0}=\frac{\partial f}{\partial x_1}\bigg\rvert_{P_0}\cos\alpha_1+\frac{\partial f}{\partial x_2}\bigg\rvert_{P_0}\cos\alpha_2+\cdots+\frac{\partial f}{\partial x_n}\bigg\rvert_{P_0}\cos\alpha_n$$
**

证：因为 $f$ 在 $P_0$ 处可微，向量 $\vec{P_0P}=(\Delta x_1,\Delta x_2,\cdots,\Delta x_n)$ 与 $l$ 同向，故
$$f(P)-f(P_0)=\frac{\partial f}{\partial x_1}\bigg\rvert_{P_0}\Delta x_1+\frac{\partial f}{\partial x_2}\bigg\rvert_{P_0}\Delta x_2+\cdots+\frac{\partial f}{\partial x_n}\bigg\rvert_{P_0}\Delta x_n+o(\|\vec{P_0P}\|)$$
故
$$\lim_{\|\vec{P_0P}\|\to0}\frac{f(P)-f(P_0)}{\|\vec{P_0P}\|}=\lim_{\|\vec{P_0P}\|\to0}\left[\frac{\partial f}{\partial x_1}\bigg\rvert_{P_0}\frac{\Delta x_1}{\|\vec{P_0P}\|}+\frac{\partial f}{\partial x_2}\bigg\rvert_{P_0}\frac{\Delta x_2}{\|\vec{P_0P}\|}+\cdots+\frac{\partial f}{\partial x_n}\bigg\rvert_{P_0}\frac{\Delta x_n}{\|\vec{P_0P}\|}+\frac{o(\|\vec{P_0P}\|)}{\|\vec{P_0P}\|}\right] \\
=\frac{\partial f}{\partial l}\bigg\rvert_{P_0}=\frac{\partial f}{\partial x_1}\bigg\rvert_{P_0}\cos\alpha_1+\frac{\partial f}{\partial x_2}\bigg\rvert_{P_0}\cos\alpha_2+\cdots+\frac{\partial f}{\partial x_n}\bigg\rvert_{P_0}\cos\alpha_n$$
因为 $\frac{\partial f}{\partial l}\bigg\rvert_{P_0}$ 存在，所以
$$\frac{\partial f}{\partial l}\bigg\rvert_{P_0}=\frac{\partial f}{\partial x_1}\bigg\rvert_{P_0}\cos\alpha_1+\frac{\partial f}{\partial x_2}\bigg\rvert_{P_0}\cos\alpha_2+\cdots+\frac{\partial f}{\partial x_n}\bigg\rvert_{P_0}\cos\alpha_n$$

注意：一个函数即使在某一点处连续，可偏导，且沿所有方向的方向导
数都存在，也不一定在该点可微。所以定义中的可微条件是必须的。

## 2. 梯度

设函数 $f$ 定义于 $\mathbb{R}^n$ 的区域 $D$ 上，或者说 $f$ 是区域 $D$ 上的一个数量场。我们的问题是在点 $P\in D$ 处 $f$ 的方向导数沿哪个方向取得最大值，即沿哪个方向数量场的变化率最大？这就是梯度（gradient）问题。

如果向量 $l$ 的方向余弦为
$$\cos\alpha_1,\cos\alpha_2,\cdots,\cos\alpha_n$$
那么 $f$ 在点 $P$ 处沿 $l$ 方向的方向导数为
$$\frac{\partial f}{\partial l}=\frac{\partial f}{\partial x_1}\cos\alpha_1+\cdots+\frac{\partial f}{\partial x_n}\cos\alpha_n$$
记 $n$ 维向量
$$\boldsymbol{g}=\left(\frac{\partial f}{\partial x_1},\cdots,\frac{\partial f}{\partial x_n}\right)$$
又记 $l$ 方向的单位向量为 $\boldsymbol{l_0}$，则
$$\boldsymbol{l_0}=\left(\cos\alpha_1,\cdots,\cos\alpha_n\right)$$
故
$$\frac{\partial f}{\partial l}=(\boldsymbol{g},\boldsymbol{l_0})$$
上式右端表示向量内积，由施瓦兹不等式
$$\left|\frac{\partial f}{\partial l}\right|=|(\boldsymbol{g},\boldsymbol{l_0})|\leq\|\boldsymbol{g}\|\|\boldsymbol{l_0}\|=\|\boldsymbol{g}\|$$
当且仅当 $\boldsymbol{g}$ 与 $\boldsymbol{l_0}$ 同向时，等号成立。而且
$$\max\frac{\partial f}{\partial l}=\|\boldsymbol{g}\|=\left[\sum_{i=1}^n\left(\frac{\partial f}{\partial x_i}\right)^2\right]^{\frac{1}{2}}$$

**
定义 2.1（梯度）设 $f$ 是 $\mathbb{R}^n$ 中区域 $D$ 上的数量场，如果 $f$ 在 $P_0\in D$ 处可微，称向量
$$\left(\frac{\partial f}{\partial x_1},\frac{\partial f}{\partial x_2},\cdots,\frac{\partial f}{\partial x_n}\right)\bigg\rvert_{P_0}$$
为 $f$ 在 $P_0$ 处的梯度，记作 ${\bf grad}f(P_0)$。
**

沿梯度方向，函数值增加最快。同样可知，方向导数的最小值在梯度的相反方向取得。
