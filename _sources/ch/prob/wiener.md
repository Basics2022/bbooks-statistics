(prob:processes:wiener)=
# Wiener process - Brownian motion

- Introduction: history and relation with other problems (diffusion?)
- Definition and some theory
- Simulation of Wiener process, demonstration of properties shown in theory section

(prob:processes:wiener:def)=
## Definition

```{prf:definition} Wiener process - Brownian motion
:label: wiener:def

A Wiener process is a random process $W(t)$ with

1. initial condition, almost surely

  $$W(0) = 0$$

2. increments with zero-mean [normal distribution](prob:rv-continuous:ex:normal)

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

Covariance of an increment follows the definition of Wiener process and the definition of [normal distribution](prob:rv-continuous:ex:normal),

  $$\mathbb{E}\left[ \left( W(t) - W(s) \right)^2  \right] = \mathbb{E}\left[ \mathscr{N}(0, |t-s|) \right] =  |t - s| \ .$$ (eq:wiener:cov:1)

Covariance of independent increments - on non-overlapping ranges - is zero, as [independence implies no correlation](prob:multidim:independence:no-correlation), i.e. zero covariance. Thus, if $a \le b \le c \le d$, $W(b)-W(a)$ and $W(d)-W(c)$ are independent by property $(3)$ in {prf:ref}`wiener:def` of Wiener process, and thus their covariance - and correlation - is zero,

  $$\mathbb{E}\left[ ( W(b) - W(a) ) ( W(d) - W(c) )  \right] = 0$$ (eq:wiener:cov:2)

Covariance of two generic increments reads

$$\mathbb{E}\left[ \left( W(t_1) - W(s_1) \right)  \left( W(t_2) - W(s_2) \right) \right] = \big| [s_1, t_1] \cap [s_2, t_2]\big|$$ (eq:wiener:cov:3)

as it's proved below.

```

```{dropdown} Proof of the covariance of two generic increments 

If $s_1 \le s_2 \le t_2 \le t_1$,

$$\begin{aligned}
  & \mathbb{E}\left[ \left( W(t_1) - W(s_1) \right)  \left( W(t_2) - W(s_2) \right) \right] = \\
  & \quad = \mathbb{E}\left[ \left( W(t_1) - W(t_2) + W(t_2) - W(s_2) + W(s_2) - W(s_1) \right) \left( W(t_2) - W(s_2) \right) \right] = \\
  & \quad = \underbrace{\mathbb{E}\left[ \left( W(t_1) - W(t_2) \right) (W(t_2) - W(s_2) ) \right]}_{=0} 
          + \underbrace{\mathbb{E}\left[ \left( W(t_2) - W(s_2) \right) (W(t_2) - W(s_2) ) \right]}_{=|t_2 - s_2|} + \\
  & \quad + \underbrace{\mathbb{E}\left[ \left( W(s_2) - W(s_1) \right) (W(t_2) - W(s_2) ) \right]}_{= 0} = \\
  & \quad  = 0 + |t_2 - s_2| + 0 = \big| [s_1, t_1] \cap [s_2, t_2] \big| \ . 
\end{aligned}$$

Similarly, if $s_1 \le s_2 \le t_1 \le t_2 $,

$$\begin{aligned}
  & \mathbb{E}\left[ \left( W(t_1) - W(s_1) \right)  \left( W(t_2) - W(s_2) \right) \right] = \\
  & \quad = \mathbb{E}\left[ \left( W(t_1) - W(s_2) + W(s_2) - W(s_1) \right) \left( W(t_2) - W(t_1) + W(t_1) - W(s_2) \right) \right] = \\
  & \quad = \underbrace{\mathbb{E}\left[ \left( W(t_1) - W(s_2) \right) (W(t_2) - W(t_1) ) \right]}_{=0} 
          + \underbrace{\mathbb{E}\left[ \left( W(t_1) - W(s_2) \right) (W(t_1) - W(s_2) ) \right]}_{=|t_1 - s_2|} + \\
  & \quad + \underbrace{\mathbb{E}\left[ \left( W(s_2) - W(s_1) \right) (W(t_2) - W(t_1) ) \right]}_{= 0}  
          + \underbrace{\mathbb{E}\left[ \left( W(s_2) - W(s_1) \right) (W(t_1) - W(s_2) ) \right]}_{= 0} = \\
  & \quad  = 0 + |t_1 - s_2| + 0 = \big| [s_1, t_1] \cap [s_2, t_2] \big| \ . 
\end{aligned}$$

All the other situations can be proved in the same way.

```

