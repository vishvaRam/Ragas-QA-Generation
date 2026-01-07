![](_page_0_Picture_0.jpeg)

# **DIFFERENTIAL EQUATIONS**

v*He who seeks for methods without having a definite problem in mind seeks for the most part in vain. – D. HILBERT* v

# **9.1 Introduction**

300 MATHEMATICS

In Class XI and in Chapter 5 of the present book, we discussed how to differentiate a given function *f* with respect to an independent variable, i.e., how to find *f* ′(*x*) for a given function *f* at each *x* in its domain of definition. Further, in the chapter on Integral Calculus, we discussed how to find a function *f* whose derivative is the function *g*, which may also be formulated as follows:

For a given function *g*, find a function *f* such that

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \mathbf{g}(\mathbf{x})\text{, where }\mathbf{y} = f(\mathbf{x}) \text{ \overbrace{\mathbf{y}}^{\text{---}} \dots \text{(1)}$$

An equation of the form (1) is known as a *differential equation*. A formal definition will be given later.

![](_page_0_Picture_8.jpeg)

In this chapter, we will study some basic concepts related to differential equation, general and particular solutions of a differential equation, formation of differential equations, some methods to solve a first order - first degree differential equation and some applications of differential equations in different areas.

# **9.2 Basic Concepts**

We are already familiar with the equations of the type:

$$\begin{cases} \begin{aligned} \chi^2 - 3\chi + 3 &= 0 \\ \sin \chi + \cos \chi &= 0 \\ \chi + \chi &= 7 \end{aligned} \end{cases} \tag{1}$$

![](_page_0_Picture_13.jpeg)

**Henri Poincare (1854-1912 )**

Let us consider the equation:

$$\mathbf{x} \times \frac{d\mathbf{y}}{d\mathbf{x}} + \mathbf{y} = \mathbf{0} \tag{4}$$

We see that equations (1), (2) and (3) involve independent and/or dependent variable (variables) only but equation (4) involves variables as well as derivative of the dependent variable *y* with respect to the independent variable *x*. Such an equation is called a *differential equation*.

In general, an equation involving derivative (derivatives) of the dependent variable with respect to independent variable (variables) is called a differential equation.

A differential equation involving derivatives of the dependent variable with respect to only one independent variable is called an ordinary differential equation, e.g.,

$$2\frac{d^2\mathbf{y}}{d\mathbf{x}^2} + \left(\frac{d\mathbf{y}}{d\mathbf{x}}\right)^3 = \mathbf{0} \text{ is an ordinary differential equation} \underset{\circ}{\longleftrightarrow} \underset{\circ}{\longleftrightarrow} \underset{\circ}{\longleftrightarrow} \mathbf{0} \tag{5}$$

Of course, there are differential equations involving derivatives with respect to more than one independent variables, called partial differential equations but at this stage we shall confine ourselves to the study of ordinary differential equations only. Now onward, we will use the term 'differential equation' for 'ordinary differential equation'.

# A**Note**

1. We shall prefer to use the following notations for derivatives:

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \mathbf{y}', \frac{d^2\mathbf{y}}{d\mathbf{x}^2} = \mathbf{y''}, \frac{d^3\mathbf{y}}{d\mathbf{x}^3} = \mathbf{y'''}$$

2. For derivatives of higher order, it will be inconvenient to use so many dashes

as supersuffix therefore, we use the notation *y n* for *n*th order derivative *n n d y dx*

## **9.2.1.** *Order of a differential equation*

Order of a differential equation is defined as the order of the highest order derivative of the dependent variable with respect to the independent variable involved in the given differential equation.

Consider the following differential equations:

$$\frac{d\mathbf{y}}{d\mathbf{x}} = e^{\mathbf{x}}\tag{6}$$

.

$$\frac{d^2\mathbf{y}}{d\mathbf{x}^2} + \mathbf{y} = \mathbf{0} \tag{7}$$

$$
\left(\frac{d^3\mathbf{y}}{d\mathbf{x}^3}\right) + \mathbf{x}^2 \left(\frac{d^2\mathbf{y}}{d\mathbf{x}^2}\right)^3 = \mathbf{0} \tag{8}
$$

The equations (6), (7) and (8) involve the highest derivative of first, second and third order respectively. Therefore, the order of these equations are 1, 2 and 3 respectively.

# **9.2.2** *Degree of a differential equation*

To study the degree of a differential equation, the key point is that the differential equation must be a polynomial equation in derivatives, i.e., *y*′, *y*″, *y*″′ etc. Consider the following differential equations:

2 3 2 3 2 2 *d y d y dy y dx dx dx* + − + = 0 ... (9)

$$\mathbf{u} \cdot \left(\frac{d\mathbf{y}}{d\mathbf{x}}\right)^2 + \left(\frac{d\mathbf{y}}{d\mathbf{x}}\right) - \sin^2\mathbf{y} = \mathbf{0} \tag{10}$$

$$\begin{pmatrix} \frac{d\mathbf{y}}{dx} + \sin\left(\frac{d\mathbf{y}}{dx}\right) = \mathbf{0} \\\\ \frac{d\mathbf{x}}{dx} = \mathbf{0} \end{pmatrix} \tag{11}$$

We observe that equation (9) is a polynomial equation in *y*″′, *y*″ and *y*′, equation (10) is a polynomial equation in *y*′ (not a polynomial in *y* though). Degree of such differential equations can be defined. But equation (11) is not a polynomial equation in *y*′ and degree of such a differential equation can not be defined.

By the degree of a differential equation, when it is a polynomial equation in derivatives, we mean the highest power (positive integral index) of the highest order derivative involved in the given differential equation.

In view of the above definition, one may observe that differential equations (6), (7), (8) and (9) each are of degree one, equation (10) is of degree two while the degree of differential equation (11) is not defined.

A**Note** Order and degree (if defined) of a differential equation are always positive integers.

2

**Example 1** Find the order and degree, if defined, of each of the following differential equations:

(i) cos 0 *dy x dx* − = (ii) 2 2 2 0 *d y dy dy xy x y dx dx dx* + − = (iii) <sup>2</sup> 0 *y y y e* ′ ′′′ + + =

## **Solution**

- (i) The highest order derivative present in the differential equation is *dy dx* , so its order is one. It is a polynomial equation in *y*′ and the highest power raised to *dy dx* is one, so its degree is one.
- (ii) The highest order derivative present in the given differential equation is 2 *d y dx* , so

its order is two. It is a polynomial equation in 2 2 *d y dx* and *dy dx* and the highest

power raised to 2 2 *d y dx* is one, so its degree is one.

(iii) The highest order derivative present in the differential equation is *y*′′′ , so its order is three. The given differential equation is not a polynomial equation in its derivatives and so its degree is not defined.

**EXERCISE 9.1**

Determine order and degree (if defined) of differential equations given in Exercises 1 to 10.

**1.** 4 4 sin( ) 0 *d y y dx* + = ′′′ **2.** *y*′ + 5*y* = 0 **3.** 4 2 2 3 0 *ds d s s dt dt* + = **4.** 2 2 2 cos 0 *d y dy dx dx* + = **5.** 2 2 cos3 sin3 *d y x x dx* = + **6.** <sup>2</sup> ( ) *y*′′′ + (*y*″) 3 + (*y*′) 4 + *y* 5 = 0 **7.** *y*′′′ + 2*y*″ + *y*′ = 0

- **8.** *y*′ + *y* = *e <sup>x</sup>* **9.** *y*″ + (*y*′) 2 + 2*y* = 0 **10.** *y*″ + 2*y*′ + sin *y* = 0
- **11.** The degree of the differential equation

3 2 2 2 sin 1 0 *d y dy dy dx dx dx* + + + = is (A) 3 (B) 2 (C) 1 (D) not defined

**12.** The order of the differential equation

2 2 2 2 3 0 *d y dy x y dx dx* − + = is (A) 2 (B) 1 (C) 0 (D) not defined

# **9.3. General and Particular Solutions of a Differential Equation**

In earlier Classes, we have solved the equations of the type:

$$\begin{array}{ccccc} & \mathfrak{x}^2 + 1 = \mathbf{0} & \updownarrow & \downarrow & \downarrow & \downarrow \\ \sin^2 \mathfrak{x} - \cos \mathfrak{x} = \mathbf{0} & \updownarrow & \downarrow & \downarrow & \downarrow \\ \end{array} \tag{2}$$

Solution of equations (1) and (2) are numbers, real or complex, that will satisfy the given equation i.e., when that number is substituted for the unknown *x* in the given equation, L.H.S. becomes equal to the R.H.S..

$$\text{Now consider the differential equation} \\ \frac{d^2y}{d\mathbf{x}^2} + \mathbf{y} = \mathbf{0} \qquad \qquad \qquad \dots \text{ (3)}$$

In contrast to the first two equations, the solution of this differential equation is a function φ that will satisfy it i.e., when the function φ is substituted for the unknown *y* (dependent variable) in the given differential equation, L.H.S. becomes equal to R.H.S..

The curve *y* = φ (*x*) is called the solution curve (integral curve) of the given differential equation. Consider the function given by

$$\mathbf{y} = \Phi \left( \mathbf{x} \right) = a \sin \left( \mathbf{x} + b \right), \tag{4}$$

where *a*, *b* ∈ **R**. When this function and its derivative are substituted in equation (3), L.H.S. = R.H.S.. So it is a solution of the differential equation (3).

Let *a* and *b* be given some particular values say *a* = 2 and 4 *b* π = , then we get a

$$\begin{array}{ll}\text{function} & \mathbf{y} = \boldsymbol{\phi}\_{\text{l}}(\mathbf{x}) = \; 2\sin\left(\mathbf{x} + \frac{\pi}{4}\right) \\\\ \end{array} \tag{5}$$

When this function and its derivative are substituted in equation (3) again L.H.S. = R.H.S.. Therefore φ1 is also a solution of equation (3).

Function φ consists of two arbitrary constants (parameters) *a*, *b* and it is called *general solution* of the given differential equation. Whereas function φ<sup>1</sup> contains no arbitrary constants but only the particular values of the parameters *a* and *b* and hence is called a *particular solution* of the given differential equation.

The solution which contains arbitrary constants is called the *general solution* (*primitive*) of the differential equation.

The solution free from arbitrary constants i.e., the solution obtained from the general solution by giving particular values to the arbitrary constants is called a *particular solution* of the differential equation.

**Example 2** Verify that the function *y* = *e* – 3*x* is a solution of the differential equation

$$\frac{d^2\mathbf{y}}{d\mathbf{x}^2} + \frac{d\mathbf{y}}{d\mathbf{x}} - 6\mathbf{y} = 0$$

**Solution** Given function is *y* = *e* – 3*x* . Differentiating both sides of equation with respect to *x* , we get

$$\frac{dy}{dx} = -3e^{\frac{-3x}{3}} \Big|\_{x=0} \quad \Big|\_{x=0} \Big|\_{x=0} \Big|\_{x=0} \Big|\_{x=0} \quad \Big|\_{x=0} \quad \Big|\_{x=0} \quad \Big|\_{x=0} \quad \Big|\_{x=0}$$

Now, differentiating (1) with respect to *x*, we have

$$\frac{d^2y}{d\alpha^2} = 9e^{-3x}$$

Substituting the values of 2 2 , *d y dy dx dx* and *y* in the given differential equation, we get L.H.S. = 9 *e*– <sup>3</sup>*<sup>x</sup>*+ (–3*e* – 3*x* ) – 6.*e* – 3*x* = 9 *e*– <sup>3</sup>*<sup>x</sup>*– 9 *e*– <sup>3</sup>*<sup>x</sup>*= 0 = R.H.S..

