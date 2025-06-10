(prob:processes)=
# Stochastic processes

**Definition of stochastic process.**

**Examples.**
- White noise, $\xi(t)$, is a zero-mean process with no correlation between its values at different times

  $$\mathbb{E}\left[ \xi(t) \, \xi(s) \right] = \delta(t-s)$$

- Wiener process (Brownian motion), $W(t)$

  $$\begin{aligned}
    & W(0) = 0 \\
    & W(t) \text{ has independent increments} \\
    & W(t) - W(s) \sim N(0, t-s) \text{ for $t > s$} \\
    & W(t) \text{ are continuous but nowhere differentiable}
  \end{aligned}$$

  Informal relation between Wiener process and white noise signal

  $$\begin{aligned}
   W(t) - W(s) & = \int_{s}^{t} \xi(\tau) \, d \tau \\
   {}^{''} \dfrac{d W(t)}{d t} & = \xi(t) {}^{``}
  \end{aligned}$$

  where the derivative relation doesn't hold in the classical sense, as $W(t)$ is nowhere differentiable

- time-discrete Markov processes

**Applications**
- LTI
- Stochastic differential equations...

  $$d X(t) = \mu(t) \, dt + \sigma(t) \, dW(t)$$

**Assumptions.**
- Stationariety
- Ergodicity

$$k_{xy}(\tau) := \mathbb{E}[x(t) y(t-\tau)] = \lim_{T\rightarrow +\infty} \left\{ \frac{1}{2T} \int_{t = -T}^{T} x(t) \, y(t-\tau) \, d t \right\}$$




