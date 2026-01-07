![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

# **LIMITS AND DERIVATIVES**

v*With the Calculus as a key, Mathematics can be successfully applied to the explanation of the course of Nature – WHITEHEAD* v

# **12.1 Introduction**

This chapter is an introduction to Calculus. Calculus is that branch of mathematics which mainly deals with the study of change in the value of a function as the points in the domain change. First, we give an intuitive idea of derivative (without actually defining it). Then we give a naive definition of limit and study some algebra of limits. Then we come back to a definition of derivative and study some algebra of derivatives. We also obtain derivatives of certain standard functions.

# **12.2 Intuitive Idea of Derivatives**

Physical experiments have confirmed that the body dropped from a tall cliff covers a distance of 4.9*t* <sup>2</sup> metres in *t* seconds,

i.e., distance *s* in metres covered by the body as a function of time *t* in seconds is given by *s* = 4.9*t* 2 *.*

The adjoining Table 13.1 gives the distance travelled in metres at various intervals of time in seconds of a body dropped from a tall cliff.

The objective is to find the veloctiy of the body at time *t* = 2 seconds from this data. One way to approach this problem is to find the average velocity for various intervals of time ending at *t* = 2 seconds and hope that these throw some light on the velocity at *t* = 2 seconds.

Average velocity between *t* = *t* 1 and *t = t<sup>2</sup>* equals distance travelled between *t = t<sup>1</sup>* and *t = t2* seconds divided by (*t* 2 – *t* 1 )*.* Hence the average velocity in the first two seconds

![](_page_0_Picture_12.jpeg)

**Sir Issac Newton (1642-1727)**

| =<br>=<br>Distance travelled between<br>t<br>2<br>and t<br>0          | Table 12.1 |          |  |
|-----------------------------------------------------------------------|------------|----------|--|
| 2<br>1<br>=<br>−<br>Time<br>interval (<br>t<br>t<br>)                 | t          | s        |  |
| 2<br>1                                                                | 0          | 0        |  |
| −<br>19.6<br>0<br>m<br>(<br>)                                         | 1          | 4.9      |  |
| =<br>9.8<br>m<br>/<br>s<br>=<br>)<br>−<br>2<br>0<br>s<br>(            | 1.5        | 11.025   |  |
| Similarly, the average velocity between t = 1                         | 1.8        | 15.876   |  |
| and t = 2 is                                                          | 1.9        | 17.689   |  |
|                                                                       | 1.95       | 18.63225 |  |
| 19.6 – 4.9<br>m<br>(<br>)<br>= 14.7 m/s                               | 2          | 19.6     |  |
| )<br>−<br>2<br>1<br>s<br>(                                            | 2.05       | 20.59225 |  |
| Likewise we compute the average velocitiy                             | 2.1        | 21.609   |  |
| between t = t<br>and t = 2 for various t<br>. The following<br>1<br>1 | 2.2        | 23.716   |  |
| Table 13.2 gives the average velocity (v), t = t<br>1                 | 2.5        | 30.625   |  |
| seconds and t = 2 seconds.                                            | 3          | 44.1     |  |

| Table 12.2 |
|------------|
|------------|

4 78.4

| t<br>1 | 0   | 1    | 1.5   | 1.8   | 1.9   | 1.95   | 1.99   |
|--------|-----|------|-------|-------|-------|--------|--------|
| v      | 9.8 | 14.7 | 17.15 | 18.62 | 19.11 | 19.355 | 19.551 |

From Table 12.2, we observe that the average velocity is gradually increasing. As we make the time intervals ending at *t* = 2 smaller, we see that we get a better idea of the velocity at *t* = 2. Hoping that nothing really dramatic happens between 1.99 seconds and 2 seconds, we conclude that the average velocity at *t* = 2 seconds is just above 19.551*m*/*s*.

This conclusion is somewhat strengthened by the following set of computation. Compute the average velocities for various time intervals starting at *t* = 2 seconds. As before the average velocity *v* between *t* = 2 seconds and *t* = *t* 2 seconds is

> = 2 2 Distance travelled between 2 seconds and seconds 2 *t t* − = <sup>2</sup> Distance travelled in seconds Distance travelled in 2 seconds 2 *t t* − −

2

= <sup>2</sup> 2 Distance travelled in seconds 19.6 2 *t t* − −

The following Table 12.3 gives the average velocity *v* in metres per second between *t* = 2 seconds and *t* 2 seconds.

| t<br>2 | 4    | 3    | 2.5   | 2.2   | 2.1   | 2.05   | 2.01   |
|--------|------|------|-------|-------|-------|--------|--------|
| v      | 29.4 | 24.5 | 22.05 | 20.58 | 20.09 | 19.845 | 19.649 |

**Table 12.3**

Here again we note that if we take smaller time intervals starting at *t* = 2, we get better idea of the velocity at *t* = 2.

In the first set of computations, what we have done is to find average velocities in increasing time intervals ending at *t* = 2 and then hope that nothing dramatic happens just before *t* = 2. In the second set of computations, we have found the average velocities decreasing in time intervals ending at *t* = 2 and then hope that nothing dramatic happens just after *t* = 2. Purely on the physical grounds, both these sequences of average velocities must approach a common limit. We can safely conclude that the velocity of the body at *t* = 2 is between 19.551*m/s* and 19.649 *m/s*. Technically, we say that the instantaneous velocity at *t* = 2 is between 19.551 *m/s* and 19.649 *m/s*. As is well-known, *velocity is the rate of change of displacement*. Hence what we have accomplished is the following. From the given data of distance covered at various time

instants we have estimated the rate of change of the distance at a given instant of time. We say that the *derivative* of the distance function *s* = 4.9*t* 2 at *t* = 2 is between 19.551 and 19.649.

An alternate way of viewing this limiting process is shown in Fig 12.1. This is a plot of distance *s* of the body from the top of the cliff versus the time *t* elapsed. In the limit as the sequence of time intervals *h*<sup>1</sup> , *h*<sup>2</sup> , ..., approaches zero, the sequence of average velocities approaches the same limit as does the sequence of ratios **Fig 12.1**

![](_page_2_Figure_9.jpeg)

$$\frac{\mathbf{C}\_1 \mathbf{B}\_1}{\mathbf{A} \mathbf{C}\_1}, \frac{\mathbf{C}\_2 \mathbf{B}\_2}{\mathbf{A} \mathbf{C}\_2}, \frac{\mathbf{C}\_3 \mathbf{B}\_3}{\mathbf{A} \mathbf{C}\_3}, \dots$$

where C1B<sup>1</sup> = *s* 1 – *s* 0 is the distance travelled by the body in the time interval *h*<sup>1</sup> = AC<sup>1</sup> , etc. From the Fig 12.1 it is safe to conclude that this latter sequence approaches the slope of the tangent to the curve at point A. In other words, the instantaneous velocity *v*(*t*) of a body at time *t* = 2 is equal to the slope of the tangent of the curve *s* = 4.9*t* 2 at *t* = 2.

## **12.3 Limits**

The above discussion clearly points towards the fact that we need to understand limiting process in greater clarity. We study a few illustrative examples to gain some familiarity with the concept of limits.

Consider the function *f*(*x*) = *x* 2 *.* Observe that as *x* takes values very close to 0, the value of *f*(*x*) also moves towards 0 (See Fig 2.10 Chapter 2). We say

$$\lim\_{x \to 0} f\left(x\right) = 0$$

(to be read as limit of *f*(*x*) as *x* tends to zero equals zero). The limit of *f*(*x*) as *x* tends to zero is to be thought of as the value *f* (*x*) should assume at *x =* 0.

In general as *x* → *a*, *f* (*x*) → *l*, then *l* is called *limit of the function f* (*x*) which is symbolically written as lim ( ) *x a f x l* → = .

Consider the following function *g*(*x*) = |*x*|, *x* ≠ 0. Observe that *g*(0) is not defined. Computing the value of *g*(*x*) for values of *x* very

near to 0, we see that the value of *g*(*x*) moves towards 0. So, <sup>0</sup> lim *x*→  *g*(*x*) = 0. This is intuitively clear from the graph of *y* = |*x*| for *x* ≠ 0. (See Fig 2.13, Chapter 2).

Consider the following function.

$$h(x) = \frac{x^2 - 4}{x - 2}, \; x \neq 2\dots$$

Compute the value of *h*(*x*) for values of *x* very near to 2 (but not at 2). Convince yourself that all these values are near to 4. This is somewhat strengthened by considering the graph of the function *y* = *h*(*x*) given here (Fig 12.2). **Fig 12.2**

![](_page_3_Figure_14.jpeg)

In all these illustrations the value which the function should assume at a given point *x* = *a* did not really depend on how is *x* tending to *a.* Note that there are essentially two ways *x* could approach a number *a* either from left or from right, i.e., all the values of *x* near *a* could be less than *a* or could be greater than *a.* This naturally leads to two limits – the *right hand limit* and the *left hand limit*. *Right hand limit* of a function *f*(*x*) is that value of *f*(*x*) which is dictated by the values of *f*(*x*) when *x* tends to *a* from the right. Similarly, the *left hand limit*. To illustrate this, consider the function

$$f\left(\mathbf{x}\right) = \begin{cases} 1, & \mathbf{x} \le \mathbf{0} \\ 2, & \mathbf{x} > \mathbf{0} \end{cases}$$

Graph of this function is shown in the Fig 12.3. It is clear that the value of *f* at 0 dictated by values of *f*(*x*) with *x* ≤ 0 equals 1, i.e., the left hand limit of *f* (*x*) at 0 is

$$\lim\_{x \to \overline{0}} f(x) = 1$$

Similarly, the value of *f* at 0 dictated by values of *f* (*x*) with *x* > 0 equals 2, i.e., the right hand limit of *f* (*x*) at 0 is

$$\lim\_{x \to 0^{+}} f\left(x\right) = 2\left.\right|$$

**Fig 12.3**

In this case the right and left hand limits are different, and hence we say that the limit of *f* (*x*) as *x* tends to zero does not exist (even though the function is defined at 0).

## *Summary*

 We say lim *x a* <sup>→</sup> **–** *f*(*x*) is the expected value of *f* at *x* = *a* given the values of *f* near *x* to the left of *a*. This value is called the *left hand limit* of *f* at *a*.

We say lim ( ) *x a f x* → <sup>+</sup> is the expected value of *f* at *x* = *a* given the values of

*f* near *x* to the right of *a*. This value is called the *right hand limit* of *f*(*x*) at *a*.

If the right and left hand limits coincide, we call that common value as the limit

of *f*(*x*) at *x* = *a* and denote it by lim *x a* → *f*(*x*).

**Illustration 1** Consider the function *f*(*x*) = *x* + 10. We want to find the limit of this function at *x* = 5. Let us compute the value of the function *f*(*x*) for *x* very near to 5. Some of the points near and to the left of 5 are 4.9, 4.95, 4.99, 4.995. . ., etc. Values of the function at these points are tabulated below. Similarly, the real number 5.001, 5.01, 5.1 are also points near and to the right of 5. Values of the function at these points are also given in the Table 12.4.

| x    | 4.9  | 4.95  | 4.99  | 4.995  | 5.001  | 5.01  | 5.1  |
|------|------|-------|-------|--------|--------|-------|------|
| f(x) | 14.9 | 14.95 | 14.99 | 14.995 | 15.001 | 15.01 | 15.1 |

**Table 12.4**

From the Table 12.4, we deduce that value of *f*(*x*) at *x =* 5 should be greater than 14.995 and less than 15.001 assuming nothing dramatic happens between *x =* 4.995 and 5.001. It is reasonable to assume that the value of the *f*(*x*) at *x* = 5 as dictated by the numbers to the left of 5 is 15, i.e.,

$$\lim\_{x \to \mathcal{S}^-} f(x) = 1 \,\mathsf{S}\_{\cdot \cdot}$$

Similarly, when *x* approaches 5 from the right, *f*(*x*) should be taking value 15, i.e.,

$$\lim\_{x \to S^{+}} f(x) = 1S^{-}.$$

Hence, it is likely that the left hand limit of *f*(*x*) and the right hand limit of *f*(*x*) are both equal to 15. Thus,

$$\lim\_{x \to \mathcal{S}^-} \mathcal{J}(x) = \lim\_{x \to \mathcal{S}^+} \mathcal{J}(x) = \lim\_{x \to \mathcal{S}^0} \mathcal{J}(x) = 1 \mathcal{S}\_{\dots}$$

This conclusion about the limit being equal to 15 is somewhat strengthened by seeing the graph of this function which is given in Fig 2.16, Chapter 2. In this figure, we note that as *x* approaches 5 from either right or left, the graph of the function *f*(*x*) *= x* +10 approaches the point (5, 15).

We observe that the value of the function at *x =* 5 also happens to be equal to 15.

**Illustration 2** Consider the function *f*(*x*) *= x*<sup>3</sup> . Let us try to find the limit of this function at *x =* 1. Proceeding as in the previous case, we tabulate the value of *f*(*x*) at *x* near 1. This is given in the Table 12.5.

| x    | 0.9   | 0.99     | 0.999       | 1.001       | 1.01     | 1.1   |
|------|-------|----------|-------------|-------------|----------|-------|
| f(x) | 0.729 | 0.970299 | 0.997002999 | 1.003003001 | 1.030301 | 1.331 |

| Table 12.5 |  |
|------------|--|
|------------|--|

From this table, we deduce that value of *f*(*x*) at *x* = 1 should be greater than 0.997002999 and less than 1.003003001 assuming nothing dramatic happens between *x =* 0.999 and 1.001. It is reasonable to assume that the value of the *f*(*x*) at *x =* 1 as dictated by the numbers to the left of 1 is 1, i.e.,

$$\lim\_{\mathbf{x}\to\mathbf{l}^-}f(\mathbf{x}) = 1\_{\mathbf{\cdot}}$$

Similarly, when *x* approaches 1 from the right, *f*(*x*)should be taking value 1, i.e.,

$$\lim\_{x \to 1^{+}} f(x) = 1\_{-}$$

Hence, it is likely that the left hand limit of *f*(*x*) and the right hand limit of *f*(*x*) are both equal to 1. Thus,

$$\lim\_{x \to 1^{-}} \mathcal{f}(x) = \lim\_{x \to 1^{+}} \mathcal{f}(x) = \lim\_{x \to 1} \mathcal{f}(x) = 1\_{\cdot}$$

This conclusion about the limit being equal to 1 is somewhat strengthened by seeing the graph of this function which is given in Fig 2.11, Chapter 2. In this figure, we note that as *x* approaches 1 from either right or left, the graph of the function *f*(*x*) *= x*<sup>3</sup>approaches the point (1, 1).

We observe, again, that the value of the function at *x* = 1 also happens to be equal to 1.

**Illustration 3** Consider the function *f*(*x*) *=* 3*x*. Let us try to find the limit of this function at *x* = 2. The following Table 12.6 is now self-explanatory.

| x    | 1.9<br>1.95 | 1.99 | 1.999 | 2.001 | 2.01 | 2.1 |
|------|-------------|------|-------|-------|------|-----|
| f(x) | 5.7<br>5.85 | 5.97 | 5.997 | 6.003 | 6.03 | 6.3 |

**Table 12.6**

As before we observe that as *x* approaches 2 from either left or right, the value of *f*(*x*) seem to approach 6. We record this as

$$\lim\_{x \to 2^{-}} f(x) = \lim\_{x \to 2^{+}} f(x) = \lim\_{x \to 2} f(x) = 6$$

Its graph shown in Fig 12.4 strengthens this fact.

Here again we note that the value of the function at *x* = 2 coincides with the limit at *x* = 2.

**Illustration 4** Consider the constant function *f*(*x*) = 3. Let us try to find its limit at *x =* 2. This function being the constant function takes the same **Fig 12.4**

![](_page_6_Figure_17.jpeg)

value (3, in this case) everywhere, i.e., its value at points close to 2 is 3. Hence

$$\lim\_{x \to \frac{\pi}{2}} f\left(x\right) = \lim\_{x \to 2^{+}} f\left(x\right) = \lim\_{x \to 2} f\left(x\right) = 3$$

Graph of *f*(*x*) *=* 3 is anyway the line parallel to *x*-axis passing through (0, 3) and is shown in Fig 2.9, Chapter 2. From this also it is clear that the required limit is 3. In fact, it is easily observed that lim 3 ( ) *x a f x* → = for any real number *a*.

**Illustration 5** Consider the function *f*(*x*) *= x*<sup>2</sup>  *+ x*. We want to find ( ) 1 lim *x f x* → . We tabulate the values of *f*(*x*) near *x =* 1 in Table 12.7.

| Table 12.7 |      |        |          |        |      |      |
|------------|------|--------|----------|--------|------|------|
| x          | 0.9  | 0.99   | 0.999    | 1.01   | 1.1  | 1.2  |
| f(x)       | 1.71 | 1.9701 | 1.997001 | 2.0301 | 2.31 | 2.64 |

**Fig 12.5**

From this it is reasonable to deduce that

$$\lim\_{x \to 1^{-}} f(x) = \lim\_{x \to 1^{+}} f(x) = \lim\_{x \to 1} f(x) = 2$$

From the graph of *f*(*x*) *= x*<sup>2</sup> + *x* shown in the Fig 12.5, it is clear that as *x* approaches 1, the graph approaches (1, 2).

Here, again we observe that the

$$\lim\_{x \to 1^{-}} f(x) = f(1)$$

Now, convince yourself of the following three facts:

$$\lim\_{x \to 1} x^2 = 1, \quad \lim\_{x \to 1} x = 1 \text{ and } \lim\_{x \to 1} x + 1 = 2$$

$$\text{Then } \qquad \lim\_{x \to 1} x^2 + \lim\_{x \to 1} x = 1 + 1 = 2 = \lim\_{x \to 1} \left[ x^2 + x \right].$$

$$\text{Also } \qquad \lim\_{x \to 1} x. \quad \lim\_{x \to 1} \left( x + 1 \right) = 1.\\ 2 = 2 = \lim\_{x \to 1} \left[ x \left( x + 1 \right) \right] = \lim\_{x \to 1} \left[ x^2 + x \right].$$

**Illustration 6** Consider the function *f*(*x*) = sin *x.* We are interested in 2 lim sin *x x* <sup>π</sup> <sup>→</sup> ,

where the angle is measured in radians.

Here, we tabulate the (approximate) value of *f*(*x*) near <sup>2</sup> π (Table 12.8)*.* From this, we may deduce that

$$\lim\_{\mathfrak{x}\to\frac{\pi}{2}^-}f\left(\mathfrak{x}\right) = \lim\_{\mathfrak{x}\to\frac{\pi}{2}^+}f\left(\mathfrak{x}\right) = \lim\_{\mathfrak{x}\to\frac{\pi}{2}}f\left(\mathfrak{x}\right) = 1$$

Further, this is supported by the graph of *f*(*x*) *=* sin *x* which is given in the Fig 3.8 (Chapter 3). In this case too, we observe that lim *x* <sup>π</sup> <sup>→</sup> sin *x* = 1.

.

2

**Table 12.8**

| x    | π      | π      | π      | π      |
|------|--------|--------|--------|--------|
|      | −      | −      | +      | +      |
|      | 0.1    | 0.01   | 0.01   | 0.1    |
|      | 2      | 2      | 2      | 2      |
| f(x) | 0.9950 | 0.9999 | 0.9999 | 0.9950 |

**Illustration 7** Consider the function *f*(*x*) = *x* + cos *x*. We want to find the 0 lim *x*→ *f* (*x*).

Here we tabulate the (approximate) value of *f*(*x*) near 0 (Table 12.9).

**Table 12.9**

| x    | – 0.1  | – 0.01  | – 0.001   | 0.001     | 0.01    | 0.1    |
|------|--------|---------|-----------|-----------|---------|--------|
| f(x) | 0.9850 | 0.98995 | 0.9989995 | 1.0009995 | 1.00995 | 1.0950 |

From the Table 13.9, we may deduce that

$$\lim\_{\mathfrak{x}\to 0^{-}} f\left(\mathfrak{x}\right) = \lim\_{\mathfrak{x}\to 0^{+}} f\left(\mathfrak{x}\right) = \lim\_{\mathfrak{x}\to 0} f\left(\mathfrak{x}\right) = 1$$

In this case too, we observe that 0 lim *x*→ *f* (*x*) = *f* (0) = 1.

Now, can you convince yourself that

[ ] 0 0 0 lim cos lim lim cos *x x x x x x x* → → → + = + is indeed true? **Illustration 8** Consider the function ( ) <sup>2</sup> 1 *f x x* = for *x* > 0 . We want to know 0 lim *x*→ *f* (*x*).

Here, observe that the domain of the function is given to be all positive real numbers. Hence, when we tabulate the values of *f*(*x*)*,* it does not make sense to talk of *x* approaching 0 from the left. Below we tabulate the values of the function for positive *x* close to 0 (in this table *n* denotes any positive integer).

From the Table 12.10 given below, we see that as *x* tends to 0, *f*(*x*) becomes larger and larger. What we mean here is that the value of *f*(*x*) may be made larger than any given number.

| Table 12.10 |  |  |
|-------------|--|--|
|-------------|--|--|

| x    | 1 | 0.1 | 0.01  | 10–n |
|------|---|-----|-------|------|
| f(x) | 1 | 100 | 10000 | 102n |

Mathematically, we say

( ) 0 lim *x f x* → = +∞

We also remark that we will not come across such limits in this course.

**Illustration 9** We want to find ( ) 0 lim *x f x* → , where

$$f'(x) = \begin{cases} \infty - 2, & x < 0 \\ 0 - 1, & x = 0 \\ \infty + 2, & \infty > 0 \end{cases}$$

As usual we make a table of *x* near 0 with *f*(*x*)*.* Observe that for negative values of *x* we need to evaluate *x* – 2 and for positive values, we need to evaluate *x* + 2.

**Table 12.11**

| x    | – 0.1 | – 0.01 | – 0.001 | 0.001 | 0.01 | 0.1 |
|------|-------|--------|---------|-------|------|-----|
| f(x) | – 2.1 | – 2.01 | – 2.001 | 2.001 | 2.01 | 2.1 |

From the first three entries of the Table 12.11, we deduce that the value of the function is decreasing to –2 and hence.

$$\lim\_{x \to 0^{-}} f\left(x\right) = -2$$

**Fig 12.6**

From the last three entires of the table we deduce that the value of the function is increasing from 2 and hence

$$\lim\_{x \to 0^{+}} f\left(x\right) = 2$$

Since the left and right hand limits at 0 do not coincide, we say that the limit of the function at 0 does not exist.

 Graph of this function is given in the Fig12.6. Here, we remark that the value of the function at *x* = 0 is well defined and is, indeed, equal to 0, but the limit of the function at *x* = 0 is not even defined.

**Illustration 10** As a final illustration, we find ( ) 1 lim *x f x* → , where

$$f'(x) = \begin{cases} x + 2 & x \neq 1 \\ 0 & x = 1 \end{cases}$$

![](_page_10_Figure_7.jpeg)

| x    | 0.9 | 0.99 | 0.999 | 1.001 | 1.01 | 1.1 |
|------|-----|------|-------|-------|------|-----|
| f(x) | 2.9 | 2.99 | 2.999 | 3.001 | 3.01 | 3.1 |

As usual we tabulate the values of *f*(*x*) for *x* near 1. From the values of *f*(*x*) for *x* less than 1, it seems that the function should take value 3 at *x* = 1., i.e.,

$$\lim\_{x \to 1^{-}} f\left(x\right) = 3\underbrace{\dots}\_{-}$$

Similarly, the value of *f*(*x*)should be 3 as dictated by values of *f*(*x*) at *x* greater than 1. i.e.

$$\lim\_{x \to 1^+} f(x) = 3\dots$$

But then the left and right hand limits coincide and hence

$$\lim\_{x \to 1^{-}} f\left(x\right) = \lim\_{x \to 1^{+}} f\left(x\right) = \lim\_{x \to 1} f\left(x\right) = \mathfrak{Z}\_{-}$$

Graph of function given in Fig 12.7 strengthens our deduction about the limit. Here, we

![](_page_10_Figure_16.jpeg)

note that in general, at a given point the value of the function and its limit may be different (even when both are defined).

**12.3.1** *Algebra of limits* In the above illustrations, we have observed that the limiting process respects addition, subtraction, multiplication and division as long as the limits and functions under consideration are well defined. This is not a coincidence. In fact, below we formalise these as a theorem without proof.

**Theorem 1** Let *f* and *g* be two functions such that both lim *x a* →  *f*(*x*) and lim *x a* → *g*(*x*) exist.

Then

(i) Limit of sum of two functions is sum of the limits of the functions, i.e.,

$$\lim\_{x \to a} \left[ f(x) + \operatorname{g}(x) \right] = \lim\_{x \to a} f(x) + \lim\_{x \to a} \operatorname{g}(x).$$

(ii) Limit of difference of two functions is difference of the limits of the functions, i.e.,

$$\lim\_{x \to a} \left[ f(x) - g(x) \right] = \lim\_{x \to a} f(x) - \lim\_{x \to a} g(x),$$

(iii) Limit of product of two functions is product of the limits of the functions, i.e.,

$$\lim\_{x \to a} \text{ [f(x) . g(x)]} = \lim\_{x \to a} f(x) . \lim\_{x \to a} g(x).$$

(iv) Limit of quotient of two functions is quotient of the limits of the functions (whenever the denominator is non zero), i.e.,

$$\lim\_{x \to a} \frac{f(x)}{\operatorname{g}(x)} = \frac{\lim\_{x \to a} f(x)}{\lim\_{x \to a} \operatorname{g}(x)}$$

A**Note** In particular as a special case of (iii), when *g* is the constant function such that *g*(*x*) = <sup>λ</sup> *,* for some real number <sup>λ</sup> , we have

$$\lim\_{x \to a} \underline{\left[ \left( \lambda. f \right) \left( x \right) \right]} = \lambda. \lim\_{x \to a} f \left( x \right)\_{.}$$

In the next two subsections, we illustrate how to exploit this theorem to evaluate limits of special types of functions.

**12.3.2** *Limits of polynomials and rational functions* A function *f* is said to be a polynomial function of degree *n f*(*x*) = *a<sup>0</sup>* + *a*<sup>1</sup> *x* + *a*<sup>2</sup> *x* <sup>2</sup> +. . . + *a<sup>n</sup> x n* , where *a*<sup>i</sup> *s* are real numbers such that *a<sup>n</sup>* ≠ 0 for some natural number *n.*

We know that lim *x a* → *x* = *a*. Hence

$$\lim\_{x \to a} x^2 = \lim\_{x \to a} (x.x) = \lim\_{x \to a} x. \lim\_{x \to a} x = a. \, a = a^2$$

An easy exercise in induction on *n* tells us that

$$\lim\_{x \to a} x^n = a^m$$

Now, let ( ) 2 0 1 2 ... *n n f x a a x a x a x* = + + + + be a polynomial function. Thinking of each of <sup>2</sup> 0 1 2 , , ,..., *n n a a x a x a x* as a function, we have

$$\lim\_{x \to a} f\left(x\right) = \lim\_{x \to a} \left[ a\_0 + a\_1 x + a\_2 x^2 + \dots + a\_n x^n \right]$$

$$= \lim\_{x \to a} a\_0 + \lim\_{x \to a} a\_1 x + \lim\_{x \to a} a\_2 x^2 + \dots + \lim\_{x \to a} a\_n x^n$$

$$= a\_0 + a\_1 \lim\_{x \to a} x + a\_2 \lim\_{x \to a} x^2 + \dots + a\_n \lim\_{x \to a} x^n$$

$$= a\_0 + a\_1 a + a\_2 a^2 + \dots + a\_n a^n$$

$$= f\left(a\right)$$

(Make sure that you understand the justification for each step in the above!)

A function *f* is said to be a rational function, if *f*(*x*) = ( ) ( ) *g x h x* , where *g*(*x*) and *h*(*x*) are polynomials such that *h*(*x*) ≠ 0. Then

$$\lim\_{x \to a} \mathcal{J}(x) = \lim\_{x \to a} \frac{\mathbf{g}\left(x\right)}{h\left(x\right)} = \frac{\lim\_{x \to a} \mathbf{g}\left(x\right)}{\lim\_{x \to a} h\left(x\right)} = \frac{\mathbf{g}\left(a\right)}{h\left(a\right)}$$

However, if *h*(*a*) = 0, there are two scenarios – (i) when *g*(*a*) ≠ 0 and (ii) when *g*(*a*) = 0. In the former case we say that the limit does not exist. In the latter case we can write *g*(*x*) = (*x* – *a*) *<sup>k</sup>g*1 (*x*), where *k* is the maximum of powers of (*x* – *a*) in *g*(*x*) Similarly, *h*(*x*) = (*x* – *a*) *l h*1 (*x*) as *h* (*a*) = 0. Now, if *k* > *l,* we have

$$\lim\_{x \to a} f\left(x\right) = \frac{\lim\_{x \to a} g\left(x\right)}{\lim\_{x \to a} h\left(x\right)} = \frac{\lim\_{x \to a} \left(x - a\right)^k g\_1\left(x\right)}{\lim\_{x \to a} \left(x - a\right)^l h\_1\left(x\right)}$$

$$=\frac{\lim\_{x\to a} (x-a)^{(k-l)}\operatorname{g}\_1(x)}{\lim\_{x\to a} h\_1(x)} = \frac{0.\operatorname{g}\_1(a)}{h\_1(a)} = 0$$

If *k* < *l,* the limit is not defined.

**Example 1** Find the limits: (i) 3 2 1 lim 1 *x x x* → − + (ii) ( ) 3 lim 1 *x x x* → + (iii) 2 10 1 lim 1 ... *x x x x* →− + + + + .

**Solution** The required limits are all limits of some polynomial functions. Hence the limits are the values of the function at the prescribed points. We have

= − + + = 1 1 1... 1 1.

- (i) <sup>1</sup> lim *x*→ [*x* <sup>3</sup> – *x* <sup>2</sup> + 1] = 1<sup>3</sup> – 1<sup>2</sup> + 1 = 1
- (ii) ( ) ( ) ( ) 3 lim 1 3 3 1 3 4 12 *x x x* → + = + = =
- (iii) 2 10 1 lim 1 ... *x x x x* →− + + + + ( ) ( ) ( ) <sup>2</sup> <sup>10</sup> = + − + − + + − 1 1 1 ... 1

**Example 2** Find the limits:

$$\begin{array}{ll} \text{(i)} & \lim\_{x \to 1} \left[ \frac{x^2 + 1}{x + 100} \right] \\\\ \text{(ii)} & \lim\_{x \to 2} \left[ \frac{x^2 - 4}{x^3 - 4x^2 + 4x} \right] \\\\ \text{(v)} & \lim\_{x \to 1} \left[ \frac{x - 2}{x^2 - 4x} - \frac{1}{x^3 - 3x^2 + 2x} \right] \end{array} \qquad \text{(iv)} \quad \lim\_{x \to 2} \left[ \frac{x^3 - 2x^2}{x^2 - 5x + 6} \right]$$

**Solution** All the functions under consideration are rational functions. Hence, we first evaluate these functions at the prescribed points. If this is of the form 0 0 , we try to rewrite the function cancelling the factors which are causing the limit to be of the form 0 0 .

.

.

.

$$\text{(i)}\quad\text{We have }\lim\_{\mathbf{x}\to\mathbf{1}}\frac{\mathbf{x}^2+1}{\mathbf{x}+100} = \frac{\mathbf{1}^2+1}{1+100} = \frac{2}{101}$$

(ii) Evaluating the function at 2, it is of the form 0 0 .

$$\begin{aligned} \text{Hence} \quad \lim\_{x \to 2} \frac{x^3 - 4x^2 + 4x}{x^2 - 4} &= \lim\_{x \to 2} \frac{x(x - 2)^2}{(x + 2)(x - 2)} \\ &= \lim\_{x \to 2} \frac{x(x - 2)}{(x + 2)} & \text{as } x \neq 2 \\\\ &= \frac{2(2 - 2)}{2 + 2} = \frac{0}{4} = 0. \end{aligned}$$

(iii) Evaluating the function at 2, we get it of the form 0 0

$$\begin{aligned} \text{Hence } \lim\_{x \to 2} \frac{x^2 - 4}{x^3 - 4x^2 + 4x} &= \lim\_{x \to 2} \frac{(x+2)(x-2)}{x(x-2)} \\ &= \lim\_{x \to 2} \frac{\left(x+2\right)}{x\left(x-2\right)} = \frac{2+2}{2\left(2-2\right)} = \frac{4}{0} \end{aligned}$$

which is not defined.

(iv) Evaluating the function at 2, we get it of the form 0 0

$$\begin{aligned} \text{Hence} \qquad \lim\_{x \to 2} \frac{x^3 - 2x^2}{x^2 - 5x + 6} &= \lim\_{x \to 2} \frac{x^2 \{x - 2\}}{\{x - 2\} \{x - 3\}} \\ &= \lim\_{x \to 2} \frac{x^2}{\{x - 3\}} = \frac{\binom{2}{2}^2}{2 - 3} = \frac{4}{-1} = -4 \end{aligned}$$

(v) First, we rewrite the function as a rational function.

$$
\left[\frac{\mathbf{x}-2}{\mathbf{x}^2-\mathbf{x}} - \frac{1}{\mathbf{x}^3-3\mathbf{x}^2+2\mathbf{x}}\right] = \left[\frac{\mathbf{x}-2}{\mathbf{x}(\mathbf{x}-1)} - \frac{1}{\mathbf{x}(\mathbf{x}^2-3\mathbf{x}+2)}\right]
$$

$$
= \left[\frac{\mathbf{x}-2}{\mathbf{x}(\mathbf{x}-1)} - \frac{1}{\mathbf{x}(\mathbf{x}-1)(\mathbf{x}-2)}\right]
$$

$$
= \left[\frac{\mathbf{x}^2-4\mathbf{x}+4-1}{\mathbf{x}(\mathbf{x}-1)(\mathbf{x}-2)}\right]
$$

$$
= \frac{\mathbf{x}^2-4\mathbf{x}+3}{\mathbf{x}(\mathbf{x}-1)(\mathbf{x}-2)}
$$

Evaluating the function at 1, we get it of the form 0 0 .

$$\begin{aligned} \text{Hence} \quad \lim\_{x \to 1} \left[ \frac{x^2 - 2}{x^2 - x} - \frac{1}{x^3 - 3x^2 + 2x} \right] &= \lim\_{x \to 1} \frac{x^2 - 4x + 3}{x(x - 1)(x - 2)} \\ \left( \begin{array}{c} \bigvee \\ \end{array} \right) &= \lim\_{x \to 1} \frac{(x - 3)(x - 1)}{x(x - 1)(x - 2)} \\ &= \lim\_{x \to 1} \frac{x - 3}{x(x - 2)} = \frac{1 - 3}{1(1 - 2)} = 2. \end{aligned}$$

We remark that we could cancel the term (*x* – 1) in the above evaluation because *x* ≠ 1 .

Evaluation of an important limit which will be used in the sequel is given as a theorem below.

**Theorem 2** For any positive integer *n,*

$$\lim\_{\mathbf{x}\to a} \frac{\mathbf{x}^n - a^n}{\mathbf{x} - a} = na^{n-1}$$

*.*

*Remark* The expression in the above theorem for the limit is true even if *n* is any rational number and *a* is positive.

**Proof** Dividing (*x n* – *a n )* by (*x* – *a),* we see that

$$\begin{aligned} \mathbf{x}^n - a^n &= (\mathbf{x} - a) \ (\mathbf{x}^{n-1} + \mathbf{x}^{n-2} \ a + \mathbf{x}^{n-3} \ a^2 + \dots + \mathbf{x} \ \mathbf{a}^{n-2} + a^{n-1}) \\\\ \text{Thus, } \lim\_{\mathbf{x} \to a} \frac{\mathbf{x}^n - a^n}{\mathbf{x} - a} &= \lim\_{\mathbf{x} \to a} \left( \mathbf{x}^{n-1} + \mathbf{x}^{n-2} \ a + \mathbf{x}^{n-3} \ a^2 + \dots + \mathbf{x} \ \mathbf{a}^{n-2} + a^{n-1} \right) \\\\ &= a^{n-1} + a \ \mathbf{a}^{n-2} + \dots + a^{n-2} \ (\mathbf{a}) \ \ \mathbf{+} a^{n-1} \\\\ &= a^{n-1} + a^{n-1} + \dots + a^{n-1} + a^{n-1} \ (\mathbf{n} \text{ terms}) \\\\ &= n a^{n-1} \end{aligned}$$

**Example 3** Evaluate:

$$\text{(i)}\quad\lim\_{\mathbf{x}\to\mathbf{1}}\frac{\mathbf{x}^{\text{IS}}-1}{\mathbf{x}^{\text{I}0}-1}\tag{ii)}\quad\text{(ii)}\quad\lim\_{\mathbf{x}\to\mathbf{0}}\frac{\sqrt{1+\mathbf{x}}-1}{\mathbf{x}}$$

**Solution** (i) We have

$$\lim\_{x \to 1} \frac{x^{15} - 1}{x^{10} - 1} = \lim\_{x \to 1} \left[ \frac{x^{15} - 1}{x - 1} + \frac{x^{10} - 1}{x - 1} \right]$$

$$= \lim\_{x \to 1} \left[ \frac{x^{15} - 1}{x - 1} \right] + \lim\_{x \to 1} \left[ \frac{x^{10} - 1}{x - 1} \right]$$

$$= 15 \cdot (1)^{14} + 10 \cdot (1)^9 \quad \text{(by the theorem above)}$$

$$= 15 + 10 = \frac{3}{2}$$

$$\text{(ii): Put } y = 1 + x, \text{ so that } y \to 1 \text{ as } x \to 0.$$

$$\text{Then } \lim\_{x \to 0} \frac{\sqrt{1 + x - 1}}{x} = \lim\_{y \to 1} \frac{\sqrt{y - 1}}{y - 1}$$

$$= \lim\_{y \to 1} \frac{\frac{1}{y^2} - \frac{1}{2}}{y - 1}$$

$$= \frac{1}{2} (0)^{\frac{1}{2} - 1} \quad \text{(by the remark above)} = -\frac{1}{2}$$

*x a* →

*x a* →

## **12.4 Limits of Trigonometric Functions**

*x a* →

The following facts (stated as theorems) about functions in general come in handy in calculating limits of some trigonometric functions.

**Theorem 3** Let *f* and *g* be two real valued functions with the same domain such that

*f* (*x*) ≤ g( *x*) for all *x* in the domain of definition, For some *a,* if both lim *x a* →  *f*(*x*) and lim  *g*(*x*) exist, then lim  *f*(*x*) ≤ lim  *g*(*x*). This is illustrated in Fig 12.8.

*x a* →

![](_page_17_Figure_5.jpeg)

**Theorem 4 (Sandwich Theorem)** Let *f,* g and *h* be real functions such that *f*(*x*) ≤ *g*( *x*) ≤ *h*(*x*) for all *x* in the common domain of definition. For some real number *a*, if lim  *f*(*x*) = *l* = lim  *h*(*x*), then lim  *g*(*x*) = *l.* This is illustrated in Fig 12.9.

![](_page_17_Figure_7.jpeg)

Given below is a beautiful geometric proof of the following important inequality relating trigonometric functions.

$$
\cos x < \frac{\sin x}{x} < 1 \qquad \text{for} \quad 0 < |x| < \frac{\pi}{2} \tag{\*}
$$

**Proof** We know that sin (– *x*) = – sin *x* and cos( *– x*) = cos *x.* Hence, it is sufficient to prove the inequality for π 0 2 < <*x* .

In the Fig 12.10, O is the centre of the unit circle such that

the angle AOC is *x* radians and 0 < *x* < π 2 . Line segments B A and

CD are perpendiculars to OA*.* Further, join AC. Then

Area of ∆OAC < Area of sector OAC < Area of ∆ OAB.

![](_page_18_Figure_6.jpeg)

**Fig 12.10**

$$\text{i.e.}, \quad \frac{1}{2} \text{OA.CD} < \frac{\varkappa}{2\pi}.\\\pi.(\text{OA})^2 < \frac{1}{2} \text{OA.AB}\_{-}.$$

i.e., CD < *x* . OA < AB.

From ∆ OCD,

sin *x* = CD OA (since OC = OA) and hence CD = OA sin *x.* Also tan *x* <sup>=</sup> AB OA and

hence AB = OA*.* tan *x*. Thus OA sin *x* < OA*. x* < OA*.* tan *x*.

Since length OA is positive, we have

sin *x* < *x* < tan *x*.

Since 0 < *x* < π 2 , sin*x* is positive and thus by dividing throughout by sin *x,* we have

1< 1 sin cos *x x x* < . Taking reciprocals throughout, we have

$$
\cos x < \frac{\sin x}{x} < 1
$$

which complete the proof.

**Theorem 5** The following are two important limits.

$$\text{(i)}\ \lim\_{\mathbf{x}\to\mathbf{0}} \frac{\sin\mathbf{x}}{\mathbf{x}} = \mathbf{l}\ .\qquad\qquad\qquad\text{(ii)}\ \lim\_{\mathbf{x}\to\mathbf{0}} \frac{1-\cos\mathbf{x}}{\mathbf{x}} = \mathbf{0}\ .$$

**Proof** (i) The inequality in (\*) says that the function sin *<sup>x</sup> x* is sandwiched between the function cos *x* and the constant function which takes value 1.

*x*

Further, since <sup>0</sup> lim *x*→ cos *x* = 1, we see that the proof of (i) of the theorem is complete by sandwich theorem.

To prove (ii), we recall the trigonometric identity 1 – cos *x* = 2 sin<sup>2</sup> 2 *x* .

Then

$$\lim\_{x \to 0} \frac{1 - \cos x}{x} = \lim\_{x \to 0} \frac{2 \sin^2 \left(\frac{x}{2}\right)}{x} = \lim\_{x \to 0} \frac{\sin \left(\frac{x}{2}\right)}{\frac{x}{2}} \cdot \sin \left(\frac{x}{2}\right)$$

$$= \lim\_{x \to 0} \frac{\sin \left(\frac{x}{2}\right)}{\frac{x}{2}} \cdot \lim\_{x \to 0} \sin \left(\frac{x}{2}\right) = 1.0 = 0$$

Observe that we have implicitly used the fact that *x* → 0 is equivalent to 0 2 *x* → . This

may be justified by putting *y* = <sup>2</sup> *x*

$$\begin{aligned} \text{Example 4 Evaluate:} \qquad & \text{(i)} \lim\_{x \to 0} \frac{\sin 4x}{\sin 2x} \qquad & \text{(ii)} \lim\_{x \to 0} \frac{\tan x}{x} \\\\ \text{Solution (i)} \qquad & \lim\_{x \to 0} \frac{\sin 4x}{\sin 2x} = \lim\_{x \to 0} \left[ \frac{\sin 4x}{4x} \cdot \frac{2x}{\sin 2x} . \right] \\\\ & = 2 \lim\_{x \to 0} \left[ \frac{\sin 4x}{4x} \right] \div \left[ \frac{\sin 2x}{2x} \right] \\\\ & = 2 \lim\_{4x \to 0} \left[ \frac{\sin 4x}{4x} \right] \div \lim\_{2x \to 0} \left[ \frac{\sin 2x}{2x} \right] \\\\ & = 2 \cdot 1 \cdot 2 \quad (\text{as } x \to 0, \, 4x \to 0 \text{ and } 2x \to 0) \end{aligned}$$

.

#### Reprint 2025-26

$$\text{(ii) We have } \lim\_{\mathbf{x} \to 0} \frac{\tan \mathbf{x}}{\mathbf{x}} = \lim\_{\mathbf{x} \to 0} \frac{\sin \mathbf{x}}{\mathbf{x} \cos \mathbf{x}} = \lim\_{\mathbf{x} \to 0} \frac{\sin \mathbf{x}}{\mathbf{x}} \cdot \lim\_{\mathbf{x} \to 0} \frac{1}{\cos \mathbf{x}} = 1.1 = 1$$

A general rule that needs to be kept in mind while evaluating limits is the following.

Say, given that the limit ( ) ( ) lim *x a f x* <sup>→</sup> *g x* exists and we want to evaluate this. First we check

the value of *f* (*a*) and *g*(*a*). If both are 0, then we see if we can get the factor which is causing the terms to vanish, i.e., see if we can write *f*(*x*) = *f* 1 (*x*) *f* 2 (*x*) so that *f* 1 (*a*) = 0 and *f* 2 (*a*) ≠ 0. Similarly, we write *g*(*x*) = *g*<sup>1</sup> (*x*) *g*<sup>2</sup> (*x*), where *g*<sup>1</sup> (*a*) = 0 and *g*2 (*a*) ≠ 0. Cancel out the common factors from *f*(*x*) and *g*(*x*) (if possible) and write

$$\frac{f(\mathbf{x})}{\mathbf{g}(\mathbf{x})} = \frac{p(\mathbf{x})}{q(\mathbf{x})} \text{, where } q(\mathbf{x}) \neq 0.$$

Then

( ) ( ) ( ) ( ) lim *x a f x p a* <sup>→</sup> *g x q a* = .

**EXERCISE 12.1**

Evaluate the following limits in Exercises 1 to 22.

**1.** <sup>3</sup> lim 3 *x x* → + **2.** π <sup>22</sup> lim *<sup>x</sup>* 7 *x* → <sup>−</sup> **3.** 2 1 limπ *r r* → **4.** 4 4 3 lim *<sup>x</sup>* 2 *x* <sup>→</sup> *x* + − **5.** 10 5 1 1 lim *<sup>x</sup>* 1 *x x* → − *x* + + − **6.** ( )<sup>5</sup> 0 1 1 lim *x x* <sup>→</sup> *x* + − **7.** 2 2 2 3 10 lim *<sup>x</sup>* 4 *x x* <sup>→</sup> *x* − − − **8.** 4 2 3 <sup>81</sup> lim *<sup>x</sup>* 2 5 3 *x* <sup>→</sup> *x x* − − − **9.** 0 lim *<sup>x</sup>* 1 *ax b* <sup>→</sup> *cx* + + **10.** 1 3 1 1 6 1 lim 1 *z z z* → − − **11.** 2 2 1 lim , 0 *x ax bx c a b c* <sup>→</sup> *cx bx a* + + + + ≠ + + **12.** 2 1 1 2 lim *<sup>x</sup>* 2 *x* →− *x* + + **13.** 0 sin lim *x ax* <sup>→</sup> *bx* **14.** 0 sin lim , , 0 *<sup>x</sup>* sin *ax a b* <sup>→</sup> *bx* ≠

**15.** ( ) ( ) <sup>π</sup> sin π lim *<sup>x</sup>* π π *x* <sup>→</sup> *x* − − **16.** 0 cos lim *<sup>x</sup>* π *x* <sup>→</sup> − *x* **17.** 0 cos 2 1 lim *<sup>x</sup>* cos 1 *x* <sup>→</sup> *x* − − **18.** 0 cos lim *<sup>x</sup>* sin *ax x x* <sup>→</sup> *b x* + **19.** <sup>0</sup> lim sec *x x x* → **20.** 0 sin lim , , 0 *<sup>x</sup>* sin *ax bx a b a <sup>b</sup>* <sup>→</sup> *ax bx* + + ≠ + , **21.** <sup>0</sup> lim (cosec cot ) *x x x* → − **22.** <sup>π</sup> 2 tan 2 lim π 2 *x x* <sup>→</sup> *x* − **23.** Find ( ) 0 lim *x f x* → and ( ) 1 lim *x f x* → , where ( ) ( ) 2 3, 0 3 1 , 0 *x x f x x x* + ≤ = + > **24.** Find ( ) 1 lim *x f x* → , where ( ) 2 2 1, 1 1, 1 *x x f x x x* − ≤ = − − > **25.** Evaluate ( ) 0 lim *x f x* → , where ( ) | | , 0 0, 0 *x x f x x x* ≠ = = **26.** Find ( ) 0 lim *x f x* → , where ( ) , 0 | | 0, 0 *x x f x x x* ≠ = = **27.** Find ( ) 5 lim *x f x* → , where *f x x* ( ) = − | | 5 **28.** Suppose ( ) , 1 4, 1 , 1 *a bx x f x x b ax x* + < = = − >

and if 1 lim *x*→ *f* (*x*) = *f* (1) what are possible values of *a* and *b*? **29.** Let *a*<sup>1</sup> , *a*<sup>2</sup> , . . ., *a<sup>n</sup>* be fixed real numbers and define a function

*f x x a x a x a* ( ) = − − − ( 1 2 ) ( )...( *<sup>n</sup>* ) .

What is 1 lim *x a* → *f* (*x*) ? For some *a* ≠ *a*<sup>1</sup> *, a*<sup>2</sup> *, ..., a<sup>n</sup>* , compute lim*x a* <sup>→</sup> *f* (*x*).

$$\mathbf{30}. \quad \text{If} \quad f(\mathbf{x}) = \begin{cases} \|\mathbf{x}\| + 1, & \mathbf{x} < \mathbf{0} \\ \mathbf{0}, & \mathbf{x} = \mathbf{0} \\ \|\mathbf{x}\| - 1, & \mathbf{x} > \mathbf{0} \end{cases}.$$

For what value (s) of *a* does lim *x a* → *f* (*x*) exists?

**31.** If the function *f(x)* satisfies ( ) 2 1 2 lim π *<sup>x</sup>* 1 *f x* <sup>→</sup> *x* − = − , evaluate ( ) 1 lim *x f x* → .

$$\text{32.} \quad \text{If } f\left(\mathbf{x}\right) = \begin{cases} m\mathbf{x}^2 + n, & \mathbf{x} < \mathbf{0} \\ m\mathbf{x} + m, & \mathbf{0} \le \mathbf{x} \le \mathbf{1} \\ m\mathbf{x}^3 + m, & \mathbf{x} > \mathbf{1} \end{cases}. \text{ For what integers } m \text{ and } n \text{ does both } \lim\_{x \to \mathbf{0}} f\left(\mathbf{x}\right).$$

and ( ) 1 lim *x f x* → exist?

## **12.5 Derivatives**

We have seen in the Section 13.2, that by knowing the position of a body at various time intervals it is possible to find the rate at which the position of the body is changing. It is of very general interest to know a certain parameter at various instants of time and try to finding the rate at which it is changing. There are several real life situations where such a process needs to be carried out. For instance, people maintaining a reservoir need to know when will a reservoir overflow knowing the depth of the water at several instances of time, Rocket Scientists need to compute the precise velocity with which the satellite needs to be shot out from the rocket knowing the height of the rocket at various times. Financial institutions need to predict the changes in the value of a particular stock knowing its present value. In these, and many such cases it is desirable to know how a particular parameter is changing with respect to some other parameter. The heart of the matter is derivative of a function at a given point in its domain of definition.

**Definition 1** *Suppose f is a real valued function and a is a point in its domain of definition. The derivative of f at a is defined by*

$$\lim\_{h \to 0} \frac{f\left(a+h\right) - f\left(a\right)}{h}$$

*provided this limit exists. Derivative of f* (*x*) *at a is denoted by f*′(*a*)*.*

Observe that *f*′(*a*) quantifies the change in *f*(*x*) at *a* with respect to *x.*

**Example 5** Find the derivative at *x* = 2 of the function *f*(*x*) = 3*x.*

**Solution** We have

$$f'(2) = \lim\_{h \to 0} \frac{f\left(2+h\right) - f\left(2\right)}{h} = \lim\_{h \to 0} \frac{3\left(2+h\right) - 3\left(2\right)}{h}$$

$$= \lim\_{h \to 0} \frac{6+3h-6}{h} = \lim\_{h \to 0} \frac{3h}{h} = \lim\_{h \to 0} 3 = 3$$

The derivative of the function 3*x* at *x* = 2 is 3.

**Example 6** Find the derivative of the function *f*(*x*) = 2*x* <sup>2</sup> + 3*x* – 5 at *x* = –1. Also prove that *f* ′ (0) + 3*f* ′ ( –1) = 0.

**Solution** We first find the derivatives of *f*(*x*) at *x* = –1 and at *x* = 0. We have

$$f^\*(-1) = \lim\_{h \to 0} \frac{f\left(-1 + h\right) - \hat{f}\left(-1\right)}{h}$$

$$= \lim\_{h \to 0} \frac{2\left(-1 + h\right)^2 + 3\left(-1 + h\right) - 5}{h} \left[ 2\left(-1\right)^2 + 3\left(-1\right) - 5 \right]$$

$$= \lim\_{h \to 0} \frac{2h^2 - h}{h} = \lim\_{h \to 0} \left(2h - 1\right) = 2\left(0\right) - 1 = -1$$
 and 
$$f^\*(0) = \lim\_{h \to 0} \frac{f\left(0 + h\right) - f\left(0\right)}{h}$$

$$= \lim\_{h \to 0} \left[ 2\left(0 + h\right)^2 + 3\left(0 + h\right) - 5\right] - \left[2\left(0\right)^2 + 3\left(0\right) - 5\right]$$

<sup>→</sup> *h*

0

*h*

$$\mathfrak{l} = \lim\_{h \to 0} \frac{2h^2 + 3h}{h} = \lim\_{h \to 0} \left(2h + 3\right) = 2\left(0\right) + 3 = 3$$

Clearly *f f* ' 0 3 ' 1 0 ( ) + − = ( )

*Remark* At this stage note that evaluating derivative at a point involves effective use of various rules, limits are subjected to. The following illustrates this.

**Example 7** Find the derivative of sin *x* at *x* = 0.

$$\begin{aligned} \text{Solution} \quad & \text{Let } f(\mathbf{x}) = \sin \mathbf{x}. \text{ Then} \\ & f'(0) = \lim\_{h \to 0} \frac{f\left(0 + h\right) - f\left(0\right)}{h} \\ &= \lim\_{h \to 0} \frac{\sin\left(0 + h\right) - \sin\left(0\right)}{h} = \lim\_{h \to 0} \frac{\sin h}{h} = 1 \stackrel{\circ}{\quad} \text{or} \end{aligned}$$

**Example 8** Find the derivative of *f*(*x*) = 3 at *x* = 0 and at *x* = 3.

**Solution** Since the derivative measures the change in function, intuitively it is clear that the derivative of the constant function must be zero at every point. This is indeed, supported by the following computation.

$$f'(0) = \lim\_{h \to 0} \frac{f\left(0 + h\right) - f\left(0\right)}{h} = \lim\_{h \to 0} \frac{3 - 3}{h} = \lim\_{h \to 0} \frac{0}{h} = 0$$
 
$$\text{Similarly} \qquad f'(3) = \lim\_{h \to 0} \frac{f\left(3 + h\right) - f\left(3\right)}{h} = \lim\_{h \to 0} \frac{3 - 3}{h} = 0$$

We now present a geometric interpretation of derivative of a function at a point. Let *y* = *f*(*x*) be a function and let P = (*a*, *f*(*a*)) and Q = (*a* + *h*, *f*(*a* + *h*) be two points close to each other on the graph of this function. The Fig 12.11 is now self explanatory.

![](_page_24_Figure_11.jpeg)

We know that ( ) ( ) ( ) 0 lim *h f a h f a f a* <sup>→</sup> *h* + − ′ =

From the triangle PQR, it is clear that the ratio whose limit we are taking is precisely equal to tan(QPR) which is the slope of the chord PQ. In the limiting process, as *h* tends to 0, the point Q tends to P and we have

$$\lim\_{h \to 0} \frac{f\left(a+h\right) - f\left(a\right)}{h} = \lim\_{Q \to \mathbb{P}} \frac{\text{QR}}{\text{PR}}$$

This is equivalent to the fact that the chord PQ tends to the tangent at P of the curve *y* = *f*(*x*). Thus the limit turns out to be equal to the slope of the tangent. Hence

$$f'(a) = \tan\Psi\dots$$

For a given function *f* we can find the derivative at every point. If the derivative exists at every point, it defines a new function called the derivative of *f .* Formally, we define derivative of a function as follows.

**Definition 2** *Suppose f is a real valued function, the function defined by*

$$\lim\_{h \to 0} \frac{f\left(x+h\right) - f\left(x\right)}{h}$$

*wherever the limit exists is defined to be the derivative of f at x and is denoted by f*′(*x*)*. This definition of derivative is also called the first principle of derivative.*

$$\text{Thus } \qquad f'(x) = \lim\_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

Clearly the domain of definition of *f*′ (*x*) is wherever the above limit exists. There are different notations for derivative of a function. Sometimes *f*′(*x*) is denoted by

( ) ( ) *<sup>d</sup> f x dx* or if *y* = *f*(*x*)*,* it is denoted by *dy dx* . This is referred to as derivative of *f*(*x*) or *y* with respect to *x.* It is also denoted by D (*f* (*x*) ). Further, derivative of *f* at *x = a*

$$\text{is also defined by } \frac{d}{d\mathfrak{x}} f(\mathfrak{x}) \Big|\_{a} \text{ or } \frac{df}{d\mathfrak{x}} \Big|\_{a} \text{ or even} \\ \Big( \frac{df}{d\mathfrak{x}} \Big)\_{\mathfrak{x} = a}.$$

**Example 9** Find the derivative of *f(x)* = 10*x.*

$$\text{Solution Since } f' \text{ ( $x$ )} = \lim\_{h \to 0} \frac{f \left(x + h\right) - f \left(x \right)}{h}$$

$$=\lim\_{h\to 0} \frac{10\left(\mathbf{x} + h\right) - 10\left(\mathbf{x}\right)}{h}$$

$$=\lim\_{h\to 0} \frac{10h}{h} = \lim\_{h\to 0} \left(10\right) = 10\left(\right)$$

**Example 10** Find the derivative of *f*(*x*) = *x* 2 *.*

$$\text{Solution We have}, f'(\mathbf{x}) \, = \lim\_{h \to 0} \frac{f\left(\mathbf{x} + h\right) - f\left(\mathbf{x}\right)}{h}$$

$$= \lim\_{h \to 0} \frac{\left(\mathbf{x} + h\right)^2 - \left(\mathbf{x}\right)^2}{h} = \lim\_{h \to 0} \left(h + 2\mathbf{x}\right) = 2\mathbf{x}$$

**Example 11** Find the derivative of the constant function *f* (*x*) = *a* for a fixed real number *a*.

$$\begin{aligned} \text{Solution We have,} &f'(\mathbf{x}) = \lim\_{h \to 0} \frac{f\left(\mathbf{x} + h\right) - f\left(\mathbf{x}\right)}{h} \\ &= \lim\_{h \to 0} \frac{a - a}{h} = \lim\_{h \to 0} \frac{0}{h} = 0 \quad \text{as } h \neq 0 \end{aligned}$$

**Example 12** Find the derivative of *f*(*x*) = 1 *x*

$$\text{Solution We have } f'(x) = \lim\_{h \to 0} \frac{f\left(x+h\right) - f\left(x\right)}{h}$$

$$=\lim\_{h\to 0} \frac{1}{\frac{(x+h)}{h}} - \frac{1}{x}$$

$$=\lim\_{h\to 0} \frac{1}{h} \left[\frac{x - (x+h)}{x(x+h)}\right]$$

$$=\lim\_{h\to 0} \frac{1}{h} \left[\frac{-h}{x(x+h)}\right] \qquad \qquad =\lim\_{h\to 0} \frac{-1}{x(x+h)} = -\frac{1}{x^2}$$

**12.5.1** *Algebra of derivative of functions* Since the very definition of derivatives involve limits in a rather direct fashion, we expect the rules for derivatives to follow closely that of limits. We collect these in the following theorem.

**Theorem 5** Let *f* and *g* be two functions such that their derivatives are defined in a common domain. Then

(i) Derivative of sum of two functions is sum of the derivatives of the functions.

$$\frac{d}{d\mathbf{x}}[f(\mathbf{x}) + \mathbf{g}(\mathbf{x})] = \frac{d}{d\mathbf{x}}f(\mathbf{x}) + \frac{d}{d\mathbf{x}}\mathbf{g}(\mathbf{x}) \dots$$

(ii) Derivative of difference of two functions is difference of the derivatives of the functions.

*.*

$$\frac{d}{d\mathbf{x}}[\int f(\mathbf{x}) - \mathbf{g}(\mathbf{x})] = \frac{d}{d\mathbf{x}}f(\mathbf{x}) - \frac{d}{d\mathbf{x}}\mathbf{g}(\mathbf{x})$$

(iii) Derivative of product of two functions is given by the following *product rule.*

$$\frac{d}{d\mathbf{x}}[f(\mathbf{x})\,\,\,\,\mathbf{g}(\mathbf{x})] = \frac{d}{d\mathbf{x}}f(\mathbf{x})\,\,\,\mathbf{g}(\mathbf{x}) + f(\mathbf{x})\,\,\frac{d}{d\mathbf{x}}\mathbf{g}(\mathbf{x})\,\,\,$$

(iv) Derivative of quotient of two functions is given by the following *quotient rule* (whenever the denominator is non–zero).

$$\frac{d}{d\mathbf{x}}\left(\frac{f(\mathbf{x})}{\mathbf{g}(\mathbf{x})}\right) = \frac{\frac{d}{d\mathbf{x}}f(\mathbf{x})\text{.}\mathbf{g}(\mathbf{x}) - f(\mathbf{x})\text{.}\frac{d}{d\mathbf{x}}\mathbf{g}(\mathbf{x})}{\left(\mathbf{g}(\mathbf{x})\right)^{2}}$$

The proofs of these follow essentially from the analogous theorem for limits. We will not prove these here. As in the case of limits this theorem tells us how to compute derivatives of special types of functions. The last two statements in the theorem may be restated in the following fashion which aids in recalling them easily:

$$\text{Let } \mathfrak{u} = f(\mathfrak{x}) \text{ and } \mathfrak{v} = \mathfrak{g} \text{ (x). Then}$$

$$\left(\mu\nu\right)' = \stackrel{\cdot}{\mu}\nu + \mu\nu'$$

This is referred to a Leibnitz rule for differentiating product of functions or the product rule. Similarly, the quotient rule is

$$\left(\frac{u}{\nu}\right)' = \frac{u'\nu - \mu\nu'}{\nu^2}$$

Now, let us tackle derivatives of some standard functions. It is easy to see that the derivative of the function *f*(*x*) = *x* is the constant

$$\text{function 1. This is because } f'(x) = \lim\_{h \to 0} \frac{f\left(x+h\right) - f\left(x\right)}{h} = \lim\_{h \to 0} \frac{x+h-x}{h}$$

$$= \lim\_{h \to 0} 1 = 1$$

We use this and the above theorem to compute the derivative of *f*(*x*) = 10*x* = *x* + .... + *x* (ten terms). By (*i*) of the above theorem

$$\frac{df(\mathbf{x})}{d\mathbf{x}} = \frac{d}{d\mathbf{x}} \text{ ( $\mathbf{x} + \dots + \mathbf{x}$ ) (ten terms)}$$

$$= \frac{d}{d\mathbf{x}} \mathbf{x}^{\text{+}} \dots + \frac{d}{d\mathbf{x}} \mathbf{x} \quad \text{(ten terms)}$$

$$= (1 + \dots + 1 \quad \text{(ten terms)} = 1 \,\mathrm{0}.$$

We note that this limit may be evaluated using product rule too. Write *f*(*x*) = 10*x* = *uv*, where *u* is the constant function taking value 10 everywhere and *v*(*x*) = *x*. Here, *f*(*x*) = 10*x* = *uv* we know that the derivative of *u* equals 0. Also derivative of *v*(*x*) = *x* equals 1. Thus by the product rule we have

$$f'(\mathbf{x}) \stackrel{\frown}{=} \begin{pmatrix} 10\,\mathbf{x} \\ \mathbf{0} \end{pmatrix} = \begin{pmatrix} \mu \boldsymbol{\nu} \end{pmatrix} \stackrel{\frown}{=} \boldsymbol{\mu}' \boldsymbol{\nu} + \boldsymbol{\mu} \boldsymbol{\nu}' = \mathbf{0}.\mathbf{x} + 10.1 = 10$$

On similar lines the derivative of *f*(*x*) = *x* <sup>2</sup> may be evaluated. We have *f*(*x*) = *x* <sup>2</sup> = *x .x* and hence

$$\begin{aligned} \frac{d f}{d \mathbf{x}} &= \frac{d}{d \mathbf{x}} (\mathbf{x}.\mathbf{x}) = \frac{d}{d \mathbf{x}} (\mathbf{x}).\mathbf{x} + \mathbf{x}.\frac{d}{d \mathbf{x}} (\mathbf{x}) \\ &= \begin{bmatrix} 1.\mathbf{x} + \mathbf{x}.1 = 2\mathbf{x} \end{bmatrix}.\end{aligned}$$

More generally, we have the following theorem.

**Theorem 6** Derivative of *f*(*x*) = *x n* is *nxn* – 1 for any positive integer *n.*

**Proof** By definition of the derivative function, we have

$$f'(\mathbf{x}) = \lim\_{h \to 0} \frac{f\left(\mathbf{x} + h\right) - f\left(\mathbf{x}\right)}{h} = \lim\_{h \to 0} \frac{\left(\mathbf{x} + h\right)^n - \mathbf{x}^n}{h}.$$

Binomial theorem tells that (*x* + *h*) *<sup>n</sup>* = ( ) ( ) ( ) <sup>1</sup> C C ... C 0 1 *n n n n n n n x x h h* − + + + and hence (*x* + *h*) *<sup>n</sup>* – *x <sup>n</sup>* = *h*(*nx<sup>n</sup>*– 1 +... + *h <sup>n</sup>*– 1)*.* Thus

$$\frac{df(\mathbf{x})}{d\mathbf{x}} = \lim\_{h \to 0} \frac{\left(\mathbf{x} + h\right)^n - \mathbf{x}^n}{h}$$

$$= \lim\_{h \to 0} \frac{h\left(n\mathbf{x}^{n-1} + ... + h^{n-1}\right)}{h}$$

$$= \lim\_{h \to 0} \left(n\mathbf{x}^{n-1} + ... + h^{n-1}\right) = \lim\_{h \to 0} n^{n-1}$$

Alternatively, we may also prove this by induction on *n* and the product rule as follows. The result is true for *n* = 1, which has been proved earlier. We have

− .

$$\begin{split} \frac{d}{dx} \left( \mathbf{x}^{n} \right) &= \frac{d}{dx} \Big( \mathbf{x} \mathbf{x}^{n-1} \Big) \\ &= \frac{d}{dx} \Big( \mathbf{x} \big). \Big( \mathbf{x}^{n-1} \big) + \mathbf{x} \frac{d}{dx} \Big( \mathbf{x}^{n-1} \big) \text{ (by product rule)} \\ &= 1 \ \mathbf{x}^{n-1} + \mathbf{x} \big( \big( n-1 \big) \mathbf{x}^{n-2} \big) \text{ (by induction hypothesis)} \\ &= \mathbf{x}^{n-1} + \left( n-1 \right) \mathbf{x}^{n-1} = n \mathbf{x}^{n-1} . \end{split}$$

*Remark* The above theorem is true for all powers of *x,* i.e., *n* can be any real number (but we will not prove it here).

**12.5.2** *Derivative of polynomials and trigonometric functions* We start with the following theorem which tells us the derivative of a polynomial function.

**Theorem 7** Let *f(x)* = <sup>1</sup> <sup>1</sup> 1 0 .... *n n n n a x a x a x a* <sup>−</sup> + + + + <sup>−</sup> be a polynomial function, where *ai s* are all real numbers and *a<sup>n</sup>* ≠ 0. Then, the derivative function is given by

$$\frac{d f^\circ(\mathbf{x})}{d\mathbf{x}} = n a\_n \mathbf{x}^{n-1} + \left(n - 1\right) a\_{n-1} \mathbf{x}^{n-2} + \dots + \left(2a\_2 \mathbf{x} + a\_1 \dots\right)$$

Proof of this theorem is just putting together part (i) of Theorem 5 and Theorem 6. **Example 13** Compute the derivative of 6*x* 100 – *x* <sup>55</sup> + *x*.

**Solution** A direct application of the above theorem tells that the derivative of the above function is 99 54 600 55 1 *x x* − + .

**Example 14** Find the derivative of *f*(*x*) = 1 + *x* + *x* <sup>2</sup> + *x* <sup>3</sup> +... + *x* <sup>50</sup> at *x* = 1.

**Solution** A direct application of the above Theorem 6 tells that the derivative of the above function is 1 + 2*x* + 3*x* <sup>2</sup> + . . . + 50*x* 49 *.* At *x* = 1 the value of this function equals

$$11 + 2(1) + 3(1)^2 + \dots + 50(1)^{49} = 1 + 2 + 3 + \dots + 50 = \frac{(50)(51)}{2} = 1275.1$$

**Example 15** Find the derivative of *f*(*x*) = *x* 1 *x* +

**Solution** Clearly this function is defined everywhere except at *x* = 0. We use the quotient rule with *u* = *x* + 1 and *v* = *x*. Hence *u*′ = 1 and *v*′ = 1. Therefore

$$\frac{df(\mathbf{x})}{d\mathbf{x}} = \frac{d}{d\mathbf{x}} \left(\frac{\mathbf{x} + 1}{\mathbf{x}}\right) = \frac{d}{d\mathbf{x}} \left(\frac{\mathbf{u}}{\mathbf{v}}\right) = \frac{\mathbf{u}'\mathbf{v} - \mathbf{u}\mathbf{v}'}{\mathbf{v}^2} = \frac{\mathbf{1}\{\mathbf{x}\} - \{\mathbf{x} + 1\}\mathbf{1}}{\mathbf{x}^2} = -\frac{\mathbf{1}\{\mathbf{x}\}}{\mathbf{x}^2}$$

**Example 16** Compute the derivative of sin *x*.

**Solution** Let *f*(*x*) = sin *x*. Then

$$\frac{df(\mathbf{x})}{d\mathbf{x}} = \lim\_{h \to 0} \frac{f\left(\mathbf{x} + h\right) - f\left(\mathbf{x}\right)}{h} = \lim\_{h \to 0} \frac{\sin\left(\mathbf{x} + h\right) - \sin\left(\mathbf{x}\right)}{h}$$

$$= \lim\_{h \to 0} \frac{2\cos\left(\frac{2\mathbf{x} + h}{2}\right)\sin\left(\frac{h}{2}\right)}{h} \text{ (using formula for } \sin\mathbf{A} - \sin\mathbf{B})$$

$$= \lim\_{h \to 0} \cos\left(\mathbf{x} + \frac{h}{2}\right) \lim\_{h \to 0} \frac{\sin\frac{h}{2}}{h} = \cos\mathbf{x}. \mathbf{l} = \cos\mathbf{x}$$

2

**Example 17** Compute the derivative of tan *x.*

**Solution** Let *f*(*x*) = tan *x*. Then

$$\frac{df(\mathbf{x})}{d\mathbf{x}} = \lim\_{h \to 0} \frac{f\left(\mathbf{x} + h\right) - f\left(\mathbf{x}\right)}{h} = \lim\_{h \to 0} \frac{\tan\left(\mathbf{x} + h\right) - \tan\left(\mathbf{x}\right)}{h}$$

$$= \lim\_{h \to 0} \frac{1}{h} \left[ \frac{\sin\left(\mathbf{x} + h\right)}{\cos\left(\mathbf{x} + h\right)} - \frac{\sin\mathbf{x}}{\cos\mathbf{x}} \right]$$

$$\begin{aligned} &= \lim\_{h \to 0} \left[ \frac{\sin \left( x + h \right) \cos x - \cos \left( x + h \right) \sin x}{h \cos \left( x + h \right) \cos x} \right] \\\\ &= \lim\_{h \to 0} \frac{\sin \left( x + h - x \right)}{h \cos \left( x + h \right) \cos x} \text{ (using formula for } \sin \left( A + B \right) \text{)} \\\\ &= \lim\_{h \to 0} \frac{\sin h}{h} \cdot \lim\_{h \to 0} \frac{1}{\cos \left( x + h \right) \cos x} \\\\ &= 1 \cdot \frac{1}{\cos^2 x} = \sec^2 x \end{aligned}$$

**Example 18** Compute the derivative of *f*(*x*) = sin<sup>2</sup> *x*.

**Solution** We use the Leibnitz product rule to evaluate this.

$$\begin{aligned} \frac{df(x)}{dx} &= \frac{d}{dx} (\sin x \sin x) \\ &= \left(\sin x\right)' \sin x + \sin x (\sin x)' \\ &= \left(\cos x\right) \sin x + \sin x (\cos x) \\ &= 2 \sin x \cos x = \sin 2x \end{aligned}$$

**EXERCISE 12.2**

- **1.** Find the derivative of *x* <sup>2</sup> – 2 at *x* = 10.
- **2.** Find the derivative of *x* at *x* = 1.
- **3.** Find the derivative of 99*x* at *x* = l00.
- **4.** Find the derivative of the following functions from first principle.

$$\begin{array}{cccc} \text{(i)} & \begin{array}{cccc} \text{x}^3 - 27 \end{array} & \begin{array}{c} \text{(i)} \end{array} & \begin{array}{c} \text{(i)} \end{array} & \begin{array}{c} \text{(i)} \end{array} \end{array} \end{array} \quad \begin{array}{c} \text{(i)} \quad \begin{array}{c} \text{(x-1)} \end{array} \begin{array}{c} \text{(x-2)} \end{array} \end{array}$$
 
$$\begin{array}{c} \text{(iii)} \quad \frac{1}{\mathbf{x} - \mathbf{1}} \end{array}$$

**5.** For the function

$$f'(\mathbf{x}) = \frac{\mathbf{x}^{100}}{100} + \frac{\mathbf{x}^{99}}{99} + \dots + \frac{\mathbf{x}^2}{2} + \mathbf{x} + \mathbf{1} \dots$$

Prove that *f f* ′ ′ (1 100 0 ) = ( ).

- **6.** Find the derivative of 1 2 2 <sup>1</sup> . . . *n n n n n x ax a x a x a* − − <sup>−</sup> + + + + + for some fixed real number *a*.
- **7.** For some constants *a* and *b*, find the derivative of

$$\text{(i)}\quad \dot{\left(x-a\right)}\left(x-b\right) \qquad\qquad\qquad\text{(ii)}\quad \left(a\right)^{2}\left(a\right)^{2}\qquad\qquad\qquad\text{(iii)}\quad \frac{x-a}{x-b}$$

- **8.** Find the derivative of *n n x a x a* − − for some constant *a*.
- **9.** Find the derivative of

$$\begin{array}{ccccc} \text{(i)} & 2\mathbf{x} - \frac{\mathbf{3}}{4} & & & \text{(ii)} & \begin{pmatrix} \mathbf{5x}^3 + \mathbf{3x} - 1 \end{pmatrix} \begin{pmatrix} \mathbf{x} - \mathbf{1} \end{pmatrix} \\ & \begin{pmatrix} \mathbf{1} - \mathbf{1} \end{pmatrix} \end{array}$$

$$\begin{array}{ccccc} \text{(iii)} & \text{x}^{-3} \text{(5+3x)} & & \text{(iv)} & \text{x}^{8} \text{(3-6x}^{-9}) \\ & & & \text{x}^{-3} & & \text{y}^{-3} \end{array}$$

$$\mathbf{r}(\mathbf{v}) = \mathbf{x}^{-4} \left( \mathbf{3} - 4\mathbf{x}^{-8} \right) \qquad \qquad \qquad \qquad \int\_{\mathbf{v}(\mathbf{x})} \mathbf{(vi)} \cdot \frac{\mathbf{v}^2}{\mathbf{x} + 1} \cdot \frac{\mathbf{x}^2}{3\mathbf{x}^2 + 1} \, d\mathbf{x}$$

## **10**. Find the derivative of cos *x* from first principle.

**11.** Find the derivative of the following functions:

- (i) sin cos *x x* (ii) sec *x* (iii) 5sec 4cos *x x* + (iv) cosec *x* (v) 3cot 5cosec *x x* +
- (vi) 5sin 6cos 7 *x x* − + (vii) 2tan 7sec *x x* −

# *Miscellaneous Examples*

**Example 19** Find the derivative of *f* from the first principle, where *f* is given by

$$\begin{array}{cccc} \text{(i)} & f'(\mathbf{x}) = \frac{2\mathbf{x} + \mathbf{3}}{\mathbf{x} - \mathbf{2}} & & & \text{(ii)} & f'(\mathbf{x}) = \mathbf{x} + \frac{1}{\mathbf{x}} \end{array}$$

**Solution** (i) Note that function is not defined at *x* = 2. But, we have

$$f'(x) = \lim\_{h \to 0} \frac{f\left(x+h\right) - f\left(x\right)}{h} = \lim\_{h \to 0} \frac{\frac{2\left(x+h\right) + 3}{x+h-2} - \frac{2x+3}{x-2}}{h}$$

$$\begin{aligned} &= \lim\_{h \to 0} \frac{(2x+2h+3)(x-2) - (2x+3)(x+h-2)}{h\left(x-2\right)\left(x+h-2\right)} \\ &= \lim\_{h \to 0} \frac{(2x+3)(x-2) + 2h\left(x-2\right) - (2x+3)\left(x-2\right) - h\left(2x+3\right)}{h\left(x-2\right)\left(x+h-2\right)} \\ &= \lim\_{h \to 0} \frac{-7}{\left(x-2\right)\left(x+h-2\right)} = -\frac{7}{\left(x-2\right)^2} \end{aligned}$$

Again, note that the function *f* ′ is also not defined at *x* = 2. (ii) The function is not defined at *x* = 0. But, we have

$$f'(x) \ = \lim\_{h \to 0} \frac{f\left(x+h\right) - f\left(x\right)}{h} = \lim\_{h \to 0} \frac{\left(x+h + \frac{1}{x+h}\right) - \left(x + \frac{1}{x}\right)}{h}$$

$$= \lim\_{h \to 0} \frac{1}{h} \left[h + \frac{1}{x+h} - \frac{1}{x}\right]$$

$$= \lim\_{h \to 0} \frac{1}{h} \left[h + \frac{x-x-h}{x\left(x+h\right)}\right] = \lim\_{h \to 0} \frac{1}{h} \left[h\left(1 - \frac{1}{x\left(x+h\right)}\right)\right]$$

$$= \lim\_{h \to 0} \left[1 - \frac{1}{x\left(x+h\right)}\right] = 1 - \frac{1}{x^2}$$

Again, note that the function *f* ′ is not defined at *x* = 0.

**Example 20** Find the derivative of *f(x)* from the first principle, where *f(x)* is

(i) sin cos *x x* + (ii) *x x* sin

$$\text{Solution (i) we have } f'(x) = \frac{f\left(x+h\right) - f\left(x\right)}{h}$$

$$= \lim\_{h \to 0} \frac{\sin\left(x+h\right) + \cos\left(x+h\right) - \sin x - \cos x}{h}$$

$$= \lim\_{h \to 0} \frac{\sin x \cos h + \cos x \sin h + \cos x \cos h - \sin x \sin h - \sin x - \cos x}{h}$$

$$=\lim\_{h\to 0} \frac{\sin h(\cos x - \sin x) + \sin x(\cos h - 1) + \cos x(\cos h - 1)}{h}$$

$$=\lim\_{h\to 0} \frac{\sin h}{h} (\cos x - \sin x) + \lim\_{h\to 0} \sin x \frac{(\cos h - 1)}{h} \quad + \lim\_{h\to 0} \cos x \frac{(\cos h - 1)}{h}$$

$$=\cos x - \sin x$$

$$\text{(ii)} \quad f^\*(\mathbf{x}) \quad = \lim\_{h\to 0} \frac{f(\mathbf{x} + h) - f(\mathbf{x})}{h} = \lim\_{h\to 0} \frac{(\mathbf{x} + h)\sin \left(\mathbf{x} + h\right) - x\sin x}{h}$$

$$=\lim\_{h\to 0} \frac{(\mathbf{x} + h)(\sin x \cos h + \sin h \cos x) - x\sin x}{h}$$

$$=\lim\_{h\to 0} \frac{x\sin x (\cos h - 1) + x\cos x \sin h + h(\sin x \cos h + \sin h \cos x)}{h}$$

$$=\lim\_{h\to 0} \frac{x\sin x (\cos h - 1)}{h} + \lim\_{h\to 0} x\cos x \frac{\sin h}{h} + \lim\_{h\to 0} (\sin x \cos h + \sin h \cos x)$$

$$=\left(x \cos x + \sin x\right)$$

**Example 21** Compute derivative of

$$\begin{array}{c} \text{(i)} \, f(\mathbf{x}) \equiv \sin \, 2\mathbf{x} \qquad \qquad \qquad \qquad \qquad \text{(ii)} \, \mathbf{g}(\mathbf{x}) \equiv \cot \mathbf{x} \, \end{array}$$

**Solution** (i) Recall the trigonometric formula sin 2*x* = 2 sin *x* cos *x*. Thus

$$\frac{df(x)}{dx} = \frac{d}{dx}(2\sin x \cos x) = 2\frac{d}{dx}(\sin x \cos x)$$

$$= 2\left[\left(\sin x\right)' \cos x + \sin x \left(\cos x\right)'\right]$$

$$= 2\left[\left(\cos x\right)\cos x + \sin x \left(-\sin x\right)\right]$$

$$= 2\left(\cos^2 x - \sin^2 x\right)$$

(ii) By definition, g(*x*) = cos cot sin *x x x* = . We use the quotient rule on this function

wherever it is defined. cos (cot ) sin *dg d d x x dx dx dx x* = =

$$=\frac{(\cos x)'(\sin x) - (\cos x)(\sin x)'}{(\sin x)^2}$$

$$=\frac{(-\sin x)(\sin x) - (\cos x)(\cos x)}{(\sin x)^2}$$

$$=-\frac{\sin^2 x + \cos^2 x}{\sin^2 x} = -\text{cosec}^2 x$$

Alternatively, this may be computed by noting that 1 cot tan *x x* = . Here, we use the fact that the derivative of *tan x* is *sec<sup>2</sup> x* which we saw in Example 17 and also that the derivative of the constant function is 0.

$$\frac{d\mathbf{g}}{d\mathbf{x}} = \frac{d}{d\mathbf{x}}(\cot \mathbf{x}) = \frac{d}{d\mathbf{x}}\left(\frac{1}{\tan \mathbf{x}}\right)$$

$$= \frac{(\mathbf{l})'(\tan \mathbf{x}) - (\mathbf{l})(\tan \mathbf{x})'}{(\tan \mathbf{x})^2}$$

$$= \frac{(\mathbf{0})(\tan \mathbf{x}) - (\sec \mathbf{x})^2}{(\tan \mathbf{x})^2}$$

$$= \frac{-\sec^2 \mathbf{x}}{\tan^2 \mathbf{x}} = -\csc \sec^2 \mathbf{x}$$

**Example 22** Find the derivative of

$$\text{(i) } \frac{x^s - \cos x}{\sin x} \qquad\qquad\qquad\qquad\qquad\text{(ii) } \frac{x + \cos x}{\tan x}$$

**Solution** (i) Let 5 cos ( ) sin *x x h x x* − = . We use the quotient rule on this function wherever

it is defined.

$$h'(x) = \frac{(x^\circ - \cos x)' \sin x - (x^\circ - \cos x)(\sin x)'}{\left(\sin x\right)^2}$$

$$=\frac{(5x^4+\sin x)\sin x - (x^8-\cos x)\cos x}{\sin^2 x}$$

$$=\frac{-x^8\cos x + 5x^4\sin x + 1}{\left(\sin x\right)^2}$$

 (ii) We use quotient rule on the function cos tan *x x x* + wherever it is defined.

$$h'(x) = \frac{(x + \cos x)' \tan x - (x + \cos x)(\tan x)'}{\left(\tan x\right)^2}$$

$$= \frac{(1 - \sin x)\tan x - (x + \cos x)\sec^2 x}{\left(\tan x\right)^2}$$

## *Miscellaneous Exercise on Chapter 12*

**1.** Find the derivative of the following functions from first principle:

$$\text{(i)}\ \text{'} - \text{x} \qquad \qquad \text{(ii)}\ \text{'} \left( \text{(-x)} \right)^{-1} \qquad \qquad \text{(iii)}\ \sin\left(\text{x} + 1\right)^{\bigvee\mathup \text{(-x)}} \qquad \text{(iv)}\ \cos\left(\text{x} - \frac{\pi}{8}\right)^{-1}$$

Find the derivative of the following functions (it is to be understood that *a, b, c, d, p, q, r* and *s* are fixed non-zero constants and *m* and *n* are integers):

$$\begin{array}{llll} \text{12. } (\mathbf{x} + a) & \text{3. } (px + q) \left(\frac{r}{x} + s\right) & \text{4. } \left(ax + b\right)(cx + d) \\\\ \text{5. } \frac{ax + b}{cx + d} & \text{7. } \frac{1}{1 - \frac{x}{x}} & \text{7. } \frac{1}{ax^2 + bx + c} \\\\ \text{8. } \frac{ax + b}{px^2 + qx + r} & \text{9. } \frac{px^2 + qx + r}{ax + b} & \text{10. } \frac{a}{x^4} - \frac{b}{x^2} + \cos x \\\\ \text{11. } 4\sqrt{x} - 2 & \text{12. } (ax + b)^n & \text{13. } (ax + b)^n \text{ ( $x + b$ )}^n \\\\ \text{14. } \sin(\mathbf{x} + a) & \text{15. } \cos x \text{ x cot } x & \text{16. } \frac{\cos x}{1 + \sin x} \end{array}$$

$$\begin{array}{llll} \text{17. } & \frac{\sin x + \cos x}{\sin x - \cos x} & \text{18. } & \frac{\sec x - 1}{\sec x + 1} & \text{19. } & \sin^n x \\\\ \text{20. } & \frac{a + b \sin x}{c + d \cos x} & \text{21. } & \frac{\sin(x + a)}{\cos x} & \text{22. } & \text{x4 } (\sin x - \text{3} \cos x) \\\\ \text{23. } & \left(x^2 + 1\right) \cos x & \text{24. } & \left(ax^2 + \sin x\right) \left(p + q \cos x\right) \\\\ \text{25. } & \left(x + \cos x\right) \left(x - \tan x\right) & \text{26. } & \frac{4x + 5 \sin x}{3x + 7 \cos x} & \text{27. } & \frac{x^2 \cos\left(\frac{\pi}{4}\right)}{\sin x} \\\\ \text{28. } & \frac{x}{1 + \tan x} & \text{29. } & \left(x + \sec x\right) \left(x - \tan x\right) & \text{30. } & \frac{\sqrt{x}}{\sin^2 x} \end{array}$$

## *Summary*

- ÆThe expected value of the function as dictated by the points to the left of a point defines the left hand limit of the function at that point. Similarly the right hand limit.
- ÆLimit of a function at a point is the common value of the left and right hand limits, if they coincide.
- ÆFor a function *f* and a real number *a*, lim *x a* → *f*(*x*) and *f* (*a*) may not be same (In

fact, one may be defined and not the other one).

ÆFor functions *f* and *g* the following holds:

$$\lim\_{x \to a} \left[ f(\mathbf{x}) \pm \mathbf{g}(\mathbf{x}) \right] = \lim\_{x \to a} f(\mathbf{x}) \pm \lim\_{x \to a} \mathbf{g}(\mathbf{x})$$

$$\lim\_{x \to a} [f(\mathbf{x}), \mathbf{g}(\mathbf{x})] = \lim\_{\mathbf{x} \to a} f(\mathbf{x}) . \lim\_{\mathbf{x} \to a} \mathbf{g}(\mathbf{x})$$

$$\lim\_{x \to a} \left[ \frac{f(x)}{\mathbf{g}(x)} \right] = \frac{\lim\_{x \to a} f(x)}{\lim\_{x \to a} \mathbf{g}(x)}$$

ÆFollowing are some of the standard limits

$$\lim\_{x \to a} \frac{x^n - a^n}{x - a} = na^{n-1}$$

$$\begin{aligned} &\lim\_{x\to 0} \frac{\sin x}{x} = 0\\ &\lim\_{x\to 0} \frac{1 - \cos x}{x} = 0 \end{aligned}$$

$$\text{The derivative of a function } f \text{ at } a \text{ is defined by}$$

$$\begin{aligned} &f'(a) = \lim\_{h \to 0} \frac{f'(a+h) - f'(a)}{h} \\ &\text{Derivative of a function } f \text{ at any point } x \text{ is defined by} \\ &f'(\infty) = \frac{df(\infty)}{dx} = \lim\_{h \to 0} \frac{f(\infty + h) - f(\infty)}{h} \\ &\text{\textbullet For functions } u \text{ and } v \text{ the following holds:} \\ &(u \pm v)' = u' \pm v' \\ &(uv)' = u'v + uv' \\ &(uv)' = u'v + uv' \\ &\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2} \text{ provided all are defined.} \end{aligned}$$

$$\text{Following are some of the standard derivatives:} $$

$$\frac{d}{dx}(x^n) = nx^{n-1} \underbrace{\boxed{\dots}}\_{\text{def}}(\sin x) = \cos x$$

$$\frac{d}{dx}(\cos x) = -\sin x$$

## *Historical Note*

In the history of mathematics two names are prominent to share the credit for inventing calculus, Issac Newton (1642 – 1727) and G.W. Leibnitz (1646 – 1717). Both of them independently invented calculus around the seventeenth century. After the advent of calculus many mathematicians contributed for further development of calculus. The rigorous concept is mainly attributed to the great

#### 256 MATHEMATICS

mathematicians, A.L. Cauchy, J.L.Lagrange and Karl Weierstrass. Cauchy gave the foundation of calculus as we have now generally accepted in our textbooks. Cauchy used D'Alembert's limit concept to define the derivative of a function. Starting with definition of a limit, Cauchy gave examples such as the limit of

$$\frac{\sin a}{a} \text{ for } !\_{\alpha} \equiv 0. \text{ He wrote } \frac{\Delta y}{\Delta x} \text{=} \frac{f(\mathbf{x} + i) - f(\mathbf{x})}{i}, \text{ and called the limit for } \frac{\Delta x}{\Delta y}$$

*i* → 0, the "function derive'e, *y*′ for *f* ′ (*x*)".

Before 1900, it was thought that calculus is quite difficult to teach. So calculus became beyond the reach of youngsters. But just in 1900, John Perry and others in England started propagating the view that essential ideas and methods of calculus were simple and could be taught even in schools. F.L. Griffin, pioneered the teaching of calculus to first year students. This was regarded as one of the most daring act in those days.

Today not only the mathematics but many other subjects such as Physics, Chemistry, Economics and Biological Sciences are enjoying the fruits of calculus.

**—** v **—**