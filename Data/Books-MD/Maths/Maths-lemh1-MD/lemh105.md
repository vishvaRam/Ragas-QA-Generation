![](_page_0_Picture_0.jpeg)

# **CONTINUITY AND DIFFERENTIABILITY**

v*The whole of science is nothing more than a refinement of everyday thinking.***" —** *ALBERT EINSTEIN* v

# **5.1 Introduction**

104 MATHEMATICS

This chapter is essentially a continuation of our study of differentiation of functions in Class XI. We had learnt to differentiate certain functions like polynomial functions and trigonometric functions. In this chapter, we introduce the very important concepts of continuity, differentiability and relations between them. We will also learn differentiation of inverse trigonometric functions. Further, we introduce a new class of functions called exponential and logarithmic functions. These functions lead to powerful techniques of differentiation. We illustrate certain geometrically obvious conditions through differential calculus. In the process, we will learn some fundamental theorems in this area.

![](_page_0_Picture_5.jpeg)

**Sir Issac Newton (1642-1727)**

# **5.2 Continuity**

We start the section with two informal examples to get a feel of continuity. Consider the function

$$f(\mathbf{x}) = \begin{cases} 1, \text{if } \mathbf{x} \le \mathbf{0} \\ 2, \text{if } \mathbf{x} > \mathbf{0} \end{cases}$$

This function is of course defined at every point of the real line. Graph of this function is given in the Fig 5.1. One can deduce from the graph that the value of the function at *nearby* points on *x*-axis remain *close* to each other except at *x* = 0. At the points near and to the left of 0, i.e., at points like – 0.1, – 0.01, – 0.001, the value of the function is 1. At the points near and to the right of 0, i.e., at points like 0.1, 0.01,

![](_page_0_Figure_11.jpeg)

0.001, the value of the function is 2. Using the language of left and right hand limits, we may say that the left (respectively right) hand limit of *f* at 0 is 1 (respectively 2). In particular the left and right hand limits do not coincide. We also observe that the value of the function at *x* = 0 concides with the left hand limit. Note that when we try to draw the graph, we cannot draw it in one stroke, i.e., without lifting pen from the plane of the paper, we can not draw the graph of this function. In fact, we need to lift the pen when we come to 0 from left. This is one instance of function being not continuous at *x* = 0.

Now, consider the function defined as

$$f(x) = \begin{cases} 1, \text{if } x \neq 0 \\ 2, \text{if } x = 0 \end{cases}$$

This function is also defined at every point. Left and the right hand limits at *x* = 0

are both equal to 1. But the value of the function at *x* = 0 equals 2 which does not coincide with the common value of the left and right hand limits. Again, we note that we cannot draw the graph of the function without lifting the pen. This is yet another instance of a function being not continuous at *x* = 0.

Naively, we may say that a function is continuous at a fixed point if we can draw the graph of the function *around* that point without lifting the pen from the plane of the paper.

![](_page_1_Figure_7.jpeg)

Mathematically, it may be phrased precisely as follows:

**Definition 1** Suppose *f* is a real function on a subset of the real numbers and let *c* be a point in the domain of *f*. Then *f* is continuous at *c* if

$$\lim\_{x \to c} f(x) = f(c)$$

More elaborately, if the left hand limit, right hand limit and the value of the function at *x* = *c* exist and equal to each other, then *f* is said to be continuous at *x* = *c*. Recall that if the right hand and left hand limits at *x* = *c* coincide, then we say that the common value is the limit of the function at *x* = *c*. Hence we may also rephrase the definition of continuity as follows: *a function is continuous at x = c if the function is defined at x = c and if the value of the function at x = c equals the limit of the function at x = c.* If *f* is not continuous at *c*, we say *f* is *discontinuous* at *c* and *c* is called a *point of discontinuity* of *f*.

**Example 1** Check the continuity of the function *f* given by *f*(*x*) = 2*x* + 3 at *x* = 1.

**Solution** First note that the function is defined at the given point *x* = 1 and its value is 5. Then find the limit of the function at *x* = 1. Clearly

$$\lim\_{x \to 1} f(x) = \lim\_{x \to 1} (2x + 3) = 2(1) + 3 = 5$$

Thus <sup>1</sup> lim ( ) 5 (1) *x f x f* → = = Hence, *f* is continuous at *x* = 1.

**Example 2** Examine whether the function *f* given by *f*(*x*) = *x* 2 is continuous at *x* = 0.

**Solution** First note that the function is defined at the given point *x* = 0 and its value is 0. Then find the limit of the function at *x* = 0. Clearly

$$\lim\_{x \to 0} f(x) = \lim\_{x \to 0} x^2 = 0^2 = 0$$
 
$$\text{Thus } \qquad \lim\_{x \to 0} f(x) = 0 = f(0)$$

Hence, *f* is continuous at *x* = 0.

**Example 3** Discuss the continuity of the function *f* given by *f*(*x*) = | *x* | at *x* = 0.

**Solution** By definition

$$\mathcal{L}f(x) = \begin{cases} -x, \text{ if } x < 0 \\ x, \quad \text{if } x \ge 0 \end{cases}$$

Clearly the function is defined at 0 and *f*(0) = 0. Left hand limit of *f* at 0 is

$$\lim\_{x \to 0^{-}} f(x) = \lim\_{x \to 0^{-}} (-x) = 0$$

Similarly, the right hand limit of *f* at 0 is

$$\lim\_{\mathfrak{x}\to 0^{+}} f(\mathfrak{x}) = \lim\_{\mathfrak{x}\to 0^{+}} \mathfrak{x} = 0$$

Thus, the left hand limit, right hand limit and the value of the function coincide at *x* = 0. Hence, *f* is continuous at *x* = 0.

**Example 4** Show that the function *f* given by

$$f(\mathbf{x}) = \begin{cases} \mathbf{x}^3 + \mathbf{3}, & \text{if } \mathbf{x} \neq \mathbf{0} \\ \mathbf{l}, & \text{if } \mathbf{x} = \mathbf{0} \end{cases}$$

is not continuous at *x* = 0.

**Solution** The function is defined at *x* = 0 and its value at *x* = 0 is 1. When *x* ≠ 0, the function is given by a polynomial. Hence,

$$\lim\_{x \to 0} f(x) = \lim\_{x \to 0} (x^3 + 3) = 0^3 + 3 = 3$$

Since the limit of *f* at *x* = 0 does not coincide with *f*(0), the function is not continuous at *x* = 0. It may be noted that *x* = 0 is the only point of discontinuity for this function.

**Example 5** Check the points where the constant function *f*(*x*) = *k* is continuous.

**Solution** The function is defined at all real numbers and by definition, its value at any real number equals *k*. Let *c* be any real number. Then

$$\lim\_{x \to c} f(x) = \lim\_{x \to c} k = k$$

Since *f*(*c*) = *k* = lim *x c* <sup>→</sup> *f*(*x*) for any real number *c*, the function *f* is continuous at every real number.

**Example 6** Prove that the identity function on real numbers given by *f*(*x*) = *x* is continuous at every real number.

**Solution** The function is clearly defined at every point and *f*(*c*) = *c* for every real number *c*. Also,

$$\lim\_{x \to c} f(x) = \lim\_{x \to c} x = c$$

Thus, lim *x c* → *f*(*x*) = *c* = *f*(*c*) and hence the function is continuous at every real number.

Having defined continuity of a function at a given point, now we make a natural extension of this definition to discuss continuity of a function.

**Definition 2** A real function *f* is said to be continuous if it is continuous at every point in the domain of *f*.

This definition requires a bit of elaboration. Suppose *f* is a function defined on a closed interval [*a*, *b*], then for *f* to be continuous, it needs to be continuous at every point in [*a*, *b*] including the end points *a* and *b*. Continuity of *f* at *a* means

$$\lim\_{\mathbf{x}\to a^{+}}f(\mathbf{x}) = f(a)$$

and continuity of *f* at *b* means

– lim ( ) *x b f x* → = *f*(*b*)

*Observe that* lim ( ) *x a f x* → <sup>−</sup>  *and* lim ( ) *x b f x* → <sup>+</sup> *do not make sense. As a consequence of this definition, if f is defined only at one point, it is continuous there, i.e., if the domain of f is a singleton, f is a continuous function.*

**Example 7** Is the function defined by *f*(*x*) = | *x* |, a continuous function? **Solution** We may rewrite *f* as

$$f(\mathbf{x}) = \begin{cases} -\mathbf{x}, \text{ if } \mathbf{x} < \mathbf{0} \\ \mathbf{x}, \quad \text{if } \mathbf{x} \ge \mathbf{0} \end{cases}$$

By Example 3, we know that *f* is continuous at *x* = 0. Let *c* be a real number such that *c* < 0. Then *f*(*c*) = – *c*. Also

$$\lim\_{x \to c} f(x) = \lim\_{x \to c} (-x) = -c \qquad \text{ (Why?)}$$

Since lim ( ) ( ) *x c f x f c* → = , *f* is continuous at all negative real numbers.

Now, let *c* be a real number such that *c* > 0. Then *f*(*c*) = *c*. Also

$$\lim\_{x \to c} f(x) = \lim\_{x \to c} x = c \qquad \qquad \text{(Why?)}$$

Since lim ( ) ( ) *x c f x f c* → = , *f* is continuous at all positive real numbers. Hence, *f* is continuous at all points.

**Example 8** Discuss the continuity of the function *f* given by *f* (*x*) = *x* 3 + *x* 2 – 1.

**Solution** Clearly *f* is defined at every real number *c* and its value at *c* is *c* 3 + *c* 2 – 1. We also know that

$$\lim\_{x \to c} f(x) = \lim\_{x \to c} \left(x^3 + x^2 - 1\right) = c^3 + c^2 - 1$$

Thus lim ( ) ( ) *x c f x f c* → = , and hence *f* is continuous at every real number. This means *f* is a continuous function.

**Example 9** Discuss the continuity of the function *f* defined by *f* (*x*) = <sup>1</sup> *x* , *x* ≠ 0.

**Solution** Fix any non zero real number *c*, we have

$$\lim\_{\mathfrak{x}\to\mathcal{c}} f(\mathfrak{x}) = \lim\_{\mathfrak{x}\to\mathcal{c}} \frac{1}{\mathfrak{x}} = \frac{1}{\mathcal{c}}$$

Also, since for *c* ≠ 0, 1 *f c*( ) *c* = , we have lim ( ) ( ) *x c f x f c* → = and hence, *f* is continuous at every point in the domain of *f*. Thus *f* is a continuous function.

We take this opportunity to explain the concept of *infinity*. This we do by analysing the function *f* (*x*) = 1 *x* near *x* = 0. To carry out this analysis we follow the usual trick of finding the value of the function at real numbers *close* to 0. Essentially we are trying to find the right hand limit of *f* at 0. We tabulate this in the following (Table 5.1).

| x        | 1 | 0.3   | 0.2 | 0.1 = 10–1 | 0.01 = 10–2 | 0.001 = 10–3 | 10–n |
|----------|---|-------|-----|------------|-------------|--------------|------|
| f<br>(x) | 1 | 3.333 | 5   | 10         | 100 = 102   | 1000 = 103   | 10n  |

| Table 5.1 |  |  |
|-----------|--|--|
|-----------|--|--|

We observe that as *x* gets closer to 0 from the right, the value of *f* (*x*) shoots up higher. This may be rephrased as: the value of *f* (*x*) may be made larger than any given number by choosing a positive real number *very close* to 0. In symbols, we write

$$\lim\_{\mathbf{x}\to\mathbf{0}^+} f(\mathbf{x}) = +\infty$$

(to be read as: the right hand limit of *f* (*x*) at 0 is plus infinity). We wish to emphasise that + ∞ is NOT a real number and hence the right hand limit of *f* at 0 does not exist (as a real number).

Similarly, the left hand limit of *f* at 0 may be found. The following table is self explanatory.

| x        | – 1 | – 0.3   | – 0.2 | – 10–1 | – 10–2 | – 10–3 | – 10–n |
|----------|-----|---------|-------|--------|--------|--------|--------|
| f<br>(x) | – 1 | – 3.333 | – 5   | – 10   | – 102  | – 103  | – 10n  |

From the Table 5.2, we deduce that the value of *f*(*x*) may be made smaller than any given number by choosing a negative real number *very close* to 0. In symbols, we write

$$\lim\_{x \to 0^{-}} f(x) = -\infty$$

(to be read as: the left hand limit of *f*(*x*) at 0 is minus infinity). Again, we wish to emphasise that – ∞ is NOT a real number and hence the left hand limit of *f* at 0 does not exist (as a real number). The graph of the reciprocal function given in Fig 5.3 is a geometric representation of the above mentioned facts. **Fig 5.3**

![](_page_5_Figure_13.jpeg)

**Example 10** Discuss the continuity of the function *f* defined by

$$f(\mathbf{x}) = \begin{cases} \mathbf{x} + \mathbf{2}, \text{if } \mathbf{x} \le 1\\ \mathbf{x} - \mathbf{2}, \text{if } \mathbf{x} > 1 \end{cases}$$

**Solution** The function *f* is defined at all points of the real line.

