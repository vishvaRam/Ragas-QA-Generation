![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

## v *All Mathematical truths are relative and conditional. — C.P. STEINMETZ* v

### **4.1 Introduction**

76 MATHEMATICS

In the previous chapter, we have studied about matrices and algebra of matrices. We have also learnt that a system of algebraic equations can be expressed in the form of matrices. This means, a system of linear equations like

$$\begin{aligned} a\_1 \ x + b\_1 \ y &= c\_1\\ a\_2 \ x + b\_2 \ y &= c\_2\\ \text{can be represented as } \begin{bmatrix} a\_1 & b\_1\\ a\_2 & b\_2 \end{bmatrix} \begin{bmatrix} \dot{x} \\ y\_1 \end{bmatrix} = \begin{bmatrix} c\_1\\ c\_2 \end{bmatrix}. \text{ Now, this is } \end{aligned}$$

system of equations has a unique solution or not, is determined by the number *a*<sup>1</sup> *b*2 – *a*2 *b*<sup>1</sup> . (Recall that if

1 1 2 2 *a b a b* ≠ or, *a*<sup>1</sup> *b*2 – *a*2 *b*<sup>1</sup> ≠ 0, then the system of linear equations has a unique solution). The number *a*<sup>1</sup> *b*2 – *a*2 *b*<sup>1</sup>

![](_page_0_Picture_8.jpeg)

**P.S. Laplace (1749-1827)**

which determines uniqueness of solution is associated with the matrix 1 1 2 2 A *a b a b* <sup>=</sup>

and is called the determinant of A or det A. Determinants have wide applications in Engineering, Science, Economics, Social Science, etc.

In this chapter, we shall study determinants up to order three only with real entries. Also, we will study various properties of determinants, minors, cofactors and applications of determinants in finding the area of a triangle, adjoint and inverse of a square matrix, consistency and inconsistency of system of linear equations and solution of linear equations in two or three variables using inverse of a matrix.

### **4.2 Determinant**

To every square matrix A = [*aij*] of order *n*, we can associate a number (real or complex) called determinant of the square matrix A, where *aij* = (*i*, *j*) th element of A. This may be thought of as a function which associates each square matrix with a unique number (real or complex). If M is the set of square matrices, K is the set of numbers (real or complex) and *f* : M → K is defined by *f* (A) = *k*, where A ∈ M and *k* ∈ K, then *f*(A) is called the determinant of A. It is also denoted by |A| or det A or ∆.

$$\text{If } \mathbf{A} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}, \text{ then determinant of } \mathbf{A} \text{ is written as } |\mathbf{A}| = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = \det(\mathbf{A})$$

*Remarks*

- (i) For matrix A, |A| is read as determinant of A and not modulus of A.
- (ii) Only square matrices have determinants.

### **4.2.1** *Determinant of a matrix of order one*

Let A = [*a* ] be the matrix of order 1, then determinant of A is defined to be equal to *a*

#### **4.2.2** *Determinant of a matrix of order two*

$$\begin{array}{cc} \textbf{Let} & \textbf{A} = \begin{bmatrix} a\_{11} & a\_{12} \\ a\_{21} & a\_{22} \end{bmatrix} \text{ be a matrix of order } 2 \times 2, \\\ & \begin{pmatrix} \cdot \\ \cdot \end{pmatrix} \end{array}$$

then the determinant of A is defined as:

$$\det(\mathbf{A}) = |\mathbf{A}| = \Delta = \begin{vmatrix} a\_{11} & a\_{12} \\ a\_{21} & a\_{22} \\ a\_{21} & a\_{22} \end{vmatrix} = a\_{11}a\_{22} - a\_{21}a\_{12}$$

**Example 1** Evaluate 2 4 –1 2 .

$$\text{Solution We have}\\
\begin{array}{ccc}
2 & 4 \\
-1 & 2
\end{array} = 2 \cdot \text{(2)} - 4 \cdot (-1) = 4 + 4 = 8.1
$$

$$\text{Example 2 Evaluate } \begin{vmatrix} \times & x+1 \\ x-1 & x \end{vmatrix}$$

**Solution** We have

$$\left| \begin{array}{c} \mathbf{x} \\ \mathbf{x} - \mathbf{1} \end{array} \right| = \mathbf{x} \left( \mathbf{x} \right) - \left( \mathbf{x} + \mathbf{1} \right) \left( \mathbf{x} - \mathbf{1} \right) \ = \mathbf{x}^2 - \left( \mathbf{x}^2 - \mathbf{1} \right) = \mathbf{x}^2 - \mathbf{x}^2 + 1 = 1$$

### **4.2.3** *Determinant of a matrix of order* **3 × 3**

Determinant of a matrix of order three can be determined by expressing it in terms of second order determinants. This is known as expansion of a determinant along a row (or a column). There are six ways of expanding a determinant of order

3 corresponding to each of three rows (R<sup>1</sup> , R<sup>2</sup> and R<sup>3</sup> ) and three columns (C<sup>1</sup> , C<sup>2</sup> and C3 ) giving the same value as shown below.

Consider the determinant of square matrix A = [*aij*] 3 × 3

$$\begin{array}{c} \text{i.e.,} \end{array} \qquad \begin{array}{c} \begin{vmatrix} a\_{11} & a\_{12} & a\_{13} \\ a\_{21} & a\_{22} & a\_{23} \\ a\_{31} & a\_{32} & a\_{33} \end{vmatrix} \end{array}$$

#### **Expansion along first Row (R<sup>1</sup> )**

**Step 1** Multiply first element *a*11 of R<sup>1</sup> by (–1)(1 + 1) [(–1)sum of suffixes in *<sup>a</sup>* <sup>11</sup>] and with the second order determinant obtained by deleting the elements of first row (R<sup>1</sup> ) and first column (C<sup>1</sup> ) of | A | as *a*<sup>11</sup> lies in R<sup>1</sup> and C<sup>1</sup> ,

$$\text{i.e.}\_{\text{-},\text{-}} \qquad \qquad (-1)^{\text{l}^{\text{-},\text{+}1}} a\_{\text{l}\text{l}} \begin{vmatrix} a\_{22} & a\_{23} \\ a\_{32} & a\_{33} \end{vmatrix}$$

**Step 2** Multiply 2nd element *a*12 of R<sup>1</sup> by (–1)1 + 2 [(–1)sum of suffixes in *<sup>a</sup>* <sup>12</sup>] and the second order determinant obtained by deleting elements of first row (R<sup>1</sup> ) and 2nd column (C<sup>2</sup> ) of | A | as *a*12 lies in R<sup>1</sup> and C<sup>2</sup> ,

$$\text{i.e.}\_{\text{-},\text{-}} \qquad \qquad (-1)^{\text{l}+2} \, a\_{\text{l}2} \left| \begin{matrix} a\_{21} & a\_{23} \\ a\_{31} & a\_{33} \end{matrix} \right| $$

**Step 3** Multiply third element *a*13 of R<sup>1</sup> by (–1)1 + 3 [(–1)sum of suffixes in *<sup>a</sup>* <sup>13</sup>] and the second order determinant obtained by deleting elements of first row (R<sup>1</sup> ) and third column (C<sup>3</sup> ) of | A | as *a*13 lies in R<sup>1</sup> and C<sup>3</sup> ,

$$\text{i.e.}\_{\text{-},\text{-}} \qquad \qquad (-1)^{1+3} \, a\_{1^3} \begin{vmatrix} a\_{21} & a\_{22} \\ a\_{31} & a\_{32} \end{vmatrix}$$

**Step 4** Now the expansion of determinant of A, that is, | A | written as sum of all three terms obtained in steps 1, 2 and 3 above is given by

$$\begin{aligned} \det A &= |\mathbf{A}| = (-1)^{1+1} \ a\_{11} \left| \begin{matrix} a\_{22} & a\_{23} \\ a\_{32} & a\_{33} \end{matrix} \right| + (-1)^{1+2} \ a\_{12} \left| \begin{matrix} a\_{21} & a\_{23} \\ a\_{31} & a\_{33} \end{matrix} \right| \\ &+ (-1)^{1+3} \ a\_{13} \left| \begin{matrix} a\_{21} & a\_{22} \\ a\_{31} & a\_{32} \end{matrix} \right| \\
\text{or} \\ |\mathbf{A}| &= a\_{11} \left( a\_{22} \ a\_{33} - a\_{32} a\_{23} \right) - a\_{12} \left( a\_{21} \ a\_{33} - a\_{31} a\_{23} \right) \\ &+ a\_{13} \left( a\_{21} \ a\_{32} - a\_{31} \ a\_{22} \right) \end{matrix} \right. \end{aligned}$$

$$\begin{aligned} &= a\_{11} \ a\_{22} \ a\_{33} - a\_{11} \ a\_{32} \ a\_{23} - a\_{12} \ a\_{21} \ a\_{33} + a\_{12} \ a\_{31} a\_{23} + a\_{13} \ a\_{21} \ a\_{32} \\ &- a\_{13} \ a\_{31} \ a\_{22} \end{aligned} \tag{1}$$

A**Note** We shall apply all four steps together.

#### **Expansion along second row** (**R<sup>2</sup>** )

$$|\mathbf{A}| = \begin{vmatrix} \mathbf{a}\_{11} & \mathbf{a}\_{12} & \mathbf{a}\_{13} \\ \mathbf{a}\_{21} & \mathbf{a}\_{22} & \mathbf{a}\_{23} \\ \mathbf{a}\_{31} & \mathbf{a}\_{32} & \mathbf{a}\_{33} \end{vmatrix}$$

Expanding along R<sup>2</sup> ,we get

