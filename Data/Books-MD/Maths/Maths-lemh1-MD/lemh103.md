![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

# v*The essence of Mathematics lies in its freedom. — CANTOR* v

# **3.1 Introduction**

34 MATHEMATICS

The knowledge of matrices is necessary in various branches of mathematics. Matrices are one of the most powerful tools in mathematics. This mathematical tool simplifies our work to a great extent when compared with other straight forward methods. The evolution of concept of matrices is the result of an attempt to obtain compact and simple methods of solving system of linear equations. Matrices are not only used as a representation of the coefficients in system of linear equations, but utility of matrices far exceeds that use. Matrix notation and operations are used in electronic spreadsheet programs for personal computer, which in turn is used in different areas of business and science like budgeting, sales projection, cost estimation, analysing the results of an experiment etc. Also, many physical operations such as magnification, rotation and reflection through a plane can be represented mathematically by matrices. Matrices are also used in cryptography. This mathematical tool is not only used in certain branches of sciences, but also in genetics, economics, sociology, modern psychology and industrial management.

In this chapter, we shall find it interesting to become acquainted with the fundamentals of matrix and matrix algebra.

# **3.2 Matrix**

Suppose we wish to express the information that Radha has 15 notebooks. We may express it as [15] with the understanding that the number inside [ ] is the number of notebooks that Radha has. Now, if we have to express that Radha has 15 notebooks and 6 pens. We may express it as [15 6] with the understanding that first number inside [ ] is the number of notebooks while the other one is the number of pens possessed by Radha. Let us now suppose that we wish to express the information of possession of notebooks and pens by Radha and her two friends Fauzia and Simran which is as follows:

| Radha                                                      | has | 15        | notebooks | and    | 6 pens, |
|------------------------------------------------------------|-----|-----------|-----------|--------|---------|
| Fauzia                                                     | has | 10        | notebooks | and    | 2 pens, |
| Simran                                                     | has | 13        | notebooks | and    | 5 pens. |
| Now this could be arranged in the tabular form as follows: |     |           |           |        |         |
|                                                            |     | Notebooks |           | Pens   |         |
| Radha                                                      |     | 15        |           | 6      |         |
| Fauzia                                                     |     | 10        |           | 2      |         |
| Simran                                                     |     | 13        |           | 5      |         |
| and this can be expressed as                               |     |           |           |        |         |
|                                                            |     |           |           |        |         |
|                                                            |     |           |           |        |         |
|                                                            |     |           |           |        |         |
|                                                            |     |           |           |        |         |
|                                                            |     |           |           |        |         |
|                                                            |     |           |           |        |         |
| or                                                         |     |           |           |        |         |
|                                                            |     | Radha     | Fauzia    | Simran |         |
| Notebooks                                                  |     | 15        | 10        | 13     |         |
| Pens                                                       |     | 6         | 2         | 5      |         |
| which can be expressed as:                                 |     |           |           |        |         |
|                                                            |     |           |           |        |         |
|                                                            |     |           |           |        |         |
|                                                            |     |           |           |        |         |
|                                                            |     |           |           |        |         |
|                                                            |     |           |           |        |         |

In the first arrangement the entries in the first column represent the number of note books possessed by Radha, Fauzia and Simran, respectively and the entries in the second column represent the number of pens possessed by Radha, Fauzia and Simran,

respectively. Similarly, in the second arrangement, the entries in the first row represent the number of notebooks possessed by Radha, Fauzia and Simran, respectively. The entries in the second row represent the number of pens possessed by Radha, Fauzia and Simran, respectively. An arrangement or display of the above kind is called a *matrix*. Formally, we define matrix as:

**Definition 1** A *matrix* is an ordered rectangular array of numbers or functions. The numbers or functions are called the elements or the entries of the matrix.

We denote matrices by capital letters. The following are some examples of matrices:

$$\mathbf{A} = \begin{bmatrix} -2 & 5 \\ 0 & \sqrt{5} \\ 3 & 6 \end{bmatrix}, \mathbf{B} = \begin{bmatrix} 2+i & 3 & -\frac{1}{2} \\ 3.5 & -1 & 2 \\ \sqrt{3} & 5 & \frac{5}{7} \end{bmatrix}, \mathbf{C} = \begin{bmatrix} 1+x & x^3 & 3 \\ \cos x & \sin x + 2\sqrt{\tan x} \end{bmatrix}$$

In the above examples, the horizontal lines of elements are said to constitute, *rows* of the matrix and the vertical lines of elements are said to constitute, *columns* of the matrix. Thus A has 3 rows and 2 columns, B has 3 rows and 3 columns while C has 2 rows and 3 columns.

#### **3.2.1** *Order of a matrix*

A matrix having *m* rows and *n* columns is called a matrix of *order m* × *n* or simply *m* × *n* matrix (read as an *m* by *n* matrix). So referring to the above examples of matrices, we have A as 3 × 2 matrix, B as 3 × 3 matrix and C as 2 × 3 matrix. We observe that A has 3 × 2 = 6 elements, B and C have 9 and 6 elements, respectively.

In general, an *m* × *n* matrix has the following rectangular array:

| all | a12                                                                                                                                                                          | aj3  aj;  alm                                                                                                                                                                                      |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     | a222 • 222                                                                                                                                                                   | ···· (12)<br>a23<br>a 2n<br>.                                                                                                                                                                      |
|     | ដំរី របស់ ពួក រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួច រួ | a j3<br>··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··· ··<br>a in<br> |
|     | am2                                                                                                                                                                          | am3 ···· ami<br>··· · amn !<br>m × n                                                                                                                                                               |

or A = [*aij*] *m* × *n* , 1≤ *i* ≤ *m*, 1≤ *j* ≤ *n i*, *j* ∈ N

Thus the *i* th row consists of the elements *ai*<sup>1</sup> , *ai*<sup>2</sup> , *ai*<sup>3</sup> ,..., *ain*, while the *j* th column consists of the elements *a*1*<sup>j</sup>* , *a*2*<sup>j</sup>* , *a*3*<sup>j</sup>* ,..., *amj* ,

In general *aij*, is an element lying in the *i* th row and *j* th column. We can also call it as the (*i*, *j*) th element of A. The number of elements in an *m* × *n* matrix will be equal to *mn*.

A**Note** In this chapter

- 1. We shall follow the notation, namely A = [*aij*] *m* × *n* to indicate that A is a matrix of order *m* × *n*.
- 2. We shall consider only those matrices whose elements are real numbers or functions taking real values.

We can also represent any point (*x*, *y*) in a plane by a matrix (column or row) as *x y* (or [*x*, *y*]). For example point P(0, 1) as a matrix representation may be given as

$$\mathbf{P} = \begin{bmatrix} \mathbf{0} \\ \mathbf{1} \end{bmatrix} \text{ or } \begin{bmatrix} \mathbf{0} \ \mathbf{1} \end{bmatrix}.$$

Observe that in this way we can also express the vertices of a closed rectilinear figure in the form of a matrix. For example, consider a quadrilateral ABCD with vertices A (1, 0), B (3, 2), C (1, 3), D (–1, 2).

Now, quadrilateral ABCD in the matrix form, can be represented as

| A<br>B                     | C<br>D                                | A<br><br>1             | 0<br>             |
|----------------------------|---------------------------------------|-------------------------|--------------------|
| 1<br>3<br>                | −<br>1<br>1<br>                      | <br>B<br>3<br>        | <br>2<br>        |
| =<br>X<br><br>0<br>2<br> | or<br><br>3<br>2<br><br>2<br>×<br>4 | =<br>Y<br><br>C<br>1   | <br>3             |
|                            |                                       | <br>−<br>D<br>1<br>  | <br>2<br>×<br>4 2 |

Thus, matrices can be used as representation of vertices of geometrical figures in a plane.

Now, let us consider some examples.

**Example 1** Consider the following information regarding the number of men and women workers in three factories I, II and III

|     | Men workers | Women workers |
|-----|-------------|---------------|
| I   | 30          | 25            |
| II  | 25          | 31            |
| III | 27          | 26            |

Represent the above information in the form of a 3 × 2 matrix. What does the entry in the third row and second column represent?

**Solution** The information is represented in the form of a 3 × 2 matrix as follows:

$$\mathbf{A} = \begin{bmatrix} 30 & 25 \\ 25 & 31 \\ 27 & 26 \end{bmatrix}$$

The entry in the third row and second column represents the number of women workers in factory III.

**Example 2** If a matrix has 8 elements, what are the possible orders it can have?

**Solution** We know that if a matrix is of order *m* × *n*, it has *mn* elements. Thus, to find all possible orders of a matrix with 8 elements, we will find all ordered pairs of natural numbers, whose product is 8.

Thus, all possible ordered pairs are (1, 8), (8, 1), (4, 2), (2, 4) Hence, possible orders are 1 × 8, 8 ×1, 4 × 2, 2 × 4

**Example 3** Construct a 3 × 2 matrix whose elements are given by <sup>1</sup> | 3 | 2 *ij a i j* = − *.*

**Solution** In general a 3 × 2 matrix is given by 11 12 21 22 31 32 A *a a a a a a* = .

Now

$$a\_{ij} = \frac{1}{2}(\underline{i} - \mathbf{3}) \mid\_i i = 1, 2, 3 \text{ and } j = 1, 2.$$

Therefore <sup>11</sup> 1 |1 3 1| 1 2 *a* = − × = <sup>12</sup> 1 5 |1 3 2 | 2 2 *a* = − × = 21 1 1 | 2 3 1| 2 2 *a* = − × = <sup>22</sup> 1 | 2 3 2 | 2 2 *a* = − × = 31 1 | 3 3 1| 0 2 *a* = − × = <sup>32</sup> 1 3 | 3 3 2 | 2 2 *a* = − × = Hence the required matrix is given by 5 1 2 1 A 2 2 3 0 2 = .

# **3.3 Types of Matrices**

In this section, we shall discuss different types of matrices.

(i) **Column matrix**

A matrix is said to be a *column matrix* if it has only one column.

$$\text{For example, } \mathbf{A} = \begin{bmatrix} \mathbf{0} \\ \sqrt{3} \\ -1 \\ 1/2 \end{bmatrix} \text{ is a column matrix of order } 4 \times 1.$$

In general, A = [*aij*] *<sup>m</sup>* × 1 is a column matrix of order *m* × 1.

#### (ii) **Row matrix**

A matrix is said to be a *row matrix* if it has only one row.

For example, 1 4 1 B 5 2 3 2 <sup>×</sup> = − is a row matrix.

In general, B = [*bij*] 1 × *n* is a row matrix of order 1 × *n*.

#### (iii) **Square matrix**

A matrix in which the number of rows are equal to the number of columns, is said to be a *square matrix*. Thus an *m* × *n* matrix is said to be a square matrix if *m* = *n* and is known as a square matrix of order '*n*'.

$$\text{For example } \mathbf{A} = \begin{bmatrix} 3 & -1 & 0 \\ 3 & 3\sqrt{2} & 1 \\ 4 & -3 & -1 \end{bmatrix} \text{ is a square matrix of order 3.}$$

In general, A = [*aij*] *m* × *m* is a square matrix of order *m*.

A**Note** If A = [*aij*] is a square matrix of order *n*, then elements (entries) *a*11, *a*22*, ...*, *ann* are said to constitute the *diagonal*, of the matrix A. Thus, if 1 3 1 A 2 4 1 3 5 6 − = − . Then the elements of the diagonal of A are 1, 4, 6.

#### (iv) **Diagonal matrix**

A square matrix B = [*bij*] *m* × *m* is said to be a *diagonal matrix* if all its non diagonal elements are zero, that is a matrix B = [*bij*] *m* × *m* is said to be a diagonal matrix if *bij* = 0, when *i* ≠ *j*.

$$\text{For example, } \mathbf{A} = \begin{bmatrix} 4 \\ \end{bmatrix}, \mathbf{B} = \begin{bmatrix} -1 & 0 \\ 0 & 2 \end{bmatrix}, \mathbf{C} = \begin{bmatrix} -1.1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{bmatrix}, \text{ are diagonal matrices.}$$

of order 1, 2, 3, respectively.

#### (v) **Scalar matrix**

A diagonal matrix is said to be a *scalar matrix* if its diagonal elements are equal, that is, a square matrix B = [*bij*] *n* × *n* is said to be a scalar matrix if

$$\begin{aligned} b\_{ij} &= 0, \quad \text{when } i \neq j\\ b\_{ij} &= k, \quad \text{when } i = j, \text{ for some constant } k. \end{aligned}$$

For example

$$\mathbf{A} = [\mathfrak{F}], \qquad \mathbf{B} = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}, \qquad \mathbf{C} = \begin{bmatrix} \sqrt{3} & 0 & 0 \\ 0 & \sqrt{3} & 0 \\ 0 & 0 & \sqrt{3} \end{bmatrix}$$