**Case 1** If *c* < 1, then *f*(*c*) = *c* + 2. Therefore, lim ( ) lim( 2) 2 *x c x c f x x c* → → = + = + Thus, *f* is continuous at all real numbers lessthan 1. **Case 2** If *c* > 1, then *f*(*c*) = *c* – 2. Therefore, lim ( ) lim *x c x c f x* → → = (*x* – 2) = *c* – 2 = *f* (*c*) Thus, *f* is continuous at all points *x* > 1. **Case 3** If *c* = 1, then the left hand limit of *f* at *x* = 1 is – – 1 1 lim ( ) lim ( 2) 1 2 3 *x x f x x* → → = + = + = The right hand limit of *f* at *x* = 1 is 1 1 lim ( ) lim ( 2) 1 2 1 *x x f x x* → <sup>+</sup> → <sup>+</sup> = − = − = −

Since the left and right hand limits of *f* at *x* = 1 do not coincide, *f* is not continuous at *x* = 1. Hence

*x* = 1 is the only point of discontinuity of *f*. The graph of the function is given in Fig 5.4.

**Example 11** Find all the points of discontinuity of the function *f* defined by

$$f(\mathbf{x}) = \begin{cases} \mathbf{x} + \mathbf{2}, \text{if } \mathbf{x} < \mathbf{1} \\ \mathbf{0}, \quad \text{if } \mathbf{x} = \mathbf{1} \\ \mathbf{x} - \mathbf{2}, \text{if } \mathbf{x} > \mathbf{1} \end{cases}$$

**Solution** As in the previous example we find that *f* is continuous at all real numbers *x* ≠ 1. The left hand limit of *f* at *x* = 1 is

$$\lim\_{\mathbf{x}\to\mathbf{1}^-}f(\mathbf{x}) = \lim\_{\mathbf{x}\to\mathbf{1}^-}(\mathbf{x}+\mathbf{2}) = 1+\mathbf{2}=\mathbf{3}$$

The right hand limit of *f* at *x* = 1 is

$$\lim\_{x \to 1^{+}} f(x) = \lim\_{x \to 1^{+}} (x - 2) = 1 - 2 = -1$$

Since, the left and right hand limits of *f* at *x* = 1 do not coincide, *f* is not continuous at *x* = 1. Hence *x* = 1 is the only point of discontinuity of *f*. The graph of the function is given in the Fig 5.5.

![](_page_6_Figure_14.jpeg)

**Fig 5.4**

**Example 12** Discuss the continuity of the function defined by

$$f(\mathbf{x}) = \begin{cases} |\mathbf{x} + \mathbf{2}, \text{if } |\mathbf{x} < \mathbf{0}| \\ -\mathbf{x} + \mathbf{2}, \text{if } |\mathbf{x} > \mathbf{0}| \end{cases}$$

**Solution** Observe that the function is defined at all real numbers except at 0. Domain of definition of this function is

D<sup>1</sup> ∪ D<sup>2</sup> where D<sup>1</sup> = {*x* ∈ **R** : *x* < 0} and D<sup>2</sup> = {*x* ∈ **R** : *x* > 0} **Case 1** If *c* ∈ D<sup>1</sup> , then lim ( ) lim *x c x c f x* → → = (*x* + 2) = *c* + 2 = *f* (*c*) and hence *f* is continuous in D<sup>1</sup> . **Case 2** If *c* ∈ D<sup>2</sup> , then lim ( ) lim *x c x c f x* → → = (*– x* + 2) = – *c* + 2 = *f* (*c*) and hence *f* is continuous in D<sup>2</sup> . Since *f* is continuous at all points in the domain of *f*, we deduce that *f* is continuous. Graph of this function is given in the Fig 5.6. Note that to graph this function we need to lift the pen from the plane **Fig 5.6**

of the paper, but we need to do that only for those points where the function is not defined.

**Example 13** Discuss the continuity of the function *f* given by

$$f(\mathbf{x}) = \begin{cases} \mathbf{x}, & \text{if } \mathbf{x} \ge \mathbf{0} \\ \mathbf{x}^2, & \text{if } \mathbf{x} < \mathbf{0} \end{cases}$$

**Solution** Clearly the function is defined at every real number. Graph of the function is given in Fig 5.7. By inspection, it seems prudent to partition the domain of definition of *f* into three disjoint subsets of the real line.

 **Fig 5.7**

Let D<sup>1</sup> = {*x* ∈ **R** : *x* < 0}, D<sup>2</sup> = {0} and D3 = {*x* ∈ **R** : *x* > 0}

**Case 1** At any point in D<sup>1</sup> , we have *f*(*x*) = *x* 2 and it is easy to see that it is continuous there (see Example 2).

**Case 2** At any point in D<sup>3</sup> , we have *f*(*x*) = *x* and it is easy to see that it is continuous there (see Example 6).

**Case 3** Now we analyse the function at *x* = 0. The value of the function at 0 is *f*(0) = 0. The left hand limit of *f* at 0 is

$$\lim\_{x \to 0^{-}} f(x) = \lim\_{x \to 0^{-}} x^{2} = 0^{2} = 0^{4}$$

The right hand limit of *f* at 0 is

$$\lim\_{x \to 0^{+}} f(x) = \lim\_{x \to 0^{+}} x = 0$$

Thus 0 lim ( ) 0 *x f x* → = = *f*(0) and hence *f* is continuous at 0. This means that *f* is

continuous at every point in its domain and hence, *f* is a continuous function.

**Example 14** Show that every polynomial function is continuous.

**Solution** Recall that a function *p* is a polynomial function if it is defined by *p*(*x*) = *a*<sup>0</sup> + *a*<sup>1</sup> *x* + ... + *a<sup>n</sup> x n* for some natural number *n*, *a<sup>n</sup>* ≠ 0 and *a<sup>i</sup>* ∈ **R**. Clearly this function is defined for every real number. For a fixed real number *c*, we have

$$\lim\_{x \to \infty} p\left(x\right) = p\left(c\right)$$

By definition, *p* is continuous at *c*. Since *c* is any real number, *p* is continuous at every real number and hence *p* is a continuous function.

**Example 15** Find all the points of discontinuity of the greatest integer function defined by *f*(*x*) = [*x*], where [*x*] denotes the greatest integer less than or equal to *x*.

**Solution** First observe that *f* is defined for all real numbers. Graph of the function is given in Fig 5.8. From the graph it looks like that *f* is discontinuous at every integral point. Below we explore, if this is true.

**Fig 5.8**

**Case 1** Let *c* be a real number which is not equal to any integer. It is evident from the graph that for all real numbers *close* to *c* the value of the function is equal to [*c*]; i.e., lim ( ) lim [ ] [ ] *x c x c f x x c* → → = = . Also *f*(*c*) = [*c*] and hence the function is continuous at all real numbers not equal to integers.

**Case 2** Let *c* be an integer. Then we can find a sufficiently small real number *r* > 0 such that [*c* – *r*] = *c* – 1 whereas [*c* + *r*] = *c*.

This, in terms of limits mean that

$$\lim\_{x \to c^{-}} f(\alpha) = c - 1,\\ \lim\_{x \to c^{+}} f(\alpha) = c^{+} $$

Since these limits cannot be equal to each other for any *c*, the function is discontinuous at every integral point.

#### *5.2.1 Algebra of continuous functions*

In the previous class, after having understood the concept of limits, we learnt some algebra of limits. Analogously, now we will study some algebra of continuous functions. Since continuity of a function at a point is entirely dictated by the limit of the function at that point, it is reasonable to expect results analogous to the case of limits.

**Theorem 1** Suppose *f* and *g* be two real functions continuous at a real number *c*. Then

- (1) *f* + *g* is continuous at *x* = *c*.
- (2) *f g* is continuous at *x* = *c*.
- (3) *f* . *g* is continuous at *x* = *c*.

$$(4)\quad \left(\frac{f}{\mathbf{g}}\right)\text{ is continuous at }x \overset{\triangle}{=} \underset{\smile}{(\text{provided }\mathbf{g}\,(c)\neq 0)}.$$

**Proof** We are investigating continuity of (*f* + *g*) at *x* = *c*. Clearly it is defined at *x* = *c*. We have

$$\lim\_{x \to c} (f+\mathbf{g})(\mathbf{x}) = \lim\_{x \to c} [f(\mathbf{x}) + \mathbf{g}(\mathbf{x})] \qquad \text{(by definition of } f+\mathbf{g})$$

$$= \lim\_{x \to c} f(\mathbf{x}) + \lim\_{x \to c} \mathbf{g}(\mathbf{x}) \qquad \text{(by the theorem on limits)}$$

$$= f(c) + \mathbf{g}(c) \qquad \qquad \text{(as } f \text{ and } \mathbf{g} \text{ are continuous)}$$

$$= (f+\mathbf{g})(c) \qquad \qquad \text{(by definition of } f+\mathbf{g})$$

Hence, *f* + *g* is continuous at *x* = *c*.

Proofs for the remaining parts are similar and left as an exercise to the reader.

#### *Remarks*

- (i) As a special case of (3) above, if *f* is a constant function, i.e., *f*(*x*) = λ for some real number λ, then the function (λ . *g*) defined by (λ . *g*) (*x*) = λ . *g*(*x*) is also continuous. In particular if λ = – 1, the continuity of *f* implies continuity of – *f*.
- (ii) As a special case of (4) above, if *f* is the constant function *f*(*x*) = λ, then the

$$\text{function } \frac{\lambda}{\text{g}} \text{ defined by } \frac{\lambda}{\text{g}}(\mathbf{x}) = \frac{\lambda}{\text{g}(\mathbf{x})} \text{ is also continuous whenever } \mathbf{g}(\mathbf{x}) \neq 0. \text{ In } \mathbf{x}$$

particular, the continuity of *g* implies continuity of <sup>1</sup> *g* .

The above theorem can be exploited to generate many continuous functions. They also aid in deciding if certain functions are continuous or not. The following examples illustrate this:

**Example 16** Prove that every rational function is continuous.

**Solution** Recall that every rational function *f* is given by

$$f(\mathbf{x}) = \frac{p(\mathbf{x})}{q(\mathbf{x})}, \ q(\mathbf{x}) \neq 0$$

where *p* and *q* are polynomial functions. The domain of *f* is all real numbers except points at which *q* is zero. Since polynomial functions are continuous (Example 14), *f* is continuous by (4) of Theorem 1.

**Example 17** Discuss the continuity of sine function.

**Solution** To see this we use the following facts

$$\lim\_{\mathbf{x}\to\mathbf{0}}\sin\mathbf{x} = \mathbf{0}$$

We have not proved it, but is intuitively clear from the graph of sin *x* near 0.

Now, observe that *f*(*x*) = sin *x* is defined for every real number. Let *c* be a real number. Put *x* = *c* + *h*. If *x* → *c* we know that *h* → 0. Therefore

$$\begin{aligned} \lim\_{x \to c} f(x) &= \lim\_{x \to c} \sin x \\ \sum\_{h \to 0} &= \lim\_{h \to 0} \sin(c+h) \\ &= \lim\_{h \to 0} [\sin c \cos h + \cos c \sin h] \\ &= \lim\_{h \to 0} [\sin c \cos h] + \lim\_{h \to 0} [\cos c \sin h] \\ &= \sin c + 0 = \sin c = f(c) \end{aligned}$$

Thus lim *x c* → *f*(*x*) = *f*(*c*) and hence *f* is a continuous function. *Remark* A similar proof may be given for the continuity of cosine function.

**Example 18** Prove that the function defined by *f*(*x*) = tan *x* is a continuous function.

**Solution** The function *f*(*x*) = tan *x* = sin cos *x x* . This is defined for all real numbers such

that cos *<sup>x</sup>* <sup>≠</sup> 0, i.e., *<sup>x</sup>* <sup>≠</sup> (2*n* +1) <sup>2</sup> π . We have just proved that both sine and cosine functions are continuous. Thus tan *x* being a quotient of two continuous functions is continuous wherever it is defined.

An interesting fact is the behaviour of continuous functions with respect to composition of functions. Recall that if *f* and *g* are two real functions, then

$$(f \circ g)\,\left(\mathbf{x}\right) \doteq f(\mathbf{g}\,(\mathbf{x})) \,\mathbf{x}$$

is defined whenever the range of *g* is a subset of domain of *f*. The following theorem (stated without proof) captures the continuity of composite functions.

**Theorem 2** Suppose *f* and *g* are real valued functions such that (*f* o *g*) is defined at *c*. If *g* is continuous at *c* and if *f* is continuous at *g* (*c*), then (*f* o *g*) is continuous at *c*.

The following examples illustrate this theorem.

**Example 19** Show that the function defined by *f*(*x*) = sin (*x* 2 ) is a continuous function.

**Solution** Observe that the function is defined for every real number. The function *f* may be thought of as a composition *g* o *h* of the two functions *g* and *h*, where *g* (*x*) = sin *x* and *h* (*x*) = *x* 2 . Since both *g* and *h* are continuous functions, by Theorem 2, it can be deduced that *f* is a continuous function.

**Example 20** Show that the function *f* defined by

