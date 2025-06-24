(prob:iid)=
# Independent identically distributed random variables

```{prf:definition} Independent identically distributed (iid) random variables

```

(prob:iid:large-numbers)=
## Law of the large numbers

(prob:iid:large-numbers:weak)=
### Weak form

**todo**

(prob:iid:large-numbers:strong)=
### Strong form

**todo**

(prob:iid:clt)=
## Central Limit Theorem

```{prf:theorem} CLT
:label: thm:clt

Let $\{ X_k \}_{k=1:n}$ a sequence of iid random variables with average value $\mathbb{E}[X_k] = \mu$ and **finite**[^clt-heavy-tails] variance $\mathbb{E}[(X_k-\mu)^2] = \sigma^2 < \infty$, then the **sample average**

$$\overline{X}_n := \dfrac{1}{n} \sum_{k=1}^n X_k \ ,$$

[converges in distribution](prob:convergence:weak) - or weakly converges - to the normal distribution $\mathscr{N}\left(\mu, \frac{\sigma^2}{n} \right)$,

$$\overline{X}_n \quad \rightarrow^d \quad \mathscr{N}\left(\mu, \frac{\sigma^2}{n} \right) \ .$$


```

[^clt-heavy-tails]: Does the CLT hold for [**heavy-tailed** distributions](prob:heavy-tailed)?

```{dropdown} Proof of CLT
:open:

Let $\{ X_k \}_{k=1:n}$ the sequence of iid random variables. Thus, $\sum_{k=1}^n X_k$ has expected value $n \mu$ and variance $n \sigma^2$. Let

$$Z_n := \dfrac{\sum_{k=1}^n X_k - n \mu}{\sqrt{n \sigma^2}} = \sum_{k=1}^{n} \dfrac{X_k - \mu}{\sqrt{n \sigma^2}} =: \sum_{k=1}^n \dfrac{Y_k}{\sqrt{n}} \ .$$

Expeceted value and variance of variables $Y_k$ are respectively $\mathbb{E}[Y_k] = 0$ and $\mathbb{E}[Y_k^2] = 1$.
The [characteristic function](prob:characteristic-fun) of $Z_n$, see {prf:ref}`ex:char-fun:independent` for the linear combination of independent variables, reads

$$\begin{aligned}
  \varphi_{Z_n}(t) 
  & = \varphi_{Y_1} \left( \dfrac{t}{\sqrt{n}} \right) \dots \varphi_{Y_n} \left( \dfrac{t}{\sqrt{n}} \right) = &&  (1) \\
  & = \left[ \varphi_{Y_1} \left( \dfrac{t}{\sqrt{n}} \right) \right]^n \ ,
\end{aligned}$$

as $(1)$ the variables are not only independent but identically distributed: as they have the same pdf, they also have the same characteristic function. Expanding in Taylor series, see example {prf:ref}`ex:char-fun:taylor` for $\frac{t}{\sqrt{n}} \rightarrow 0$, the approximation of the characteristic function reads (remembering that $Y_n$ have zero expected value and unit variance),

$$\varphi_{Y_1}\left( \dfrac{t}{\sqrt{n}} \right) \sim 1 - \dfrac{t^2}{2 n} \ ,$$

while

$$\varphi_{Z_n}(t) = \left[ \varphi_{Y_1} \left( \dfrac{t}{\sqrt{n}} \right) \right]^n \sim \left[  1 - \dfrac{t^2}{2 n}  \right]^n \sim e^{- \frac{t^2}{2}} \ ,$$

i.e. it converges to the characteristic function of a normal distribution $\mathscr{N}(0,1)$, see {prf:ref}`ex:char-fun:normal`.

**Levy's continuity theorem** completes the proof. **todo**


```


