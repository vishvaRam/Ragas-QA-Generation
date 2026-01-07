![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

# **BINOMIALTHEOREM**

v*Mathematics is a most exact science and its conclusions are capable of absolute proofs.* **–** *C.P. STEINMETZ*v

## **7.1 Introduction**

126 MATHEMATICS

In earlier classes, we have learnt how to find the squares and cubes of binomials like *a* + *b* and *a* – *b*. Using them, we could evaluate the numerical values of numbers like (98)<sup>2</sup> = (100 – 2)<sup>2</sup> , (999)<sup>3</sup> = (1000 – 1)<sup>3</sup> , etc. However, for higher powers like (98)<sup>5</sup> , (101)<sup>6</sup> , etc., the calculations become difficult by using repeated multiplication. This difficulty was overcome by a theorem known as binomial theorem. It gives an easier way to expand (*a* + *b*) *n* , where *n* is an integer or a rational number. In this Chapter, we study binomial theorem for positive integral indices only.

![](_page_0_Picture_6.jpeg)

## **7.2 Binomial Theorem for Positive Integral Indices**

**Blaise Pascal (1623-1662)**

4

Let us have a look at the following identities done earlier:

$$\begin{array}{ll}(a+b)^{0} = 1 & a+b \neq 0\\(a+b)^{1} = a+b\\(a+b)^{2} = a^{2} + 2ab^{2} + b^{2}\\(a+b)^{3} = a^{3} + 3a^{2}b + 3ab^{2} + b^{3}\\(a+b)^{4} = (a+b)^{3}\ (a+b) = a^{4} + 4a^{3}b + 6a^{2}b^{2} + 4ab^{3} + b^{4}\end{array}$$

In these expansions, we observe that

- (i) The total number of terms in the expansion is one more than the index. For example, in the expansion of (*a + b*) 2 , number of terms is 3 whereas the index of (*a* + *b*) 2 is 2.
- (ii) Powers of the first quantity '*a*' go on decreasing by 1 whereas the powers of the second quantity '*b*' increase by 1, in the successive terms.
- (iii) In each term of the expansion, the sum of the indices of *a* and *b* is the same and is equal to the index of *a* + *b*.

We now arrange the coefficients in these expansions as follows (Fig 7.1):

| Fig 7.1 |  |  |  |  |  |  |  |  |  |  |
|---------|--|--|--|--|--|--|--|--|--|--|

Do we observe any pattern in this table that will help us to write the next row? Yes we do. It can be seen that the addition of 1's in the row for index 1 gives rise to 2 in the row for index 2. The addition of 1, 2 and 2, 1 in the row for index 2, gives rise to 3 and 3 in the row for index 3 and so on. Also, 1 is present at the beginning and at the end of each row. This can be continued till any index of our interest.

We can extend the pattern given in Fig 7.2 by writing a few more rows.

![](_page_1_Figure_5.jpeg)

## **Pascal's Triangle**

The structure given in Fig 7.2 looks like a triangle with 1 at the top vertex and running down the two slanting sides. This array of numbers is known as *Pascal's triangle*, after the name of French mathematician Blaise Pascal. It is also known as *Meru Prastara* by Pingla.

Expansions for the higher powers of a binomial are also possible by using Pascal's triangle. Let us expand (2*x* + 3*y*) 5 by using Pascal's triangle. The row for index 5 is

1 5 10 10 5 1 Using this row and our observations (i), (ii) and (iii), we get (2*x* + 3*y*) <sup>5</sup> = (2*x*) 5 + 5(2*x*) 4 (3*y*) + 10(2*x*) 3 (3*y*) 2 +10 (2*x*) 2 (3*y*) 3 + 5(2*x*)(3*y*) 4 +(3*y*) 5 = 32*x* 5 + 240*x* <sup>4</sup>y + 720*x* 3y 2 + 1080*x* 2*y* 3 + 810*xy*<sup>4</sup> + 243*y* 5 .

#### 128 MATHEMATICS

Now, if we want to find the expansion of (2*x* + 3*y*) <sup>12</sup>, we are first required to get the row for index 12. This can be done by writing all the rows of the Pascal's triangle till index 12. This is a slightly lengthy process. The process, as you observe, will become more difficult, if we need the expansions involving still larger powers.

We thus try to find a rule that will help us to find the expansion of the binomial for any power without writing all the rows of the Pascal's triangle, that come before the row of the desired index.

For this, we make use of the concept of combinations studied earlier to rewrite

the numbers in the Pascal's triangle. We know that ! C !( )! *n r n r n – r* = , 0 ≤ *r* ≤ *n* and *n* is a non-negative integer. Also, *<sup>n</sup>*C<sup>0</sup> = 1 = *<sup>n</sup>*C*<sup>n</sup>* The Pascal's triangle can now be rewritten as (Fig 7.3)

![](_page_2_Figure_5.jpeg)

**Fig 7.3 Pascal's triangle**

Observing this pattern, we can now write the row of the Pascal's triangle for any index without writing the earlier rows. For example, for the index 7 the row would be

> <sup>7</sup>C<sup>0</sup> <sup>7</sup>C<sup>1</sup> <sup>7</sup>C<sup>2</sup> <sup>7</sup>C<sup>3</sup> <sup>7</sup>C<sup>4</sup> <sup>7</sup>C<sup>5</sup> <sup>7</sup>C<sup>6</sup> <sup>7</sup>C7.

Thus, using this row and the observations (i), (ii) and (iii), we have

$$(a+b)^{\gamma} = {}^{\gamma}\mathbf{C}\_{0}a^{\gamma} + \,{}^{\gamma}\mathbf{C}\_{1}a^{\delta}b + \,{}^{\gamma}\mathbf{C}\_{2}a^{\delta}b^{2} + \,{}^{\gamma}\mathbf{C}\_{3}a^{4}b^{3} + \,{}^{\gamma}\mathbf{C}\_{4}a^{3}b^{4} + \,{}^{\gamma}\mathbf{C}\_{5}a^{2}b^{5} + \,{}^{\gamma}\mathbf{C}\_{6}ab^{6} + \,{}^{\gamma}\mathbf{C}\_{7}b^{7}$$

An expansion of a binomial to any positive integral index say *n* can now be visualised using these observations. We are now in a position to write the expansion of a binomial to any positive integral index.

...

*k* )

