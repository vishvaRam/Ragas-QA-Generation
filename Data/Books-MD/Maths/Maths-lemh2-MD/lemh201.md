![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

![](_page_0_Picture_2.jpeg)

v *Just as a mountaineer climbs a mountain – because it is there, so a good mathematics student studies new material because it is there. — JAMES B. BRISTOL* v

### **7.1 Introduction**

Differential Calculus is centred on the concept of the derivative. The original motivation for the derivative was the problem of defining tangent lines to the graphs of functions and calculating the slope of such lines. Integral Calculus is motivated by the problem of defining and calculating the area of the region bounded by the graph of the functions.

If a function *f* is differentiable in an interval I, i.e., its derivative *f* ′exists at each point of I, then a natural question arises that given *f* ′at each point of I, can we determine the function? The functions that could possibly have given function as a derivative are called anti derivatives (or primitive) of the function. Further, the formula that gives

![](_page_0_Picture_7.jpeg)

**G .W. Leibnitz (1646 -1716)**

all these anti derivatives is called the *indefinite integral* of the function and such process of finding anti derivatives is called integration. Such type of problems arise in many practical situations. For instance, if we know the instantaneous velocity of an object at any instant, then there arises a natural question, i.e., can we determine the position of the object at any instant? There are several such practical and theoretical situations where the process of integration is involved. The development of integral calculus arises out of the efforts of solving the problems of the following types:

- (a) the problem of finding a function whenever its derivative is given,
- (b) the problem of finding the area bounded by the graph of a function under certain conditions.

These two problems lead to the two forms of the integrals, e.g., indefinite and definite integrals, which together constitute the *Integral Calculus*.

#### 226 MATHEMATICS

There is a connection, known as the *Fundamental Theorem of Calculus*, between indefinite integral and definite integral which makes the definite integral as a practical tool for science and engineering. The definite integral is also used to solve many interesting problems from various disciplines like economics, finance and probability.

In this Chapter, we shall confine ourselves to the study of indefinite and definite integrals and their elementary properties including some techniques of integration.

### **7.2 Integration as an Inverse Process of Differentiation**

Integration is the inverse process of differentiation. Instead of differentiating a function, we are given the derivative of a function and asked to find its primitive, i.e., the original function. Such a process is called *integration* or *anti differentiation*. Let us consider the following examples:

$$\begin{array}{ccccc} \text{We know that} & \frac{d}{dx}(\sin x) = \cos x & & & \\ & \cdot & \cdot & \cdot & \cdot \\ & & \frac{d}{dx}(\frac{x^3}{3}) = x^2 & \cdot & \cdot & \cdot \\ & & \frac{d}{dx}(\frac{x^3}{3}) = x^2 & \cdot & \cdot & \cdot \\ \end{array} \tag{1}$$

and ( ) *<sup>d</sup> <sup>x</sup> e dx* = *e* ... (3) We observe that in (1), the function cos *x* is the derived function of sin *x*. We say that sin *x* is an anti derivative (or an integral) of cos *x*. Similarly, in (2) and (3), 3 3 *x* and *<sup>x</sup>* are the anti derivatives (or integrals) of *x* 2 and *e x* , respectively. Again, we note that

*e* for any real number C, treated as constant function, its derivative is zero and hence, we can write (1), (2) and (3) as follows :

*x*

$$\frac{d}{d\boldsymbol{\chi}}\left(\sin\left(\boldsymbol{\chi}+\mathbf{C}\right)\right) = \cos\left(\boldsymbol{\chi}\right),\\\frac{d}{d\boldsymbol{\chi}}\left(\frac{\boldsymbol{\chi}^3}{3}+\mathbf{C}\right) = \boldsymbol{\chi}^2 \text{ and } \frac{d}{d\boldsymbol{\chi}}\left(e^{\boldsymbol{\chi}}+\mathbf{C}\right) = e^{\boldsymbol{\chi}^3}$$

Thus, anti derivatives (or integrals) of the above cited functions are not unique. Actually, there exist infinitely many anti derivatives of each of these functions which can be obtained by choosing C arbitrarily from the set of real numbers. For this reason C is customarily referred to as *arbitrary constant*. In fact, C is the *parameter* by varying which one gets different anti derivatives (or integrals) of the given function.

More generally, if there is a function F such that F ( ) = ( ) *<sup>d</sup> x f x dx* , <sup>∀</sup> *<sup>x</sup>*∈ I (interval), then for any arbitrary real number C, (also called *constant of integration*)

$$\frac{d}{d\boldsymbol{\chi}} \left[ \mathbf{F}(\boldsymbol{\chi}) + \mathbf{C} \right] = f(\boldsymbol{\chi}), \; \boldsymbol{x} \in \mathcal{I}$$

Thus, {F + C, C ∈ **R**} denotes a family of anti derivatives of *f*.

*Remark* Functions with same derivatives differ by a constant. To show this, let *g* and *h* be two functions having the same derivatives on an interval I.

Consider the function *f* = *g* – *h* defined by *f*(*x*) = *g*(*x*) – *h*(*x*), ∀ *x* ∈ I

Then

$$\frac{df}{d\boldsymbol{\chi}} = f' = \boldsymbol{g}' - h' \text{giving } f'(\boldsymbol{\chi}) = \boldsymbol{g}'(\boldsymbol{\chi}) - h'(\boldsymbol{\chi}) \, ^\cdot \boldsymbol{\upchi} \, \boldsymbol{x} \in \Gamma$$

or *f*′ (*x*) = 0, ∀ *x* ∈ I by hypothesis,

i.e., the rate of change of *f* with respect to *x* is zero on I and hence *f* is constant.

In view of the above remark, it is justified to infer that the family {F + C, C ∈ **R**} provides all possible anti derivatives of *f*.

We introduce a new symbol, namely, *f x dx* ( ) ∫ which will represent the entire class of anti derivatives read as the indefinite integral of *f* with respect to *x*.

$$\text{Symbolically, we write } \int f(\mathbf{x}) \, d\mathbf{x} = \mathbf{F}(\mathbf{x}) + \mathbf{C}.$$

$$\text{Notation Given that } \frac{dy}{d\chi} = f'(\chi) \text{, we write}\\
\psi = \bigcap\_{\chi \subset \chi} f'(\chi) \, d\chi.$$

For the sake of convenience, we mention below the following symbols/terms/phrases with their meanings as given in the Table (7.1).

| Symbols/Terms/Phrases                  | Meaning                                               |
|----------------------------------------|-------------------------------------------------------|
| ∫<br>f<br>(<br>x<br>)<br>dx            | Integral of f with respect to x                       |
| ∫<br>f<br>x<br>dx<br>f(x) in<br>(<br>) | Integrand                                             |
| ∫<br>f<br>(<br>x<br>)<br>dx<br>x in    | Variable of integration                               |
| Integrate                              | Find the integral                                     |
| An integral of f                       | A function F such that                                |
|                                        | F′(x) = f (x)                                         |
| Integration                            | The process of finding the integral                   |
| Constant of Integration                | Any real number C, considered as<br>constant function |

We already know the formulae for the derivatives of many important functions. From these formulae, we can write down immediately the corresponding formulae (referred to as standard formulae) for the integrals of these functions, as listed below which will be used to find integrals of other functions.

**Derivatives Integrals (Anti derivatives)**

(i) 1 1 *n d x <sup>n</sup> x dx n* + <sup>=</sup> <sup>+</sup> ; 1 C 1 *n <sup>n</sup> x x dx n* + = + + ∫ , *n* ≠ –1 Particularly, we note that ( ) 1 *d x dx* <sup>=</sup> ; *dx x* = + <sup>C</sup> ∫ (ii) ( ) sin cos *<sup>d</sup> x x dx* <sup>=</sup> ; cos sin C *x dx x* = + ∫ (iii) ( ) – cos sin *<sup>d</sup> x x dx* <sup>=</sup> ; sin cos C *x dx – x* = + ∫ (iv) ( ) <sup>2</sup> tan sec *d x x dx* = ; 2 sec tan C *x dx x* = + ∫ (v) ( ) <sup>2</sup> – cot cosec *d x x dx* = ; 2 cosec cot C *x dx – x* = + ∫ (vi) ( ) sec sec tan *d x x x dx* <sup>=</sup> ; sec tan sec C *x x dx x* = + ∫ (vii) ( ) – cosec cosec cot *d x x x dx* <sup>=</sup> ; cosec cot – cosec C *x x dx x* = + ∫ (viii) ( ) – 1 2 1 sin 1 *d x dx – x* = ; – 1 2 sin C 1 *dx x – x* = + ∫ (ix) ( ) – 1 2 1 – cos 1 *d x dx – x* = ; – 1 2 cos C 1 *dx – x – x* = + ∫ (x) ( ) – 1 2 1 tan 1 *d x dx x* = + ; – 1 2 tan C 1 *dx x x* = + + ∫ (xi) ( ) *<sup>d</sup> x x e e dx* = ; C *x x e dx e* = + ∫

$$\begin{aligned} \text{(iii)} \quad &\frac{d}{d\mathbf{x}} (\log \|\mathbf{x}\|) = \frac{1}{\alpha}, \text{s.t.} \quad &\int \frac{1}{\alpha} \, d\mathbf{x} = \log \|\mathbf{x}\| + \mathbf{C}, \\\ \text{(iii)} \quad &\frac{d}{d\mathbf{x}} \left(\frac{a^x}{\log a}\right) = a^x \; ; \quad &\int a^x \, d\mathbf{x} = \frac{a^x}{\log a} + \mathbf{C} \end{aligned}$$

A**Note** In practice, we normally do not mention the interval over which the various functions are defined. However, in any specific problem one has to keep it in mind.

### **7.2.1** *Some properties of indefinite integral*

In this sub section, we shall derive some properties of indefinite integrals.

(I) The process of differentiation and integration are inverses of each other in the sense of the following results :

$$\frac{d}{d\boldsymbol{\chi}}\Big[\boldsymbol{f}(\boldsymbol{\chi})\,d\boldsymbol{\chi} = \boldsymbol{f}(\boldsymbol{\chi})\Big]$$

and *f x dx* ′( ) ∫ = *f*(*x*) + C, where C is any arbitrary constant.

**Proof** Let F be any anti derivative of *f*, i.e.,

*dx* ∫

$$\frac{d}{d\boldsymbol{\chi}}\operatorname{F}(\boldsymbol{\chi}) = \operatorname{f}(\boldsymbol{\chi}) \underset{\boldsymbol{\chi}}{\operatorname{d}} \boldsymbol{\chi}$$

$$\begin{aligned} \text{Then} \\ \text{Therefore} \qquad \frac{d}{dx} \begin{Bmatrix} f(\mathbf{x}) \ dx\_1 = F(\mathbf{x}) + \mathbf{C} \\ \cdot \\ \frac{d}{dx} \begin{Bmatrix} f(\mathbf{x}) \ dx\_2 = \frac{d}{dx} \end{Bmatrix} \mathbf{F}(\mathbf{x}) + \mathbf{C} \end{Bmatrix} \end{aligned}$$

*dx*

*f x dx*

Therefore ( ) *<sup>d</sup>*

$$=\frac{d}{d\boldsymbol{\chi}}\,\mathrm{F}(\boldsymbol{\chi}) = f\,(\boldsymbol{\chi})$$

*x*

Similarly, we note that

$$f'(\mathbf{x}) = \frac{d}{d\mathbf{x}} f(\mathbf{x})$$

and hence *f x dx* ′( ) ∫

where C is arbitrary constant called constant of integration.

(II) Two indefinite integrals with the same derivative lead to the same family of curves and so they are equivalent.

= *f* (*x*) + C

**Proof** Let *f* and *g* be two functions such that

$$\frac{d}{d\boldsymbol{\alpha}}\int f(\boldsymbol{\alpha}) \, d\boldsymbol{\alpha} = \frac{d}{d\boldsymbol{\alpha}}\int \operatorname{g}\left(\boldsymbol{\alpha}\right) \, d\boldsymbol{\alpha}$$
 
$$\text{or} \qquad \frac{d}{d\boldsymbol{\alpha}}\Big[\int f(\boldsymbol{\alpha}) \, d\boldsymbol{\alpha} - \int \operatorname{g}\left(\boldsymbol{\alpha}\right) \, d\boldsymbol{\alpha}\Big] = 0$$

Hence *f x dx – g x dx* ( ) ( ) ∫ ∫ <sup>=</sup> C, where C is any real number (Why?) or *f x dx* ( ) ∫ <sup>=</sup>*g x dx* ( ) C<sup>+</sup> ∫

So the families of curves {∫ *f x dx* ( ) C , C R + ∈ 1 1 }

$$\text{and}\\
\qquad \left\{ \int \mathbf{g}\left(\mathbf{x}\right) \, d\mathbf{x} + \mathbf{C}\_2, \mathbf{C}\_2 \in \mathbb{R} \right\} \text{ are identical.}$$

Hence, in this sense, *f x dx g x dx* ( ) and ( ) ∫ ∫ are equivalent.

A **Note** The equivalence of the families {∫ *f x dx* ( ) + C ,C1 1 ∈**R**} and {∫ *g x dx* ( ) + C ,C2 2 <sup>∈</sup>**R**} is customarily expressed by writing *f x dx g x dx* ( ) = ( ) ∫ ∫ , without mentioning the parameter.

(III) [ *f x g x dx f x dx g x dx* ( ) + ( ) ( ) + ( ) ] <sup>=</sup> ∫ ∫ ∫

**Proof** By Property (I), we have

$$\frac{d}{dx}\left[\int \left[f\left(\mathbf{x}\right) + \mathbf{g}\left(\mathbf{x}\right)\right]d\mathbf{x}\right] = f(\mathbf{x}) + \mathbf{g}\left(\mathbf{x}\right) \tag{1}$$

On the otherhand, we find that

$$\frac{d}{d\mathbf{x}}\left[\int f(\mathbf{x}) \, d\mathbf{x} + \int \mathbf{g}(\mathbf{x}) \, d\mathbf{x}\right] = \frac{d}{d\mathbf{x}}\int f(\mathbf{x}) \, d\mathbf{x} + \frac{d}{d\mathbf{x}}\int \mathbf{g}(\mathbf{x}) \, d\mathbf{x}$$

$$= f(\mathbf{x}) + \mathbf{g}(\mathbf{x}) \, d\mathbf{x} \qquad\qquad\qquad\qquad\qquad\qquad\qquad\dots \quad(2)$$

Thus, in view of Property (II), it follows by (1) and (2) that

$$\int \left(f(\mathbf{x}) + \mathbf{g}(\mathbf{x})\right)d\mathbf{x} = \int f(\mathbf{x}) \, d\mathbf{x} + \int \mathbf{g}(\mathbf{x}) \, d\mathbf{x} \, \dots$$

(IV) For any real number *k*, *k f x dx k f x dx* ( ) ( ) <sup>=</sup> ∫ ∫

$$\text{Proof }\text{By the Property (I), }\frac{d}{d\mathbf{x}}\Big[k\,\,f(\mathbf{x})\,\,d\mathbf{x} = k\,\,f(\mathbf{x})\,.$$

$$\text{Also}\qquad \frac{d}{d\boldsymbol{\chi}} \left[ \boldsymbol{k} \int f(\boldsymbol{\chi}) \, d\boldsymbol{\chi} \right] = \boldsymbol{k} \frac{d}{d\boldsymbol{\chi}} \int f(\boldsymbol{\chi}) \, d\boldsymbol{\chi} = \boldsymbol{k} \, f(\boldsymbol{\chi})$$

Therefore, using the Property (II), we have *k f x dx k f x dx* ( ) ( ) <sup>=</sup> ∫ ∫ .

(V) Properties (III) and (IV) can be generalised to a finite number of functions *f* 1 , *f* 2 , ..., *f n* and the real numbers, *k*<sup>1</sup> , *k*<sup>2</sup> , ..., *k<sup>n</sup>* giving

$$\begin{aligned} &\int \left[k\_1 f\_1(\mathbf{x}) + k\_2 f\_2^\*\left(\mathbf{x}\right) + ... + k\_n f\_n^\*\left(\mathbf{x}\right)\right] d\mathbf{x} \\ &= \, ^\cdot k\_1 \int f\_1(\mathbf{x}) \, d\mathbf{x} + k\_2 \int f\_2^\*\left(\mathbf{x}\right) \, d\mathbf{x} + ... + k\_n \int f\_n^\*\left(\mathbf{x}\right) \, d\mathbf{x} \, ... \end{aligned}$$

To find an anti derivative of a given function, we search intuitively for a function whose derivative is the given function. The search for the requisite function for finding an anti derivative is known as integration by the method of inspection. We illustrate it through some examples.

**Example 1** Write an anti derivative for each of the following functions using the method of inspection:

(i) cos 2*x* (ii) 3*x* 2 + 4*x* 3 (iii) 1 *x* , *x* ≠ 0

### **Solution**

(i) We look for a function whose derivative is cos 2*x*. Recall that

$$\frac{d}{dx}\sin 2x = 2\cos 2x$$

$$\text{or }\qquad \cos 2x = \frac{1}{2}\frac{d}{dx}\text{ (sin }2x) = \frac{d}{dx}\left(\frac{1}{2}\sin 2x\right)$$

Therefore, an anti derivative of cos 2*x* is 1 sin 2 2 *x* .

(ii) We look for a function whose derivative is 3*x* 2 + 4*x* 3 . Note that

$$\frac{d}{d\boldsymbol{\chi}} \left( \boldsymbol{\chi^3} + \boldsymbol{\chi^4} \right) = 3\boldsymbol{\chi^2} + 4\boldsymbol{\chi^3}.$$

Therefore, an anti derivative of 3*x* 2 + 4*x* <sup>3</sup>is *x*<sup>3</sup> + *x* 4 .

#### 232 MATHEMATICS

(iii) We know that

$$\frac{d}{d\mathbf{x}}\left(\log\,\mathbf{x}\right) = \frac{1}{\mathbf{x}}\text{, }\mathbf{x} > 0\text{ and }\frac{d}{d\mathbf{x}}\left[\log\left(-\mathbf{x}\right)\right] = \frac{1}{-\mathbf{x}}\left(-\mathbf{l}\right) = \frac{1}{\mathbf{x}}\text{, }\mathbf{x} < 0\text{, }$$

Combining above, we get ( ) <sup>1</sup> log 0 *<sup>d</sup> x , x dx x* = ≠

Therefore, 1 *dx x* log *x* <sup>=</sup> ∫ is one of the anti derivatives of 1 *x* .

**Example 2** Find the following integrals:

(i) 3 2 *x –* 1 *dx x* ∫ (ii) 2 3 ( 1) *x dx* <sup>+</sup> ∫ (iii) ∫ 3 2 1 ( 2 – ) + *x x e dx x*

**Solution**

(i) We have

$$\begin{aligned} \int \frac{\mathbf{x}^3 - 1}{\mathbf{x}^2} \, d\mathbf{x} &= \int \mathbf{x} \, d\mathbf{x} - \int \mathbf{x}^{-2} \, d\mathbf{x} \\ &= \left(\frac{\mathbf{x}^{1+1}}{1+1} + \mathbf{C}\_1\right) - \left(\frac{\mathbf{x}^{-2+1}}{2+1} + \mathbf{C}\_2\right) + \mathbf{C}\_1, \mathbf{C}\_2 \text{ are constants of integration} \\ &= \frac{\mathbf{x}^2}{2} + \mathbf{C}\_1 - \frac{\mathbf{x}^{-1}}{-1} - \mathbf{C}\_2 = \frac{\mathbf{x}^2}{2} + \frac{1}{\mathbf{x}} + \mathbf{C}\_1 - \mathbf{C}\_2 \\ &= \frac{\mathbf{x}^2}{2} + \frac{1}{\mathbf{x}} + \mathbf{C}\_3, \text{where } \mathbf{C} = \mathbf{C}\_1 - \mathbf{C}\_2 \text{ is another constant of integration.} \end{aligned}$$

A**Note** From now onwards, we shall write only one constant of integration in the final answer.

(ii) We have

$$\begin{aligned} \int \left(\mathbf{x}^{\frac{2}{3}} + \mathbf{l}\right) d\mathbf{x} &= \int \mathbf{x}^{\frac{2}{3}} \, d\mathbf{x} + \int d\mathbf{x} \\ &= \frac{\mathbf{x}^{\frac{2}{3} + 1}}{\mathbf{3}} + \mathbf{x} + \mathbf{C} = \frac{\mathbf{3}}{\mathbf{5}} \, \mathbf{x}^{\frac{\mathbf{5}}{3}} + \mathbf{x} + \mathbf{C} \end{aligned}$$

$$\begin{aligned} \text{(iii)} \quad \text{We have } \int \left(\mathbf{x}^{\frac{3}{2}} + 2 \ \mathbf{e}^{x} - \frac{1}{\chi}\right) d\mathbf{x} &= \int \mathbf{x}^{\frac{3}{2}} \, d\mathbf{x} + \int 2 \ \mathbf{e}^{x} \, d\mathbf{x} - \int \frac{1}{\chi} \, d\mathbf{x} \\ &= \frac{\frac{3}{2} + 1}{\frac{3}{2} + 1} + 2 \ \mathbf{e}^{x} - \log\left|\mathbf{x}\right| + \mathbf{C} \\ &= \frac{2}{5} \times \frac{\frac{5}{2}}{\frac{3}{2}} + 2 \ \mathbf{e}^{x} - \log\left|\mathbf{x}\right| + \mathbf{C} \end{aligned}$$

**Example 3** Find the following integrals:

$$\begin{aligned} \text{(i)} \quad & \int (\sin x + \cos x) \, dx \\ & \text{(ii)} \quad \int \frac{1 - \sin x}{\cos^2 x} \, dx \end{aligned} \quad \text{(iii)} \int \cos x \, dx \quad \text{(v)} \int \frac{1 - \sin x}{\cos^2 x} \, dx$$

### **Solution**

- (i) We have (sin cos ) sin cos *x x dx x dx x dx* + = + ∫ ∫ ∫ = – cos sin C *x x* + +
- (ii) We have 2 (cosec (cosec + cot ) cosec cosec cot *x x x dx x dx x x dx* <sup>=</sup> <sup>+</sup> ∫ ∫ ∫ = – cot cosec C *x – x* +
- (iii) We have

$$\int \frac{1-\sin x}{\cos^2 x} \, dx = \int \frac{1}{\cos^2 x} \, dx - \int \frac{\sin x}{\cos^2 x} \, dx$$

$$= \int \sec^2 x \, dx - \int \tan x \sec x \, dx$$

$$= \tan x - \sec x + C$$

**Example 4** Find the anti derivative F of *f* defined by *f* (*x*) = 4*x* 3 – 6, where F (0) = 3 **Solution** One anti derivative of *f* (*x*) is *x* 4 – 6*x* since

$$\frac{d}{d\mathbf{x}}\left(\mathbf{x}^4 - 6\mathbf{x}\right) = 4\mathbf{x}^3 - 6\mathbf{x}$$

Therefore, the anti derivative F is given by

$$\mathbf{F}(\mathbf{x}) = \mathbf{x}^4 - 6\mathbf{x} + \mathbf{C}, \text{ where } \mathbf{C} \text{ is constant.}$$

#### 234 MATHEMATICS

Given that F(0) = 3, which gives,

3 = 0 – 6 × 0 + C or C = 3

Hence, the required anti derivative is the unique function F defined by

$$F(x) = x^4 - 6x + 3.5$$

### *Remarks*

- (i) We see that if F is an anti derivative of *f*, then so is F + C, where C is any constant. Thus, if we know one anti derivative F of a function *f*, we can write down an infinite number of anti derivatives of *f* by adding any constant to F expressed by F(*x*) + C, C ∈ **R**. In applications, it is often necessary to satisfy an additional condition which then determines a specific value of C giving unique anti derivative of the given function.
- (ii) Sometimes, F is not expressible in terms of elementary functions viz., polynomial, logarithmic, exponential, trigonometric functions and their inverses etc. We are

therefore blocked for finding *f x dx* ( ) ∫ . For example, it is not possible to find

2 *– x e dx* ∫ by inspection since we can not find a function whose derivative is 2 *– x e*

(iii) When the variable of integration is denoted by a variable other than *x*, the integral formulae are modified accordingly. For instance

$$\int \mathbf{y}^4 \, d\mathbf{y} = \frac{\mathbf{y}^{4+1}}{4+1} + \mathbf{C} = \frac{1}{5} \left( \mathbf{y}^5 + \mathbf{C} \right)$$

**EXERCISE 7.1**

Find an anti derivative (or integral) of the following functions by the method of inspection.

2*x*

**1.** sin 2*x* **2.** cos 3*x* **3.** *e*

$$\begin{array}{ccccc} \textbf{4.} & (a\textbf{x} + b)^{2} & \raisebox{-.5.5.5}{\times} & \raisebox{-.5.5.5}{\times} & \sin 2\overrightarrow{x} - 4 & e^{3x} \end{array}$$

Find the following integrals in Exercises 6 to 20:

**6.** <sup>3</sup> (4 + 1) *<sup>x</sup> e dx* ∫ **7.** <sup>2</sup> 2 1 *x dx* (1 – ) *x* ∫ **8.** <sup>2</sup> ( ) *ax bx c dx* + + ∫ **9.** <sup>2</sup> (2 ) *<sup>x</sup> x e dx* <sup>+</sup> ∫ **10.** 2 1 *x – dx x* <sup>∫</sup> **11.** 3 2 2 *x x –* 5 4 *dx x* + ∫ **12.** 3 *x x*3 4 *dx x* + + ∫ **13.** 3 2 1 1 *x x x – dx x –* − + ∫ **14.** (1 ) *– x x dx* ∫

- **15.** <sup>2</sup> *x x x dx* ( 3 2 3) + + ∫ **16.** (2 3cos ) *<sup>x</sup> x – x e dx* <sup>+</sup> ∫ **17.** <sup>2</sup> (2 3sin 5 ) *x – x x dx* <sup>+</sup> ∫ **18.** sec (sec tan ) *x x x dx* <sup>+</sup> ∫
- **19.** 2 2 sec cosec *x dx x* ∫ **20.** <sup>2</sup> 2 – 3sin cos *x x* ∫ *dx*.

Choose the correct answer in Exercises 21 and 22.

$$\begin{aligned} \text{(21. The anti derivative of } \left(\sqrt{x} + \frac{1}{\sqrt{x}}\right) \text{ equals} \\ \text{(A)} \quad \frac{1}{3}x^{\frac{1}{3}} + 2x^{\frac{1}{2}} + \text{C} & \qquad \text{(B)} \quad \frac{2}{3}x^{\frac{2}{3}} + \frac{1}{2}x^{2} + \text{C} \\ \text{(C)} \quad \frac{2}{3}x^{\frac{3}{2}} + 2x^{\frac{1}{2}} + \text{C} & \qquad \text{(D)} \quad \frac{3}{2}x^{\frac{3}{2}} + \frac{1}{2}x^{\frac{1}{2}} + \text{C} \\ \text{22. If } \frac{d}{dx}f(x) = 4x^3 - \frac{3}{x^4} \text{ such that } f(2) = 0. \text{ Then } f(x) \text{ is} \\ \text{(A)} \quad x^4 + \frac{1}{x^3} - \frac{129}{9} \qquad \text{(B)} \quad x^3 + \frac{1}{x^4} + \frac{129}{9} \end{aligned}$$

$$\begin{array}{ccccccc} \text{(A)} & \cdots & \text{(A)} & \text{(B)} & \cdots & \text{(A^4)} & 8\\ \cdot & x^3 & 8 & & & &\\ \text{(C)} & x^4 + \frac{1}{x^3} + \frac{129}{8} & & & & \text{(D)} & x^3 + \frac{1}{x^4} - \frac{129}{8} \\ \end{array}$$

### **7.3 Methods of Integration**

In previous section, we discussed integrals of those functions which were readily obtainable from derivatives of some functions. It was based on inspection, i.e., on the search of a function F whose derivative is *f* which led us to the integral of *f*. However, this method, which depends on inspection, is not very suitable for many functions. Hence, we need to develop additional techniques or methods for finding the integrals by reducing them into standard forms. Prominent among them are methods based on:

- 1. Integration by Substitution
- 2. Integration using Partial Fractions
- 3. Integration by Parts

### **7.3.1** *Integration by substitution*

In this section, we consider the method of integration by substitution.

The given integral *f x dx* ( ) ∫ can be transformed into another form by changing the independent variable *x* to *t* by substituting *x* = *g* (*t*).

$$\begin{aligned} \text{Consider} & \qquad \mathbf{I} = \int f(\mathbf{x}) \, d\mathbf{x} \\ \text{Put } \mathbf{x} = \mathbf{g}(t) \text{ so that } \frac{d\mathbf{x}}{\mathbf{x}} = \mathbf{g}'(t). \end{aligned}$$

$$\begin{aligned} \text{Put } \boldsymbol{x} = \mathbf{g}(t) \text{ so that } \frac{\boldsymbol{\pi}}{\boldsymbol{d}t} = \mathbf{g}'(t). \\ \text{We write } & \quad d\boldsymbol{x} = \mathbf{g}'(t) \text{ } dt \\ \text{Thus } & \quad \mathbf{I} = \begin{bmatrix} f'(\boldsymbol{x}) \ \boldsymbol{d}\mathbf{x} = \int f(\boldsymbol{g}(t)) \ \mathbf{g}'(t) \ \mathbf{d}t \end{bmatrix}. \end{aligned}$$

This change of variable formula is one of the important tools available to us in the name of integration by substitution. It is often important to guess what will be the useful substitution. Usually, we make a substitution for a function whose derivative also occurs in the integrand as illustrated in the following examples.

**Example 5** Integrate the following functions w.r.t. *x*:

(i) sin *mx* (ii) 2*x* sin (*x* 2 + 1) (iii) 4 2 tan sec *x x x* (iv) 1 2 sin (tan ) 1 *– x* + *x*

### **Solution**

(i) We know that derivative of *mx* is *m*. Thus, we make the substitution *mx* = *t* so that *mdx* = *dt*.

$$\text{Therefore, } \quad \int \widehat{\sin m} \, d\mathbf{x} = \frac{1}{m} \int \sin t \, dt = -\frac{1}{m} \cos t + \mathbf{C} = -\frac{1}{m} \cos m\mathbf{x} + \mathbf{C}$$

(ii) Derivative of *x* 2 + 1 is 2*x*. Thus, we use the substitution *x* 2 + 1 = *t* so that 2*x dx* = *dt*.

$$\text{Therefore, } \int 2x \sin \left(\chi^2 + 1\right) \, d\chi = \int \sin t \, dt = -\cos t + C = -\cos \left(\chi^2 + 1\right) + C$$

(iii) Derivative of *x* is 1 2 1 1 2 2 *– x x* = . Thus, we use the substitution

$$
\sqrt{\infty} = \overset{\triangle}{r}\text{so that }\frac{1}{2\sqrt{\infty}}\,d\mathfrak{x} = dt\text{ giving }\,d\mathfrak{x} = 2t\,\,dt.
$$

Thus, 4 2 4 2 tan sec 2 tan sec *x x t t t dt dx x t* <sup>=</sup> ∫ ∫ = 4 2 2 tan sec *t t dt* ∫

Again, we make another substitution tan *t* = *u* so that sec<sup>2</sup> *t dt* = *du*

$$\begin{aligned} \text{Therefore,} \qquad &2\int \tan^4 t \sec^2 t \, dt = 2\int u^4 \, du = 2\frac{u^5}{5} + \text{C} \\ &= \frac{2}{5}\tan^5 t + \text{C} \ (\text{since } u = \tan t) \\ &= \frac{2}{5}\tan^5 \sqrt{\chi} + \text{C} \ (\text{since } t = \sqrt{\chi}) \\ \text{Hence,} \qquad &\int \frac{\tan^4 \sqrt{\chi} \sec^2 \sqrt{\chi}}{\sqrt{\chi}} \, d\chi = \frac{2}{5}\tan^5 \sqrt{\chi} + \text{C} \end{aligned}$$

**Alternatively**, make the substitution tan *x t* =

$$\text{(iv)}\quad\text{Derivative of }\tan^{-1}x = \frac{1}{1+x^2}\text{. Thus, we use the substitution}$$

$$\tan^{-1}\alpha = t \text{ so that } \frac{d\alpha}{1+\alpha^2} = dt.$$

$$\text{Therefore, } \int \frac{\sin \left(\tan^{-1} x\right)}{1 + x^2} dx = \left[ \sin t \, dt \right]\_{\text{---}}^{\text{---}} = -\cos t \, t + C = -\cos \left(\tan^{-1} x\right) + C$$

Now, we discuss some important integrals involving trigonometric functions and their standard integrals using substitution technique. These will be used later without reference.

**(i)** ∫ **tan = log sec + C** *x dx x*

We have

$$
\int \tan x \, dx = \int \frac{\sin x}{\cos x} \, dx
$$

Put cos *x* = *t* so that sin *x dx* = – *dt*

$$\begin{aligned} \text{Then } \underset{\begin{aligned} \text{Then } \underset{\begin{aligned} \text{C} \end{aligned}}{\text{C}} \end{aligned}}{\text{Then } \underset{\begin{aligned} \text{C} \end{aligned}}{\text{C}} \int \text{tan } x \, dx = -\int \frac{dt}{t} = -\log|t| + \text{C} = -\log|\cos x| + \text{C} \\ \text{or } \int \text{tan } x \, dx = \log|\sec x| + \text{C} \end{aligned}$$

**(ii)** ∫ **cot = log sin + C** *x dx x*

$$\text{We have } \int \cot x \, dx = \int \frac{\cos x}{\sin x} \, dx$$

#### 238 MATHEMATICS

Put sin *x* = *t* so that cos *x dx* = *dt* Then cot *dt x dx t* <sup>=</sup> ∫ ∫ = log C *<sup>t</sup>* <sup>+</sup> = log sin C *<sup>x</sup>* <sup>+</sup>

#### **(iii)** ∫ **sec = log sec + tan + C** *x dx x x*

We have

$$\int \sec x \, dx = \int \frac{\sec x \left(\sec x + \tan x\right)}{\sec x + \tan x} \, dx$$

Put sec *x* + tan *x* = *t* so that sec *x* (tan *x* + sec *x*) *dx* = *dt* Therefore, sec log + C = log sec tan C *dt x dx <sup>t</sup> x x t* = = + + ∫ ∫

**(iv)** ∫ **cosec = log cosec – cot + C** *x dx x x*

We have

$$\int \text{cossec} \ge d\mathbf{x} = \int \frac{\text{cossec} \ge (\text{cossec} \ge + \cot \hat{\mathbf{x}})}{(\text{cossec} \ge + \cot \hat{\mathbf{x}})} d\mathbf{x}$$

Put cosec *x* + cot *x* = *t* so that – cosec *x* (cosec *x* + cot *x*) *dx* = *dt*

$$\begin{aligned} \text{So} \qquad & \int \text{cosec } x \, dx = -\int \frac{dt}{t} = -\log|t| = -\log|\text{cosec } x + \cot x| + C\\ & = -\log\left|\frac{\text{cosec }^2 x - \cot^2 x}{\text{cosec } x - \cot x}\right| + C\\ & = \log|\text{cosec } x - \cot x| + C \end{aligned}$$

**Example 6** Find the following integrals:

$$\text{(i)} \quad \int \sin^3 x \cos^2 x \, dx \stackrel{\triangle}{\underset{\dots}{\longrightarrow}} \text{(ii)} \quad \int \frac{\sin x}{\sin \left(x + a\right)} \, dx \quad \text{(iii)} \int \frac{1}{1 + \tan x} \, dx$$

### **Solution**

(i) We have

$$\begin{aligned} \int \sin^3 x \cos^2 x \, dx &= \int \sin^2 x \cos^2 x \, (\sin x) \, dx \\ &= \int (1 - \cos^2 x) \cos^2 x \, (\sin x) \, dx \end{aligned}$$

Put *t* = cos *x* so that *dt* = – sin *x dx*

$$\begin{aligned} \text{Therefore, } \quad \int \sin^2 x \cos^2 x \left(\sin x\right) dx &= \frac{1}{3} \left(1 - t^2\right) t^2 \text{ } dt \\ &= -\int \left(t^2 - t^4\right) dt = -\left(\frac{t^3}{3} - \frac{t^5}{5}\right) + \text{C.} \\ &= -\frac{1}{3} \cos^3 x + \frac{1}{5} \cos^3 x + \text{C.} \end{aligned}$$

(ii) Put *x* + *a* = *t*. Then *dx* = *dt*. Therefore

$$\int \frac{\sin x}{\sin \left(\alpha + a\right)} \, dx = \int \frac{\sin \left(t - a\right)}{\sin t} \, dt$$

$$= \int \frac{\sin t \cos a - \cos t \sin a}{\sin t} \, dt$$

$$= \cos a \int dt - \sin a \int \cot t \, dt$$

$$= \left(\cos a\right)t - \left(\sin a\right) \left[\log \left| \sin t \right| + C\_1 \right]$$

$$= \left(\cos a\right)\left(\alpha + a\right) - \left(\sin a\right)\left[\log \left| \sin(\alpha + a) \right| + C\_1 \right]$$

$$= x \cos a + a \cos a - \left(\sin a\right) \log \left| \sin(\alpha + a) \right| - C\_1 \sin a$$

$$\int \sin x \, dx$$

Hence, sin ( ) *dx x a* + ∫ = *x* cos *a* – sin *a* log |sin (*x* + *a*)| + C,

where, C = – C<sup>1</sup> sin *a* + *a* cos *a*, is another arbitrary constant.

$$\begin{aligned} \text{(iii)} \quad &\int \frac{d\mathbf{x}}{1 + \tan x} = \int \frac{\cos x \, dx}{\cos x + \sin x} \\ &= \frac{1}{2} \int \frac{(\cos x + \sin x + \cos x - \sin x) \, dx}{\cos x + \sin x} \\ &= \frac{1}{2} \int dx + \frac{1}{2} \int \frac{\cos x - \sin x}{\cos x + \sin x} \, dx \\ &= \frac{x}{2} + \frac{\mathbf{C}\_1}{2} + \frac{1}{2} \int \frac{\cos x - \sin x}{\cos x + \sin x} \, dx \end{aligned} \tag{10}$$

Now, consider cos sin <sup>I</sup> cos sin *x – x dx x x* = + ∫ Put cos *x* + sin *x* = *t* so that (cos *x* – sin *x*) *dx* = *dt* Therefore <sup>2</sup> I log C *dt t t* = = + ∫ = <sup>2</sup> log cos sin C *x x* + + Putting it in (1), we get C<sup>1</sup> C<sup>2</sup> 1 + + log cos sin 1 tan 2 2 2 2 *dx x x x x* = + + + ∫ = C C 1 2 1 + log cos sin 2 2 2 2 *x x x* + + + = C C 1 2 1 + log cos sin C C 2 2 2 2 *x x x ,* + + = + **EXERCISE 7.2**

Integrate the functions in Exercises 1 to 37:

$$\begin{array}{llll} \text{1.} & \frac{2x}{1+x^2} & \text{2.} & \frac{\left(\log x\right)^2}{x} & \text{3.} & \frac{1}{x+x\log x} \\\\ \text{1.} & \sin x \sin \left(\cos x\right) & \text{5.} & \sin \left(ax+b\right)\cos \left(ax+b\right) \\\\ \text{6.} & \sqrt{ax+b} & \text{7.} & x\sqrt{x+2} & \text{8.} & x\sqrt{1+2x^2} \\\\ \text{9.} & \left(4x+2\right)\sqrt{x^2+x+1} & \text{10.} & \frac{1}{x-\sqrt{x}} & \text{11.} & \frac{x}{\sqrt{x+4}}, x>0 \\\\ \text{12.} & \left(x^3-1\right)^3 & \text{13.} & \frac{x^2}{\left(2+3x\right)^3} & \text{14.} & \frac{1}{x\left(\log x\right)^2}, x>0, \, m \neq 1 \\\\ \text{15.} & \frac{x}{9-4x^2} & \text{16.} & e^{2x+3} & \text{17.} & e^{x^2} \\\\ \text{16.} & \frac{e^{\text{m}^{-1}x}}{1+x^2} & \text{19.} & \frac{e^{2x}-1}{e^{2x}+1} & \text{20.} & \frac{e^{2x}-e^{-2x}}{e^{2x}+e^{-2x}} \end{array}$$

$$\begin{array}{llll} \text{21. } \tan^2(2x-3) & \text{22. } \sec^2\left(7-4x\right) & \text{23. } \frac{\sin^{-1}x}{\sqrt{1-x^2}}\\ \text{24. } \frac{2\cos x-3\sin x}{6\cos x+4\sin x} & \text{25. } \frac{1}{\cos^2 x \left(1-\tan x\right)^2} & \text{26. } \frac{\cos\sqrt{x}}{\sqrt{x}}\\ \text{27. } \sqrt{\sin 2x}\cos 2x & \text{28. } \frac{\cos x}{\sqrt{1+\sin x}} & \text{29. } \cot x \log \sin x\\ \text{30. } \frac{\sin x}{1+\cos x} & \text{31. } \frac{\sin x}{\left(1+\cos x\right)^2} & \text{32. } \frac{1}{1+\cot x} \\ \text{33. } \frac{1}{1-\tan x} & \text{34. } \frac{\sqrt{\tan x}}{\sin x \cos x} & \text{35. } \frac{\left(1+\log x\right)^2}{x} \\ \text{36. } \frac{(x+1)\left(x+\log x\right)^2}{x} & \text{37. } \frac{x^3 \sin\left(\tan^{-1}x^4\right)}{1+x^3} \end{array}$$

Choose the correct answer in Exercises 38 and 39.

$$\begin{aligned} \text{(38. } \int \frac{10x^9 + 10^x \log\_e 10 \, dx}{x^{10} + 10^x} \text{ equals} \\ \text{(A)} \quad 10^x - x^{10} + \text{C} & \quad \text{(B)} \quad 10^x + x^{10} + \text{C} \\ \text{(C)} \quad (10^x - x^{10})^{-1} + \text{C} & \quad \text{(D)} \quad \log\left(10^x + x^{10}\right) + \text{C} \\ \text{(A)} \quad \int \frac{dx}{\sin^2 x \cos^2 x} \text{ equals} \\ \text{(A)} \quad \tan x + \cot x + \text{C} & \quad \text{(B)} \quad \tan x - \cot x + \text{C} \\ \text{(C)} \quad \tan x \cot x + \text{C} & \quad \text{(D)} \quad \tan x - \cot 2x + \text{C} \end{aligned}$$

### **7.3.2** *Integration using trigonometric identities*

When the integrand involves some trigonometric functions, we use some known identities to find the integral as illustrated through the following example.

**Example 7** Find (i) <sup>2</sup> cos *x dx* ∫ (ii) sin 2 cos 3 *x x dx* ∫ (iii) <sup>3</sup> sin *x dx* ∫

#### 242 MATHEMATICS

### **Solution**

(i) Recall the identity cos 2*x* = 2 cos<sup>2</sup> *x* – 1, which gives

$$
\cos^2 x = \frac{1 + \cos 2x}{2}
$$

$$
\text{Therefore, } \quad \int \cos^2 x \, dx = \frac{1}{2} \int (1 + \cos 2x) \, dx = \frac{1}{2} \int d\mathbf{x} + \frac{1}{2} \int \cos 2x \, dx
$$

$$
= \frac{\times}{2} + \frac{1}{4} \sin 2x + \mathbf{C}
$$

$$
= \frac{\times}{2}
$$

(ii) Recall the identity sin *x* cos *y* = 1 2 [sin (*x* + *y*) + sin (*x* – *y*)] (Why?)

$$\langle \text{Why?} \rangle$$

$$\begin{aligned} \text{Then} \quad \int \sin 2x \cos 3x \, dx &= \frac{1}{2} \left[ \int \sin 5x \, dx - \int \sin x \, dx \right] \\ &= \frac{1}{2} \left[ -\frac{1}{5} \cos 5x + \cos x \right] + \text{C} \\ &\ge -\frac{1}{10} \cos 5x + \frac{1}{2} \cos x + \text{C} \\ \text{Then } \sin x \cos x \cos x - \sin x \cos x &= \frac{1}{2} \sin x + \text{C} \end{aligned}$$

$$\begin{aligned} \text{(iii)} \quad \text{From the identity } \sin 3x &= 3 \sin x - 4 \sin^3 x \text{, we find that } \\ \int\_{\sin^3 x}^{\infty} &= \frac{3 \sin x - \sin 3x}{\sqrt{\sin x}} \end{aligned} $$

$$\text{Therefore, } \int \sin^3 x \, dx = \frac{1}{4} \int \sin x \, dx - \frac{1}{4} \int \sin 3x \, dx$$

$$\stackrel{\smile}{\longrightarrow} \stackrel{\smile}{\longcdot} \stackrel{\smile}{\longrightarrow} -\frac{3}{4} \cos \mathfrak{x} + \frac{1}{12} \cos 3\mathfrak{x} + \mathbf{C}$$

**Alternatively,**  3 2 sin sin sin *x dx x x dx* <sup>=</sup> ∫ ∫<sup>=</sup> 2 (1 – cos ) sin *x x dx* ∫ Put cos *x* = *t* so that – sin *x dx* = *dt*

4

$$\begin{aligned} \text{Therefore, } \quad \int \sin^3 x \, dx &= \frac{1}{3} \int \left( 1 - t^2 \right) dt = -\int dt + \int t^2 \, dt = -t + \frac{t^3}{3} + \text{C.}\\ &= -\cos x + \frac{1}{3} \cos^3 x + \text{C.} \end{aligned}$$

*Remark* It can be shown using trigonometric identities that both answers are equivalent.

### **EXERCISE 7.3**

Find the integrals of the functions in Exercises 1 to 22:

| 1.  | sin2<br>(2x + 5)                                                                                | 2.  | sin 3x cos 4x                                                         | 3.  | cos 2x cos 4x cos 6x                               |  |
|-----|-------------------------------------------------------------------------------------------------|-----|-----------------------------------------------------------------------|-----|----------------------------------------------------|--|
| 4.  | sin3<br>(2x + 1)                                                                                | 5.  | sin3 x cos3 x                                                         | 6.  | sin x sin 2x sin 3x                                |  |
| 7.  | sin 4x sin 8x                                                                                   | 8.  | 1<br>–<br>cos<br>x<br>+<br>1<br>cos<br>x                              | 9.  | cos<br>x<br>+<br>1<br>cos<br>x                     |  |
| 10. | sin4 x                                                                                          | 11. | cos4<br>2x                                                            | 12. | 2<br>x<br>sin<br>+<br>1<br>cos<br>x                |  |
| 13. | cos 2<br>x –<br>cos 2<br>α<br>cos<br>x –<br>cos<br>α                                            | 14. | cos<br>x –<br>sin<br>x<br>+<br>1<br>sin 2<br>x                        | 15. | tan3<br>2x sec 2x                                  |  |
| 16. | tan4x                                                                                           | 17. | 3<br>3<br>+<br>sin<br>x<br>cos<br>x<br>2<br>2<br>sin<br>x<br>cos<br>x | 18. | 2<br>+<br>x<br>x<br>cos 2<br>2sin<br>2<br>cos<br>x |  |
| 19. | 1<br>3<br>sin<br>x<br>cos<br>x                                                                  | 20. | cos 2<br>x<br>2<br>x<br>+<br>x<br>(<br>cos<br>sin<br>)                | 21. | sin – 1 (cos x)                                    |  |
| 22. | 1<br>cos (<br>x – a<br>) cos (<br>x – b                                                         | )   |                                                                       |     |                                                    |  |
|     | Choose the correct answer in Exercises 23 and 24.                                               |     |                                                                       |     |                                                    |  |
| 23. | 2<br>2<br>−<br>sin<br>x<br>cos<br>x<br>∫<br>dx<br>is equal to<br>2<br>2<br>sin<br>x<br>cos<br>x |     |                                                                       |     |                                                    |  |
|     | (A)<br>tan x + cot x + C                                                                        |     | (B)                                                                   |     | tan x + cosec x + C                                |  |

$$\begin{array}{ll} \text{(24.)} & \int \frac{e^x (1+x)}{\cos^2(e^x x)} dx \text{ equals} \\ & \text{(A)} \quad -\cot \left( \epsilon x^i \right) + \text{C} \\ & \text{(C)} \quad \tan \left( e^i \right) + \text{C} \end{array} \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\text{(B)} \quad \tan \left( \epsilon e^i \right) + \text{C} \\ & \text{(C)} \quad \tan \left( e^i \right) + \text{C} \end{array}$$

(C) – tan *x* + cot *x* + C (D) tan *x* + sec *x* + C

### **7.4 Integrals of Some Particular Functions**

In this section, we mention below some important formulae of integrals and apply them for integrating many other related standard integrals:

$$(1) \quad \int \frac{d\mathbf{x}}{\mathbf{x}^2 - a^2} = \frac{1}{2a} \log \left| \frac{\mathbf{x} - a}{\mathbf{x} + a} \right| + C$$

$$(2) \quad \int \frac{d\mathbf{x}}{a^2 - \mathbf{x}^2} = \frac{1}{2a} \log \left| \frac{a+\mathbf{x}}{a-\mathbf{x}} \right| + \mathbf{C}$$

$$(3) \quad \int \frac{d\mathbf{x}}{\frac{1}{2} - \frac{1}{2}} = \frac{1}{4} \tan^{-1} \frac{\mathbf{x}}{-} + \mathbf{C}$$

$$\text{(3)} \quad \int \frac{\text{at}}{\text{x}^2 + a^2} = \frac{1}{a} \tan^{-1} \frac{a}{a} + c$$

$$\mathbf{(4)} \quad \int \frac{d\mathbf{x}}{\sqrt{\mathbf{x}^2 - a^2}} = \log\left|\mathbf{x} + \sqrt{\mathbf{x}^2 - a^2}\right| + \mathbf{C}$$

$$\text{(5)} \quad \int \frac{d\mathbf{x}}{\sqrt{a^2 - \mathbf{x}^2}} = \sin^{-1}\frac{\mathbf{x}}{a} + \mathbf{C}$$

$$\mathbf{u}(6) \quad \int \frac{d\mathbf{x}}{\sqrt{\mathbf{x}^2 + a^2}} = \log\left|\mathbf{x} + \sqrt{\mathbf{x}^2 + a^2}\right| + C$$

We now prove the above results:

\*\*(1)\*\* We have \*\* $\frac{1}{x^2 - a^2} = \frac{1}{(x - a)(x + a)}$ 

$$= \frac{1}{2a} \left[ \frac{(x + a) - (x - a)}{(x - a)(x + a)} \right] = \frac{1}{2a} \left[ \frac{1}{x - a} - \frac{1}{x + a} \right]$$

Therefore,  $\int \frac{dx}{x^2 - a^2} = \frac{1}{2a} \left[ \int \frac{dx}{x - a} - \int \frac{dx}{x + a} \right]$ 

$$= \frac{1}{2a} \left[ \log|\left(x - a\right)| - \log|\left(x + a\right)| \right] + C$$

$$= \frac{1}{2a} \log \left| \frac{x - a}{x + a} \right| + C$$

**(2)** In view of (1) above, we have

$$\frac{1}{a^2 - \chi^2} = \frac{1}{2a} \left[ \frac{(a+\chi) + (a-\chi)}{(a+\chi)(a-\chi)} \right] = \frac{1}{2a} \left[ \frac{1}{a-\chi} + \frac{1}{a+\chi} \right]$$

$$\begin{aligned} \text{Therefore, } \int \frac{dx}{a^2 - x^2} &= \frac{1}{2a} \left[ \int \frac{dx}{a - \chi} + \int \frac{dx}{a + \chi} \right] \\ &= \frac{1}{2a} \left[ -\log|a - \chi| + \log|a + \chi| \right] + \text{Cl} \\ &= \frac{1}{2a} \log \left| \frac{a + \chi}{a - \chi} \right| + \text{Cl} \end{aligned}$$

A**Note** The technique used in (1) will be explained in Section 7.5.

$$\begin{aligned} \text{(3)} \quad \text{Put } x = a \tan \theta. \text{ Then } dx = a \sec^2 \theta \, d\theta. \\ \text{Therefore, } \quad \int \frac{dx}{x^2 + a^2} = \int \frac{a \sec^2 \theta \, d\theta}{a^2 \tan^2 \theta + a^2} \\ \text{(4)} \quad \text{Let } x = a \sec \theta. \text{ Then } dx = a \sec \theta \tan \theta \, d\theta. \\ \text{Therefore, } \quad \int \frac{dx}{\sqrt{x^2 - a^2}} = \int \frac{a \sec \theta \tan \theta \, d\theta}{\sqrt{a^2 \sec^2 \theta - a^2}} \\ = \int \sec \theta \, d\theta = \log \left| \sec \theta + \tan \theta \right| + C\_1 \\ = \log \left| \frac{\sqrt{x}}{a} + \sqrt{\frac{x^2}{a^2} - 1} \right| + C\_1 \\ = \log \left| x + \sqrt{x^2 - a^2} \right| - \log \left| a \right| + C\_1 \\ = \log \left| x + \sqrt{x^2 - a^2} \right| + C, \text{ where C = C\_1 - \log \ln |a| \\ \text{(5)} \quad \text{Let } x = a \sec \theta. \text{ Then } dx = a \sec \theta \, d\theta \end{aligned}$$

**(5)** Let *x* = *a* sinθ. Then *dx* = *a* cosθ dθ.

$$\begin{aligned} \text{Therefore,} \\ \int \frac{dx}{\sqrt{a^2 - x^2}} &= \int \frac{a \cos \theta \, d\theta}{\sqrt{a^2 - a^2 \sin^2 \theta}} \\ &= \int d\theta = \theta + \mathcal{C} = \sin^{-1} \frac{\mathcal{X}}{a} + \mathcal{C} \\ \text{Let } \mathbf{x} = a \tan \theta. \text{ Then } dx = a \sec^2 \theta. \text{ d.} \end{aligned}$$

**(6)** Let *x* = *a* tan θ. Then *dx* = *a* sec<sup>2</sup>θ dθ.

$$\begin{aligned} \text{Therefore,} \qquad & \int \frac{d\mathbf{x}}{\sqrt{\mathbf{x}^2 + a^2}} = \begin{aligned} &\int \frac{a \sec^2 \theta \, d\theta}{\sqrt{a^2 \tan^2 \theta + a^2}} \\ &= \int \sec \theta \, d\theta = \log \left| (\sec \theta + \tan \theta) \right| + C\_1 \end{aligned} $$

$$\begin{aligned} &= \left| \log \left| \frac{\mathbf{x}}{a} + \sqrt{\frac{\mathbf{x}^2}{a^2} + 1} \right| + \mathbf{C}\_1 \right| \\ &= \left| \log \left| \mathbf{x} + \sqrt{\mathbf{x}^2 + a^2} \right| - \log|a| + \mathbf{C}\_1 \\ &= \left| \log \left| \mathbf{x} + \sqrt{\mathbf{x}^2 + a^2} \right| + \mathbf{C}, \text{ where } \mathbf{C} = \mathbf{C}\_1 - \log|a| \end{aligned} \right.$$

Applying these standard formulae, we now obtain some more formulae which are useful from applications point of view and can be applied directly to evaluate other integrals.

**(7) To find the integral** <sup>2</sup> *dx ax bx c* + + ∫ , we write *ax*<sup>2</sup> + *bx* + *c* = 2 2 2 2 2 4 *b c b c b a x x a x – a a a a a* + + = + + 

$$\text{Now, put } x + \frac{b}{2a} = t \text{ so that } dx = dt \text{ and } \sqrt{\text{writing } \frac{c}{a} - \frac{b^2}{4a^2}} = \pm k^2 \text{. We find the }$$

integral reduced to the form 2 2 1 *dt a t k* ± ∫ depending upon the sign of 2 2 4 *c b – a a* and hence can be evaluated.

**(8) To find the integral of the type** , proceeding as in (7), we

obtain the integral using the standard formulae.

**(9) To find the integral of the type** <sup>2</sup> *px q dx ax bx c* + + + ∫ , where *p*, *q*, *a*, *b*, *c* are

constants, we are to find real numbers A, B such that

$$p\infty + q = \mathbf{A}\,\frac{d}{d\mathbf{x}}(a\mathbf{x}^2 + b\mathbf{x} + c) + \mathbf{B} = \mathbf{A}\,(2a\mathbf{x} + b) + \mathbf{B}$$

To determine A and B, we equate from both sides the coefficients of *x* and the constant terms. A and B are thus obtained and hence the integral is reduced to one of the known forms.

**(10) For the evaluation of the integral of the type** 2 ( ) *px q dx ax bx c* + + + ∫ , we proceed

as in (9) and transform the integral into known standard forms.

Let us illustrate the above methods by some examples.

**Example 8** Find the following integrals:

$$\text{(i)} \quad \int \frac{d\mathbf{x}}{\mathbf{x}^2 - 16} \qquad\qquad\qquad\text{(ii)} \quad \int \frac{d\mathbf{x}}{\sqrt{2\mathbf{x} - \mathbf{x}^2}}$$

**Solution**

$$\text{(i)}\quad \text{We have } \int \frac{d\mathbf{x}}{\mathbf{x}^2 - 16} = \int \frac{d\mathbf{x}}{\mathbf{x}^2 - 4^2} = \frac{1}{8} \log \left| \frac{\mathbf{x} - 4}{\mathbf{x} + 4} \right| + \text{C} \quad \text{[by 7.4 (1)]}$$

$$\text{(ii)} \quad \int \frac{d\boldsymbol{\alpha}}{\sqrt{2\boldsymbol{\alpha} - \boldsymbol{\alpha}^2}} = \int \frac{d\boldsymbol{\alpha}}{\sqrt{1 - \left(\boldsymbol{\alpha} - 1\right)^2}}.$$

Put *x* – 1 = *t*. Then *dx* = *dt*.

$$\text{Therefore, } \qquad \int \frac{dx}{\sqrt{2x - x^2}} = \int \frac{dt}{\sqrt{1 - t^2}} = \sin^{-1}(t) + C \qquad \qquad \text{[by 7.4 (S)]}$$

$$=\sin^{-1}\left(\mathbf{x}-1\right)+\mathbf{C}$$

**Example 9** Find the following integrals :

$$\text{(i)} \quad \int \frac{dx}{x^2 - 6x + 13} \qquad \text{(ii)} \quad \int \frac{dx}{3x^2 + 13x - 10} \qquad \text{(iii)} \quad \int \frac{dx}{\sqrt{5x^2 - 2x}}$$

### **Solution**

$$\text{2(i)}\quad \text{We have: } \ x^2 + 6\alpha + 1\overline{3} = \lambda^2 - 6\alpha + 3^2 - 3^2 + 13 = (\alpha - 3)^2 + 4\alpha$$

$$\text{So, } \quad \sqrt{\frac{1}{\sqrt{2}}} \int \frac{dx}{x^2 - 6x + 13} = \int \frac{1}{\left(x - 3\right)^2 + 2^2} \, dx$$

$$\text{Let } \begin{array}{c} \text{Let } \\ \cdot \end{array} \begin{array}{c} \text{x} - \text{3} = \text{t. Then } d\text{x} = dt \\ \cdot \end{array}$$

$$\begin{aligned} \text{Therefore,} \qquad \int \frac{d\mathbf{x}}{\mathbf{x}^2 - 6\mathbf{x} + 13} &= \int \frac{dt}{t^2 + 2^2} = \frac{1}{2} \tan^{-1} \frac{t}{2} + \mathbf{C} & \qquad \text{[by 7.4 (3)]}\\ &= \frac{1}{2} \tan^{-1} \frac{\mathbf{x} - 3}{2} + \mathbf{C} \end{aligned}$$

#### 248 MATHEMATICS

(ii) The given integral is of the form 7.4 (7). We write the denominator of the integrand,

$$\begin{aligned} 3x^2 + 13x - 10 &= 3\left(x^2 + \frac{13x}{3} - \frac{10}{3}\right) \\ &= 3\left[\left(x + \frac{13}{6}\right)^2 - \left(\frac{17}{6}\right)^2\right] \text{ (completing the square)} \end{aligned}$$

$$\text{Thus}\quad\int \frac{dx}{3x^2 + 13x - 10} = \frac{1}{3} \int \frac{dx}{\left(x + \frac{13}{6}\right)^2 - \left(\frac{17}{6}\right)^2}$$

Put 13 6 *x t* + = . Then *dx* = *dt*.

$$\text{Therefore, } \quad \int \frac{dx}{3x^2 + 13x - 10} = \frac{1}{3} \int \frac{dt}{t^2 - \left(\frac{17}{6}\right)^2} \times \frac{1}{3}$$

$$=\frac{1}{3\times2\times\frac{17}{6}}\log\left|\frac{t-\frac{17}{6}}{t+\frac{17}{6}}\right|+\text{C}\_1\tag{\text{by 7.4 (i)}}$$

$$=\frac{1}{17}\log\left|\frac{\mathbf{x}+\frac{13}{6}-\frac{17}{6}}{\mathbf{x}+\frac{13}{6}+\frac{17}{6}}\right|+\mathbf{C\_1}$$

$$=\frac{1}{17}\log\left|\frac{6\mathbf{x}-4}{6\mathbf{x}+30}\right|+\mathbf{C\_1}$$

$$=\frac{1}{17}\log\left|\frac{3\mathbf{x}-2}{\mathbf{x}+5}\right|+\mathbf{C\_1}+\frac{1}{17}\log\frac{1}{3}$$

$$=\frac{1}{17}\log\left|\frac{3\mathbf{x}-2}{\mathbf{x}+5}\right|+\mathbf{C\_1}\text{ where }\mathbf{C}=\mathbf{C\_1}+\frac{1}{17}\log\frac{1}{3}$$

$$\begin{aligned} \text{(iii)} \quad &\text{We have } \int \frac{dx}{\sqrt{5x^2 - 2x}} = \int \frac{dx}{\sqrt{5\left(x^2 - \frac{2x}{5}\right)}} \\ &= \frac{1}{\sqrt{5}} \int \frac{dx}{\sqrt{\left(x - \frac{1}{5}\right)^2 - \left(\frac{1}{5}\right)^2}} \text{ (completing the square)}. \end{aligned}$$

Put 1 5 *x – t* = . Then *dx* = *dt*.

$$\begin{aligned} \text{Therefore, } \qquad \int \frac{dx}{\sqrt{5x^2 - 2x}} &= \frac{1}{\sqrt{5}} \int \frac{dt}{\sqrt{t^2 - \left(\frac{1}{5}\right)^2}} \\ &= \frac{1}{\sqrt{5}} \log \left| t + \sqrt{t^2 - \left(\frac{1}{5}\right)^2} \right| + C \qquad \text{[by 7.4 (4)]} \\ &= \frac{1}{\sqrt{5}} \log \left| x - \frac{1}{5} + \sqrt{x^2 - \frac{2x}{5}} \right| + C \end{aligned}$$

**Example 10** Find the following integrals:

$$\text{(i)} \quad \int \frac{\lambda + 2}{2\lambda^2 + 6\lambda + 5} \, d\lambda$$

### **Solution**

(i) Using the formula 7.4 (9), we express

$$\mathbf{x} + \mathbf{2} = \mathbf{A} \frac{d}{d\mathbf{x}} (2\boldsymbol{\omega}^2 + 6\boldsymbol{\omega} + \mathbf{5}) + \mathbf{B} \stackrel{\cdot}{=} \mathbf{A} \left(4\boldsymbol{\omega} + 6\boldsymbol{\uptheta}\right) + \mathbf{B}$$

Equating the coefficients of *x* and the constant terms from both sides, we get

$$\begin{aligned} \text{4A = 1 and 6A + B = 2 \quad \text{or} \quad A = \frac{1}{4} \text{ and B = } \frac{1}{2}.\\ \text{Therefore, } \quad \int \frac{x+2}{2x^2 + 6x + 5} = \frac{1}{4} \int \frac{4x+6}{2x^2 + 6x + 5} dx + \frac{1}{2} \int \frac{dx}{2x^2 + 6x + 5} \\ = \frac{1}{4} \text{I}\_1 + \frac{1}{2} \text{I}\_2 \qquad \text{(say)} \quad \qquad \qquad \dots \text{(1)} \end{aligned}$$

#### 250 MATHEMATICS

In I<sup>1</sup> , put 2*x* 2 + 6*x* + 5 = *t*, so that (4*x* + 6) *dx* = *dt* Therefore, I 1 = <sup>1</sup> log C *dt t t* = + ∫ = 2 1 log | 2 6 5 | C *x x* + + + ... (2)

and 
$$\mathbf{I}\_2 = \int \frac{d\mathbf{x}}{2\boldsymbol{\chi}^2 + 6\boldsymbol{\chi} + \mathbf{S}} = \frac{1}{2} \int \frac{d\mathbf{x}}{\boldsymbol{\chi}^2 + 3\boldsymbol{\chi} + \frac{\mathbf{S}}{2}}$$
 
$$= \frac{1}{2} \int \frac{d\mathbf{x}}{\left(\mathbf{x} + \frac{3}{2}\right)^2 + \left(\frac{1}{2}\right)^2} \qquad \bigvee \qquad \bigvee \qquad \bigvee \qquad \mathbf{C}$$

Put <sup>3</sup> 2 *x t* + = , so that *dx* = *dt*, we get

$$\mathbf{I}\_2 = \frac{1}{2} \left[ \frac{dt}{t^2 + \left(\frac{1}{2}\right)^2} = \frac{1}{2 \times \frac{1}{2}} \tan^{-1} 2t + \mathbf{C}\_2 \right] \tag{\text{by 7.4 (3)}}$$

$$\sum\_{\dots} \text{ = } \tan^{-1} \mathbf{2} \left( \mathbf{x} + \frac{\mathbf{3}}{2} \right) + \mathbf{C}\_2 = \tan^{-1} \left( 2x + 3 \right) + \mathbf{C}\_2 \qquad \dots \text{ (3)}$$

Using (2) and (3) in (1), we get

$$\int \frac{x+2}{2x^2+6x+5} \, dx = \frac{1}{4} \log \left| 2x^2 + 6x + 5 \right| + \frac{1}{2} \tan^{-1} \left( 2x + 3 \right) + C$$

where, C = C C 1 2 4 2 +

(ii) This integral is of the form given in 7.4 (10). Let us express

$$\alpha + \mathfrak{Z} = \operatorname{A} \frac{d}{d\mathfrak{x}} \left( \mathfrak{F} - 4\mathfrak{x} - \mathfrak{x}^2 \right) + \operatorname{B} = \operatorname{A} \left( -4 - 2\mathfrak{x} \right) + \operatorname{B} \mathfrak{F}$$

Equating the coefficients of *x* and the constant terms from both sides, we get

$$- \text{ 2A} = 1 \text{ and } -4 \text{ A} + \text{B} = 3 \text{, i.e., } \text{A} = -\frac{1}{2} \text{ and B} = 1$$

$$\begin{aligned} \text{Therefore,} \quad \int \frac{\mathbf{x} + 3}{\sqrt{5 - 4\mathbf{x} - \mathbf{x}^2}} d\mathbf{x} &= -\frac{1}{2} \int \frac{\left(-4 - 2\mathbf{x}\right) d\mathbf{x}}{\sqrt{5 - 4\mathbf{x} - \mathbf{x}^2}} + \int \frac{d\mathbf{x}}{\sqrt{5 - 4\mathbf{x} - \mathbf{x}^2}} \\ &= -\frac{1}{2} \left[ \mathbf{I}\_1 + \mathbf{I}\_2 \right] \end{aligned} \tag{1}$$

In I<sup>1</sup> , put 5 – 4*x* – *x* 2 = *t*, so that (– 4 – 2*x*) *dx* = *dt*.

$$\begin{aligned} \text{Therefore,} & \qquad \mathbf{I}\_{\mathbf{i}} = \int \frac{(-4 - 2\boldsymbol{x}) \, d\mathbf{x}}{\sqrt{5 - 4\boldsymbol{x} - \boldsymbol{x}^{2}}} = \int \frac{d\mathbf{t}}{\sqrt{\mathbf{t}}} = 2\sqrt{\mathbf{t}} + \mathbf{C}\_{1} \\ & = 2\sqrt{5 - 4\boldsymbol{x} - \boldsymbol{x}^{2}} + \mathbf{C}\_{1} \\ \text{Now consider} & \qquad \mathbf{I}\_{\mathbf{i}} = \int \frac{d\mathbf{x}}{\sqrt{5 - 4\boldsymbol{x}^{2} - \boldsymbol{x}^{2}}} = \int \frac{d\mathbf{x}}{\sqrt{9 - \left(\mathbf{x} + \mathbf{2}\right)^{2}}} \end{aligned} \tag{21}$$

Put *x* + 2 = *t*, so that *dx* = *dt*.

Therefore, I 2 = 1 2 2 2 sin + C 3 3 *dt t – t* = − ∫ [by 7.4 (5)]

$$\mathbf{b} = \sin^{-1}\frac{\mathbf{x} + \mathbf{2}}{\sqrt{3}} + \mathbf{C}\_2 \quad \quad \quad \quad \quad \quad \quad \quad \quad \dots \text{ (3)}$$

Substituting (2) and (3) in (1), we obtain

$$\int \frac{\mathbf{x} + \mathbf{3}}{\sqrt{5 - 4\mathbf{x} - \mathbf{x}^2}} = -\sqrt{5 - 4\mathbf{x} - \mathbf{x}^2} + \sin^{-1}\frac{\mathbf{x} + \mathbf{2}}{3} + \mathbf{C}, \text{ where } \mathbf{C} = \mathbf{C}\_2 - \frac{\mathbf{C}\_1}{2}$$

**EXERCISE 7.4**

Integrate the functions in Exercises 1 to 23.

$$\begin{array}{ccccc} \text{1.} & \frac{3x^2}{x^6+1} & \text{2.} & \frac{1}{\sqrt{1+4x^2}} & \text{3.} & \frac{1}{\sqrt{\left(2-x\right)^2+1}}\\ \text{4.} & \frac{1}{\sqrt{9-25x^2}} & \text{5.} & \frac{3x}{1+2x^4} & \text{6.} & \frac{x^2}{1-x^6} \\ \text{7.} & \frac{x-1}{\sqrt{x^2-1}} & \text{8.} & \frac{x^2}{\sqrt{x^6+a^6}} & \text{9.} & \frac{\sec^2x}{\sqrt{\tan^2x+4}} \\ \end{array}$$

$$\begin{array}{llll} \text{10.} & \frac{1}{\sqrt{x^2+2x+2}} & \text{11.} & \frac{1}{9x^2+6x+5} & \text{12.} & \frac{1}{\sqrt{7-6x-x^2}}\\ \text{13.} & \frac{1}{\sqrt{(x-1)(x-2)}} & \text{14.} & \frac{1}{\sqrt{8+3x-x^2}} & \text{15.} & \frac{1}{\sqrt{(x-a)(x-b)}}\\ \text{16.} & \frac{4x+1}{\sqrt{2x^2+x-3}} & \text{17.} & \frac{x+2}{\sqrt{x^2-1}} & \text{18.} & \frac{5x-2}{1+2x+3x^2}\\ \text{19.} & \frac{6x+7}{\sqrt{(x-5)(x-4)}} & \text{20.} & \frac{x+2}{\sqrt{4x-x^2}} & \text{21.} & \frac{x+2}{\sqrt{x^2+2x+3}}\\ \text{22.} & \frac{x+3}{x^2-2x-5} & \text{23.} & \frac{5x+3}{\sqrt{x^2+4x+10}} & \text{18.} \end{array}$$

Choose the correct answer in Exercises 24 and 25.

$$\begin{aligned} \text{24.} \quad & \int \frac{dx}{\mathbf{x}^2 + 2x + 2} \text{ equals} \\ & \text{(A)} \quad x \tan^{-1}(x+1) + \text{C} \qquad & \text{(B)} \quad \tan^{-1}(x+1) + \text{C} \\ & \text{(C)} \quad (x+1)\tan^{-1}x + \text{C} \qquad & \text{(D)} \quad \tan^{-1}x + \text{C} \\ & \text{25.} \quad & \int \frac{dx}{\sqrt{9x - 4x^2}} \text{ equals} \\ & \text{(A)} \quad \frac{1}{9} \sin^{-1}\left(\frac{9x - 8}{8}\right) + \text{C} \qquad & \text{(B)} \quad \frac{1}{2} \sin^{-1}\left(\frac{8x - 9}{9}\right) + \text{C} \\ & \text{(C)} \quad \frac{1}{3} \sin^{-1}\left(\frac{9x - 8}{8}\right) + \text{C} \qquad & \text{(D)} \quad \frac{1}{2} \sin^{-1}\left(\frac{9x - 8}{8}\right) + \text{C} \end{aligned}$$

### **7.5 Integration by Partial Fractions**

Recall that a rational function is defined as the ratio of two polynomials in the form P( ) Q( ) *x x* , where P (*x*) and Q(*x*) are polynomials in *x* and Q(*x*) ≠ 0. If the degree of P(*x*)

is less than the degree of Q(*x*), then the rational function is called proper, otherwise, it is called improper. The improper rational functions can be reduced to the proper rational

$$\text{functions by long division process. Thus, if } \frac{\mathbf{P}(\mathbf{x})}{\mathbf{Q}(\mathbf{x})} \text{ is improper, then } \frac{\mathbf{P}(\mathbf{x})}{\mathbf{Q}(\mathbf{x})} = \mathbf{T}(\mathbf{x}) + \frac{\mathbf{P}\_1(\mathbf{x})}{\mathbf{Q}(\mathbf{x})}, \text{ then } \mathbf{P}\_2(\mathbf{x}) = \mathbf{T}(\mathbf{x}) + \frac{\mathbf{P}\_2(\mathbf{x})}{\mathbf{Q}(\mathbf{x})} \mathbf{T}(\mathbf{x}) = \mathbf{T}(\mathbf{x}) + \frac{\mathbf{P}\_1(\mathbf{x})}{\mathbf{Q}(\mathbf{x})} \mathbf{T}(\mathbf{x}) = \mathbf{T}(\mathbf{x}) + \frac{\mathbf{P}\_2(\mathbf{x})}{\mathbf{Q}(\mathbf{x})} \mathbf{T}(\mathbf{x}) = \mathbf{T}(\mathbf{x}) + \frac{\mathbf{P}\_1(\mathbf{x})}{\mathbf{Q}(\mathbf{x})} \mathbf{T}(\mathbf{x}) = \mathbf{T}(\mathbf{x}) + \frac{\mathbf{P}\_2(\mathbf{x})}{\mathbf{Q}(\mathbf{x})} \mathbf{T}(\mathbf{x})$$

where T(*x*) is a polynomial in *x* and P ( ) <sup>1</sup> Q( ) *x x* is a proper rational function. As we know

how to integrate polynomials, the integration of any rational function is reduced to the integration of a proper rational function. The rational functions which we shall consider here for integration purposes will be those whose denominators can be factorised into

linear and quadratic factors. Assume that we want to evaluate P( ) Q( ) *x dx x* ∫ , where P( ) Q( ) *x x*

is proper rational function. It is always possible to write the integrand as a sum of simpler rational functions by a method called partial fraction decomposition. After this, the integration can be carried out easily using the already known methods. The following Table 7.2 indicates the types of simpler partial fractions that are to be associated with various kind of rational functions.

| S.No. | Form of the rational function                                                               | Form of the partial fraction                                         |
|-------|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| 1.    | +<br>px<br>q<br>≠<br>, a<br>b<br>(<br>x<br>–<br>a<br>) (<br>x<br>–<br>b<br>)                | A<br>B<br>+<br>x – a<br>x – b                                        |
| 2.    | +<br>px<br>q<br>2<br>(<br>x<br>–<br>a<br>)                                                  | A<br>B<br>+<br>)2<br>x – a<br>x – a<br>(                             |
| 3.    | 2<br>+<br>+<br>px<br>qx<br>r<br>x<br>a<br>x – b<br>x – c<br>(<br>–<br>) (<br>) (<br>)       | A<br>B<br>C<br>+<br>+<br>x – a<br>x – b<br>x – c                     |
| 4.    | 2<br>+<br>+<br>px<br>qx<br>r<br>2<br>(<br>x<br>–<br>a<br>)<br>(<br>x – b<br>)               | A<br>B<br>C<br>+<br>+<br>2<br>x – a<br>x – b<br>(<br>x – a<br>)      |
| 5.    | 2<br>+<br>+<br>px<br>qx<br>r<br>2<br>+<br>+<br>(<br>x<br>–<br>a<br>) (<br>x<br>bx<br>c<br>) | A<br>B<br>x<br>+ C<br>,<br>+<br>2<br>x – a<br>+<br>+<br>x<br>bx<br>c |
|       | where x<br>2<br>+ bx + c cannot be factorised further                                       |                                                                      |

**Table 7.2**

In the above table, A, B and C are real numbers to be determined suitably.

$$\text{Example 11 Find } \int \frac{dx}{\left(\alpha + 1\right)\left(x + 2\right)}$$

**Solution** The integrand is a proper rational function. Therefore, by using the form of partial fraction [Table 7.2 (i)], we write

$$\frac{1}{\left(\mathbf{x} + \mathbf{l}\right)\left(\mathbf{x} + \mathbf{2}\right)} = \frac{\mathbf{A}}{\mathbf{x} + 1} + \frac{\mathbf{B}}{\mathbf{x} + 2} \tag{1}$$

where, real numbers A and B are to be determined suitably. This gives

$$1 = \mathbf{A} \ (\mathbf{x} + \mathbf{2}) + \mathbf{B} \ (\mathbf{x} + \mathbf{1}).$$

Equating the coefficients of *x* and the constant term, we get

$$\mathbf{A} + \mathbf{B} = 0$$

$$\mathbf{\hat{P}A} + \mathbf{B} = 1$$

$$\begin{aligned} \text{and} \\ \text{Solvinor these amounts we get } \mathbf{A} - \mathbf{1} \text{ and } \mathbf{B} - \mathbf{1} \end{aligned}$$

Solving these equations, we get A =1 and B = – 1.

Thus, the integrand is given by

$$\frac{1}{\left(\infty+1\right)\left(\infty+2\right)} = \frac{1}{\left(\infty+1\right)} + \frac{-1}{\left(\infty+2\right)}$$

$$\begin{aligned} \text{Therefore,} \\ & \int \frac{dx}{\left(\frac{x+1}{\sqrt{x+1}}\right)\left(x+2\right)} = \int \frac{dx}{\sqrt{x+1}} - \int \frac{dx}{x+2} \\ & = \log|x+1| - \log|x+2| + C \\ & = \log\left|\frac{x+1}{x+2}\right| + C \end{aligned}$$

*Remark* The equation (1) above is an identity, i.e. a statement true for all (permissible) values of *x*. Some authors use the symbol '≡' to indicate that the statement is an identity and use the symbol '=' to indicate that the statement is an equation, i.e., to indicate that the statement is true only for certain values of *x*.

$$\text{Example 12 Find } \int \frac{x^2 + 1}{x^2 - 5x + 6} \, dx$$

**Solution** Here the integrand 2 2 1 5 6 *x x – x* + + is not proper rational function, so we divide *x* 2 + 1 by *x* 2 – 5*x* + 6 and find that

$$\frac{\mathbf{x}^2 + 1}{\mathbf{x}^2 - 5\mathbf{x} + 6} = 1 + \frac{5\mathbf{x} - 5}{\mathbf{x}^2 - 5\mathbf{x} + 6} = 1 + \frac{5\mathbf{x} - 5}{(\mathbf{x} - 2)(\mathbf{x} - 3)}$$

$$\text{Let } \mathbf{ \tilde{S}}\mathbf{x} - \mathbf{S} = \frac{\mathbf{A}}{(\mathbf{x} - 2)(\mathbf{x} - 3)} = \frac{\mathbf{A}}{\mathbf{x} - 2} + \frac{\mathbf{B}}{\mathbf{x} - 3}$$

$$\text{So that } \mathbf{ \tilde{S}}\mathbf{x} - \mathbf{S} = \mathbf{A}\left(\mathbf{x} - 3\right) + \mathbf{B}\left(\mathbf{x} - 2\right)$$

Let

Equating the coefficients of *x* and constant terms on both sides, we get A + B = 5 and 3A + 2B = 5. Solving these equations, we get A = – 5 and B = 10

$$\text{Thus,}\qquad\frac{\text{x}^2+1}{\text{x}^2-\text{5x}+6}=1-\frac{\text{5}}{\text{x}-\text{2}}+\frac{10}{\text{x}-\text{3}}.$$

Therefore,

$$\begin{aligned} \int \frac{\chi^2 + 1}{\chi^2 - 5\chi + 6} \, d\mathfrak{x} &= \int d\mathfrak{x} - 5 \int \frac{1}{\chi - 2} \, d\mathfrak{x} + 10 \int \frac{d\mathfrak{x}}{\chi - 3} \, d\mathfrak{x} \\ &= \mathfrak{x} - 5 \log|\mathfrak{x} - 2| + 10 \log|\mathfrak{x} - 3| + \text{C.} \end{aligned}$$

**Example 13** Find <sup>2</sup> 3 2 ( 1) ( 3) *x dx x x* − + + ∫

**Solution** The integrand is of the type as given in Table 7.2 (4). We write

$$\frac{3\mathbf{x} - 2\mathbf{a}}{\left(\mathbf{x} + 1\right)^2 \left(\mathbf{x} + 3\right)} = \frac{\mathbf{A}}{\mathbf{x} + 1} + \frac{\mathbf{C}}{\left(\mathbf{x} + 1\right)^2} + \frac{\mathbf{C}}{\mathbf{x} + 3}$$

$$\text{So that}$$

$$\begin{pmatrix} 3\mathbf{x} - 2 = \mathbf{A} \ \left(\mathbf{x} + 1\right) \left(\mathbf{x} + 3\right) + \mathbf{B} \ \left(\mathbf{x} + 3\right) + \mathbf{C} \ \left(\mathbf{x} + 1\right)^2\\ \vdots \end{pmatrix}$$

$$\equiv \mathbf{A} \left(\mathbf{x}^2 + 4\mathbf{x} + 3\right) + \mathbf{B} \ \left(\mathbf{x} + 3\right) + \mathbf{C} \ \left(\mathbf{x}^2 + 2\mathbf{x} + 1\right)$$

Comparing coefficient of *x* 2 , *x* and constant term on both sides, we get A + C = 0, 4A + B + 2C = 3 and 3A + 3B + C = – 2. Solving these equations, we get

11 5 11 A B and C 4 2 4 *– –* = = = *,* . Thus the integrand is given by

$$\frac{3x-2}{\left(\alpha+1\right)^{2}\left(x+3\right)} = \frac{11}{4\left(x+1\right)} - \frac{5}{2\left(x+1\right)^{2}} - \frac{11}{4\left(x+3\right)}$$

$$\text{Therefore, } \int \frac{3x-2}{\left(x+1\right)^{2}\left(x+3\right)} = \frac{11}{4} \int \frac{dx}{x+1} - \frac{5}{2} \int \frac{dx}{\left(x+1\right)^{2}} - \frac{11}{4} \int \frac{dx}{x+3}$$

$$= \frac{11}{4} \log \left| \begin{array}{c} x+1 \\ \end{array} \right| + \frac{5}{2\left(x+1\right)} - \frac{11}{4} \log \left| \begin{array}{c} x+3 \\ \end{array} \right| + C$$

$$= \frac{11}{4} \log \left| \frac{x+1}{x+3} \right| + \frac{5}{2\left(x+1\right)} + C$$

$$\text{Example 14 Find } \int \frac{x^2}{\left(x^2 + 1\right)\left(x^2 + 4\right)} dx$$

$$\text{Solution }\text{ Consider }\frac{\text{x}^2}{\left(\text{x}^2+1\right)\left(\text{x}^2+4\right)}\text{ and put }\text{x}^2=\text{y.}$$

Then

$$\frac{\chi^2}{\left(\chi^2+1\right)\left(\chi^2+4\right)} = \frac{\chi}{\left(\chi+1\right)\left(\chi+4\right)}$$

$$\text{Write}\qquad\qquad\qquad\frac{\text{y}}{\text{(y+1)(y+4)}}=\frac{\text{A}}{\text{y}+1}+\frac{\text{B}}{\text{y}+4}$$

Thus,

So that *y* = A (*y* + 4) + B (*y* + 1)

Comparing coefficients of *y* and constant terms on both sides, we get A + B = 1 and 4A + B = 0, which give

$$\mathbf{A} = -\frac{1}{3} \quad \text{and} \quad \mathbf{B} = \frac{4}{3}$$

$$\frac{\chi^2}{\left(\chi^2+1\right)\left(\chi^2+4\right)} = -\frac{1}{3\left(\chi^2+1\right)} + \frac{4}{3\left(\chi^2+4\right)}$$

$$\begin{aligned} \text{Therefore,} \qquad & \int \frac{x^2 dx}{(x^2+1)\left(x^2+4\right)} = -\frac{1}{3} \int \frac{dx}{x^2+1} + \frac{4}{3} \int \frac{dx}{x^2+4} \\ & \qquad \qquad = -\frac{1}{3} \tan^{-1} x + \frac{4}{3} \times \frac{1}{2} \tan^{-1} \frac{x}{2} + C \\ & \qquad \qquad \qquad = -\frac{1}{3} \tan^{-1} x + \frac{2}{3} \tan^{-1} \frac{x}{2} + C \end{aligned}$$

In the above example, the substitution was made only for the partial fraction part and not for the integration part. Now, we consider an example, where the integration involves a combination of the substitution method and the partial fraction method.

$$\text{Example 15 Find } \int \frac{\left(3\sin\phi - 2\right)\cos\phi}{5 - \cos^2\phi - 4\sin\phi} \,d\phi$$

**Solution** Let *y* = sinφ

$$\text{Then } \qquad \qquad d\mathbf{y} = \cos\phi \,\, d\phi$$

Therefore, ( ) 2 3 sin 2 cos 5 cos 4 sin *– d – –* φ φ φ φ φ ∫ = <sup>2</sup> (3 – 2) 5 (1 ) 4 *y dy – – y – y* ∫ = <sup>2</sup> 3 2 4 4 *y – dy y – y* + ∫ = ( )<sup>2</sup> 3 2 I (say) 2 *y – y –* <sup>=</sup> ∫

Now, we write

( )<sup>2</sup> 3 2 2 *y – y –* = <sup>2</sup> A B *y* 2 ( 2) *y* + − − [by Table 7.2 (2)]

Therefore, 3*y* – 2 = A (*y* – 2) + B

Comparing the coefficients of *y* and constant term, we get A = 3 and B – 2A = – 2, which gives A = 3 and B = 4.

Therefore, the required integral is given by

$$\begin{aligned} \text{I} &= \int \left\{ \frac{3}{y-2} + \frac{4}{(y-2)^2} \right\} dy = 3 \int \frac{dy}{y-2} + 4 \int \frac{dy}{(y-2)^2} \\ &= 3 \log|\text{y} - 2| + 4 \left( -\frac{1}{y-2} \right) + C \\ &= 3 \log|\sin\phi - 2| + \frac{4}{2 - \sin\phi} + C \\ &= 3 \log|2 - \sin\phi| + \frac{4}{2 - \sin\phi} + C \text{ (since, } 2 - \sin\phi \text{ is always positive)} \end{aligned}$$

**Example 16** Find 2 2 1 ( 2) ( 1) *x x dx x x* + + + + ∫

**Solution** The integrand is a proper rational function. Decompose the rational function into partial fraction [Table 2.2(5)]. Write

$$\frac{\mathbf{x}^2 + \mathbf{x} + 1}{\left(\mathbf{x}^2 + 1\right)\left(\mathbf{x} + 2\right)} = \frac{\mathbf{A}}{\mathbf{x} + 2} + \frac{\mathbf{B}\mathbf{x} + \mathbf{C}}{\left(\mathbf{x}^2 + 1\right)}$$
 Therefore, 
$$\mathbf{x}^2 + \mathbf{x} + 1 = \mathbf{A}\left(\mathbf{x}^2 + 1\right) + \left(\mathbf{B}\mathbf{x} + \mathbf{C}\right)\left(\mathbf{x} + 2\right)$$

Equating the coefficients of *x* 2 , *x* and of constant term of both sides, we get A + B =1, 2B + C = 1 and A + 2C = 1. Solving these equations, we get

$$\mathbf{A} = \frac{3}{5}, \mathbf{B} = \frac{2}{5} \text{ and } \mathbf{C} = \frac{1}{5}$$

Thus, the integrand is given by

$$\frac{\mathbf{x}^2 + \mathbf{x} + 1}{\left(\mathbf{x}^2 + 1\right)\left(\mathbf{x} + 2\right)} = \frac{3}{5\left(\mathbf{x} + 2\right)} + \frac{\frac{2}{5}\mathbf{x} + \frac{1}{5}}{\mathbf{x}^2 + 1} = \frac{3}{5\left(\mathbf{x} + 2\right)} + \frac{1}{5} \left(\frac{2\mathbf{x} + 1}{\mathbf{x}^2 + 1}\right)$$

$$\text{Therefore, } \quad \int \frac{\mathbf{x}^2 + \mathbf{x} + 1}{\left(\mathbf{x}^2 + 1\right)\left(\mathbf{x} + 2\right)} d\mathbf{x} = \frac{3}{5} \int \frac{d\mathbf{x}}{\mathbf{x} + 2} + \frac{1}{5} \int \frac{2\mathbf{x}}{\mathbf{x}^2 + 1} d\mathbf{x} + \frac{1}{5} \int \frac{1}{\mathbf{x}^2 + 1} d\mathbf{x}$$

$$= \frac{3}{5} \log \left|\mathbf{x} + 2\right| + \frac{1}{5} \log \left|\mathbf{x}^2 + 1\right| + \frac{1}{5} \tan^{-1} \mathbf{x} + \mathbf{C}$$

### **EXERCISE 7.5**

Integrate the rational functions in Exercises 1 to 21.

- **1.** ( 1) ( 2) *x x x* + + **2.** <sup>2</sup> 1 *x –* 9 **3.** 3 1 ( 1) ( 2) ( 3) *x – x – x – x –* **4.** ( 1) ( 2) ( 3) *x x – x – x –* **5.** <sup>2</sup> 2 3 2 *x x x* + + **6.** 2 1 (1 2 ) *– x x – x* **7.** <sup>2</sup> ( 1) ( – 1) *x x x* + **8.** <sup>2</sup> ( 1) ( 2) *x x – x* + **9.** 3 2 3 5 1 *x x – x x* + − + **10.** <sup>2</sup> 2 3 ( 1) (2 3) *x x – x* − + **11.** <sup>2</sup> 5 ( 1) ( 4) *x x x* + − **12.** 3 2 1 1 *x x x* + + − **13.** <sup>2</sup> 2 (1 ) (1 ) − + *x x* **14.** <sup>2</sup> 3 1 ( 2) *x – x* + **15.** <sup>4</sup> 1 *x* −1 **16.** 1 ( 1) *<sup>n</sup> x x* + [Hint: multiply numerator and denominator by *x <sup>n</sup>* – 1 and put *x*
- **17.** cos (1 – sin ) (2 – sin ) *x x x* [Hint : Put sin *x* = *t*]

*n* = *t* ]

$$\begin{array}{llll} \text{18.} & \frac{\left(\alpha^{2}+1\right)\left(\alpha^{2}+2\right)}{\left(\alpha^{2}+3\right)\left(\alpha^{2}+4\right)} & \text{19.} & \frac{2\chi}{\left(\alpha^{2}+1\right)\left(\alpha^{2}+3\right)} & \text{20.} & \frac{1}{\text{x}\left(\alpha^{4}-1\right)}\\ \cdot & \cdot & & &\\ \text{21.} & \frac{1}{\left(e^{x}-1\right)} \left[\text{Hint}\mathrel{\mathop{:}}{\text{Put}}\,e^{x}=t\right] \end{array}$$

Choose the correct answer in each of the Exercises 22 and 23.

$$\begin{aligned} \text{(22. } \int \frac{x \, dx}{(x-1)(x-2)} \text{ equals} \\ \text{(A)} \quad \log \left| \frac{(x-1)^2}{x-2} \right| + \text{C} & \qquad \text{(B)} \quad \log \left| \frac{(x-2)^2}{x-1} \right| + \text{C} \\ \text{(C)} \quad \log \left| \left( \frac{x-1}{x-2} \right)^2 \right| + \text{C} & \qquad \text{(D)} \quad \log \left| \left( x-1\right)\left(x-2\right) \right| + \text{C} \\ \text{(23. } \int \frac{dx}{x\left(x^2+1\right)} \text{ equals} \\ \text{(A)} \quad \log \left| x \right| - \frac{1}{2} \log \left( x^2 + 1 \right) + \text{C} & \qquad \text{(B)} \quad \log \left| x \right| + \frac{1}{2} \log \left( x^2 + 1 \right) + \text{C} \\ \text{(C)} \quad -\log \left| x \right| + \frac{1}{2} \log \left( x^2 + 1 \right) + \text{C} & \qquad \text{(D)} \quad \frac{1}{2} \log \left| x \right| + \log \left( x^2 + 1 \right) + \text{C} \end{aligned}$$

### **7.6 Integration by Parts**

In this section, we describe one more method of integration, that is found quite useful in integrating products of functions.

If *u* and *v* are any two differentiable functions of a single variable *x* (say). Then, by the product rule of differentiation, we have

$$\rho \frac{d}{d\mathbf{x}}(\mu \mathbf{v}) = \mu \frac{d\mathbf{v}}{d\mathbf{x}} + \nu \frac{d\mu}{d\mathbf{x}}$$

Integrating both sides, we get

$$\begin{aligned} \bigcup \mathcal{U} \end{aligned} \qquad \text{and} \qquad \begin{aligned} \bigcup \mathcal{U} \end{aligned} \qquad \text{and} \qquad \begin{aligned} \mathcal{U} &= \int u \frac{dv}{dx} \, dx + \int v \frac{du}{dx} \, dx \\ \int u \frac{dv}{dx} \, dx &= \mu v - \int v \frac{du}{dx} \, dx \\ \vdots \\ u &= f(\mathbf{x}) \text{ and } \frac{dv}{d\mathbf{x}} = \mathbf{g}(\mathbf{x}) \text{. Then} \end{aligned} \qquad \text{... (1)}$$

or

$$\frac{du}{d\boldsymbol{\chi}} = f'(\boldsymbol{\chi}) \text{ and } \boldsymbol{\nu} = \int \boldsymbol{g}(\boldsymbol{\chi}) \, d\boldsymbol{\chi}$$

Therefore, expression (1) can be rewritten as

$$
\int f(\mathbf{x}) \, \mathbf{g}(\mathbf{x}) \, d\mathbf{x} = \int f(\mathbf{x}) \int \mathbf{g}(\mathbf{x}) \, d\mathbf{x} - \int \left[ \int \mathbf{g}(\mathbf{x}) \, d\mathbf{x} \right] f'(\mathbf{x}) \, d\mathbf{x}
$$
 
$$
\text{i.e., } \qquad
\int f(\mathbf{x}) \, \mathbf{g}'(\mathbf{x}) \, d\mathbf{x} = \int f(\mathbf{x}) \int \mathbf{g}'(\mathbf{x}) \, d\mathbf{x} - \int \left[ f'(\mathbf{x}) \int \mathbf{g}(\mathbf{x}) \, d\mathbf{x} \right] d\mathbf{x}
$$

If we take *f* as the first function and *g* as the second function, then this formula may be stated as follows:

**"The integral of the product of two functions = (first function) × (integral of the second function) – Integral of [(differential coefficient of the first function)** *×* **(integral of the second function)]"**

$$\text{Example 17 Find } \int x \cos x \, dx$$

**Solution** Put *f* (*x*) = *x* (first function) and *g* (*x*) = cos *x* (second function).

Then, integration by parts gives

$$\int \mathbf{x} \cos \mathbf{x} \, d\mathbf{x} = \int \mathbf{\dot{\phi}} \cos \mathbf{x} \, d\mathbf{x} - \int \mathbf{\dot{l}} \frac{d}{d\mathbf{x}} (\mathbf{x}) \int \mathbf{\dot{\phi}} \cos \mathbf{x} \, d\mathbf{x} \, d\mathbf{x}$$

$$\stackrel{\circ}{=} \stackrel{\circ}{x} \sin^{\times} x - \int \sin^{\times} x \, dx \stackrel{\circ}{=} x \sin x + \cos x + C$$

Suppose, we take *f*(*x*) = cos *x* and *g*(*x*) = *x*. Then

$$\int \mathbf{x} \cos x \, dx = \cos x \int \mathbf{x} \, dx - \int \left[ \frac{d}{dx} (\cos x) \int \mathbf{x} \, dx \right] dx$$

$$\int \sqrt{\cos x} \, dx = \left( \cos x \right) \frac{x^2}{2} + \int \sin x \, \frac{x^2}{2} \, dx$$

Thus, it shows that the integral *x x dx* cos ∫ is reduced to the comparatively more complicated integral having more power of *x*. Therefore, the proper choice of the first function and the second function is significant.

### *Remarks*

- (i) It is worth mentioning that integration by parts is not applicable to product of functions in all cases. For instance, the method does not work for *x x dx* sin ∫ . The reason is that there does not exist any function whose derivative is *x* sin *x*.
- (ii) Observe that while finding the integral of the second function, we did not add any constant of integration. If we write the integral of the second function cos *x*

as sin *x* + *k*, where *k* is any constant, then

$$\begin{aligned} \int \mathbf{x} \cos \mathbf{x} \, d\mathbf{x} &= \mathbf{x} \left( \sin \mathbf{x} + k \right) - \int (\sin \mathbf{x} + k) \, d\mathbf{x} \\ &= \mathbf{x} \left( \sin \mathbf{x} + k \right) - \int (\sin \mathbf{x} \, d\mathbf{x} - \int k \, d\mathbf{x} \\ &= \mathbf{x} \left( \sin \mathbf{x} + k \right) - \cos \mathbf{x} - k \mathbf{x} + \mathbf{C} = \stackrel{\circ}{\mathbf{x}} \sin \mathbf{x} + \cos \mathbf{x} + \mathbf{C} \end{aligned}$$

This shows that adding a constant to the integral of the second function is superfluous so far as the final result is concerned while applying the method of integration by parts.

(iii) Usually, if any function is a power of *x* or a polynomial in *x*, then we take it as the first function. However, in cases where other function is inverse trigonometric function or logarithmic function, then we take them as first function.

**Example 18** Find log *x dx* ∫

**Solution** To start with, we are unable to guess a function whose derivative is log *x*. We take log *x* as the first function and the constant function 1 as the second function. Then, the integral of the second function is *x*.

$$\begin{aligned} \text{Hence,} \\ &= \int (\log x.1) \, dx = \log \mu \int 1 \, dx - \int \frac{d}{dx} (\log x) \int 1 \, dx \, dx \\ &= (\log \mu) \cdot x - \int \frac{1}{x} \ge dx = \infty \log x - x + C \dots \end{aligned}$$

**Example 19** Find *<sup>x</sup> x e dx* ∫

**Solution** Take first function as *x* and second function as *e x* . The integral of the second function is *e x* .

$$\text{Therefore, } \qquad \lor \begin{cases} \int \chi e^{x} dx = \chi e^{x} - \int 1 \cdot e^{x} dx = \chi e^{x} - e^{x} + C. \end{cases}$$

$$\text{Example 20 Find } \int \frac{\alpha \sin^{-1} x}{\sqrt{1 - x^2}} \, dx$$

**Solution** Let first function be sin – 1*x* and second function be <sup>2</sup> 1 *x* − *x* .

First we find the integral of the second function, i.e., 2 1 *x dx* − *x* ∫

Put *t* =1 – *x* 2 . Then *dt* = – 2*x dx* .

#### 262 MATHEMATICS

$$\text{Therefore, } \qquad \int \frac{\mathbf{x} \, d\mathbf{x}}{\sqrt{1 - \mathbf{x}^2}} = -\frac{1}{2} \int \frac{dt}{\sqrt{t}} = -\sqrt{t} = -\sqrt{1 - \mathbf{x}^2}$$

Hence,

$$\begin{aligned} \int \frac{x \sin^{-1} x}{\sqrt{1 - x^2}} dx &= (\sin^{-1} x) \left( -\sqrt{1 - x^2} \right) - \int \frac{1}{\sqrt{1 - x^2}} \left( -\sqrt{1 - x^2} \right) dx \\ &= -\sqrt{1 - x^2} \sin^{-1} x + x + \mathbf{C} = x - \sqrt{1 - x^2} \sin^{-1} x + \mathbf{C} \end{aligned}$$

**Alternatively**, this integral can also be worked out by making substitution sin–1 *x* = θ and then integrating by parts.

**Example 21** Find sin *<sup>x</sup> e x dx* ∫

**Solution** Take *e <sup>x</sup>* as the first function and sin *x* as second function. Then, integrating by parts, we have

$$\begin{aligned} \mathbf{I} &= \int e^{x} \sin x \, dx = e^{x} (-\cos x) + \int e^{x} \cos x \, dx \\ &= -e^{x} \cos x + \mathbf{I}\_{\text{1}} \text{ (say)} \end{aligned} \tag{1}$$

Taking *e <sup>x</sup>* and cos *x* as the first and second functions, respectively, in I<sup>1</sup> , we get

$$\mathbf{I}\_1 = \ e^{\mathbf{x}} \sin \mathbf{x} - \int e^{\mathbf{x}} \sin \mathbf{x} \, d\mathbf{x}$$

Substituting the value of I<sup>1</sup> in (1), we get

$$\mathbf{I} = -\,e^x \cos x + e^x \sin x - \mathbf{I} \text{ or } \,2\mathbf{I} = e^x \left(\sin x - \cos x\right)\mathbf{I}$$

$$\text{Hence, } \qquad \mathbf{I} = \int e^{\mathbf{x}} \sin \chi \, d\mathbf{x} = \frac{\mathbf{e}^{\mathbf{x}}}{2} (\sin \chi - \cos \chi) + \mathbf{C}$$

**Alternatively**, above integral can also be determined by taking sin *x* as the first function and *e x* the second function.

**7.6.1** *Integral of the type* [ ( ) + ( )] *<sup>x</sup> e f x f x dx* ′ ∫

$$\begin{aligned} \text{We have } \begin{aligned} \text{We have } \begin{aligned} \text{(a)} \end{aligned} \end{aligned} \begin{aligned} \text{(b)} \begin{aligned} \text{(c)} \begin{aligned} \text{(c)} \end{aligned} \end{aligned} \begin{aligned} \text{(c)} \begin{aligned} \text{(d)} \begin{aligned} \text{(e)} \end{aligned} \end{aligned} \begin{aligned} \text{(e)} \begin{aligned} \text{(e)} \end{aligned} \begin{aligned} \text{(e)} \begin{aligned} \text{(e)} \end{aligned} \end{aligned} \begin{aligned} \text{(e)} \begin{aligned} \text{(e)} \end{aligned} \end{aligned} \begin{aligned} \text{(e)} \begin{aligned} \text{(e)} \end{aligned} \end{aligned} \end{aligned} \end{aligned} \begin{aligned} \text{(e)} \begin{aligned} \text{(e)} \begin{aligned} \text{(e)} \end{aligned} \end{aligned} \end{aligned} \end{aligned} \end{cases}$$

Taking *f*(*x*) and *e x* as the first function and second function, respectively, in I<sup>1</sup> and integrating it by parts, we have I<sup>1</sup> = *f* (*x*) *e <sup>x</sup>–* ( ) C *<sup>x</sup> f x e dx* ′ <sup>+</sup> ∫

Substituting I<sup>1</sup> in (1), we get

$$\mathbf{I} = \stackrel{\circ}{e}^x f'(\mathbf{x}) - \int f'(\mathbf{x}) \, e^x \, d\mathbf{x} + \int e^x \, f'(\mathbf{x}) \, d\mathbf{x} + \mathbf{C} \, = e^x f'(\mathbf{x}) + \mathbf{C} \, \mathbf{x}$$

$$\text{Thus, } \qquad \int e^x [f(x) + f'(x)] dx \stackrel{!}{=} e^x f(x) + \text{Cl}\_2$$

$$\text{Example 22 Find (i) } \int e^x (\tan^{-1} x + \frac{1}{1 + x^2}) \, dx \quad \text{(ii) } \int \frac{\left(x^2 + 1\right) e^x}{\left(x + 1\right)^2} \, dx$$

### **Solution**

$$\text{(i)}\quad \text{We have } \text{I} = \int e^{\mathbf{x}} (\tan^{-1} \mathbf{x} + \frac{1}{1 + \mathbf{x}^2}) \, d\mathbf{x}$$

$$\begin{aligned} \text{Consider } f(\mathbf{x}) &= \tan^{-1} \mathbf{x}, \text{ then } \boldsymbol{f}'(\mathbf{x}) = \frac{1}{1 + \mathbf{x}^2} \\ \text{Thus, the given integrand is of the form } \boldsymbol{e}^{\boldsymbol{x}} \left[ \boldsymbol{f}'(\mathbf{x}) + \boldsymbol{f}'(\mathbf{x}) \right]. \end{aligned}$$

$$\text{Therefore, } \operatorname{I} = \int e^{x} (\tan^{-1} x + \frac{1}{1 + x^{2}}) \, dx = \, e^{x} \tan^{-1} x + \,\_{\diamondsuit} \mathbf{C}\_{(1)}$$

$$\text{(ii)}\quad\text{We have}\quad\text{I}=\int \frac{\left(\chi^2+1\right)e^x}{\left(\chi+1\right)^2}d\chi = \int e^x \left(\frac{\chi^2-1+1+1}{\left(\chi+1\right)^2}\right)d\chi$$

$$\frac{1}{\sqrt{2}} = \int e^{x^{\frac{1}{2}}} \frac{\left(\frac{x^{2}}{x+1}\right)^{2}}{\left(\left(x+1\right)^{2}\right)^{2}} + \frac{2}{\left(\left(x+1\right)^{2}\right)^{2}} \operatorname{l} \, d\boldsymbol{x} \stackrel{\operatorname{l}}{=} \left\{ e^{x} \operatorname{l} \, \frac{\left(x-1\right)}{\left(x+1\right)^{2}} + \frac{2}{\left(x+1\right)^{2}} \operatorname{l} \, d\boldsymbol{x} \right\}$$

Consider 1 ( ) 1 *x f x x* − = + , then <sup>2</sup> 2 ( ) ( 1) *f x x* ′ = +

Thus, the given integrand is of the form *e x* [*f* (*x*) + *f* ′(*x*)].

$$\text{Therefore, } \qquad \sqrt{\frac{\chi^2 + 1}{\left(\chi + 1\right)^2}} \ e^{x} \, d\chi = \frac{\chi - 1}{\chi + 1} e^{x} + C$$

### **EXERCISE 7.6**

Integrate the functions in Exercises 1 to 22.

**1.** *x* sin *x* **2.** *x* sin 3*x* **3.** *x* <sup>2</sup> *e <sup>x</sup>* **4.** *x* log *x* **5.** *x* log 2*x* **6.** *x* 2 log *x* **7.** *x* sin– 1*x* **8.** *x* tan–1 *x* **9.** *x* cos–1 *x* **10.** (sin–1*x*) <sup>2</sup> **11.** 1 2 cos 1 *x x x* − − **12.** *x* sec<sup>2</sup>*x* **13.** tan–1*x* **14.** *x* (log *x*) <sup>2</sup> **15.** (*x* 2 + 1) log *x*

$$\begin{array}{cccc} \text{16.} & e^x \left(\sin x + \cos x\right) & \text{17.} & \frac{\times e^x}{\left(1+x\right)^2} & \text{18.} & e^x \left(\frac{1+\sin x}{1+\cos x}\right) \\\\ \text{19.} & e^x \left(\frac{1}{x} - \frac{1}{x^2}\right) & \text{20.} & \frac{\left(\alpha-3\right)e^x}{\left(x-1\right)^3} & \text{21.} & e^{2x}\sin x \\\\ \text{22.} & \sin^{-1}\left(\frac{2x}{1+x^2}\right) & & \\\\ \text{Choose the correct answer in Exercises 23 and 24.} & & \end{array}$$

$$\begin{aligned} \text{(2.3. } \int x^2 e^{x^5} dx \text{ equals} \\ \text{(A) } \frac{1}{3} e^{x^5} + \text{C} & \qquad \text{(B) } \frac{1}{3} e^{x^5} + \text{C} \\ \text{(C) } \frac{1}{2} e^{x^5} + \text{C} & \qquad \text{(D) } \frac{1}{2} e^{x^5} + \text{C} \\ \text{(2.4. } \int e^x \sec x \,(\text{l} + \tan x) \, dx \text{ equals} \\ \text{(A) } e^x \cos x + \text{C} & \qquad \text{(B) } e^x \sec x + \text{C} \\ \text{(C) } \ e^x \sin x + \text{C} & \qquad \text{(D) } e^x \tan x + \text{C} \end{aligned}$$

### **7.6.2** *Integrals of some more types*

Here, we discuss some special types of standard integrals based on the technique of integration by parts :

$$\begin{array}{llll} \text{(i)} & \int \sqrt{\mathbf{x}^2 - a^2} \ \mathrm{d}x & \text{(ii)} & \int \sqrt{\mathbf{x}^2 + a^2} \ \mathrm{d}x & \text{(iii)} & \int \sqrt{a^2 - \mathbf{x}^2} \ \mathrm{d}x \\\\ \text{(i)} & \text{Let } \mathrm{I} = \int \sqrt{\mathbf{x}^2 - a^2} \ \mathrm{d}x & & \\ \end{array}$$

Taking constant function 1 as the second function and integrating by parts, we have

$$\begin{split} \mathcal{I} &= \, \text{x} \, \sqrt{\mathbf{x}^2 - a^2}^2 - \int \frac{1}{2} \frac{2\boldsymbol{\chi}}{\sqrt{\mathbf{x}^2 - a^2}} \, \text{x} \, d\boldsymbol{\chi} \\ &= \, \text{x} \, \sqrt{\mathbf{x}^2 - a^2}^2 - \int \frac{\mathbf{x}^2}{\sqrt{\mathbf{x}^2 - a^2}} \, d\boldsymbol{\chi} = \, \text{x} \, \sqrt{\mathbf{x}^2 - a^2}^2 - \int \frac{\mathbf{x}^2 - a^2 + a^2}{\sqrt{\mathbf{x}^2 - a^2}} \, d\boldsymbol{\chi} \end{split}$$

$$=\left(\mathbf{x}\sqrt{\mathbf{x}^2 - a^2} - \int \sqrt{\mathbf{x}^2 - a^2}\,d\mathbf{x} - a^2\right)\frac{d\mathbf{x}}{\sqrt{\mathbf{x}^2 - a^2}}$$

$$=\left(\mathbf{x}\sqrt{\mathbf{x}^2 - a^2} - \mathbf{I} - a^2\right)\frac{d\mathbf{x}}{\sqrt{\mathbf{x}^2 - a^2}}$$

$$=\frac{1}{\sqrt{\mathbf{x}^2 - a^2}}$$

$$\text{or} \qquad \qquad 2\text{I} = \propto \sqrt{\alpha^2 - a^2} - a^2 \int \frac{d\mathbf{x}}{\sqrt{\mathbf{x}^2 - a^2}}$$

or **I =** ∫ **2 2** *x – a dx* **= 2 2 2 2 2 – – log + – + C 2 2** *x a x a x x a*

Similarly, integrating other two integrals by parts, taking constant function 1 as the second function, we get

$$\text{(ii)}\quad\int\sqrt{\mathbf{x}^2 + a^2} \,d\mathbf{x} = \frac{1}{2} \ge \sqrt{\mathbf{x}^2 + a^2}^2 + \frac{a^2}{2}\log\left|\mathbf{x} + \sqrt{\mathbf{x}^2 + a^2}^2\right| + \text{(C.c.)}$$

$$(\text{iii)}\quad\int\sqrt{a^2-x^2}\,d\mathbf{x} = \frac{1}{2}\,\text{x}\,\sqrt{a^2-x^2}\,+\frac{a^2}{2}\,\text{sin}^{-1}\frac{\mathbf{x}}{a}+\mathbf{C}$$

**Alternatively**, integrals (i), (ii) and (iii) can also be found by making trigonometric substitution *x* = *a* secθ in (i), *x* = *a* tanθ in (ii) and *x* = *a* sinθ in (iii) respectively.

**Example 23** Find <sup>2</sup> *x x dx* + + 2 5 ∫

**Solution** Note that

$$\begin{aligned} \int \sqrt{x^2 + 2x + 5} \, dx &= \int \sqrt{(x+1)^2 + 4} \, dx \\ \text{Put } x + 1 &= \text{y, so that } dx = dy. \text{ Then} \\ \int \sqrt{x^2 + 2x + 5} \, dx &= \left\lceil \sqrt{y^2 + 2^2} \, dy \right\rceil \\ &= \frac{1}{2} \left\| y \sqrt{y^2 + 4} \right\| + \frac{4}{2} \log \left| y + \sqrt{y^2 + 4} \right| + C \qquad \text{[using 7.6.2 (ii)]} \\ &= \frac{1}{2} (x + 1) \sqrt{x^2 + 2x + 5} + 2 \log \left| x + 1 + \sqrt{x^2 + 2x + 5} \right| + C \\ \text{Example 24 Find } \int \sqrt{3 - 2x - x^2} \, dx \\ \text{Solution Note that } \int \sqrt{3 - 2x - x^2} \, dx &= \int \sqrt{4 - \left(x + 1\right)^2} \, dx \end{aligned}$$

$$\begin{aligned} \text{Put } x+1 &= \text{y so that } dx = dy. \\ \text{Thus } & \int \sqrt{3-2x-x^2} \, dx = \int \sqrt{4-y^2} \, dy \\ &= \frac{1}{2} \text{ y } \sqrt{4-y^2} + \frac{4}{2} \sin^{-1} \frac{y}{2} + \text{C} \qquad \text{[using 7.6.2 (iii)]} \\ &= \frac{1}{2} \left( \text{x}+1 \right) \sqrt{3-2x-x^2} + 2 \sin^{-1} \left( \frac{\text{x}+1}{2} \right) + \text{C} \\\\ \text{EXERCISE 7.7} \end{aligned}$$

Integrate the functions in Exercises 1 to 9.

**1.** <sup>2</sup> 4 − *x* **2.** <sup>2</sup> 1 4 − *x* **3.** <sup>2</sup> *x x* + + 4 6 **4.** <sup>2</sup> *x x* + + 4 1 **5.** <sup>2</sup> 1 4 − −*x x* **6.** <sup>2</sup> *x x* + − 4 5 **7.** <sup>2</sup> 1 3 + −*x x* **8.** <sup>2</sup> *x x* + 3 **9.** 2 1 9 *x* +

Choose the correct answer in Exercises 10 to 11.

$$\begin{aligned} \text{10. } \quad & \int \sqrt{1+x^2} \ \, dx \text{ is equal to} \\ \text{(A) } \quad & \frac{x}{2}\sqrt{1+x^2} + \frac{1}{2}\log\left| \left(x+\sqrt{1+x^2}\right) \right| + \text{C} \\ \text{(B) } \quad & \frac{2}{3}(1+x^2)^{\frac{3}{2}} + \text{C} \\ \text{(D) } \quad & \frac{x^2}{2}\sqrt{1+x^2} + \frac{1}{2}x^2\log\left| x+\sqrt{1+x^2} \right| + \text{C} \\ \text{(D) } \quad & \frac{x^2}{2}\sqrt{1+x^2} + \frac{1}{2}x^2\log\left| x+\sqrt{1+x^2} \right| + \text{C} \\ \text{(A) } \quad & \frac{1}{2}(x+4)\sqrt{x^2-8x+7}+9\log\left| x-4+\sqrt{x^2-8x+7} \right| + \text{C} \\ \text{(B) } \quad & \frac{1}{2}(x+4)\sqrt{x^2-8x+7}+9\log\left| x+4+\sqrt{x^2-8x+7} \right| + \text{C} \\ \text{(C) } \quad & \frac{1}{2}(x-4)\sqrt{x^2-8x+7}-3\sqrt{2}\log\left| x-4+\sqrt{x^2-8x+7} \right| + \text{C} \\ \text{(D) } \quad & \frac{1}{2}(x-4)\sqrt{x^2-8x+7}-\frac{9}{2}\log\left| x-4+\sqrt{x^2-8x+7} \right| + \text{C} \end{aligned}$$

## **7.7 Definite Integral**

In the previous sections, we have studied about the indefinite integrals and discussed few methods of finding them including integrals of some special functions. In this section, we shall study what is called definite integral of a function. The definite integral

has a unique value. A definite integral is denoted by ( ) *b a f x dx* ∫ , where *a* is called the

lower limit of the integral and *b* is called the upper limit of the integral. The definite integral is introduced either as the limit of a sum or if it has an anti derivative F in the interval [*a*, *b*], then its value is the difference between the values of F at the end points, i.e., F*(b)* – F*(a)*.

### **7.8 Fundamental Theorem of Calculus**

### **7.8.1** *Area function*

We have defined ( ) *b a f x dx* ∫ as the area of

the region bounded by the curve *y* = *f*(*x*), the ordinates *x* = *a* and *x* = *b* and *x*-axis. Let *x*

be a given point in [*a*, *b*]. Then ( ) *x a f x dx* ∫

represents the area of the light shaded region in Fig 7.1 [Here it is assumed that *f*(*x*) > 0 for *x* ∈ [*a*, *b*], the assertion made below is equally true for other functions as well]. The area of this shaded region depends upon the value of *x*.

![](_page_42_Figure_11.jpeg)

In other words, the area of this shaded region is a function of *x*. We denote this function of *x* by A(*x*). We call the function A(*x*) as *Area function* and is given by

$$\mathbf{A}\left(\mathbf{x}\right) = \int\_{a}^{x} f(\mathbf{x}) \, d\mathbf{x} \tag{1}$$

Based on this definition, the two basic fundamental theorems have been given. However, we only state them as their proofs are beyond the scope of this text book.

### **7.8.2** *First fundamental theorem of integral calculus*

**Theorem 1** Let *f* be a continuous function on the closed interval [*a*, *b*] and let A (*x*) be the area function. Then **A**′**(***x***) =** *f* **(***x***),** for all *x* ∈ **[***a***,** *b***]**.

### **7.8.3** *Second fundamental theorem of integral calculus*

We state below an important theorem which enables us to evaluate definite integrals by making use of anti derivative.

**Theorem 2** Let *f* be continuous function defined on the closed interval [*a*, *b*] and F be

$$\text{Can antiderivative of } f. \text{ Then } \int\_{a}^{b} f(\mathbf{x}) \, d\mathbf{x} = \left[ \mathbf{F}(\mathbf{x}) \right]\_{a}^{b} = \mathbf{F}(b) - \mathbf{F}(a).$$

### *Remarks*

- (i) In words, the Theorem 2 tells us that ( ) *b a f x dx* ∫ = (value of the anti derivative F of *f* at the upper limit *b* – value of the same anti derivative at the lower limit *a*).
- (ii) This theorem is very useful, because it gives us a method of calculating the definite integral more easily, without calculating the limit of a sum.
- (iii) The crucial operation in evaluating a definite integral is that of finding a function whose derivative is equal to the integrand. This strengthens the relationship between differentiation and integration.
- (iv) In ( ) *b a f x dx* ∫ , the function *f* needs to be well defined and continuous in [*a*, *b*].

For instance, the consideration of definite integral 1 3 2 2 2 *x x dx* ( –1) ∫ <sup>−</sup> is erroneous

since the function *f* expressed by *f*(*x*) = 1 <sup>2</sup> <sup>2</sup> *x x*( –1) is not defined in a portion – 1 < *x* < 1 of the closed interval [– 2, 3].

**Steps for calculating** ( ) *b a f x dx* ∫ .

(i) Find the indefinite integral *f x dx* ( ) ∫ . Let this be F(*x*). There is no need to keep integration constant C because if we consider F(*x*) + C instead of F(*x*), we get

$$\int\_{a}^{b} f\left(\mathbf{x}\right)d\mathbf{x} = \left[\mathbf{F}\left(\mathbf{x}\right) + \mathbf{C}\right]\_{a}^{b} = \left[\mathbf{F}(b) + \mathbf{C}\right] - \left[\mathbf{F}(a) + \mathbf{C}\right] = \mathbf{F}(b) - \mathbf{F}(a)\,,$$

Thus, the arbitrary constant disappears in evaluating the value of the definite integral.

(ii) Evaluate F(*b*) – F(*a*) = [F ( )]*<sup>b</sup> a x* , which is the value of ( ) *b a f x dx* ∫ .

We now consider some examples

**Example 25** Evaluate the following integrals:

$$\begin{array}{ll} \text{(i)} \quad \int\_{-2}^{3} \mathbf{x}^{2} \, d\mathbf{x} & \text{(ii)} \quad \int\_{-4}^{9} \frac{\sqrt{x}}{(30 - x^{2})^{2}} \, dx \\\\ \text{(iii)} \quad \int\_{-1}^{2} \frac{\mathbf{x} \, d\mathbf{x}}{(\mathbf{x} + 1)(\mathbf{x} + 2)} & \text{(iv)} \quad \int\_{0}^{\frac{\pi}{4}} \sin^{3} 2t \cos 2t \, dt \end{array}$$

### **Solution**

(i) Let 3 2 2 <sup>I</sup> <sup>=</sup> *x dx* ∫ . Since 3 2 F ( ) 3 *x x dx x* = = ∫ ,

Therefore, by the second fundamental theorem, we get

$$\text{I} = \text{F} \,(\text{3}) - \text{F} \,(\text{2}) = \frac{27}{\text{3}} - \frac{8}{\text{3}} = \frac{19}{\text{3}}$$

(ii) Let 9 3 4 2 2 I (30 – ) *x dx x* = ∫ . We first find the anti derivative of the integrand.

$$\text{Put } 30 - x^2 = t. \text{ Then } -\frac{3}{2}\sqrt{x} \text{ } dx = dt \text{ or } \sqrt{x} \text{ } dx = -\frac{2}{3}dt$$

$$\text{Thus, } \int \frac{\sqrt{x}}{\left(30 - x^{\frac{3}{2}}\right)^2} dx = -\frac{2}{3}\int \frac{dt}{t^2} = \frac{2}{3}\left[\frac{1}{t}\right] = \frac{2}{3}\left[\frac{1}{\left(30 - x^{\frac{3}{2}}\right)}\right] = \text{F}\left(x\right)$$

Therefore, by the second fundamental theorem of calculus, we have

$$\mathbf{I} = \mathbf{F}(9) - \mathbf{F}(4) = \frac{2}{3} \left[ \frac{1}{\left(30 - \alpha^{\frac{3}{2}}\right)} \right]\_{4}^{9}$$

$$= \frac{2}{3} \left[ \frac{1}{\left(30 - 27\right)} - \frac{1}{30 - 8} \right] = \frac{2}{3} \left[ \frac{1}{3} - \frac{1}{22} \right] = \frac{19}{99}$$

$$\text{(iii)} \quad \text{Let } \operatorname{I} = \int\_{-1}^{2} \frac{\mathbf{x} \, d\mathbf{x}}{\left(\mathbf{x} + \mathbf{l}\right) \left(\mathbf{x} + \mathbf{2}\right)}$$

#### 270 MATHEMATICS

Using partial fraction, we get –1 2 ( 1) ( 2) 1 2 *x x x x x* = + + + + +

$$\text{So } \qquad \int \frac{\mathbf{x} \, d\mathbf{x}}{\left(\mathbf{x} + \mathbf{l}\right) \left(\mathbf{x} + 2\right)} = \left\lceil -\log \left| \begin{array}{c} \mathbf{x} + 1 \\ \end{array} \right| + 2\log \left| \begin{array}{c} \mathbf{x} + 2 \\ \end{array} \right| = \mathbf{F}(\mathbf{x}).$$

Therefore, by the second fundamental theorem of calculus, we have I = F(2) – F(1) = [– log 3 + 2 log 4] – [– log 2 + 2 log 3] = – 3 log 3 + log 2 + 2 log 4 = <sup>32</sup> log 27 

(iv) Let <sup>4</sup> <sup>3</sup> 0 I sin 2 cos 2 *t t dt* π = ∫ . Consider <sup>3</sup> sin 2 cos 2 ∫ *t t dt*

Put sin 2*t* = *u* so that 2 cos 2*t dt* = *du* or cos 2*t dt* = 1 2  *du*

$$\text{So }\qquad \int \sin^3 2t \cos 2t \, dt \equiv \frac{1}{2} \int \mu^3 \, d\mu.$$

$$\mathbf{f} = \frac{1}{8} \left[ \mu^4 \mathbf{l} \right] = \frac{1}{8} \sin^4 2t = \mathbf{F} \,(t) \text{ say}$$

Therefore, by the second fundamental theorem of integral calculus

$$\mathbf{I} = \mathbf{F} \left( \frac{\pi}{4} \right) - \mathbf{F} \left( 0 \right) = \frac{1}{8} \left[ \sin^{4} \frac{\pi}{2} - \sin^{4} 0 \right] = \frac{1}{8}$$

$$\sqrt{\left( \dots \right)} \frac{\sqrt{\left( \dots \right)} \frac{1}{\pi \mathbf{v} \mathbf{u} \mathbf{n} \mathbf{v} \mathbf{e} \mathbf{e} \mathbf{e} \mathbf{u}}}$$

**EXERCISE 7.8**

Evaluate the definite integrals in Exercises 1 to 20.

$$\begin{array}{llll} \text{1.} & \int\_{-1}^{1} (\mathbf{x} + \mathbf{1}) \, d\mathbf{x} & \text{2.} & \int\_{-2}^{3} \frac{1}{\pi} \, d\mathbf{x} & \text{3.} & \int\_{-1}^{2} (4\mathbf{x}^{3} - 5\mathbf{x}^{2} + 6\mathbf{x} + 9) \, d\mathbf{x} \\\\ \text{4.} & \int\_{0}^{\frac{\pi}{4}} \sin 2\mathbf{x} \, d\mathbf{x} & \text{5.} & \int\_{0}^{\frac{\pi}{2}} \cos 2\mathbf{x} \, d\mathbf{x} & \text{6.} & \int\_{-4}^{\frac{\pi}{4}} e^{\mathbf{x}} \, d\mathbf{x} & \text{7.} & \int\_{0}^{\frac{\pi}{4}} \tan \mathbf{x} \, d\mathbf{x} \\\\ \text{8.} & \int\_{-\frac{\pi}{6}}^{\frac{\pi}{4}} \cos \mathbf{c} \, d\mathbf{x} & \text{9.} & \int\_{0}^{\frac{1}{\pi}} \frac{d\mathbf{x}}{\sqrt{1 - \mathbf{x}^{2}}} & \text{10.} & \int\_{0}^{\frac{1}{\pi}} \frac{d\mathbf{x}}{1 + \mathbf{x}^{2}} & \text{11.} & \int\_{-2}^{3} \frac{d\mathbf{x}}{\sqrt{x^{2} - 1}} \end{array}$$

$$\begin{array}{llll} \text{12.} & \int\_{0}^{\frac{\pi}{2}} \cos^{2} x \, dx & \text{13.} & \int\_{-2}^{3} \frac{\text{x} \, dx}{\text{x}^{2} + 1} & \text{14.} & \int\_{0}^{1} \frac{2\text{x} + 3}{5\text{x}^{2} + 1} \, dx & \text{15.} & \int\_{0}^{1} \text{x} \, e^{x^{2}} \, dx \\\\ \text{16.} & \int\_{1}^{2} \frac{5\text{x}^{2}}{\text{x}^{2} + 4\text{x} + 3} & \text{17.} & \int\_{0}^{\frac{\pi}{4}} (2\sec^{2}{x} \, + \text{x}^{3} + 2) \, dx & \text{18.} & \int\_{0}^{\pi} (\sin^{2}{\frac{x}{2}} - \cos^{2}{\frac{x}{2}}) \, dx \\\\ \end{array}$$

$$\mathbf{19.} \quad \int\_{0}^{2} \frac{6\boldsymbol{x} + 3}{\boldsymbol{\chi}^{2} + 4} d\boldsymbol{x} \qquad \mathbf{20.} \quad \int\_{0}^{1} (\boldsymbol{x} \, e^{\boldsymbol{x}} + \sin \frac{\pi \boldsymbol{x}}{4}) \, d\boldsymbol{x}$$

Choose the correct answer in Exercises 21 and 22.

![](_page_46_Figure_4.jpeg)

### **7.9 Evaluation of Definite Integrals by Substitution**

In the previous sections, we have discussed several methods for finding the indefinite integral. One of the important methods for finding the indefinite integral is the method of substitution.

To evaluate ( ) *b a f x dx* ∫ , by substitution, the steps could be as follows:

- 1. Consider the integral without limits and substitute, *y* = *f* (*x*) or *x* = *g*(*y*) to reduce the given integral to a known form.
- 2. Integrate the new integrand with respect to the new variable without mentioning the constant of integration.
- 3. Resubstitute for the new variable and write the answer in terms of the original variable.
- 4. Find the values of answers obtained in (3) at the given limits of integral and find the difference of the values at the upper and lower limits.

A**Note** In order to quicken this method, we can proceed as follows: After performing steps 1, and 2, there is no need of step 3. Here, the integral will be kept in the new variable itself, and the limits of the integral will accordingly be changed, so that we can perform the last step.

Let us illustrate this by examples.

$$\text{Example 26 Evaluate } \stackrel{\cdot}{\int\_{-1}^{1} \dots \int\_{-1}^{s}} \pi \lambda^4 \sqrt{x^8 + 1} \text{ d}\lambda.$$

**Solution** Put *t* = *x*<sup>5</sup> + 1, then *dt* = 5*x* <sup>4</sup> *dx*.

$$\text{Therefore, } \qquad \int 5x^4 \sqrt{x^8 + 1} \, dx = \int \sqrt{t} \, dt = \frac{2}{3}t^{\frac{3}{2}} = \frac{2}{3}(\alpha^8 + 1)^{\frac{3}{2}}$$

Hence,

$$\int\_{-1}^{1} \mathbf{5} \times^{4} \sqrt{\mathbf{x}^{\frac{\mathbf{s}}{\mathbf{s}}} + 1} \, d\mathbf{x} = \frac{2}{3} \left[ \left( \mathbf{x}^{\frac{\mathbf{s}}{\mathbf{s}}} + 1 \right)^{\frac{\mathbf{s}}{\mathbf{s}}} \right]\_{-1}^{1}$$

$$=\frac{2}{3}\left[\left(1^{\frac{\delta}{\epsilon}}+1\right)^{\frac{3}{2}}-\left(\left(-1\right)^{\frac{\delta}{\epsilon}}+1\right)^{\frac{3}{2}}\right]$$

$$=\frac{2}{3}\left[2^{\frac{3}{2}}-0^{\frac{3}{2}}\right]=\frac{2}{3}\left(2\sqrt{2}\right)=\frac{4\sqrt{2}}{3}$$

**Alternatively**, first we transform the integral and then evaluate the transformed integral with new limits.

$$\mathbf{Let}$$

$$\text{Let } \quad \qquad \qquad \qquad \lor \quad \lor \qquad \qquad t = \ge^{\mathfrak{s}} + 1. \text{ Then } dt = \mathfrak{s} \ge^{4} d\mathfrak{x}.$$

Note that, when *x* = – 1, *t* = 0 and when *x* = 1, *t* = 2 Thus, as *x* varies from – 1 to 1, *t* varies from 0 to 2

$$\begin{aligned} \text{Therefore} \quad \int\_{-1}^{1} 5x^4 \sqrt{x^3 + 1} \, dx &= \int\_{0}^{2} \sqrt{t} \, dt \\ &= \frac{2}{3} \left[ t^{\frac{3}{2}} \right]\_{0}^{2} = \frac{2}{3} \left[ 2^{\frac{3}{2}} - 0^{\frac{3}{2}} \right] = \frac{2}{3} \left( 2\sqrt{2} \right) = \frac{4\sqrt{2}}{3} \end{aligned}$$

**Example 27** Evaluate – 1 <sup>1</sup> 2 0 tan 1 *x dx* + *x* ∫

**Solution** Let *t* = tan – 1*x*, then <sup>2</sup> 1 1 *dt dx x* = + . The new limits are, when *x* = 0, *t* = 0 and when *x* = 1, 4 *t* π = . Thus, as *x* varies from 0 to 1, *t* varies from 0 to 4 π . Therefore –1 <sup>1</sup> 2 0 tan 1 *x dx* + *x* ∫ = 2 4 4 0 0 2 *t t dt* π π <sup>∫</sup> = 2 2 1 – 0 2 16 32 π π <sup>=</sup> 

# **EXERCISE 7.9**

Evaluate the integrals in Exercises 1 to 8 using substitution.

**1.** 1 <sup>2</sup> <sup>0</sup> 1 *x dx x* + ∫ **2.** <sup>2</sup> <sup>5</sup> 0 sin cos *d* π φ φ φ ∫ **3.** 1 – 1 2 0 2 sin 1 *x dx x* <sup>+</sup> ∫ **4.** 2 0 *x x* <sup>+</sup> <sup>2</sup> ∫ (Put *x* + 2 = *<sup>t</sup>* 2 ) **5.** <sup>2</sup> 2 0 sin 1 cos *x dx x* π + ∫ **6.** 2 <sup>2</sup> <sup>0</sup> 4 – *dx x x* + ∫ **7.** 1 <sup>2</sup> <sup>1</sup> 2 5 *dx x x* <sup>−</sup> + + ∫ **8.** 2 2 2 1 1 1 – 2 *x e dx x x* <sup>∫</sup>

Choose the correct answer in Exercises 9 and 10.

**9.** The value of the integral 1 <sup>3</sup> <sup>3</sup> <sup>1</sup> 1 4 3 ( ) *x x dx x* − ∫ is (A) 6 (B) 0 (C) 3 (D) 4 **10.** If *f*(*x*) = 0 sin *x t t dt* ∫ , then *f* ′(*x*) is (A) cos*x* + *x* sin *x* (B) *x* sin*x* (C) *x* cos*x* (D) sin*x* + *x* cos*x*

### **7.10 Some Properties of Definite Integrals**

We list below some important properties of definite integrals. These will be useful in evaluating the definite integrals more easily.

$$\begin{aligned} \mathbf{P\_0} & \quad \int\_a^b f(\mathbf{x}) \, d\mathbf{x} = \int\_a^b f(t) \, dt \\ \mathbf{P\_1} & \quad \int\_a^b f(\mathbf{x}) \, d\mathbf{x} = -\int\_b^a f(\mathbf{x}) \, d\mathbf{x} \text{ . In particular,} \int\_a^b f(\mathbf{x}) \, d\mathbf{x} = 0 \\ \mathbf{P\_2} & \quad \int\_a^b f(\mathbf{x}) \, d\mathbf{x} = \int\_a^c f(\mathbf{x}) \, d\mathbf{x} + \int\_c^b f(\mathbf{x}) \, d\mathbf{x} \end{aligned}$$

$$\begin{aligned} \mathbf{P}\_3: \quad \int\_a^b f(x) \, dx &= \int\_a^b f(a+b-x) \, dx \\ \mathbf{P}\_4: \quad \int\_0^a f(x) \, dx &= \int\_0^a f(a-x) \, dx \\ &\quad \text{(Note that } \mathbf{P}\_4 \text{ is a particular case of } \mathbf{P}\_3) \\ \mathbf{P}\_5: \quad \int\_0^{2a} f(x) \, dx &= \int\_0^a f(x) \, dx + \int\_0^a f(2a-x) \, dx \\ \mathbf{P}\_6: \quad \int\_0^{2a} f(x) \, dx &= 2 \int\_0^a f(x) \, dx; \text{ if } \, f(2a-x) = f(x) \quad \text{and} \\ &0 \text{ if } f(2a-x) = -f(x) \end{aligned}$$
 
$$\mathbf{P}\_7: \quad \text{(i) } \int\_{-a}^a f(x) \, dx = 2 \int\_0^a f(x) \, dx, \text{ if } f \text{ is an even function, i.e., if } f(-x) = f(x).$$
 
$$\text{(ii) } \int\_{-a}^a f(x) \, dx = 0, \text{ if } f \text{ is an odd function, i.e., if } f(-x) = -f(x).$$
  $\text{We give the proofs of these properties one by one.}$ 

**Proof of P<sup>0</sup>** It follows directly by making the substitution *x* = *t*.

**Proof of P<sup>1</sup>** Let F be anti derivative of *f*. Then, by the second fundamental theorem of calculus, we have ( ) F ( ) – F ( ) – [F ( ) F ( )] ( ) *b a a b f x dx b a a b f x dx* <sup>=</sup> = − = − ∫ ∫ Here, we observe that, if *a* = *b*, then ( ) 0 *a a f x dx* <sup>=</sup> ∫ .

**Proof of P<sup>2</sup>** Let F be anti derivative of *f*. Then

$$\int\_{a}^{b} f(x) \, d\mathbf{x} = \mathbf{F}(b) - \mathbf{F}(a) \tag{1}$$

$$\int\_{a}^{c} f(\mathbf{x}) \, d\mathbf{x} = \mathbf{F}(c) - \mathbf{F}(a) \tag{2}$$

$$\text{and} \qquad \bigvee\_{c \ge 1} \bigvee\_{c \ge 1} \bigvee\_{c=1}^{b} f(\mathbf{x}) \, d\mathbf{x} = \mathbf{F}(b) - \mathbf{F}(c) \, \tag{3}$$

Adding (2) and (3), we get ( ) ( ) F( ) – F( ) ( ) *c b b a c a f x dx f x dx b a f x dx* + = = ∫ ∫ ∫ This proves the property P<sup>2</sup> .

**Proof of P<sup>3</sup>** Let *t* = *a* + *b* – *x*. Then *dt* = – *dx*. When *x* = *a*, *t* = *b* and when *x* = *b*, *t* = *a*. Therefore

$$\int\_{a}^{b} f(\alpha) \, d\alpha = \text{---} \int\_{b}^{a} f(a+b-t) \, dt$$

$$=\int\_{-a}^{b} f\left(a+b-t\right)dt \text{ (by } \mathbf{P}\_{\downarrow})$$

$$=\int\_{-a}^{b} f\left(a+b-\mathbf{x}\right)d\mathbf{x} \text{ by } \mathbf{P}\_{\mathbf{0}}$$

**Proof of P<sup>4</sup>** Put *t* = *a* – *x*. Then *dt* = – *dx*. When *x* = 0, *t* = *a* and when *x* = *a*, *t* = 0. Now proceed as in P<sup>3</sup> .

\*\*Proof of  $\mathbf{P\_g}$ 
\*\*Using  $\mathbf{P\_2}$ , we have
 $\int\_0^{2a} f(\mathbf{x}) \, d\mathbf{x} = \int\_0^a f(\mathbf{x}) \, d\mathbf{x} + \int\_a^{2a} f(\mathbf{x}) \, d\mathbf{x} \dots$ 

Let *t =* 2*a – x* in the second integral on the right hand side. Then *dt* = – *dx*. When *x* = *a*, *t* = *a* and when *x* = 2*a*, *t* = 0. Also *x* = 2*a* – *t*.

Therefore, the second integral becomes

$$\int\_{a}^{2a} f(\mathbf{x}) \, d\mathbf{x} = \int\_{a}^{0} f(2a - t) \, dt = \int\_{0}^{a} f(2a - t) \, dt = \int\_{0}^{a} f(2a - \lambda) \, d\lambda$$

Hence

$$\int\_{0}^{2a} f(\mathbf{x}) \, d\mathbf{x} = \int\_{0}^{a} f(\mathbf{x}) \, d\mathbf{x} + \int\_{0}^{a} f(2a - \mathbf{x}) \, d\mathbf{x}$$

$$\textbf{Proof of } \textbf{P\_6} \text{ Using } \textbf{P\_5}, \text{ we have } \int\_0^{2a} f(\vec{x}) \, d\vec{x} = \int\_0^a f(\vec{x}) \, d\vec{x} + \int\_0^a f(2a - \textbf{x}) \, d\textbf{x} \qquad \dots \text{ (1)}$$

$$\text{Now, if } \newline \qquad \begin{array}{c} f(2a \\_ \newline \qquad \newline f(2a \\_ \\_ \\_) = f(\text{x}) \text{, then (1) becomes } \newline \qquad \end{array}$$

0

$$\int\_{0}^{2a} f(\mathbf{x}) \, d\mathbf{x} = \int\_{0}^{a} f(\mathbf{x}) \, d\mathbf{x} + \int\_{0}^{a} f(\mathbf{x}) \, d\mathbf{x} = 2 \int\_{0}^{a} f(\mathbf{x}) \, d\mathbf{x},$$
 and if 
$$\int\_{0}^{a} f(2a - \mathbf{x}) = -f(\mathbf{x}) \text{, then (1) becomes}$$
 
$$\int\_{0}^{2a} f(\mathbf{x}) \, d\mathbf{x} = \int\_{0}^{a} f(\mathbf{x}) \, d\mathbf{x} - \int\_{0}^{a} f(\mathbf{x}) \, d\mathbf{x} = 0$$

**Proof of P<sup>7</sup>** Using P<sup>2</sup> , we have

$$\int\_{-a}^{a} f(\alpha) \, d\alpha = \int\_{-a}^{0} f(\alpha) \, d\alpha + \int\_{0}^{a} f(\alpha) \, d\alpha \text{ . Then}$$

0 0

Let *t* = – *x* in the first integral on the right hand side. *dt* = – *dx*. When *x* = – *a*, *t* = *a* and when *x* = 0, *t* = 0. Also *x* = – *t*.

$$\begin{aligned} \text{Therefore} \\ &= \int\_{-a}^{a} f(\mathbf{x}) \, d\mathbf{x} = \frac{1}{- } \int\_{a}^{0} f(-t) \, dt + \int\_{0}^{a} f(\mathbf{x}) \, d\mathbf{x} \\ &= \int\_{0}^{a} f(-\mathbf{x}) \, d\mathbf{x} + \int\_{0}^{a} f(\mathbf{x}) \, d\mathbf{x} \qquad \text{(by } \mathbf{P}\_{0}\text{)}\dots \text{(1)} \end{aligned}$$

#### 276 MATHEMATICS

(i) Now, if *f* is an even function, then *f*(–*x*) = *f*(*x*) and so (1) becomes

$$\int\_{-a}^{a} f\left(\mathbf{x}\right)d\mathbf{x} = \int\_{0}^{a} f\left(\mathbf{x}\right)d\mathbf{x} + \int\_{0}^{a} f\left(\mathbf{x}\right)d\mathbf{x} = 2\int\_{0}^{a} f\left(\mathbf{x}\right)d\mathbf{x}$$

(ii) If *f* is an odd function, then *f*(–*x*) = – *f*(*x*) and so (1) becomes

$$\int\_{-a}^{a} f(\lambda) \, d\lambda = -\int\_{-0}^{a} f(\lambda) \, d\lambda + \int\_{0}^{a} f(\lambda) \, d\lambda = 0$$

**Example 28** Evaluate 2 3 1 *x x dx* – ∫ <sup>−</sup>

**Solution** We note that *x* 3 – *x* ≥ 0 on [– 1, 0] and *x* 3 – *x* ≤ 0 on [0, 1] and that *x* 3 – *x* ≥ 0 on [1, 2]. So by P<sup>2</sup> we write

2 3 1 *x x dx* – ∫ <sup>−</sup> = 0 1 2 3 3 3 1 0 1 ( – ) – ( – ) ( – ) *x x dx x x dx x x dx* − + + ∫ ∫ ∫ = 0 1 2 3 3 3 1 0 1 ( – ) ( – ) ( – ) *x x dx x x dx x x dx* − + + ∫ ∫ ∫ = 0 1 2 4 2 2 4 4 2 – 1 0 1 – – – 4 2 2 4 4 2 *x x x x x x* + + <sup>=</sup> ( ) 1 1 1 1 1 1 – – – 4 – 2 – – 4 2 2 4 4 2 + + = 1 1 1 1 1 1 – 2 4 2 2 4 4 2 + + − + − + = 3 3 11 <sup>2</sup> 2 4 4 − + = **Example 29** Evaluate <sup>4</sup> <sup>2</sup> – sin *x dx* π ∫ <sup>π</sup>

**Solution** We observe that sin<sup>2</sup> *x* is an even function. Therefore, by P<sup>7</sup> (i), we get

$$\begin{aligned} \int \frac{\frac{\pi}{4}}{\frac{-\pi}{4}} \sin^2 x \, dx &= \, 2 \int\_0^{\frac{\pi}{4}} \sin^2 x \, dx \\ &= \, 2 \int\_0^{\frac{\pi}{4}} \frac{(1 - \cos 2x)}{2} \, dx = \int\_0^{\frac{\pi}{4}} (1 - \cos 2x) \, dx \end{aligned}$$

4

$$= \left[ \left. x - \frac{1}{2} \sin 2x \right\}\_0^{\frac{\pi}{4}} = \left( \frac{\pi}{4} - \frac{1}{2} \sin \frac{\pi}{2} \right) - 0 = \frac{\pi}{4} - \frac{1}{2} \right]$$

**Example 30** Evaluate <sup>2</sup> <sup>0</sup> sin 1 cos *x x dx x* π + ∫

Solution Let I =  $\int\_{0}^{\pi} \frac{\chi \sin \chi}{1 + \cos^{2} \chi} \, d\chi$ . Then, by P\_{4}, we have

$$\mathrm{I} = \int\_{0}^{\pi} \frac{(\pi - \chi) \sin \left(\pi - \chi\right) \, d\chi}{1 + \cos^{2} \left(\pi - \chi\right)}$$

$$= \int\_{0}^{\pi} \frac{(\pi - \chi) \sin \chi \, d\chi}{1 + \cos^{2} \chi} = \pi \int\_{0}^{\pi} \frac{\sin \chi \, d\chi}{1 + \cos^{2} \chi} - \mathrm{I}$$

or

$$2 \text{ I = } \pi \int\_{0}^{\pi} \frac{\sin \chi \, d\chi}{1 + \cos^{2} \chi}$$

$$\begin{aligned} \text{or} \qquad \begin{aligned} \text{or} \qquad \end{aligned} \qquad \begin{aligned} \text{i)} \quad \text{i)} \quad & \overline{\text{I} + \cos^2 \text{x}} \\ \text{i)} \quad & \overline{\text{I} = \frac{\pi}{2} \int\_0^{\pi} \frac{\sin x \, dx}{1 + \cos^2 x} \end{aligned} \qquad \text{or} \qquad \begin{aligned} \text{i)} \quad & \overline{\text{I} + \cos^2 \text{x}} \\ \text{ii)} \quad & \overline{\text{I} + \cos^2 \text{x}} \end{aligned} $$

Put cos *x* = *t* so that – sin *x dx* = *dt*. When *x* = 0, *t* = 1 and when *x* = π, *t* = – 1. Therefore, (by P<sup>1</sup> ) we get

*x*

$$\begin{aligned} \mathbf{I} &= \frac{-\pi}{2} \int\_{-1}^{-1} \frac{dt}{1+t^2} = \frac{\pi}{2} \int\_{-1}^{1} \frac{dt}{1+t^2} \\ &= \pi \int\_{0}^{1} \frac{dt}{1+t^2} \quad \text{(by } \mathbf{P}\_{\gamma}, \text{ since } \frac{1}{1+t^2} \text{ is even function)} \\ &= \pi \left[ \tan^{-1} t \right]\_{0}^{1} = \pi \left[ \tan^{-1} 1 - \tan^{-1} 0 \right] = \pi \left[ \frac{\pi}{4} - 0 \right] = \frac{\pi^2}{4} \\ &\dots \end{aligned}$$

**Example 31** Evaluate 1 5 4 1 sin cos *x x dx* ∫<sup>−</sup>

**Solution** Let I = 1 5 4 1 sin cos *x x dx* − ∫ . Let *f*(*x*) = sin<sup>5</sup> *x* cos<sup>4</sup> *x*. Then

*f* (– *x*) = sin<sup>5</sup> (– *x*) cos<sup>4</sup> (– *x*) = – sin<sup>5</sup> *x* cos<sup>4</sup> *x* = – *f* (*x*), i.e., *f* is an odd function. Therefore, by P<sup>7</sup> (ii), I = 0

$$\text{Example 32 Evaluate } \int\_{-0}^{\frac{\pi}{2}} \frac{\sin^4 x}{\sin^4 x + \cos^4 x} \, dx$$

$$\text{Solution Let } \mathbf{I} = \int\_0^{\frac{\pi}{2}} \frac{\sin^4 x}{\sin^4 x + \cos^4 x} \, dx \tag{1}$$

Then, by P<sup>4</sup>

$$\mathbf{I} = \int\_0^{\frac{\pi}{2}} \frac{\sin^4(\frac{\pi}{2} - x)}{\sin^4(\frac{\pi}{2} - x) + \cos^4(\frac{\pi}{2} - x)} \, d\mathbf{x} = \int\_0^{\frac{\pi}{2}} \frac{\cos^4 x}{\cos^4 x + \sin^4 x} \, d\mathbf{x} \tag{21}$$

Adding (1) and (2), we get

$$\text{2I} = \int\_0^{\frac{\pi}{2}} \frac{\sin^4 x + \cos^4 x}{\sin^4 x + \cos^4 x} \, dx = \int\_0^{\frac{\pi}{2}} \, dx = \left[ \text{x} \right]\_0^{\frac{\pi}{2}} = \frac{\pi}{2}$$

Hence I =

$$\text{Example 33 Evaluate } \int \frac{\frac{\pi}{3}}{\frac{\pi}{6}} \frac{d\mathbf{x}}{1 + \sqrt{\tan x}}$$

4 π

6

$$\text{Solution} \quad \text{Let } \mathbf{I} = \int \frac{\frac{\pi}{3}}{\frac{\pi}{6}} \frac{\left(\frac{d\chi}{dx}\right)}{1 + \sqrt{\tan x}} = \int \frac{\frac{\pi}{3}}{\frac{\pi}{6}} \frac{\sqrt{\cos x}}{\sqrt{\cos x} + \sqrt{\sin x}} \qquad \qquad \qquad \qquad \qquad \dots \text{ (1)}$$

$$\begin{array}{ll} \text{Then, by } \mathbf{P}\_3 & \mathbf{I} = \int\_{-\frac{\pi}{6}}^{\frac{\pi}{3}} \sqrt{\cos\left(\frac{\pi}{3} + \frac{\pi}{6} - x\right)} \, dx \\ & & \times \int\_{-\frac{\pi}{6}}^{\frac{\pi}{3}} \sqrt{\cos\left(\frac{\pi}{3} + \frac{\pi}{6} - x\right)} + \sqrt{\sin\left(\frac{\pi}{3} + \frac{\pi}{6} - x\right)} \\ & & & \\ & & = \int\_{-\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{\sqrt{\sin x}}{\sqrt{\sin x} + \sqrt{\cos x}} \, dx & & & \dots \end{array}$$

Adding (1) and (2), we get

$$\text{2I} = \int\_{\frac{\pi}{6}}^{\frac{\pi}{3}} d\boldsymbol{x} = \left[\boldsymbol{x}\right]\_{\frac{\pi}{6}}^{\frac{\pi}{3}} = \frac{\pi}{3} - \frac{\pi}{6} = \frac{\pi}{6}\text{. Hence }\mathbf{I} = \frac{\pi}{12}$$

#### **Example 34** Evaluate <sup>2</sup> 0 log sin *x dx* π ∫

**Solution** Let I = 2 0 log sin *x dx* π ∫

Then, by P<sup>4</sup>

$$\mathbf{I} = \int\_0^{\frac{\pi}{2}} \log \sin \left(\frac{\pi}{2} - x\right) d\mathbf{x} = \int\_0^{\frac{\pi}{2}} \log \cos x \, d\mathbf{x}$$

Adding the two values of I, we get

$$\begin{aligned} \text{2I} &= \int\_0^{\frac{\pi}{2}} (\log \sin x + \log \cos x) \, dx \\ &= \int\_0^{\frac{\pi}{2}} (\log \sin x \cos x + \log 2 - \log 2) \, dx \text{ (by adding and subtracting } \log 2) \\ &= \int\_0^{\frac{\pi}{2}} \log \sin 2x \, dx - \int\_0^{\frac{\pi}{2}} \log 2 \, dx \quad \text{(Why?)} \end{aligned}$$

Put 2*x* = *t* in the first integral. Then 2 *dx* = *dt*, when *x* = 0, *t* = 0 and when 2 *x* π = , *t* = π.

Therefore 2I = 0 1 log sin log 2 2 2 *t dt* <sup>π</sup> π <sup>−</sup> ∫ = 2 0 2 log sin log 2 2 2 *t dt* π π <sup>−</sup> ∫ [by P<sup>6</sup> as sin (π – *t*) = sin *t*) = 2 0 log sin log 2 2 *x dx* π π <sup>−</sup> ∫ (by changing variable *t* to *x*) = I log 2 2 π − Hence <sup>2</sup> 0 log sin *x dx* π ∫ = – log 2 2 π .

### **EXERCISE 7.10**

By using the properties of definite integrals, evaluate the integrals in Exercises 1 to 19.

**1.** <sup>2</sup> <sup>2</sup> 0 cos *x dx* π ∫ **2.** <sup>2</sup> 0 sin sin cos *x dx x x* π + ∫ **3.** 3 2 2 3 3 0 2 2 sin sin cos *x dx x x* π + ∫ **4.** 5 2 5 5 0 cos sin cos *x dx x x* π + ∫ **5.** 5 5 | 2 | *x dx* − <sup>+</sup> ∫ **6.** 8 2 *x dx* <sup>−</sup> <sup>5</sup> ∫ **7.** 1 0 (1 )*<sup>n</sup> x x dx* <sup>−</sup> ∫ **8.** <sup>4</sup> 0 log (1 tan ) *x dx* π <sup>+</sup> ∫ **9.** 2 0 *x x dx* <sup>2</sup> <sup>−</sup> ∫ **10.** <sup>2</sup> 0 (2log sin log sin 2 ) *x x dx* π <sup>−</sup> ∫ **11.** <sup>22</sup> – 2 sin *x dx* π ∫ π **12.** <sup>0</sup> 1 sin *x dx x* π + ∫ **13.** <sup>72</sup> – 2 sin *x dx* π ∫ π **14.** 2 5 0 cos *x dx* π ∫ **15.** <sup>2</sup> 0 sin cos 1 sin cos *x x dx x x* π − + ∫ **16.** 0 log (1 cos ) *x dx* π <sup>+</sup> ∫ **17.** <sup>0</sup> *<sup>a</sup> x dx x a x* + − ∫ **18.** 4 0 *x dx* <sup>−</sup><sup>1</sup> ∫ **19.** Show that 0 0 ( ) ( ) 2 ( ) *a a f x g x dx f x dx* <sup>=</sup> ∫ ∫ , if *f* and *g* are defined as *f*(*x*) = *f*(*a* – *x*) and *g*(*x*) + *g*(*a* – *x*) = 4 Choose the correct answer in Exercises 20 and 21. **20.** The value of <sup>2</sup> <sup>3</sup> <sup>5</sup> 2 ( cos tan 1) *x x x x dx* π −π + + + ∫ is (A) 0 (B) 2 (C) π (D) 1 **21.** The value of <sup>2</sup> 0 4 3 sin log 4 3 cos *x dx x* π + <sup>+</sup> ∫ is

(A) 2 (B) 3 4 (C) 0 (D) –2

### *Miscellaneous Examples*

**Example 35** Find cos 6 1 sin 6 *x x dx* <sup>+</sup> ∫

**Solution** Put *t* = 1 + sin 6*x*, so that *dt* = 6 cos 6*x dx*

Therefore 1 2 1 cos 6 1 sin 6 6 *x x dx t dt* + = ∫ ∫ = 3 3 2 2 1 2 1 ( ) C = (1 sin 6 ) C 6 3 9 × + + + *t x* **Example 36** Find 1 4 4 5 ( ) *x x dx x* − ∫ **Solution** We have 1 1 4 4 4 3 5 4 1 (1 ) ( ) *x x <sup>x</sup> dx dx x x* − − <sup>=</sup> ∫ ∫ Put – 3 3 4 1 3 1 1 – , so t *x t dx dt* hat *x x* − = = = Therefore 1 4 1 4 4 5 ( ) 1 3 *x x dx t dt x* − <sup>=</sup> ∫ ∫<sup>=</sup> 5 5 4 4 3 1 4 4 1 C = 1 C 3 5 15 *t x* × + − + **Example 37** Find 4 2 ( 1) ( 1) *x dx x x* − + ∫ **Solution** We have 4 2 ( 1)( 1) *x x x* − + = 3 2 1 ( 1) 1 *x x x x* + + − + − = <sup>2</sup> 1 ( 1) ( 1) ( 1) *x x x* + + − + ... (1)

$$\text{Now express}\qquad\frac{1}{(\mathbf{x}-\mathbf{l})(\mathbf{x}^2+\mathbf{l})} = \frac{\mathbf{A}}{(\mathbf{x}-\mathbf{l})} + \frac{\mathbf{B}\mathbf{x}+\mathbf{C}}{(\mathbf{x}^2+\mathbf{l})}\tag{2}$$

#### 282 MATHEMATICS

$$\begin{aligned} \text{So} \\ &= (\mathbf{A} + \mathbf{B}) \times \mathbf{\hat{n}} + (\mathbf{B} \times \mathbf{\hat{n}}) + (\mathbf{B} \times \mathbf{\hat{n}}) \\ &= (\mathbf{A} + \mathbf{B}) \times \mathbf{\hat{n}} + (\mathbf{C} - \mathbf{B}) \times \mathbf{\hat{n}} + \mathbf{A} - \mathbf{C} \end{aligned}$$

Equating coefficients on both sides, we get A + B = 0, C – B = 0 and A – C = 1, which give 1 1 A , B C – = = = . Substituting values of A, B and C in (2), we get

$$\frac{1}{\left(\infty - 1\right)\left(\infty^2 + 1\right)} = \frac{1}{2\left(\infty - 1\right)} - \frac{1}{2} \frac{\infty}{\left(\infty^2 + 1\right)} - \frac{1}{2\left(\infty^2 + 1\right)} \qquad \qquad \dots \text{ (3)}$$

Again, substituting (3) in (1), we have

2 2

$$\frac{\mathbf{x}^4}{\left(\left(\mathbf{x}-\mathbf{l}\right)\left(\mathbf{x}^2+\mathbf{x}+\mathbf{l}\right)\right)} = \left(\mathbf{x}+\mathbf{l}\right) + \frac{1}{2\left(\mathbf{x}-\mathbf{l}\right)} - \frac{1}{2} \frac{\mathbf{x}}{\left(\mathbf{x}^2+\mathbf{l}\right)} - \frac{1}{2\left(\mathbf{x}^2+\mathbf{l}\right)}$$

Therefore

$$\int \frac{x^4}{\left(x-1\right)\left(x^2+x+1\right)}dx = \frac{x^2}{2} + x + \frac{1}{2}\log\left|\frac{x-1}{\left(x\right)\_{\infty}}\right| - \frac{1}{4}\log\left(x^2+1\right) - \frac{1}{2}\tan^{-1}x + C$$

$$\text{Example 38 Find } \int \left[ \log \left( \log x \right) + \frac{1}{\left( \log x \right)^{2}} \right] dx$$

$$\begin{aligned} \text{Solution } \text{Let } \operatorname{I} &= \int \left[ \log \left( \log x \right) + \frac{1}{\left( \log x \right)^2} \right] dx \\ &= \int \log \left( \log x \right) dx + \int \frac{1}{\left( \log x \right)^2} dx \end{aligned}$$

In the first integral, let us take 1 as the second function. Then integrating it by parts, we get

$$\begin{aligned} \mathbf{I} &= \ x \log \left( \log \lambda \right) - \int \frac{1}{\mathbf{x} \log \mathbf{x}} \times d\mathbf{x} + \int \frac{d\mathbf{x}}{\left( \log \mathbf{x} \right)^2} \\ &= \frac{1}{\mathbf{x}} \log \left( \log \mathbf{x} \right) - \int \frac{d\mathbf{x}}{\log \mathbf{x}} + \int \frac{d\mathbf{x}}{\left( \log \mathbf{x} \right)^2} \\ &\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\dots \text{(1)} \end{aligned}$$

Again, consider log *dx x* ∫ , take 1 as the second function and integrate it by parts,

$$\text{Use have } \int \frac{d\mathbf{x}}{\log x} = \left[ \frac{\mathbf{x}}{\log x} - \int \mathbf{x} \left\{ -\frac{1}{\left(\log x\right)^2} \left(\frac{1}{x}\right) \right\} d\mathbf{x} \right] \tag{2}$$

Putting (2) in (1), we get

$$\mathrm{I} = x \log \left( \log x \right) - \frac{x}{\log x} - \int \frac{d\mathbf{x}}{\left( \log \mathbf{x} \right)^2} + \int \frac{d\mathbf{x}}{\left( \log x \right)^2} = x \log \left( \log x \right) - \frac{x}{\log x} + C$$

**Example 39** Find cot tan *x x dx* + ∫ **Solution** We have

$$\mathbf{I} = \int \left[ \sqrt{\cot x} + \sqrt{\tan x} \right] dx = \int \sqrt{\tan x} (1 + \cot x) \, dx$$

Put tan *x* = *t* 2 , so that sec<sup>2</sup>*x dx* = 2*t dt*

$$\text{or} \qquad \qquad \qquad dx = \frac{2t \, dt}{1 + t^4}$$

$$\text{Then } \qquad \qquad \mathbf{I} = \int t \left( 1 + \frac{1}{t^2} \right) \frac{2t}{(1 + t^4)} \, dt$$

$$=2\int \frac{(t^2+1)}{t^4+1}dt = 2\int \frac{\left(1+\frac{1}{t^2}\right)dt}{\left(t^2+\frac{1}{t^2}\right)} = 2\int \frac{\left(1+\frac{1}{t^2}\right)dt}{\left(t-\frac{1}{t}\right)^2+2}$$

Put 1 *t t* − = *y*, so that <sup>2</sup> 1 1 *t* <sup>+</sup> *dt* = *dy*. Then

$$\mathbf{I} = 2 \oint \frac{\mathbf{dy}}{\mathbf{y}^2 + \left(\sqrt{2}\right)^2} = \sqrt{2} \tan^{-1} \frac{\mathbf{y}}{\sqrt{2}} + \mathbf{C} = \sqrt{2} \tan^{-1} \frac{\begin{pmatrix} t - 1 \\ t \end{pmatrix}}{\sqrt{2}} + \mathbf{C}$$

$$= \sqrt{2} \tan^{-1} \left(\frac{t^2 - 1}{\sqrt{2}}\right) + \mathbf{C} = \sqrt{2} \tan^{-1} \left(\frac{\tan x - 1}{\sqrt{2 \tan x}}\right) + \mathbf{C}$$

**Example 40** Find 4 sin 2 cos 2 9 – cos (2 ) *x x dx x* ∫ **Solution** Let 4 sin 2 cos 2 <sup>I</sup> 9 – cos 2 *x x dx x* = ∫

Put cos<sup>2</sup> (2*x*) = *t* so that 4 sin 2*x* cos 2*x dx* = – *dt*

Therefore –1 1 2 2 <sup>1</sup> <sup>1</sup> 1 1 I – – sin C sin cos 2 C 4 4 3 4 3 9 – *dt t x t* <sup>−</sup> <sup>=</sup> <sup>=</sup> + = − <sup>+</sup> ∫ 3

**Example 41** Evaluate 2 1 *x x dx* sin ( ) − <sup>π</sup> ∫

$$\text{Solution } \text{Here } f(\mathbf{x}) = \mathbb{I} \ge \sin \pi \mathbf{x} \text{ | } = \begin{cases} \ge \sin \pi \ge \text{for } -1 \le \mathbf{x} \le 1 \\\\ -\infty \sin \pi \ge \text{for } 1 \le \mathbf{x} \le \frac{3}{2} \end{cases}$$

Therefore 3 2 1 | sin | *x x dx* − <sup>π</sup> ∫ = 3 1 2 1 1 *x x dx x x dx* sin sin − π + − π ∫ ∫

$$\frac{1}{\pi} = \int\_{-1}^{1} \pi \sin \pi x \, dx - \int\_{-1}^{\frac{3}{2}} x \sin \pi x \, dx$$

Integrating both integrals on righthand side, we get

$$\int\_{-1}^{\frac{3}{2}} \|x\sin\pi x\| \, dx = \left[\frac{-x\cos\pi x}{\pi} + \frac{\sin\pi x}{\pi^2}\right]\_{-1}^{1} - \left[\frac{-x\cos\pi x}{\pi} + \frac{\sin\pi x}{\pi^2}\right]\_{1}^{\frac{3}{2}}$$

$$= \frac{2}{\pi} - \left[-\frac{1}{\pi^2} \frac{1}{\pi}\right] = \frac{3}{\pi} + \frac{1}{\pi^2}$$

**Example 42** Evaluate 2 2 2 2 <sup>0</sup> cos sin *x dx a x b x* π + ∫

> π π

∫

$$\text{Solution Let}\\
\text{I} = \int\_{0}^{\pi} \frac{\sqrt{x} \, dx}{a^2 \cos^2 x + b^2 \sin^2 x} = \int\_{0}^{\pi} \frac{(\pi - x) \, dx}{a^2 \cos^2(\pi - x) + b^2 \sin^2(\pi - x)} \quad \text{(using } \text{P}\_4\text{)}$$

$$\begin{aligned} &= \pi \int\_0^\pi \frac{dx}{a^2 \cos^2 x + b^2 \sin^2 x} - \int\_0^\pi \frac{x \, dx}{a^2 \cos^2 x + b^2 \sin^2 x} \\ &= \pi \int\_0^\pi \frac{dx}{a^2 \cos^2 x + b^2 \sin^2 x} - \text{I} \end{aligned}$$

*dx a x b x*

+

Thus 2I = 2 2 2 2 <sup>0</sup> cos sin

$$\text{or}$$

$$\begin{aligned} \text{for } \qquad &= \frac{\pi}{2} \int \frac{\pi}{a} \frac{dx}{a^2 \cos^2 x + b^2 \sin^2 x} = \frac{\pi}{2} \cdot 2 \int \frac{\frac{\pi}{2}}{a} \frac{dx}{a^2 \cos^2 x + b^2 \sin^2 x} \text{ (using } \mathbf{P}\_d\text{)}\\ &= \pi \left[ \int\_0^{\frac{\pi}{4}} \frac{dx}{a^2 \cos^2 x + b^2 \sin^2 x} + \int \frac{\frac{\pi}{2}}{\frac{\pi}{4}} \frac{dx}{a^2 \cos^2 x + b^2 \sin^2 x} \right] \\\\ &= \pi \left[ \int\_0^{\frac{\pi}{4}} \frac{\sec^2 x \, dx}{a^2 + b^2 \tan^2 x} + \int \frac{\frac{\pi}{2}}{\frac{\pi}{4}} \frac{\csc \infty^2 x \, dx}{a^2 \cot^2 x + b^2} \right] \\\\ &= \pi \left[ \int\_0^1 \frac{dt}{a^2 + b^2 t^2} - \int\_1^0 \frac{du}{a^2 u^2 + b^2} \right] \left( p u t \tan x = \mathtt{t} \, and \ \mathtt{cot} \, x = dt \right) \\\\ &= \frac{\pi}{ab} \left[ \tan^{-1} \frac{bt}{a} \right]\_0^1 - \frac{\pi}{ab} \left[ \tan^{-1} \frac{a u}{b} \right]\_1^0 = \pi \frac{\pi}{ab} \left[ \tan^{-1} \frac{b}{a} + \tan^{-1} \frac{a}{b} \right] = \frac{\pi^2}{2ab} \end{aligned}$$

### *Miscellaneous Exercise on Chapter 7*

Integrate the functions in Exercises 1 to 23.

**1.** <sup>3</sup> 1 *x x* − **2.** 1 *x a x b* + + + **3.** 2 1 *x ax x* − [Hint:Put *x*= *a t* ] **4.** <sup>3</sup> 2 4 4 1 *x x*( 1) + **5.** <sup>1</sup> <sup>1</sup> 2 3 1 *x x* + [Hint: <sup>11</sup> 1 1 2 3 3 6 1 1 *x x x x* 1 = + + , put *x* = *t* 6 ] **6.** <sup>2</sup> 5 ( 1) ( 9) *x x x* + + **7.** sin sin ( ) *x x a* − **8.** 5 log 4 log 3 log 2 log *x x x x e e e e* − − **9.** <sup>2</sup> cos 4 sin *x* − *x* **10.** 8 8 2 2 sin cos 1 2sin cos *x x x* − − **11.** 1 cos ( ) cos ( ) *x a x b* + + **12.** 3 8 1 *x* − *x* **13.** (1 ) (2 ) *x x x e* + + *e e* **14.** 2 2 1 ( 1) ( 4) *x x* + + **15.** cos<sup>3</sup> *x e* log sin*<sup>x</sup>* **16.** *e* 3 log*x* (*x* 4 + 1)– 1 **17.** *f* ′ (*ax* + *b*) [*f* (*ax* + *b*)]*<sup>n</sup>*

$$\begin{array}{llll} \text{118.} & \frac{1}{\sqrt{\sin^3 x \sin \left(x + \alpha\right)}} & \text{19.} & \sqrt{\frac{1-\sqrt{x}}{1+\sqrt{x}}} & \text{20.} & \frac{2+\sin 2x}{1+\cos 2x}e^x\\ \text{21.} & \frac{x^2+x+1}{\left(x+1\right)^2 \left(x+2\right)} & \text{22.} & \tan^{-1}\sqrt{\frac{1-x}{1+x}} \\ \text{23.} & & & \frac{\sqrt{x^2+1}\left[\log\left(x^2+1\right)-2\log x\right]}{x^4} \\ \end{array}$$

Evaluate the definite integrals in Exercises 24 to 31.

**24.** 2 1 sin 1 cos π π − <sup>−</sup> ∫ *<sup>x</sup> x e dx x* **25.** <sup>4</sup> 4 4 0 sin cos cos sin *x x dx x x* π + ∫ **26.** 2 2 2 2 0 cos cos 4 sin *x dx x x* π + ∫ **27.** <sup>3</sup> 6 sin cos sin 2 *x x dx x* π π + ∫ **28.** 1 <sup>0</sup> 1 *dx* + − *x x* ∫ **29.** <sup>4</sup> 0 sin cos 9 16 sin 2 *x x dx x* π + + ∫ **30.** <sup>2</sup> <sup>1</sup> 0 sin 2 tan (sin ) *x x dx* π − ∫ **31.** 4 1 [| 1| | 2 | | 3|] *x x x dx* − + − + − ∫ Prove the following (Exercises 32 to 37) **32.** 3 2 1 2 2 log ( 1) 3 3 *dx x x* = + + ∫ **33.** 1 0 1 *x x e dx* <sup>=</sup> ∫ **34.** 1 17 4 1 *x x dx* cos 0 − <sup>=</sup> ∫ **35.** <sup>3</sup> <sup>2</sup> 0 2 sin 3 *x dx* π <sup>=</sup> ∫ **36.** <sup>4</sup> <sup>3</sup> 0 2 tan 1 log2 *x dx* π = − ∫ **37.** 1 1 0 sin 1 2 *x dx* <sup>−</sup> <sup>π</sup> = − ∫ Choose the correct answers in Exercises 38 to 40 **38.** *dx* ∫ is equal to

$$\begin{aligned} \text{So,} \quad & \frac{\text{J}}{e^{x} + e^{-x}} \text{ is equal to} \\ & \text{(A) } \tan^{-1}(e^{x}) + \text{C} \quad & \text{(B) } \tan^{-1}(e^{-x}) + \text{C} \\ & \text{(C) } \log\left(e^{x} - e^{-x}\right) + \text{C} \quad & \text{(D) } \log\left(e^{x} + e^{-x}\right) + \text{C} \\ & \text{(D) } \frac{\cos 2x}{\left(\sin x + \cos x\right)^{2}} \, dx \text{ is equal to} \end{aligned}$$

$$\begin{array}{cccc} \text{(A)} & \frac{-1}{\sin x + \cos x} + \text{C} & \text{(B)} & \log|\sin x + \cos x| + \text{C} \\\\ \text{(C)} & \log|\sin x - \cos x| + \text{C} & \text{(D)} & \frac{1}{(\sin x + \cos x)^2} \\\\ & & \cdot \end{array}$$

**40.** If *f* (*a* + *b* – *x*) = *f* (*x*), then ( ) *b a x f x dx* ∫ is equal to

$$\begin{array}{ll} \text{(A)} \quad \frac{a+b}{2} \int\_{a}^{b} f(b-\mathbf{x}) \, d\mathbf{x} & \text{(B)} \quad \frac{a+b}{2} \int\_{a}^{b} f(b+\mathbf{x}) \, d\mathbf{x} \\\\ \text{(C)} \quad \frac{b-a}{2} \int\_{a}^{b} f(\mathbf{x}) \, d\mathbf{x} & \text{(D)} \quad \frac{a+b}{2} \int\_{a}^{b} f(\mathbf{x}) \, d\mathbf{x} \end{array}$$

### *Summary*

® Integration is the inverse process of differentiation. In the differential calculus, we are given a function and we have to find the derivative or differential of this function, but in the integral calculus, we are to find a function whose differential is given. Thus, integration is a process which is the inverse of differentiation.

Let F( ) ( ) *<sup>d</sup> x f x dx* <sup>=</sup> . Then we write *f x dx x* ( ) F ( ) C = + ∫ . These integrals are called indefinite integrals or general integrals, C is called constant of integration. All these integrals differ by a constant.

® Some properties of indefinite integrals are as follows:

- 1. [ ( ) ( )] ( ) ( ) *f x g x dx f x dx g x dx* + = + ∫ ∫ ∫
- 2. For any real number *k*, *k f x dx k f x dx* ( ) ( ) <sup>=</sup> ∫ ∫

More generally, if *f* 1 , *f* 2 , *f* 3 , ... , *f n* are functions and *k* 1 , *k* 2 , ... ,*k n* are real numbers. Then

$$\int \left[k\_1 \, f\_1(\mathbf{x}) + k\_2 \, f\_2(\mathbf{x}) + \dots + k\_n \, f\_n(\mathbf{x})\right] d\mathbf{x}$$

$$=k\_1 \int f\_1(\mathbf{x}) \, d\mathbf{x} + k\_2 \int f\_2(\mathbf{x}) \, d\mathbf{x} + \dots + k\_n \int f\_n(\mathbf{x}) \, d\mathbf{x}$$

® **Some standard integrals**

$$\text{(i)} \quad \int \mathbf{x}^n d\mathbf{x} = \frac{\mathbf{x}^{n+1}}{n+1} + \mathbf{C} \text{ , } n \neq -1. \text{ Particularly, } \int d\mathbf{x} = \mathbf{x} + \mathbf{C}$$

$$\begin{aligned} \text{(ii)} & \int \cos x \, dx = \sin x + \text{C} & \text{(iii)} & \int \sin x \, dx = -\cos x + \text{C} \\ \text{(iv)} & \int \sec^2 x \, dx = \tan x + \text{C} & \text{(v)} & \int \cos \sec^2 x \, dx = -\cot x + \text{C} \\ \text{(vi)} & \int \sec x \, \tan x \, dx = \sec x + \text{C} & \\ \text{(vii)} & \int \cos \sec x \cot x \, dx = -\cos \text{sec} \, x + \text{C} & \text{(viii)} & \int \frac{dx}{\sqrt{1 - x^2}} = \sin^{-1} x + \text{C} \\\\ \text{(xi)} & \int \frac{dx}{\sqrt{1 - x^2}} = -\cos^{-1} x + \text{C} & \text{(x)} & \int \frac{dx}{1 + x^2} = \tan^{-1} x + \text{C} \\\\ \text{(xi)} & \int \frac{dx}{1 + x^2} = -\cot^{-1} x + \text{C} & \text{(xi)} & \int e^x \, dx = e^x + \text{C} \\\\ \text{(xi)} & \int a^x \, dx = \frac{a^x}{\log a} + \text{C} & \text{(xi)} & \int \frac{1}{x} \, dx = \log|\, x \neq +\text{C} \end{aligned}$$

# ® **Integration by partial fractions**

Recall that a rational function is ratio of two polynomials of the form P( ) Q( ) *x x* , where P(*x*) and Q (*x*) are polynomials in *x* and Q (*x*) ≠ 0. If degree of the polynomial P (*x*) is greater than the degree of the polynomial Q (*x*), then we

may divide P (*x*) by Q (*x*) so that P( ) P ( ) <sup>1</sup> T ( ) Q( ) Q( ) *x x x x x* = + , where T(*x*) is a polynomial in *x* and degree of P<sup>1</sup> (*x*) is less than the degree of Q(*x*). T(*x*) being polynomial can be easily integrated. P ( ) <sup>1</sup> Q( ) *x x* can be integrated by

expressing P ( ) <sup>1</sup> Q( ) *x x* as the sum of partial fractions of the following type:

1. ( ) ( ) *px q x a x b* + − − = A B *x a x b* + − − , *a* ≠ *b* 2. <sup>2</sup> ( ) *px q x a* + − = <sup>2</sup> A B *x a* ( ) *x a* + − −

$$\begin{array}{rcl} \text{3.} & \frac{px^2 + qx + r}{\left(x - a\right)\left(x - b\right)\left(x - c\right)} & = & \frac{\text{A}}{\left(x - a\right)} + \frac{\text{B}}{x - b} + \frac{\text{C}}{x - c} \\\\ \text{4.} & \frac{px^2 + qx + r}{\left(x - a\right)^2\left(x - b\right)} & = & \frac{\text{A}}{\left(x - a\right)} + \frac{\text{B}}{\left(x - a\right)^2} + \frac{\text{C}}{x - b} \\\\ \text{5.} & \frac{px^2 + qx + r}{\left(x - a\right)\left(x^2 + bx + c\right)} & = & \frac{\text{A}}{\left(x - a\right)} + \frac{\text{B}x + \text{C}}{x^2 + bx + c} \end{array}$$

where *x* 2 + *bx* + *c* can not be factorised further.

# ® **Integration by substitution**

A change in the variable of integration often reduces an integral to one of the fundamental integrals. The method in which we change the variable to some other variable is called the method of substitution. When the integrand involves some trigonometric functions, we use some well known identities to find the integrals. Using substitution technique, we obtain the following standard integrals.

$$\text{(i)} \quad \int \tan x \, dx = \log|\sec x| + \text{C} \quad \text{(ii)} \quad \int \text{(j)} \int \text{(k)} \, dx = \log|\sin x| + \text{C}$$

$$\text{(iii)} \quad \int \sec x \, dx = \log \left| \sec x + \tan x \right| + C$$

$$\text{(iv)} \quad \int \text{cosec}\,\underline{\text{x}}\,d\underline{\eta} \equiv \log\left|\cos\underline{\text{c}}\,\underline{\text{c}}\,\underline{\text{c}}\,\underline{\text{c}}\right| + \text{C}$$

® **Integrals of some special functions**

(i) 2 2 1 log C 2 *dx x a x a a x a* − = + − + ∫ (ii) 2 2 1 log C 2 *dx a x a x a a x* + = + − − ∫ (iii) <sup>1</sup> 2 2 1 tan C *dx <sup>x</sup> x a a a* − = + + ∫ (iv) 2 2 2 2 log C *dx x x a x a* = + − + − ∫ (v) 1 2 2 sin C *dx x a a x* − = + − ∫

$$\text{(vi)} \quad \int \frac{d\mathbf{x}}{\sqrt{\mathbf{x}^2 + a^2}} = \log|\mathbf{x} + \sqrt{\mathbf{x}^2 + a^2}| + \mathbf{C}$$

® **Integration by parts** For given functions *f* 1 and *f* 2 , we have

$$\int f\_1(\mathbf{x}) \cdot f\_2(\mathbf{x}) \, d\mathbf{x} = f\_1(\mathbf{x}) \int f\_2(\mathbf{x}) \, d\mathbf{x} - \int \left[ \frac{d}{d\mathbf{x}} f\_1(\mathbf{x}) \cdot \int f\_2(\mathbf{x}) \, d\mathbf{x} \right] d\mathbf{x} \quad \text{i.e., the}$$

integral of the product of two functions = first function × integral of the second function – integral of {differential coefficient of the first function × integral of the second function}. Care must be taken in choosing the first function and the second function. Obviously, we must take that function as the second function whose integral is well known to us.

$$\bullet \quad \bigvee e^{\times}[f(\alpha) + f'(\alpha)] \, d\alpha = \big[ e^{\times}f'(\alpha) \, d\alpha + \mathbf{C} \big]$$

® **Some special types of integrals**

$$\text{(i)} \quad \int \sqrt{x^2 - a^2} \ \text{d}x = \frac{x}{2} \sqrt{x^2 - a^2} \\ \quad -\frac{a^2}{2} \log \left| x + \sqrt{x^2 - a^2} \right| + C$$

$$\text{(ii)} \quad \int \sqrt{\mathbf{x}^2 + a^2} \ \mathrm{d}x = \frac{\mathbf{x}}{2} \sqrt{\mathbf{x}^2 + a^2} + \frac{a^2}{2} \log \left| \mathbf{x} + \sqrt{\mathbf{x}^2 + a^2} \right| + C$$

$$\text{(iii)} \quad \int \sqrt{a^2 - x^2} \, dx = \frac{x}{2} \sqrt{a^2 - x^2} + \frac{a^2}{2} \sin^{-1} \frac{x}{a} + C$$

$$\text{(iv) Integrals of the types } \int \frac{dx}{ax^2 + bx + c} \text{ or } \int \frac{dx}{\sqrt{ax^2 + bx + c}} \text{ can be}$$

transformed into standard form by expressing

$$ax^2 + bx + c = a\left[\underbrace{x^2 + \frac{b}{a}x + \frac{c}{a}}\_{\cdot}\right] = a\left[\left(x + \frac{b}{2a}\right)^2 + \left(\frac{c}{a} - \frac{b^2}{4a^2}\right)\right]$$

(v) Integrals of the types <sup>2</sup> <sup>2</sup> or *px q dx px q dx ax bx c ax bx c* + + + + + + ∫ ∫ can be transformed into standard form by expressing

$$\begin{aligned} p\mathbf{x} + q &= \mathbf{A}\frac{d}{d\mathbf{x}}(a\mathbf{x}^2 + b\mathbf{x} + c) + \mathbf{B} = \mathbf{A}\left(2a\mathbf{x} + b\right) + \mathbf{B}\text{, where } \mathbf{A} \text{ and } \mathbf{B} \text{ are} \\ \text{determined by comparing coefficients on both sides.} \end{aligned}$$

® We have defined ( ) *b a f x dx* ∫ as the area of the region bounded by the curve *y* = *f* (*x*), *a* ≤ *x* ≤ *b*, the *x*-axis and the ordinates *x* = *a* and *x* = *b*. Let *x* be a given point in [*a*, *b*]. Then ( ) *x a f x dx* ∫ represents the **Area function** A (*x*).

This concept of area function leads to the Fundamental Theorems of Integral Calculus.

# ® **First fundamental theorem of integral calculus**

Let the area function be defined by A(*x*) = ( ) *x a f x dx* ∫ for all *x* ≥ *a*, where the function *f* is assumed to be continuous on [*a*, *b*]. Then A′ (*x*) = *f* (*x*) for all *x* ∈ [*a*, *b*].

® **Second fundamental theorem of integral calculus**

Let *f* be a continuous function of *x* defined on the closed interval [*a*, *b*] and

let F be another function such that F( ) ( ) *<sup>d</sup> x f x dx* = for all *x* in the domain of

$$\text{If, then } \int\_{-a}^{b} f(\alpha) \, d\alpha = \left[ \mathbf{F}(\alpha) + \mathbf{C} \right]\_{a}^{b} = \mathbf{F}(b) - \mathbf{F}(a) \dots$$

This is called the definite integral of *f* over the range [*a*, *b*], where *a* and *b* are called the limits of integration, *a* being the lower limit and *b* the upper limit.

**—**v**—**