$$\begin{aligned} |\mathbf{A}| &= (-\mathbf{l})^{2+1} a\_{21} \begin{vmatrix} a\_{12} & a\_{13} \\ a\_{32} & a\_{33} \end{vmatrix} + (-\mathbf{l})^{2+2} a\_{22} \begin{vmatrix} a\_{11} & a\_{13} \\ a\_{31} & a\_{33} \end{vmatrix} \end{aligned} $$
 
$$\begin{array}{c|cc} \cdot & & & a\_{11} & a\_{12} \end{array} \begin{vmatrix} a\_{11} & a\_{12} \end{vmatrix} \end{aligned} $$

2 3 11 12

+

$$\begin{aligned} &+ \left(-1\right)^{2+3} a\_{23} \left[\begin{array}{c} a\_{11} \\ a\_{21} \end{array}\right]\_{2} \\ &= -a\_{21} \left(a\_{12} \; a\_{33} - a\_{32} \; a\_{13}\right) + a\_{22} \left(a\_{11} \; a\_{33} - a\_{31} \; a\_{13}\right) \\ &- a\_{23} \left(a\_{11} \; a\_{32} + a\_{31} \; a\_{12}\right) \\ \mid \mathbf{A} \mid = -a\_{21} \; a\_{12} \; a\_{33} + a\_{21} \; a\_{32} \; a\_{13} + a\_{22} \; a\_{11} \; a\_{33} - a\_{22} \; a\_{31} \; a\_{13} - a\_{23} \; a\_{11} \; a\_{32} \\ &+ a\_{23} \; a\_{31} \; a\_{12} \\ &= a\_{11} \; a\_{22} \; a\_{33} - a\_{11} \; a\_{23} \; a\_{32} - a\_{12} \; a\_{21} \; a\_{33} + a\_{12} \; a\_{23} \; a\_{31} + a\_{13} \; a\_{21} \; a\_{32} \\ &- a\_{13} \; a\_{31} \; a\_{22} \end{aligned} \tag{21}$$

**Expansion along first Column (C<sup>1</sup> )**

$$|\mathbf{A}| = \begin{vmatrix} a\_{11} & a\_{12} & a\_{13} \\ a\_{21} & a\_{22} & a\_{23} \\ a\_{31} & a\_{32} & a\_{33} \end{vmatrix}$$

By expanding along C<sup>1</sup> , we get

$$\begin{aligned} |A\_{\mid}\rangle &= a\_{11} \left( -1 \right)^{1+1} \left| \begin{matrix} a\_{22} & a\_{23} \\ a\_{32} & a\_{33} \end{matrix} \right| + a\_{21} \left( -1 \right)^{2+1} \left| \begin{matrix} a\_{12} & a\_{13} \\ a\_{32} & a\_{33} \end{matrix} \right| \\ &+ a\_{31} \left( -1 \right)^{3+1} \left| \begin{matrix} a\_{12} & a\_{13} \\ a\_{22} & a\_{23} \end{matrix} \right| \\ &= a\_{11} \left( a\_{22} \ a\_{33} - a\_{23} \ a\_{32} \right) - a\_{21} \left( a\_{12} \ a\_{33} - a\_{13} \ a\_{32} \right) + a\_{31} \left( a\_{12} \ a\_{23} - a\_{13} \ a\_{22} \right) \end{aligned}$$

$$\begin{aligned} |\mathbf{A}| &= a\_{11} \ a\_{22} \ a\_{33} - a\_{11} \ a\_{23} \ a\_{32} - a\_{21} \ a\_{12} \ a\_{33} + a\_{21} \ a\_{13} \ a\_{32} + a\_{31} \ a\_{12} \ a\_{23} \\ &- a\_{31} \ a\_{13} \ a\_{22} \\ &= a\_{11} \ a\_{22} \ a\_{33} - a\_{11} \ a\_{23} \ a\_{32} - a\_{12} \ a\_{21} \ a\_{33} + a\_{12} \ a\_{23} \ a\_{31} + a\_{13} \ a\_{21} \ a\_{32} \\ &- a\_{13} \ a\_{31} \ a\_{22} \end{aligned}$$

Clearly, values of |A| in (1), (2) and (3) are equal. It is left as an exercise to the reader to verify that the values of |A| by expanding along R<sup>3</sup> , C<sup>2</sup> and C<sup>3</sup> are equal to the value of |A| obtained in (1), (2) or (3).

Hence, expanding a determinant along any row or column gives same value.

#### *Remarks*

- (i) For easier calculations, we shall expand the determinant along that row or column which contains maximum number of zeros.
- (ii) While expanding, instead of multiplying by (–1)*<sup>i</sup>* + *<sup>j</sup>* , we can multiply by +1 or –1 according as (*i* + *j*) is even or odd.

$$\begin{aligned} \text{(iii)} \quad &\text{Let } \mathbf{A} = \begin{bmatrix} \mathbf{2} & \mathbf{2} \\ \mathbf{4} & \mathbf{0} \end{bmatrix} \text{ and } \mathbf{B} = \begin{bmatrix} \mathbf{1} & \mathbf{1} \\ \mathbf{2} & \mathbf{0} \end{bmatrix}, \text{ Then, it is easy to verify that } \mathbf{A} = \mathbf{2B}. \text{ Also, } \\ |\mathbf{A}| = \mathbf{0} - \mathbf{8} = -\mathbf{8} \text{ and } |\mathbf{B}| = \mathbf{0} - \mathbf{2} = -\mathbf{2}. \end{aligned} $$

Observe that, |A| = 4(– 2) = 2<sup>2</sup> |B| or |A| = 2*<sup>n</sup>* |B|, where *n* = 2 is the order of square matrices A and B.

In general, if A = *k*B where A and B are square matrices of order *n*, then | A| = *k n* | B |, where *n* = 1, 2, 3

**Example 3** Evaluate the determinant ∆ = 1 2 4 –1 3 0 4 1 0 .

**Solution** Note that in the third column, two entries are zero. So expanding along third column (C<sup>3</sup> ), we get

$$\begin{aligned} \Delta &= 4 \begin{vmatrix} -1 & 3 \\ 4 & 1 \end{vmatrix} - 0 \begin{vmatrix} 1 & 2 \\ 4 & 1 \end{vmatrix} + 0 \begin{vmatrix} 1 & 2 \\ -1 & 3 \end{vmatrix} \\ &= 4 \begin{pmatrix} -1 - 12 \end{pmatrix} - 0 + 0 \begin{pmatrix} -5 \end{pmatrix} \end{aligned}$$

**Example 4** Evaluate ∆ = 0 sin – cos –sin 0 sin cos –sin 0 α α α β α β . **Solution** Expanding along R<sup>1</sup> , we get

∆ = 0 sin – sin sin – sin 0 0 – sin – cos – sin 0 cos 0 cos – sin β α β α α α β α α β = 0 – sin α (0 – sin β cos α) – cos α (sin α sin β – 0) = sin α sin β cos α – cos α sin α sin β = 0 **Example 5** Find values of *x* for which 3 3 2 1 4 1 *x x* = . **Solution** We have 3 3 2 1 4 1 *x x* = i.e. 3 – *x* 2 = 3 – 8 i.e. *x* 2 = 8 Hence *x* = ± 2 2 **EXERCISE 4.1** Evaluate the determinants in Exercises 1 and 2. **1.** 2 4 –5 –1 **2.** (i) cos – sin sin cos θ θ θ θ (ii) 2 – 1 – 1 1 1 *x x x x x* + + + **3.** If A = 1 2 4 2 , then show that | 2A | = 4 | A |

$$\begin{array}{rcl} \text{4.} & \text{If} & \text{A} = \begin{bmatrix} \text{1} & \text{0} & \text{1} \\ \text{0} & \text{1} & \text{2} \\ \text{0} & \text{0} & \text{4} \end{bmatrix}, \text{ then show that } |\text{3 A}| = 2 \,\text{7} \,\big|\text{A} \mid \\\\ \text{4.} & \text{5} \end{array}$$

**5.** Evaluate the determinants

|     | 3 | –1 | –2 |      | 3 | – 4 | 5  |
|-----|---|----|----|------|---|-----|----|
| (i) | 0 | 0  | –1 | (ii) | 1 | 1   | –2 |
|     | 3 | –5 | 0  |      | 2 | 3   | 1  |

$$\begin{array}{c|c|c|c|c|c|c} \text{(iii)} & \mathbf{0} & \mathbf{1} & \mathbf{2} & & & & \\ \text{(iii)} & -\mathbf{1} & \mathbf{0} & -\mathbf{3} & & & & \text{(iv)} & \mathbf{0} & \mathbf{2} & -\mathbf{1} \\ & -\mathbf{2} & \mathbf{3} & \mathbf{0} & & & & & \mathbf{(iv)} & \mathbf{2} & -\mathbf{5} & \mathbf{0} \\ \text{(b)} & \text{If } \mathbf{A} = \begin{bmatrix} 1 & 1 & -2 \\ 2 & 1 & -3 \\ 5 & 4 & -9 \\ 5 & 4 & -9 \end{bmatrix}, \text{ find } |\mathbf{A}| \\\\ \text{7.} & \text{ Find values of } \mathbf{x}, \text{ if } \\\\ \text{(i)} & \begin{vmatrix} 2 & 4 \\ 5 & 1 \end{vmatrix} = \begin{vmatrix} 2x & 4 \\ 6 & x \end{vmatrix} & \text{(ii)} & \begin{vmatrix} 2 & 3 \\ 4 & 5 \end{vmatrix} = \begin{vmatrix} x & 3 \\ 2x & 5 \end{vmatrix} \\\\ \text{8.} & \text{ If } \begin{vmatrix} \mathbf{x} & 2 \\ 18 & x \end{vmatrix} = \begin{vmatrix} 6 & 2 \\ 18 & 6 \end{vmatrix}, \text{ then } x \text{ is equal to} \\\\ \text{(A)} & \begin{pmatrix} \mathbf{B} \end{pmatrix} \neq \mathbf{6} \qquad \mathbf{ (C)} = \mathbf{6}. & \text{(D)} \end{array}$$