$$f(\mathbf{x}) = |1 - \mathbf{x} + |\mathbf{x}| |,$$

where *x* is any real number, is a continuous function.

**Solution** Define *g* by *g* (*x*) = 1 – *x* + | *x*| and *h by h* (*x*) = | *x*| for all real *x*. Then

$$\begin{aligned} (h \circ \mathbf{g})\left(\mathbf{x}\right) &= h\left(\mathbf{g}\left(\mathbf{x}\right)\right) \\ &= h\left(1 - \mathbf{x} + \left\lfloor \mathbf{x} \right\rfloor\right) \\ &= \left\lfloor 1 - \mathbf{x} + \left\lfloor \mathbf{x} \right\rfloor \right\rfloor = f(\mathbf{x}) \end{aligned}$$

In Example 7, we have seen that *h* is a continuous function. Hence *g* being a sum of a polynomial function and the modulus function is continuous. But then *f* being a composite of two continuous functions is continuous.

# **EXERCISE 5.1**

- **1.** Prove that the function *f*(*x*) = 5*x* 3 is continuous at *x* = 0, at *x* = 3 and at *x* = 5.
- **2.** Examine the continuity of the function *f*(*x*) = 2*x* 2 – 1 at *x* = 3.
- **3.** Examine the following functions for continuity.

$$\begin{array}{ll} \text{(a)} \quad f(\mathbf{x}) = \mathbf{x} - \mathbf{5} & \text{(b)} \quad f(\mathbf{x}) = \frac{1}{\mathbf{x} - \mathbf{5}} \text{, } \mathbf{x} \neq \mathbf{5} \\\\ \text{(c)} \quad f(\mathbf{x}) = \frac{\mathbf{x}^2 - 2\mathbf{5}}{\mathbf{x} + \mathbf{5}} \text{, } \mathbf{x} \neq -\mathbf{5} & \text{(d)} \quad f(\mathbf{x}) = |\mathbf{x} - \mathbf{5}| \end{array}$$

- **4.** Prove that the function *f*(*x*) = *x n* is continuous at *x* = *n*, where *n* is a positive integer.
- **5.** Is the function *f* defined by

$$f(\mathbf{x}) = \begin{cases} \mathbf{x}, & \text{if } \mathbf{x} \le 1 \\ \mathbf{S}, & \text{if } \mathbf{x} > 1 \end{cases}$$

continuous at *x* = 0? At *x* = 1? At *x* = 2?

Find all points of discontinuity of *f*, where *f* is defined by

- **6.** 2 3, if 2 ( ) 2 3, if > 2 *x x f x x x* + ≤ = − **7.** | | 3, if 3 ( ) 2 , if 3 < 3 6 2, if 3 *x x f x x x x x* + ≤ − = − − < + ≥ **8.** | | , if 0 ( ) 0, if 0 *x x f x x x* ≠ = = **9.** , if 0 ( ) | | 1, if 0 *x x f x x x* < = − ≥ **10.** <sup>2</sup> 1, if 1 ( ) 1, if 1 *x x f x x x* + ≥ = + < **11.** 3 2 3, if 2 ( ) 1, if 2 *x x f x x x* − ≤ = + > **12.** 10 2 1, if 1 ( ) *x x f x* − ≤ = >
- **13.** Is the function defined by

, if 1

*x x*

$$f'(x) = \begin{cases} x + \mathsf{S}, & \text{if } x \le 1 \\ x - \mathsf{S}, & \text{if } x > 1 \end{cases}$$

a continuous function?

Discuss the continuity of the function *f*, where *f* is defined by

$$\begin{array}{ll} \text{14.} \quad f(\mathbf{x}) = \begin{cases} \text{3, if } 0 \le \mathbf{x} \le 1 \\ \text{4, if } 1 < \mathbf{x} < 3 \\ \text{5, if } 3 \le \mathbf{x} \le 10 \end{cases} \end{array} \quad \text{15.} \quad f(\mathbf{x}) = \begin{cases} \text{2x, if } \mathbf{x} < 0 \\ \mathbf{0}, & \text{if } 0 \le \mathbf{x} \le 1 \\ \text{4x, if } \mathbf{x} \ge 1 \end{cases}$$

$$16. \quad f(\mathbf{x}) = \begin{cases} -2, & \text{if } \mathbf{x} \le -1 \\ 2\mathbf{x}, & \text{if } -1 < \mathbf{x} \le 1 \\ 2, & \text{if } \mathbf{x} > 1 \end{cases}$$

**17.** Find the relationship between *a* and *b* so that the function *f* defined by

$$f(\mathbf{x}) = \begin{cases} a\mathbf{x} + \mathbf{l}, & \text{if } \mathbf{x} \le \mathbf{3} \\ b\mathbf{x} + \mathbf{3}, & \text{if } \mathbf{x} > \mathbf{3} \end{cases}$$

is continuous at *x* = 3.

**18.** For what value of λ is the function defined by

$$f'(\mathbf{x}) = \begin{cases} \lambda \left(\mathbf{x}^2 - 2\mathbf{x}\right), & \text{if } \mathbf{x} \le \mathbf{0}, \\ 4\mathbf{x} + \mathbf{I}, & \text{if } \mathbf{x} > \mathbf{0}. \end{cases}$$

continuous at *x* = 0? What about continuity at *x* = 1?

- **19.** Show that the function defined by *g* (*x*) = *x* [*x*] is discontinuous at all integral points. Here [*x*] denotes the greatest integer less than or equal to *x*.
- **20.** Is the function defined by *f*(*x*) = *x* 2 – sin *x* + 5 continuous at *x* = π?
- **21.** Discuss the continuity of the following functions:
	- (a) *f*(*x*) = sin *x* + cos *x* (b) *f*(*x*) = sin *x* cos *x*
	- (c) *f*(*x*) = sin *x* . cos *x*
- **22.** Discuss the continuity of the cosine, cosecant, secant and cotangent functions.
- **23.** Find all points of discontinuity of *f*, where

$$f'(\mathbf{x}) = \begin{cases} \frac{\sin \mathbf{x}}{\mathbf{x}}, & \text{if } \mathbf{x} < \mathbf{0} \\ \mathbf{x} + \mathbf{1}, & \text{if } \mathbf{x} \ge \mathbf{0} \end{cases}$$

**24.** Determine if *f* defined by

$$f'(x) = \begin{cases} x^2 \sin \frac{1}{x}, & \text{if } x \neq 0\\ 0, & \text{if } x = 0 \end{cases}$$

is a continuous function?

# **25.** Examine the continuity of *f*, where *f* is defined by

$$f'(x) = \begin{cases} \sin x - \cos x, & \text{if } x \neq 0 \\ -1, & \text{if } x = 0 \end{cases}$$

Find the values of *k* so that the function *f* is continuous at the indicated point in Exercises 26 to 29.

**26.** cos , if 2 2 ( ) 3, if 2 *k x x x f x x* π <sup>≠</sup> π − = <sup>π</sup> <sup>=</sup> at *x* = <sup>2</sup> π

- **27.** 2 , if 2 ( ) 3, if 2 *kx x f x x* ≤ = > at *x* = 2
- **28.** 1, if ( ) cos , if *kx x f x x x* + ≤ π = > π at *x* = π
- **29.** 1, if 5 ( ) 3 5, if 5 *kx x f x x x* + ≤ = − > at *x* = 5
- **30.** Find the values of *a* and *b* such that the function defined by

$$\sum f'(x) = \begin{cases} 5, & \text{if } x \not\le 2 \\ ax + b, & \text{if } 2 < x < 10 \\ 21, & \text{if } x \ge 10 \end{cases}$$

is a continuous function.

- **31.** Show that the function defined by *f*(*x*) = cos (*x* 2 ) is a continuous function.
- **32.** Show that the function defined by *f*(*x*) = | cos *x* | is a continuous function.
- **33.** Examine that sin | *x* | is a continuous function.
- **34.** Find all the points of discontinuity of *f* defined by *f*(*x*) = | *x* | | *x* + 1 |.

# **5.3. Differentiability**

Recall the following facts from previous class. We had defined the derivative of a real function as follows:

Suppose *f* is a real function and *c* is a point in its domain. The derivative of *f* at *c* is defined by

$$\lim\_{h \to 0} \frac{f(c+h) - f(c)}{h}$$

provided this limit exists. Derivative of *f* at *c* is denoted by *f* ′(*c*) or ( ( )) | *<sup>c</sup> d f x dx* . The function defined by

$$f'(\mathbf{x}) = \lim\_{h \to 0} \frac{f(\mathbf{x} + h) - f(\mathbf{x})}{h}$$

wherever the limit exists is defined to be the derivative of *f*. The derivative of *f* is denoted by *<sup>f</sup>* ′(*x*) or ( ( )) *<sup>d</sup> f x dx* or if *y* = *f*(*x*) by *dy dx* or *y*′. The process of finding derivative of a function is called differentiation. We also use the phrase *differentiate f*(*x*) *with respect to x* to mean *find f* ′(*x*).

The following rules were established as a part of algebra of derivatives:

- (1) (*u* ± *v*)′ = *u*′ ± *v*′
- (2) (*uv*)′ = *u*′*v* + *uv*′ (Leibnitz or product rule)
- (3) 2 *u u v uv v v* ′ ′ − ′ = , wherever *v* ≠ 0 (Quotient rule).

The following table gives a list of derivatives of certain standard functions:

| Table 5.3 |
|-----------|
|           |
|           |

| f<br>(x)  | x<br>n  | sin x | cos x   | tan x  |
|-----------|---------|-------|---------|--------|
| ′(x)<br>f | nxn – 1 | cos x | – sin x | sec2 x |

Whenever we defined derivative, we had put a caution *provided the limit exists*. Now the natural question is; what if it doesn't? The question is quite pertinent and so is

its answer. If 0 ( ) ( ) lim *h f c h f c* <sup>→</sup> *h* + − does not exist, we say that *f* is not differentiable at *c*.

In other words, we say that a function *f* is differentiable at a point *c* in its domain if both

$$\lim\_{h \to 0^{-}} \frac{f(c+h) - f(\mathfrak{e})}{h} \text{ and } \lim\_{h \to 0^{+}} \frac{f(c+h) - f(c)}{h} \text{ are finite and equal. A function is said}$$

to be differentiable in an interval [*a*, *b*] if it is differentiable at every point of [*a*, *b*]. As in case of continuity, at the end points *a* and *b*, we take the right hand limit and left hand limit, which are nothing but left hand derivative and right hand derivative of the function at *a* and *b* respectively. Similarly, a function is said to be differentiable in an interval (*a*, *b*) if it is differentiable at every point of (*a*, *b*).

**Theorem 3** If a function *f* is differentiable at a point *c*, then it is also continuous at that point.

**Proof** Since *f* is differentiable at *c*, we have

$$\lim\_{\mathbf{x}\to\mathbf{c}}\frac{f(\mathbf{x}) - f(\mathbf{c})}{\mathbf{x} - \mathbf{c}} = f'(\mathbf{c})$$

But for *x* ≠ *c*, we have

$$f(\mathbf{x}) - f(\mathbf{c}) = \frac{f(\mathbf{x}) - f(\mathbf{c})}{\mathbf{x} - \mathbf{c}} \cdot (\mathbf{x} - \mathbf{c})$$

$$\text{Therefore } \qquad \lim\_{\mathbf{x} \to \mathbf{c}} [f(\mathbf{x}) - f(\mathbf{c})] = \lim\_{\mathbf{x} \to \mathbf{c}} \left[ \frac{f(\mathbf{x}) - f(\mathbf{c})}{\mathbf{x} - \mathbf{c}} . \right] \text{.}$$

or lim [ ( )] lim [ ( )] *x c x c f x f c* → → − = ( ) ( ) lim . lim [( )] *x c x c f x f c x c* → → *x c* − <sup>−</sup> <sup>−</sup> = *f* ′(*c*) . 0 = 0

$$\text{or}\qquad\qquad\qquad\qquad\Big\downarrow\!\\\lim\_{\mathbf{x}\to\mathbf{c}}f(\mathbf{x})\;\!=\!\!/\!(\mathcal{C})^{\mathbf{c}}$$

Hence *f* is continuous at *x* = *c*.

**Corollary 1** Every differentiable function is continuous.

We remark that the converse of the above statement is not true. Indeed we have seen that the function defined by *f*(*x*) = | *x* | is a continuous function. Consider the left hand limit

$$\lim\_{h \to 0^+} \frac{f(0+h) - f(0)}{h} = \frac{-h}{h} = -1$$

The right hand limit

$$\lim\_{h \to 0^+} \frac{f(0+h) - f(0)}{h} = \frac{h}{h} = 1$$

Since the above left and right hand limits at 0 are not equal, 0 (0 ) (0) lim *h f h f* <sup>→</sup> *h* + −

does not exist and hence *f* is not differentiable at 0. Thus *f* is not a differentiable function.

# **5.3.1** *Derivatives of composite functions*

To study derivative of composite functions, we start with an illustrative example. Say, we want to find the derivative of *f*, where

$$f(\mathbf{x}) = (2\mathbf{x} + 1)^3$$