are scalar matrices of order 1, 2 and 3, respectively.

#### (vi) **Identity matrix**

A square matrix in which elements in the diagonal are all 1 and rest are all zero is called an *identity matrix*. In other words, the square matrix A = [*aij*] *n* × *n* is an

$$\text{identity matrix}, \text{ if } a\_{ij} = \begin{cases} 1 & \text{if } \quad i = j \\ 0 & \text{if } \quad i \neq j \end{cases}.$$

We denote the identity matrix of order *n* by I *n .* When order is clear from the context, we simply write it as I.

For example [1], 1 0 0 1 , 1 0 0 0 1 0 0 0 1 are identity matrices of order 1, 2 and 3,

respectively.

Observe that a scalar matrix is an identity matrix when *k* = 1. But every identity matrix is clearly a scalar matrix.

#### (vii) **Zero matrix**

A matrix is said to be *zero matrix* or *null matrix* if all its elements are zero.

For example, [0], 0 0 0 0 , 0 0 0 0 0 0 , [0, 0] are all zero matrices. We denote zero matrix by O. Its order will be clear from the context.

#### **3.3.1** *Equality of matrices*

**Definition 2** Two matrices A = [*aij*] and B = [*bij*] are said to be equal if

- (i) they are of the same order
- (ii) each element of A is equal to the corresponding element of B, that is *aij* = *bij* for all *i* and *j*.

For example, 2 3 2 3 and 0 1 0 1 are equal matrices but 3 2 2 3 and 0 1 0 1 are

not equal matrices. Symbolically, if two matrices A and B are equal, we write A = B.

$$\text{If } \begin{bmatrix} x & y \\ z & a \\ b & c \end{bmatrix} = \begin{bmatrix} -1.5 & 0 \\ 2 & \sqrt{6} \\ 3 & 2 \end{bmatrix}, \text{ then } x = -1.5, y = 0, z = 2, a = \sqrt{6}, b = 3, c = 2.$$

$$\text{Example 4: If } \begin{bmatrix} x + 3 & (z + 4 & 2y - 7) \\ -6 & a - 1 & 0 \\ b - 3 & -21 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 6 & 3y - 2 \\ -6 & -3 & 2c + 2 \\ 2b + 4 & -21 & 0 \end{bmatrix}$$

Find the values of *a*, *b*, *c*, *x*, *y* and *z*.

**Solution** As the given matrices are equal, therefore, their corresponding elements must be equal. Comparing the corresponding elements, we get

$$\begin{array}{cccc} x+3 = 0, & & z+4 = 6, & & 2y-7 = 3y-2\\ a-1 = -3, & & 0 = 2c+2 & & b-3 = 2b+4, \\ \end{array}$$

Simplifying, we get

$$a = -2, \; b = -7, \; c = -1, \; x = -3, \; y = -5, \; z = 25$$

**Example 5** Find the values of *a*, *b*, *c*, and *d* from the following equation:

$$
\begin{bmatrix} 2a+b & a-2b \\ \mathcal{S}c-d & 4c+3d \end{bmatrix} = \begin{bmatrix} 4 & -3 \\ 11 & 24 \end{bmatrix}
$$

**Solution** By equality of two matrices, equating the corresponding elements, we get

$$\begin{aligned} 2a + b &= 4 \\ a - 2b &= -3 \end{aligned} \qquad \begin{aligned} 5c - d &= 11 \\ 4c + 3d &= 24 \end{aligned}$$

Solving these equations, we get

$$a = 1, \; b = 2, \; c = 3 \text{ and } d = 4$$

**EXERCISE 3.1**

- **1.** In the matrix 2 5 19 7 5 A 35 2 12 2 3 1 5 17 − = − − , write:
	- (i) The order of the matrix, (ii) The number of elements,
	- (iii) Write the elements *a*13, *a*21, *a*33, *a*24, *a*23.
- **2.** If a matrix has 24 elements, what are the possible orders it can have? What, if it has 13 elements?
- **3.** If a matrix has 18 elements, what are the possible orders it can have? What, if it has 5 elements?
- **4.** Construct a 2 × 2 matrix, A = [*aij*], whose elements are given by:

$$\text{(i)}\quad a\_{\vec{y}} = \frac{\left(\vec{i} + \left[\vec{j}\right]^2\right)}{2} \qquad \text{(ii)}\quad \underbrace{a\_{\vec{y}}}\_{\longrightarrow} = \frac{\vec{i}}{\vec{j}} \qquad \text{(iii)}\qquad a\_{\vec{y}} = \frac{\left(\vec{i} + 2\vec{j}\right)^2}{2}$$

**5.** Construct a 3 × 4 matrix, whose elements are given by:

$$\text{(i)}\quad a\_{ij} = \frac{1}{2} \left| -3i + \widehat{j\_i} \right| \quad \text{(ii)}\quad a\_{ij} = 2i - j$$

**6.** Find the values of *x*, *y* and *z* from the following equations:

$$\text{(i)} \begin{bmatrix} 4 & -3 \\ 1 & 5 \end{bmatrix} = \begin{bmatrix} y & z \\ 1 & 5 \end{bmatrix} \quad \text{(ii)} \begin{bmatrix} x+y & 2 \\ 5+z & xy \end{bmatrix} = \begin{bmatrix} 6 & 2 \\ 5 & 8 \end{bmatrix} \\ \text{(iii)} \quad \begin{bmatrix} x+y+z \\ x+z \\ y+z \end{bmatrix} = \begin{bmatrix} 9 \\ 5 \\ 7 \end{bmatrix} \quad \text{(iv)} \begin{bmatrix} x+y \\ y+z \end{bmatrix} = \begin{bmatrix} 1 \\ 5 \\ 7 \end{bmatrix} \quad \text{(v)} \begin{bmatrix} x+y \\ y+z \end{bmatrix} = \begin{bmatrix} 1 \\ 5 \\ 7 \end{bmatrix} \quad \text{(v)} \begin{bmatrix} 2 \\ 3 \\ -1 \end{bmatrix} = \begin{bmatrix} 1 \\ -1 \\ 1 \end{bmatrix}$$

**7.** Find the value of *a*, *b*, *c* and *d* from the equation:

$$
\begin{bmatrix} a-b & 2a+c \\ 2a-b & 3c+d \end{bmatrix} = \begin{bmatrix} -1 & \mathfrak{S} \\ 0 & 13 \end{bmatrix}
$$

- **8.** A = [*aij*] *<sup>m</sup>* × *n\* is a square matrix, if (A) *m* < *n* (B) *m* > *n* (C) *m* = *n* (D) None of these
- **9.** Which of the given values of *x* and *y* make the following pair of matrices equal 3 7 5 1 2 3 *x y x* + + − , 0 2 8 4 *y* − (A) 1 , 7 3 *x y* − = = (B) Not possible to find (C) *y* = 7, 2 3 *x* − = (D) 1 2 , 3 3 *x y* − − = =
- **10.** The number of all possible matrices of order 3 × 3 with each entry 0 or 1 is: (A) 27 (B) 18 (C) 81 (D) 512

# **3.4 Operations on Matrices**

In this section, we shall introduce certain operations on matrices, namely, addition of matrices, multiplication of a matrix by a scalar, difference and multiplication of matrices.

## **3.4.1** *Addition of matrices*

Suppose Fatima has two factories at places A and B. Each factory produces sport shoes for boys and girls in three different price categories labelled 1, 2 and 3. The quantities produced by each factory are represented as matrices given below:

|   | Factory at A |       |   | Factory at B |       |  |
|---|--------------|-------|---|--------------|-------|--|
|   | Boys         | Girls |   | Boys         | Girls |  |
|   | 80           | 60    | 1 | 90           | 50    |  |
| 2 | 75           | 65    | 2 | 70           | રેરે  |  |
| 3 | 90           | ૪૨    | 3 | 75           | 75    |  |

Suppose Fatima wants to know the total production of sport shoes in each price category. Then the total production

In category 1 : for boys (80 + 90), for girls (60 + 50)

In category 2 : for boys (75 + 70), for girls (65 + 55)

In category 3 : for boys (90 + 75), for girls (85 + 75)

$$\begin{aligned} \text{This can be represented in the matrix form as} \begin{bmatrix} 80+90 & 60+50 \\ 75+70 & 65+55 \\ 90+75 & 85+75 \end{bmatrix}. \end{aligned} $$

This new matrix is the **sum** of the above two matrices. We observe that the sum of two matrices is a matrix obtained by adding the corresponding elements of the given matrices. Furthermore, the two matrices have to be of the same order.

$$\begin{aligned} \text{Thus, if } \mathbf{A} = \begin{bmatrix} a\_{11} & a\_{12} & a\_{13} \\ a\_{21} & a\_{22} & a\_{23} \end{bmatrix} \text{ is a } 2 \times 3 \text{ matrix and } \mathbf{B} = \begin{bmatrix} b\_{11} & b\_{12} & b\_{13} \\ b\_{21} & b\_{22} & b\_{23} \end{bmatrix} \text{ is another.} \end{aligned}$$

2×3 matrix. Then, we define 11 11 12 12 13 13 21 21 22 22 23 23 A + B *a b a b a b a b a b a b* + + + = + + + .

In general, if A = [*aij*] and B = [*bij*] are two matrices of the same order, say *m* × *n*. Then, the sum of the two matrices A and B is *defined* as a matrix C = [*cij*] *m* × *n* , where *cij* = *aij* + *bij*, for all possible values of *i* and *j*.

$$\text{Example 6: Given } \mathbf{A} = \begin{bmatrix} \sqrt{3} & 1 & -1 \\ 2 & 3 & 0 \end{bmatrix} \text{ and } \mathbf{B} = \begin{bmatrix} 2 & \sqrt{5} & 1 \\ -2 & 3 & \frac{1}{2} \\ -2 & 3 & \frac{1}{2} \end{bmatrix}, \text{ find } \mathbf{A} + \mathbf{B}$$

Since A, B are of the same order 2 × 3. Therefore, addition of A and B is defined and is given by

$$\mathbf{A} + \mathbf{B} = \begin{bmatrix} 2 + \sqrt{3} & 1 + \sqrt{5} & 1 - 1 \\ 2 - 2 & 3 + 3 & 0 + \frac{1}{2} \\ \end{bmatrix} \begin{bmatrix} 2 + \sqrt{3} & 1 + \sqrt{5} & 0 \\ 0 & 6 & 1 \\ \end{bmatrix}$$

# A**Note**

1. We emphasise that if A and B are not of the same order, then A + B is not

defined. For example if 2 3 A 1 0 <sup>=</sup> , 1 2 3 B , 1 0 1 <sup>=</sup> then A + B is not defined.

2. We may observe that addition of matrices is an example of binary operation on the set of matrices of the same order.

#### **3.4.2** *Multiplication of a matrix by a scalar*

Now suppose that Fatima has doubled the production at a factory A in all categories (refer to 3.4.1).

Previously quantities (in standard units) produced by factory A were

|   | Boys | Girls |  |  |
|---|------|-------|--|--|
| 1 | 80   | 60    |  |  |
| 2 | 75   | 65    |  |  |
| 3 | 90   | 85    |  |  |

Revised quantities produced by factory A are as given below:

|   | Boys                   | Girls                  |
|---|------------------------|------------------------|
| 1 | ×<br>2<br>80<br>      | ×<br>2<br>60<br>      |
| 2 | <br>×<br>2<br>75<br> | <br>×<br>2<br>65<br> |
| 3 | <br>×<br>2<br>90<br> | <br>×<br>2<br>85<br> |

This can be represented in the matrix form as 160 120 150 130 180 170 . We observe that

the new matrix is obtained by multiplying each element of the previous matrix by 2.

In general, we may define *multiplication of a matrix* by a scalar as follows: if A = [*aij*] *m* × *n* is a matrix and *k* is a scalar, then *k*A is another matrix which is obtained by multiplying each element of A by the scalar *k*.