### **4.3 Area of a Triangle**

In earlier classes, we have studied that the area of a triangle whose vertices are (*x*1 , *y*<sup>1</sup> ), (*x*<sup>2</sup> , *y*<sup>2</sup> ) and (*x*<sup>3</sup> , *y*<sup>3</sup> ), is given by the expression <sup>1</sup> 2 [*x*1 (*y*2 –*y*<sup>3</sup> ) + *x*<sup>2</sup> (*y*<sup>3</sup> –*y*<sup>1</sup> ) + *x*3 (*y*<sup>1</sup> –*y*<sup>2</sup> )]. Now this expression can be written in the form of a determinant as

$$
\Delta = \frac{1}{\mathcal{Z}} \begin{vmatrix}
\mathbf{x}\_i & \mathbf{y}\_i & 1 \\
\mathbf{x}\_i & \mathbf{y}\_i & 1 \\
\mathbf{x}\_i & \mathbf{y}\_i & 1
\end{vmatrix} \tag{1}
$$

#### *Remarks*

- (i) Since area is a positive quantity, we always take the absolute value of the determinant in (1).
- (ii) If area is given, use both positive and negative values of the determinant for calculation.
- (iii) The area of the triangle formed by three collinear points is zero.

**Example 6** Find the area of the triangle whose vertices are (3, 8), (– 4, 2) and (5, 1). **Solution** The area of triangle is given by

$$
\Delta = \frac{1}{2} \begin{vmatrix} \mathbf{3} & \mathbf{8} & 1 \\ -4 & \mathbf{2} & 1 \\ \mathbf{5} & 1 & 1 \end{vmatrix}
$$

$$\begin{aligned} &= \frac{1}{2} \left[ 3(2-1) - 8(-4-5) + 1(-4-10) \right] \\ &= \frac{1}{2} \left( 3 + 72 - 14 \right) = \frac{61}{2} \end{aligned}$$

**Example 7** Find the equation of the line joining A(1, 3) and B (0, 0) using determinants and find *k* if D(*k,* 0) is a point such that area of triangle ABD is 3sq units.

**Solution** Let P (*x, y*) be any point on AB. Then, area of triangle ABP is zero (Why?). So

$$\frac{1}{2} \begin{vmatrix} 0 & 0 & 1 \\ 1 & 3 & 1 \\ x & y & 1 \end{vmatrix} = 0$$
 
$$\text{This gives } \begin{aligned} \frac{1}{2}(y - 3x) &= 0 \text{ or } y = 3x, \\ \end{aligned}$$

which is the equation of required line AB.

Also, since the area of the triangle ABD is 3 sq. units, we have

$$
\frac{1}{2} \begin{vmatrix} 1 & 3 & 1 \\ 0 & 0 & 1 \\ k & 0 & 1 \end{vmatrix} = \pm 3
$$

This gives, <sup>3</sup> 3 2 − *k* = ± , i.e., *k* = ∓ 2.

**EXERCISE 4.2**

- **1.** Find area of the triangle with vertices at the point given in each of the following :
	- (i) (1, 0), (6, 0), (4, 3) (ii) (2, 7), (1, 1), (10, 8)
	- (iii) (–2, –3), (3, 2), (–1, –8)

```
2. Show that points
```
A (*a, b + c*), B (*b, c + a*), C (*c, a + b*) are collinear.

**3.** Find values of *k* if area of triangle is 4 sq. units and vertices are

(i) (*k*, 0), (4, 0), (0, 2) (ii) (–2, 0), (0, 4), (0, *k*)

- **4.** (i) Find equation of line joining (1, 2) and (3, 6) using determinants.
	- (ii) Find equation of line joining (3, 1) and (9, 3) using determinants.
- **5.** If area of triangle is 35 sq units with vertices (2, 6), (5, 4) and (*k*, 4). Then *k* is
	- (A) 12 (B) –2 (C) –12, –2 (D) 12, –2

### **4.4 Minors and Cofactors**

In this section, we will learn to write the expansion of a determinant in compact form using minors and cofactors.

**Definition 1** Minor of an element *aij* of a determinant is the determinant obtained by deleting its *i*th row and *j*th column in which element *aij* lies. Minor of an element *aij* is denoted by M*ij*.

*Remark* Minor of an element of a determinant of order *n*(*n* ≥ 2) is a determinant of order *n* – 1.

**Example 8** Find the minor of element 6 in the determinant 1 2 3 4 5 6 7 8 9 ∆ =

**Solution** Since 6 lies in the second row and third column, its minor M23 is given by

$$\mathbf{M}\_{23} = \begin{vmatrix} \mathbf{1} & \mathbf{2} \\ \mathbf{7} & \mathbf{8} \end{vmatrix} = \mathbf{8} - \mathbf{14} = -\mathbf{6} \text{ (obtained by deleting } \mathbf{R}\_2 \text{ and } \mathbf{C}\_3 \text{ in } \Delta).$$

**Definition 2** Cofactor of an element *aij* , denoted by A*ij* is defined by A*ij* = (–1)*<sup>i</sup>*+*<sup>j</sup>* M*ij* , where M*ij* is minor of *aij* .

**Example 9** Find minors and cofactors of all the elements of the determinant 1 –2 4 3

**Solution** Minor of the element *aij* is M*ij* Here *a*11 = 1. So M11 = Minor of *a*11= 3 M<sup>12</sup> = Minor of the element *a*12 = 4 M21 = Minor of the element *a*21 = –2 M22 = Minor of the element *a*22 = 1 Now, cofactor of *aij* is A*ij*. So A11 = (–1)1 + 1 M11 = (–1)<sup>2</sup> (3) = 3 A12 = (–1)1 + 2 M12 = (–1)<sup>3</sup> (4) = – 4 A21 = (–1)2 + 1 M21 = (–1)<sup>3</sup> (–2) = 2 A22 = (–1)2 + 2 M22 = (–1)<sup>4</sup> (1) = 1

**Example 10** Find minors and cofactors of the elements *a*11, *a*21 in the determinant

$$
\Delta = \begin{vmatrix} a\_{11} & a\_{12} & a\_{13} \\ a\_{21} & a\_{22} & a\_{23} \\ a\_{31} & a\_{32} & a\_{33} \end{vmatrix}
$$

**Solution** By definition of minors and cofactors, we have

$$\begin{aligned} \text{Minor of } a\_{11} = \mathbf{M}\_{11} &= \begin{vmatrix} a\_{22} & a\_{23} \\ a\_{32} & a\_{33} \end{vmatrix} = a\_{22} \ a\_{33} - a\_{23} \ a\_{32} \\ \text{Cofactor of } a\_{11} = \mathbf{A}\_{11} &= (-1)^{l+1} \quad \mathbf{M}\_{11} = a\_{22} \ a\_{33} - a\_{23} \ a\_{32} \\ \text{Minor of } a\_{21} = \mathbf{M}\_{21} &= \begin{vmatrix} a\_{12} & a\_{13} \\ a\_{32} & a\_{33} \end{vmatrix} = a\_{12} \ a\_{33} - a\_{13} a\_{32} \\ \text{Coefficient of } a\_{11} &= \begin{vmatrix} 1 & 0 \\ 0 & 0 \end{vmatrix} \end{aligned}$$

Cofactor of *a*21 = A21 = (–1)2+1 M21 = (–1) (*a*12 *a*33 – *a*13 *a*32) = – *a*12 *a*33 + *a*13 *a*<sup>32</sup>

*Remark* Expanding the determinant ∆, in Example 21, along R<sup>1</sup> , we have

$$\Delta = (-1)^{l+1} a\_{11} \begin{vmatrix} a\_{22} & a\_{23} \\ a\_{32} & a\_{33} \end{vmatrix} + (-1)^{l+2} a\_{12} \begin{vmatrix} a\_{21} & a\_{23} \\ a\_{31} & a\_{33} \end{vmatrix} + (-1)^{l+3} a\_{13} \begin{vmatrix} a\_{21} & a\_{22} \\ a\_{31} & a\_{32} \end{vmatrix}$$

= *a*11 A11 + *a*12 A12 + *a*13 A13, where A*ij* is cofactor of *aij*

 = sum of product of elements of R<sup>1</sup> with their corresponding cofactors

Similarly, ∆ can be calculated by other five ways of expansion that is along R<sup>2</sup> , R<sup>3</sup> , C1 , C<sup>2</sup> and C<sup>3</sup> .

Hence ∆ = sum of the product of elements of any row (or column) with their corresponding cofactors.

A**Note** If elements of a row (or column) are multiplied with cofactors of any other row (or column), then their sum is zero. For example,

$$\begin{aligned} \Delta &= a\_{11} \mathbf{A}\_{2} + a\_{12} \mathbf{A}\_{22} + a\_{13} \mathbf{A}\_{23} \\ &= a\_{11} \begin{vmatrix} -1 \\ a\_{12} \end{vmatrix} + a\_{12} \begin{vmatrix} -1 \\ a\_{21} \end{vmatrix} + a\_{12} \begin{vmatrix} -1 \\ a\_{21} \end{vmatrix} + a\_{13} \begin{vmatrix} -1 \\ a\_{31} \end{vmatrix} + a\_{13} \begin{vmatrix} -1 \\ a\_{31} \end{vmatrix} \begin{vmatrix} a\_{11} & a\_{12} \\ a\_{31} & a\_{32} \end{vmatrix} \\ &= \begin{vmatrix} a\_{11} & a\_{12} & a\_{13} \\ a\_{11} & a\_{12} & a\_{13} \\ a\_{31} & a\_{32} & a\_{33} \end{vmatrix} = 0 \text{ (since } \mathbf{R}\_{1} \text{ and } \mathbf{R}\_{2} \text{ are identical)} \\ &= \dots \end{aligned}$$