Therefore, the given function is a solution of the given differential equation.

**Example 3** Verify that the function *y* = *a* cos *x* + *b* sin *x*, where, *a*, *b* ∈ **R** is a solution of the differential equation 2 2 0 *d y y dx* + =

**Solution** The given function is

$$y = a\cos x + b\sin x \quad \qquad \qquad \qquad \dots \text{(1)}$$

Differentiating both sides of equation (1) with respect to *x*, successively, we get

$$\frac{d\mathbf{y}}{d\mathbf{x}} = -a\sin\mathbf{x} + b\cos\mathbf{x}$$

$$\frac{d^2\mathbf{y}}{d\mathbf{x}^2} = -a\cos\mathbf{x} - b\sin\mathbf{x}$$

Substituting the values of 2 2 *d y dx* and *y* in the given differential equation, we get

L.H.S. = (– *a* cos *x* – *b* sin *x*) + (*a* cos *x* + *b* sin *x*) = 0 = R.H.S.

Therefore, the given function is a solution of the given differential equation.

# **EXERCISE 9.2**

In each of the Exercises 1 to 10 verify that the given functions (explicit or implicit) is a solution of the corresponding differential equation:

- **1.** *y* = *e x* + 1 : *y*″ – *y*′ = 0 **2.** *y* = *x* 2 + 2*x* + C : *y*′ – 2*x* – 2 = 0 **3.** *y* = cos *x* + C : *y*′ + sin *x* = 0 **4.** *y* = <sup>2</sup> 1+ *x* : *y*′ = <sup>2</sup> 1 *xy* + *x* **5.** *y* = A*x* : *xy*′ = *y* (*x* ≠ 0) **6.** *y* = *x* sin *x* : *xy*′ = *y* + *x* 2 2 *x y* − (*x* ≠ 0 and *x* > *y* or *x* < *– y*) **7.** *xy* = log *y* + C : *y*′ = 2 1 *y* − *xy* (*xy* ≠ 1) **8.** *y* – cos *y* = *x* : (*y* sin *y* + cos *y* + *x*) *y*′ = *y* **9.** *x + y =* tan–1*y* : *y* 2 *y*′ + *y* 2 + 1 = 0 **10.** *y* = 2 2 *a x* − *x* ∈ (–*a*, *a*) : *x* + *y dy dx* = 0 (*<sup>y</sup>* <sup>≠</sup> 0) **11.** The number of arbitrary constants in the general solution of a differential equation of fourth order are: (A) 0 (B) 2 (C) 3 (D) 4
- **12.** The number of arbitrary constants in the particular solution of a differential equation of third order are:
	- (A) 3 (B) 2 (C) 1 (D) 0

# **9.4. Methods of Solving First Order, First Degree Differential Equations**

In this section we shall discuss three methods of solving first order first degree differential equations.

# **9.4.1** *Differential equations with variables separable*

A first order-first degree differential equation is of the form

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \mathbf{F}(\mathbf{x}, \mathbf{y}) \tag{1}$$

If F (*x*, *y*) can be expressed as a product g (*x*) *h*(*y*), where, *g*(*x*) is a function of *x* and *h*(*y*) is a function of *y*, then the differential equation (1) is said to be of variable separable type. The differential equation (1) then has the form

$$\frac{d\mathbf{y}}{d\mathbf{x}} = h \text{ (y) } \dots \text{ g} \text{(x)}\tag{2}$$

If *h*(*y*) ≠ 0, separating the variables, (2) can be rewritten as

$$\frac{1}{h(\mathbf{y})}\ \mathrm{d}\mathbf{y} = \mathrm{g}\begin{pmatrix} \mathbf{x} \\ \end{pmatrix} \begin{pmatrix} \mathrm{d}\mathbf{x} \\ \end{pmatrix} \tag{3}$$

Integrating both sides of (3), we get

$$\int \frac{1}{h(\mathbf{y})} \, d\mathbf{y} = \int g(\mathbf{x}) \, d\mathbf{x} \tag{14}$$

Thus, (4) provides the solutions of given differential equation in the form

$$H(\mathbf{y}) = \mathbf{G}\left(\mathbf{x}\right) + \mathbf{C}$$

Here, H (*y*) and G (*x*) are the anti derivatives of 1 *h y*( ) and *<sup>g</sup>* (*x*) respectively and C is the arbitrary constant.

**Example 4** Find the general solution of the differential equation <sup>1</sup> 2 *dy x dx y* + = − , (*y* ≠ 2)

**Solution** We have

$$\frac{dy}{dx} = \frac{x+1}{2-y} \tag{1}$$

Separating the variables in equation (1), we get

$$(\mathcal{Q} - \mathbf{y}) \text{ dy = (x+1) } d\mathbf{x} \tag{2}$$

Integrating both sides of equation (2), we get

$$\int (2 - y) \, dy = \int (x + 1) \, dx$$

$$2\text{ y} - \frac{\text{y}^2}{2} = \frac{\text{x}^2}{2} + \text{x} + \text{C}\_1$$

or

or *x* 2 + *y* 2 + 2*x* – 4*y* + 2 C<sup>1</sup> = 0

$$\text{or } \begin{aligned} \text{x}^2 + \text{y}^2 + 2\text{x} - 4\text{y} + \text{C} = 0, \text{ where } \text{C} = 2\text{C}\_{\perp} \end{aligned}$$

which is the general solution of equation (1).

**Example 5** Find the general solution of the differential equation 2 2 1 1 *dy y dx x* + = + .

**Solution** Since 1 + *y* <sup>2</sup> ≠ 0, therefore separating the variables, the given differential equation can be written as

$$\frac{d\mathbf{y}}{1+\mathbf{y}^2} = \frac{d\mathbf{x}}{1+\mathbf{x}^2} \tag{1}$$

Integrating both sides of equation (1), we get

$$\int \frac{d\mathbf{y}}{1+\mathbf{y}^2} = \int \frac{d\mathbf{x}}{1+\mathbf{x}^2}$$

$$\text{or} \qquad \qquad \qquad \tan^{-1} \text{ y = \tan^{-1} x + C}$$

which is the general solution of equation (1).

**Example 6** Find the particular solution of the differential equation <sup>2</sup> 4 *dy xy dx* = − given

that *y* = 1, when *x* = 0.

**Solution** If *y* ≠ 0, the given differential equation can be written as

$$\frac{dy}{y^2} = -4x \, dx \, \overbrace{\dots}^{\dots} \qquad \qquad \qquad \qquad \dots \text{(1)}$$

... (2)

Integrating both sides of equation (1), we get

$$
\int \frac{d\mathbf{y}}{\mathbf{y}^2} = -4 \int \mathbf{x} \, d\mathbf{x}
$$

$$
-\frac{1}{\mathbf{y}} = -2\mathbf{x}^2 + \mathbf{C}
$$

or

or *y* = <sup>2</sup>

Substituting *y* = 1 and *x* = 0 in equation (2), we get, C = – 1.

Now substituting the value of C in equation (2), we get the particular solution of the

1 2 C *x* −

$$\text{given differential equation as}\quad y = \frac{1}{2x^2 + 1}\text{.}$$

**Example 7** Find the equation of the curve passing through the point (1, 1) whose differential equation is *x dy* = (2*x* 2 + 1) *dx* (*x* ≠ 0).

**Solution** The given differential equation can be expressed as

$$d\mathbf{y}^{\ast \ast} = \left(\frac{2x^2 + 1}{x}\right) d\mathbf{x}^{\ast \ast}$$
 
$$d\mathbf{y} = \left(2x + \frac{1}{x}\right) d\mathbf{x} \tag{1}$$

Integrating both sides of equation (1), we get

$$\int \mathrm{d}\mathbf{y} = \int \left(2\mathbf{x} + \frac{1}{\mathbf{x}}\right)d\mathbf{x}$$
 
$$\mathbf{y} = \mathbf{x}^2 + \log|\mathbf{x}| + \mathbf{C} \qquad \qquad \qquad \underset{\bigcirc \mathbf{y}}{\bigcirc \text{....(2)}} \dots \bigcirc \mathbf{y}$$

Equation (2) represents the family of solution curves of the given differential equation but we are interested in finding the equation of a particular member of the family which passes through the point (1, 1). Therefore substituting *x* = 1, *y* = 1 in equation (2), we get C = 0.

Now substituting the value of C in equation (2) we get the equation of the required curve as *y* = *x* 2 + log | *x* |.

**Example 8** Find the equation of a curve passing through the point (–2, 3), given that

the slope of the tangent to the curve at any point (*x*, *y*) is 2 2*x y* .

**Solution** We know that the slope of the tangent to a curve is given by *dy dx* .

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \frac{2\mathbf{x}}{\mathbf{y}^2} \tag{1}$$

Separating the variables, equation (1) can be written as

$$\mathbf{y}^2 \ d\mathbf{y} = \mathbf{2x} \ d\mathbf{x} \tag{2}$$

Integrating both sides of equation (2), we get

$$
\int \mathbf{y}^2 d\mathbf{y} = \int 2\mathbf{x} \, d\mathbf{x}
$$

$$
\frac{\mathbf{y}^3}{3} = \mathbf{x}^2 + \mathbf{C} \quad \quad \quad \quad \quad \quad \quad \quad \quad \dots \text{(3)}
$$

or

so,

\* The notation *dy dx* due to Leibnitz is extremely flexible and useful in many calculation and formal transformations, where, we can deal with symbols *dy* and *dx* exactly as if they were ordinary numbers. By treating *dx* and *dy* like separate entities, we can give neater expressions to many calculations. Refer: Introduction to Calculus and Analysis, volume-I page 172, By Richard Courant, Fritz John Spinger – Verlog New York.

Substituting *x* = –2, *y* = 3 in equation (3), we get C = 5.

Substituting the value of C in equation (3), we get the equation of the required curve as

$$\frac{\text{y}^3}{3} = \text{x}^2 + \text{S} \quad \text{or} \quad \text{y} = \left(3\text{x}^2 + 1\text{S}\right)^{\frac{1}{3}}$$

**Example 9** In a bank, principal increases continuously at the rate of 5% per year. In how many years Rs 1000 double itself?

**Solution** Let P be the principal at any time *t*. According to the given problem,

$$\begin{aligned} \frac{dp}{dt} &= \left(\frac{\mathbf{\mathcal{S}}}{100}\right) \times \mathbf{P} \\ \frac{dp}{dt} &= \frac{\mathbf{P}}{20} \\ \vdots & \vdots \end{aligned} \qquad \begin{aligned} \mathbf{\mathcal{P}} & \stackrel{\scriptstyle \mathbf{\mathcal{P}}}{\bigtriangleup} \\ \bigtriangleup & \stackrel{\scriptstyle \mathbf{\mathcal{P}}}{\bigtriangleup} \cdots \bigtriangleup \end{aligned}$$

or

separating the variables in equation (1), we get

$$\frac{dp}{P} = \frac{dt}{20} \Big/ \Big/ \Big/ \Big/ \Big/ \Big/ \Big/ \Big/ \Big/ \Big/ \Big/ \Big/}{\int \Big/ \Big/ \int \Big/ \Big/ \Big} \qquad \qquad \dots \text{(2)}$$

Integrating both sides of equation (2), we get

$$\log \mathbf{P} = \frac{t}{\mathbf{20}} + \mathbf{C}\_1$$
 