In other words, *k*A = *k* [*aij*] *m* × *n* = [*k* (*aij*)] *m* × *n* , that is, (*i*, *j*) th element of *k*A is *kaij* for all possible values of *i* and *j*.

|                 |                    | 3 | 1 | 1.5<br>         |                       |    |                  |
|-----------------|---------------------|---|---|------------------|-----------------------|----|------------------|
| For example, if | <br>A =<br>       | 5 | 7 | <br>−<br>3<br> | , then                |    |                  |
|                 | <br>              | 2 | 0 | <br>5<br>      |                       |    |                  |
|                 |                     |   |   |                  |                       |    |                  |
|                 |                    | 3 | 1 | 1.5<br>         | 9<br>                | 3  | 4.5<br>         |
|                 | <br>3A =<br>3<br> | 5 | 7 | <br>−<br>3<br> | <br>=<br>3<br>5<br> | 21 | <br>−<br>9<br> |
|                 | <br>              | 2 | 0 | <br>5<br>      | <br>6<br>           | 0  | <br>15<br>     |

**Negative of a matrix** The negative of a matrix is denoted by – A. We define –A = (– 1) A.

$$\begin{aligned} \text{For example, let} \\ \begin{bmatrix} \mathbf{A} \end{bmatrix} \text{A} & \mathbf{A} = \begin{bmatrix} 3 & 1 \\ -5 & \mathbf{x} \end{bmatrix}, \text{ then} \\ -\mathbf{A} &= (-1)\mathbf{A} = (-1) \begin{bmatrix} 3 & 1 \\ -5 & \mathbf{x} \end{bmatrix} = \begin{bmatrix} -3 & -1 \\ \mathbf{5} & -\mathbf{x} \end{bmatrix} \end{aligned}$$

**Difference of matrices** If A = [*aij*], B = [*bij*] are two matrices of the same order, say *m* × *n*, then difference A – B is defined as a matrix D = [*dij*], where *dij* = *aij* – *bij*, for all value of *i* and *j*. In other words, D = A – B = A + (–1) B, that is sum of the matrix A and the matrix – B.

$$\text{Example 7 If } \mathbf{A} = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{bmatrix} \\ \text{and } \mathbf{B} = \begin{bmatrix} 3 & -1 & 3 \\ -1 & 0 & 2 \end{bmatrix}, \text{ then find } 2\mathbf{A} - \mathbf{B}.$$

**Solution** We have

$$\begin{aligned} \mathbf{2A} - \mathbf{B} &= 2 \begin{bmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{bmatrix} - \begin{bmatrix} 3 & -1 & 3 \\ -1 & 0 & 2 \end{bmatrix} \\ &= \begin{bmatrix} 2 & 4 & 6 \\ 4 & 6 & 2 \end{bmatrix} + \begin{bmatrix} -3 & 1 & -3 \\ 1 & 0 & -2 \end{bmatrix} \\ &= \begin{bmatrix} 2 - 3 & 4 + 1 & 6 - 3 \\ 4 + 1 & 6 + 0 & 2 - 2 \end{bmatrix} \equiv \begin{bmatrix} -1 & 5 & 3 \\ 5 & 6 & 0 \end{bmatrix} \end{aligned}$$

#### **3.4.3** *Properties of matrix addition*

The addition of matrices satisfy the following properties:

- (i) **Commutative Law** If A = [*aij*], B = [*bij*] are matrices of the same order, say *m* × *n*, then A + B = B + A.
	- Now A + B = [*aij*] + [*bij*] = [*aij* + *bij*] = [*bij* + *aij*] (addition of numbers is commutative) = ([*bij*] + [*aij*]) = B + A
- (ii) **Associative Law** For any three matrices A = [*aij*], B = [*bij*], C = [*cij*] of the same order, say *m* × *n*, (A + B) + C = A + (B + C).

$$\begin{aligned} \text{Now} \quad & (\mathbf{A} + \mathbf{B}) + \mathbf{C} = ([a\_{\boldsymbol{y}}] + [b\_{\boldsymbol{y}}]) + [c\_{\boldsymbol{y}}] \\ &= [a\_{\boldsymbol{y}} + b\_{\boldsymbol{y}}] + [c\_{\boldsymbol{y}}] = [(a\_{\boldsymbol{y}} + b\_{\boldsymbol{y}}) + c\_{\boldsymbol{y}}] \\ &= [a\_{\boldsymbol{y}} + (b\_{\boldsymbol{y}} + c\_{\boldsymbol{y}})] \\ &= [a\_{\boldsymbol{y}}] + [(b\_{\boldsymbol{y}} + c\_{\boldsymbol{y}})] = [a\_{\boldsymbol{y}}] + ([b\_{\boldsymbol{y}}] + [c\_{\boldsymbol{y}}]) = \mathbf{A} + (\mathbf{B} + \mathbf{C}) \end{aligned}$$

- (iii) **Existence of additive identity** Let A = [*aij*] be an *m* × *n* matrix and O be an *m* × *n* zero matrix, then A + O = O + A = A. In other words, O is the additive identity for matrix addition.
- (iv) **The existence of additive inverse** Let A = [*aij*] *m* × *n* be any matrix, then we have another matrix as – A = [– *aij*] *m* × *n* such that A + (– A) = (– A) + A= O. So – A is the additive inverse of A or negative of A.

#### **3.4.4** *Properties of scalar multiplication of a matrix*

If A = [*aij*] and B = [*bij*] be two matrices of the same order, say *m* × *n*, and *k* and *l* are scalars, then

(i) *k*(A +B) = *k* A + *k*B, (ii) (*k* + *l*)A = *k* A + *l* A

$$\begin{aligned} \text{(ii)} \quad &k \text{ (A + B)} = k \text{ ([}a\_{\dot{y}}\text{]} + [b\_{\dot{y}}] \text{)}\\ &= k \text{ [}a\_{\dot{y}} + b\_{\dot{y}}] \text{ = [}k \text{ (}a\_{\dot{y}} + b\_{\dot{y}}] \text{]} = \text{[}(k \ a\_{\dot{y}}) + (k \ b\_{\dot{y}}) \text{]}\\ &= \text{[}k \ a\_{\dot{y}}\text{]} + [k \ b\_{\dot{y}}] = k \text{ [}a\_{\dot{y}}\text{]} + k \text{ [}b\_{\dot{y}}\text{]} = k \text{A} + k \text{\bar{B}} \end{aligned}$$

$$\begin{aligned} \text{(iii)} \quad &(k+l) \text{ A} = (k+l) \begin{bmatrix} a\_{ij} \end{bmatrix} \\ &= \begin{bmatrix} (k+l) \ a\_{ij} \end{bmatrix} + \begin{bmatrix} k \ a\_{ij} \end{bmatrix} + \begin{bmatrix} l \ a\_{ij} \end{bmatrix} = k \begin{bmatrix} a\_{ij} \end{bmatrix} + \begin{bmatrix} l \ a\_{ij} \end{bmatrix} = k \text{ A} + l \text{ A} \end{aligned}$$

**Example 8** If 8 0 2 2 A 4 2 and B 4 2 3 6 5 1 − = − = − , then find the matrix X, such that

2A + 3X = 5B.

#### **Solution** We have 2A + 3X = 5B

or 2A + 3X – 2A = 5B – 2A

or 2A – 2A + 3X = 5B – 2A (Matrix addition is commutative)

- or X = 1 3 (5B – 2A)
- or O + 3X = 5B 2A (– 2A is the additive inverse of 2A) or 3X = 5B – 2A (O is the additive identity)
- or

$$\mathbf{X} = \frac{1}{3} \left( \mathbf{5} \begin{bmatrix} 2 & -2 \\ 4 & 2 \\ -5 & 1 \end{bmatrix} - 2 \begin{bmatrix} 8 & 0 \\ 4 & -2 \\ 3 & 6 \end{bmatrix} \right) = \frac{1}{3} \left( \begin{bmatrix} 10 & -10 \\ 20 & 10 \\ -25 & 5 \end{bmatrix} + \begin{bmatrix} -16 & 0 \\ -8 & 4 \\ -6 & -12 \end{bmatrix} \right)$$

$$\mathbf{I} = \frac{1}{3} \begin{bmatrix} 10 - 16 & -10 + 0 \\ 20 - 8 & 10 + 4 \\ -25 - 6 & 5 - 12 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} -6 & -10 \\ 12 & 14 \\ -31 & -7 \end{bmatrix} = \begin{bmatrix} -2 & \frac{-10}{3} \\ 4 & \frac{14}{3} \\ \frac{-31}{3} & \frac{-7}{3} \end{bmatrix}$$

.

.

$$\text{Example 9 Find } \mathbf{X} \text{ and } \mathbf{Y}, \text{ if } \mathbf{X} + \mathbf{Y} = \begin{bmatrix} 5 & 2 \\ 0 & 9 \end{bmatrix} \text{ and } \mathbf{X} - \mathbf{Y} = \begin{bmatrix} 3 & 6 \\ 0 & -1 \end{bmatrix}.$$

**Solution** We have ( ) ( ) 5 2 3 6 X Y X Y 0 9 0 1 + + − = + <sup>−</sup>

$$\text{or}$$

$$\begin{aligned} \text{or} \qquad &(\mathbf{X} + \mathbf{X}) + (\mathbf{Y} - \mathbf{Y}) = \begin{bmatrix} \mathbf{8} & \mathbf{8} \\ \mathbf{0} & \mathbf{8} \end{bmatrix} \Longrightarrow & \mathbf{2X} = \begin{bmatrix} \mathbf{8} & \mathbf{8} \\ \mathbf{0} & \mathbf{8} \end{bmatrix}, \\ \text{or} \qquad & \mathbf{X} = \frac{1}{2} \begin{bmatrix} \mathbf{8} & \mathbf{8} \\ \mathbf{0} & \mathbf{8} \end{bmatrix} \equiv \begin{bmatrix} \mathbf{4} & \mathbf{4} \\ \mathbf{0} & \mathbf{4} \end{bmatrix} \end{aligned}$$

Also (X + Y) – (X – Y) = 5 2 3 6

or (X – X) + (Y + Y) = 5 3 2 6 0 9 1 − − <sup>+</sup> ⇒ 2 4 2Y 0 10 − <sup>=</sup>

0 9 0 1 <sup>−</sup> <sup>−</sup>

$$\text{or}\\
\qquad \qquad \qquad \lor \quad \bigvee \quad \bigvee \\
\qquad \qquad \quad \text{Y} = \frac{1}{2} \begin{bmatrix} 2 & -4 \\ 0 & 10 \end{bmatrix} = \begin{bmatrix} 1 & -2 \\ 0 & 5 \end{bmatrix} \\
$$

**Example 10** Find the values of *x* and *y* from the following equation:

$$2\begin{bmatrix} \times & \mathbf{5} \\ \mathbf{7} & \mathbf{y} - \mathbf{3} \end{bmatrix} + \begin{bmatrix} \mathbf{3} & -4 \\ 1 & \mathbf{2} \end{bmatrix} = \begin{bmatrix} 7 & 6 \\ 15 & 14 \end{bmatrix}$$

**Solution** We have

$$2\begin{bmatrix} \mathbf{x} & \mathbf{S} \\ \mathbf{7} & \mathbf{y} - \mathbf{3} \end{bmatrix} + \begin{bmatrix} \mathbf{3} & -4 \\ \mathbf{1} & \mathbf{2} \end{bmatrix} = \begin{bmatrix} 7 & 6 \\ 15 & 14 \end{bmatrix} \Rightarrow \begin{bmatrix} 2\mathbf{x} & 10 \\ 14 & 2\mathbf{y} - 6 \end{bmatrix} + \begin{bmatrix} \mathbf{3} & -4 \\ \mathbf{1} & \mathbf{2} \end{bmatrix} = \begin{bmatrix} 7 & 6 \\ 15 & 14 \end{bmatrix}$$

$$\begin{aligned} \text{or} \qquad \begin{bmatrix} 2x+3 & 10-4 \\ 14+1 & 2y-6+2 \end{bmatrix} &= \begin{bmatrix} 7 & 6 \\ 15 & 14 \end{bmatrix} \Rightarrow \begin{bmatrix} 2x+3 & 6 \\ 15 & 2y-4 \end{bmatrix} = \begin{bmatrix} 7 & 6 \\ 15 & 14 \end{bmatrix} \\ \text{or} \qquad \begin{aligned} 2x+3 & = 7 & \text{and} \qquad 2y-4=14 \\ 2x=7-3 & \text{and} \qquad 2y=18 \\ x=\frac{4}{2} & \text{and} \qquad y=\frac{18}{2} \end{aligned} \\ \text{i.e.} \qquad \begin{aligned} \text{x}=\frac{4}{2} & \text{and} \qquad y=9. \end{aligned}$$

