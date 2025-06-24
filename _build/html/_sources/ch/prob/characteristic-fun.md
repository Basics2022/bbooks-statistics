(prob:characteristic-fun)=
# Characteristic functions

Characteristic function of a random variable $X$ is defined as

$$\varphi_X(t) := \mathbb{E} \left[ e^{i t X} \right] \ .$$

Characteristic function of a continuous random variable with proabibility density function $f(x)$ thus reads

$$\varphi_X(t) := \mathbb{E} \left[ e^{i t X} \right] = \int_{x \in D_x} f(x) e^{i t x} \, dx \ ,$$

i.e. its the [**Fourier transform**](https://basics2022.github.io/bbooks-math-miscellanea/ch/complex/fourier-transform.html#fourier-transform) of its pdf.

```{prf:example} Characteristic function of a multi-dimensional variable
:label: ex:char-fun:multidimensional

$$Z(\mathbf{Y})$$

$$\varphi_{Z(\mathbf{Y})} := \mathbb{E}\left[ e^{i t Z(\mathbf{Y})} \right] = \int_{\mathbf{y}} e^{i t Z(\mathbf{y})} f(\mathbf{y}) \, d \mathbf{y}$$

```
```{prf:example} Characteristic function of a linear combination of independent variables
:label: ex:char-fun:independent

$$Z(\mathbf{Y}) = a_1 Y_1 + \dots a_n Y_n \ ,$$

with 

$$f(\mathbf{y}) = f(y_1, \dots, y_n) =  f_1(y_1) \dots f_n(y_n) \ .$$

$$\begin{aligned}
  \varphi_{Z(\mathbf{Y})} 
  & := \mathbb{E}\left[ e^{i t Z(\mathbf{Y})} \right] = \\
  & = \int_{\mathbf{y}} e^{i t \left( \sum_k a_k y_k \right)} f(\mathbf{y}) \, d \mathbf{y} = \\
  & = \int_{y_1} e^{i t a_1 y_1} f_1(y_1) \, d y_1 \, \dots \int_{y_n} e^{i t a_n y_n} f_n(y_n) \, d y_n = \\
  & = \varphi_{Y_1}(a_1 t) \dots \varphi_{Y_n}(a_n t) \ . 
\end{aligned}$$

```

```{prf:example}  Taylor expansion of characteristic function
:label: ex:char-fun:taylor

For "small" values of $t$, an approximation of the characteristic function is provided by Taylor expansion around $t=0$,

$$\begin{aligned}
\int e^{ i y t } f(y) \, dy 
& = \int \left[ 1 + i y t - \dfrac{1}{2} (yt)^2 + o(t^2) \right] f(y) dy = && (1) \\
& = 1 + i \mu t - \dfrac{1}{2} t^2 \left( \sigma^2 + \mu^2 \right) + o(t^2)
\end{aligned}$$

as $(1)$ $\sigma^2 = \mathbb{E}[(y - \mu)^2] = \mathbb{E}[y^2] - \mu^2$

```

```{prf:example} Characteristic function of a normal distribution $\mathscr{N}(0,1)$
:label: ex:char-fun:normal

$$f(x) = \dfrac{1}{\sqrt{2 \pi}} \exp\left( -\dfrac{x^2}{2} \right)$$

$$\begin{aligned}
\int_{x=-\infty}^{+\infty} e^{ i x t } f(x) \, dx
& = \dfrac{1}{\sqrt{2 \pi}} \int_{x=-\infty}^{+\infty} e^{ i x t - \frac{x^2}{2} }  \, dx = && (1)  \\
& = \dfrac{1}{\sqrt{2 \pi}} \int_{x=-\infty}^{+\infty} e^{ - \frac{(x-it)^2}{2} }  \, dx \, e^{-\frac{t^2}{2}} = && (2)  \\
& = \dfrac{1}{\sqrt{2 \pi}} \, \sqrt{2 \pi} \, e^{-\frac{t^2}{2}} = e^{-\frac{t^2}{2}}  \\
\end{aligned}$$

having $(1)$ completed the square $(x - it)^2 = x^2 - i 2 x t - t^2$, and evaluated the integral **todo** (it's similar to the standard result $\int_{-\infty}^{+\infty} e^{x^2} \, dx = \sqrt{2 \pi}$, but with complex variable. Link to math material, complex calculus).

```