$$\mathbf{P} = e^{\frac{t}{20}} e^{\mathbf{C}\_1}$$

or P = C <sup>20</sup> *t e* (where *e* <sup>C</sup><sup>1</sup> = C ) ... (3) Now P = 1000, when *t* = 0

Substituting the values of P and *t* in (3), we get C = 1000. Therefore, equation (3), gives

$$\mathbb{P} = 1000 \ e^{\frac{t}{20}}$$

Let *t* years be the time required to double the principal. Then

$$2000 = 1000 \, e^{\frac{t}{20}} \implies t = 20 \, \log\_e 20$$

# **EXERCISE 9.3**

For each of the differential equations in Exercises 1 to 10, find the general solution:

**1.** 1 cos 1 cos *dy x dx x* − = + **2.** <sup>2</sup> 4 ( 2 2) *dy y y dx* = − − < <

$$\begin{aligned} \text{1. } \quad & \frac{dy}{dx} + y = 1 \text{ (y} \neq 1) & \text{4. } \quad & \sec^2 x \tan y \, dx + \sec^2 y \tan x \, dy = 0\\ \text{1. } \quad & \left(e^x + e^{-x}\right) \, dy - \left(e^x - e^{-x}\right) \, dx = 0 & \text{6. } \quad & \frac{dy}{dx} = \left(1 + x^2\right) \left(1 + y^2\right) \\\\ \text{1. } \quad & y \log y \, dx - x \, dy = 0 & \text{8. } \quad & x^s \frac{dy}{dx} = -y^s \\\\ \text{9. } \quad & \frac{dy}{dx} = \sin^{-1} x & \text{10. } \quad & e^x \tan y \, dx + \left(1 - e^x\right) \sec^2 y \, dy = 0 \end{aligned}$$

For each of the differential equations in Exercises 11 to 14, find a particular solution satisfying the given condition:

**11.** 3 2 ( 1) *dy x x x dx* + + + = 2*x* 2 + *x*; *y* = 1 when *x* = 0

$$\text{12.} \quad \text{x } (\text{x}^2 - 1) \frac{d\text{y}}{d\text{x}} = 1 \text{ ; } \text{y} = 0 \text{ when } \text{x} = 2$$

$$\mathbf{13.} \quad \cos\left(\frac{dy}{dx}\right) = a \text{ ( $a \in \mathbf{R}$ )}; \text{ y =  $1$  when } \boldsymbol{\lambda} = \mathbf{0}$$

$$\mathbf{14.} \quad \frac{d\mathbf{y}}{d\mathbf{x}} = \mathbf{y} \tan \mathbf{x} \text{ ; } \mathbf{y} = \mathbf{1} \text{ when } \mathbf{x} = \mathbf{0}.$$

- **15.** Find the equation of a curve passing through the point (0, 0) and whose differential equation is *y*′ = *e x* sin *x.*
- **16.** For the differential equation ( 2) ( 2) *dy xy x y dx* = + + , find the solution curve passing through the point (1, –1).
- **17.** Find the equation of a curve passing through the point (0, –2) given that at any point (*x*, *y*) on the curve, the product of the slope of its tangent and *y* coordinate of the point is equal to the *x* coordinate of the point.
- **18.** At any point (*x*, *y*) of a curve, the slope of the tangent is twice the slope of the line segment joining the point of contact to the point (– 4, –3). Find the equation of the curve given that it passes through (–2, 1).
- **19.** The volume of spherical balloon being inflated changes at a constant rate. If initially its radius is 3 units and after 3 seconds it is 6 units. Find the radius of balloon after *t* seconds.

- **20.** In a bank, principal increases continuously at the rate of *r*% per year. Find the value of *r* if Rs 100 double itself in 10 years (log*<sup>e</sup>* 2 = 0.6931).
- **21.** In a bank, principal increases continuously at the rate of 5% per year. An amount of Rs 1000 is deposited with this bank, how much will it worth after 10 years (*e* 0.5 = 1.648).
- **22.** In a culture, the bacteria count is 1,00,000. The number is increased by 10% in 2 hours. In how many hours will the count reach 2,00,000, if the rate of growth of bacteria is proportional to the number present?

**23.** The general solution of the differential equation *dy x y e dx* + = is

(A) *e x* + *e* –*y* = C (B) *e x* + *e y* = C (C) *e* –*x* + *e y* = C (D) *e* –*x* + *e* –*y* = C

# **9.4.2** *Homogeneous differential equations*

Consider the following functions in *x* and *y*

F1 (*x*, *y*) = *y* 2 + 2*xy*, F<sup>2</sup> (*x*, *y*) = 2*x* – 3*y*, F3 (*x*, *y*) = cos *y x* , F<sup>4</sup> (*x*, *y*) = sin *x* + cos *y*

If we replace *x* and *y* by λ*x* and λ*y* respectively in the above functions, for any nonzero constant λ, we get

$$\begin{aligned} \mathcal{F}\_1^- (\lambda x, \lambda y) &= \lambda^2 \left(y^2 + 2xy\right) = \lambda^2 \mathcal{F}\_1^- (\lambda^\prime, y) \\ \mathcal{F}\_2^- (\lambda x, \lambda y) &= \lambda^2 \left(2x - 3y\right) = \lambda^2 \mathcal{F}\_2^- (x, y) \\ \mathcal{F}\_3^- (\lambda x, \lambda y) &= \cos\left(\frac{\lambda y}{\lambda x}\right) = \cos\left(\frac{y}{x}\right) = \lambda^0 \mathcal{F}\_3^- (x, y) \end{aligned}$$

F4 (λ*x*, λ*y*) = sin λ*x* + cos λ*y* ≠ λ *n* F4 (*x*, *y*), for any *n* ∈ **N**

Here, we observe that the functions F<sup>1</sup> , F<sup>2</sup> , F<sup>3</sup> can be written in the form F(λ*x*, λ*y*) = λ *n* F(*x*, *y*) but F<sup>4</sup> can not be written in this form. This leads to the following definition:

A function F(*x*, *y*) is said to be *homogeneous function of degree n* if

F(λ*x*, λ*y*) = λ *n* F(*x*, *y*) for any nonzero constant λ.

We note that in the above examples, F<sup>1</sup> , F<sup>2</sup> , F<sup>3</sup> are homogeneous functions of degree 2, 1, 0 respectively but F<sup>4</sup> is not a homogeneous function.

We also observe that

$$\begin{aligned} \mathbf{F}\_{\downarrow}(\mathbf{x}, \mathbf{y}) &= \mathbf{x}^2 \left( \frac{\mathbf{y}^2}{\mathbf{x}^2} + \frac{2\mathbf{y}}{\mathbf{x}} \right) = \mathbf{x}^2 h\_{\mathbf{l}} \left( \frac{\mathbf{y}}{\mathbf{x}} \right), \\ \text{or} \quad \mathbf{F}\_{\downarrow}(\mathbf{x}, \mathbf{y}) &= \mathbf{y}^2 \left( 1 + \frac{2\mathbf{x}}{\mathbf{y}} \right) = \mathbf{y}^2 h\_2 \left( \frac{\mathbf{x}}{\mathbf{y}} \right) \end{aligned}$$

$$\text{or}$$

$$\mathcal{F}\_2(\mathbf{x}, \mathbf{y}) = \left. x^1 \left( 2 - \frac{3\mathbf{y}}{x} \right) = x^1 h\_3 \left( \frac{\mathbf{y}}{x} \right) \right|$$

$$\text{or}$$

$$\mathcal{F}\_2(\mathbf{x}, \mathbf{y}) = \left. \mathbf{y}^1 \left( 2 \frac{\mathbf{x}}{\mathbf{y}} - 3 \right) = \mathbf{y}^1 h\_4 \left( \frac{\mathbf{x}}{\mathbf{y}} \right)$$

$$\mathcal{F}\_3(\mathbf{x}, \mathbf{y}) = \left. x^0 \cos \left( \frac{\mathbf{y}}{x} \right) \right| = \mathbf{x}^0 \left. h\_5 \left( \frac{\mathbf{y}}{x} \right) \right|$$

$$\mathcal{F}\_4(\mathbf{x}, \mathbf{y}) \neq \mathbf{x}^n \left. h\_6 \left( \frac{\mathbf{y}}{x} \right) \right|, \text{ for any } n \in \mathbb{N}$$

$$\text{or}$$

$$\mathcal{F}\_4(\mathbf{x}, \mathbf{y}) \neq \mathcal{F}\_5^n \left. h\_7 \left( \frac{\mathbf{x}}{\mathbf{y}} \right) \right|, \text{ for any } n \in \mathbb{N}$$

Therefore, a function F (*x*, *y*) is a homogeneous function of degree *n* if