**Example 11** Two farmers Ramkishan and Gurcharan Singh cultivates only three varieties of rice namely Basmati, Permal and Naura. The sale (in Rupees) of these varieties of rice by both the farmers in the month of September and October are given by the following matrices A and B.

| September Sales (in Rupees) |         |        |       |                          |  |
|-----------------------------|---------|--------|-------|--------------------------|--|
|                             | Basmati | Permal | Naura |                          |  |
|                             | 10,000  | 20,000 |       | 30,000   Ramkishan       |  |
|                             | 50,000  | 30,000 |       | 10,000   Gurcharan Singh |  |

|   | Basmatı | Permal | Naura |                          |
|---|---------|--------|-------|--------------------------|
| B | 5000    | 10,000 |       | 6000   Ramkishan         |
|   | 20,000  | 10,000 |       | 10,000   Gurcharan Singh |

- (i) Find the combined sales in September and October for each farmer in each variety.
- (ii) Find the decrease in sales from September to October.
- (iii) If both farmers receive 2% profit on gross sales, compute the profit for each farmer and for each variety sold in October.

#### **Solution**

(i) Combined sales in September and October for each farmer in each variety is given by

|         | Basmatı | Permal Naura                                                                                                                                                                   |                           |
|---------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| A + B = | 15,000  | 30,000 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | 36,000   Ramkishan        |
|         | 70,000  | 40,000 -                                                                                                                                                                       | 20,000    Gurcharan Singh |

(ii) Change in sales from September to October is given by

$$\mathbf{A} - \mathbf{B} = \begin{bmatrix} \text{Basmat} & \text{Perman} & \text{Naura} \\ 5000 & 10,000 & 24,000 \\ 30,000 & 20,000 & 0 \end{bmatrix} \text{Ramikishan}$$

$$\begin{aligned} \text{(iii)} \quad &2\% \text{ of B} = \frac{2}{100} \times \mathbf{B} = 0.02 \times \mathbf{B} \\ &= 0.02 \begin{bmatrix} \text{Basmat} & \text{Perman} & \text{Naura} \\ 5000 & 10,000 & 6000 \\ 20,000 & 10,000 & 10,000 \end{bmatrix} \text{Ramikishan} \\ &= \begin{bmatrix} \text{Basmat} & \text{Perman} & \text{Naura} \\ 100 & 200 & 120 \\ 400 & 700 & 200 \end{bmatrix} \text{Ramikishan} \end{aligned}$$

Thus, in October Ramkishan receives ` 100, ` 200 and ` 120 as profit in the sale of each variety of rice, respectively, and Grucharan Singh receives profit of `400, ` 200 and ` 200 in the sale of each variety of rice, respectively.

#### **3.4.5** *Multiplication of matrices*

Suppose Meera and Nadeem are two friends. Meera wants to buy 2 pens and 5 story books, while Nadeem needs 8 pens and 10 story books. They both go to a shop to enquire about the rates which are quoted as follows:

Pen – ` 5 each, story book – ` 50 each.

How much money does each need to spend? Clearly, Meera needs ` (5 × 2 + 50 × 5) that is ` 260, while Nadeem needs (8 × 5 + 50 × 10) `, that is ` 540. In terms of matrix representation, we can write the above information as follows:

**Requirements Prices per piece (in Rupees) Money needed (in Rupees)**

| 2<br>      | 5<br>       | 5<br><br>         | ×<br>+<br>×<br>5<br>2<br>5<br>50<br>260<br><br><br><br><br>=                 |
|-------------|--------------|---------------------|----------------------------------------------------------------------------------|
| <br>8<br> | <br>10<br> | <br><br>50<br>  | <br><br><br><br>×<br>+<br>×<br>8<br>5<br>10<br>50<br>540<br><br><br><br> |

Suppose that they enquire about the rates from another shop, quoted as follows: pen – ` 4 each, story book – ` 40 each.

Now, the money required by Meera and Nadeem to make purchases will be respectively ` (4 × 2 + 40 × 5) = ` 208 and ` (8 × 4 + 10 × 40) = ` 432

Again, the above information can be represented as follows:

**Requirements Prices per piece (in Rupees) Money needed (in Rupees)**

$$
\begin{bmatrix} \mathbf{2} & \mathbf{5} \\ \mathbf{8} & \mathbf{10} \end{bmatrix} \qquad \qquad \qquad \qquad \begin{bmatrix} \mathbf{4} \\ \mathbf{40} \end{bmatrix} \qquad \qquad \qquad \qquad \qquad \begin{bmatrix} \mathbf{4} \times \mathbf{2} + \mathbf{40} \times \mathbf{5} \\ \mathbf{8} \times \mathbf{4} + \mathbf{10} \times \mathbf{4} \mathbf{0} \end{bmatrix} = \begin{bmatrix} \mathbf{208} \\ \mathbf{432} \end{bmatrix}
$$

Now, the information in both the cases can be combined and expressed in terms of matrices as follows:

**Requirements Prices per piece (in Rupees) Money needed (in Rupees)**

| <br>2<br>5<br><br><br><br>8<br>10<br><br> | <br>5<br>4<br><br><br><br>50<br>40<br><br> | ×<br>+<br>×<br>×<br>+<br>×<br><br>5<br>2<br>5<br>50<br>4<br>2<br>40<br>5<br><br><br><br>×<br>+<br>×<br>×<br>+<br>×<br>8<br>5<br>10<br>5 0<br>8<br>4<br>10<br>4 0<br><br> |
|-------------------------------------------------|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                 |                                                  | 260<br>208<br><br><br>=<br><br><br>540<br>432<br><br>                                                                                                                    |

The above is an example of multiplication of matrices. We observe that, for multiplication of two matrices A and B, the number of columns in A should be equal to the number of rows in B. Furthermore for getting the elements of the product matrix, we take rows of A and columns of B, multiply them element-wise and take the sum. Formally, we define multiplication of matrices as follows:

The *product* of two matrices A and B is *defined* if the number of columns of A is equal to the number of rows of B. Let A = [*aij*] be an *m* × *n* matrix and B = [*bjk*] be an *n* × *p* matrix. Then the product of the matrices A and B is the matrix C of order *m* × *p*. To get the (*i*, *k*) th element *cik* of the matrix C, we take the *i* th row of A and *k* th column of B, multiply them elementwise and take the sum of all these products. In other words, if A = [*aij*] *m* × *n* , B = [*bjk*] *n* × *p* , then the *i* th row of A is [*ai*<sup>1</sup> *ai*2 ... *ain*] and the *k* th column of

$$\mathbf{B} \text{ is } \begin{bmatrix} b\_{1k} \\ b\_{2k} \\ \vdots \\ \vdots \\ b\_{nk} \end{bmatrix}, \text{ then } \mathbf{c}\_{ik} = a\_{i1}b\_{1k} + a\_{i2}b\_{2k} + a\_{i3}b\_{3k} + \dots + a\_{in}b\_{nk} = \sum\_{j=1}^{n} a\_{ij}b\_{jk} \dots$$

The matrix C = [*cik*] *m* × *p* is the product of A and B.

$$\text{For example, if } \mathbf{C} = \begin{bmatrix} 1 & -1 & 2 \\ 0 & 3 & 4 \end{bmatrix} \text{ and } \mathbf{D} = \begin{bmatrix} 2 & 7 \\ -1 & 1 \\ 5 & -4 \end{bmatrix} \text{, then the product CD is defined.}$$

and is given by 2 7 1 1 2 CD 1 1 0 3 4 5 4 <sup>−</sup> <sup>=</sup> <sup>−</sup> <sup>−</sup> . This is a 2 × 2 matrix in which each

entry is the sum of the products across some row of C with the corresponding entries down some column of D. These four computations are

$$\begin{array}{c|c|c|c|c} \text{Entry in} & \text{Entry} & \begin{bmatrix} 1 & -1 & 2 \\ 1 & -1 & 2 \\ 0 & 3 & 4 \end{bmatrix} & \begin{bmatrix} 2 & 7 \\ -1 & 1 \\ -5 & -4 \end{bmatrix} = \begin{bmatrix} (1)(2)+(-1)(-1)+(2)(5) & ? \\ ? & ? & ? \\ ? & ? & ? \end{bmatrix} \\\\ \text{Entry} & \text{Error} & \begin{bmatrix} 1 & -1 & 2 \\ 0 & 3 & 4 \end{bmatrix} & \begin{bmatrix} 2 & 7 \\ -1 & 1 \\ 5 & -4 \end{bmatrix} = \begin{bmatrix} 13 & (1)(7)+(-1)(1)+2(-4) \\ ? & ? \end{bmatrix} \\\\ \text{Entry in} & \begin{bmatrix} 1 & -1 & 2 \\ 0 & 3 & 4 \end{bmatrix} & \begin{bmatrix} 2 & 7 \\ -1 & 1 \\ 5 & -4 \end{bmatrix} = \begin{bmatrix} 13 & & -2 \\ 0(2)+3(-1)+4(5) & ? \end{bmatrix} \\\\ \text{Entry in} & \text{Error} & \begin{bmatrix} 1 & -1 & 2 \\ 0 & 3 & 4 \end{bmatrix} & \begin{bmatrix} 2 & 7 \\ -1 & 1 \\ 5 & -4 \end{bmatrix} = \begin{bmatrix} 13 & & -2 \\ 17 & 0 & (7)+3(1)+4(-4) \end{bmatrix} \\\\ \text{Thus } \text{CD} &= \begin{bmatrix} 13 & & 2 \\ 17 & -13 \end{bmatrix} \\\\ \text{Example 12 Find AB, if A} = \begin{bmatrix} 6 & 9 \\ 2 & 3 \end{bmatrix} \text{ and B} = \begin{bmatrix} 2 & 6 & 0 \\ 7 & 9 & 8 \end{bmatrix}. \end{array}$$

**Solution** The matrix A has 2 columns which is equal to the number of rows of B. Hence AB is defined. Now

$$\begin{aligned} \mathbf{AB} &= \begin{bmatrix} 6(2) + 9(7) & 6(6) + 9(9) & 6(0) + 9(8) \\ 2(2) + 3(7) & 2(6) + 3(9) & 2(0) + 3(8) \end{bmatrix} \\\\ &= \begin{bmatrix} 12 + 63 & 36 + 81 & 0 + 72 \\ 4 + 21 & 12 + 27 & 0 + 24 \end{bmatrix} = \begin{bmatrix} 75 & 117 & 72 \\ 25 & 39 & 24 \end{bmatrix} \end{aligned}$$

*Remark* If AB is defined, then BA need not be defined. In the above example, AB is defined but BA is not defined because B has 3 column while A has only 2 (and not 3) rows. If A, B are, respectively *m* × *n*, *k* × *l* matrices, then both AB and BA are defined **if and only if** *n* = *k* and *l* = *m*. In particular, if both A and B are square matrices of the same order, then both AB and BA are defined.

#### **Non-commutativity of multiplication of matrices**

Now, we shall see by an example that even if AB and BA are both defined, it is not necessary that AB = BA.

$$\text{Example 13: If } \mathbf{A} = \begin{bmatrix} 1 & -2 & 3 \\ -4 & 2 & 5 \end{bmatrix} \text{ and } \mathbf{B} = \begin{bmatrix} 2 & 3 \\ 4 & 5 \\ 2 & 1 \end{bmatrix}, \text{ then find AB, BA. Show that}$$

#### AB ≠ BA.

**Solution** Since A is a 2 × 3 matrix and B is 3 × 2 matrix. Hence AB and BA are both defined and are matrices of order 2 × 2 and 3 × 3, respectively. Note that

$$\mathbf{AB} = \begin{bmatrix} 1 & -2 & 3 \\ -4 & 2 & 5 \end{bmatrix} \begin{bmatrix} 2 & 3 \\ 4 & 5 \\ 2 & 1 \end{bmatrix} = \begin{bmatrix} 1 \\ -8 + 8 + 10 & -12 + 10 + 5 \\ -8 + 8 + 10 & -12 + 10 + 5 \end{bmatrix} = \begin{bmatrix} 0 & -4 \\ 10 & 3 \end{bmatrix}$$

and

