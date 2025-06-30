(prob:processes:calculus)=
# Stochastic calculus

(prob:processes:calculus:ito-lemma)=
## Ito's lemma

It allows to find the differential of a time-dependent function of a stochastic process. Let $f(t,x)$ be a twice-differentiable scalar function. Its Taylor series gives

$$
\Delta f = \dfrac{\partial f}{\partial t} \Delta t + \dfrac{\partial f}{\partial x} \Delta x 
  + \dfrac{1}{2}\dfrac{\partial^2 f}{\partial t^2} \Delta t^2  
  +             \dfrac{\partial^2 f}{\partial t \partial x} \Delta t \, \Delta x  
  + \dfrac{1}{2}\dfrac{\partial^2 f}{\partial x^2} \Delta x^2 
$$

If the argument $x$ of the function $f$ is chosen to be a random process $X_t$ satisfying [Ito drift-diffusion process](prob:processes:calculus:ito-process:drift-diffusion),

$$d X_t = \mu_t \, dt + \sigma_t \, dW_t \ ,$$

the differential of function $f(t,X_t)$ results from the limit of Taylor series 

$$\begin{aligned}
  df
  & = \lim_{dt \rightarrow 0, dW_t \rightarrow 0} \left\{ \Delta f \right\} = \\
  & = \lim_{dt \rightarrow 0, dW_t \rightarrow 0} \left\{ \partial_t f dt + \partial_x f d X_t + \dfrac{1}{2} \left[ \partial_{tt} f \, dt^2 + 2 \partial_{xt} \, dt dX_t + \partial_{xx} f dX_t^2 \right] \right\} = \\
  & = \lim_{dt \rightarrow 0, dW_t \rightarrow 0} \left\{ \partial_t f dt + \partial_x f \left( \mu_t dt + \sigma_t dW_t \right) + \dfrac{1}{2} \left[ \partial_{tt} f \, dt^2 + 2 \partial_{xt} \, dt \left( \mu_t dt + \sigma_t dW_t \right) + \partial_{xx} f \left( \mu_t dt + \sigma_t dW_t \right)^2 \right] \right\} = \\
\end{aligned}$$

For $dt \rightarrow 0$, $\left(d W_t\right)^2 = O(dt)$; keeping only terms of order lower than or equal to $O(dt)$, the differential becomes,

$$df = \left( \partial_t f + \mu_t \partial_x f  \right) dt + \sigma_t \partial_x f \, d W_t + \dfrac{\sigma_t^2}{2} \partial_{xx} f \, dW_t^2 \ .$$

Replacing $dW_t^2$ with $d t$ **todo** *why?*, and recalling the SDE of the Ito drift-diffusion process,

$$\begin{aligned}
  df
  & = \left( \partial_t f + \mu_t \partial_x f + \dfrac{\sigma_t^2}{2} \partial_{xx} f \right) dt + \sigma_t \partial_x f \, d W_t = \\
  & = \left( \partial_t f +  \dfrac{\sigma_t^2}{2} \partial_{xx} f \right) dt + \partial_x f \left( \mu \, dt + \sigma_t \, d W_t \right) = \\
  & = \left( \partial_t f +  \dfrac{\sigma_t^2}{2} \partial_{xx} f \right) dt + \partial_x f \, dX_t \ .
\end{aligned}$$

(prob:processes:calculus:ito-calculus)=
## Ito's calculus

Integegration w.r.t. Browinan motion produces a random variable that can be defined as

$$\int_{0}^{t} F \, dW := \lim_{n \rightarrow +\infty} \sum_{[t_{i-1},t_i] \in \pi_n} F_{t_{i-1}} \left( W_{t_i} - W_{t_{i-1}} \right) \ ,$$

being $\pi_n$ a partition of interval $[0,t]$, and $H$ a random proces **todo** *with some characteristics...*

````{prf:example} Integral of a Brownian motion w.r.t. itself

$$Y(t) = \int_{s=0}^t W_s \, dW_s = \dfrac{1}{2} W_t^2 - \dfrac{t}{2} \ .$$

The expected value for each $t$ of the random process $Y_t$ is zero for all $t$, $\mathbb{E}\left[ W_t^2 \right]= 0$, as the expected value of $W_t^2$ is the variance of $W_t$, and thus $t$ by definition of the Wiener process.

```{dropdown} Evaluation of the integral

Let $f(t,x) = x^2$. Let's find the differential $df$ evaluated for $x = W_t$ using [Ito's lemma](prob:processes:calculus:ito-lemma), retaining only terms with order up to $O(dt)$. Since $\partial_t f \equiv 0$,

$$\begin{aligned}
  df & = \partial_x f|_{x=W_t} dW_t + \dfrac{1}{2} \partial_{xx} f|_{x=W_t} dW_t^2 
\end{aligned}$$

and thus, replacing $dW_t^2 = dt$,

$$\begin{aligned}
  d W_t^2 & =  2 W_t \, dW_t + dt \ .
\end{aligned}$$

or

$$\begin{aligned}
  W_t \, d W_t & = d \left( \dfrac{W_t^2}{2} \right) - \dfrac{dt}{2} \ .
\end{aligned}$$

Thus (**todo** *add details if needed. A bit too much freedom in using differentials over stochastic processes here*),

$$\begin{aligned}
  Y(t)
  & = \int_{s=0}^t W_s \, dW_s \, ds = \\
  & = \int_{s=0}^t \left( \dfrac{W_s}{2} \right) \, ds - \int_{s=0}^t \dfrac{1}{2} \, ds = \\
  & = \dfrac{1}{2} \left( W_t^2 - W_0^2 \right) - \dfrac{t}{2} \ .
\end{aligned}$$
```