$$\overbrace{\left(\begin{array}{c}\Box\\\Box\end{array}\right)\mathbf{F}(\mathbf{x},\mathbf{y})=\lambda^{n}g\left(\frac{\mathbf{y}}{\chi}\right)^{n}\quad\text{or}\qquad\mathbf{y}^{n}h\left(\frac{\mathbf{x}}{\chi}\right)^{n}$$

A differential equation of the form *dy dx* = F (*x, y*) is said to be *homogenous* if F(*x*, *y*) is a homogenous function of degree zero.

To solve a homogeneous differential equation of the type

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \mathbf{F}(\mathbf{x}, \mathbf{y}) = \mathbf{g}\left(\frac{\mathbf{y}}{\mathbf{x}}\right) \tag{1}$$

We make the substitution *y* = *v* . *x* ... (2)

Differentiating equation (2) with respect to *x*, we get

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \mathbf{v} + \mathbf{x}\frac{d\mathbf{v}}{d\mathbf{x}}\tag{3}$$

Substituting the value of *dy dx* from equation (3) in equation (1), we get

$$
\begin{aligned}
\lambda \nu + \varkappa \frac{d\nu}{d\varkappa} &= \mathcal{g}\left(\nu\right) \\
\cdot \qquad &\times \\
\times \frac{d\nu}{d\varkappa} &= \mathcal{g}\left(\nu\right) - \nu
\end{aligned}
\tag{4}
$$

or

Separating the variables in equation (4), we get

$$\frac{d\upsilon}{d\varrho(\upsilon) - \upsilon} = \frac{d\upsilon}{\upsilon} \tag{5}$$

Integrating both sides of equation (5), we get

$$\int \frac{d\mathbf{v}}{\mathbf{g}\left(\mathbf{v}\right) - \mathbf{v}} = \int \frac{1}{\mathbf{x}} d\mathbf{x} + \mathbf{C} \tag{\stackrel{\frown}{\underset{\bigtriangleup}{\rightleftharpoons}}} \stackrel{\frown}{\dots} \text{(6)}$$

Equation (6) gives general solution (primitive) of the differential equation (1) when we replace *v* by *<sup>y</sup> x* .

A**Note** If the homogeneous differential equation is in the form F( , ) *dx x y dy* = where, F (*x*, *y*) is homogenous function of degree zero, then we make substitution *x v y* = i.e., *x* = *vy* and we proceed further to find the general solution as discussed above by writing F( , ) . *dx <sup>x</sup> x y h dy y* = =

**Example 10** Show that the differential equation (*x* – *y*) *dy dx* = *x* + 2*y* is homogeneous and solve it.

**Solution** The given differential equation can be expressed as

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \frac{\mathbf{x} + 2\mathbf{y}}{\mathbf{x} - \mathbf{y}} \tag{1}$$
 
$$\frac{\cdot}{\cdot x + 2\mathbf{y}}$$

Let F(*x*, *y*) = *x y* + −

$$\text{Now }\mathbf{\hat{x}} = \mathbf{\hat{x}} \text{ and } \mathbf{\hat{y}} = \frac{\mathbf{\hat{x}}(\mathbf{x} + \mathbf{2y})}{\mathbf{\hat{x}}(\mathbf{x} - \mathbf{y})} = \mathbf{\hat{x}}^0 \cdot \mathbf{f}(\mathbf{x}, \mathbf{y})$$

Therefore, F(*x*, *y*) is a homogenous function of degree zero. So, the given differential equation is a homogenous differential equation.

## **Alternatively**,

or

$$\frac{dy}{dx} = \left(\frac{1 + \frac{2\,\mathrm{y}}{\mathrm{x}}}{1 - \frac{\mathrm{y}}{\mathrm{x}}}\right) = \mathrm{g}\left(\frac{\mathrm{y}}{\mathrm{x}}\right) \tag{2}$$

R.H.S. of differential equation (2) is of the form *g y x* and so it is a homogeneous

function of degree zero. Therefore, equation (1) is a homogeneous differential equation. To solve it we make the substitution

$$\mathbf{y} = \mathbf{v}\mathbf{x} \qquad \qquad \qquad \qquad \qquad \bigvee \quad \bigvee \quad \bigvee \quad \quad \quad \quad \dots \text{(3)}$$

Differentiating equation (3) with respect to, *x* we get

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \nu + \lambda \frac{d\mathbf{y}}{d\mathbf{x}} \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad (4)$$

Substituting the value of *y* and *dy dx* in equation (1) we get

$$\begin{aligned} \left(\begin{array}{c} \text{v} + x \frac{d\nu}{dx} = \frac{1+\sqrt{2}\nu}{1-\nu} \\ \text{x} \frac{d\nu}{dx} = \frac{1+2\nu}{1-\nu} - \nu \end{array} \right) \end{aligned}$$

$$\text{or} \qquad \qquad \qquad \lor \quad \bigvee \quad \bigvee \quad \quad \text{x} \\ \frac{d\nu}{d\mathbf{x}} = \frac{\nu^2 + \nu + 1}{1 - \nu}$$

$$\text{or} \qquad \underbrace{\cdots}\_{\sqrt{\cdot \cdot \cdot} \cdots} \overset{\cdots}{\nu - 1} \frac{\nu - 1}{\nu^2 + \nu + 1} d\nu = \frac{-d\nu}{x}$$

Integrating both sides of equation (5), we get

$$
\int \frac{1}{\nu^2 + \nu + 1} d\nu \,\,\, = \,\, - \int \frac{\cdots}{\infty}
$$

$$
\text{or}
\qquad
\frac{1}{2} \int \frac{2\nu + 1 - 3}{\nu^2 + \nu + 1} d\nu \,\,\, = -\log|\chi| + C\_{\chi}
$$

$$\frac{1}{2}\int \frac{2\nu+1}{\nu^2+\nu+1}d\nu - \frac{3}{2}\int \frac{1}{\nu^2+\nu+1}d\nu = -\log|\,\nu| + C\_1$$

or

$$\text{or} \qquad \frac{1}{2}\log\left|\boldsymbol{\nu}^2 + \boldsymbol{\nu} + 1\right| - \frac{3}{2}\int \frac{1}{\left(\boldsymbol{\nu} + \frac{1}{2}\right)^2 + \left(\frac{\sqrt{3}}{2}\right)^2} d\boldsymbol{\nu} = -\log|\boldsymbol{\nu}| + C\_1$$

$$\text{For } \frac{1}{2}\log\left|\nu^2 + \nu + 1\right| - \frac{3}{2} \cdot \frac{2}{\sqrt{3}} \tan^{-1}\left(\frac{2\nu + 1}{\sqrt{3}}\right) = -\log\left|x\right| + C\_1$$

$$\text{for } \begin{aligned} \text{For } \begin{aligned} \text{ } \frac{1}{2}\log\left|\nu^2 + \nu + 1\right| + \frac{1}{2}\log \nu^2 = \sqrt{3}\tan^{-1}\left(\frac{2\nu + 1}{\sqrt{3}}\right) + \text{C}\_1\\ \text{ } \begin{array}{c} \text{ } \end{array} \end{aligned} \end{aligned} \left(\frac{2\nu + 1}{\sqrt{3}}\right) + \text{C}\_1 \begin{pmatrix} \text{Why} \\ \text{(Why?)} \end{aligned} \right)$$

Replacing *v* by *y x* , we get

$$\text{For } \begin{aligned} \text{For } \begin{aligned} \frac{1}{2}\log\left|\frac{y^2}{x^2} + \frac{y}{x} + 1\right| + \frac{1}{2}\log x^2 &= \sqrt{3}\tan^{-1}\left(\frac{2y+x}{\sqrt{3}x}\right) + C\_1\\ \end{aligned} \end{aligned}$$

or

$$\frac{1}{2}\log\left|\left(\frac{y^2}{x^2} + \frac{y}{x} + 1\right)\chi^2\right| = \sqrt{3}\tan^{-1}\left(\frac{2\bar{y} + \chi}{\sqrt{3}\chi}\right) + C\_1$$

or

$$\log\left|\left(\mathbf{y}^{\frac{1}{2}}+\mathbf{x}\mathbf{y}+\mathbf{x}^{2}\right)\right| = 2\sqrt{3}\tan^{-1}\left(\frac{2\mathbf{y}+\mathbf{x}}{\sqrt{3}\mathbf{x}}\right) + 2\mathbf{C}\_{1}$$

$$\text{or} \qquad \qquad \log \left| \begin{pmatrix} \mathbf{x}^2 + \mathbf{y} \mathbf{y} + \mathbf{y}^2 \\ \mathbf{y} \end{pmatrix} \right| = 2\sqrt{3} \tan^{-1} \left( \frac{\mathbf{x} + 2\mathbf{y}}{\sqrt{3}\mathbf{x}} \right) + C$$

which is the general solution of the differential equation (1)

**Example 11** Show that the differential equation cos cos *y dy y x y x x dx x* = + is homogeneous and solve it.

**Solution** The given differential equation can be written as

$$\frac{dy}{dx} = \frac{y\cos\left(\frac{y}{x}\right) + x}{x\cos\left(\frac{y}{x}\right)}\tag{1}$$

It is a differential equation of the form F( , ) *dy x y dx* = .

$$\text{Here } \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text{F}(\mathbf{x}, \mathbf{y}) = \frac{\mathbf{y} \cos \left( \frac{\mathbf{y}}{\mathbf{x}} \right) + \mathbf{x}}{\mathbf{x} \cos \left( \frac{\mathbf{y}}{\mathbf{x}} \right)} \text{ }$$

Replacing *x* by λ*x* and *y* by λ*y*, we get

$$\mathcal{F}(\lambda x, \lambda y) = \frac{\lambda \text{[by} \cos \left(\frac{y}{x}\right) + x]}{\lambda \left(x \cos \frac{y}{x}\right)} = \lambda^0 \left[\mathcal{F}(x, y)\right] \quad (1)$$

Thus, F(*x*, *y*) is a homogeneous function of degree zero.

Therefore, the given differential equation is a homogeneous differential equation. To solve it we make the substitution

$$\mathbf{y} = \nu \mathbf{x} \cup \bigvee \qquad \qquad \qquad \bigvee \qquad \qquad \qquad \qquad \dots (2)$$

Differentiating equation (2) with respect to *x*, we get

$$\frac{d\mathbf{\hat{y}}}{d\mathbf{x}} = \mathbf{v} + \mathbf{\hat{x}} \frac{d\mathbf{y}}{d\mathbf{x}} \tag{3}$$

Substituting the value of *y* and *dy dx* in equation (1), we get

$$\frac{\nu + x\frac{d\nu}{dx}}{\cos\nu} = \frac{\nu\cos\nu + 1}{\cos\nu}$$
 for 
$$x\frac{d\nu}{dx} = \frac{\nu\cos\nu + 1}{\cos\nu} - \nu$$
 for 
$$x\frac{d\nu}{dx} = \frac{1}{\cos\nu}$$
 for 
$$\cos\nu \text{ } d\nu = \frac{dx}{x}$$

$$
\begin{aligned}
\text{Therefore} \quad \qquad \int \cos \nu \, d\nu &= \int \frac{1}{\chi} \, d\chi
\end{aligned}
$$

or sin *v* = log | *x* | + log |C| or sin *v* = log |C*x*|

Replacing *v* by *y x* , we get

$$\sin\left(\frac{y}{x}\right) = \log|\mathbf{C}x|$$

which is the general solution of the differential equation (1).

**Example 12** Show that the differential equation 2 2 0 *x x y y y e dx y x e dy* + − = is homogeneous and find its particular solution, given that, *x* = 0 when *y* = 1.

**Solution** The given differential equation can be written as

$$\frac{d\mathbf{x}}{d\mathbf{y}} = \frac{2\pi e^{\frac{\mathbf{x}}{\mathbf{y}}} + \mathbf{y}}{2\mathbf{y}e^{\frac{\mathbf{x}}{\mathbf{y}}}} \qquad \dots \qquad \bigvee\_{\mathbf{y} \in \mathbb{R}^{n}} \tag{1}$$