$$\mathbf{BA} = \begin{bmatrix} 2 & 3 \\ 4 & 5 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} 1-2 & 3 \\ -4 & 2 \\ -4 & 2 \end{bmatrix} = \begin{bmatrix} 2-12 & -4+6 & 6+15 \\ 4+20 & -8+10 & 12+25 \\ 2-4 & -4+2 & 6+5 \end{bmatrix} = \begin{bmatrix} -10 & 2 & 21 \\ -16 & 2 & 37 \\ -2 & -2 & 11 \end{bmatrix}$$

Clearly AB ≠ BA

In the above example both AB and BA are of different order and so AB ≠ BA. But one may think that perhaps AB and BA could be the same if they were of the same order. But it is not so, here we give an example to show that even if AB and BA are of same order they may not be same.

$$\begin{array}{c} \begin{array}{c} \begin{array}{c} \\ \end{array} \end{array} \text{Example 14.} \\ \begin{array}{c} \\ \end{array} \text{A} = \begin{bmatrix} 1 & 0 \\ 0 & -1 \\ \end{bmatrix} \text{ and } \begin{array}{c} \\ \end{array} \\ \begin{array}{c} \\ \end{array} \text{and } \begin{array}{c} \\ \end{array} \text{B} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \\ \end{bmatrix}, \text{ then } \begin{array}{c} \\ \text{AB} = \begin{bmatrix} 0 & 1 \\ -1 & 0 \\ \end{bmatrix}. \\ \text{and } \begin{array}{c} \\ \end{array} \text{BA} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \\ \end{bmatrix}. \text{ Clearly } \text{AB} \neq \text{BA}. \end{array} \end{array}$$

Thus matrix multiplication is not commutative.

A**Note** This does not mean that AB ≠ BA for every pair of matrices A, B for which AB and BA, are defined. For instance,

$$\begin{array}{c} \text{If} \quad \mathbf{A} = \begin{bmatrix} 1 & \mathbf{0} \\ \mathbf{0} & \mathbf{2} \end{bmatrix}, \quad \mathbf{B} = \begin{bmatrix} \mathbf{3} & \mathbf{0} \\ \mathbf{0} & \mathbf{4} \end{bmatrix}, \text{ then } \mathbf{AB} = \mathbf{B} \mathbf{A} = \begin{bmatrix} \mathbf{3} & \mathbf{0} \\ \mathbf{0} & \mathbf{8} \end{bmatrix}. \end{array}$$

Observe that multiplication of diagonal matrices of same order will be commutative.

#### **Zero matrix as the product of two non zero matrices**

We know that, for real numbers *a*, *b* if *ab* = 0, then either *a* = 0 or *b* = 0. This need not be true for matrices, we will observe this through an example.

$$\begin{aligned} \text{Example 15 Find AB, if } \mathbf{A} = \begin{bmatrix} \mathbf{0} & -1 \\ \mathbf{0} & 2 \end{bmatrix} \text{ and } \mathbf{B} = \begin{bmatrix} 3 & 5 \\ 0 & 0 \end{bmatrix}. \\ \text{Solution We have } \mathbf{A}\mathbf{B} = \begin{bmatrix} \mathbf{0} & -1 \\ \mathbf{0} & 2 \end{bmatrix} \begin{bmatrix} 3 & 5 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} \mathbf{0} & \mathbf{0} \\ \mathbf{0} & \mathbf{0} \end{bmatrix}. \end{aligned}$$

Thus, if the product of two matrices is a zero matrix, it is not necessary that one of the matrices is a zero matrix.

#### **3.4.6** *Properties of multiplication of matrices*

The multiplication of matrices possesses the following properties, which we state without proof.

1. **The associative law** For any three matrices A, B and C. We have

(AB) C = A (BC), whenever both sides of the equality are defined.

2. **The distributive law** For three matrices A, B and C.

$$\text{(i)}\ \text{A} \ (\text{B} + \text{C}) = \text{AB} + \text{AC}$$

- (ii) (A+B) C = AC + BC, whenever both sides of equality are defined.
- 3. **The existence of multiplicative identity** For every square matrix A, there exist an identity matrix of same order such that IA = AI = A.

Now, we shall verify these properties by examples.

$$\begin{array}{cccc} \text{Example 1 6} & \text{If} & \text{A} = \begin{bmatrix} 1 & 1 & -1 \\ 2 & 0 & 3 \\ 3 & -1 & 2 \end{bmatrix}, & \text{B} = \begin{bmatrix} 1 & 3 \\ 0 & 2 \\ -1 & 4 \end{bmatrix} \text{ and } & \text{C} = \begin{bmatrix} 1 & 2 & 3 & -4 \\ 2 & 0 & -2 & 1 \end{bmatrix}, & \text{find } \end{array}$$

A(BC), (AB)C and show that (AB)C = A(BC).

**Solution** We have 1 1 1 1 3 1 0 1 3 2 4 2 1 AB 2 0 3 0 2 2 0 3 6 0 12 1 18 3 1 2 1 4 3 0 2 9 2 8 1 15 − + + + − <sup>=</sup> = + − + + = − − − + − − + (AB) (C) 2 1 2 2 4 0 6 2 8 1 1 2 3 4 1 18 1 36 2 0 3 36 4 18 2 0 2 1 1 15 1 30 2 0 3 30 4 15 + + − − + − = − = − + − + − − + − + + − − + = 4 4 4 7 35 2 39 22 31 2 27 11 − − − − Now BC = 1 3 1 6 2 0 3 6 4 3 1 2 3 4 0 2 0 4 0 0 0 4 0 2 2 0 2 1 1 4 1 8 2 0 3 8 4 4 + + − − + − = + + − + − − − + − + − − + = 7 2 3 1 4 0 4 2 7 2 11 8 − − − − − Therefore A(BC) = 1 1 1 7 2 3 1 2 0 3 4 0 4 2 3 1 2 7 2 11 8 − − − − − − − = 7 4 7 2 0 2 3 4 11 1 2 8 14 0 21 4 0 6 6 0 33 2 0 24 21 4 14 6 0 4 9 4 22 3 2 16 + − + + − − + − + − + + + − − + − − + + − + + − − + − − − + = 4 4 4 7 35 2 39 22 31 2 27 11 − − − − . Clearly, (AB) C = A (BC)

$$\text{Example 17 If } \mathbf{A} = \begin{bmatrix} 0 & 6 & 7 \\ -6 & 0 & 8 \\ 7 & -8 & 0 \end{bmatrix}, \mathbf{B} = \begin{bmatrix} 0 & 1 & 1 \\ 1 & 0 & 2 \\ 1 & 2 & 0 \end{bmatrix}, \mathbf{C} = \begin{bmatrix} 2 \\ -2 \\ 3 \end{bmatrix}.$$

Calculate AC, BC and (A + B)C. Also, verify that (A + B)C = AC + BC

**Solution** Now, 0 7 8 A +B 5 0 10 8 6 0 = − − So (A + B) C = 0 7 8 2 0 14 24 10 5 0 10 2 10 0 30 20 8 6 0 3 16 12 0 28 − + − − = − + + = − + + Further AC = 0 6 7 2 0 12 21 9 6 0 8 2 12 0 24 12 7 8 0 3 14 16 0 30 − + − − = − + + = − + + and BC = 0 1 1 2 0 2 3 1 1 0 2 2 2 0 6 8 1 2 0 3 2 4 0 2 − + − = + + = − + − So AC + BC = 9 1 10 12 8 20 30 2 28 + = − Clearly, (A + B) C = AC + BC **Example 18** If 1 2 3 A 3 2 1 4 2 1 = − , then show that A<sup>3</sup> – 23A – 40 I = O **Solution** We have <sup>2</sup> 1 2 3 1 2 3 19 4 8 A A.A 3 2 1 3 2 1 1 12 8 4 2 1 4 2 1 14 6 15 = = − − = 

So A<sup>3</sup> = A A<sup>2</sup> = 1 2 3 19 4 8 63 46 69 3 2 1 1 12 8 69 6 23 4 2 1 14 6 15 92 46 63 − = − 

Now

$$\mathbf{A}^3 - 23\mathbf{A} - 40\mathbf{I} = \begin{bmatrix} 63 & 46 & 69 \\ 69 & -6 & 23 \\ 92 & 46 & 63 \end{bmatrix} - 23 \begin{bmatrix} 1 & 2 & 3 \\ 3 & -2 & 1 \\ 4 & 2 & 1 \end{bmatrix} - 40 \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

$$= \begin{bmatrix} 63 & 46 & 69 \\ 69 & -6 & 23 \\ 92 & 46 & 63 \end{bmatrix} - \begin{bmatrix} -23 & -46 & -69 \\ -69 & 46 & -23 \\ -92 & -46 & -23 \end{bmatrix} + \begin{bmatrix} -40 & 0 & 0 \\ 0 & -40 & 0 \\ 0 & 0 & -40 \end{bmatrix}$$

$$= \begin{bmatrix} 63 - 23 - 40 & 46 - 46 + 0 & 69 - 69 + 0 \\ 69 - 69 + 0 & -6 + 46 - 40 & 23 - 23 + 0 \\ 92 - 92 + 0 & 46 - 46 + 0 & 63 - 23 - 40 \end{bmatrix}$$

$$= \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$

**Example 19** In a legislative assembly election, a political group hired a public relations firm to promote its candidate in three ways: telephone, house calls, and letters. The cost per contact (in paise) is given in matrix A as

|     | Cost per contact        |           |
|-----|-------------------------|-----------|
|     | <br>40<br>            | Telephone |
| A = | <br><br>100<br><br> | Housecall |
|     | <br><br>50<br><br>  | Letter    |

The number of contacts of each type made in two cities X and Y is given by

$$\mathbf{B} = \begin{bmatrix} 1000 & \mathbf{S}00 & \mathbf{S}000 \\ 1000 & \mathbf{S}00 & \mathbf{S}000 \\ 3000 & 1000 & 10,000 \end{bmatrix} \xrightarrow{\mathbf{X}} \mathbf{Y}. \text{ Find the total amount spent by the group in the two}$$

cities X and Y.

**Solution** We have

$$\begin{aligned} \text{BA} &= \begin{bmatrix} 40,000 + 50,000 + 250,000 \\ 120,000 + 100,000 + 500,000 \end{bmatrix} \xrightarrow{} \text{Y} \\ &= \begin{bmatrix} 340,000 \\ 720,000 \end{bmatrix} \xrightarrow{} \text{Y} \end{aligned}$$

So the total amount spent by the group in the two cities is 340,000 paise and 720,000 paise, i.e., `3400 and ` 7200, respectively.

**EXERCISE 3.2**

$$\begin{array}{c} \begin{array}{ccc} \cdot & \cdot\\ \cdot & \text{Let} & \mathbf{A} = \begin{bmatrix} 2 & 4\\ 3 & 2 \end{bmatrix}, \mathbf{B} = \begin{bmatrix} 1 & 3\\ -2 & 5 \end{bmatrix}, \mathbf{C} = \begin{bmatrix} -2 & 5\\ 3 & 4 \end{bmatrix} \end{array}$$

Find each of the following:

- (i) A + B (ii) A B (iii) 3A C
- (iv) AB (v) BA
- **2.** Compute the following:

$$\begin{array}{c} \text{(i)} \quad \begin{bmatrix} a & b \\ -b & a \end{bmatrix} + \begin{bmatrix} a & b \\ b & a \end{bmatrix} \\ \text{(ii)} \quad \begin{bmatrix} -1 & 4 & -6 \\ 8 & 5 & (6 & ) \\ 2 & 8 & 5 & (6 & ) \end{bmatrix} \begin{bmatrix} 2 & 7 & 6 \\ -2ac & a^2 + b^2 & \\ -2ac & -2ab \end{bmatrix} \\ \text{(iii)} \quad \begin{bmatrix} -1 & 4 & -6 \\ 8 & 5 & (6 & ) \\ 2 & 8 & 5 & (6 & ) \end{bmatrix} \begin{bmatrix} 12 & 7 & 6 \\ 8 & 0 & 5 & (\text{iv}) \\ 3 & 2 & (4 & ) \end{bmatrix} \begin{bmatrix} \cos^2 x & \sin^2 x \\ \sin^2 x & \cos^2 x \end{bmatrix} + \begin{bmatrix} \sin^2 x & \cos^2 x \\ \cos^2 x & \sin^2 x \end{bmatrix} \end{array}$$

**3.** Compute the indicated products.