One way is to expand (2*x* + 1)<sup>3</sup> using binomial theorem and find the derivative as a polynomial function as illustrated below.

$$\frac{d}{d\mathbf{x}}f(\mathbf{x}) = \frac{d}{d\mathbf{x}}\left[\left(2\mathbf{x} + \mathbf{l}\right)^{3}\right]$$

$$= \frac{d}{d\mathbf{x}}\left(8\mathbf{x}^{3} + 12\mathbf{x}^{2} + 6\mathbf{x} + \mathbf{l}\right)$$

$$= 24\mathbf{x}^{2} + 24\mathbf{x} + 6$$

$$= 6\left(2\mathbf{x} + 1\right)^{2}$$

$$f(\mathbf{x}) = (h \otimes g)(\mathbf{x})$$

Now, observe that *f*(*x*) = (*h* o *g*) (*x*)

where *g*(*x*) = 2*x* + 1 and *h*(*x*) = *x* 3 . Put *t* = *g*(*x*) = 2*x* + 1. Then *f*(*x*) = *h*(*t*) = *t* 3 . Thus

$$\frac{df}{d\mathbf{x}} = \ \ \ \mathbf{6} \ (2\mathbf{x} + \mathbf{1})^2 = \mathbf{3} (2\mathbf{x} + \mathbf{1})^2 \ \ \ \ \ \ \ \mathbf{2} = \mathbf{3} \\ t^2 \ \ \ \ \mathbf{2} = \frac{d\mathbf{h}}{dt} \cdot \frac{dt}{d\mathbf{x}}$$

The advantage with such observation is that it simplifies the calculation in finding the derivative of, say, (2*x* + 1)<sup>100</sup> . We may formalise this observation in the following theorem called the chain rule.

**Theorem 4 (Chain Rule)** Let *f* be a real valued function which is a composite of two

functions *u* and *v* ; i.e., *f* = *v* o *u*. Suppose *t* = *u*(*x*) and if both *dt dx* and *dv dt* exist, we have

$$\frac{df}{d\mathbf{x}} = \frac{d\mathbf{v}}{dt} \cdot \frac{dt}{d\mathbf{x}}$$

We skip the proof of this theorem. Chain rule may be extended as follows. Suppose *f* is a real valued function which is a composite of three functions *u*, *v* and *w*; i.e.,

*f* = (*w* o *u*) o *v*. If *t* = *v* (*x*) and *s* = *u* (*t*), then

$$\frac{d f}{d \mathbf{x}} = \frac{d(\mathbf{w} \bullet \mathbf{u})}{d t} \cdot \frac{d t}{d \mathbf{x}} = \frac{d \mathbf{w}}{d \mathbf{s}} \cdot \frac{d \mathbf{s}}{d t} \cdot \frac{d t}{d \mathbf{x}}$$

provided all the derivatives in the statement exist. Reader is invited to formulate chain rule for composite of more functions.

**Example 21** Find the derivative of the function given by *f*(*x*) = sin (*x* 2 ).

**Solution** Observe that the given function is a composite of two functions. Indeed, if *t* = *u*(*x*) = *x* 2 and *v*(*t*) = sin *t*, then

$$f(\mathbf{x}) \equiv (\nu \text{ o } \mu) \text{ (x)} \equiv \nu(\mu(\mathbf{x})) \equiv \nu(\mathbf{x}^2) \equiv \sin \,\, \mathbf{x}^2$$

Put *t* = *u*(*x*) = *x* 2 . Observe that cos *dv t dt* = and 2 *dt x dx* = exist. Hence, by chain rule

$$\frac{df}{d\mathbf{x}} = \frac{d\mathbf{v}}{dt} \cdot \frac{dt}{d\mathbf{x}} = \cos t \cdot 2\mathbf{x}$$

It is normal practice to express the final result only in terms of *x*. Thus

$$\frac{df}{d\mathbf{x}} = \frac{\cdot}{\cos t \cdot 2} \mathbf{x} = 2\mathbf{x}\cos\mathbf{x}^2$$

# **EXERCISE 5.2**

Differentiate the functions with respect to *x* in Exercises 1 to 8.

- **1.** sin (*x* 2 + 5) **2.** cos (sin *x*) **3.** sin (*ax* + *b*) **4.** sec (tan ( *x* )) **5.** sin ( ) *ax b* + **6.** cos *x* 3 . sin<sup>2</sup> (*x* 5 )
- 

cos ( ) *cx d* +

**7.** ( ) 2 2 cot *x* **8.** cos( *x* )

**9.** Prove that the function *f* given by

$$f(\mathbf{x}) = |\mathbf{x} - \mathbf{1}|, \mathbf{x} \in \mathbf{R}$$

is not differentiable at *x* = 1.

**10.** Prove that the greatest integer function defined by

$$f(\mathbf{x}) = \{\mathbf{x}\}, \ 0 \le \mathbf{x} \le 3$$
  $\text{is not differentiable at } \mathbf{x} = \mathbf{l} \text{ and } \mathbf{x} = 2$ .

# **5.3.2** *Derivatives of implicit functions*

Until now we have been differentiating various functions given in the form *y* = *f*(*x*). But it is not necessary that functions are always expressed in this form. For example, consider one of the following relationships between *x* and *y*:

> *x* – *y* – π = 0 *x* + sin *xy* – *y* = 0

In the first case, we can *solve for y* and rewrite the relationship as *y* = *x* – π. In the second case, it does not seem that there is an easy way to *solve for y*. Nevertheless, there is no doubt about the dependence of *y* on *x* in either of the cases. When a relationship between *x* and *y* is expressed in a way that it is easy to *solve for y* and write *y* = *f*(*x*), we say that *y* is given as an *explicit function* of *x*. In the latter case it is implicit that *y* is a function of *x* and we say that the relationship of the second type, above, gives function *implicitly*. In this subsection, we learn to differentiate implicit functions.

**Example 22** Find *dy dx* if *x* – *y* = π.

**Solution** One way is to solve for *y* and rewrite the above as

$$y = x - \pi$$

$$\frac{dy}{dx} = 1$$

But then

**Alternatively**, *directly* differentiating the relationship w.r.t., *x*, we have

$$\frac{d}{d\mathbf{x}}(\mathbf{x} - \mathbf{y}) = \frac{d\boldsymbol{\pi}}{d\mathbf{x}}$$

Recall that *d dx* π means to differentiate the constant function taking value π

everywhere w.r.t., *x*. Thus

$$\frac{d}{d\mathbf{x}}(\mathbf{x}) - \frac{d}{d\mathbf{x}}(\mathbf{y}) = \mathbf{0}$$

which implies that

$$\frac{d\mathbf{v}}{d\mathbf{x}} = \frac{d\hat{\mathbf{x}}}{d\mathbf{x}} = \mathbf{l}$$

**Example 23** Find *dy dx* , if *y* + sin *y* = cos *x*.

**Solution** We differentiate the relationship directly with respect to *x*, i.e.,

$$\frac{d\boldsymbol{y}}{d\boldsymbol{\alpha}} + \frac{d}{d\boldsymbol{\alpha}}(\sin\boldsymbol{\nu}) = \frac{d}{d\boldsymbol{\alpha}}(\cos\boldsymbol{\nu})$$

which implies using chain rule

$$\frac{d\mathbf{y}}{d\mathbf{x}} + \cos \mathbf{y} \cdot \frac{d\mathbf{y}}{d\mathbf{x}} = -\sin \mathbf{x}$$

$$\text{This gives } \begin{aligned} \frac{d\mathbf{y}}{d\mathbf{x}} &= \frac{\cdot}{d\mathbf{x}} = -\frac{\sin \mathbf{x}}{1 + \cos \mathbf{y}} \\ \text{where } \begin{aligned} \mathbf{y} &\neq (2n+1)\,\,\pi \end{aligned} \end{aligned}$$

# **5.3.3** *Derivatives of inverse trigonometric functions*

We remark that inverse trigonometric functions are continuous functions, but we will not prove this. Now we use chain rule to find derivatives of these functions.

**Example 24** Find the derivative of *f* given by *f*(*x*) = sin–1 *x* assuming it exists.

**Solution** Let *y* = sin–1 *x*. Then, *x* = sin *y*. Differentiating both sides w.r.t. *x*, we get

> 1 = cos *y dy dx dy dx*<sup>=</sup> <sup>1</sup> 1 1 cos *y* cos(sin ) *x* − =

which implies that

Observe that this is defined only for cos *y* ≠ 0, i.e., sin–1 *x* ≠ , 2 2 π π − , i.e., *x* ≠ – 1, 1,

i.e., *x* ∈ (– 1, 1).

To make this result a bit more attractive, we carry out the following manipulation. Recall that for *x* ∈ (– 1, 1), sin (sin–1 *x*) = *x* and hence

$$\cos^2 \chi = 1 - (\sin \chi)^2 = 1 - (\sin \left( (\sin^{-1} \chi) \right))^2 = 1 - \chi^2$$

Also, since *y* ∈ , 2 2 π π <sup>−</sup> , cos *y* is positive and hence cos *y* = <sup>2</sup> 1− *x* Thus, for *x* ∈ (– 1, 1),

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \frac{1}{\cos \mathbf{y}} = \frac{1}{\sqrt{1 - \mathbf{x}^2}}$$

| f(x)          | sin–1 x           | cos-1 x                    | tan-1x            |
|---------------|-------------------|----------------------------|-------------------|
| f<br>1<br>(x) | 1<br>2<br>1−<br>x | −<br>1<br>2<br>−<br>1<br>x | 1<br>2<br>1+<br>x |
| Domain off    | (-1, 1)           | (-1, 1)                    | R                 |

# **EXERCISE 5.3**

$$\begin{aligned} \text{Find } \frac{dy}{dx} & \text{ in the following:}\\ 1. & \quad 2. + 3y = \sin x & 2. \quad 2x + 3y = \sin y & 3. \quad ax + by^2 = \cos y\\ 4. & \quad xy + y^2 = \tan x + y & 5. \quad x^2 + xy + y^2 = 100 & 6. \quad x^3 + x^2y + y^2 + y^2 = 81\\ 7. & \quad \sin^2 y + \cos xy = \kappa & 8. \quad \sin^2 x + \cos^2 y = 1 & 9. \quad y = \sin^{-1} \left(\frac{2x}{1 + x^2}\right) \\\\ 10. & \quad y = \tan^{-1} \left(\frac{3x - x^3}{1 - 3x^2}\right), \quad -\frac{1}{\sqrt{3}} < x < \frac{1}{\sqrt{3}}\\ 11. & \quad y = \cos^{-1} \left(\frac{1 - x^2}{1 + x^2}\right), 0 < x < 1 \\\\ 12. & \quad y = \sin^{-1} \left(\frac{1 - x^2}{1 + x^2}\right), 0 < x < 1 \\\\ 13. & \quad y = \cos^{-1} \left(\frac{2x}{1 + x^2}\right), -1 < x < 1 \\\\ 14. & \quad y = \sin^{-1} \left(2x\sqrt{1 - x^2}\right), -\frac{1}{\sqrt{2}} < x < \frac{1}{\sqrt{2}}\\ 15. & \quad y = \sec^{-1} \left(\frac{1}{2x^2 - 1}\right), 0 < x < \frac{1}{\sqrt{2}} \end{aligned}$$

# **5.4 Exponential and Logarithmic Functions**

Till now we have learnt some aspects of different classes of functions like polynomial functions, rational functions and trigonometric functions. In this section, we shall learn about a new class of (related) functions called exponential functions and logarithmic functions. It needs to be emphasized that many statements made in this section are motivational and precise proofs of these are well beyond the scope of this text.

The Fig 5.9 gives a sketch of *y* = *f* 1 (*x*) = *x*, *y* = *f* 2 (*x*) = *x* 2 , *y* = *f* 3 (*x*) = *x* 3 and *y* = *f* 4 (*x*) = *x* 4 . Observe that the curves get steeper as the power of *x* increases. Steeper the curve, faster is the rate of growth. What this means is that for a fixed increment in the value of *x* (> 1), the increment in the value of *y* = *f n*  (*x*) increases as *n* increases for *n* = 1, 2, 3, 4. It is conceivable that such a statement is true for all positive values of *n*, where *f n*  (*x*) = *x n* . Essentially, this means that the graph of *y* = *f n*  (*x*) *leans* more towards the *y*-axis as *n* increases. For example, consider *f* <sup>10</sup>(*x*) = *x* <sup>10</sup> and *f* <sup>15</sup>(*x*) = *x* <sup>15</sup>. If *x* increases from 1 to 2, *f* 10 increases from 1 to 2<sup>10</sup> whereas *f* 15 increases from 1 to 2<sup>15</sup>. Thus, for the same increment in *x*, *f* <sup>15</sup> grow faster than *f* 10.

Upshot of the above discussion is that the growth of polynomial functions is dependent on the degree of the polynomial function – higher the degree, greater is the growth. The next natural question is:

![](_page_22_Figure_3.jpeg)

Is there a function which grows faster than any polynomial function. The answer is in affirmative and an example of such a function is

$$\mathcal{Y}\_- = f(\mathbf{x}) = 10^\times.$$

