(prob:rare-events:heavy-tailed)=
# Heavy-tailed distributions

- Does the [CLT](prob:iid:clt) hold for heavy-tailed distributions?

(prob:heavy-tailed:classification)=
## Classification

```{dropdown} Heavy-tailed
:open:

$$\lim_{x\rightarrow+\infty} e^{tx}\overline{F}(x) = \infty \ , \quad \text{for all $t > 0$} \ ,$$

being $\overline{F}(x) :=  \text{P}(X > x)$ the tail cumulative distribution function.

**todo** *alternative definition in terms of moment generating function of $X$*

```


```{dropdown} Long-tailed distribution
:open:

$$\lim_{x \rightarrow + \infty} \text{P}(X > x + t | X > x) = 1 \ ,$$

for all $t > 0$, or equivalently

$$\overline{F}(x+t) \sim \overline{F}(x) \ , \quad \text{for $x\rightarrow +\infty$} \ ,$$

being $\overline{F}(x) :=  \text{P}(X > x)$ the tail cumulative distribution function.

```

```{dropdown} Sub-exponential distribution
:open:

...

```

## Examples

- Cauchy distribution
- Power-law distribution



## References
- [Clauset, Aaron and Woodard, Ryan, "Estimating the historical and future probabilities of large terrorist events." Annals of Applied Statistics 7(4), 1838-1865 (2013).](https://aaronclauset.github.io/rareevents/)