**7.2.1** *Binomial theorem for any positive integer n*,

$$(a+b)^{n} = \text{"C}\_{0}a^{n} + \text{"C}\_{1}a^{n-1}b + \text{"C}\_{2}a^{n-2}b^{2} + ... + \text{"C}\_{n-1}a.b^{n-1} + \text{"C}\_{n}b^{n}$$

**Proof** The proof is obtained by applying principle of mathematical induction.

Let the given statement be

P(*n*) : (*a* + *b*) *n* = *<sup>n</sup>*C<sup>0</sup> *a n* + *<sup>n</sup>*C<sup>1</sup> *a <sup>n</sup>*– 1*b* + *<sup>n</sup>*C<sup>2</sup> *a <sup>n</sup>*– 2*b* 2 + ...+ *<sup>n</sup>*C*n*–1*a*.*b <sup>n</sup>*– 1 + *<sup>n</sup>*C*<sup>n</sup> b n* For *n* = 1, we have P (1) : (*a* + *b*) 1 = <sup>1</sup>C<sup>0</sup> *a* 1 + <sup>1</sup>C<sup>1</sup> *b* 1 = *a* + *b* Thus, P (1) is true.

Suppose P (*k*) is true for some positive integer *k*, i.e.

$$(a+b)^{k} = {}^{k}\mathbf{C}\_{0}a^{k} + {}^{k}\mathbf{C}\_{1}a^{k-1}b + {}^{k}\mathbf{C}\_{2}a^{k-2}b^{2} + ... + {}^{k}\mathbf{C}\_{k}b^{k}$$

We shall prove that P(*k* + 1) is also true, i.e.,

$$\begin{aligned} (a+b)^{k+1} &= {}^{k+1}\mathbf{C}\_{0}a^{k+1} + {}^{k+1}\mathbf{C}\_{1}a\bar{b} \neq {}^{k+1}\mathbf{C}\_{2}a^{k-1}b^{2} + \dots + {}^{k+1}\mathbf{C}\_{k+1}b^{k+1} \\ \text{Now, } (a+b)^{k+1} &= (a+b)\ (a+b)^{k} \\ &= (a+b)\ ({}^{k}\mathbf{C}\_{0}a^{k} + {}^{k}\mathbf{C}\_{1}a^{k-1}b + {}^{k}\mathbf{C}\_{2}a^{k-2}b^{2} + \dots + {}^{k}\mathbf{C}\_{k-1}ab^{k-1} + {}^{k}\mathbf{C}\_{k}b^{k}) \\ &\quad \times \quad \times \quad \text{from (1)} \end{aligned}$$

$$\begin{aligned} \mathbf{J} &= \mathbf{^{k}C\_{0}}a^{k+1} + \mathbf{^{k}C\_{1}}a^{k}b + \mathbf{^{k}C\_{2}}a^{k-1}b^{2} + \dots + \mathbf{^{k}C\_{k-1}}a^{2}b^{k-1} + \mathbf{^{k}C\_{k}}ab^{k} + \mathbf{^{k}C\_{0}}ab^{k} \\ &+ \mathbf{^{k}C\_{1}}a^{k-1}b^{2} + \mathbf{^{k}C\_{2}}a^{k-2}b^{2} + \dots + \mathbf{^{k}C\_{k-1}}ab^{k} + \mathbf{^{k}C\_{k}}b^{k+1} \\ &\qquad \text{[by actual multiplication]} \end{aligned}$$

$$\begin{aligned} &= \,^k \mathbf{C}\_0 a^{k+1} + \left( ^k \mathbf{C}\_1 + ^k \mathbf{C}\_0 \right) a^k b + \left( ^k \mathbf{C}\_2 + ^k \mathbf{C}\_1 \right) a^{k-1} b^2 + \dots \\ &+ \left( ^k \mathbf{C}\_k + ^k \mathbf{C}\_{k-1} \right) a b^k + \,^k \mathbf{C}\_k b^{k+1} \qquad \text{[grouping like terms]} \\ &\equiv \,^{k+1} \mathbf{C}\_0 a^{k+1} + \,^{k+1} \mathbf{C}\_1 a^k b + \,^{k+1} \mathbf{C}\_2 a^{k-1} b^2 + \dots + \,^{k+1} \mathbf{C}\_k a b^k + \,^{k+1} \mathbf{C}\_{k+1} \, b^{k+1} \\ &\text{(by using } \,^{k+1} \mathbf{C}\_0 \text{–} \mathbf{I}\_r \text{ -} \,^k \mathbf{C}\_{r-1} = \,^{k+1} \mathbf{C}\_r \qquad \text{and} \quad \,^k \mathbf{C}\_k = \,^{k+1} \mathbf{C}\_{k+1}) \end{aligned}$$

Thus, it has been proved that P (*k* + 1) is true whenever P(*k*) is true. Therefore, by principle of mathematical induction, P(*n*) is true for every positive integer *n*.

We illustrate this theorem by expanding (*x* + 2)<sup>6</sup> :

$$\begin{aligned} \mathbf{x}^6 (\mathbf{x} + \mathbf{2})^6 &= \mathbf{^6C\_6} \mathbf{x}^6 + \mathbf{^6C\_1} \mathbf{x}^5 \mathbf{.2} + \mathbf{^6C\_2} \mathbf{x}^4 \mathbf{2}^2 + \mathbf{^6C\_3} \mathbf{x}^3 \mathbf{.2}^3 + \mathbf{^6C\_4} \mathbf{x}^4 + \mathbf{^6C\_5} \mathbf{x}^5 + \mathbf{^6C\_6} \mathbf{2}^6 \mathbf{. \tilde{x}} \\ &= \mathbf{x}^6 + 12\mathbf{x}^5 + 60\mathbf{x}^4 + 160\mathbf{x}^3 + 240\mathbf{x}^2 + 192\mathbf{x} + 64 \end{aligned}$$

Thus (*x* + 2)<sup>6</sup> = *x* 6 + 12*x* 5 + 60*x* 4 + 160*x* <sup>3</sup>+ 240*x* 2 + 192*x* + 64.

#### Reprint 2025-26

#### 130 MATHEMATICS

### **Observations**

**1.** The notation ∑<sup>=</sup> − *n k n kk k n a b* 0 C stands for

*<sup>n</sup>*C<sup>0</sup> *a nb* 0 + *<sup>n</sup>*C<sup>1</sup> *a <sup>n</sup>*–1*b* 1 + ...+ *<sup>n</sup>*C<sup>r</sup> *a n–rb r* + ...+*<sup>n</sup>*C*<sup>n</sup> a n–nb n* , where *b* <sup>0</sup>= 1 = *an–n* . Hence the theorem can also be stated as

$$(a+b)^{n} = \sum\_{k=0}^{n} \, ^{n}\mathbf{C}\_{k} \, a^{n-k} b^{k} \, .$$

- **2.** The coefficients *<sup>n</sup>*C*<sup>r</sup>* occuring in the binomial theorem are known as binomial coefficients.
- **3.** There are (*n*+1) terms in the expansion of (*a*+*b*) *n* , i.e., one more than the index.
- **4.** In the successive terms of the expansion the index of *a* goes on decreasing by unity. It is *n* in the first term, (*n*–1) in the second term, and so on ending with zero in the last term. At the same time the index of *b* increases by unity, starting with zero in the first term, 1 in the second and so on ending with *n* in the last term.
- **5.** In the expansion of (*a*+*b*) *n* , the sum of the indices of *a* and *b* is *n* + 0 = *n* in the first term, (*n* – 1) + 1 = *n* in the second term and so on 0 + *n* = *n* in the last term. Thus, it can be seen that the sum of the indices of *a* and *b* is *n* in every term of the expansion.

#### **7.2.2** *Some special cases* In the expansion of (*a* + *b*) *n* ,

(i) Taking *a* = *x* and *b* = – *y*, we obtain

$$\begin{aligned} (\mathbf{x} - \mathbf{y})^n &= [\mathbf{x} + (\mathbf{-y})]^n \\ &= \mathbf{^nT\_\eta \mathbf{x}^n} + \mathbf{^nT\_\mathbf{r} \mathbf{x}^{n-1}} (-\mathbf{y}) + \mathbf{^nT\_\mathbf{r} \mathbf{x}^{n-2}} (-\mathbf{y})^2 + \mathbf{^nT\_\mathbf{r} \mathbf{x}^{n-3}} (-\mathbf{y})^3 + \dots + \mathbf{^nT\_\mathbf{r} \mathbf{ (-y)}^n} \\ &= \mathbf{^nT\_\eta \mathbf{x}^n} - \mathbf{^nT\_\mathbf{r} \mathbf{x}^{n-1}} \mathbf{y} + \mathbf{^nT\_\mathbf{r} \mathbf{x}^{n-2}} \mathbf{y}^2 - \mathbf{^nT\_\mathbf{r} \mathbf{x}^{n-3}} \mathbf{y}^3 + \dots + (-1)^n \mathbf{^nT\_\mathbf{r} \mathbf{y}^n} \\ \text{s. } (\mathbf{x} - \mathbf{y})^n &= \mathbf{^nT\_\eta \mathbf{x}^n} + \mathbf{^nT\_\mathbf{r} \mathbf{x}^{n-1}} \mathbf{y} + \mathbf{^nT\_\mathbf{r} \mathbf{x}^{n-2}} \mathbf{y}^2 + \dots + (-1)^n \mathbf{^nT\_\mathbf{r} \mathbf{y}^n} \mathbf{y}^n \end{aligned}$$

Thus (*x*–*y*) = *<sup>n</sup>*C<sup>0</sup> *x* – *<sup>n</sup>*C<sup>1</sup> *x <sup>n</sup>*– 1 *y* + *<sup>n</sup>*C<sup>2</sup> *x <sup>n</sup>*– 2 *y* + ... + (–1)*<sup>n</sup> <sup>n</sup>*C*<sup>n</sup> y* Using this, we have (*x*–2*y*) 5 = <sup>5</sup>C<sup>0</sup> *x* 5 – <sup>5</sup>C<sup>1</sup> *x* <sup>4</sup>(2*y*) + <sup>5</sup>C<sup>2</sup> *x* 3 (2*y*) 2 – <sup>5</sup>C<sup>3</sup> *x* 2 (2*y*) 3 <sup>5</sup>C4 *x*(2*y*) <sup>4</sup>– <sup>5</sup>C<sup>5</sup> (2*y*) 5

$$\mathbf{x} = \mathbf{x}^{\rm s} - 10\mathbf{x}^{\rm s}\mathbf{y} + 40\mathbf{x}^{\rm s}\mathbf{y}^{\rm z} - 80\mathbf{x}^{\rm z}\mathbf{y}^{\rm s} + 80\mathbf{x}\mathbf{y}^{\rm s} - 32\mathbf{y}^{\rm s}\mathbf{y}^{\rm z}$$

+ ... + *<sup>n</sup>*C*<sup>n</sup>*

*x n* +

(ii) Taking *a* = 1, *b* = *x*, we obtain

*<sup>n</sup>* = *<sup>n</sup>*C<sup>0</sup>

+ *<sup>n</sup>*C<sup>1</sup>

*x* + *<sup>n</sup>*C<sup>2</sup> *x* 2 + *<sup>n</sup>*C<sup>3</sup> *x* 3

$$\begin{aligned} (\mathbf{1} + \mathbf{x})^{\mathbf{n}} &= \mathsf{''C}\_0 (\mathbf{1})^{\mathbf{n}} + \mathsf{''C}\_1 (\mathbf{1})^{\mathbf{n} - 1} \mathsf{x} + \mathsf{''C}\_2 (\mathbf{1})^{\mathbf{n} - 2} \mathsf{x}^2 + \dots + \mathsf{''C}\_n \mathsf{x}^n \\ &= \mathsf{''C}\_0 + \mathsf{''C}\_1 \mathsf{x} + \mathsf{''C}\_2 \mathsf{x}^2 + \mathsf{''C}\_3 \mathsf{x}^3 + \dots + \mathsf{''C}\_n \mathsf{x}^n \end{aligned}$$

Thus (1 + *x*)

In particular, for *x* = 1, we have

$$\mathbf{2}^{n} = \text{''C}\_{0} + \text{''C}\_{1} + \text{''C}\_{2} + \dots + \text{''C}\_{n}.$$

(iii) Taking *a* = 1, *b* = – *x,* we obtain

$$(1 - \varkappa)^{n} = \text{''C}\_{0} - \text{''C}\_{1}\varkappa + \text{''C}\_{2}\varkappa^{2} - \dots + (-1)^{n} \text{''C}\_{n}\varkappa^{n}$$

In particular, for *x* = 1, we get

$$\mathbf{0} = \mathbf{\tilde{C}\_0} - \mathbf{\tilde{c}C\_1} + \mathbf{\tilde{c}C\_2} - \dots + (-1)^{n} \mathbf{\tilde{c}C\_n}$$

**Example 1** Expand 4 <sup>2</sup> 3 *x x* <sup>+</sup> , *x* ≠<sup>0</sup>

**Solution** By using binomial theorem, we have

$$\begin{aligned} \mathbf{x}^2 + \frac{3}{\mathbf{x}} &= \mathbf{^4C\_0} \mathbf{x}^2 \mathbf{i} + \mathbf{^4C\_1} \mathbf{(x}^2 \mathbf{i})^3 \left(\frac{\mathbf{3}}{\mathbf{x}}\right) + \mathbf{^4C\_2} \mathbf{(x}^2 \mathbf{i}^2 \left(\frac{\mathbf{3}}{\mathbf{x}}\right)^2 + \mathbf{^4C\_3} \mathbf{(x}^2 \mathbf{i}\right) \left(\frac{\mathbf{3}}{\mathbf{x}}\right)^3 + \mathbf{^4C\_4} \left(\frac{\mathbf{3}}{\mathbf{x}}\right)^4 \\ &= \mathbf{x}^8 + 4 \mathbf{x}^6 \cdot \frac{\mathbf{3}}{\mathbf{x}} + 6 \mathbf{x}^4 \cdot \frac{\mathbf{9}}{\mathbf{x}^2} + 4 \mathbf{^4C\_2} \frac{27}{\mathbf{x}^3} + \frac{81}{\mathbf{x}^4} \\ &= \mathbf{x}^8 + 12 \mathbf{x}^5 + 54 \mathbf{x}^2 + \frac{108}{\mathbf{x}} + \frac{81}{\mathbf{x}^4} .\end{aligned}$$

**Example 2** Compute (98)<sup>5</sup> .

**Solution** We express 98 as the sum or difference of two numbers whose powers are easier to calculate, and then use Binomial Theorem.

$$\begin{aligned} \text{Write } 98 &= 100 - 2 \\ \text{Therefore, } (98)^\circ &= (100 - 2)^\circ \\ &= \,^5\text{C}\_0^\circ(100)^\circ - \,^5\text{C}\_1(100)^\circ 2 + \,^5\text{C}\_2(100)^\circ 2^2 \\ &\quad \times - \,^5\text{C}\_3(100)^2(2)^3 + \,^5\text{C}\_4(100)(2)^4 - \,^5\text{C}\_5(2)^5 \\ &= 10000000000 - 5 \times 100000000 \times 2 + 10 \times 1000000 \times 4 - 10 \times 10000 \times 2 \\ &\quad \times 8 + 5 \times 100 \times 16 - 32 \end{aligned}$$

= 10040008000 – 1000800032 = 9039207968.

**Example 3** Which is larger (1.01)<sup>1000000</sup> or 10,000?

**Solution** Splitting 1.01 and using binomial theorem to write the first few terms we have

$$(1.01)^{100000} = (1 + 0.01)^{1000000}$$

$$= {}^{1000000}\text{C}\_0 + {}^{1000000}\text{C}\_1(0.01) + \text{other positive terms}$$

$$= 1 + 1000000 \times 0.01 + \text{other positive terms}$$

$$= 1 + 10000 + \text{other positive terms}$$

$$> 10000$$

$$> 10000$$

$$\text{Hence} \qquad (1.01)^{1000000} > 10000$$

**Example 4** Using binomial theorem, prove that 6*<sup>n</sup>*–5*n* always leaves remainder 1 when divided by 25.

**Solution** For two numbers *a* and *b* if we can find numbers *q* and *r* such that *a* = *bq* + *r*, then we say that *b* divides *a* with *q* as quotient and *r* as remainder. Thus, in order to show that 6*<sup>n</sup>*– 5*n* leaves remainder 1 when divided by 25, we prove that 6 *<sup>n</sup>*– 5*n* = 25*k* + 1, where *k* is some natural number.

We have

$$(1+a)^{n} = \text{"C}\_{0} + \text{"C}\_{1}a + \text{"C}\_{2}a^{2} + \text{"C}\_{\dots} + \text{"C}\_{n}a^{n}$$

For *a* = 5, we get

$$(1+\mathfrak{S})^{n} = {}^{n}\mathbf{C}\_{0} + {}^{n}\mathbf{C}\_{1}\mathfrak{S} + {}^{n}\mathbf{C}\_{2}\mathfrak{S}^{2} + \dots + {}^{n}\mathbf{C}\_{n}\mathfrak{S}^{n}$$

i.e. (6)*<sup>n</sup>*

$$\text{i.e.} \qquad \qquad \mathsf{G}^{\circ}-\mathsf{S}\mathsf{n} = 1 + \mathsf{S}^{2} \left( \mathsf{\scriptscriptstyle{\mathsf{C}C}}\_{2} + \mathsf{\scriptscriptstyle{\mathsf{C}C}}\_{3} \mathsf{S} + \dots + \mathsf{\scriptscriptstyle{\mathsf{S}}^{\circ \circ 2}} \right)$$

. *<sup>n</sup>*C<sup>2</sup> + 5<sup>3</sup> . *n*C3

= 1 + 5*n* + 5<sup>2</sup>

$$\text{or} \qquad \mathsf{G}^{n} - \mathsf{S}n = \underset{\circ}{1} + \underset{\circ}{2}\underbrace{\mathsf{S}}\_{\circ} \left( \stackrel{\circ}{\mathsf{C}}\_{2} + \stackrel{\circ}{\mathsf{S}} \stackrel{\circ}{\mathsf{C}}\_{3} + \dots + \stackrel{\circ}{\mathsf{S}}^{n \cdot 2} \right)$$

or 6 *n* – 5*n* = 25*k*+1 where *k* = *<sup>n</sup>*C2 + 5 . *n*C3 + ... + 5*<sup>n</sup>*–2 .

This shows that when divided by 25, 6*<sup>n</sup>* – 5*n* leaves remainder 1.

**EXERCISE 7.1**

+ ... + 5*<sup>n</sup>*

Expand each of the expressions in Exercises 1 to 5.

$$1.\quad(1-2x)^5\qquad\qquad\qquad\qquad\qquad\qquad2.\quad\left(\frac{2}{x}-\frac{x}{2}\right)^5\qquad\qquad\qquad3.\quad(2x-3)^6$$

$$4. \quad \left(\frac{\text{x}}{3} + \frac{1}{\text{x}}\right)^{8} \qquad\qquad\qquad\qquad\text{s.}\quad\left(\text{x} + \frac{1}{\text{x}}\right)^{6}\text{)}$$

Using binomial theorem, evaluate each of the following:

- **6.** (96)<sup>3</sup> **7.** (102)<sup>5</sup> **8.** (101)<sup>4</sup>
- **9.** (99)<sup>5</sup>
- **10.** Using Binomial Theorem, indicate which number is larger (1.1)<sup>10000</sup>or 1000.
- **11.** Find (*a* + *b*) 4 – (*a* – *b*) 4 . Hence, evaluate <sup>4</sup> + )23( – 4 )2–3( .
- **12.** Find (*x* + 1)<sup>6</sup> + (*x* – 1)<sup>6</sup> . Hence or otherwise evaluate ( 2 + 1)<sup>6</sup> + ( 2 – 1)<sup>6</sup> .
- **13.** Show that 9*<sup>n</sup>*+1 8*n* 9 is divisible by 64, whenever *n* is a positive integer.
- **14.** Prove that ∑<sup>=</sup> = *n r nr n r* 0 3 4C .

## *Miscellaneous Exercise on Chapter 7*

**1.** If *a* and *b* are distinct integers, prove that *a* – *b* is a factor of *a n* – *b n* , whenever *n* is a positive integer.

[**Hint** write *a n* = (*a* – *b* + *b*) *n* and expand]

- **2.** Evaluate ( ) ( ) 6 6 3 2 3 2 + − − .
- **3.** Find the value of ( ) ( ) 4 4 2 2 2 2 *a a a a* + − + − − 1 1 .
- **4.** Find an approximation of (0.99)<sup>5</sup> using the first three terms of its expansion.

$$\textbf{5.}\quad\textbf{Expand using Binomial Theorem}\\
\left(1+\frac{\textbf{x}}{2}-\frac{\textbf{2}}{\textbf{x}}\right)^{4},\textbf{x}\neq\textbf{0}\dots$$

**6.** Find the expansion of (3*x* 2 – 2*ax* + 3*a* 2 ) 3 using binomial theorem.

## *Summary*

- ÆThe expansion of a binomial for any positive integral *n* is given by Binomial Theorem, which is (*a* + *b*) *n* = *<sup>n</sup>*C<sup>0</sup> *a n* + *<sup>n</sup>*C<sup>1</sup> *a <sup>n</sup>*– 1*b* + *<sup>n</sup>*C<sup>2</sup> *a <sup>n</sup>*– 2*b* 2 + ...+ *<sup>n</sup>*C*n* – 1*a*.*b <sup>n</sup>*– 1 + *<sup>n</sup>*C*<sup>n</sup> b n .*
- ÆThe coefficients of the expansions are arranged in an array. This array is called *Pascal's triangle*.

## *Historical Note*

The ancient Indian mathematicians knew about the coefficients in the expansions of (*x* + *y*) *n* , 0 ≤ *n* ≤ 7. The arrangement of these coefficients was in the form of a diagram called *Meru-Prastara*, provided by Pingla in his book *Chhanda shastra* (200B.C.). This triangular arrangement is also found in the work of Chinese mathematician Chu-shi-kie in 1303. The term binomial coefficients was first introduced by the German mathematician, Michael Stipel (1486-1567) in approximately 1544. Bombelli (1572) also gave the coefficients in the expansion of (*a* + *b*) *n* , for *n* = 1,2 ...,7 and Oughtred (1631) gave them for *n* = 1, 2,..., 10. The arithmetic triangle, popularly known as *Pascal's triangle* and similar to the *Meru-Prastara* of Pingla was constructed by the French mathematician Blaise Pascal (1623-1662) in 1665.

The present form of the binomial theorem for integral values of *n* appeared in *Trate du triange arithmetic*, written by Pascal and published posthumously in 1665.

**—** v **—**