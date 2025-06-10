(prob:processes:wiener)=
# Wiener process - Brownian motion

```{prf:definition} Wiener process - Brownian motion
:label: wiener:def

A Wiener process is a random process $W(t)$ with

1. initial condition, almost surely

  $$W(0) = 0$$

2. stationary and normally distributed increments,

  $$W(t) - W(s) \sim \mathscr{N}(0,|t-s|)$$

3. $W$ has independent increments: $W(t) - W(t+u)$ is independent from $W_s$, $s < t$

4. in $W(t)$ is almost surely continuous in $t$

```

```{admonition} Almost sure convergence in statistics

"Almost surely" here means [almost sure converngece](prob:convergence:strong) and it is explained in the section dealing with [convergence in statistics](prob:convergence), and used below to prove some properties of a Wiener process.

```

<!--
```{admonition} 
:class: tip
```
-->

## Properties

```{prf:property} Covariance of increments

By definition of covariance of an increment, and definition of [normal distribution](prob:rv-continuous:ex:normal) reads

  $$\mathbb{E}\left[ \left( W(t) - W(s) \right)^2  \right] = \mathbb{E}\left[ \mathscr{N}(0, |t-s|) \right] =  |t - s| \ .$$

Covariance of independent increments is zero, as [independence implies no correlation](prob:multidim:independence:no-correlation), i.e. zero covariance. Thus, if $a \le b \le c \le d$, $W(b)-W(a)$ and $W(d)-W(c)$ are independent by defintion of Wiener process, and their correlation is zero,

  $$\mathbb{E}\left[ ( W(b) - W(a) ) ( W(d) - W(c) )  \right] = 0$$

Co


```


```{prf:property} Covariance of increments

$$\mathbb{E}\left[ \left( W(t_1) - W(s_1) \right)  \left( W(t_2) - W(s_2) \right) \right] = \big| [s_1, t_1] \cap [s_2, t_2]\big|$$

```
```{dropdown} Proof
:open:

If $s_1 \le s_2 \le t_2 \le t_1$,

$$\begin{aligned}
  \mathbb{E}\left[ \left( W(t_1) - W(s_1) \right)  \left( W(t_2) - W(s_2) \right) \right] 
  & = \mathbb{E}\left[ W(t_1) W(t_2) \right] - \mathbb{E}\left[ W(t_1) W(s_2) \right] + \\
  & - \mathbb{E}\left[ W(s_1) W(t_2) \right] + \mathbb{E}\left[ W(s_1) W(s_2) \right] = \\
  & = (t_1 - t_2) - (t_1 - s_2) - (t_2 - s_1) + (s_2 - s_1) = \\
  & =
\end{aligned}$$

```