Similarly, we can try for other rows and columns.

**Example 11** Find minors and cofactors of the elements of the determinant

2 3 5 6 0 4 1 5 7 *– –* and verify that *a*<sup>11</sup> A31 + *a*12 A32 + *a*13 A33= 0

**Solution** We have M11 = 0 4 5 7*–* = 0 –20 = –20; A11 = (–1)1+1 (–20) = –20 M12 = 6 4 1 7*–* = – 42 – 4 = – 46; A12 = (–1)1+2 (– 46) = 46 M13 = 6 0 1 5 = 30 – 0 = 30; A13 = (–1)1+3 (30) = 30 M21 = 3 5 5 7 *– –* = 21 – 25 = – 4; A21 = (–1)2+1 (– 4) = 4 M22 = 2 5 1 7*–* = –14 – 5 = –19; A22 = (–1)2+2 (–19) = –19 M23 = 2 3 1 5 *–* = 10 + 3 = 13; A23 = (–1)2+3 (13) = –13 M31 = 3 5 0 4 *–* = –12 – 0 = –12; A31 = (–1)3+1 (–12) = –12 M32 = 2 5 6 4 = 8 – 30 = –22; A32 = (–1)3+2 (–22) = 22 and M33 = 2 3 6 0 *–* = 0 + 18 = 18; A33 = (–1)3+3 (18) = 18 Now *a*11 = 2, *a*12 = –3, *a*13 = 5; A31 = –12, A32 = 22, A33 = 18 So *a*11 A31 + *a*12 A32 + *a*13 A<sup>33</sup> = 2 (–12) + (–3) (22) + 5 (18) = –24 – 66 + 90 = 0

# **EXERCISE 4.3**

Write Minors and Cofactors of the elements of following determinants:

$$\begin{array}{ccccc|c} \text{1.} & \text{(i)} & \begin{vmatrix} 2 & -4 \\ 0 & 3 \end{vmatrix} & & \text{(ii)} & \begin{vmatrix} a & c \\ b & d \end{vmatrix} \\\\ \text{2.} & \text{(i)} & \begin{vmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{vmatrix} & & \text{(iii)} & \begin{vmatrix} 1 & 0 & 4 \\ 3 & 5 & -1 \\ 0 & 1 & 2 \end{vmatrix} \end{array}$$

**3.** Using Cofactors of elements of second row, evaluate ∆ = 5 3 8 2 0 1 1 2 3 . **4.** Using Cofactors of elements of third column, evaluate ∆ = 1 1 1 *x yz y zx z xy* .

$$\begin{array}{ll} \mathsf{5.} \quad \text{If } \Delta = \begin{vmatrix} a\_{11} & a\_{12} & a\_{13} \\ a\_{21} & a\_{22} & a\_{23} \\ a\_{31} & a\_{32} & a\_{33} \end{vmatrix} \text{ and } \mathsf{A}\_{ij} \text{ is } \mathsf{C} \text{ofactors of } a\_{ji} \text{, then value of } \Delta \text{ is given by} \\\\ \begin{array}{ll} \mathrm{(A)} \quad a\_{11}\mathrm{A}\_{31} + a\_{12}\mathrm{A}\_{32}^{-} + a\_{13}\mathrm{A}\_{33} & \text{(B)} \quad a\_{11}\mathrm{A}\_{11} + a\_{12}\mathrm{A}\_{21} + a\_{13}\mathrm{A}\_{31} \\ \mathrm{(C)} \quad a\_{21}\mathrm{A}\_{11} + a\_{22}\mathrm{A}\_{12} + a\_{23}\mathrm{A}\_{13} & \text{(D)} \quad a\_{11}\mathrm{A}\_{11} + a\_{21}\mathrm{A}\_{21} + a\_{31}\mathrm{A}\_{31} \end{array} \\\end{array}$$

### **4.5 Adjoint and Inverse of a Matrix**

In the previous chapter, we have studied inverse of a matrix. In this section, we shall discuss the condition for existence of inverse of a matrix.

To find inverse of a matrix A, i.e., A–1 we shall first define adjoint of a matrix.

### **4.5.1** *Adjoint of a matrix*

**Definition 3** The adjoint of a square matrix A = [*aij*] *n* × *n* is defined as the transpose of the matrix [A*ij*] *n* × *n* , where A*ij* is the cofactor of the element *aij* . Adjoint of the matrix A is denoted by *adj* A.

Let

$$\mathbf{A} = \begin{bmatrix} a\_{11} & a\_{12} & a\_{13} \\ a\_{21} & a\_{22} & a\_{23} \\ a\_{31} & a\_{32} & a\_{33} \end{bmatrix}$$

$$\begin{aligned} \text{Then} \qquad adj \mathbf{A} = \text{Transpose} \mathbf{of} \begin{bmatrix} \mathbf{A}\_{11} & \mathbf{A}\_{12} & \mathbf{A}\_{13} \\ \mathbf{A}\_{21} & \mathbf{A}\_{22} & \mathbf{A}\_{23} \\ \mathbf{A}\_{31} & \mathbf{A}\_{32} & \mathbf{A}\_{33} \end{bmatrix} = \begin{bmatrix} \mathbf{A}\_{11} & \mathbf{A}\_{21} & \mathbf{A}\_{31} \\ \mathbf{A}\_{12} & \mathbf{A}\_{22} & \mathbf{A}\_{32} \\ \mathbf{A}\_{13} & \mathbf{A}\_{23} & \mathbf{A}\_{33} \end{bmatrix} \end{aligned}$$

**Example 12** 2 3 Find A for A = 1 4 *adj* **Solution** We have A<sup>11</sup> = 4, A12 = –1, A21 = –3, A22 = 2 Hence *adj* A = 11 21 12 22 A A 4 –3 = A A –1 2 

*Remark* For a square matrix of order 2, given by

$$\mathbf{A} = \begin{bmatrix} a\_{11} & a\_{12} \\ a\_{21} & a\_{22} \end{bmatrix}$$

The *adj* A can also be obtained by interchanging *a*11 and *a*22 and by changing signs of *a*12 and *a*21, i.e.,

![](_page_12_Figure_6.jpeg)

We state the following theorem without proof.

**Theorem 1** If A be any given square matrix of order *n*, then

$$(\mathbf{A}(adj \mid \mathbf{A}) = (adj \mid \mathbf{A}) \,\mathbf{A} = \,\|\mathbf{A}\|\,\mathbf{I})$$

where I is the identity matrix of order *n*

#### **Verification**

$$\begin{array}{cccc} \text{Let} & \begin{bmatrix} a\_{11} & a\_{12} & a\_{13} \\ a\_{21} & a\_{22} & a\_{23} \\ a\_{31} & a\_{32} & a\_{33} \end{bmatrix}, \text{ then } adj & \text{A} = \begin{bmatrix} \mathbf{A}\_{11} & \mathbf{A}\_{21} & \mathbf{A}\_{31} \\ \mathbf{A}\_{12} & \mathbf{A}\_{22} & \mathbf{A}\_{32} \\ \mathbf{A}\_{13} & \mathbf{A}\_{23} & \mathbf{A}\_{33} \end{bmatrix} \end{array}$$

Since sum of product of elements of a row (or a column) with corresponding cofactors is equal to |A| and otherwise zero, we have

$$\mathbf{A} \ (adj \ \mathbf{A}) = \begin{bmatrix} |\mathbf{A}| & \mathbf{0} & \mathbf{0} \\ \mathbf{0} & |\mathbf{A}| & \mathbf{0} \\ \mathbf{0} & \mathbf{0} & |\mathbf{A}| \end{bmatrix} = \mathbf{\overset{\cdot}{|}\mathbf{A}|} \begin{bmatrix} 1 & \mathbf{0} & \mathbf{0} \\ \mathbf{0} & 1 & \mathbf{0} \\ \mathbf{0} & \mathbf{0} & 1 \end{bmatrix} = \mathbf{\overset{\cdot}{|}\mathbf{A}|} \mathbf{I} $$

Similarly, we can show (*adj* A) A = A I

Hence A (*adj* A) = (*adj* A) A = A I

**Definition 4** A square matrix A is said to be singular if A = 0.

For example, the determinant of matrix A = 1 2 4 8 is zero

Hence A is a singular matrix.

**Definition 5** A square matrix A is said to be non-singular if A ≠ 0

$$\text{Let } \mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}. \text{ Then } |\mathbf{A}| = \begin{vmatrix} 1 & 2 \\ 3 & 4 \end{vmatrix} = 4 - 6 = -2 \neq 0.$$

Hence A is a nonsingular matrix

We state the following theorems without proof.

**Theorem 2** If A and B are nonsingular matrices of the same order, then AB and BA are also nonsingular matrices of the same order.

**Theorem 3** The determinant of the product of matrices is equal to product of their respective determinants, that is, AB = A B , where A and B are square matrices of the same order

$$\text{Remark }\text{We know that } (\text{adj }\mathbf{A}) \text{ } \mathbf{A} = \begin{bmatrix} \mathbf{A} \\ \mathbf{A} \end{bmatrix} \text{ } \mathbf{I} = \begin{bmatrix} \mathbf{A} \\ \mathbf{0} & \|\mathbf{A}\| & \mathbf{0} \\ \mathbf{0} & \mathbf{0} & \|\mathbf{A}\| \end{bmatrix} \text{,} \begin{bmatrix} \mathbf{A} \\ \mathbf{A} \end{bmatrix} \neq \mathbf{0}$$

Writing determinants of matrices on both sides, we have

$$\left| (adj \, \mathbf{A}) \mathbf{A} \right| = \begin{vmatrix} |\mathbf{A}| & 0 & 0 \\ 0 & |\mathbf{A}| & 0 \\ 0 & 0 & |\mathbf{A}| \end{vmatrix}$$