Our claim is that this function *f* grows faster than *f n* (*x*) = *x n* for any positive integer *n*. For example, we can prove that 10*<sup>x</sup>* grows faster than *f* <sup>100</sup>(*x*) = *x* <sup>100</sup>. For large values of *x* like *x* = 10<sup>3</sup> , note that *f* 100 (*x*) = (10<sup>3</sup> ) <sup>100</sup> = 10<sup>300</sup> whereas *f*(10<sup>3</sup> ) = <sup>3</sup> <sup>10</sup> 10 = 10<sup>1000</sup> . Clearly *f*(*x*) is much greater than *f* <sup>100</sup>(*x*). It is not difficult to prove that for all *x* > 10<sup>3</sup> , *f*(*x*) > *f* <sup>100</sup> (*x*). But we will not attempt to give a proof of this here. Similarly, by choosing large values of *x*, one can verify that *f*(*x*) grows faster than *f n* (*x*) for any positive integer *n*.

**Definition 3** The exponential function with positive base *b* > 1 is the function

$$\nu = f(\mathbf{x}) = b^x$$

The graph of *y* = 10*<sup>x</sup>* is given in the Fig 5.9.

It is advised that the reader plots this graph for particular values of *b* like 2, 3 and 4. Following are some of the salient features of the exponential functions:

- (1) Domain of the exponential function is **R**, the set of all real numbers.
- (2) Range of the exponential function is the set of all positive real numbers.
- (3) The point (0, 1) is always on the graph of the exponential function (this is a restatement of the fact that *b* 0 = 1 for any real *b* > 1).
- (4) Exponential function is ever increasing; i.e., as we move from left to right, the graph rises above.

(5) For very large negative values of *x*, the exponential function is very close to 0. In other words, in the second quadrant, the graph approaches *x*-axis (but never meets it).

Exponential function with base 10 is called the *common exponential function*. In the Appendix A.1.4 of Class XI, it was observed that the sum of the series

$$1 + \frac{1}{1!} + \frac{1}{2!} + \dots$$

is a number between 2 and 3 and is denoted by *e*. Using this *e* as the base we obtain an extremely important exponential function *y* = *e x .*

This is called *natural exponential function*.

It would be interesting to know if the inverse of the exponential function exists and has *nice* interpretation. This search motivates the following definition.

**Definition 4** Let *b* > 1 be a real number. Then we say logarithm of *a* to base *b* is *x* if *b x* = *a*.

Logarithm of *a* to base *b* is denoted by log*<sup>b</sup> a*. Thus log*<sup>b</sup> a* = *x* if *b x* = *a*. Let us work with a few explicit examples to get a feel for this. We know 2<sup>3</sup> = 8. In terms of logarithms, we may rewrite this as log<sup>2</sup> 8 = 3. Similarly, 10<sup>4</sup> = 10000 is equivalent to saying log10 10000 = 4. Also, 625 = 5<sup>4</sup> = 25<sup>2</sup> is equivalent to saying log<sup>5</sup> 625 = 4 or log25 625 = 2.

On a slightly more mature note, fixing a base *b* > 1, we may look at logarithm as a function from positive real numbers to all real numbers. This function, called the *logarithmic function*, is defined by

$$\begin{array}{c} \log\_b: \mathbf{R}^+ \to \mathbf{R} \\ \mathbf{x} \to \log\_b \mathbf{x} = \mathbf{y} \quad \text{if } b^\circ = \mathbf{x} \end{array}$$

As before if the base *b* = 10, we say it is *common logarithms* and if *b* = *e*, then we say it is *natural logarithms*. Often natural logarithm is denoted by *ln*. *In this chapter*, *log x denotes the logarithm function to base e*, i.e., *ln x* will be written as simply log *x*. The Fig 5.10 gives the plots of logarithm function to base 2, *e* and 10.

Some of the important observations about the logarithm function to any base *<sup>b</sup>* > 1 are listed below: **Fig 5.10**

![](_page_23_Figure_13.jpeg)

- (1) We cannot make a meaningful definition of logarithm of non-positive numbers and hence the domain of log function is **R**<sup>+</sup> .
- (2) The range of log function is the set of all real numbers.
- (3) The point (1, 0) is always on the graph of the log function.
- (4) The log function is ever increasing, i.e., as we move from left to right the graph rises above.
- (5) For *x* very near to zero, the value of log *x* can be made lesser than any given real number. In other words in the fourth quadrant the graph approaches *y*-axis (but never meets it).
- (6) Fig 5.11 gives the plot of *y* = *e x* and *y* = *ln x*. It is of interest to observe that the two curves are the mirror images of each other reflected in the line *y* = *x*.

![](_page_24_Figure_7.jpeg)

 **Fig 5.11**

Two properties of 'log' functions are proved below:

(1) There is a standard change of base rule to obtain log*<sup>a</sup> p* in terms of log*<sup>b</sup> p*. Let log*<sup>a</sup> p* = α, log*<sup>b</sup> p* = β and log*<sup>b</sup> a* = γ. This means *a* α = *p*, *b* β = *p* and *b* γ = *a*. Substituting the third equation in the first one, we have

$$\begin{aligned} \brace{\bigcup\_{\alpha \in \Phi} (b^{\gamma})^{\alpha} = b^{\gamma a} = p} \quad &(b^{\gamma})^{\alpha} = b^{\gamma a} = p \\ \text{Using this in the second equation, we get} \\ \phantom{\rule{10.0pt}{ $b^{\delta} = p = b^{\gamma a}$ }} \quad &b^{\delta} = p = b^{\gamma a} \end{aligned}$$

which implies β = αγ or α = β γ . But then

$$\log\_a p = \frac{\log\_b p}{\log\_b a}$$

(2) Another interesting property of the log function is its effect on products. Let log*<sup>b</sup> pq* = α. Then *b* α = *pq*. If log*<sup>b</sup> p* = β and log*<sup>b</sup> q* = γ, then *b* β = *p* and *b* γ = *q*. But then *b* α = *pq* = *b*<sup>β</sup>*b* γ = *b* β + γ

which implies α = β + γ, i.e.,

$$
\log\_b pq = \log\_b p + \log\_b q
$$

A particularly interesting and important consequence of this is when *p* = *q*. In this case the above may be rewritten as

$$
\log\_b p^2 = \log\_b p + \log\_b p = 2\log p
$$

An easy generalisation of this (left as an exercise!) is

$$\log\_b p^\* = n \log p$$

for any positive integer *n*. In fact this is true for any real number *n*, but we will not attempt to prove this. On the similar lines the reader is invited to verify

$$\log\_b \frac{\mathbf{x}}{\mathbf{y}} = \log\_b \mathbf{x} - \log\_b \mathbf{y}$$

**Example 25** Is it true that *x* = *e* log *x* for all real *x*?

**Solution** First, observe that the domain of log function is set of all positive real numbers. So the above equation is not true for non-positive real numbers. Now, let *y* = *e* log *x* . If *y* > 0, we may take logarithm which gives us log *y* = log (*e* log *x* ) = log *x* . log *e* = log *x*. Thus *y* = *x*. Hence *x* = *e* log *x* is true only for positive values of *x*.

One of the striking properties of the natural exponential function in differential calculus is that it doesn't change during the process of differentiation. This is captured in the following theorem whose proof we skip.

#### **Theorem 5\***

- (1) The derivative of *e x* w.r.t., *x* is *e x* ; i.e., *d dx* (*<sup>e</sup> x* ) = *e x* .
- (2) The derivative of log *x* w.r.t., *x* is <sup>1</sup> *x* ; i.e., *d dx* (log *x*) = 1 *x* .

**Example 26** Differentiate the following w.r.t. *x*:

$$\begin{array}{ccccccccc} \text{(i)} & e^{-x} & \text{(ii)} & \sin\left(\text{lóg}\,\text{x}\right), x \ge 0 & \text{(iii)} & \cos^{-1}\left(e^{x}\right) & \text{(iv)} & e^{\cos x} \end{array}$$

#### **Solution**

(i) Let *y* = *e* – *x* . Using chain rule, we have

$$\frac{d\mathbf{y}}{d\mathbf{x}} = e^{-\mathbf{x}} \cdot \frac{d}{d\mathbf{x}} \ (-\mathbf{x}) \equiv -e^{-\mathbf{x}}$$

(ii) Let *y* = sin (log *x*). Using chain rule, we have

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \cos\left(\log\mathbf{x}\right) \cdot \frac{d}{d\mathbf{x}}\left(\log\mathbf{x}\right) = \frac{\cos\left(\log\mathbf{x}\right)}{\mathbf{x}}$$

*<sup>\*</sup> Please see supplementary material on Page 222.*

(iii) Let *y* = cos–1 (*e x* ). Using chain rule, we have

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \frac{-1}{\sqrt{1 - \left(e^{x}\right)^{2}}} \cdot \frac{d}{d\mathbf{x}} \left(e^{x}\right) = \frac{-e^{x}}{\sqrt{1 - e^{2x}}}$$

(iv) Let *y* = *e* cos *x* . Using chain rule, we have

$$\frac{d\boldsymbol{y}}{d\boldsymbol{x}} = \stackrel{\cdot}{\boldsymbol{e}} e^{\cos x} \cdot (-\sin x) = -(\sin x) \stackrel{\cdot}{\boldsymbol{e}} e^{\cos x}$$

**EXERCISE 5.4**

Differentiate the following w.r.t. *x*:

$$\begin{array}{llll} \text{1.} & \frac{e^{x}}{\sin x} & \text{2.} & e^{\sin^{-1}x} & \text{3.} & e^{x^{i}} \\\\ \text{4.} & \sin \left(\tan^{-1} e^{x}\right) & \text{5.} & \log \left(\cos e^{x}\right) & \text{6.} & e^{x} + e^{x^{i}} + \dots + e^{x^{i}} \\\\ \text{7.} & \sqrt{e^{\sqrt{x}}} & \text{x > 0} & \text{8.} & \log \left(\log x\right), x > \text{I} & \text{9.} & \frac{\cos x}{\log x} & x > 0 \\\\ \text{10.} & \cos \left(\log x + e^{\circ}\right), x > 0 & & & & \end{array}$$

# **5.5. Logarithmic Differentiation**

In this section, we will learn to differentiate certain special class of functions given in the form

$$\mathcal{Y} \equiv f(\mathbf{x}) \equiv [\boldsymbol{\mu}(\mathbf{x})]^{\nu(\mathbf{x})}$$

By taking logarithm (to base *e*) the above may be rewritten as

$$\log\_{\cdot} y = \nu(x) \log\_{\cdot} [\mu(\alpha)]^{\frac{1}{2}}$$

Using chain rule we may differentiate this to get

$$\frac{1}{\nu \chi} \cdot \frac{d\nu}{d\mathbf{x}} = \nu(\mathbf{x}) \cdot \frac{1}{\nu(\mathbf{x})} \cdot u'(\mathbf{x}) + \nu'(\mathbf{x}) \cdot \log \left[ u(\mathbf{x}) \right]$$

which implies that

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \mathcal{y} \left[ \frac{\nu(\mathbf{x})}{\mu(\mathbf{x})} \cdot \mu'(\mathbf{x}) + \nu'(\mathbf{x}) \cdot \log \left[ \mu(\mathbf{x}) \right] \right]$$

The main point to be noted in this method is that *f*(*x*) and *u*(*x*) must always be positive as otherwise their logarithms are not defined. This process of differentiation is known as *logarithms differentiation* and is illustrated by the following examples:

$$\text{Example 27 Differention } \sqrt{\frac{(\text{x} - \text{3})\left(\text{x}^2 + 4\right)}{3\text{x}^2 + 4\text{x} + 5}} \text{ w.r.t. x.}$$

$$\text{Solution Let } \begin{array}{l} \text{Let } \ y = \sqrt{\frac{(x-3)\left(x^2+4\right)}{\left(3x^2+4x+5\right)}} \end{array}$$

Taking logarithm on both sides, we have

$$\log y = \frac{1}{2} \left[ \log \left( \mathbf{x} - \mathbf{3} \right) + \log \left( \mathbf{x}^2 + 4 \right) - \log \left( 3\mathbf{x}^2 + 4\mathbf{x} + \mathbf{S} \right) \right]$$

Now, differentiating both sides w.r.t. *x*, we get

$$\frac{1}{y} \cdot \frac{dy}{dx} = \frac{1}{2} \left[ \frac{1}{(x-3)} + \frac{2x}{x^2 + 4} - \frac{6x + 4}{3x^2 + 4x + 5} \right]$$

$$\frac{dy}{dx} = \frac{y}{2} \left[ \frac{1}{(x-3)} + \frac{2x}{x^2 + 4} - \frac{6x + 4}{3x^2 + 4x + 5} \right]$$

$$= \frac{1}{2} \sqrt{\frac{(x-3)(x^2 + 4)}{3x^2 + 4x + 5}} \left[ \frac{1}{(x-3)} + \frac{2x}{x^2 + 4} - \frac{6x + 4}{3x^2 + 4x + 5} \right]$$

or