$$\begin{array}{c} \text{(i)} \quad \begin{bmatrix} a & b \\ -b & a \end{bmatrix} \begin{bmatrix} a & -b \\ b & a \end{bmatrix} \end{array} \text{(ii)} \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \begin{bmatrix} 2 & 3 & 4 \end{bmatrix} \qquad \text{(iii)} \begin{bmatrix} 1 & -2 & 5 \\ 2 & 3 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{bmatrix} \\\\ \text{(iv)} \begin{bmatrix} 2 & 3 & 4 \\ 3 & 4 & 5 \\ 4 & 5 & 6 \end{bmatrix} \begin{bmatrix} 1 & -3 & 5 \\ 0 & 2 & 4 \\ 3 & 0 & 5 \end{bmatrix} \qquad \text{(v)} \begin{bmatrix} 2 & 1 \\ 3 & 2 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 1 \\ -1 & 2 & 1 \end{bmatrix} \\\\ \text{(vi)} \begin{bmatrix} 3 & -1 & 3 \\ -1 & 0 & 2 \end{bmatrix} \begin{bmatrix} 2 & -3 \\ 1 & 0 \\ 3 & 1 \end{bmatrix} \end{array} \text{(vi)} \begin{bmatrix} 2 & 3 \\ 1 & 0 \\ 3 & 1 \end{bmatrix} \end{array}$$

**4.** If 1 2 3 3 1 2 4 1 2 A 5 0 2 , B 4 2 5 and C 0 3 2 1 1 1 2 0 3 1 2 3 − − = = = − − , then compute (A+B) and (B – C). Also, verify that A + (B – C) = (A + B) – C. **5.** If 2 5 2 3 <sup>1</sup> <sup>1</sup> 3 3 5 5 1 2 4 1 2 4 <sup>A</sup> and B 3 3 3 5 5 5 7 2 7 6 2 <sup>2</sup> 3 3 5 5 5 = = , then compute 3A – 5B. **6.** Simplify cos sin sin cos cos + sin sin cos cos sin θ θ θ − θ θ θ − θ θ θ θ **7.** Find X and Y, if (i) 7 0 3 0 X + Y and X – Y 2 5 0 3 <sup>=</sup> <sup>=</sup> (ii) 2 3 2 2 2X + 3Y and 3X 2Y 4 0 1 5 − <sup>=</sup> + = <sup>−</sup> **8.** Find X, if Y = 3 2 1 4 and 2X + Y = 1 0 3 2 <sup>−</sup> **9.** Find *x* and *y*, if 1 3 0 5 6 2 0 1 2 1 8 *y x* + = **10.** Solve the equation for *x*, *y*, *z* and *t*, if 1 1 3 5 2 3 3 0 2 4 6 *x z y t* − + = **11.** If 2 1 10 3 1 5 *x y* − + = , find the values of *x* and *y*. **12.** Given 6 4 3 1 2 3 *x y x x y z w w z w* + = + − + , find the values of *x*, *y*, *z* and *w*.

$$\begin{array}{ll} \text{13.} \quad \text{If } \operatorname{F}(\mathbf{x}) = \begin{bmatrix} \cos x & -\sin x & 0\\ \sin x & \cos x & 0\\ 0 & 0 & 1 \end{bmatrix}, \text{ show that } \operatorname{F}(\mathbf{x}) \operatorname{F}(\mathbf{y}) = \operatorname{F}(\mathbf{x} + \mathbf{y}). \text{ 2.} \\\\ \text{14.} \quad \text{If } \operatorname{F}(\mathbf{x}) = \operatorname{F}(\mathbf{x} + \mathbf{y}). \text{ 3.} \end{array}$$

**14.** Show that

(i) 5 1 2 1 2 1 5 1 6 7 3 4 3 4 6 7 − − <sup>≠</sup> (ii) 1 2 3 1 1 0 1 1 0 1 2 3 0 1 0 0 1 1 0 1 1 0 1 0 1 1 0 2 3 4 2 3 4 1 1 0 − − − ≠ − **15.** Find A<sup>2</sup> – 5A + 6I, if 2 0 1 A 2 1 3 1 1 0 = − **16.** If 1 0 2 A 0 2 1 2 0 3 = , prove that A<sup>3</sup> – 6A<sup>2</sup> + 7A + 2I = 0 **17.** If 3 2 1 0 A and I= 4 2 0 1 − <sup>=</sup> <sup>−</sup> , find *k* so that A<sup>2</sup> = *k*A – 2I **18.** If 0 tan <sup>2</sup> <sup>A</sup> tan 0 2 α − = α and I is the identity matrix of order 2, show that I + A = (I – A) cos sin sin cos α − α α α

**19.** A trust fund has ` 30,000 that must be invested in two different types of bonds. The first bond pays 5% interest per year, and the second bond pays 7% interest per year. Using matrix multiplication, determine how to divide ` 30,000 among the two types of bonds. If the trust fund must obtain an annual total interest of: (a) `1800 (b) `2000

