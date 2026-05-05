(prob:rare-events)=
# Rare Events

This section deals with random variables that can be modelled with probability distributions with tail events that are not that rare, and possibly with extreme outcomes, like natural disasters or terrorist events[^rare-events-terrorists]. These probability distributions have heavy or fat tails, not decaying as fast as tails of a normal distribution do. As a consequence of their very nature, these variables may show some *weird behavior*:
- moments may not exists, or may be infinite: some of these distributions have infinite variance, some have not-defined expected value,...
- results as the [central limit theorem](prob:iid:large-numbers) don't hold, as the required assumptions are not satisfied by these distributions
- ...

[^rare-events-terrorists]: [Estimating the probability of rare events] (https://aaronclauset.github.io/rareevents/), A.~Clauset adn R.~Woodard.

```{admonition} Author's Note
:class: warning

The motivation for writing this section comes from a suggestion by a friend, who pointed me to a [Veritasium video](https://www.youtube.com/watch?v=HBluLfX2F_k&t=1555s). It was something I had been meaning to do for a long time, like many other things, for that matter. However, watching that video provided a concrete opportunity to finally sit down and start writing this section.

It is likely that this section will also draw inspiration from the podcast [*La logica del rischio*](https://www.pasqualecirillo.eu/ldr/) by P. Cirillo, at least as far as the examples are concerned. Since this is a work in progress, more specific references will be added as the work develops.

```

```{dropdown} Contents
:open:

[**Introduction to heavy-tailed distributions.**](prob:rare-events:heavy-tailed)

[**Power-law distributions.**](prob:rare-events:power-law)

```

```{dropdown} References
:open:

- [You've (Likely) Been Playing The Game of Life Wrong](https://www.youtube.com/watch?v=HBluLfX2F_k&t=1555s), Veritasium, YouTube video.
- [La logica del rischio](https://www.pasqualecirillo.eu/ldr/), P.Cirillo.
- [Estimating the probability of rare events](https://aaronclauset.github.io/rareevents/), A.Clauset and R.Woodard.

```