$$\begin{array}{ccccc} \text{i.e.} & & & |(adj \text{ A})| \ |\text{A}| = \left| \text{A} \right|^{3} \begin{vmatrix} \mathbf{l} & \mathbf{0} & \mathbf{0} \\ \mathbf{0} & \mathbf{l} & \mathbf{0} \\ \mathbf{0} & \mathbf{0} & \mathbf{l} \end{vmatrix} & & & \text{(Why?)} \\ \end{array} \tag{\text{Why?}}$$

$$\text{i.e.}\\\qquad\qquad\qquad|(adj\ A)\mid |\mathcal{A}| = |\mathcal{A}|^\Box\text{ (1)}$$

$$\mathbf{i.e.}$$

i.e. |(*adj* A)| = | A | 2

In general, if A is *a* square matrix of order *n*, then |*adj*(A)| = |A| *n* – 1 .

**Theorem 4** A square matrix A is invertible if and only if A is nonsingular matrix. **Proof** Let A be invertible matrix of order *n* and I be the identity matrix of order *n*.

$$\text{Then, there exists a square matrix } \mathbf{B} \text{ of order } n \text{ such that } \mathbf{A}\mathbf{B} = \mathbf{B}\mathbf{A} = \mathbf{I}$$

$$\begin{array}{ccccc} \text{Now} & & \mathbf{AB} = \mathbf{I}. & \mathbf{So} \begin{vmatrix} \mathbf{AB} \end{vmatrix} = \begin{vmatrix} \mathbf{I} \end{vmatrix} & \text{or} & \begin{vmatrix} \mathbf{A} \end{vmatrix} \begin{vmatrix} \mathbf{B} \end{vmatrix} = \mathbf{I} & \begin{vmatrix} \mathbf{A} \end{vmatrix} \begin{vmatrix} \mathbf{B} \end{vmatrix} = \mathbf{I} & \begin{vmatrix} \mathbf{A} \end{vmatrix} \mathbf{B} \begin{vmatrix} \mathbf{E} \end{vmatrix} = \mathbf{A} \end{array}$$

This gives A ≠ 0. Hence A is nonsingular.

Conversely, let A be nonsingular. Then A ≠ 0

$$\text{Now } \qquad \text{A } (\text{adj } \mathbf{A}) = (\text{adj } \mathbf{A}) \mathbf{A} = \bigvee \mathbf{A} \big| \mathbf{I}^\top \tag{Theorem 1}$$

$$\text{for } \mathbf{A} = \mathbf{A} \left( \frac{1}{|\mathbf{A}|} adj \,\mathbf{A} \right) = \left( \frac{1}{|\mathbf{A}|} adj \,\mathbf{A} \right) \mathbf{A} = \widehat{\mathbf{I}}$$

$$\text{or} \qquad \mathbf{AB} = \widehat{\mathbf{BA}} = \overset{\circ}{\mathbf{I}}, \text{ where } \mathbf{B} = \frac{\overset{\circ}{\mathbf{I}} \mathbf{I}}{|\mathbf{A}^{\circ}|}\\\text{adj } \mathbf{A}$$

Thus A is invertible and A–1 = 1 A | A | *adj*

**Example 13** If A = 1 3 3 1 4 3 1 3 4 , then verify that A *adj* A = |A| I. Also find A–1 .

**Solution** We have A = 1 (16 – 9) –3 (4 – 3) + 3 (3 – 4) = 1 ≠ 0 Now A11 = 7, A12 = –1, A13 = –1, A21 = –3, A22 = 1,A23 = 0, A31 = –3, A32 = 0, A33 = 1

$$\begin{array}{ccc} \text{Therefore} & & & \begin{bmatrix} 7 & -3 & -3 \\ -1 & 1 & 0 \\ -1 & 0 & 1 \end{bmatrix} \end{array}$$

$$\begin{aligned} \text{Now} \qquad \mathbf{A} \begin{pmatrix} \operatorname{adj} \mathbf{A} \\ \end{pmatrix} &= \begin{bmatrix} 1 & 3 & 3 \\ 1 & 4 & 3 \\ 1 & 3 & 4 \end{bmatrix} \begin{bmatrix} 7 & -3 & -3 \\ -1 & 1 & 0 \\ -1 & 0 & 1 \end{bmatrix} \\ &= \begin{bmatrix} 7 - 3 - 3 & -3 + 3 + 0 & -3 + 0 + 3 \\ 7 - 4 - 3 & -3 + 4 + 0 & -3 + 0 + 3 \\ 7 - 3 - 4 & -3 + 3 + 0 & -3 + 0 + 4 \end{bmatrix} \\ &= \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = (1) \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = [\mathbf{A}], \mathbf{1} \\ \text{Also} \qquad \mathbf{A}^{-1} &= \frac{1}{|\mathbf{A}|} \begin{bmatrix} 7 & -3 & -3 \\ -1 & 1 & 0 \\ -1 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 7 & -3 & -3 \\ -1 & 1 & 0 \\ -1 & 0 & 1 \end{bmatrix} \\ &= \begin{bmatrix} 2 & 3 \end{bmatrix} \end{aligned}$$

**Example 14** If A = 2 3 1 2 and B 1 4 1 3 − <sup>=</sup> <sup>−</sup> <sup>−</sup> , then verify that (AB)–1 = B–1A–1 . **Solution** We have AB = 2 3 1 2 1 5 1 4 1 3 5 14 − − <sup>=</sup> − − <sup>−</sup> Since, AB = –11 ≠ 0, (AB)–1 exists and is given by

$$(\mathbf{AB})^{-1} = \frac{1}{\left| \mathbf{AB} \right|} \operatorname{adj}(\mathbf{AB}) = -\frac{1}{11} \begin{bmatrix} -14 & -5 \\ -5 & -1 \end{bmatrix}^{\top} = \frac{1}{11} \begin{bmatrix} 14 & 5 \\ 5 & 1 \end{bmatrix}^{\top}$$

Further, A = –11 ≠ 0 and B = 1 ≠ 0. Therefore, A–1 and B–1 both exist and are given by

$$\begin{aligned} \mathbf{A}^{-1} &= -\frac{1}{11} \begin{bmatrix} -4 & -3 \\ -1 & 2 \end{bmatrix}, \mathbf{B}^{-1} = \begin{bmatrix} 3 & 2 \\ 1 & 1 \end{bmatrix} \\ \text{Therefore} \quad \mathbf{B}^{-1} \mathbf{A}^{-1} &= -\frac{1}{11} \begin{bmatrix} 3 & 2 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} -4 & -3 \\ -1 & 2 \end{bmatrix} = -\frac{1}{11} \begin{bmatrix} -14 & -5 \\ -5 & -1 \end{bmatrix} = \frac{1}{11} \begin{bmatrix} 14 & 5 \\ 5 & 1 \end{bmatrix} \\ \text{Hence} \quad (\mathbf{AB})^{-1} &= \mathbf{B}^{-1} \mathbf{A}^{-1} \end{aligned}$$

**Example 15** Show that the matrix A = 2 3 1 2 satisfies the equation A<sup>2</sup> – 4A + I = O, where I is 2 × 2 identity matrix and O is 2 × 2 zero matrix. Using this equation, find A–1 .

$$\begin{aligned} \text{Solution We have } \mathbf{A}^2 = \mathbf{A} \cdot \mathbf{A} &= \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix} = \begin{bmatrix} 7 & 12 \\ 4 & 7 \end{bmatrix} \\ \text{Hence} \\ \mathbf{Hence} &= \mathbf{A}^2 - 4\mathbf{A} + \mathbf{I} = \begin{bmatrix} 7 & 12 \\ 4 & 7 \end{bmatrix} - \begin{bmatrix} 8 & 12 \\ 4 & 8 \end{bmatrix} + \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} = \mathbf{O} \\ \text{Now} \\ \mathbf{A}^2 - 4\mathbf{A} + \mathbf{I} = \mathbf{O} \end{aligned}$$

Therefore A A – 4A = – I

or A A (A–1) – 4 A A–1 = – I A–1 (Post multiplying by A–1 because |A| ≠ 0)

$$\text{or} \qquad \qquad \text{A (A A^{-l})} - 4\text{I} = -\text{A}^{-1}$$

1

−

A

or AI – 4I = – A–1

$$\begin{array}{rcl} \text{or} & \mathbf{A}^{-1} &=& \mathbf{4I} - \mathbf{A} \\ & & \begin{bmatrix} \mathbf{2} & \mathbf{3} \end{bmatrix} \begin{bmatrix} \mathbf{2} & \mathbf{3} \\ \mathbf{1} & \mathbf{2} \end{bmatrix} \end{array} = \begin{bmatrix} \mathbf{4} & \mathbf{0} \\ \mathbf{0} & \mathbf{4} \end{bmatrix} \begin{bmatrix} \mathbf{2}\_{\otimes} & \mathbf{3} \\ \mathbf{1} & \mathbf{2} \end{bmatrix} = \begin{bmatrix} \mathbf{2} & -\mathbf{3} \\ -\mathbf{1} & \mathbf{2} \end{bmatrix} \\\ \mathbf{1}\_{\circ} & \begin{bmatrix} \mathbf{2} & -\mathbf{3} \end{bmatrix} \begin{bmatrix} \mathbf{2} & \mathbf{3} \end{bmatrix} \end{array}$$

Hence

# 1 2 <sup>=</sup> <sup>−</sup>

**EXERCISE 4.4**

Find adjoint of each of the matrices in Exercises 1 and 2.

$$\begin{array}{cccc} \text{1.} & \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} & & \begin{pmatrix} 2 \\ & \end{pmatrix} \end{array} \qquad \begin{array}{ccc} \begin{bmatrix} 1 & -1 & 2 \\ 2 & 3 & 5 \\ -2 & 0 & 1 \end{bmatrix} \end{array}$$