```{prf:property} Statistics of maximum

$$P\left( M(t) \ge a  \right) = 2 P \left( W(t) \ge a \right) = 2 - 2 \, \phi\left( \frac{a}{\sqrt{t}} \right) \ ,$$

with 

  $$M(t) = \max_{0 \le \tau \le t} W(\tau)$$

and 

 $$\phi(x) = \int_{y = -\infty}^{x} p_{\mathscr{N}(0,1)}(x) \, dx$$

is the cumulative probability function of a normal distribution $\mathscr{N}(0,1)$.

```

```{dropdown} Proof.

**The second inequality** immediately follows from the very definition of Wiener process with initial conditions $W(0)$,

$$\begin{aligned}
  P \left( W(t) - W(0) \ge a \right) 
  & = P \left( \mathscr{N}(0,t) \ge a \right) = && (1) \\
  & = P \left( \mathscr{N}\left(0, 1 \right) > \frac{a}{\sqrt{t}} \right) = \\
  & = \int_{x=\frac{a}{\sqrt{t}}}^{+\infty} p(y) \, dy = && (2) \\
  & = 1 - \int_{x=-\infty}^{\frac{a}{\sqrt{t}}} p(y) \, dy = 1 - \phi \left( \frac{a}{\sqrt{t}}  \right)
\end{aligned}$$

having used $(1)$ scaling rule for [transformation of probability functions](prob:transformations)... **todo**, and $(2)$ the normalization condition of the probability density $1 = \int_{x = -\infty}^{+\infty} p(x) \, dx$, and the definition of cumulative probability function.

**First inequality.** In order to prove the first inequality, it could be useful to introduce the definition of **stepping time**, $\tau_a$, as the random variable defined as 

$$\tau_a = \min_s \left\{ s: W(s) = a \right\} \ .$$

Using *reflection principle*, it follows

$$\begin{aligned}
 P( M(t) \ge a ) 
 & = && (1) \\
 & = P( M(t) \ge a, W(t) \ge a) + P( M(t) \ge a,  W(t) < a) = && (2) \\
 & = P( W(t) \ge a ) + P( M(t) \ge a,  W(t) - W(\tau_a) < 0) = && (3) \\
 & = P( W(t) \ge a ) + P( M(t) \ge a,  W'(t - \tau_a) < 0) = && (4) \\
 & = P( W(t) \ge a ) + P( M(t) \ge a ) P (  W'(t - \tau_a) < 0) = && (5) \\
 & = P( W(t) \ge a ) + \dfrac{1}{2} P( M(t) \ge a ) \ .
 \end{aligned}$$

haing $(1)$ used "marginalization" to write $P(A) = P(A,B) + P(A, \overline{B})$, $(2)$ recognized that if $B: \, W(t) \ge a$ then $A: \, M(t) \ge a$ or $B \subseteq A$, and thus $P(A,B) = P(B)$, and that $a = W(\tau_a)$, $(3)$ defined the Wiener process $W'(t - \tau_a) := W(t) - W(\tau_a)$, independent from $W(s)$, $0 \le s \le \tau_a$, $(4)$ exploited the independence of the two conditions (**todo** *be more explicit, proof needed?*), $(5)$ and the symmetry of Wiener process to get $P(W'(t-\tau_a) < 0) = \frac{1}{2}$.

Thus, it follows the requied relation

$$P(M(t) \ge a) = 2 P(W(t) \ge a) \ .$$


<!--
From the very nature of a Wiener process it follows that
- $P\left( W(t) - W(s) > 0 \right) = P\left( W(t) - W(s) < 0 \right)$
- $P\left( W(t) - W(\tau_a) > 0 | t > \tau_a \right) = P\left( W(t) - W(\tau_a) < 0 | t > \tau_a \right)$ or equivalently, as $W(\tau_a) = a$,

  $$P\left( W(t) - a > 0 | t > \tau_a \right) = P\left( W(t) - a < 0 | t > \tau_a \right)$$

As the two conditions $M(t) \ge a$ and $t \ge \tau_a$ are equivalent,

$$\begin{aligned}
  P(M(t) \ge a) 
  & = P(t \ge \tau_a) = && (1) \\
  & = P(W(t) \ge a, t \ge \tau) + P(W(t) \le a, t \ge \tau) = && (2) \\
  & = 2 P(W(t) \ge a, t \ge \tau) = && (3) \\
  & = 2 P(W(t) \ge a) \ .
\end{aligned}$$

having $(1)$ written probability as sum of probability of a set of 2 simple disjoint events, $(2)$ used symmetry property, $(3)$ removed the second condition from joint probability
-->

```