$$\begin{array}{l} \text{Example 28 Differentiate } a^x \text{ w.r.t. x, where } a \text{ is a positive constant.}\\ \text{Solution } \text{Let } y = a^x. \text{ Then }\\ \qquad \qquad \log y = x \log a \end{array}$$

Differentiating both sides w.r.t. *x*, we have

$$
\frac{1}{\nu} \frac{d\wp}{dx} = \log a
$$

$$
\frac{d\wp}{dx} = \wp \log a
$$

or

$$\text{"plus"}$$

$$\begin{aligned} \text{Thus} \quad \begin{aligned} \text{Thus} \\ \text{Alterm:} \end{aligned} \quad \begin{aligned} \frac{d}{dx}(a^x) &= a^x \log a \\ \frac{d}{dx}(a^x) &= \frac{d}{dx}(e^{x \log a}) = e^{x \log a} \frac{d}{dx}(x \log a) \\ &= e^{x \log a} \cdot \log a = a^x \log a. \end{aligned}$$

$$\textbf{Alternatively}$$

#### **Example 29** Differentiate *x* sin *x* , *x* > 0 w.r.t. *x*.

**Solution** Let *y* = *x* sin *x .* Taking logarithm on both sides, we have

> 1 . *dy*

log *y* = sin *x* log *x*

Therefore

or

$$\frac{1}{y}\frac{d\mathbf{y}}{d\mathbf{x}} = \stackrel{\cdot}{(\sin x)}\frac{1}{\mathbf{x}} + \log x \cos x$$

.

*y dx*<sup>=</sup> sin (log ) log (sin ) *<sup>d</sup> <sup>d</sup>*

*x x x x dx dx* +

$$\begin{aligned} \text{or} \qquad & \frac{d\boldsymbol{y}}{d\boldsymbol{x}} = \mathcal{Y} \left[ \frac{\sin \boldsymbol{x}}{\boldsymbol{x}} + \cos \boldsymbol{x} \log \boldsymbol{x} \right] \\ &= \boldsymbol{x}^{\sin \boldsymbol{x}} \left[ \frac{\sin \boldsymbol{x}}{\boldsymbol{x}} + \cos \boldsymbol{x} \log \boldsymbol{x} \right] \\ &= \boldsymbol{x}^{\sin \boldsymbol{x} - 1} \cdot \sin \boldsymbol{x} + \boldsymbol{x}^{\sin \boldsymbol{x}} \cdot \cos \boldsymbol{x} \log \boldsymbol{x} \end{aligned}$$

**Example 30** Find *dy dx* , if *y <sup>x</sup>* + *x <sup>y</sup>* + *x <sup>x</sup>* = *a b*

**Solution** Given that *y <sup>x</sup>* + *x <sup>y</sup>* + *x <sup>x</sup>* = *a b* . Putting *u* = *y x* , *v* = *x y* and *w* = *x x* , we get *u* + *v* + *w* = *a*

$$\text{Therefore}\qquad\qquad\qquad\frac{d\mu}{dx} + \frac{dv}{d\mathbf{x}} + \frac{dw}{d\mathbf{x}} = 0\qquad\qquad\qquad\qquad\dots \text{(l)}$$

*b*

Now, *u* = *y x* . Taking logarithm on both sides, we have

log *u* = *x* log *y*

Differentiating both sides w.r.t. *x*, we have

$$\frac{1}{u} \cdot \frac{du}{dx} = \chi \frac{d}{dx}(\log y) + \log y \frac{d}{dx}(\mathbf{x})$$

$$= \chi \frac{1}{y} \cdot \frac{d\mathbf{y}}{dx} + \log y \cdot \mathbf{l}$$

$$\frac{du}{dx} = u \left(\frac{\chi}{y} \frac{d\mathbf{y}}{dx} + \log y\right) = \chi^x \left[\frac{\chi}{y} \frac{d\mathbf{y}}{dx} + \log y\right] \quad \dots (2)$$

So

Also *v* = *x y* Taking logarithm on both sides, we have

$$
\log \nu = \nu \log \ge 1
$$

Differentiating both sides w.r.t. *x*, we have

$$\frac{1}{\nu} \cdot \frac{d\nu}{d\mathbf{x}} = \nu \frac{d}{d\mathbf{x}} (\log x) + \log x \frac{d\mathbf{y}}{d\mathbf{x}}$$

$$= \nu \cdot \frac{1}{\mathbf{x}} + \log x \cdot \frac{d\mathbf{y}}{d\mathbf{x}}$$

$$\text{So } \qquad \frac{d\nu}{d\mathbf{x}} = \nu \left[ \frac{\nu}{\mathbf{x}} + \log x \frac{d\nu}{d\mathbf{x}} \right]$$

$$= \mathbf{x}^{\nu} \left[ \frac{\nu}{\mathbf{x}} + \log x \frac{d\nu}{d\mathbf{x}} \right] \tag{13}$$

$$\text{Again } \qquad \nu = \mathbf{x}^{\nu}$$

So

Taking logarithm on both sides, we have

$$
\log w = x \log x.
$$

Differentiating both sides w.r.t. *x*, we have

$$\frac{1}{w} \cdot \frac{dw}{dx} = x \frac{d}{dx} (\log x) + \log x \cdot \frac{d}{dx}(x)$$

$$\begin{aligned} \left(\sum\right) &= x \cdot \frac{1}{x} + \log x \cdot 1\\ &= \frac{dw}{dx} = w \left(1 + \log x\right) \\ &= x^x \left(1 + \log x\right) &\dots \end{aligned}$$

. log

*x y x x*

i.e.

From (1), (2), (3), (4), we have

$$\left(\mathbf{y}^{x}\left(\frac{\mathbf{x}}{\mathbf{y}}\frac{d\mathbf{y}}{d\mathbf{x}}+\log\mathbf{y}\right)\right)+\mathbf{x}^{y}\left(\frac{\mathbf{y}}{\mathbf{x}}+\log\mathbf{x}\frac{d\mathbf{y}}{d\mathbf{x}}\right)+\mathbf{x}^{x}\left(1+\log\mathbf{x}\right)=\mathbf{0}$$

$$\text{or}\qquad\left(\mathbf{x}\cdot\mathbf{y}^{x-1}+\mathbf{x}^{y}\cdot\log\mathbf{x}\right)\frac{d\mathbf{y}}{d\mathbf{x}}=-\mathbf{x}^{x}\left(1+\log\mathbf{x}\right)-\mathbf{y}\cdot\mathbf{x}^{y-1}-\mathbf{y}^{x}\log\mathbf{y}$$

$$\text{Therefore }\qquad\qquad\qquad\qquad\frac{d\mathbf{y}}{d\mathbf{x}}=\frac{-\left[\mathbf{y}^{x}\log\mathbf{y}+\mathbf{y}\cdot\mathbf{x}^{y-1}+\mathbf{x}^{x}(\mathbf{I}+\log\mathbf{x})\right]}{\mathbf{x}\cdot\mathbf{y}^{x-1}+\mathbf{x}^{y}\log\mathbf{x}}$$

Therefore

# **EXERCISE 5.5**

Differentiate the functions given in Exercises 1 to 11 w.r.t. *x*.

- **1.** cos *x* . cos 2*x* . cos 3*x* **2.** ( 1) ( 2) ( 3) ( 4) ( 5) *x x x x x* − − − − − **3.** (log *x*) cos *<sup>x</sup>* **4.** *x x* – 2sin *<sup>x</sup>* **5.** (*x +* 3)<sup>2</sup> . (*x* + 4)<sup>3</sup> . (*x* + 5)<sup>4</sup> **6.** 1 1 <sup>1</sup> *x x x x x* <sup>+</sup> + + **7.** (log *x*) *x* + *x* log *<sup>x</sup>* **8.** (sin *x*) *x* + sin–1 *x* **9.** *x* sin *x* + (sin *x*) cos *<sup>x</sup>* **10.** 2 cos 2 1 1 *x x x x x* + + − **11.** (*x* cos *x*) *x* + 1 ( sin ) *<sup>x</sup> x x* Find *dy dx* of the functions given in Exercises 12 to 15.
- **12.** *x y* + *y x* = 1 **13.** *y <sup>x</sup>* = *x y*
- **14.** (cos *x*) *y* = (cos *y*) *<sup>x</sup>* **15.** *xy* = *e*
- **16.** Find the derivative of the function given by *f*(*x*) = (1 + *x*) (1 + *x* 2 ) (1 + *x* 4 ) (1 + *x* 8 ) and hence find *f* ′(1).
- **17.** Differentiate (*x* 2 – 5*x* + 8) (*x* 3 + 7*x* + 9) in three ways mentioned below:
	- (i) by using product rule
	- (ii) by expanding the product to obtain a single polynomial.
	- (iii) by logarithmic differentiation.

Do they all give the same answer?

**18.** If *u*, *v* and *w* are functions of *x*, then show that

$$\frac{d}{d\mathbf{x}}\text{ ( $u$ .  $v$ .  $w$ )} = \frac{du}{d\mathbf{x}}\text{  $v$ .  $w+u$ . }\frac{d\mathbf{v}}{d\mathbf{x}}\text{ .  $w+u$ .  $v$ }\text{ }\frac{d\mathbf{w}}{d\mathbf{x}}$$

(*x* – *y*)

in two ways - first by repeated application of product rule, second by logarithmic differentiation.

# **5.6 Derivatives of Functions in Parametric Forms**

Sometimes the relation between two variables is neither explicit nor implicit, but some link of a third variable with each of the two variables, separately, establishes a relation between the first two variables. In such a situation, we say that the relation between them is expressed via a third variable. The third variable is called the parameter. More precisely, a relation expressed between two variables *x* and *y* in the form *x* = *f*(*t*), *y* = *g* (*t*) is said to be parametric form with *t* as a parameter.

In order to find derivative of function in such form, we have by chain rule.

$$
\frac{d\mathbf{v}}{dt} = \frac{d\mathbf{y}}{d\mathbf{x}} \cdot \frac{d\mathbf{x}}{dt}
$$

$$
\frac{d\mathbf{y}}{dt} = \frac{\frac{d\mathbf{y}}{dt}}{\frac{d\mathbf{x}}{dt}} \left(\text{whenever } \frac{d\mathbf{x}}{dt} \neq 0\right)
$$

*x* = *a* cos θ, *y* = *a* sin θ

Thus

So

or

$$\frac{dy}{dt} = \frac{\cdot}{f'(t)} \left( \text{as} \frac{dy}{dt} = \text{g'}(t) \text{and} \frac{dx}{dt} = f'(t) \right) \text{ [provided} \, f'(t) \neq 0\text{]}$$

$$\text{Example 31 Find } \frac{d\mathbf{y}}{d\mathbf{x}} \text{, if } \mathbf{x} = a\cos\theta, \mathbf{y} = a\sin\theta.$$

**Solution** Given that

$$\begin{aligned} \text{Therefore} \qquad \frac{d\mathbf{x}}{d\theta} &= -a \sin \theta, \frac{d\mathbf{y}}{d\theta} = a \cos \theta \\ \text{or} \qquad \frac{d\mathbf{y}}{d\theta} &= -a \sin \theta \end{aligned}$$

$$\text{Hence}\qquad\qquad\frac{d\mathbf{y}}{d\mathbf{x}}=\frac{\frac{\mathbf{x}}{d\boldsymbol{\Theta}}}{\frac{d\mathbf{x}}{d\boldsymbol{\Theta}}}=\frac{a\cos\theta}{-a\sin\theta}=-\cot\theta$$

**Example 32** Find *dy dx* , if *x* = *at*<sup>2</sup> , *y* = 2*at*. **Solution** Given that *x* = *at*<sup>2</sup> , *y* = 2*at*

$$\frac{d\mathbf{x}}{dt} = 2at \quad \text{and} \quad \frac{d\mathbf{y}}{dt} = 2at$$

$$\text{Therefore } \qquad \qquad \qquad \frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}} = \frac{2a}{2at} = \frac{1}{t}$$

**Example 33** Find *dy dx* , if *x* = *a* (θ + sin θ), *y* = *a* (1 – cos θ). **Solution** We have *dx d*θ <sup>=</sup>*a*(1 + cos θ), *dy d*θ = *a* (sin θ) Therefore *dy dx*<sup>=</sup> sin tan (1 cos ) 2 *dy d a dx a d* θ θ θ = = + θ θ

A**Note** It may be noted here that *dy dx* is expressed in terms of parameter only without directly involving the main variables *x* and *y*.

