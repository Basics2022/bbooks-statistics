(ml:intro)=
# Introduction to Machine Learning

Artificial intelligence can be broadly defined as a field dealing with making machines perform tasks that require intelligence, when performed by humans, like: reasoning, perception, representation, language processing, planning, learning

**Machine learning** is a branch of AI focused on statistical algoritms that can **learn from data** and **generalize to unseen data** and perform tasks, without explicit instructions.[^ml-optimization]

[^ml-optimization]: "Without explicit instructions" means that a systems has no user-coded behavior, but learns it usually via **optimization**, usually either involving minimization of an error function or maximization of an objective function or energy/information content.

**Three core paradigms.** Algorithms in machine learning can be divided into three paradigms:

- [**Supervised Learning, SL**](ml:sl): algorithm learns from labelled data; many applications can be reduced to 2 main tasks: **regression** (or function approximation) and **classification**.

- [**Unsupervised Learning, UL**](ml:ul): algorithm learns pattern from un-labelled data; examples of taks in UL are clustering, dimensionality reduction (and recognition of *main* components in data), compression (retaining only relevant components in data). Some historical algorithms and linear algebra decompositions can be interpreted or generalized as unsupervised learning. 

- [**Reinforcement Learning, RL**](ml:rl): an algorithm (**agent**) learns a **policy** - i.e. the way to behave - interacting with an **environment**, and maximizing some performance to efficiently perform required tasks. Applications of RL includes **planning** and **control**.


**Goals and methodology.** ML is mainly a engineering-oriented and an application-focused discipline, relying on statistical inference (**todo** *be more explicit*). A [ML model](ml:models) usually takes an input $\mathbf{u}$, and produces an output $\mathbf{y}$, depending on its own structure and a set of parameters $\boldsymbol{\theta}$ and hyper-parameters $\boldsymbol{\mu}$. Learning usually relies on [**optimization**](https://basics2022.github.io/bbooks-math-miscellanea/ch/optimization/intro.html) of an objective function

$$L(\boldsymbol{\theta}; \boldsymbol{\mu}) \ ,$$

w.r.t. parameters $\boldsymbol{\theta}$, whose value is learned/adjusted towards an optimal solution $\boldsymbol{\theta}^*$ that makes $L(\boldsymbol{\theta}^*; \boldsymbol{\mu})$ extreme. The choice of hyper-parameters $\boldsymbol{\mu}$ instead influences the training process and model behavior. Optimization usually relies on gradient methods, updating the parameters in the direction of the gradient of the objective function w.r.t. the parameters,

$$\boldsymbol{\theta} \ \leftarrow \ \boldsymbol{\theta} + \alpha \nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}; \boldsymbol{\mu}) \ .$$

<!--
Recent development in hardware made feasible the design, construction and tuning of **large-dimensional** models, as the **multi-layered neural networks** used in **Deep learning**.[^deep-learning]
-->

Optimization of model parameters is made fast by the use of **back-propagation** and **automatic differentiation** (AD), which efficiently compute gradients of the cost function with respect to the model’s parameters, and technically feasible for large-dimensional models - as the ones used in multi-layered neural networks, in deep learning[^deep-learning] - by recent hardware improvement. These algorithms are not only feasible but also particularly well-suited (being a major driver for new designs) to modern processing architectures, such as **GPUs** and **TPUs**, that accelerate the large-scale matrix and tensor computations involved in both the forward and backward passes of training.

[^deep-learning]: Deep learning can be roughly defined as that branch of machine learning using multi-layered neural networks, indeed.

**todo** *Show NVIDIA, TSMC revenues*

<!--

| Year | Revenue ($M\$$) |
| ---- | --------------- |
| 2013 |  4280           | 
| 2014 |  4130           |
| 2015 |  4682           |
| 2016 |  5010           |
| 2017 |  6910           |
| 2018 |  9714           |
| 2019 | 11716           |
| 2020 | 10918           |
| 2021 | 16675           |
| 2022 | 26914           |
| 2033 | 26974           |
| 2024 | 60922           |
| 2025 |130497           |

-->

<!--
```{code-cell} python
import plotly.graphic_objects as go

year = [ 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024 ]
revs = [
   4280, 
   4130,
   4682,
   5010,
   6910,
   9714,
  11716,
  10918,
  16675,
  26914,
  26974,
  60922,
 130497
]

fig = go.Figure(data=[go.Bar(x=year, y=revs)])
fig.show()


```
-->

---

**todo** Add references: Bishop,...