Verify A (*adj* A) = (*adj* A) A = |A| I in Exercises 3 and 4

$$\begin{array}{cccc} \text{3.} & \begin{bmatrix} 2 & 3 \\ -4 & -6 \end{bmatrix} & & 4. \begin{bmatrix} 1 & -1 & 2 \\ 3 & 0 & -2 \\ 1 & 0 & 3 \end{bmatrix} \end{array}$$

Find the inverse of each of the matrices (if it exists) given in Exercises 5 to 11.

**5.** 2 2 4 3 − **6.** − − 1 5 3 2 **7.** 1 2 3 0 2 4 0 0 5 

**8.** 1 0 0 3 3 0 5 2 1− **9.** 2 1 3 4 1 0 7 2 1 − − **10.** 1 1 2 0 2 3 3 2 4 − − − **11.** 1 0 0 0 cos sin 0 sin cos α α α − α **12.** Let A = 3 7 2 5 and B = 6 8 7 9 . Verify that (AB)–1 = B–1 A–1 . **13.** If A = 3 1 −1 2 , show that A<sup>2</sup> – 5A + 7I = O. Hence find A–1 . **14.** For the matrix A = 3 2 1 1 , find the numbers *a* and *b* such that A<sup>2</sup> + *a*A + *b*I = O. **15.** For the matrix A = 1 1 1 1 2 3 2 1 3 − − Show that A<sup>3</sup>– 6A<sup>2</sup>+ 5A + 11 I = O. Hence, find A–1 . **16.** If A = 2 1 1 1 2 1 1 1 2 − − − − Verify that A<sup>3</sup> – 6A<sup>2</sup> + 9A – 4I = O and hence find A–1 **17.** Let A be a nonsingular square matrix of order 3 × 3. Then |*adj* A| is equal to (A) | A | (B) | A | 2 (C) | A | 3 (D) 3|A| **18.** If A is an invertible matrix of order 2, then det (A–1) is equal to (A) det (A) (B) 1 det (A) (C) <sup>1</sup> (D) <sup>0</sup>

### **4.6 Applications of Determinants and Matrices**

In this section, we shall discuss application of determinants and matrices for solving the system of linear equations in two or three variables and for checking the consistency of the system of linear equations.

**Consistent system** A system of equations is said to be *consistent* if its solution (one or more) exists.

**Inconsistent system** A system of equations is said to be *inconsistent* if its solution does not exist.

A**Note** In this chapter, we restrict ourselves to the system of linear equations having unique solutions only.

### **4.6.1** *Solution of system of linear equations using inverse of a matrix*

Let us express the system of linear equations as matrix equations and solve them using inverse of the coefficient matrix.

Consider the system of equations

$$\begin{aligned} a\_1 \ge + \, b\_1 \, \mathbf{y} + c\_1 \, \mathbf{z} &= \, d\_1\\ a\_2 \ge + \, b\_2 \, \mathbf{y} + c\_2 \, \mathbf{z} &= d\_2\\ a\_3 \ge + \, b\_3 \, \mathbf{y} + c\_3 \, \mathbf{z} &= d\_3\\ \text{Let } \mathbf{A} = \begin{bmatrix} a\_1 & b\_1 & c\_1\\ a\_2 & b\_2 & c\_2\\ a\_3 & b\_3 & c\_3 \end{bmatrix}, \mathbf{X} = \begin{bmatrix} \mathbf{x} \\ \mathbf{y} \\ \mathbf{z} \end{bmatrix} \text{ and } \mathbf{B} = \begin{bmatrix} d\_1\\ d\_2\\ d\_3 \end{bmatrix} \end{aligned}$$

Then, the system of equations can be written as, AX = B, i.e.,

| <br>a<br>1      | b<br>1 | c<br><br>1      | <br>x<br>           |   | <br>d<br>1        |       |
|------------------|--------|------------------|-----------------------|---|--------------------|--------|
| <br>a<br><br>2 | b<br>2 | <br>c<br><br>2 | <br><br>y<br><br> | = | <br>d<br><br>2   | <br> |
| <br>a<br><br>3 | b<br>3 | <br>c<br><br>3 | <br><br>z<br><br> |   | <br>d<br> <br>3 |       |

**Case I** If A is a nonsingular matrix, then its inverse exists. Now

|    | AX =<br>B           |                           |
|----|---------------------|---------------------------|
| or | A–1 (AX) =<br>A–1 B | (premultiplying by A–1)   |
| or | (A–1A) X =<br>A–1 B | (by associative property) |
| or | I X =<br>A–1 B      |                           |
| or | A–1 B<br>X =        |                           |

This matrix equation provides unique solution for the given system of equations as inverse of a matrix is unique. This method of solving system of equations is known as Matrix Method.

**Case II** If A is a singular matrix, then |A| = 0.

In this case, we calculate (*adj* A) B.

If (*adj* A) B ≠ O, (O being zero matrix), then solution does not exist and the system of equations is called inconsistent.

If (*adj* A) B = O, then system may be either consistent or inconsistent according as the system have either infinitely many solutions or no solution.

**Example 16** Solve the system of equations

$$\begin{aligned} 2x + 5y &= 1 \\ 3x + 2y &= 7 \end{aligned}$$

**Solution** The system of equations can be written in the form AX = B, where

$$\mathbf{A} = \begin{bmatrix} \mathbf{2} & \mathbf{5} \\ \mathbf{3} & \mathbf{2} \end{bmatrix}, \mathbf{X} = \begin{bmatrix} \mathbf{x} \\ \mathbf{y} \end{bmatrix} \text{and } \mathbf{B} = \begin{bmatrix} \mathbf{1} \\ \mathbf{7} \end{bmatrix}$$

 

Now, A = –11 ≠ 0, Hence, A is nonsingular matrix and so has a unique solution.

$$\begin{array}{cc} \text{Note that} \\\\ \begin{array}{c} \\\\ \end{array} \end{array} \qquad \begin{array}{c} \text{A}^{-1} = -\frac{1}{11} \begin{bmatrix} 2 & -5 \\ -3 & 2 \\ \end{bmatrix} \\\\ \begin{array}{c} \\\\ \end{array} \end{array} \begin{array}{c} \text{2.} \\ \begin{array}{c} \\ \\ \\ \end{array} \end{array} \begin{array}{c} \text{3.} \\ \begin{array}{c} \\ \\ \\ \end{array} \end{array} \begin{array}{c} \text{3.} \\ \begin{array}{c} \\ \\ \\ \end{array} \end{array} \begin{array}{c} \text{4.} \\ \begin{array}{c} \\ \\ \\ \\ \end{array} \begin{array}{c} \text{5.} \\ \\ \\ \end{array} \end{array} \begin{array}{c} \text{5.} \\ \begin{array}{c} \\ \\ \\ \\ \end{array} \begin{array}{c} \text{6.} \\ \\ \\ \end{array} \begin{array}{c} \text{7.} \\ \\ \end{array} \end{array} \begin{array}{c} \text{7.} \\ \text{8.} \\ \\ \text{9.} \\ \end{array} \begin{array}{c} \text{7.} \\ \text{8.} \\ \text{9.} \\ \end{array} \begin{array}{c} \text{8.} \\ \text{9.} \\ \\ \end{array} \begin{array}{c} \text{7.} \\ \text{8.} \\ \text{9.} \\ \text{10.} \\ \end{array} \end{array} \begin{array}{c} \text{7.} \\ \text{8.} \\ \text{11.} \\ \text{12.} \\ \text{13.} \\ \text{14.} \\ \text{15.} \\ \text{16.} \\ \text{17.} \\ \text{17.} \\ \text{18.} \\ \text{18.} \end{array}$$

$$\begin{aligned} \text{Therefore} \quad \mathbf{X} &= \mathbf{A}^{-1} \mathbf{B} = -\frac{1}{11} \begin{bmatrix} 2 & -5 \\ -3 & 2 \end{bmatrix} \begin{bmatrix} 1 \\ 7 \end{bmatrix} \\ \text{i.e.} \quad \mathbf{A} &= \begin{bmatrix} \mathbf{x} \\ \mathbf{y} \end{bmatrix} = -\frac{1}{11} \begin{bmatrix} -33 \\ 11 \end{bmatrix} = \begin{bmatrix} 3 \\ -1 \end{bmatrix} \end{aligned}$$

i.e.

Hence *x* = 3, *y* = – 1

**Example 17** Solve the following system of equations by matrix method.

$$\begin{aligned} 3x - 2y + 3z &= 8 \\ 2x + y - z &= 1 \\ 4x - 3y + 2z &= 4 \end{aligned}$$

**Solution** The system of equations can be written in the form AX = B, where

$$\mathbf{A} = \begin{bmatrix} 3 & -2 & 3 \\ 2 & 1 & -1 \\ 4 & -3 & 2 \end{bmatrix}, \mathbf{X} = \begin{bmatrix} x \\ y \\ z \end{bmatrix} \text{ and } \mathbf{B} = \begin{bmatrix} 8 \\ 1 \\ 4 \end{bmatrix}$$

We see that

$$\left| \mathbf{A} \right| = \mathbf{3} \left( 2 - 3 \right) + 2(4 + 4) + \mathbf{3} \left( -6 - 4 \right) = -17 \neq 0$$

Hence, A is nonsingular and so its inverse exists. Now

$$\begin{aligned} \mathbf{A}\_{11} &= -1, & \mathbf{A}\_{12} = -8, & \mathbf{A}\_{13} = -10, \\ \mathbf{A}\_{21} &= -5, & \mathbf{A}\_{22} = -6, & \mathbf{A}\_{23} = 1 \\ \mathbf{A}\_{31} &= -1, & \mathbf{A}\_{32} = 9, & \mathbf{A}\_{33} = 7 \end{aligned}$$