```{prf:property} $W(t)$ is almost surely not differentiable

For all time $t$, a Wiener process is almost surely not differentiable, i.e. ...**todo**

```

```{dropdown} Proof.

**todo** *check details*

Wiener process is differentiable in $t$ if the limit 

$$\lim_{h \rightarrow 0} \dfrac{W(t+h) - W(t)}{h} = \ell$$

exists finite. Definition of limit reads,

$$\forall \varepsilon > 0 \quad \exists U_{0,\delta} \quad \text{s.t.} \quad \left| \, \frac{W(t+h) - W(t)}{h} - \ell \, \right| < \varepsilon \qquad \forall h \in U_{0,\delta} \backslash \{ 0 \}$$

**todo** *how to go from this definition to the following one?*

---

Let $E_{\varepsilon, A, t_0}$ be the event s.t. for a given $t_0$, $W(t)$ is differentiable in $t_0$, i.e. $\exists$ $A$, $\varepsilon_0$ const.  s.t. $\forall \varepsilon$ s.t. $0 < \varepsilon < \varepsilon_0$, $W(t) - W(t_0) \le A \varepsilon$ holds for $\forall \varepsilon$, $0 < t - t_0 \le \varepsilon$.

Let $E_{A, t_0} = \cap_{\varepsilon} E_{\varepsilon, A, t_0}$. Then

$$\begin{aligned}
  P\left( E_{\varepsilon, A, t_0} \right) 
  & = P \left( |W(t) - W(t_0)| \le A \varepsilon \text{ for } \forall t-t_0 \text{ s.t. } 0 < t - t_0 \le \varepsilon \right) =  && (1) \\
  & = P \left( M(t - t_0)| \le A \varepsilon \right) = && (2) \\
  & = 1 - P \left( M(t - t_0)| \ge A \varepsilon \right) = && (3) \\
  & = 1 - \left[ 2 - 2 \phi \left( \dfrac{A \varepsilon}{\sqrt{\Delta t}} \right) \right] = \\
  & = - 1 + 2 \phi \left( \dfrac{A \varepsilon}{\sqrt{\Delta t}} \right)  \ ,
\end{aligned}$$

having used $(1)$..., $(2)$..., $(3)$...

Now, being $\varepsilon \le \Delta t$, it follows that $\frac{\varepsilon}{\sqrt{\Delta t}} \le \sqrt{\Delta t}$. As $\varepsilon \rightarrow 0$, then $\frac{\varepsilon}{\sqrt{\Delta t}} \rightarrow 0$, and $\phi\left( \frac{A \varepsilon}{\sqrt{\Delta t}} \right) \rightarrow \frac{1}{2}$, and $P(E_{\varepsilon,A,t_0}) \rightarrow 0$


```

