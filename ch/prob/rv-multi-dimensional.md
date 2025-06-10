(prob:multidim)=
# Multi-dimensional stochastic variables

- joint distribution

  $$p_{XY}(x,y) $$

- marginal distribution. For continuous variables

  $$p_X(x) := \int_{y} p_{XY}(x,y) \, dy$$

  while for discrete variables
  
  $$p_X(x_i) = \sum_j p_{XY}(x_i,y_j)$$

- conditional distribution, $p_{X|Y}(x|y)$. The following holds

  $$p_{XY} = p_{X|Y} \, p_Y = p_{Y|X} p_X$$

For continuous r.v., integrating over $x$ the relation $p(x,y) = p(x|y) p(y)$

$$\begin{aligned}
  \int_{x} p(x,y) d x = \int_{x} p(x|y) \, p(y) \, dx = p(y) \underbrace{\int_{x} p(x|y) \, dx}_{= 1} = p(y) \ ,
\end{aligned}$$

as the normalization condition holds for conditional distribution $p(x|y)$.

```{prf:property}

$$\begin{aligned}
  p(i,j) = p(i|j) p(j)
\end{aligned}$$

$$\sum_i p(i,j) = \underbrace{\sum_i p(i|j)}_{=1} p(j) = p(j)$$


```


(prb:multidim:moments)=
## Moments

- expected value

  $$\boldsymbol{\mu}_{\mathbf{X}} := \mathbb{E}\left[ \mathbf{X} \right] = \int_{\mathbf{x}} p(\mathbf{x}) \, \mathbf{x} \,  d \mathbf{x}$$

- covariance

  $$\boldsymbol{\sigma}^2_{\mathbf{X}} := \mathbb{E} \left[ \Delta \mathbf{X} \, \Delta \mathbf{X}^T \right] = \int_{\mathbf{x}} p(\mathbf{x}) \, \Delta \mathbf{x} \Delta \mathbf{x}^T \, d \mathbf{x} \ ,$$

  with $\Delta \mathbf{X} := \mathbf{X} - \boldsymbol{\mu}_{\mathbf{X}} $, and $\Delta \mathbf{x} = \mathbf{x} - \boldsymbol{\mu}_{\mathbf{X}}$.

  Taking a pair of components $X_i$, $X_j$ of the random vector $\mathbf{X}$, their covariance is the $ij$ component of the array $\boldsymbol{\sigma}^2$, 

  $$\sigma^2_{ij} := \mathbb{E}\left[ \Delta X_i \, \Delta X_j \right] =: \rho_{ij} \sigma_i \sigma_j \ ,$$

  having introduced **(Pearson) correlation**, $\rho_{ij}$, between random variable $X_i$ and $X_j$, and being $\sigma_i$ the standard deviation of variable $X_i$, square root of its variance $\sigma^2_i$,

  $$\begin{aligned}
    \sigma^2_i 
    & = \mathbb{E}\left[ \left( X_i - \mu_i \right)^2  \right] = \\
    & = \int_{\mathbf{x}} (x_i - \mu_i)^2 p_{\mathbf{X}}(\mathbf{x}) d \mathbf{x} = \\
    & = \int_{x_i} (x_i - \mu_i)^2 p_i (x_i) \, d x_i 
  \end{aligned}$$

  Here the integrals read

  $$\begin{aligned}
    \mu_i 
    & = \int_{\mathbf{x}} x_i \, p_{\mathbf{X}}(\mathbf{x}) x_i \, d \mathbf{x} = \\
    & = \int_{\mathbf{x}} x_i \, p(x_1, x_2, \dots, x_i, \dots, x_n) d x_1 d x_2 \dots d x_i \dots d x_n = \\
    & = \int_{\mathbf{x}} x_i \, p(x_i) p(x_1, x_2, \dots, x_{i-1}, x_{i+1}, \dots, x_n | x_i) d x_1 d x_2 \dots d x_i \dots d x_n = \\
    & = \int_{x_i} x_i \, p(x_i) \underbrace{\int_{x_1} \dots \int_{x_n} p(x_1, x_2, \dots, x_{i-1}, x_{i+1}, \dots, x_n | x_i) d x_1 \dots d x_{i-1} d x_{i+1} \dots d x_n}_{= 1 \text{ $\forall x_i$}} d x_i = \\
    & = \int_{x_i} x_i \, p(x_i) \, d x_i \ .
  \end{aligned}$$

**Property of correlation.** $|\rho_{XY}| \le 1$. Proof with Cauchy-Schwartz inequality **todo**

```{admonition} Notation
:class: tip

Here, covariance is indicated as $\boldsymbol{\sigma}^2$. This is not a power $2$, but just a symbol, at most recalling that covariance matrix is **semi-definite positive**.

```

**Properties of covariance.**
- symmetric
- semi-definite positive
- spectrum...




(prob:multidim:bayes)=
## Bayes' theorem

```{prf:theorem} Bayes' theorem

Where $p_Y(y) \ne 0$,

$$p_{X|Y}(x|y) = \dfrac{p_{XY}(x,y)}{p_Y(y)}$$

```

(prob:multidim:independence)=
## Statistical independence

```{prf:definition} Independent random variables
Given two random variables $X$, $Y$ with joint distribution, the random variable $X$ is independent from $Y$ if its conditional probability equals its marginal probability,

$$p_{X|Y} = p_X \ ,$$

i.e. the probability of $X$ doesn't depend on $Y$.

```

(prob:multidim:independence:no-correlation)=
### Independence implies no correlation

Given two random variables $X$, $Y$ are independent if $p(x|y) = p(x)$ and thus $p(x,y) = p(x) p(y)$. Covariance of two random variable reads

$$\sigma^2_{xy} = \mathbb{E} \left[ (X - \mu_X) (Y - \mu_Y)  \right] \ ,$$

and if they're independent, it immediately follows that their covariance $\sigma^2_{XY}$ is zero (and so their correlation $\rho_{XY}$)

$$\sigma^2_{xy} = \underbrace{\mathbb{E} \left[ X - \mu_X \right]}_{=0} \underbrace{\mathbb{E} \left[ Y - \mu_Y \right]}_{=0} = 0 \ ,$$

as the expected value of the deviation from the expected value is zero, $\mathbb{E} \left[ X - \mathbb{E}[X] \right] = 0$.

```{dropdown} Proof for continuous r.v.

$$\begin{aligned}
  \sigma^2_{xy}
  & = \mathbb{E} \left[ (X - \mu_X) (Y - \mu_Y)  \right] = \\
  & = \int_{x,y} ( x - \mu_X) ( y - \mu_Y) p(x,y) \, dx dy = && (1) \\
  & = \int_{x,y} ( x - \mu_X) ( y - \mu_Y) p(x) p(y) \, dx dy = \\
  & = \int_{x} ( x - \mu_X) p(x) dx \, \int_{y} ( y - \mu_Y) p(y) dy = && (2) \\
\end{aligned}$$

having used here the common notation abuse $p_X(x) = p(x)$ and $(1)$ statistical independence, $p(x,y) = p(x) p(y)$, and $(2)$ $\mathbb{E}\left[ X - \mathbb{E}[X] \right] = 0$.

```

```{dropdown} Proof for discrete r.v.

Repeat the proof for continuous r.v. using summations instead of integrals.


```