````

(prob:processes:calculus:ito-process)=
## Ito processes

(prob:processes:calculus:ito-process:drift-diffusion)=
### Ito drift-diffusion process

An Ito drift-diffusion process is a stochastic process satisfying the stochastic differential equation (SDE)

$$dX_t = \mu_t \, dt + \sigma_t \, dW_t \ ,$$ (eq:ito:drift-diff)

with $W_t$ a Wiener process. If $\mu_t = \mu$, $\sigma_t = \sigma$ are constant a closed-form solution can be found using [Ito's lemma](prob:processes:calculus:ito-lemma), for $f(t,x) = x$, or by direct (stochastic) integration of the SDE {eq}`eq:ito:drift-diff`, as

$$\begin{aligned}
  \int_{s=0}^t dX_s & = \int_{s=0}^t \mu \, ds + \int_{s=0}^t \sigma \, dW_s \\
\end{aligned}$$
$$\begin{aligned}
  X_t - X_0 & = \mu t + \sigma \left( W_t - W_0 \right) \ ,
\end{aligned}$$

so that $X_t - X_0 \sim \mathscr{N}\left( \mu t, \sigma^2 t \right)$.

```{admonition} Scaling of a Wiener process
:class: tip

Term $\sigma W_t$ represents a scaling of a Wiener process $W_t \sim \mathscr{N}(0, t)$ with zero expected value and variance $t$. Multiplication by factor $\sigma$ results in a multiplication of the expected value by $\sigma$ and variance by $\sigma^2$.

```


(prob:processes:calculus:ito-process:gbm)=
### Geometric Brownian Motion, GBM

A geometric Brownian motion is a stochastic process satisfying the SDE

$$d X_t = \mu X_t \, dt + \sigma X_t \, dW_t \ .$$

```{prf:example} GBM in Finance
:label: example:gbm:finance

GBM can be used as a model of the price of an asset with constant expected return and variance of returns with normal distribution.

```

Let $f(x) = \ln x$ be evaluated for $x = X_t$. Ito's lemma, with $\partial_t f \equiv 0$, provides the expression of the differential

$$\begin{aligned}
  d f
  & = \partial_x f|_{X_t} d X_t + \dfrac{1}{2} \partial_{xx} f|_{X_t} d X_t^2 = \\
  & = \partial_x f|_{X_t} \left( \mu X_t \, dt + \sigma X_t \, dW_t \right) + \dfrac{1}{2} \partial_{xx} f|_{X_t}  \left( \mu X_t \, dt + \sigma X_t \, dW_t \right)^2 = \\
  & = \dfrac{1}{X_t} \left( \mu X_t \, dt + \sigma X_t \, dW_t \right) - \dfrac{1}{2} \dfrac{1}{X_t^2} \sigma^2 X^2_t \, dW^2_t = \\
  d \left( \ln X_t \right) & = \left( \mu - \dfrac{\sigma^2}{2} \right) \, dt + \sigma \, dW_t \ ,
\end{aligned}$$

whose solution after integration reads

$$\ln X_t = \ln X_0 + \left( \mu - \dfrac{\sigma^2}{2} \right) \, t + \sigma \, W_t \ ,$$

or

$$X_t = X_0 \, e^{\left( \mu - \frac{\sigma^2}{2} \right) \, t + \sigma W_t} \ .$$


(prob:processes:calculus:ito-process:gbm-drift)=
### Geometric Brownian Motion with drift

A geometric Brownian motion is a stochastic process satisfying the SDE

$$d X_t = \mu X_t \, dt - C \, dt + \sigma X_t \, dW_t \ .$$

```{prf:example} GBM with constant withdrawal in finance
:label: example:gbm-drift:finance

GBM with drift can be used in finance as a model to represent DCA strategy and pension withdrawal, and to show and discuss **sequence risk**.

```

The solution reads

$$X_t = X_0 e^{\left( \mu - \frac{\sigma^2}{2} \right) (t-t_0) + \sigma ( W_t - W_0)} + \int_{s=0}^{t} C e^{\left( \mu - \frac{\sigma^2}{2} \right) (t-s) + \sigma ( W_t - W_s)} \, ds \ .$$

```{dropdown} Integration factor method for linear SDEs
:open:

Integration factor method for linear SDEs

$$d X_t = a \, dt + b \, dW_t \ ,$$

with $a(X_t, t, W_t)$, $b(X_t, t, W_t)$

aims at finding an exponential factor $e^{\alpha t + \beta W_t}$ that allows to get an integrable expression of the differential

$$d \left( e^{\alpha t + \beta W_t} X_t \right) = d \, f\left( t, W_t, X_t \right) \ .$$

Taylor expansion of this expression up to terms of order $dt \sim dW_t^2$ reads

$$\begin{aligned}
  d \, f(t,W_t,X_t)
  & = \partial_t f \, dt + \partial_w f \, d W_t + \partial_x f \, \underbrace{dX_t}_{a dt + b dW_t} + \\
  & + \dfrac{1}{2} \left( \underbrace{\partial_{tt} f \, dt^2}_{o(dt)} + \partial_{ww} f \, \underbrace{dW_t^2}_{dt} + \partial_{xx}  f\, \underbrace{dX_t^2}_{b^2 \, dW_t^2 = b^2 \, dt} + \underbrace{2 \partial_{tw} f \, dt \, dW_t + 2 \partial_{tx} f \, dt \, dX_t}_{o(dt)} + 2 \partial_{xw} f \, \underbrace{dW_t \, dX_t}_{b dW_t^2 = b dt}  \right) = \\
  & = dt \left[ \partial_t f + a \partial_x f + \dfrac{1}{2} \partial_{ww} f + \dfrac{1}{2} b^2 \partial_{xx} f + 2 b \partial_{xw} f \right] + d W_t \left[ \partial_w f + b \partial_x f \right] \\
\end{aligned}$$

```

```{dropdown} Proof (with integration factor method, for linear SDEs)
:open:

GBM motion with drift and constant coefficients is governed by SDE

$$d X_t = \mu X_t \, dt - C \, dt + \sigma X_t \, dW_t \ .$$

Referring to the general expression of SDEs, coefficients $a$, $b$ of the GBM with drift read

$$\begin{aligned}
  a & = \mu \, X_t + C \\
  b & = \sigma \, X_t \ .
\end{aligned}$$


Partial derivatives of function $f = e^{\alpha t + \beta w} \, x$ appearing in the solution of SDEs through integration factor method read

$$\begin{aligned}
  \partial_t    f & = e^{\alpha t + \beta w} \, x \, \alpha   \\
  \partial_w    f & = e^{\alpha t + \beta w} \, x \, \beta    \\
  \partial_x    f & = e^{\alpha t + \beta w}                  \\
  \partial_{xx} f & = 0                                       \\
  \partial_{wx} f & = e^{\alpha t + \beta w}      \, \beta    \\
  \partial_{ww} f & = e^{\alpha t + \beta w} \, x \, \beta^2  \\
\end{aligned}$$

It's now possible to simplify the RHS of the the expression of the differential $df$. Namely, it's possible to choose values of $\alpha$, $\beta$ in order to get simpler expressions of the factors of the differentials $dt$  and $d W_t$ 

$$\begin{aligned}
  dW_t: \quad  \partial_{W_t} f 
  & = \left.\left( \partial_w f + b \partial_x f \right)\right|_{t,W_t,X_t} = \\
  & = e^{\alpha t + \beta W_t} \, \left( X_t \beta + b \right) = \\
  & = e^{\alpha t + \beta W_t} \, X_t \left( \beta + \sigma \right) \\
  dt  : \quad  \partial_{  t} f  \quad 
  & = \left.\left[ \partial_t f + a \partial_x f + \dfrac{1}{2} \partial_{ww} f + \dfrac{1}{2} b^2 \partial_{xx} f + b \partial_{xw} f \right]\right|_{t,W_t,X_t} \\
  & = e^{\alpha t + \beta W_t} \left[ X_t \alpha + a + \dfrac{1}{2} X_t \beta^2 + 0 + b \beta \right] = \\
  & = e^{\alpha t + \beta W_t} \left[ X_t \alpha + \mu X_t + C + \dfrac{1}{2} X_t \beta^2 + \sigma X_t \beta \right] = \\
  & = e^{\alpha t + \beta W_t} \left[ X_t \left( \alpha + \mu + \dfrac{1}{2} \beta^2 + \sigma \beta \right) + C \right] \ .
\end{aligned}$$

Setting 

$$\begin{aligned}
  \beta  & = - \sigma \\ 
  \alpha & = - \mu - \dfrac{1}{2} \beta^2 - \sigma \beta = - \mu + \dfrac{\sigma^2}{2} \ , 
\end{aligned}$$

the differential $d f$ becomes


$$d\left( e^{\left( -\mu + \frac{\sigma^2}{2} \right) t - \sigma W_t} \, X_t \right) = C e^{\left( -\mu + \frac{\sigma^2}{2} \right) t - \sigma W_t}$$

and integration gives

$$X_t = X_0 e^{\left( \mu - \frac{\sigma^2}{2} \right) (t-t_0) + \sigma ( W_t - W_0)} + \int_{s=0}^{t} C e^{\left( \mu - \frac{\sigma^2}{2} \right) (t-s) + \sigma ( W_t - W_s)} \, ds \ .$$


```