$$\text{Let } \overbrace{\begin{array}{c} \text{F}(\mathbf{x}, \mathbf{y}) = \frac{2\,\text{xe}^{\mathbf{y}} \,\,\,\,\,\text{ye}}{\text{2}\,\text{ye}^{\mathbf{y}} \\ \text{2}\,\text{ye}^{\mathbf{y}} \end{array}} \text{F}(\mathbf{x}, \mathbf{y}) = \begin{array}{c} \text{2xe}^{\mathbf{y}} \,\,\,\,\,\text{ye} \\ \text{2}\,\text{ye}^{\mathbf{y}} \end{array} \end{aligned}$$

*x*

$$\text{Then } \begin{aligned} \text{Then } \lambda &= \lambda \left( 2xe^{\frac{x}{y}} - y \right) \\ \lambda &= \lambda \left( 2xe^{\frac{x}{y}} - y \right) \\ \lambda &= \lambda \left( 2ye^{\frac{x}{y}} \right) \end{aligned} \text{Then } \begin{aligned} \lambda \left( 2xe^{\frac{x}{y}} - y \right) \\ \lambda \left( 2ye^{\frac{x}{y}} \right) \end{aligned}$$

Thus, F(*x*, *y*) is a homogeneous function of degree zero. Therefore, the given differential equation is a homogeneous differential equation.

To solve it, we make the substitution

$$
\boldsymbol{\omega} = \nu \boldsymbol{\gamma} \tag{2}
$$

Differentiating equation (2) with respect to *y*, we get

$$\frac{d\mathbf{x}}{d\mathbf{y}} = \nu + \mathbf{y}\frac{d\mathbf{v}}{d\mathbf{y}}$$

Substituting the value of and *dx x dy* in equation (1), we get

> *dv v y dy* + = 2 1 2 *v v v e e* −

> > 2 1 2

*e* − −

*v v v e*

*v*

*dv y dy* =

or

$$\text{or} \qquad \qquad \qquad \text{y} \\ \frac{d\text{v}}{d\text{y}} = -\frac{1}{2e^v}$$

$$\text{or} \qquad \qquad \qquad 2e^v \, d\nu = \frac{-d\text{yr}}{\text{yr}}$$

$$\text{or} \qquad \qquad \int 2e^v \cdot d\nu = -\int \frac{dy}{\gamma}$$

$$\text{or} \qquad \qquad \text{\textquotedblleft } e^v = -\log|y| + C$$

and replacing *v* by *x y* , we get

$$\mathcal{D}e^{\mathcal{V}} + \log \check{\mathbb{I}}\mathbf{y} = \mathbf{C} \quad \bigvee \tag{3}$$

Substituting *x* = 0 and *y* = 1 in equation (3), we get

*x*

$$2\ e^0 + \log|\operatorname{I}\operatorname{I}| = \operatorname{C} \implies \operatorname{C} = 2\ \text{I}$$

Substituting the value of C in equation (3), we get

$$\stackrel{\underline{\pi}}{2^{e^{\underline{\pi}}}+\log|\underline{\mathbf{y}}|} = 2$$

which is the particular solution of the given differential equation.

**Example 13** Show that the family of curves for which the slope of the tangent at any

$$\text{point } (\mathbf{x}, \mathbf{y}) \text{ on it is } \frac{\mathbf{x}^2 + \mathbf{y}^2}{2 \mathbf{x} \mathbf{y}}, \text{ is given by } \mathbf{x}^2 - \mathbf{y}^2 = c\mathbf{x}.$$

**Solution** We know that the slope of the tangent at any point on a curve is *dy dx* .

$$\text{Therefore, } \qquad \qquad \frac{\text{d}\mathbf{y}}{d\mathbf{x}} = \frac{\mathbf{x}^2 + \mathbf{y}^2}{2\mathbf{x}\mathbf{y}}$$

*dy dx* = 2 2 1 2 *y x y x* + ... (1)

or

## Clearly, (1) is a homogenous differential equation. To solve it we make substitution

*dv*

*dx*

2 1 2 *v v* +

2

1

|

|

$$\mathbf{y} = \nu \mathbf{x}$$

Differentiating *y* = *vx* with respect to *x*, we get

*dx*<sup>=</sup> *v x* +

> *dv v x*

*dx* + =

*dy*

or

$$
\alpha \frac{d\nu}{d\mathbf{x}} = \frac{1 - \nu}{2\nu}
$$

 = *dx x*

or

$$1 - \nu^2 \qquad \text{or} \qquad \frac{\nu}{\sqrt{\left(\frac{2\nu}{\nu^2}\right)}} \frac{1}{\nu} = -\frac{d\nu}{\nu}$$

2 2

*v dv*

$$\text{Therefore } \qquad \qquad \int \frac{\omega \mathbf{v}}{\left(\begin{array}{c} \mathbf{v}^2 \end{array} \right. \qquad \qquad \int \frac{\omega \mathbf{v}}{\left(\begin{array}{c} \mathbf{v} \end{array} \right.]} d\mathbf{v} = \text{--} \Big[\begin{array}{c} \frac{1}{\omega} \, d\mathbf{x} \\\\ \dots \end{array} \right.$$

2

2

*v*

- or log | *v* 2 – 1 | = – log | *x* | + log |C<sup>1</sup>
- or log |(*v*

 – 1) (*x*)| = log |C<sup>1</sup> or (*v* 2 – 1) *x* = ± C<sup>1</sup>

Replacing *v* by *y x* , we get

$$\left(\frac{\text{y}^2}{\text{x}^2} - 1\right)\text{x} = \pm \text{C}\_1$$
 
$$(\text{y}^2 - \text{x}^2) = \pm \text{C}\_1 \text{ x or } \text{x}^2 - \text{y}^2 = \text{C}\text{x}$$

# **EXERCISE 9.4**

In each of the Exercises 1 to 10, show that the given differential equation is homogeneous and solve each of them.

**1.** (*x* 2 + *xy*) *dy* = (*x* 2 + *y* 2 ) *dx* **2.** *x y y x* + ′ = **3.** (*x* – *y*) *dy* – (*x* + *y*) *dx* = 0 **4.** (*x* 2 – *y* 2 ) *dx* + 2*xy dy* = 0 **5.** 2 2 2 2 *dy x x y xy dx* = − + **6.** *x dy* – *y dx* = 2 2 *x y dx* + **7.** cos sin sin cos *y y y y x y y dx y x x dy x x x x* + = − **8.** sin 0 *dy <sup>y</sup> x y x dx x* − + = **9.** log 2 0 *<sup>y</sup> y dx x dy x dy x* <sup>+</sup> − = **10.**

For each of the differential equations in Exercises from 11 to 15, find the particular solution satisfying the given condition:

$$11. \quad (\text{x} + \text{y}) \text{ dy} + (\text{x} - \text{y}) \text{ dx} = 0; \text{ y} = 1 \text{ when } \text{x} = 1.$$

$$\text{12.} \quad \text{x}^2 \text{ } dy + (\text{xy} + \text{y}^2) \text{ } d\text{x} = 0; \text{ } \text{y} \neq 1 \text{ when } \text{x} = 1.$$

$$\mathbf{13.} \quad \left[ \text{x} \sin^2 \left( \frac{\mathbf{y}}{\mathbf{x}} \right) - \mathbf{y} \right] \\ \text{dx} + \mathbf{x} \, \mathbf{dy} = \mathbf{0}; \, \mathbf{y} = \frac{\pi}{4} \quad \text{when } \mathbf{x} = 1$$

$$\mathbf{14.} \quad \frac{d\mathbf{y}}{d\boldsymbol{\kappa}} - \frac{\mathbf{y}}{\boldsymbol{\kappa}} + \operatorname{cosec}\left(\frac{\mathbf{y}}{\boldsymbol{\kappa}}\right) = \mathbf{0} \text{ ; } \mathbf{y} = \mathbf{0} \text{ when } \boldsymbol{\kappa} = 1$$

$$\mathbf{15.} \quad 2\alpha \mathbf{y} + \mathbf{y}^2 - 2\boldsymbol{\alpha}^2 \frac{d\mathbf{y}}{d\boldsymbol{\alpha}} = \mathbf{0}; \text{ y = 2 when } \boldsymbol{\alpha} = 1$$

**16.** A homogeneous differential equation of the from *dx x <sup>h</sup> dy y* <sup>=</sup> can be solved by making the substitution.

$$\begin{array}{ccccc} \text{(A)} \ y = \nu \text{x} & \qquad \text{(B)} \ \nu = \text{yx} & \qquad \text{(C)} \ \text{ x} = \nu \text{y} & \qquad \text{(D)} \ \text{ x} = \nu \end{array}$$

**17.** Which of the following is a homogeneous differential equation?

$$(\mathbf{A}) \ (4\mathbf{x} + 6\mathbf{y} + \mathbf{S}) \ d\mathbf{y} - (3\mathbf{y} + 2\mathbf{x} + 4) \ d\mathbf{x} = 0$$

- (B) (*xy*) *dx* (*x* 3 + *y* 3 ) *dy* = 0
- (C) (*x* 3 + 2*y* 2 ) *dx* + 2*xy dy* = 0
- (D) *y* <sup>2</sup> *dx* + (*x* 2 – *xy* – *y* 2 ) *dy* = 0

**9.4.3** *Linear differential equations*

A differential equation of the from

$$\frac{d\mathbf{y}}{d\mathbf{x}} + \mathbf{P}\mathbf{y} = \mathbf{Q}$$

where, P and Q are constants or functions of *x* only, is known as a first order linear differential equation. Some examples of the first order linear differential equation are

$$\frac{d\mathbf{y}}{dx} + \mathbf{y} = \sin x$$

$$\frac{d\mathbf{y}}{dx} + \left(\frac{1}{x}\right)\mathbf{y} = e^x$$

$$\frac{d\mathbf{y}}{dx} + \left(\frac{\mathbf{y}}{x\log x}\right) = \frac{1}{x}$$

Another form of first order linear differential equation is

$$\frac{d\mathbf{x}}{dy} + \mathbf{P\_1}\mathbf{x} = \mathbf{Q\_1}$$

where, P<sup>1</sup> and Q<sup>1</sup> are constants or functions of *y* only. Some examples of this type of differential equation are

$$\frac{d\mathbf{x}}{dy} + \mathbf{x} = \cos y$$

$$\frac{d\mathbf{x}}{dy} + \frac{-2x}{y} = y^2 e^{-y}$$

To solve the first order linear differential equation of the type

$$\frac{d\mathbf{y}}{d\boldsymbol{\alpha}} + \mathbf{P}\mathbf{y} = \mathbf{Q} \tag{1}$$

Multiply both sides of the equation by a function of *x* say *g* (*x*) to get

*g*(*x*) *dy dx* + P.(*g*(*x*)) *y*<sup>=</sup> Q . *<sup>g</sup>* (*x*) ... (2)

Choose *g* (*x*) in such a way that R.H.S. becomes a derivative of *y* . *g* (*x*).

i.e. *g* (*x*) *dy dx* + P. *<sup>g</sup>*(*x*) *y*<sup>=</sup> *d dx* [*<sup>y</sup>* . *<sup>g</sup>* (*x*)]

or *g* (*x*)

$$\begin{array}{ll} \text{or} & \text{g} \left( \text{x} \right) \xrightarrow{\circ \text{\raisebox{-0.5ex}{ $\times$ }}} \text{P. g} \left( \text{x} \right) \text{ y} = \text{g} \left( \text{x} \right) \xrightarrow{\circ \text{\raisebox{-0.5ex}{ $\times$ }}} \text{y} \left( \text{x} \right) \\\\ \Rightarrow & \text{P. g} \left( \text{x} \right) = \text{g}^{\prime} \left( \text{x} \right) \end{array}$$

*dy*

or P = ( ) ( ) *g x g x* ′

Integrating both sides with respect to *x*, we get

$$\int \mathbf{P}d\mathbf{x} = \int \frac{\mathbf{g}'(\mathbf{x})}{\mathbf{g}(\mathbf{x})}d\mathbf{x}$$

*dy*

or <sup>P</sup>⋅*dx* ∫ = log (*g* (*x*))

> *e* ∫

or g (*x*) = <sup>P</sup> *dx*

On multiplying the equation (1) by *g*(*x*) = P *dx e* ∫ , the L.H.S. becomes the derivative of some function of *x* and *y*. This function *g*(*x*) = <sup>P</sup> *dx e* ∫ is called *Integrating Factor*

Substituting the value of *g* (*x*) in equation (2), we get

(I.F.) of the given differential equation.

=

=

*ye* <sup>P</sup>*dx* ∫

or

*dx* Integrating both sides with respect to *x*, we get

*d*

 = Q P .*e dx dx* <sup>∫</sup> ∫ or *<sup>y</sup>*<sup>=</sup> *e e dx* <sup>−</sup> *dx dx* ∫ ∫ <sup>+</sup> ∫ P P . . Q C

which is the general solution of the differential equation.

## **Steps involved to solve first order linear differential equation:**

- (i) Write the given differential equation in the form P Q *dy y dx* + = where P, Q are constants or functions of *x* only.
- (ii) Find the Integrating Factor (I.F) = .
- (iii) Write the solution of the given differential equation as

$$\text{y (I.F)} = \int \text{(Q} \times \text{I.F)} \, d\text{x} + \text{C}\_1$$

In case, the first order linear differential equation is in the form P Q 1 1 *dx x dy* + = ,

where, P<sup>1</sup> and Q<sup>1</sup> are constants or functions of *y* only. Then I.F = <sup>P</sup><sup>1</sup> *dy e* and the solution of the differential equation is given by

$$\text{ax} \ (\text{I.F}) = \int \left( \mathbf{Q}\_1 \times \text{I.F} \right) d\mathbf{y} + \underset{\leftrightarrow}{\text{C}}$$

**Example 14** Find the general solution of the differential equation cos *dy y x dx* − = . **Solution** Given differential equation is of the form

$$\frac{d\mathbf{y}}{dx} + \mathbf{P}\mathbf{y} = \mathbf{Q}, \text{ where } \mathbf{P} = -\mathbf{1} \text{ and } \mathbf{Q} = \cos x$$

Therefore I.F =

Multiplying both sides of equation by I.F, we get

 = *e* –*<sup>x</sup>* cos *x* or ( ) *dy <sup>x</sup> ye dx* − = *e* –*<sup>x</sup>* cos *x*

On integrating both sides with respect to *x*, we get

$$ye^{-x} = \int e^{-x} \cos x \, dx + \mathcal{C} \tag{1}$$
  $\text{Let } \qquad \mathcal{I} = \int e^{-x} \cos x \, dx$  
$$= \cos x \Big(\frac{e^{-x}}{-1}\Big) - \int (-\sin x) \left(-e^{-x}\right) \, dx$$

$$\begin{aligned} &= -\cos x \, e^{-x} - \left[ \sin x \, e^{-x} \, dx \right. \\ &= -\cos x \, e^{-x} - \left[ \sin x \, (-e^{-x}) - \int \cos x \, (-e^{-x}) \, dx \right] \\ &= -\cos x \, e^{-x} + \sin x \, e^{-x} - \int \cos x \, e^{-x} \, dx \\ \text{or} & \qquad \text{I} = -e^{-x} \cos x + \sin x \, e^{-x} - \text{I} \\ \text{or} & \qquad 2\text{I} = (\sin x - \cos x) \, e^{-x} \end{aligned}$$

$$\text{or} \qquad \qquad \qquad \qquad \qquad \text{I} = \frac{(\sin x - \cos x) \, e^{-x}}{2}$$

Substituting the value of I in equation (1), we get

$$ye^{-x} = \left(\frac{\sin x - \cos x}{2}\right)e^{-x} + \text{Cl}$$
 
$$\text{or}$$
 
$$\text{or}$$
 
$$\text{or}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$
 
$$\text{Use}$$

which is the general solution of the given differential equation.

**Example 15** Find the general solution of the differential equation <sup>2</sup> 2 ( 0) *dy x y x x dx* + = ≠ . **Solution** The given differential equation is

$$\begin{cases} \mathbf{x} \frac{\partial \mathbf{y}}{\partial \mathbf{x}} + 2\mathbf{y} = \mathbf{x}^2 \\\\ \mathbf{x} \frac{\partial \mathbf{x}}{\partial \mathbf{x}} = \mathbf{x}^2 \end{cases} \tag{1}$$

*x*

Dividing both sides of equation (1) by *x*, we get

$$\frac{dy}{dx} + \frac{2}{x}y' = x$$

which is a linear differential equation of the type P Q *dy y dx* + = , where 2 P *x* = and Q = *x*.

$$\text{So } \qquad \qquad \circ \stackrel{\circ}{\text{'I:F}} = \stackrel{\circ}{e^{\int\_{\infty}^{2} dx}} = e^{2\log x} = \stackrel{\circ}{e^{\log x^2}} = \stackrel{\circ}{\text{'I as } e^{\log f'(x)} = f'(x)} \text{ [}$$

Therefore, solution of the given equation is given by

$$\begin{aligned} \text{y} \quad \boldsymbol{\chi}^2 = \int \left( \boldsymbol{\chi} \right) \left( \boldsymbol{\chi}^2 \right) d\boldsymbol{\chi} + \mathbf{C} &= \int \boldsymbol{\chi}^3 d\boldsymbol{\chi} + \mathbf{C} \\ \text{or} \quad \mathbf{y} &= \frac{\boldsymbol{\chi}^2}{4} + \mathbf{C} \, \boldsymbol{\chi}^{-2} \end{aligned}$$

which is the general solution of the given differential equation.

**Example 16** Find the general solution of the differential equation *y dx* – (*x* + 2*y* 2 ) *dy* = 0. **Solution** The given differential equation can be written as

$$\frac{d\mathbf{x}}{dy} - \frac{\mathbf{x}}{y} = 2\mathbf{y}$$

This is a linear differential equation of the type P Q 1 1 *dx x dy* + = , where <sup>1</sup> 1 P *y* = − and

$$\text{Q}\_{\text{l}} = 2 \text{y}. \text{ Therefore } \text{ I.F} = e^{\int -\frac{1}{y} \, d\mathbf{y}} = e^{-\log y} = e^{\log(\text{y})^{-1}} = \frac{1}{y}$$

Hence, the solution of the given differential equation is

$$
\alpha \frac{1}{\mathcal{Y}} = \int (2\,\mathcal{Y}) \left(\frac{1}{\mathcal{Y}}\right) d\mathcal{Y} + \mathcal{C}
$$

$$
\frac{\alpha}{\mathcal{Y}} = \int (2d\mathbf{y})\_0 + \mathcal{C}
$$

= 2*y* + C

2 + C*y*

or

or

or *x* = 2*y*

which is a general solution of the given differential equation.

**Example 17** Find the particular solution of the differential equation

*x y*

$$\frac{dy}{dx} + y \cot x = 2x + x^2 \cot x \ (x \neq 0)$$

given that *y* = 0 when 2 *x* π = .

**Solution** The given equation is a linear differential equation of the type P Q *dy y dx* + = , where P = cot *x* and Q = 2*x* + *x* 2 cot *x.* Therefore

$$\text{I.F} = \,e^{\int \cot x \, dx} = e^{\log \sin x} = \sin x$$

Hence, the solution of the differential equation is given by *y* . sin *x* = ∫(2*x* + *x* 2 cot *x*) sin *x dx* + C

$$\begin{array}{ccc} \text{or} & \begin{array}{c} \text{y} \ \sin \ \text{x} = \int \end{array} \begin{array}{c} \text{2x} \ \sin \ x \ d\lambda + \int \lambda^2 \cos \ x \ d\lambda + \text{C} \end{array} \end{array}$$

$$\text{For } \sin x = \sin x \left(\frac{2\chi^2}{2}\right) - \int \cos x \left(\frac{2\chi^2}{2}\right) dx + \int \chi^2 \cos x \, dx + C$$

$$\text{or} \qquad \text{y} \\ \sin x = \int x^2 \sin x - \int x^2 \cos x \, dx + \int x^2 \cos x \, dx + \text{Cl}$$

$$\begin{array}{cccc}\text{or} & \begin{array}{c} \text{y } \sin \ \text{x} = \text{x}^2 \sin \ \text{x} + \text{C} & \begin{array}{c} \text{Constant} \end{array} \end{array} \end{array} \tag{1}$$

Substituting *y* = 0 and <sup>2</sup> *x* π = in equation (1), we get

$$0 = \left(\frac{\pi}{2}\right)^2 \sin\left(\frac{\pi}{2}\right) + C$$

2

4 − π

or C =

Substituting the value of C in equation (1), we get

$$y\sin x = \left(x^2 \sin x - \frac{\pi^2}{4}\right)$$
 
$$y = \frac{\pi^2}{x^2 - \frac{\pi^2}{4}} \left(\sin x \neq 0\right)$$

4 sin

*x*

which is the particular solution of the given differential equation.

**Example 18** Find the equation of a curve passing through the point (0, 1). If the slope of the tangent to the curve at any point (*x*, *y*) is equal to the sum of the *x* coordinate (abscissa) and the product of the *x* coordinate and *y* coordinate (ordinate) of that point.

**Solution** We know that the slope of the tangent to the curve is *dy dx* .

Therefore,

### *dy dx*<sup>=</sup> *<sup>x</sup>* + *xy dy xy dx* − = *x* ... (1)

or

This is a linear differential equation of the type P Q *dy y dx* + = , where P = – *x* and Q = *x*.

$$\text{Therefore,}\\
\begin{aligned}
\text{Therefore,} \quad \text{I.F}=e^{\int^{\left[-\infty\right]dx}}=e^{\frac{-\lambda^2}{2}}\\
\end{aligned}$$

Hence, the solution of equation is given by

$$\mathbf{y} \cdot e^{\frac{-\mathbf{x}^2}{2}} = \int (\mathbf{x}) \begin{pmatrix} \frac{-\mathbf{x}^2}{2} \\ e^{-\frac{\mathbf{x}^2}{2}} \end{pmatrix} d\mathbf{x} + \mathbf{C} \mathbf{C} \mathbf{} \tag{2}$$
  $\text{Let } \mathbf{I} = \int (\mathbf{x}) \, e^{\frac{-\mathbf{x}^2}{2}} \, d\mathbf{x}$ 

$$\text{Let } \frac{-\chi^2}{2} = t \text{, then } -\chi \text{ } d\chi = dt \text{ or } \chi \text{ } d\chi = -dt.$$

 Therefore, I = 2 – <sup>2</sup> *x t t e dt e e* − − = − = ∫

Substituting the value of I in equation (2), we get

$$\mathbf{y}\ e^{\frac{-\mathbf{x}^2}{2}} = \underline{\mathbf{-}}e^{\frac{-\mathbf{x}^2}{2}} + \mathbf{C} \qquad \text{e} \qquad \overset{\circ}{\underset{\mathbf{y}}{\overset{\circ}{\phantom{\frac{\cdot}{\cdot}}}}} \overset{\circ}{\underset{\mathbf{y}}{\overset{\circ}{\cdot}}} \tag{3}$$

$$\mathbf{y} = \underline{\mathbf{-}}\mathbf{1} + \mathbf{C}e^{\frac{-\mathbf{x}^2}{2}} \qquad \overset{\circ}{\underset{\mathbf{y}}{\overset{\circ}{\cdot}}} \tag{4}$$

or *y* =

Now (3) represents the equation of family of curves. But we are interested in finding a particular member of the family passing through (0, 1). Substituting *x* = 0 and *y* = 1 in equation (3) we get

$$1 = -1 + \mathcal{C} \dots \mathcal{e}^0 \quad \text{or} \quad \mathcal{C} = 2.$$

Substituting the value of C in equation (3), we get

$$\gamma = \frac{\omega}{-1 + 2\,e^{\frac{x^2}{2}}}$$

which is the equation of the required curve.

**EXERCISE 9.5**

For each of the differential equations given in Exercises 1 to 12, find the general solution:

$$\begin{aligned} \text{1.} \quad & \frac{d\mathbf{y}}{dx} + 2\mathbf{y} = \sin x & \text{2.} \quad \frac{d\mathbf{y}}{dx} + 3\mathbf{y} = e^{-2x} & \text{3.} \quad \frac{d\mathbf{y}}{dx} + \frac{\mathbf{y}}{x} = \mathbf{x}^2\\ \text{4.} \quad & \frac{d\mathbf{y}}{dx} + (\sec x)\mathbf{y} = \tan x \left(0 \le x < \frac{\pi}{2}\right) & \text{5.} \quad \cos^2 x \frac{d\mathbf{y}}{dx} + \mathbf{y} = \tan x \left(0 \le x < \frac{\pi}{2}\right) & \text{6.}\\ \text{6.} \quad & \mathbf{x} \frac{d\mathbf{y}}{dx} + 2\mathbf{y} = \mathbf{x}^2 \log x & \text{7.} \quad \mathbf{x} \log x \frac{d\mathbf{y}}{dx} + \mathbf{y} = \frac{2}{x} \log x \\ \text{8.} \quad & (1 + x^2) \text{ dy} + 2\mathbf{x} \mathbf{y} \, dx = \cot x \, dx \text{ (x \ne 0)} \end{aligned}$$

$$\mathbf{0}. \quad \mathbf{x} \frac{d\mathbf{y}}{d\mathbf{x}} + \mathbf{y} - \mathbf{x} + \mathbf{x}\mathbf{y} \cot \mathbf{x} = \mathbf{0} \ (\mathbf{x} \neq \mathbf{0}) \quad \mathbf{1} \mathbf{0}. \quad (\mathbf{x} + \mathbf{y}) \frac{d\mathbf{y}}{d\mathbf{x}} = \mathbf{1}$$

**11.** *y dx* + (*x* – *y* 2 ) *dy* = 0 **12.** <sup>2</sup> ( 3 ) ( 0) *dy x y y y dx* + = > .

For each of the differential equations given in Exercises 13 to 15, find a particular solution satisfying the given condition:

$$13. \quad \frac{d\mathbf{y}}{d\boldsymbol{\chi}} + 2\,\boldsymbol{\chi}\tan\boldsymbol{\chi} = \sin\boldsymbol{\chi};\,\,\mathbf{y} = \mathbf{0} \quad \text{when} \quad \boldsymbol{\chi} = \frac{\pi}{3}$$

$$14. \quad (1+\chi^2)\frac{d\mathbf{y}}{d\chi} + 2\chi\mathbf{y} = \frac{1}{1+\chi^2};\ \mathbf{y} = 0 \quad \text{when } \chi = 1$$

- **15.** 3 cot sin 2 ; 2 when 2 *dy y x x y x dx* π − = = =
- **16.** Find the equation of a curve passing through the origin given that the slope of the tangent to the curve at any point (*x*, *y*) is equal to the sum of the coordinates of the point.
- **17.** Find the equation of a curve passing through the point (0, 2) given that the sum of the coordinates of any point on the curve exceeds the magnitude of the slope of the tangent to the curve at that point by 5.

(C)

1 *x*

**18.** The Integrating Factor of the differential equation <sup>2</sup> 2 *dy x y x dx* − = is

$$\text{(A)}\ e$$

–*x*

(D) *x*

(B) *e* **19.** The Integrating Factor of the differential equation

–*y*

$$\begin{array}{ccccc} \text{(1-y}^2) \frac{d\mathbf{x}}{d\mathbf{y}} + \mathbf{y}\mathbf{x} \triangleq \text{(ay)} (-1 < \mathbf{y} < \mathbf{1}) & \text{is} \\\\ \text{(A)} \quad \frac{1}{\mathbf{y}^2 - 1} & \text{(B)} \quad \frac{1}{\sqrt{\mathbf{y}^2 - 1}} & \text{(C)} \quad \frac{1}{1 - \mathbf{y}^2} & \text{(D)} \quad \frac{1}{\sqrt{1 - \mathbf{y}^2}} \end{array}$$

# *Miscellaneous Examples*

**Example 19** Verify that the function *y* = *c* 1 *e ax* cos *bx* + *c* 2 *e ax* sin *bx,* where *c* 1 , *c* 2 are arbitrary constants is a solution of the differential equation

$$\frac{d^2\mathbf{y}}{d\mathbf{x}^2} - 2a\frac{d\mathbf{y}}{d\mathbf{x}} + \left(a^2 + b^2\right)\mathbf{y} = 0$$

## **Solution** The given function is

$$y = e^{\alpha x} \left[ c\_1 \cos bx + c\_2 \sin bx \right] \tag{1}$$

Differentiating both sides of equation (1) with respect to *x*, we get

$$\frac{dy}{dx} = e^{ax} \left[ -bc\_1 \sin bx + b \, c\_2 \cos bx \right] + \left[ c\_1 \cos bx + c\_2 \sin bx \right] e^{ax} \cdot a$$

$$\frac{dy}{dx} = e^{ax} [(b \, c\_2 + a \, c\_1) \cos bx + (a \, c\_2 - b \, c\_1) \sin bx] \tag{10}$$

or

Differentiating both sides of equation (2) with respect to *x*, we get

$$\frac{d^2\mathbf{y}}{dx^2} = e^{ax} [(bc\_2 + ac\_1)(-b\sin b\mathbf{x}) + (ac\_2 - bc\_1)(b\cos b\mathbf{x})]$$

$$+ [(bc\_2 + ac\_1)\cos b\mathbf{x} + (ac\_2 - bc\_1)\sin b\mathbf{x}]e^{ax}a$$

$$= e^{ax} [(a^2c\_2 - 2abc\_1 - b^2c\_2)\sin b\mathbf{x} + (a^2c\_1 + 2abc\_2 - b^2c\_1)\cos b\mathbf{x}]$$

Substituting the values of 2 2 , *d y dy dx dx* and *y* in the given differential equation, we get

L.H.S. = <sup>2</sup> <sup>2</sup> <sup>2</sup> <sup>2</sup> 2 1 2 1 2 1 [ 2 )sin ( 2 )cos ] *ax e a c abc b c bx a c abc b c bx* − − + + − 2 1 2 1 2 [( )cos ( )sin ] *ax* − + + − *ae bc ac bx ac bc bx* 2 2 1 2 ( ) [ cos sin ] *ax* + + *a b e c bx c bx* + = ( ) 2 2 2 2 2 2 1 2 2 1 2 2 2 2 2 2 2 1 2 1 2 1 1 1 2 2 2 sin ( 2 2 2 )cos *ax a c abc b c a c abc a c b c bx e a c abc b c abc a c a c b c bx* − − − + + + + + − − − + + = [0 sin 0cos ] *ax e bx bx* × + = *e ax* × 0 = 0 = R.H.S.

Hence, the given function is a solution of the given differential equation.

**Example 20** Find the particular solution of the differential equation log 3 4 *dy x y dx* = + given that *y* = 0 when *x* = 0.

**Solution** The given differential equation can be written as

$$\frac{d\mathbf{y}}{d\mathbf{x}} = e^{(3\mathbf{x} + 4\mathbf{y})}$$

... (1)

or *dy dx* = *e* 3*x* . *e* 4*y*

Separating the variables, we get

4 *y dy e* = *e* 3*x dx*

*e dy* <sup>−</sup> ∫ <sup>=</sup>

Therefore <sup>4</sup> *<sup>y</sup>*

4 4 *y e* − − = 3 C 3 *x e* +

3*x e dx* ∫

or

or 4 *e* 3*x* + 3 *e* – 4*y* + 12 C = 0 ... (2)

Substituting *x* = 0 and *y* = 0 in (2), we get

$$4 + 3 + 12 \text{ C} = 0 \text{ or C} = \frac{4 \cdot 7}{12}$$

Substituting the value of C in equation (2), we get

4 *e* 3*x* + 3 *e* – 4*y* – 7 = 0,

which is a particular solution of the given differential equation.

**Example 21** Solve the differential equation

$$(\mathbf{x}\ \mathrm{d}\mathbf{y} - \widehat{\mathbf{y}\ \mathrm{d}\mathbf{x}})\mathbf{y}\ \sin\left(\frac{\mathbf{y}}{\mathbf{x}}\right) = \overset{\text{(\textbf{y})}}{\text{(\textbf{y})}}\mathbf{x} + \mathbf{x}\ \mathrm{d}\mathbf{y})\,\mathbf{x}\ \cos\left(\frac{\mathbf{y}}{\mathbf{x}}\right).$$

**Solution** The given differential equation can be written as

$$\begin{aligned} \left[ \text{xy} \sin \left( \frac{y}{\varkappa} \right) - \text{x}^2 \cos \left( \frac{y}{\varkappa} \right) \right] dy &= \left[ \text{xy} \cos \left( \frac{y}{\varkappa} \right) + \text{y}^2 \sin \left( \frac{y}{\varkappa} \right) \right] dx \\ \frac{dy}{dx} &= \frac{\text{xy} \cos \left( \frac{y}{\varkappa} \right) + \text{y}^2 \sin \left( \frac{y}{\varkappa} \right)}{\text{xy} \sin \left( \frac{y}{\varkappa} \right) - \text{x}^2 \cos \left( \frac{y}{\varkappa} \right)} \end{aligned}$$

or

Dividing numerator and denominator on RHS by *x* 2 , we get

$$\frac{d\mathbf{y}}{d\mathbf{x}} = \frac{\frac{\mathbf{y}}{\mathbf{x}}\cos\left(\frac{\mathbf{y}}{\mathbf{x}}\right) + \left(\frac{\mathbf{y}^2}{\mathbf{x}^2}\right)\sin\left(\frac{\mathbf{y}}{\mathbf{x}}\right)}{\frac{\mathbf{y}}{\mathbf{x}}\sin\left(\frac{\mathbf{y}}{\mathbf{x}}\right) - \cos\left(\frac{\mathbf{y}}{\mathbf{x}}\right)}\tag{11}$$

Clearly, equation (1) is a homogeneous differential equation of the form *dy y g dx x* <sup>=</sup> . To solve it, we make the substitution

*y* = *vx* ... (2) or *dy dx*<sup>=</sup> *dv v x dx* +

$$\text{or} \qquad \begin{aligned} \stackrel{\cdot}{\nu} + \stackrel{\cdot}{\nu} \frac{d\nu}{d\chi} &= \frac{\nu \cos \nu + \nu^2 \sin \nu}{\nu \sin \nu - \cos \nu} \end{aligned}$$

(using (1) and (2))

... (3)

$$\text{or} \qquad \qquad \qquad \times \frac{d\boldsymbol{\nu}}{d\boldsymbol{\chi}} = \frac{2\nu \cos \nu}{\nu \sin \nu - \cos \nu}$$

$$\text{or} \qquad \left(\frac{\nu \sin \nu - \cos \nu}{\nu \cos \nu}\right) d\nu = \frac{2 \, d\nu}{\times}$$

$$\text{Therefore } \qquad \int \left( \frac{\nu \sin \nu - \cos \nu}{\nu \cos \nu} \right) d\nu = \mathcal{Q} \Big[ \frac{1}{x\_{\beta}} d\mu \Big]$$

$$\text{or} \qquad \int \tan\nu \,d\nu - \int\_{\frac{1}{\lambda}\nu}^{\frac{1}{\lambda}} d\nu = 2 \int \frac{1}{\varkappa} \,d\varkappa$$

$$\text{or} \qquad \qquad \log|\sec\nu| - \log|\nu| = 2\log|\dot{\kappa}| + \log|\mathbf{C}\_1|$$

or <sup>2</sup> sec log *<sup>v</sup> v x* = log |C<sup>1</sup>

$$\text{or} \qquad \qquad \qquad \qquad \lor \quad \stackrel{\mathbf{sec}\,\mathbf{v}}{\text{v}\,\mathbf{x}^2} = \pm \mathbf{C}\_1$$

Replacing *v* by *y x* in equation (3), we get

$$\frac{\sec\left(\frac{y}{x}\right)}{\left(\frac{y}{x}\right)(\alpha^2)} = \text{C where, C = \pm C\_1}$$
 
$$\text{or}$$
 
$$\sec\left(\frac{y}{x}\right) = \text{C} \text{ xy}$$

|

which is the general solution of the given differential equation.

**Example 22** Solve the differential equation

(tan–1*y* – *x*) *dy* = (1 + *y* 2 ) *dx.*

**Solution** The given differential equation can be written as

$$\frac{d\mathbf{x}}{d\mathbf{y}} + \frac{\mathbf{x}}{1 + \mathbf{y}^2} = \frac{\tan^{-1}\mathbf{y}}{1 + \mathbf{y}^2} \tag{1}$$

Now (1) is a linear differential equation of the form P<sup>1</sup> *dx dy* + *x* = Q<sup>1</sup> ,

$$\text{where,}\qquad \mathbf{P\_{\cdot}} = \frac{1}{1+\mathbf{y}^{2}} \text{ and } \mathbf{Q\_{l}} = \frac{\tan^{-1}\mathbf{y}}{1+\mathbf{y}^{2}}\cdot\mathbf{s}$$

$$\text{Therefore, } \qquad \text{I.F} = \begin{cases} \frac{1}{1+\mathbf{y}^2} \,\mathrm{dy} \\ e^{\tan^{-1}\mathbf{y}} \end{cases} = e^{\tan^{-1}\mathbf{y}}$$

Thus, the solution of the given differential equation is

$$\int\_{\mathbf{x}} \mathbf{x} e^{i\mathbf{n}^{-1}\cdot\mathbf{y}} = \int \left(\frac{\tan^{-1}\mathbf{y}}{1+\mathbf{y}^2}\right) e^{i\mathbf{n}^{-1}\cdot\mathbf{y}} d\mathbf{y} + \mathbf{C} \tag{10.10}$$

$$\text{Let } \qquad \text{I} = \int \left( \frac{\tan^{-1} \text{y}}{1 + \text{y}^2} \right) e^{\tan^{-1} \text{y}} \, d\text{y}$$

Substituting tan–1 *y* = *t* so that <sup>2</sup> 1 1 *dy dt y* <sup>=</sup> <sup>+</sup> , we get

$$\mathbf{I} = \int t \, e^t dt = t \, e^t - \begin{bmatrix} 1 & e^t \ d t = t \ e^t - e^t = e^t \ (t - 1) \end{bmatrix}$$

$$\text{or} \qquad \qquad \text{I} = \ e^{\tan^{-1}(\sqrt{\tan^{-1}}\text{y} - 1)}$$

Substituting the value of I in equation (2), we get

$$\text{l.x.}\,e^{\tan^{-1}y} = e^{\tan^{-1}y}(\tan^{-1}y - 1) + \text{Cl}\_2$$

or *x =* 1 1 tan (tan 1) C *<sup>y</sup> y e* − − − − +

which is the general solution of the given differential equation.

# *Miscellaneous Exercise on Chapter 9*

**1.** For each of the differential equations given below, indicate its order and degree (if defined).

$$\begin{aligned} \text{(i)} \quad &\frac{d^2 \mathbf{y}}{d\mathbf{x}^2} + 5\mathbf{x} \left(\frac{d\mathbf{y}}{d\mathbf{x}}\right)^2 - 6\mathbf{y} = \log \mathbf{x} \qquad &\text{(ii)} \quad \left(\frac{d\mathbf{y}}{d\mathbf{x}}\right)^3 - 4\left(\frac{d\mathbf{y}}{d\mathbf{x}}\right)^2 + 7\mathbf{y} = \sin \mathbf{x} \\\\ \text{(iii)} \quad &\frac{d^4 \mathbf{y}}{d\mathbf{x}^4} - \sin \left(\frac{d^3 \mathbf{y}}{d\mathbf{x}^3}\right) = 0 \end{aligned}$$

**2.** For each of the exercises given below, verify that the given function (implicit or explicit) is a solution of the corresponding differential equation.

$$\begin{aligned} \text{(i)} \quad &\text{xy} = a \; e^x + b \; e^{-x} + x^2 & \qquad : \; x \frac{d^2 \; y}{dx^2} + 2 \frac{d \mathbf{y}}{dx} - x \mathbf{y} + x^2 - 2 = 0 \\\\ \text{(ii)} \quad &\text{y} = e^x \; (a \; \cos x + b \; \sin x) \quad : \; \frac{d^2 \; y}{dx^2} - 2 \frac{d \mathbf{y}}{dx} + 2 \mathbf{y} = 0 \\\\ \text{(iii)} \quad &\mathbf{y} = x \sin 3x \quad : \; : \; \frac{d^2 \; y}{dx^2} + 9 \mathbf{y} - 6 \cos 3x = 0 \\\\ \text{(iv)} \quad &\mathbf{x}^2 = 2 \mathbf{y}^2 \log \mathbf{y} \quad : \; : \; (\mathbf{x}^2 + \mathbf{y}^2) \frac{d \mathbf{y}}{dx} - x \mathbf{y} = 0 \end{aligned}$$

- **3.** Prove that *x* 2 – *y* 2 = *c* (*x* 2 + *y* 2 ) 2 is the general solution of differential equation (*x* 3 – 3*x y*<sup>2</sup> ) *dx* = (*y* 3 – 3*x* <sup>2</sup>*y*) *dy*, where *c* is a parameter.
- **4.** Find the general solution of the differential equation 2 2 1 0 1 *dy y dx x* − + = − .
- **5.** Show that the general solution of the differential equation 2 2 1 0 1 *dy y y dx x x* + + + = + + is given by (*x* + *y* + 1) = A (1 – *x* – *y* – 2*xy*), where A is parameter.
- **6.** Find the equation of the curve passing through the point 0, 4 π whose differential equation is sin *x* cos *y dx* + cos *x* sin *y dy* = 0.
- **7.** Find the particular solution of the differential equation (1 + *e* 2*x* ) *dy* + (1 + *y* 2 ) *e x dx* = 0, given that *y* = 1 when *x* = 0.
- **8.** Solve the differential equation <sup>2</sup> ( 0) *x x y y y e dx x e y dy y* = + ≠ .

- **9.** Find a particular solution of the differential equation (*x y*) (*dx* + *dy*) = *dx dy,* given that *y* = –1, when *x* = 0. (Hint: put *x* – *y* = *t*)
- **10.** Solve the differential equation 2 1( 0) *x e y dx x x x dy* <sup>−</sup> − = ≠ .

**11.** Find a particular solution of the differential equation cot *dy y x dx* + = 4*x* cosec *x*

(*<sup>x</sup>* <sup>≠</sup> 0), given that *y* = 0 when <sup>2</sup> *x* π = .

**12.** Find a particular solution of the differential equation (*x* + 1) *dy dx* = 2 *<sup>e</sup>* –*y* – 1, given that *y* = 0 when *x* = 0.

**13.** The general solution of the differential equation 0 *y dx x dy y* − = is

$$\text{(A)}\quad \text{xy} = \text{C} \qquad \qquad \text{(B)}\quad \text{x} = \stackrel{\cdot}{\text{Cy}^2} \qquad \text{(C)}\quad \text{y} = \stackrel{\cdot}{\text{Cx}}^{\cdot} \qquad \qquad \text{(D)}\quad \text{y} = \text{Cx}^2$$

**14.** The general solution of a differential equation of the type P Q 1 1 *dx x dy* + = is

$$\begin{array}{ll} \text{(A)} \quad \text{y } e^{\int \mathrm{P\_{i}} \, d\mathbf{y}} = \int \Big( \mathbf{Q\_{i}} e^{\int \mathrm{P\_{i}} \, d\mathbf{y}} \Big) \, d\mathbf{y} + \mathbf{C} \\\\ \text{(B)} \quad \text{y } e^{\int \mathrm{P\_{i}} \, d\mathbf{x}} = \int \Big( \mathbf{Q\_{i}} e^{\int \mathrm{P\_{i}} \, d\mathbf{x}} \Big) \, d\mathbf{x} + \mathbf{C} \end{array}$$

(C) ( ) <sup>P</sup><sup>1</sup> <sup>P</sup><sup>1</sup> Q C <sup>1</sup> *dy dy x e e dy* ∫ ∫ <sup>=</sup> <sup>+</sup> ∫

$$(\mathbf{D}) \quad \propto e^{\int \mathbf{P}\_{\parallel} \, d\mathbf{x}} = \int \left( \mathbf{Q}\_{\parallel} e^{\int \mathbf{P}\_{\parallel} \, d\mathbf{x}} \right) \, d\mathbf{x} + \mathbf{C}\_{\perp}$$

**15.** The general solution of the differential equation *e x dy* + (*y e<sup>x</sup>* + 2*x*) *dx* = 0 is

(A) *x e<sup>y</sup>* + *x* 2 = C (B) *x e<sup>y</sup>* + *y* 2 = C (C) *y e<sup>x</sup>* + *x* 2 = C (D) *y e<sup>y</sup>* + *x* 2 = C

# *Summary*

- ® An equation involving derivatives of the dependent variable with respect to independent variable (variables) is known as a differential equation.
- ® Order of a differential equation is the order of the highest order derivative occurring in the differential equation.
- ® Degree of a differential equation is defined if it is a polynomial equation in its derivatives.
- ® Degree (when defined) of a differential equation is the highest power (positive integer only) of the highest order derivative in it.
- ® A function which satisfies the given differential equation is called its solution. The solution which contains as many arbitrary constants as the order of the differential equation is called a general solution and the solution free from arbitrary constants is called particular solution.
- ® Variable separable method is used to solve such an equation in which variables can be separated completely i.e. terms containing *y* should remain with *dy* and terms containing *x* should remain with *dx*.
- ® A differential equation which can be expressed in the form

( , ) or ( , ) *dy dx f x y g x y dx dy* = = where, *f* (*x*, *y*) and *g*(*x*, *y*) are homogenous

functions of degree zero is called a homogeneous differential equation.

® A differential equation of the form +P Q *dy y dx* = , where P and Q are constants or functions of *x* only is called a first order linear differential equation.

# *Historical Note*

One of the principal languages of Science is that of differential equations. Interestingly, the date of birth of differential equations is taken to be November, 11,1675, when Gottfried Wilthelm Freiherr Leibnitz (1646 - 1716) first put in black

and white the identity <sup>1</sup> <sup>2</sup> 2 *y dy y* <sup>=</sup> ∫ , thereby introducing both the symbols ∫ and *dy*.

Leibnitz was actually interested in the problem of finding a curve whose tangents were prescribed. This led him to discover the '*method of separation of variables*' 1691. A year later he formulated the '*method of solving the homogeneous* *differential equations of the first order*'. He went further in a very short time to the discovery of the '*method of solving a linear differential equation of the first-order*'. How surprising is it that all these methods came from a single man and that too within 25 years of the birth of differential equations!

In the old days, what we now call the 'solution' of a differential equation, was used to be referred to as 'integral' of the differential equation, the word being coined by James Bernoulli (1654 - 1705) in 1690. The word 'solution was first used by Joseph Louis Lagrange (1736 - 1813) in 1774, which was almost hundred years since the birth of differential equations. It was Jules Henri Poincare (1854 - 1912) who strongly advocated the use of the word 'solution' and thus the word 'solution' has found its deserved place in modern terminology. The name of the '*method of separation of variables*' is due to John Bernoulli (1667 - 1748), a younger brother of James Bernoulli.

Application to geometric problems were also considered. It was again John Bernoulli who first brought into light the intricate nature of differential equations. In a letter to Leibnitz, dated May 20, 1715, he revealed the solutions of the differential equation

$$x^2 \, \!\!\/ \!\/ \!\/ \!\/ = 2\text{Jy},$$

which led to three types of curves, viz., parabolas, hyperbolas and a class of cubic curves. This shows how varied the solutions of such innocent looking differential equation can be. From the second half of the twentieth century attention has been drawn to the investigation of this complicated nature of the solutions of differential equations, under the heading '*qualitative analysis of differential equations*'. Now-a-days, this has acquired prime importance being absolutely necessary in almost all investigations.

**—**v**—**