$$\begin{array}{llll} \text{Therefore} & \mathbf{A}^{-1} = -\frac{1}{17} \begin{bmatrix} -1 & -5 & -1 \\ -8 & -6 & 9 \\ -10 & 1 & 7 \end{bmatrix} \\\\ \text{So} & \mathbf{X} = \mathbf{A}^{-1}\mathbf{B} = -\frac{1}{17} \begin{bmatrix} -1 & -5 & -1 \\ -8 & -6 & 9 \\ -10 & 1 & 7 \end{bmatrix} \begin{bmatrix} 8 \\ 1 \\ 4 \end{bmatrix} \\\\ \text{i.e.} & \begin{bmatrix} x \\ y \\ z \end{bmatrix} = -\frac{1}{17} \begin{bmatrix} -17 \\ -34 \\ -51 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \\\\ \text{Hence} & x = 1, y = 2 \text{ and } z = 3. \end{array}$$

**Example 18** The sum of three numbers is 6. If we multiply third number by 3 and add second number to it, we get 11. By adding first and third numbers, we get double of the second number. Represent it algebraically and find the numbers using matrix method.

**Solution** Let first, second and third numbers be denoted by *x*, *y* and *z*, respectively. Then, according to given conditions, we have

$$\begin{array}{c} \mathbf{x} + \mathbf{y} + z = 6 \\ \mathbf{y} + 3z = 11 \\ \mathbf{A} + z = 2 \mathbf{y} \text{ or } \mathbf{x} - 2 \mathbf{y} + z = 0 \\ \text{This system can be written as A X = (B, where} \\ \mathbf{A} = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 3 \end{bmatrix}, \mathbf{X} = \begin{bmatrix} \mathbf{x} \\ \mathbf{y} \end{bmatrix} \text{ and } \mathbf{B} \end{array}$$

$$\mathbf{A} = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 3 \\ 1 & 2 & 1 \end{bmatrix}, \mathbf{X} = \begin{bmatrix} x \\ y \\ z \end{bmatrix} \text{ and } \mathbf{B} = \begin{bmatrix} 6 \\ 11 \\ 0 \end{bmatrix}$$

Here A 1 1 6 – (0 – 3) 0 –1 9 0 = + + = ≠ ( ) ( ) . Now we find *adj* A

$$\begin{aligned} \mathbf{A}\_{11} &= 1 \ (1+6) = 7, & \mathbf{A}\_{12} &= -(0-3) = 3, & \mathbf{A}\_{13} &= -1 \\ \mathbf{A}\_{21} &= -(1+2) = -3, & \mathbf{A}\_{22} &= 0, & \mathbf{A}\_{23} &= -(-2-1) = 3 \\ \mathbf{A}\_{31} &= (3-1) = 2, & \mathbf{A}\_{32} &= -(3-0) = -3, & \mathbf{A}\_{33} &= (1-0) = 1 \\ \text{Hence} & \text{adj } \mathbf{A} &= \begin{bmatrix} 7 & -3 & 2 \\ 3 & 0 & -3 \\ -1 & 3 & 1 \end{bmatrix} \end{aligned}$$

Thus A –1 = 1 A *adj* (A) = 7 3 2 1 3 0 3 9 1 3 1 *– – –* Since X = A–1 B X = 7 3 2 6 1 3 0 3 11 9 1 3 1 0 *– – –* or *x y z* = 1 9 42 33 0 18 0 0 6 33 0 − + + + − + + = 1 9 9 18 27 = 1 2 3 Thus *x* = 1, *y* = 2, *z* = 3 **EXERCISE 4.5** Examine the consistency of the system of equations in Exercises 1 to 6. **1.** *x* + 2*y* = 2 **2.** 2*x* – *y* = 5 **3.** *x* + 3*y* = 5 2*x* + 3*y* = 3 *x* + *y* = 4 2*x* + 6*y* = 8 **4.** *x* + *y* + *z* = 1 **5.** 3*x*–*y* – 2*z* = 2 **6.** 5*x* – *y* + 4*z* = 5 2*x* + 3*y* + 2*z* = 2 2*y* – *z* = –1 2*x* + 3*y* + 5*z* = 2 *ax* + *ay* + 2*az* = 4 3*x* – 5*y* = 3 5*x* – 2*y* + 6*z* = –1 Solve system of linear equations, using matrix method, in Exercises 7 to 14. **7.** 5*x* + 2*y* = 4 **8.** 2*x* – *y* = –2 **9.** 4*x* – 3*y* = 3 7*x* + 3*y* = 5 3*x* + 4*y* = 3 3*x* – 5*y* = 7 **10.** 5*x* + 2*y* = 3 **11.** 2*x* + *y* + *z* = 1 **12.** *x* – *y* + *z* = 4 3*x* + 2*y* = 5 *x* – 2*y* – *z* = 3 2 2*x* + *y* – 3*z* = 0 3*y* – 5*z* = 9 *x* + *y* + *z* = 2 **13.** 2*x* + 3*y* +3 *z* = 5 **14.** *x* – *y* + 2*z* = 7 *x* – 2*y* + *z* = – 4 3*x* + 4*y* – 5*z* = – 5 3*x* – *y* **–** 2*z* = 3 2*x* – *y* + 3*z* = 12

$$\begin{aligned} \text{15.} \quad \text{If } \mathbf{A} = \begin{bmatrix} 2 & -3 & 5 \\ 3 & 2 & -4 \\ 1 & 1 & -2 \end{bmatrix}, \text{ find } \mathbf{A}^{-1}. \text{ Using } \mathbf{A}^{-1} \text{ solve the system of equations} \\ \mathbf{x} \\ \mathbf{2x} - 3\mathbf{y} + 5\mathbf{z} &= 11 \\ 3\mathbf{x} + 2\mathbf{y} - 4\mathbf{z} &= -\mathbf{5} \\ \mathbf{x} + \mathbf{y} - 2\mathbf{z} &= -\mathbf{3} \end{aligned}$$

**16.** The cost of 4 kg onion, 3 kg wheat and 2 kg rice is ` 60. The cost of 2 kg onion, 4 kg wheat and 6 kg rice is ` 90. The cost of 6 kg onion 2 kg wheat and 3 kg rice is ` 70. Find cost of each item per kg by matrix method.

#### *Miscellaneous Examples*

$$\begin{aligned} \text{Example 19 Use product:} & \begin{bmatrix} 1 & 1 & 2 \\ 0 & 2 & 3 \\ 3 & 2 & 4 \end{bmatrix} \begin{bmatrix} 2 & 0 & 1 \\ 9 & 2 & 3 \\ 6 & 1 & 2 \end{bmatrix} \text{ to solve the system of equations} \\ \text{x} - y + 2z &= 1 \\ 2y - 3z &= 4 \\ 3x - 2y + 4z &= 2 \\ \text{Solution Consider the product:} & \begin{bmatrix} 1 & -1 & 2 \\ 0 & 2 & -3 \\ 3 & -2 & 4 \end{bmatrix} \begin{bmatrix} -2 & 0 & 1 \\ 9 & 2 & -3 \\ 6 & 1 & -2 \end{bmatrix} \\ &= \begin{bmatrix} -2 - 9 + 12 & 0 - 2 + 2 & 1 + 3 - 4 \\ 0 + 18 - 18 & 0 + 4 - 3 & 0 - 6 + 6 \\ -6 - 18 + 24 & 0 - 4 + 4 & 3 + 6 - 8 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \\ \text{Hence} & \begin{bmatrix} 1^{-1} - 1 & 2 \\ 0 & 2 & -3 \\ 3 & -2 & 4 \end{bmatrix} = \begin{bmatrix} -2 & 0 & 1 \\ 9 & 2 & -3 \\ 6 & 1 & -2 \end{bmatrix} \\ \text{Now, given system of equations can be written, in matrix form, as follows} \\ \text{[ $1 & -1} - 2 \text{ ] [$ 1 & -1]} \end{bmatrix} \end{aligned}$$

1 2

 

0 2 –3 3 –2 4

 

*y z* =

*–*

$$\begin{aligned} \text{or} \qquad \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 1 & -1 & 2 \\ 0 & 2 & -3 \\ 3 & -2 & 4 \end{bmatrix}^{-1} \begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 2 & 0 & 1 \\ 9 & 2 & 3 \\ 6 & 1 & 2 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix} \\ &= \begin{bmatrix} -2 + 0 + 2 \\ 9 + 2 - 6 \\ 6 + 1 - 4 \end{bmatrix} = \begin{bmatrix} 0 \\ 5 \\ 3 \end{bmatrix} \\ \text{Hence} \qquad \begin{aligned} x = 0, y = 5 \text{ and } z = \end{aligned} \end{aligned}$$

#### *Miscellaneous Exercises on Chapter 4*

**1.** Prove that the determinant sin cos – sin – 1 cos 1 *x x x* θ θ θ θ is independent of θ.

$$\begin{array}{ll} \text{2.} & \text{Evaluate} \\ \text{2.} & \text{Evaluate} \\ \text{2.} & \begin{vmatrix} \cos\alpha\cos\beta & \cos\alpha\sin\beta & -\sin\alpha \\ -\sin\beta & \cos\beta & 0 \\ \sin\alpha\cos\beta & \sin\alpha\sin\beta & \cos\alpha \end{vmatrix} \end{array}$$

$$\begin{aligned} \text{3.} \quad \text{If } \mathbf{A}^{-1} &= \begin{bmatrix} 3 & -1 & 1 \\ -15 & 6 & -5 \\ 5 & -2 & 2 \end{bmatrix} \text{and } \mathbf{B} = \begin{bmatrix} 1 & 2 & -2 \\ -1 & 3 & 0 \\ 0 & -2 & 1 \end{bmatrix}, \text{ find} \{\mathbf{AB}\}^{-1} \\ \text{4.} \quad \text{Let } \mathbf{A} &= \begin{bmatrix} 1 & 2 & 1 \\ 2 & 3 & 1 \\ 1 & 1 & 5 \end{bmatrix}. \text{ Verify that} \\ \text{(i) } \begin{bmatrix} \operatorname{adj}\mathbf{A}^{-1} & = \operatorname{adj}\mathbf{(A^{-1})} & \text{(ii) } & \text{(A^{-1})^{-1} = \mathbf{A}} \\ -\mathbf{A} & \mathbf{y} & \mathbf{x} + \mathbf{y} & \mathbf{x} \\ \mathbf{x} + \mathbf{y} & \mathbf{x} & \mathbf{y} & \mathbf{x} \end{bmatrix} \\ \text{5.} \quad \text{Evaluate} \begin{bmatrix} 1 & \mathbf{x} & \mathbf{y} \\ 1 & \mathbf{x} + \mathbf{y} & \mathbf{y} \\ 1 & \mathbf{x} + \mathbf{y} & \mathbf{y} \end{bmatrix} \end{aligned}$$

Using properties of determinants in Exercises 11 to 15, prove that:

**7.** Solve the system of equations

| 2<br>+<br>x | 3<br>+<br>y | 10<br>=<br>4<br>z |
|-------------|-------------|-------------------|
| 4<br>–<br>x | 6<br>+<br>y | 5<br>=1<br>z      |
| 6<br>+<br>x | 9<br>–<br>y | 20<br>=<br>2<br>z |

Choose the correct answer in Exercise 17 to 19.

**8.** If *x*, *y*, *z* are nonzero real numbers, then the inverse of matrix 0 0 A 0 0 0 0 *x y z* = is

$$\begin{aligned} \text{(A)} \quad & \begin{bmatrix} x^{-1} & 0 & 0 \\ 0 & y^{-1} & 0 \\ 0 & 0 & z^{-1} \end{bmatrix} \\ & \text{(C)} \quad \frac{1}{\text{xyz}} \begin{bmatrix} x & 0 & 0 \\ 0 & y & 0 \\ 0 & 0 & z^{-1} \end{bmatrix} \\ & \text{(C)} \quad \frac{1}{\text{xyz}} \begin{bmatrix} x & 0 & 0 \\ 0 & y & 0 \\ 0 & 0 & z \end{bmatrix} \\ & \text{(D)} \quad \text{Let } \mathbf{A} = \begin{bmatrix} 1 & \sin\theta & 1 \\ -\sin\theta & 1 & \sin\theta \\ -1 & -\sin\theta & 1 \end{bmatrix}, \text{ where } 0 \le \theta \le 2\pi. \text{ Then} \\ & \text{(A)} \quad \text{Det(A)} = 0 \qquad \text{(B)} \quad \text{Det(A)} \in \left(2, \infty\right) \end{aligned}$$

$$\begin{array}{ccccc}\cdot\\(\text{C})\quad\text{Det}(\text{A})\in(\text{2, 4})\end{array}\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\text{(D)}\quad\text{Det}(\text{A})\in[\text{2, 4}]\quad\qquad$$

#### *Summary*

- Æ Determinant of a matrix A = [*a*11] 1×1 is given by | *a*<sup>11</sup> | = *a*<sup>11</sup>
- Æ Determinant of a matrix <sup>A</sup> <sup>=</sup> *a a a a* 11 12 21 22 is given by

$$\left| \mathbf{A} \right| = \begin{vmatrix} a\_{11} & a\_{12} \\ a\_{21} & a\_{22} \end{vmatrix} = a\_{11} \begin{vmatrix} a\_{22} - a\_{12} \ a\_{21} \end{vmatrix}$$

Æ Determinant of a matrix <sup>A</sup> <sup>=</sup> *a b c a b c a b c* 1 1 1 2 2 2 3 3 3 is given by (expanding along R<sup>1</sup> )

$$\begin{vmatrix} \mathbf{A} \end{vmatrix} = \begin{vmatrix} a\_1 & b\_1 & c\_1 \\ a\_2 & b\_2 & c\_2 \\ a\_3 & b\_3 & c\_3 \end{vmatrix} = a\_1 \begin{vmatrix} b\_2 & c\_2 \\ b\_3 & c\_3 \end{vmatrix} - b\_1 \begin{vmatrix} a\_2 & c\_2 \\ a\_3 & c\_3 \end{vmatrix} + c\_1 \begin{vmatrix} a\_2 & b\_2 \\ a\_3 & b\_3 \end{vmatrix}$$

#### **For any square matrix A, the |A| satisfy following properties.**

Æ Area of a triangle with vertices (*<sup>x</sup>* 1 , *y* 1 ), (*x* 2 , *y* 2 ) and (*x* 3 , *y* 3 ) is given by

$$
\Delta = \frac{1}{2} \begin{vmatrix} \mathbf{x}\_1 & \mathbf{y}\_1 & 1\\ \mathbf{x}\_2 & \mathbf{y}\_2 & 1\\ \mathbf{x}\_3 & \mathbf{y}\_3 & 1 \end{vmatrix}
$$

- Æ Minor of an element *aij* of the determinant of matrix A is the determinant obtained by deleting *i* th row and *j th* column and denoted by M*ij*.
- Æ Cofactor of *aij* of given by A*ij* = (– 1)*<sup>i</sup>*<sup>+</sup> *<sup>j</sup>* <sup>M</sup>*ij*
- Æ Value of determinant of a matrix A is obtained by sum of product of elements of a row (or a column) with corresponding cofactors. For example,

$$|\mathbf{A}| \equiv a\_{11}\mathbf{A}\_{11} + a\_{12}\mathbf{A}\_{12} + a\_{13}\mathbf{A}\_{13},$$

Æ If elements of one row (or column) are multiplied with cofactors of elements of any other row (or column), then their sum is zero. For example, *a*11 A21 + *a*<sup>12</sup> A22 + *a*13 A23 = 0

- Æ If 11 12 13 21 22 23 31 32 33 A , *a a a a a a a a a* = then 11 21 31 12 22 32 13 23 33 A A A A A A A A A A *adj* = , where A*ij* is cofactor of *aij*
- Æ A (*adj* A) = (*adj* A) A = |A| I, where A is square matrix of order *n*.
- Æ A square matrix A is said to be singular or non-singular according as |A| = 0 or |A| ≠ 0.
- Æ If AB = BA = I, where B is square matrix, then B is called inverse of A. Also A–1 = B or B–1 = A and hence (A–1) –1 = A.
- Æ A square matrix A has inverse if and only if A is non-singular.

$$\mathbf{O} \quad \mathbf{A}^{-1} = \frac{1}{|\mathbf{A}|} (adj \mathbf{A})^2$$

Æ If *<sup>a</sup>*1 *<sup>x</sup>* <sup>+</sup>*b*<sup>1</sup> *y* + *c*<sup>1</sup> *z* = *d*<sup>1</sup> *a*2 *x* + *b*<sup>2</sup> *y* + *c* 2 *z* = *d*<sup>2</sup> *a*3 *x* + *b*<sup>3</sup> *y* + *c* 3 *z* = *d*<sup>3</sup> ,

then these equations can be written as A X = B, where

$$\mathbf{A} = \begin{bmatrix} a\_1 & b\_1 & c\_1 \\ a\_2 & b\_2 & c\_2 \\ a\_3 & b\_3 & c\_3 \end{bmatrix}, \mathbf{X} = \begin{bmatrix} \mathbf{x} \\ \mathbf{y} \\ \mathbf{z} \end{bmatrix} \text{ and } \mathbf{B} = \begin{bmatrix} d\_1 \\ d\_2 \\ d\_3 \end{bmatrix}$$

- Æ Unique solution of equation AX = B is given by X = A–1 B, where A 0 <sup>≠</sup> *.*
- Æ A system of equation is consistent or inconsistent according as its solution exists or not.
- Æ For a square matrix A in matrix equation AX = B
	- (i) |A| ≠ 0, there exists unique solution
	- (ii) |A| = 0 and (*adj* A) B ≠ 0, then there exists no solution
	- (iii) |A| = 0 and (*adj* A) B = 0, then system may or may not be consistent.

### *Historical Note*

The Chinese method of representing the coefficients of the unknowns of several linear equations by using rods on a calculating board naturally led to the discovery of simple method of elimination. The arrangement of rods was precisely that of the numbers in a determinant. The Chinese, therefore, early developed the idea of subtracting columns and rows as in simplification of a determinant *Mikami, China*, *pp* 30, 93.

Seki Kowa, the greatest of the Japanese Mathematicians of seventeenth century in his work '*Kai Fukudai no Ho*' in 1683 showed that he had the idea of determinants and of their expansion. But he used this device only in eliminating a quantity from two equations and not directly in the solution of a set of simultaneous linear equations. T. Hayashi, "*The Fakudoi and Determinants in Japanese Mathematics*," in the proc. of the Tokyo Math. Soc., V.

Vendermonde was the first to recognise determinants as independent functions. He may be called the formal founder. Laplace (1772), gave general method of expanding a determinant in terms of its complementary minors. In 1773 Lagrange treated determinants of the second and third orders and used them for purpose other than the solution of equations. In 1801, Gauss used determinants in his theory of numbers.

The next great contributor was Jacques - Philippe - Marie Binet, (1812) who stated the theorem relating to the product of two matrices of *m*-columns and *n*rows, which for the special case of *m* = *n* reduces to the multiplication theorem.

Also on the same day, Cauchy (1812) presented one on the same subject. He used the word 'determinant' in its present sense. He gave the proof of multiplication theorem more satisfactory than Binet's.

The greatest contributor to the theory was Carl Gustav Jacob Jacobi, after this the word determinant received its final acceptance.