**Example 34** Find 2 2 2 3 3 3 , if *dy x y a dx* + = . **Solution** Let *x* = *a* cos<sup>3</sup> θ, *y* = *a* sin<sup>3</sup> θ. Then 2 2 3 3 *x y* + = 2 2 3 3 3 3 ( cos ) ( sin ) *a a* θ + θ = 2 2 <sup>3</sup> 2 2 <sup>3</sup> *a* (cos (sin ) θ + θ = *a*

Hence, *x* = *a* cos<sup>3</sup>θ, *y* = *a* sin<sup>3</sup>θ is parametric equation of 2 2 2 3 3 3 *x y a* + =

$$\frac{d\mathbf{x}}{d\theta} = -3a\cos^2\theta\sin\theta \text{ and } \frac{d\mathbf{y}}{d\theta} = 3a\sin^2\theta\cos\theta$$

Therefore

Now

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \frac{\frac{d\mathbf{y}}{d\Theta}}{\frac{d\mathbf{x}}{d\Theta}} = \frac{3a\sin^2\theta\cos\Theta}{-3a\cos^2\theta\sin\Theta} = -\tan\Theta = -\sqrt[3]{\frac{\mathbf{y}}{\mathbf{x}}}$$

**EXERCISE 5.6**

If *x* and *y* are connected parametrically by the equations given in Exercises 1 to 10, without eliminating the parameter, Find *dy dx* . **1.** *x* = 2*at*<sup>2</sup> , *y* = *at*<sup>4</sup> **2.** *x* = *a* cos θ, *y* = *b* cos θ **3.** *x* = sin *t*, *y* = cos 2*t* **4.** *x* = 4*t*, *y* = 4 *t* **5.** *x* = cos θ – cos 2θ, *y* = sin θ – sin 2θ **6.** *x* = *a* (θ – sin θ), *y* = *a* (1 + cos θ) **7.** *x* = 3 sin cos 2 *t t* , 3 cos cos 2 *t y t* = **8.** cos log tan 2 *t x a t* = + *y* = *a* sin *t* **9.** *x* = *a* sec θ, *y* = *b* tan θ **10.** *x* = *a* (cos θ + θ sin θ), *y* = *a* (sin θ – θ cos θ) **11.** If 1 1 sin cos , , show that *<sup>t</sup> <sup>t</sup> dy y x a y a dx x* − − = = = − **5.7 Second Order Derivative**

Let *y* = *f*(*x*). Then

$$\underbrace{\text{dy}}\_{\text{d}\mathbf{x}} = f'(\mathbf{x}) \bigvee \underbrace{\bigvee \dots \bigvee \dots}\_{\text{d}\mathbf{x} \dots \bigvee \dots} \bigvee \tag{1}$$

If *f* ′(*x*) is differentiable, we may differentiate (1) again w.r.t. *x*. Then, the left hand

side becomes *d dy dx dx* which is called the *second order derivative* of *y* w.r.t. *x* and

is denoted by 2 2 *d y dx* . The second order derivative of *f*(*x*) is denoted by *f* ″(*x*). It is also denoted by D<sup>2</sup> *y* or *y*″ or *y* 2 if *y* = *f*(*x*). We remark that higher order derivatives may be defined similarly.

**Example 35** Find 2 2 *d y dx* , if *y* = *x* 3 + tan *x*.

**Solution** Given that *y* = *x* 3 + tan *x*. Then

$$\begin{aligned} \frac{d\mathbf{y}}{d\mathbf{x}} &= 3\mathbf{x}^2 + \sec^2 \mathbf{x} \\ \frac{d^2\mathbf{y}}{d\mathbf{x}^2} &= \frac{d}{d\mathbf{x}} \left( 3\mathbf{x}^2 + \sec^2 \mathbf{x} \right) \\ &= 6\mathbf{x} + 2\sec \mathbf{x} \cdot \sec \mathbf{x} \tan \mathbf{x} = 6\mathbf{x} + 2\sec^2 \mathbf{x} \tan \mathbf{x} \end{aligned}$$

Therefore

**Example 36** If *y* = A sin *x* + B cos *x*, then prove that 2 2 0 *d y y dx* + = .

**Solution** We have

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \mathbf{A}\cos\mathbf{x} - \mathbf{B}\sin\mathbf{x}$$

$$\frac{d^2\mathbf{y}}{d\mathbf{x}^2} = \frac{d}{d\mathbf{x}}\left(\mathbf{A}\cos\mathbf{x} - \mathbf{B}\sin\mathbf{x}\right)$$

$$= -\mathbf{A}\sin\mathbf{x} - \mathbf{B}\cos\mathbf{x} = -\mathbf{y}$$

$$\frac{d^2\mathbf{y}}{d\mathbf{x}^2} + \mathbf{y} = \mathbf{0}$$

$$\text{37. If } \mathbf{y} = 3e^{2\mathbf{x}} + 2e^{3\mathbf{x}} \text{ proves that } \frac{d^2\mathbf{y}}{d\mathbf{x}} - 5\frac{d\mathbf{y}}{d\mathbf{y}} + 6\mathbf{y} = 0$$

Hence

and

**Example 37** If *y* = 3*e* 2*x* + 2*e* 3*x* , prove that 2 5 6 0 *d y dy y dx dx* − + = .

**Solution** Given that *y* = 3*e* 2*x* + 2*e* 3*x* . Then

$$\frac{d\mathbf{y}}{d\mathbf{x}} = 6e^{2\mathbf{x}} + 6e^{3\mathbf{x}} = 6\left(e^{2\mathbf{x}} + e^{3\mathbf{x}}\right)$$

$$\text{Therefore}$$

$$\frac{d^2y}{d\mathbf{x}^2} = 12e^{2\mathbf{x}} + 18e^{3\mathbf{x}} = 6\left(2e^{2\mathbf{x}} + 3e^{3\mathbf{x}}\right)$$

Hence

$$\begin{aligned} \frac{d^2y}{d\mathbf{x}^2} - \mathbf{5} \frac{d\mathbf{y}}{d\mathbf{x}} + 6\mathbf{y} &= 6 \ (2e^{2\mathbf{x}} + \mathbf{3}e^{3\mathbf{x}})\\ -\mathbf{3} \ (e^{2\mathbf{x}} + e^{3\mathbf{x}}) + 6 \ (3e^{2\mathbf{x}} + 2e^{3\mathbf{x}}) &= 0 \end{aligned}$$

$$\text{Example 38 If } y = \sin^{-1} x \text{, show that } (1 - x^2) \, \, \frac{d^2 y}{d x^2} - x \frac{dy}{d x} = 0 \dots$$

**Solution** We have *y* = sin–1 *x*. Then

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \frac{1}{\sqrt{(1 - x^2)}}$$

2 (1 ) 1 *dy x*

*dx* − =

or

$$\text{So}\qquad\qquad\qquad\frac{d}{d\mathbf{x}}\Big(\sqrt{\left(1-\mathbf{x}^{2}\right)}\cdot\frac{d\mathbf{y}}{d\mathbf{x}}\Big)=\mathbf{0}$$

$$\text{or} \qquad \qquad \qquad \sqrt{\left(1-\mathbf{x}^2\right)} \cdot \frac{d^2y}{d\mathbf{x}^2} + \frac{dy}{d\mathbf{x}} \cdot \frac{d}{d\mathbf{x}} \Big| \sqrt{\left(1-\mathbf{x}^2\right)} \Big|\_{\stackrel{\circ}{\rightarrow}} = 0$$

$$\sqrt{\left(1-\chi^2\right)}\cdot\frac{d^2\chi}{d\chi^2}\cdot\frac{d\psi}{d\chi}\cdot\frac{2\chi}{2\sqrt{1-\chi^2}}\stackrel{\leftharpoons}{=}0$$

or

Hence 2 2 2 (1 ) 0 *d y dy x x dx dx* − − =

**Alternatively**, Given that *y* = sin–1 *x*, we have

$$\mathcal{Y}\_1 = \frac{1}{\sqrt{1 - \mathbf{x}^2}}, \text{ i.e., } \left(1 - \mathbf{x}^2\right) \mathcal{Y}\_1^2 = 1$$

$$\begin{array}{ll}\text{So} & \left(\mathbf{l}-\mathbf{x}^{2}\right)\cdot\mathbf{2}\boldsymbol{\uprho}\_{1}\mathbf{\color[rgb]{0,0,1}{0}}+\boldsymbol{\uprho}\_{1}^{2}\left(\mathbf{0}-\mathbf{2}\mathbf{x}\right)=\mathbf{0} \\\text{Hence} & \left(\mathbf{l}-\mathbf{x}^{2}\right)\boldsymbol{\uprho}\_{2}-\mathbf{x}\boldsymbol{\uprho}\_{1}=\mathbf{0} \end{array}$$

**EXERCISE 5.7**

Find the second order derivatives of the functions given in Exercises 1 to 10.

**1.** *x* 2 + 3*x* + 2 **2.** *x* <sup>20</sup> **3.** *x* . cos *x* **4.** log *x* **5.** *x* 3 log *x* **6.** *e x* sin 5*x* **7.** *e* <sup>6</sup>*<sup>x</sup>*cos 3*x* **8.** tan–1 *x* **9.** log (log *x*) **10.** sin (log *x*) **11.** If *y* = 5 cos *x* – 3 sin *x*, prove that 2 2 0 *d y y dx* + =

$$12. \quad \text{If } \mathcal{y} = \cos^{-1} x \text{, Find } \begin{array}{c} d^2 \mathcal{y} \\ d\mathfrak{x}^2 \end{array} \\ \text{in terms of } \mathcal{y} \text{ alone.}$$

**13.** If *y* = 3 cos (log *x*) + 4 sin (log *x*), show that *x* 2 *y*2 + *xy*<sup>1</sup> + *y* = 0

$$14. \quad \text{If } y = \text{A}e^{m\mathbf{x}} + \text{B}e^{m\mathbf{x}}\text{, show that } \frac{d^2y}{d\mathbf{x}^2} - (m+n)\frac{dy}{d\mathbf{x}} + mny = 0$$

**15.** If *y* = 500*e* 7*x* + 600*e –*7*x* , show that 2 2 <sup>49</sup> *d y y dx* =

$$16. \quad \text{If } e^v(x+1) = 1 \text{, show that } \frac{d^2y}{dx^2} = \left(\frac{dy}{dx}\right)^2.$$

**17.** If *y* = (tan–1 *x*) 2 , show that (*x* 2 + 1)<sup>2</sup> *y* 2 + 2*x* (*x* 2 + 1) *y* 1 = 2

# *Miscellaneous Examples*

**Example 39** Differentiate w.r.t. *x*, the following function:

$$\text{(i)}\quad\sqrt{3x+2}+\frac{1}{\sqrt{2x^2+4}}\qquad\text{(ii)}\quad\log\_2(\log x)$$

**Solution**

$$\text{(i)}\quad \text{Let } y = \sqrt{3x+2} + \frac{1}{\sqrt{2x^2+4}} = \left(3x+2\right)^{\frac{1}{2}} + \left(2x^2+4\right)^{-\frac{1}{2}}$$

Note that this function is defined at all real numbers <sup>2</sup> 3 *x* > − . Therefore

$$\frac{d\psi}{dx} = \frac{1}{2} (3x+2)^{\frac{1}{2}-1} \cdot \frac{d}{dx} (3x+2) + \left(-\frac{1}{2}\right) (2x^2+4)^{-\frac{1}{2}-1} \cdot \frac{d}{dx} (2x^2+4)$$

$$= \frac{1}{2} (3x+2)^{-\frac{1}{2}} \cdot (3) - \left(\frac{1}{2}\right) (2x^2+4)^{-\frac{3}{2}} \cdot 4x$$

$$= \frac{3}{2\sqrt{3}x+2} - \frac{2x}{\left(2x^2+4\right)^{\frac{3}{2}}}$$

This is defined for all real numbers 2 3 *x* > − *.*

$$\text{(ii)}\quad \text{Let } y = \log\_7(\log x) = \frac{\log \left(\log x\right)}{\log 7} \text{ (by change of base formula)}.$$

The function is defined for all real numbers *x* > 1. Therefore

$$\frac{d\psi}{d\mathbf{x}} = \frac{1}{\log 7} \frac{d}{d\mathbf{x}} (\log \left(\log \mathbf{x}\right))$$

$$= \frac{1}{\log 7} \frac{1}{\log \mathbf{x}} \cdot \frac{d}{d\mathbf{x}} (\log \mathbf{x})$$

$$= \frac{1}{\mathbf{x} \log 7 \log \mathbf{x}}$$

**Example 40** Differentiate the following w.r.t. *x*.

$$\text{(i)}\quad\cos^{-1}\left(\sin x\right)\qquad\text{(ii)}\quad\tan^{-1}\left(\frac{\sin x}{1+\cos x}\right)\qquad\text{(iii)}\quad\sin^{-1}\left(\frac{\sqrt{2^{x+1}}}{1+4^x}\right)$$

#### **Solution**

(i) Let *f* (*x*) = cos –1 (sin *x*). Observe that this function is defined for all real numbers. We may rewrite this function as

$$\begin{aligned} f(\mathbf{x}) &= \cos^{-1}\left(\sin\mathbf{x}\right) \\ &= \cos^{-1}\left[\cos\left(\frac{\pi}{2} - x\right)\right] \\ &= \frac{\pi}{2} - \mathbf{x} \end{aligned}$$

Thus *f* ′(*x*) = – 1.

(ii) Let *f*(*x*) = tan –1 sin 1 cos *x x* <sup>+</sup> . Observe that this function is defined for all real

numbers, where cos *x* ≠ – 1; i.e., at all odd multiplies of π. We may rewrite this function as

$$\begin{aligned} f(\mathbf{x}) &= \tan^{-1} \left( \frac{\sin \mathbf{x}}{1 + \cos \mathbf{x}} \right) \\ &= \tan^{-1} \left[ \frac{2 \sin \left( \frac{\mathbf{x}}{2} \right) \cos \left( \frac{\mathbf{x}}{2} \right)}{2 \cos^2 \frac{\mathbf{x}}{2}} \right] \end{aligned}$$

$$=\frac{\cdot}{\cdot \cdot \cdot} \tan^{-1} \left[ \tan \left( \frac{\chi}{2} \right) \right] = \frac{\chi}{2}$$

Observe that we could cancel cos 2 *x* in both numerator and denominator as it is not equal to zero. Thus *f* ′(*x*) = 1 . 2

(iii) Let *f*(*x*) = sin –1 1 2 1 4 *x x* + <sup>+</sup> . To find the domain of this function we need to find all

*x* such that 1 2 1 1 1 4 *x x* + − ≤ ≤ + . Since the quantity in the middle is always positive,

we need to find all *x* such that 1 2 1 1 4 *x x* + ≤ + , i.e., all *x* such that 2*<sup>x</sup>* + 1 ≤ 1 + 4*<sup>x</sup>* . We

may rewrite this as 2 ≤ 1 2 *x* + 2*<sup>x</sup>* which is true for all *x*. Hence the function is defined at every real number. By putting 2*<sup>x</sup>* = tan θ, this function may be rewritten as

$$f(\mathbf{x}) = \sin^{-1}\left[\frac{2^{x+1}}{1+4^x}\right]$$

$$= \sin^{-1}\left[\frac{2^x \cdot 2}{1+\left(2^x\right)^2}\right]$$

$$= \sin^{-1}\left[\frac{2\tan\theta}{1+\tan^2\theta}\right]$$

$$= \sin^{-1}\left[\sin 2\theta\right]$$

$$= 2\theta = 2\tan^{-1}\left(2^x\right)$$

$$f'(\mathbf{x}) = 2\cdot\frac{1}{1+\left(2^x\right)^2}\cdot\frac{d}{dx}\left(2^x\right)$$

$$= \frac{2}{1+4^x}\cdot(2^x)\log 2$$

$$= \frac{2^{x+1}\log 2}{1+4^x}$$

(sin )

*x*

*d*

sin *x* cos *x*

*x dx* ⋅

**Example 41** Find *f* ′(*x*) if *f*(*x*) = (sin *x*) sin *x* for all 0 < *x* < π.

**Solution** The function *y* = (sin *x*) sin *x* is defined for all positive real numbers. Taking logarithms, we have

$$
\log y = \log \left(\sin \pi\right)^{\sin x} = \sin \pi \log \left(\sin \pi\right),
$$

Then

$$\frac{1}{y}\frac{d\psi}{d\mathbf{x}} = \frac{d}{d\mathbf{x}}\left(\sin\mathbf{x}\log(\sin\mathbf{x})\right)$$

$$\frac{1}{\sin\mathbf{x}\cos\mathbf{y}\cos\mathbf{x}} = \frac{1}{1}$$

= cos *x* log (sin *x*) + sin *x* .

$$\begin{aligned} & \quad \sin x & \quad \sin x\\ &= \cos x \log \left( \sin x \right) + \cos x\\ &= \left( 1 + \log \left( \sin x \right) \right) \cos x \end{aligned}$$

Thus

*dx*<sup>=</sup> *<sup>y</sup>*((1 + log (sin *x*)) cos *x*) = (1 + log (sin *x*)) ( sin *x*) **Example 42** For a positive constant *a* find *dy* , where

$$\mathbf{x} = \mathbf{a}^{t + \frac{1}{t}}, \quad \text{and } \mathbf{x} = \left(t + \frac{1}{t}\right)^{a^{t}}$$

$$\mathbf{y} = \mathbf{a}^{t + \frac{1}{t}}, \quad \text{and } \mathbf{x} = \left(t + \frac{1}{t}\right)^{a^{t}}$$

**Solution** Observe that both *y* and *x* are defined for all real *t* ≠ 0. Clearly

$$\frac{d\mathbf{y}}{dt} = \frac{d}{dt} \left( a^{t+\frac{1}{t}} \right) = a^{t+\frac{1}{t}} \frac{d}{dt} \left( t + \frac{1}{t} \right) \cdot \log a$$

$$= a^{\frac{t+1}{t}} \left( 1 - \frac{1}{t^2} \right) \log a$$
Similarly 
$$\frac{d\mathbf{x}}{dt} = a \left[ t + \frac{1}{t} \right]^{a-1} \cdot \frac{d}{dt} \left( t + \frac{1}{t} \right)$$

$$= a \left[ t + \frac{1}{t} \right]^{a-1} \cdot \left( 1 - \frac{1}{t^2} \right)$$

*dx dt* <sup>≠</sup> 0 only if *<sup>t</sup>* <sup>≠</sup> ± 1. Thus for *<sup>t</sup>* <sup>≠</sup> ± 1,

*dy*

$$\frac{d\mathbf{y}}{dx} = \frac{\frac{d\mathbf{y}}{dt}}{\frac{d\mathbf{x}}{dt}} = \frac{a^{\frac{t+1}{t}} \left(1 - \frac{1}{t^2}\right) \log a}{a \left[t + \frac{1}{t}\right]^{a-1} \cdot \left(1 - \frac{1}{t^2}\right)}$$

$$= \frac{a^{\frac{t+1}{t}} \log a}{a \left(t + \frac{1}{t}\right)^{a-1}}$$

**Example 43** Differentiate sin<sup>2</sup> *x* w.r.t. *e* cos *x* .

**Solution** Let *u* (*x*) = sin<sup>2</sup> *x* and *v* (*x*) = *e* cos *x* . We want to find / / *du du dx dv dv dx* = . Clearly

$$\frac{du}{d\mathbf{x}} = 2\sin x \cos x \text{ and } \frac{dv}{d\mathbf{x}} = e^{\cos x} \left(-\sin x\right) = -\left(\sin x\right)e^{\frac{\phi}{\cos x}}$$

$$\text{Thus } \qquad \frac{du}{d\mathbf{v}} = \frac{2\sin x \cos x}{-\sin x \ e^{\cos x}} = -\frac{2\cos x}{e^{\cos x}}$$

*Miscellaneous Exercise on Chapter 5*

π

Differentiate w.r.t. *x* the function in Exercises 1 to 11.

$$\begin{array}{cccc} 1. & (3x^2 - 9x + 5)^\bullet \left( \underset{\text{---}\,\text{2}}{\bigfrown} \right) & \underset{\text{---}\,\text{3}}{\bigfrown} \quad \text{2. } \sin^3 x + \cos^6 x\\ 3. & (5x)^{3\cos 2x} & \text{3. } \sin^{-1}(x\sqrt{\pi}), \text{ 0 } \leq x \leq 1. \end{array}$$

$$\begin{aligned} \text{5.} \quad & \frac{\cos^{-1} \frac{\pi}{2}}{\sqrt{2\pi + 7}}, -2 < \infty < 2\\ \text{6.} \quad & \cot^{-1} \left[ \frac{\sqrt{1 + \sin x} + \sqrt{1 - \sin x}}{\sqrt{1 + \sin x} - \sqrt{1 - \sin x}} \right], 0 < \infty < \frac{\pi}{2} \end{aligned}$$

$$7. \quad (\log x)^{\log x}, x \ge 1$$

**8.** cos (*a* cos *x* + *b* sin *x*), for some constant *a* and *b*.

$$9. \quad (\sin x - \cos x)^{\left(\sin x - \cos x\right)}, \quad \frac{\pi}{4} < x < \frac{3\pi}{4}$$

**10.** *x x* + *x a* + *a x* + *a a* , for some fixed *a* > 0 and *x* > 0

$$\begin{array}{ll} \text{11.} & \text{x}^{\text{x}^{2}-3}+\text{(}\text{x}-\text{3}\text{)}^{\text{x}^{2}}, \text{ for } \text{x} > \text{3} \\\\ \text{12.} & \text{Find } \frac{d\text{y}}{d\text{x}}, \text{ if } \text{y} = 12 \text{ (}1-\cos t), \text{x} = 10 \text{ (}t-\sin t), \text{ } -\frac{\pi}{2} < t < \frac{\pi}{2} \\ & \cdot \text{ } \cdot \text{ }\_{d\text{y}} & \cdot \end{array}$$

$$\text{13. Find } \frac{d\mathbf{y}}{d\mathbf{x}} \text{, if } \mathbf{y} = \sin^{-1}\mathbf{x} + \sin^{-1}\sqrt{1-\mathbf{x}^2}, \text{ } 0 < \mathbf{x} < 1.$$

**14.** If *x y y x* 1 1 0 + + + = , for , – 1 < *x* < 1, prove that

$$\frac{d\mathbf{y}}{d\mathbf{x}} = -\frac{1}{\left(1+\mathbf{x}\right)^2}$$

**15.** If (*x* – *a*) 2 + (*y* – *b*) 2 = *c* 2 , for some *c* > 0, prove that

$$\frac{\left[1+\left(\frac{d\mathcal{Y}}{dx}\right)^2\right]^{\frac{3}{2}}}{\frac{d^2\mathcal{Y}}{dx^2}}$$

is a constant independent of *a* and *b*.

- **16.** If cos *y* = *x* cos (*a* + *y*), with cos *a* ≠ ± 1, prove that 2 cos ( ) sin *dy a y dx a* + = .
- **17.** If *x* = *a* (cos *t* + *t* sin *t*) and *y* = *a* (sin *t t* cos *t*), find 2 2 *d y dx* .
- **18.** If *f*(*x*) = | *x* | 3 , show that *f* ″(*x*) exists for all real *x* and find it.
- **19.** Using the fact that sin (A + B) = sin A cos B + cos A sin B and the differentiation, obtain the sum formula for cosines.
- **20.** Does there exist a function which is continuous everywhere but not differentiable at exactly two points? Justify your answer.

$$\text{21.} \quad \text{If } \mathbf{y} = \begin{vmatrix} f(\mathbf{x}) & \mathbf{g}(\mathbf{x}) & h(\mathbf{x}) \\ l & m & n \\ a & b & c \end{vmatrix}, \text{ prove that } \frac{d\mathbf{y}}{d\mathbf{x}} = \begin{vmatrix} f'(\mathbf{x}) & \mathbf{g}'(\mathbf{x}) & h'(\mathbf{x}) \\ l & m & n \\ a & b & c \end{vmatrix}$$

$$\text{22.}\quad \text{If } \mathbf{y} = \stackrel{\cdot}{e} e^{a \cos^{-1} \mathbf{x}}, -1 \le \mathbf{x} \le \mathbf{l}, \text{ show that } \left(\mathbf{l} - \mathbf{x}^2\right) \frac{d^2 \mathbf{y}}{d \mathbf{x}^2} - \mathbf{x} \frac{d \mathbf{y}}{d \mathbf{x}} - a^2 \mathbf{y} = \mathbf{0} \cdot \mathbf{x}$$

# *Summary*

- Æ A real valued function is *continuous* at a point in its domain if the limit of the function at that point equals the value of the function at that point. A function is continuous if it is continuous on the whole of its domain.
- Æ Sum, difference, product and quotient of continuous functions are continuous. i.e., if *f* and *g* are continuous functions, then

$$(f \pm g)\left(\chi\right) \equiv f(\chi) \pm g\left(\chi\right) \text{ is continuous.}$$

$$(f \cdot g)$$
 (x) = f(x) \, . \, g(x) \text{ is continuous.}

$$\left(\frac{f}{\mathbf{g}}\right)(\mathbf{x}) = \frac{f(\mathbf{x})}{\mathbf{g}(\mathbf{x})} \text{ (wherever } \mathbf{g}(\mathbf{x}) \neq \mathbf{0}) \text{ is continuous.)}$$

