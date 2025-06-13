(ml:sl:theory)=
# SL: theory

Supervised learning can be thought as a **function approximation problem**. Given a set of data 

$$\left\{ (x_i, y_i) \right\}_{i=1:N} \ ,$$

supervised learning can be formulated as the evaluation of a function $\hat{y}(x, \boldsymbol{\theta})$, or a **model**, that *approximates well* the relation between input $x_i$ and output $y_i$,

$$y_i \simeq \hat{y}\left( x_i; \boldsymbol{\theta} \right) \ .$$

Two main tasks of SL can be distinguished on the output of the function: **regression** can be formulated as function approximation with continuous output, while in **classification** the function maps inputs to discrete output/**labels** 

**Learning process** aims at finding values of the parameters $\boldsymbol{\theta}$ (and hyper-parameters $\boldsymbol{\mu}$), that minimize a "prediction" error function, e.g. for a scalar output function,

$$E(\boldsymbol{\theta}) = \dfrac{1}{2} \sum_{i \in D_{Tr}} | \hat{y}(x_i; \boldsymbol{\theta}) - y_i |^2 \ ,$$

being $D_{Tr}$ the set of indices belonging to the *training set*. Minimization usually relies on gradient methods of the error function w.r.t. the parameters $\boldsymbol{\theta}$,

$$\begin{aligned}
  \nabla_{\boldsymbol{\theta}} E(\boldsymbol{\theta}, \mathbf{x}_{Tr}, \mathbf{y}_{Tr}) & = \sum_{i \in D_{Tr}} \left( \hat{y}(x_i; \boldsymbol{\theta}) - y_i \right) \nabla_{\boldsymbol{\theta}} \hat{y}(x_i; \boldsymbol{\theta}) \\
  \boldsymbol{\theta} & \leftarrow \boldsymbol{\theta} - \alpha \nabla_{\boldsymbol{\theta}} E(\boldsymbol{\theta}, \mathbf{x}_{Tr}, \mathbf{y}_{Tr}) \ ,
\end{aligned}$$

with $\alpha$ an hyper-parameter called *learning rate*, governing the "length" of the update step.
Other objective functions to be maximised or minimized can be used. Slight variations to objective functions allow for regularization (e.g. parameter weighting)

**Dataset.** Available data $\{ x_i, y_i \}_i$ is divided in different sets:
- training set: for learning/tuning model parameters, minimizing an error function
- validation set: for early stopping, and hyper-parameter tuning (e.g. to avoid 
- test set: to evaluate model performance


