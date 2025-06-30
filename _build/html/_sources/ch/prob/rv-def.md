(prob:rv-def)=
# Definition of stochastic variable

In this section, first a formal definition of a stochastic (or random) variable is provided and then discussed. While the definition may initially appear abstract or esoteric, but their nothing more than an extension of set theory. Understanding concepts such as *probability space*, *$\sigma$-algebra*, *measure*, opens the path to a rigorous approach to probability theory.



```{prf:definition} Random variable
:label: def:rv

Given a **probability space** $(\Omega, \mathcal{F}, \nu)$ and a **measurable space** $(E, \mathcal{E})$, a **random variable** is a measurable function, $X: \Omega \ \rightarrow \ E$.

```

Here, the set $\Omega$ is usually defined as the **event set**, $\mathcal{F}$ is a **$\sigma$-algebra** on $\Omega$, $\nu$ is a **probability measure**; the set $E$ is usually defined as the **set of possible outcomes**, and $\mathcal{E}$ is a **$\sigma$-algebra** on it.

Ok, let's explain now every concept appearing in the definition of a random variable.

```{prf:definition} $\sigma$-algebra
:label: def:sigma-algebra

A $\sigma$-algebra $\mathcal{F}$ on a set $\Omega$, a $\sigma$-algebra is a family of subsets of $\Omega$ that satisfies some properties:
1. $\Omega$ is in the $\sigma$-algebra
2. closure under complementation. Taking any subset of $\Omega$ that belongs to the $\sigma$-algebra, its complent belongs to the $\sigma$-algebra as well
3. closure under countable union. A countable (that can be indexed by integer numbers) union of elements in the $\sigma$-algebra defines an element that belongs to the $\sigma$-algebra

```

```{prf:definition} Measurable space $ (\Omega, \mathcal{F})$
:label: def:measurable-space

```

```{prf:definition} Probability measure $\nu$
:label: def:prob-measure

```

```{prf:definition} Probability space $ (\Omega, \mathcal{F}, \nu)$
:label: def:prob-space

If $(\Omega, \mathcal{F})$ is a measureble space and $\nu$ is a probability measure, then the triplet $(\Omega, \mathcal{F}, \nu)$ is a probability space.

```

```{warning} Event space not coinciding with the power set of events

If event space $\Omega$ doesn't coincide with the power set but it's a subset of it, then it's not guaranteed that such an event space can be used to define a $\sigma$-algebra.

```