**20.** The bookshop of a particular school has 10 dozen chemistry books, 8 dozen physics books, 10 dozen economics books. Their selling prices are `80, `60 and ` 40 each respectively. Find the total amount the bookshop will receive from selling all the books using matrix algebra.

Assume X, Y, Z, W and P are matrices of order 2 × *n*, 3 × *k*, 2 × *p*, *n* × 3 and *p* × *k*, respectively. Choose the correct answer in Exercises 21 and 22.

- **21.** The restriction on *n*, *k* and *p* so that PY + WY will be defined are:
	- (A) *k* = 3, *p* = *n* (B) *k* is arbitrary, *p* = 2
	- (C) *p* is arbitrary, *k* = 3 (D) *k* = 2, *p* = 3
- **22.** If *n* = *p*, then the order of the matrix 7X 5Z is:

(A) *p* × 2 (B) 2 × *n* (C) *n* × 3 (D) *p* × *n*

## **3.5. Transpose of a Matrix**

In this section, we shall learn about transpose of a matrix and special types of matrices such as symmetric and skew symmetric matrices.

**Definition 3** If A = [*aij*] be an *m* × *n* matrix, then the matrix obtained by interchanging the rows and columns of A is called the *transpose* of A. Transpose of the matrix A is denoted by A′ or (A<sup>T</sup> ). In other words, if A = [*aij*] *m* × *n* , then A′ = [*aji*] *n* × *m* . For example,

$$\begin{aligned} \text{if } \mathbf{A} = \begin{bmatrix} 3 & 5 \\ \sqrt{3} & 1 \\ 0 & -1 \\ \mathbf{5} \end{bmatrix}\_{3 \times 2}, \text{ then } \mathbf{A}' = \begin{bmatrix} 3 & \sqrt{3} & 0 \\ 5 & 1 & \frac{-1}{5} \\ \mathbf{5} & 1 & \frac{-1}{5} \end{bmatrix}\_{2 \times 3} \end{aligned}$$

#### *3.5.1 Properties of transpose of the matrices*

We now state the following properties of transpose of matrices without proof. These may be verified by taking suitable examples.

For any matrices A and B of suitable orders, we have

- (i) (A′)′ = A, (ii) (*k*A)′ = *k*A′ (where *k* is any constant)
- (iii) (A + B)′ = A′ + B′ (iv) (A B)′ = B′ A′

**Example 20** If 3 3 2 2 1 2 A and B 4 2 0 1 2 4 − <sup>=</sup> <sup>=</sup> , verify that (i) (A′)′ = A, (ii) (A + B)′ = A′ + B′,

(iii) (*k*B)′ = *k*B′, where *k* is any constant.

#### **Solution**

(i) We have

$$\mathbf{A} = \begin{bmatrix} 3 & \sqrt{3} & 2 \\ 4 & 2 & 0 \end{bmatrix} \implies \mathbf{A}' = \begin{bmatrix} 3 & 4 \\ \sqrt{3} & 2 \\ 2 & 0 \end{bmatrix} \Longrightarrow \begin{pmatrix} \mathbf{A}' \end{pmatrix}' = \begin{bmatrix} 3 & \sqrt{3} & 2 \\ 4 & 2 & 0 \end{bmatrix} = \mathbf{A}'$$

Thus (A′)′ = A

(ii) We have

$$\mathbf{A} = \begin{bmatrix} 3 & \sqrt{3} & 2 \\ 4 & 2 & 0 \end{bmatrix}, \quad \mathbf{B} = \begin{bmatrix} 2 & -1 & 2 \\ 1 & 2 & 4 \end{bmatrix} \Rightarrow \mathbf{A} + \mathbf{B} = \begin{bmatrix} 5 & \sqrt{3} - 1 & 4 \\ 5 & 4 & 4 \end{bmatrix}$$

$$\text{Therefore } \mathbf{A} = (\mathbf{A} + \mathbf{B})' = \begin{bmatrix} 5 & \mathbf{A} \\ \sqrt{3} - 1 & 2 \\ 4 & 2 \end{bmatrix}$$

$$\text{Now } \mathbf{A}' = \begin{bmatrix} 3 & 4 \\ \sqrt{3} & 2 \\ 2 & 0 \end{bmatrix}, \mathbf{B}' = \begin{bmatrix} 2 & 1 \\ -1 & 2 \\ 2 & 4 \end{bmatrix},$$

$$\mathbf{So} \qquad \begin{array}{ccccc} \begin{pmatrix} \binom{\circ}{\circ} \\ & \mathbf{A}' + \mathbf{B}' = \mathbf{0} \\ & \mathbf{A}' + \mathbf{B}' = \mathbf{0} \\ & \mathbf{A} & \mathbf{4} \end{pmatrix} \\ \mathbf{S} = \begin{bmatrix} \mathbf{S} & \mathbf{S} \\ & \mathbf{A}' - \mathbf{1} & \mathbf{4} \\ & \mathbf{4} & \mathbf{4} \end{bmatrix} \end{array}$$

$$\begin{array}{cccc}\text{Thus} & & \begin{array}{c} \end{array} \begin{array}{c} \begin{array}{c} \text{(A)}+\text{B)'}=\text{A'}+\text{B'} \end{array} \end{array} \end{array}$$

(iii) We have

$$\begin{array}{cccc} \bigcirc & & & \mathbf{k} \mathbf{B} = k \begin{bmatrix} 2 & -1 & 2 \\ 1 & 2 & 4 \end{bmatrix} = \begin{bmatrix} 2k & -k & 2k \\ k & 2k & 4k \end{bmatrix} \\\\ \text{Then} & & (\mathbf{k} \mathbf{B})' = \begin{bmatrix} 2k & k \\ -k & 2k \\ 2k & 4k \end{bmatrix} = k \begin{bmatrix} 2 & 1 \\ -1 & 2 \\ 2 & 4 \end{bmatrix} = k \mathbf{B}' \end{array}$$

Thus (*k*B)′ = *k*B′

$$\text{Example 21: If } \mathbf{A} = \begin{bmatrix} -2 \\ 4 \\ 5 \end{bmatrix}, \mathbf{B} = \begin{bmatrix} 1 & 3 & -6 \end{bmatrix}, \text{ verify that (AB)' = B'A'.} $$

**Solution** We have

$$\mathbf{A} = \begin{bmatrix} -2 \\ 4 \\ \mathbf{S} \end{bmatrix}, \mathbf{B} = \begin{bmatrix} 1 & 3 & -6 \end{bmatrix}$$

4 1 3 6

−

=

2 6 12 4 12 24 5 15 30

− − − − 

2

 − 

5

 

then AB = [ ]

$$\begin{array}{rcl} \text{Now} & \mathbf{A}' = \begin{bmatrix} -2 \ 4 \ 5 \end{bmatrix}, & \mathbf{B}' = \begin{bmatrix} 1 \\ 3 \\ -6 \end{bmatrix} \\\\ \mathbf{B}'\mathbf{A}' = \begin{bmatrix} 1 \\ 3 \\ -2 \end{bmatrix} \begin{bmatrix} -2 \ 4 \ 5 \end{bmatrix} = \begin{bmatrix} -2 & 4 & 5 \\ -6 & 12 & 15 \end{bmatrix} = (\mathbf{A}\mathbf{B})' \end{array}$$

Clearly (AB)′ = B′A′

#### **3.6 Symmetric and Skew Symmetric Matrices**

**Definition 4** A square matrix A = [*aij*] is said to be *symmetric* if A′ = A, that is, [*aij*] = [*aji*] for all possible values of *i* and *j*.

6 12 24 30

 − − − 

$$\text{For example, } \mathbf{A} = \begin{bmatrix} \sqrt{3} & 2 & 3 \\ 2 & -1.5 & -1 \\ 3 & -1 & 1 \end{bmatrix} \text{ is a symmetric matrix as } \mathbf{A}' = \mathbf{A}'$$

**Definition 5** A square matrix A = [*aij*] is said to be *skew symmetric* matrix if A′ = – A, that is *aji* = – *aij* for all possible values of *i* and *j*. Now, if we put *i* = *j*, we have *aii* = – *aii*. Therefore 2*aii* = 0 or *aii* = 0 for all *i*'s.

This means that all the diagonal elements of a skew symmetric matrix are zero.

$$\text{For example, the matrix } \mathbf{B} = \begin{bmatrix} 0 & e & f \\ -e & 0 & g \\ -f & -g & 0 \end{bmatrix} \text{ is a skew symmetric matrix as } \mathbf{B}' = -\mathbf{B}'$$

Now, we are going to prove some results of symmetric and skew-symmetric matrices.

**Theorem 1** For any square matrix A with real number entries, A + A′ is a symmetric matrix and A – A′ is a skew symmetric matrix.

**Proof** Let B = A + A′, then

$$\begin{aligned} \mathbf{B'} &= (\mathbf{A} + \mathbf{A'})' \\ &= \mathbf{A'} + (\mathbf{A'})' \text{ (as } (\mathbf{A} + \mathbf{B})' = \mathbf{A'} + \mathbf{B'}) \\ &= \mathbf{A'} + \mathbf{A} \text{ (as } (\mathbf{A})' = \mathbf{A}) \\ &= \mathbf{A} + \mathbf{A'} \text{ (as } \mathbf{A} + \mathbf{B} = \mathbf{B} + \mathbf{A}) \\ &= \mathbf{B} \end{aligned}$$
 
$$\begin{aligned} \text{Therefore} \\ \text{Now let} \\ \mathbf{C} &= \mathbf{A} - \mathbf{A'} \\ \mathbf{C'} &= (\mathbf{A} - \mathbf{A'})' = (\mathbf{A'} - (\mathbf{A'})' \quad \text{(Why?)} \\ &= \mathbf{A'} - \mathbf{A} \quad (\text{Why?}) \\ &= -(\mathbf{A} - \mathbf{A'})' = -\mathbf{C} \end{aligned}$$
 
$$\text{Therefore}$$
 
$$\mathbf{C} = \mathbf{A} - \mathbf{A'} \text{ is a skew symmetric matrix.}$$

**Theorem 2** Any square matrix can be expressed as the sum of a symmetric and a skew symmetric matrix.

**Proof** Let A be a square matrix, then we can write

$$\mathbf{A} = \frac{1}{2}(\mathbf{A} + \mathbf{A}') + \frac{1}{2}(\mathbf{A} - \mathbf{A}')$$

From the Theorem 1, we know that (A + A′) is a symmetric matrix and (A – A′) is a skew symmetric matrix. Since for any matrix A, (*k*A)′ = *k*A′, it follows that 1 (A A ) 2 + ′

is symmetric matrix and 1 (A A ) 2 − ′ is skew symmetric matrix. Thus, any square matrix can be expressed as the sum of a symmetric and a skew symmetric matrix.

**Example 22** Express the matrix 2 2 4 B 1 3 4 1 2 3 − − = − − − as the sum of a symmetric and a

skew symmetric matrix.

**Solution** Here

$$\mathbf{B}' = \begin{bmatrix} 2 & -1 & 1 \\ -2 & 3 & -2 \\ -4 & 4 & -3 \end{bmatrix}$$

$$\text{Let } \mathbf{P} = \frac{1}{2}(\mathbf{B} + \mathbf{B}') = \frac{1}{2} \begin{bmatrix} 4 & -3 & -3 \\ -3 & 6 & 2 \\ -3 & 2 & -6 \end{bmatrix} = \begin{bmatrix} 2 & \frac{-3}{2} & \frac{-3}{2} \\ -\frac{3}{2} & 3 & 1 \\ -\frac{3}{2} & 1 & -3 \end{bmatrix},$$

$$\text{Now } \mathbf{P}' = \begin{bmatrix} 2 & \frac{-3}{2} & \frac{-3}{2} \\ \frac{-3}{2} & 3 & 1 \\ -\frac{3}{2} & 1 & -3 \end{bmatrix}$$

$$\text{Thus } \mathbf{P} = \frac{1}{2}(\mathbf{B} + \mathbf{B}') \text{ is a symmetric matrix.}$$

$$\mathbf{A} \mathbf{b} = \frac{1}{2}(\mathbf{B} - \mathbf{B}') = \frac{1}{2} \begin{bmatrix} 0 & -1 & -5 \\ 1 & 0 & 6 \\ 5 & -6 & 0 \end{bmatrix} = \begin{bmatrix} 0 & -1 & -5 \\ 1 & 0 & 3 \\ 2 & 0 & 3 \\ 2 & -3 & 0 \end{bmatrix}$$

$$\begin{array}{ccccc} & & & & 0 & \frac{1}{2} & \frac{5}{3} \\ \text{Then} & & & \mathbf{Q}' = \begin{bmatrix} 0 & \frac{1}{2} & \frac{5}{3} \\ \frac{-1}{2} & 0 & -3 \\ \frac{-5}{2} & 3 & 0 \end{bmatrix} = -\mathbf{Q} \\\hline \\ & & & \\ \hline \end{array}$$

Thus Q = 1 (B – B ) 2 ′ is a skew symmetric matrix.

$$\begin{array}{cccc} \text{Now} & \mathbf{P} + \mathbf{Q} = \begin{bmatrix} 2 & \frac{-3}{2} & \frac{-3}{2} \\ \frac{-3}{2} & 3 & 1 \\ \frac{-3}{2} & 1 & -3 \end{bmatrix} + \begin{bmatrix} 0 & \frac{-1}{2} & \frac{-5}{2} \\ \frac{1}{2} & 0 & 3 \\ \frac{-3}{2} & -3 & 0 \end{bmatrix} = \begin{bmatrix} 2 & -2 & -4 \\ -1 & 3 & 4 \\ 1 & -2 & -3 \end{bmatrix} = \mathbf{B} \end{array}$$

Thus, B is represented as the sum of a symmetric and a skew symmetric matrix.

# **EXERCISE 3.3**

**1.** Find the transpose of each of the following matrices:

$$\begin{array}{cccc} \text{(i)} & \begin{bmatrix} 5 \\ 1 \\ 2 \\ -1 \end{bmatrix} & \text{(ii)} & \begin{bmatrix} 1 & -1 \\ 2 & 3 \end{bmatrix} & \text{(iii)} & \begin{bmatrix} -1 & 5 & 6 \\ 3 & 5 & 6 \\ 2 & 3 & -1 \end{bmatrix} \\\\ \text{2.} & \text{If A} = \begin{bmatrix} -1 & 2 & 3 \\ 5 & 7 & 9 \\ -2 & 1 & 1 \end{bmatrix} & \text{(iii)} & \text{B} = \begin{bmatrix} -4 & 1 & -5 \\ 1 & 2 & 0 \\ 1 & 3 & 1 \end{bmatrix}, \text{then verify that} \\\\ \text{(i)} & \text{(A+B)'} = \text{A'+B'}, \text{ (i)} & \begin{bmatrix} 3 & 4 \\ -1 & 2 \\ -1 & 2 \end{bmatrix} & \text{(ii)} & \begin{bmatrix} (-1 & 2 & 1] \\ 1 & 2 & 3 \end{bmatrix}, \text{then verify that} \\\\ \text{3.} & \text{If A' = [-1 & 2] } & \text{and } \text{ B} = \begin{bmatrix} -1 & 2 & 1 \\ -1 & 2 & 3 \end{bmatrix}, \text{then verify that} \\ \text{(ii)} & \text{(A+B)'} = \text{A'+B'} & \text{(ii) } (\text{A} - \text{B})' = \text{A'+B'} \end{array}$$

**4.** If 2 3 1 0 A and B 1 2 1 2 − − ′ = = , then find (A + 2B)′ **5.** For the matrices A and B, verify that (AB)′ = B′A′, where (i) [ ] 1 A 4 , B 1 2 1 3 = − = − (ii) [ ] 0 A 1 , B 1 5 7 2 = = **6.** If (i) cos sin A sin cos α α = − α α , then verify that A′ A = I (ii) If sin cos A cos sin α α = − α α , then verify that A′ A = I **7.** (i) Show that the matrix 1 1 5 A 1 2 1 5 1 3 − = − is a symmetric matrix. (ii) Show that the matrix 0 1 1 A 1 0 1 1 1 0 − = − − is a skew symmetric matrix. **8.** For the matrix 1 5 A 6 7 <sup>=</sup> , verify that (i) (A + A′) is a symmetric matrix (ii) (A – A′) is a skew symmetric matrix **9.** Find ( ) <sup>1</sup> A A 2 <sup>+</sup> ′ and ( ) <sup>1</sup> A A 2 − ′ , when 0 A 0 0 *a b a c b c* = − − −

**10.** Express the following matrices as the sum of a symmetric and a skew symmetric matrix:

![](_page_34_Figure_1.jpeg)

Choose the correct answer in the Exercises 11 and 12.

- **11.** If A, B are symmetric matrices of same order, then AB BA is a
	- (A) Skew symmetric matrix (B) Symmetric matrix
		-
	- (C) Zero matrix (D) Identity matrix
- 

$$\begin{aligned} \text{12.} \quad \text{If } \mathbf{A} = \begin{bmatrix} \cos \alpha & -\sin \alpha \\ \sin \alpha & \cos \alpha \end{bmatrix}, \text{and } \mathbf{A} + \mathbf{A}' = \mathbf{I}, \text{ then the value of } \mathbf{q} \text{ is} \\ \text{(A) } \frac{\pi}{6} \\ \text{(B) } \pi \\ \text{(C) } \pi \end{aligned} \qquad \begin{aligned} \text{(A) } \mathbf{a} + \mathbf{A}' &= \mathbf{I}, \text{ then the value of } \mathbf{q} \text{ is} \\ \begin{array}{l} \text{(A) } \frac{\pi}{3} \\ \frac{\pi}{3} \\ \text{(D) } \frac{3\pi}{2} \end{array} \end{aligned}$$

# **3.7 Invertible Matrices**

**Definition 6** If A is a square matrix of order *m*, and if there exists another square matrix B of the same order *m*, such that AB = BA = I, then B is called the *inverse* matrix of A and it is denoted by A– 1. In that case A is said to be invertible.

| For example, let                                    | <br><br>−<br>2<br>3<br><br><br>2<br>3<br>A =<br>and B =<br>be two matrices.<br><br><br><br><br>−<br>1<br>2<br>1<br>2<br> <br><br>                          |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Now                                                 | −<br><br> <br><br>2<br>3<br>2<br>3<br><br> <br><br>AB =<br>−<br>1<br>2<br>1<br>2<br><br> <br>                                                              |
|                                                     | −<br>−<br>+<br><br><br><br><br>4<br>3<br>6<br>6<br>1<br>0<br>=<br>=<br>=<br>I<br><br><br><br><br>−<br>−<br>+<br>2<br>2<br>3<br>4<br>0<br>1<br><br><br><br> |
| Also                                                | <br><br>1<br>0<br>=<br>BA =<br>. Thus B is the inverse of A, in other<br>I<br><br><br>0<br>1<br>                                                                 |
| words B = A– 1 and A is inverse of B, i.e., A = B–1 |                                                                                                                                                                        |

# A**Note**

- 1. A rectangular matrix does not possess inverse matrix, since for products BA and AB to be defined and to be equal, it is necessary that matrices A and B should be square matrices of the same order.
- 2. If B is the inverse of A, then A is also the inverse of B.

**Theorem 3** (Uniqueness of inverse) Inverse of a square matrix, if it exists, is unique. **Proof** Let A = [*aij*] be a square matrix of order *m*. If possible, let B and C be two inverses of A. We shall show that B = C.

Since B is the inverse of A

AB = BA = I ... (1)

Since C is also the inverse of A

$$\begin{array}{ccccc} \text{AC}=\text{CA}=\text{I} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@} & \text{@$$

**Theorem 4** If A and B are invertible matrices of the same order, then (AB)–1 = B–1 A–1 . **Proof** From the definition of inverse of a matrix, we have

|       | (AB)<br>(AB)–1 =<br>1     |                                     |
|-------|---------------------------|-------------------------------------|
| or    | A–1 (AB) (AB)–1 =<br>A–1I | (Pre multiplying both sides by A–1) |
| or    | (A–1A) B (AB)–1 =<br>A–1  | (Since A–1 I = A–1)                 |
| or    | IB (AB)–1 =<br>A–1        |                                     |
| or    | B (AB)–1 =<br>A–1         |                                     |
| or    | B–1 B (AB)–1 =<br>B–1 A–1 |                                     |
| or    | I (AB)–1 =<br>B–1 A–1     |                                     |
| Hence | (AB)–1 =<br>B–1<br>A–1    |                                     |
|       |                           |                                     |
|       |                           |                                     |

**EXERCISE 3.4**

**1.** Matrices A and B will be inverse of each other only if

$$(\mathbf{A})\,\mathbf{A}\mathbf{B} \equiv \mathbf{B}\mathbf{A} \,(\mathbf{B})\,\mathbf{A}\mathbf{B} \equiv \mathbf{B}\mathbf{A} \mathbf{=0}$$

$$\text{(C)}\,\text{AB} = 0, \text{BA} = \text{I} \text{ (D)}\,\text{AB} = \text{BA} = \text{I}$$

# *Miscellaneous Examples*

$$\text{Example 23 If } \mathbf{A} = \begin{bmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{bmatrix}, \text{ then prove that } \mathbf{A}'' = \begin{bmatrix} \cos n\theta & \sin n\theta \\ -\sin n\theta & \cos n\theta \end{bmatrix}, n \in \mathbb{N}.$$

**Solution** We shall prove the result by using principle of mathematical induction.

$$\begin{aligned} \text{We have } & \qquad \mathbf{P}(n): \text{If } \mathbf{A} = \begin{bmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{bmatrix}, \text{ then } \mathbf{A}'' = \begin{bmatrix} \cos n\theta & \sin n\theta \\ -\sin n\theta & \cos n\theta \end{bmatrix}, n \in \mathbb{N} \\\ & \qquad \mathbf{P}(1): \text{ A} = \begin{bmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{bmatrix}, \text{ so } \mathbf{A}^{\dagger} = \begin{bmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{bmatrix} \end{aligned}$$

Therefore, the result is true for *n* = 1. Let the result be true for *n* = *k*. So

$$\mathbf{P}(k) \text{ : A = } \begin{bmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{bmatrix}, \text{ then } \mathbf{A}^k = \begin{bmatrix} \cos k\theta & \sin k\theta \\ -\sin k\theta & \cos k\theta \end{bmatrix}$$

Now, we prove that the result holds for *n* = *k* +1

$$\begin{aligned} \mathbf{A}^{k+1} &= \mathbf{A} \cdot \mathbf{A}^{k} = \begin{bmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} \cos k\theta & \sin k\theta \\ -\sin k\theta & \cos k\theta \end{bmatrix} \\ &= \begin{bmatrix} \cos \theta \cos k\theta - \sin \theta \sin k\theta & \cos \theta \sin k\theta + \sin \theta \cos k\theta \\ -\sin \theta \cos k\theta + \cos \theta \sin k\theta & -\sin \theta \sin k\theta + \cos \theta \cos k\theta \end{bmatrix} \\ &= \begin{bmatrix} \cos(\theta + k\theta) & \sin(\theta + k\theta) \\ -\sin(\theta + k\theta) & \cos(\theta + k\theta) \end{bmatrix} = \begin{bmatrix} \cos(k+1)\theta & \sin(k+1)\theta \\ -\sin(k+1)\theta & \cos(k+1)\theta \end{bmatrix} \end{aligned}$$

Therefore, the result is true for *n* = *k* + 1. Thus by principle of mathematical induction,

we have cos sin A sin cos *n n n n n* θ θ = − θ θ , holds for all natural numbers.

**Example 24** If A and B are symmetric matrices of the same order, then show that AB is symmetric if and only if A and B commute, that is AB = BA.

**Solution** Since A and B are both symmetric matrices, therefore A′ = A and B′ = B.

Let AB be symmetric, then (AB)′ = AB

But (AB)′ = B′A′= BA (Why?)

Therefore BA = AB

Conversely, if AB = BA, then we shall show that AB is symmetric.

$$\text{Now}\qquad\qquad\qquad\qquad(\text{AB})' \equiv \text{B'A'}\qquad$$

= B A (as A and B are symmetric)

$$=\mathbf{A}\mathbf{B}$$

Hence AB is symmetric.

**Example 25** Let 2 1 5 2 2 5 A , B , C 3 4 7 4 3 8 − <sup>=</sup> = = . Find a matrix D such that

CD – AB = O.

**Solution** Since A, B, C are all square matrices of order 2, and CD – AB is well defined, D must be a square matrix of order 2.

$$\begin{array}{ll} \text{Let} & \mathbf{D} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}. \text{ Then,} & \mathbf{CD} - \mathbf{AB} = \mathbf{0} \text{ gives} \\\\ \begin{bmatrix} 2 & 5 \\ 3 & 8 \end{bmatrix} \begin{bmatrix} a & b \\ c & d \end{bmatrix} - \begin{bmatrix} 2 & -1 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 5 & 2 \\ 7 & 4 \end{bmatrix} = \mathbf{0} \\\\ \text{or} & \begin{bmatrix} 2a + 5c & 2b + 5d \\ 3a + 8c & 3b + 8d \end{bmatrix} \begin{bmatrix} 3 & 0 \\ 43 & 22 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} \\\\ \text{or} & \begin{bmatrix} 2a + 5c - 3 & 2b + 5d \\ 3a + 8c - 43 & 3b + 8d - 22 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} \end{array}$$

By equality of matrices, we get

$$2a + 5c - 3 = 0 \tag{l}$$

$$3a + 8c - 43 = 0 \tag{2}$$

$$\begin{aligned} \stackrel{\cdots}{2}b + \stackrel{\cdots}{5}d &= 0 \\ &\quad \stackrel{\cdots}{3}b \end{aligned} \tag{3}$$

$$\text{and} \qquad \qquad \Im b + 8d - 22 = 0 \tag{4}$$

Solving (1) and (2), we get *a* = –191, *c* = 77. Solving (3) and (4), we get *b* = – 110, *d* = 44.

Therefore D =

$$\mathbf{D} = \begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} -191 & -110 \\ 77 & 44 \end{bmatrix}$$

# *Miscellaneous Exercise on Chapter 3*

- **1.** If A and B are symmetric matrices, prove that AB BA is a skew symmetric matrix.
- **2.** Show that the matrix B′AB is symmetric or skew symmetric according as A is symmetric or skew symmetric.
- **3.** Find the values of *x*, *y*, *z* if the matrix 0 2 A *y z x y z x y z* = − − satisfy the equation

A′A = I.

**4.** For what values of *x* : [ ] 1 2 0 0 1 2 1 2 0 1 2 1 0 2 *x* = O?

$$\mathbf{S}. \quad \text{If } \mathbf{A} = \begin{bmatrix} 3 & 1 \\ -1 & 2 \end{bmatrix}, \text{ show that} \\ \mathbf{A}^2 - \mathbf{S}\mathbf{A} + \mathbf{7}\mathbf{I} = \mathbf{0}.$$

- **6.** Find *x*, if [ ] 1 0 2 5 1 0 2 1 4 O 2 0 3 1 *x x* − − =
- **7.** A manufacturer produces three products *x*, *y*, *z* which he sells in two markets. Annual sales are indicated below:

| Market | Products |        |        |
|--------|----------|--------|--------|
| I      | 10,000   | 2,000  | 18,000 |
| II     | 6,000    | 20,000 | 8,000  |

- (a) If unit sale prices of *x*, *y* and *z* are ` 2.50, ` 1.50 and ` 1.00, respectively, find the total revenue in each market with the help of matrix algebra.
- (b) If the unit costs of the above three commodities are ` 2.00, ` 1.00 and 50 paise respectively. Find the gross profit.

