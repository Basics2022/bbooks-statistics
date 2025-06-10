(prob:convergence)=
# Convergence in statistics


(prob:convergence:weak)=
## Convergence in distribution - weak convergence

A sequence of $X_i$ of real-valued random variables, cumulative distribution functions $F_i$, converges in distribution to a random variable $X$ with cumulative distribution $F$ is

$$\lim_{n \rightarrow +\infty} F_n(x) = F(x) \ ,$$

for $\forall x \in \mathbb{R}$ where $F(x)$ is continuous.

For multi-valued random variables, the condition reads

$$\lim_{n \rightarrow +\infty} P( X_n \in A) = P( X \in A) \ ,$$

for every $A \subset \mathbb{R}^n$ ...**todo**


(prob:convergence:probability)=
## Convergence in probability

$$\lim_{n \rightarrow + \infty} P \left(\left| X_n - X \right| > \varepsilon  \right) = 0$$

```{warning} Convergence in probability and convergence in distribution

Convergence in probability $ \rightarrow $ convergence in distribution, but not viceversa.

[Example taken from wikipedia](https://en.wikipedia.org/wiki/Convergence_of_random_variables#Counterexamples)

```


(prob:convergence:strong)=
## Almost sure convergence - strong convergence

$$P\left( \lim_{n \rightarrow +\infty} X_n = X \right) = 1$$

i.e. events for which $X_n$ doesn't converge to $X$ has probability $0$,

$$P\left( \omega \in \Omega: \ \lim_{n \rightarrow + \infty} X_n(\omega) = X(\omega) \right) = 1$$


(prob:convergence:point)=
## Sure convergence - pointwise convergence

$$\left\{ \omega \in \Omega: \ \lim_{n \rightarrow + \infty} X_n(\omega) = X(\omega) \right\} = \Omega \ .$$

The same definition of almost sure convergence, without allowing the existance of sets with zero probability where convergence is not satisfied. Thus, it's likely there is no point in using sure converence instead of almost sure convergence in proability theory.


(prob:convergence:mean)=
## Convergence in absolute moments: mean,...

$$\lim_{n \rightarrow +\infty} \mathbb{E}\left( \left| X_n - X \right|^r \right) = 0$$