- Æ Every differentiable function is continuous, but the converse is not true.
- Æ Chain rule is rule to differentiate composites of functions. If *f* = *v* o *u*, *t* = *u* (*x*)

$$\text{and if both } \frac{dt}{d\mathfrak{x}} \text{ and } \frac{d\nu}{dt} \text{ exist then}$$

$$\frac{df}{d\mathbf{x}} = \frac{d\nu}{dt} \cdot \frac{dt}{d\mathbf{x}}$$

Æ Following are some of the standard derivatives (in appropriate domains):

$$\begin{aligned} \frac{d}{dx}(\sin^{-1}x) &= \frac{1}{\sqrt{1-x^2}} & \frac{d}{dx}(\cos^{-1}x) &= -\frac{1}{\sqrt{1-x^2}}\\ \frac{d}{dx}(\tan^{-1}x) &= \frac{1}{1+x^2} &\\ \frac{d}{dx}(e^x) &= e^x & \frac{d}{dx}(\log x) &= \frac{1}{x} \end{aligned}$$

Æ Logarithmic differentiation is a powerful technique to differentiate functions of the form *f*(*x*) = [*u* (*x*)]*<sup>v</sup>* (*x*) . Here both *f*(*x*) and *u*(*x*) need to be positive for this technique to make sense.

![](_page_42_Figure_14.jpeg)