$$\textbf{8.} \quad \text{Find the matrix } \textbf{X} \text{ so that } \textbf{X} \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix} = \begin{bmatrix} -7 & -8 & -9 \\ 2 & 4 & 6 \end{bmatrix}.$$

Choose the correct answer in the following questions:

$$\begin{aligned} \text{9.} \quad \text{If } \mathbf{A} = \begin{bmatrix} \alpha & \beta \\ \gamma & -\alpha \end{bmatrix} \text{ is such that } \mathbf{A}^2 &= \mathbf{I}, \text{ then} \\ \text{(A)} \quad \mathbf{1} + \alpha^2 + \beta\gamma &= 0 & \text{(B)} & \mathbf{1} - \alpha^2 + \beta\gamma &= 0 \\ \text{(C)} \quad \mathbf{1} - \alpha^2 - \beta\gamma &= 0 & \text{(D)} & \mathbf{1} + \alpha^2 - \beta\gamma &= 0 \\ \text{10.} \quad \text{If the matrix } \mathbf{A} \text{ is both symmetric and skew symmetric, then} \\ (\mathbf{A}) &\text{ A linear-dimensional matrix} \end{aligned}$$

- (A) A is a diagonal matrix (B) A is a zero matrix
	- (C) A is a square matrix (D) None of these

**11.** If A is square matrix such that A<sup>2</sup> = A, then (I + A)³ – 7 A is equal to

(A) A (B) I – A (C) I (D) 3A

### *Summary*

- Æ A matrix is an ordered rectangular array of numbers or functions.
- Æ A matrix having *m* rows and *n* columns is called a matrix of order *m* × *n*.
- Æ [*aij*] *<sup>m</sup>* × 1 is a column matrix.
- Æ [*aij*] 1 × *n* is a row matrix.
- Æ An *m* × *n* matrix is a square matrix if *m* = *n*.
- Æ A = [*aij*] *m* × *m* is a diagonal matrix if *aij* = 0, when *i* ≠ *j*.
- Æ A = [*aij*] *n* × *n* is a scalar matrix if *aij* = 0, when *i* ≠ *j*, *aij* = *k*, (*k* is some constant), when *i* = *j*.
- Æ A = [*aij*] *n* × *n* is an identity matrix, if *aij* = 1, when *i* = *j*, *aij* = 0, when *i* ≠ *j*.
- Æ A zero matrix has all its elements as zero.
- Æ A = [*aij*] = [*bij*] = B if (i) A and B are of same order, (ii) *aij* = *bij* for all possible values of *i* and *j*.

$$\bullet \quad k\mathbf{A} = k[a\_{ij}]\_{m \times n} = [k(a\_{ij})]\_{m \times n}$$

$$\mathbf{A} \cdot \mathbf{-A} = (-1)\mathbf{A}$$

$$\mathbf{O} \quad \mathbf{A} - \mathbf{B} = \mathbf{A} + (-1)^{\circ} \mathbf{B}$$

$$\mathbf{O} \quad \mathbf{A} + \mathbf{B} = \mathbf{B} + \mathbf{A}$$

- Æ (A + B) + C = A + (B + C), where A, B and C are of same order.
- Æ *<sup>k</sup>*(A + B) = *k*A + *k*B, where A and B are of same order, *k* is constant.
- Æ (*k* + *l*) A = *k*A + *l*A, where *k* and *l* are constant.
- Æ If A = [*aij*] *m* × *n* and B = [*bjk*] *n* × *p* , then AB = C = [*cik*] *m* × *p* , where = =1 *ik ij jk j c a b* ∑

*n*

- Æ (i) A(BC) = (AB)C, (ii) A(B + C) = AB + AC, (iii) (A + B)C = AC + BC
- Æ If A = [*aij*] *m* × *n* , then A′ or A<sup>T</sup> = [*aji*] *n* × *m*
- Æ (i) (A′)′ = A, (ii) (*k*A)′ = *k*A′, (iii) (A + B)′ = A′ + B′, (iv) (AB)′ = B′A′
- Æ A is a symmetric matrix if A′ = A.
- Æ A is a skew symmetric matrix if A′ = –A.
- Æ Any square matrix can be represented as the sum of a symmetric and a skew symmetric matrix.
- Æ If A and B are two square matrices such that AB = BA = I, then B is the inverse matrix of A and is denoted by A–1 and A is the inverse of B.

**—**v**—**

Æ Inverse of a square matrix, if it exists, is unique.

![](_page_41_Figure_0.jpeg)

MATRICES 75