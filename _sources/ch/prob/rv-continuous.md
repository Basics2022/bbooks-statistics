(prob:rv-continuous)=
# Continuous stochastic variables




(prob:rv-continuous:ex)=
## Examples

Here some common examples of continuous random variables are introduced. Their functional dependence on the value of the r.v. is quite easy to remember, while the normalization factor could look quite "esoteric".

(prob:rv-continuous:ex:normal)=
### Normal distribution, $\mathscr{N}(\mu, \sigma^2)$

pdf is

$$f(x; \mu, \sigma^2) = \dfrac{1}{\sqrt{2 \pi \sigma^2}}  e^{-\frac{(x-\mu)^2}{2 \sigma^2}}  \quad \propto \quad e^{- \frac{(x-\mu)^2}{2 \sigma^2}}$$

| Moment         | Value        |
| -------------- | ------------ |
| Expected value | $\mu$        |
| Variance       | $\sigma^2$   |

Expected value, $\mu$; variance, $\sigma^2$.

```{dropdown} Unitariety

$$\int_{x=-\infty}^{+\infty} e^{-\frac{(x-\mu)^2}{2 \sigma^2}} = \sqrt{2 \pi \sigma^2}$$

**todo** *integral $\int_{-\infty}^{+\infty} e^{- \alpha x^2} dx$*

```


```{dropdown} Expected value

$$\begin{aligned}
  \mathbb{E}\left[ X \right] 
  & =  \int_{x = -\infty}^{+\infty} x \dfrac{1}{\sqrt{2 \pi \sigma^2}}  e^{-\frac{(x-\mu)^2}{2 \sigma^2}}   \\
\end{aligned}$$

```

```{dropdown} Variance

$$\begin{aligned}
  \mathbb{E}\left[ (X-\mu)^2 \right] 
  & =  \dots
\end{aligned}$$

```


(prob:rv-continuous:ex:chi-2)=
### Chi-square, $\chi_N^2$

$$\chi_N^2 := \sum_{n=1}^N X^2_n$$

pdf is

$$f(x; n) = \dots \quad \propto \quad  x^{\frac{n}{2} - 1} e^{- \frac{x}{2}} $$

(prob:rv-continuous:ex:t-student)=
### Student-$t$ distribution, $t_{\nu}$

$$t_{\nu} = \dfrac{Z}{\sqrt{\dfrac{K}{\nu}}} \ ,$$

with $Z \sim \mathscr{N}(0,1)$, and $K \sim \chi^2_\nu$.

pdf is

$$f(x; n) = \dots \quad \propto \quad \left( 1 + \frac{x^2}{n} \right)^{-\frac{n+1}{2}} $$

