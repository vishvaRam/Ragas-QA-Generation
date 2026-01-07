![](_page_0_Picture_0.jpeg)

# **THREE DIMENSIONAL GEOMETRY**

## v *The moving power of mathematical invention is not reasoning but imagination. – A.DEMORGAN* v

## **11.1 Introduction**

In Class XI, while studying Analytical Geometry in two dimensions, and the introduction to three dimensional geometry, we confined to the Cartesian methods only. In the previous chapter of this book, we have studied some basic concepts of vectors. We will now use vector algebra to three dimensional geometry. The purpose of this approach to 3-dimensional geometry is that it makes the study simple and elegant\*.

In this chapter, we shall study the direction cosines and direction ratios of a line joining two points and also discuss about the equations of lines and planes in space under different conditions, angle between two lines, two planes, a line and a plane, shortest distance between two skew lines and distance of a point from a plane. Most of

![](_page_0_Picture_6.jpeg)

**Leonhard Euler (1707-1783)**

the above results are obtained in vector form. Nevertheless, we shall also translate these results in the Cartesian form which, at times, presents a more clear geometric and analytic picture of the situation.

## **11.2 Direction Cosines and Direction Ratios of a Line**

From Chapter 10, recall that if a directed line L passing through the origin makes angles α, β and γ with *x*, *y* and *z*-axes, respectively, called direction angles, then cosine of these angles, namely, cos α, cos β and cos γ are called direction cosines of the directed line L.

If we reverse the direction of L, then the direction angles are replaced by their supplements, i.e., , and . Thus, the signs of the direction cosines are reversed.

<sup>\*</sup> For various activities in three dimensional geometry, one may refer to the Book *"A Hand Book for designing Mathematics Laboratory in Schools",* NCERT, 2005

![](_page_1_Figure_1.jpeg)

Note that a given line in space can be extended in two opposite directions and so it has two sets of direction cosines. In order to have a unique set of direction cosines for a given line in space, we must take the given line as a directed line. These unique direction cosines are denoted by *l*, *m* and *n*.

*Remark* If the given line in space does not pass through the origin, then, in order to find its direction cosines, we draw a line through the origin and parallel to the given line. Now take one of the directed lines from the origin and find its direction cosines as two parallel line have same set of direction cosines.

Any three numbers which are proportional to the direction cosines of a line are called the *direction ratios* of the line. If *l*, *m*, *n* are direction cosines and *a*, *b*, *c* are direction ratios of a line, then *a* = λ*l*, *b*=λ*m* and *c* = λ*n*, for any nonzero λ ∈ **R**.

A**Note** Some authors also call direction ratios as direction numbers.

Let *a*, *b*, *c* be direction ratios of a line and let *l*, *m* and *n* be the direction cosines (*d*.*c*'s) of the line. Then

$$\begin{array}{cccc} \multicolumn{2}{c}{\begin{array}{c} l} & & & \frac{l}{a} = \frac{m}{b} = \frac{n}{c} = k \text{ (say)}, \, k \text{ being a constant.}\\ \text{Therefore} & & & l = ak, \, m = bk, \, n = ck & & & \dots \text{(1)}\\ \text{But} & & & l^2 + m^2 + n^2 = 1\\ \text{Therefore} & & & k^2 \, (a^2 + b^2 + c^2) = 1\\ \end{array} \\ \text{or} \\ \begin{array}{c} \text{(1)}\\k = \frac{\pm}{\sqrt{a^2 + b^2 + c^2}} \end{array}$$

Hence, from (1), the *d*.*c*.'*s* of the line are

$$d = \pm \frac{a}{\sqrt{a^2 + b^2 + c^2}}, m = \pm \frac{b}{\sqrt{a^2 + b^2 + c^2}}, n = \pm \frac{c}{\sqrt{a^2 + b^2 + c^2}}$$

where, depending on the desired sign of *k*, either a positive or a negative sign is to be taken for *l*, *m* and *n*.

For any line, if *a*, *b*, *c* are direction ratios of a line, then *ka*, *kb*, *kc*; *k* ≠ 0 is also a set of direction ratios. So, any two sets of direction ratios of a line are also proportional. Also, for any line there are infinitely many sets of direction ratios.

#### **11.2.1** *Direction cosines of a line passing through two points*

Since one and only one line passes through two given points, we can determine the direction cosines of a line passing through the given points P(*x*<sup>1</sup> , *y*1 , *z* 1 ) and Q(*x*<sup>2</sup> , *y*2 , *z* 2 ) as follows (Fig 11.2 (a)).

![](_page_2_Figure_7.jpeg)

**Fig 11.2**

Let *l*, *m*, *n* be the direction cosines of the line PQ and let it makes angles α, β and γ with the *x*, *y* and *z*-axis, respectively.

Draw perpendiculars from P and Q to XY-plane to meet at R and S. Draw a perpendicular from P to QS to meet at N. Now, in right angle triangle PNQ, ∠PQN= γ (Fig 11.2 (b).

$$\text{Therefore, } \stackrel{\sim}{\longrightarrow} \quad \stackrel{\sim}{\longrightarrow} \quad \cos \chi = \frac{\text{NQ}}{\text{PQ}} = \frac{z\_2 - z\_1}{\text{PQ}}$$

Similarly cosα = 2 1 2 1 and cos PQ PQ *x x* − *y y* − β=

Hence, the direction cosines of the line segment joining the points P(*x* 1 , *y*1 , *z*1 ) and Q(*x* 2 , *y*<sup>2</sup> , *z*<sup>2</sup> ) are

$$\frac{x\_2 - x\_1}{\text{PQ}}, \frac{y\_2 - y\_1}{\text{PQ}}, \frac{z\_2 - z\_1}{\text{PQ}}$$

2 1 2 1 2 1 ( ) ( ) *x x y y z z* − + − + −

where PQ = ( ) <sup>2</sup> <sup>2</sup> <sup>2</sup>

A**Note** The direction ratios of the line segment joining P(*x*<sup>1</sup> , *y*1 , *z* 1 ) and Q(*x*<sup>2</sup> , *y*2 , *z* 2 ) may be taken as

$$\left(\mathbf{x}\_{2} - \mathbf{x}\_{1}, \,\mathbf{y}\_{2} - \mathbf{y}\_{1}, \,\mathbf{z}\_{2} - \mathbf{z}\_{1} \text{ or } \mathbf{x}\_{1} - \mathbf{x}\_{2}, \,\mathbf{y}\_{1} - \mathbf{y}\_{2}, \,\mathbf{z}\_{1} - \mathbf{z}\_{2}\right)$$

**Example 1** If a line makes angle 90°, 60° and 30° with the positive direction of *x*, *y* and *z*-axis respectively, find its direction cosines.

**Solution** Let the *d* . *c* .'*s* of the lines be *l* , *m*, *n*. Then *l* = cos 90<sup>0</sup> = 0, *m* = cos 60<sup>0</sup> = 1 2 ,

$$n = \cos \ 30^{\circ} = \frac{\sqrt{3}}{2} \dots$$

**Example 2** If a line has direction ratios 2, – 1, – 2, determine its direction cosines.

**Solution** Direction cosines are

$$\frac{2}{\sqrt{2^2+(-1)^2+(-2)^2}}, \frac{-1}{\sqrt{2^2+(-1)^2+(-2)^2}}, \frac{-2}{\sqrt{2^2+(-1)^2+(-2)^2}}$$

or

**Example 3** Find the direction cosines of the line passing through the two points (– 2, 4, – 5) and (1, 2, 3).

**Solution** We know the direction cosines of the line passing through two points P(*x* 1 , *y* 1 , *z* 1 ) and Q(*x* 2 , *y* 2 , *z* 2 ) are given by

$$\begin{array}{cccc} & & \ddots & & \ddots & & \ddots\\ & & & & \mathbf{PQ} & & \mathbf{PQ} & \mathbf{QQ} \end{array}$$
  $\text{where} \qquad \begin{array}{cccc} & & \mathbf{x\_2 - x\_1} & \mathbf{y\_2 - y\_1} & \mathbf{z\_2 - z\_1} \\ & & \mathbf{PQ} & & \mathbf{PQ} \end{array}$  
$$\text{PQ} = \sqrt{\left(\mathbf{x\_2 - x\_1}\right)^2 + \left(\mathbf{y\_2 - y\_1}\right)^2 + \left(z\_2 - z\_1\right)^2}$$

Here P is (– 2, 4, – 5) and Q is (1, 2, 3).

So PQ = <sup>2</sup> <sup>2</sup> <sup>2</sup> (1 ( 2)) (2 4) (3 ( 5)) − − + − + − − = 77

Thus, the direction cosines of the line joining two points is

$$\frac{3}{\sqrt{77}}, \frac{-2}{\sqrt{77}}, \frac{8}{\sqrt{77}}$$

**Example 4** Find the direction cosines of *x*, *y* and *z*-axis.

**Solution** The *x*-axis makes angles 0°, 90° and 90° respectively with *x*, *y* and *z*-axis. Therefore, the direction cosines of *x*-axis are cos 0°, cos 90°, cos 90° i.e., 1,0,0. Similarly, direction cosines of *y*-axis and *z*-axis are 0, 1, 0 and 0, 0, 1 respectively.

**Example 5** Show that the points A (2, 3, – 4), B (1, – 2, 3) and C (3, 8, – 11) are collinear.

**Solution** Direction ratios of line joining A and B are

1 – 2, – 2 – 3, 3 + 4 i.e., – 1, – 5, 7.

The direction ratios of line joining B and C are

3 –1, 8 + 2, – 11 – 3, i.e., 2, 10, – 14.

It is clear that direction ratios of AB and BC are proportional, hence, AB is parallel to BC. But point B is common to both AB and BC. Therefore, A, B, C are collinear points.

## **EXERCISE 11.1**

- **1.** If a line makes angles 90°, 135°, 45° with the *x*, *y* and *z*-axes respectively, find its direction cosines.
- **2.** Find the direction cosines of a line which makes equal angles with the coordinate axes.
- **3.** If a line has the direction ratios –18, 12, 4, then what are its direction cosines ?
- **4.** Show that the points (2, 3, 4), (– 1, 2, 1), (5, 8, 7) are collinear.
- **5.** Find the direction cosines of the sides of the triangle whose vertices are (3, 5, – 4), (– 1, 1, 2) and (– 5, – 5, – 2).

## **11.3 Equation of a Line in Space**

We have studied equation of lines in two dimensions in Class XI, we shall now study the vector and cartesian equations of a line in space.

A line is uniquely determined if

- (i) it passes through a given point and has given direction, or
- (ii) it passes through two given points.

**11.3.1** *Equation of a line through a given point and parallel to given vector*  Let be the position vector of the given point A with respect to the origin O of the rectangular coordinate system. Let *l* be the line which passes through the point A and is parallel to a given vector . Let be the position vector of an arbitrary point P on the line (Fig 11.3).

Then AP uuur is parallel to the vector , i.e., AP uuur = λ , where λ is some real number. uuur uuur uuur

$$\begin{aligned} \text{But} \\ \text{i.e.} \end{aligned} \qquad \begin{aligned} \text{AP} &= \text{ OP} - \text{OA} \\ \text{i.e.} \end{aligned}$$

Conversely, for each value of the parameter λ, this equation gives the position vector of a point P on the line. Hence, the vector equation of the line is given by r r

![](_page_5_Figure_6.jpeg)

*Remark* If ˆ ˆ ˆ = + + r *b ai bj ck* , then *a*, *b*, *c* are direction ratios of the line and conversely, if *a*, *b*, *c* are direction ratios of a line, then ˆ ˆ ˆ = + + r *b ai bj ck* will be the parallel to the line. Here, *b* should not be confused with | |.

= **»**

### **Derivation of cartesian form from vector form**

Let the coordinates of the given point A be (*x*<sup>1</sup> , *y*<sup>1</sup> , *z* 1 ) and the direction ratios of the line be *a*, *b*, *c*. Consider the coordinates of any point P be (*x*, *y*, *z*). Then

$$\overrightarrow{\mathbf{r}} = \mathbf{x}\hat{\mathbf{i}} + \mathbf{y}\hat{\mathbf{j}} + \mathbf{z}\hat{\mathbf{k}},\\\overrightarrow{\mathbf{a}} = \mathbf{x}\_1\hat{\mathbf{i}} + \mathbf{y}\_1\hat{\mathbf{j}} + \mathbf{z}\_1\hat{\mathbf{k}}$$

$$\text{and}\\
\qquad\qquad\vec{b} = a\hat{i} + b\hat{j} + c\hat{k} \qquad\triangle\triangle\triangle\triangle\dots\qquad\qquad\dots$$

Substituting these values in (1) and equating the coefficients of ˆ ˆ *i j* , and *k* ˆ , we get

$$\mathbf{x} = \mathbf{x}\_1 + \lambda\_1 a; \mathbf{y} = \mathbf{y}\_1 + \lambda\_1 b; \ z = z\_1 + \lambda\_1 c \tag{2}$$

These are parametric equations of the line. Eliminating the parameter λ from (2), we get

$$\frac{\frac{1}{c}\frac{\mathbf{z}-(x\_1)}{c}}{a^\circ} = \frac{\mathbf{y}-\mathbf{y}\_1}{b} = \frac{\mathbf{z}-\mathbf{z}\_1}{c} \tag{3}$$

This is the Cartesian equation of the line.

$$\boxed{\text{Note}}\underbrace{\text{If }l,m,n}\_{\text{all}}\text{ are the direction cosines of the line, the equation of the line is}$$

$$\frac{\begin{array}{c} \mathbf{x} - \mathbf{x}\_{1} \\ \mathbf{l} \end{array}}{\mathbf{l}} = \frac{\mathbf{y} - \mathbf{y}\_{1}}{m} = \frac{\mathbf{z} - \mathbf{z}\_{1}}{n}$$

**Example 6** Find the vector and the Cartesian equations of the line through the point (5, 2, – 4) and which is parallel to the vector ˆ ˆ ˆ 3 2 8 *i j k* + − . **Solution** We have

 = ˆ ˆ ˆ ˆ ˆ ˆ 5 2 4 and 3 2 8 + − = + − r *i j k b i j k*

Therefore, the vector equation of the line is

$$\vec{r} = \mathbf{5}\hat{i} + \mathbf{2}\hat{j} - 4\hat{k} + \lambda\left(\mathbf{3}\hat{i} + \mathbf{2}\hat{j} - 8\hat{k}\right)$$

Now, is the position vector of any point P(*x*, *y*, *z*) on the line.

Therefore, ˆ ˆ ˆ *xi y j z k* + + = ˆ ˆ ˆ ˆ ˆ ˆ 5 2 4 ( 3 2 8 ) *i j k i j k* + − + λ + − = ˆ ˆ ˆ (5 3 ) (2 2 ) ( 4 8 ) + λ + + λ + − − λ *i j k*

Eliminating λ , we get

$$\frac{x-5}{3} = \frac{y-2}{2} = \frac{z+4}{-8}$$

which is the equation of the line in Cartesian form.

## **11.4 Angle between Two Lines**

Let L<sup>1</sup> and L<sup>2</sup> be two lines passing through the origin and with direction ratios *a*<sup>1</sup> , *b*<sup>1</sup> , *c*<sup>1</sup> and *a*<sup>2</sup> , *b*<sup>2</sup> , *c*<sup>2</sup> , respectively. Let P be a point on L<sup>1</sup> and Q be a point on L<sup>2</sup> . Consider the directed lines OP and OQ as given in Fig 11.6. Let θ be the acute angle between OP and OQ. Now recall that the directed line segments OP and OQ are vectors with components *a*1 , *b*<sup>1</sup> , *c*<sup>1</sup> and *a*<sup>2</sup> , *b*<sup>2</sup> , *c*<sup>2</sup> , respectively. Therefore, the angle θ between them is given by

$$\cos \theta = \left| \frac{(a\_1 a\_2) + b\_1 b\_2 + c\_1 c\_2}{\sqrt{a\_1^2 + b\_1^2 + c\_1^2} \sqrt{a\_2^2 + b\_2^2 + c\_2^2}} \right|$$

The angle between the lines in terms of sin θ is given by

$$\begin{aligned} \sin\Theta &= \sqrt{1 - \cos^2\Theta} \\ &= \sqrt{1 - \frac{\left(a\_1a\_2 + b\_1b\_2 + c\_1c\_2\right)^2}{\left(a\_1^2 + b\_1^2 + c\_1^2\right)\left(a\_2^2 + b\_2^2 + c\_2^2\right)}} \\ &= \frac{\sqrt{\left(a\_1^2 + b\_1^2 + c\_1^2\right)\left(a\_2^2 + b\_2^2 + c\_2^2\right) - \left(a\_1a\_2 + b\_1b\_2 + c\_1c\_2\right)^2}}{\sqrt{\left(a\_1^2 + b\_1^2 + c\_1^2\right)\sqrt{\left(a\_2^2 + b\_2^2 + c\_2^2\right)}}} \\ &= \frac{\sqrt{\left(a\_1\ b\_2 - a\_2\ b\_1\right)^2 + \left(b\_1\ c\_2 - b\_2\ c\_1\right)^2 + \left(c\_1\ a\_2 - c\_2\ a\_1\right)^2}}{\sqrt{\left(a\_1^2 + b\_1^2 + c\_1^2\right)\sqrt{a\_2^2 + b\_2^2 + c\_2^2}}} \quad \dots \text{ (2)} \end{aligned}} \quad \dots \text{ (2)}$$

![](_page_6_Figure_14.jpeg)

... (1)

A**Note** In case the lines L1 and L<sup>2</sup> do not pass through the origin, we may take lines L and L 1 2 ′ ′ which are parallel to L<sup>1</sup> and L<sup>2</sup> respectively and pass through the origin.

If instead of direction ratios for the lines L<sup>1</sup> and L<sup>2</sup> , direction cosines, namely, *l* 1 , *m*<sup>1</sup> , *n*1 for L<sup>1</sup> and *l* 2 , *m*<sup>2</sup> , *n*2 for L<sup>2</sup> are given, then (1) and (2) takes the following form:

$$\cos \Theta = \mathop{\!|l\_{\mathbf{i}\_1} l\_{\mathbf{i}\_2} + m\_{\mathbf{i}\_1} m\_{\mathbf{i}\_2} + n\_{\mathbf{i}\_1} n\_{\mathbf{i}\_2}|} \quad \text{ (as } \overset{\!|l\_{\mathbf{i}\_1} + m\_{\mathbf{i}\_1}^2 + n\_{\mathbf{i}\_1}^2 = \overset{\!\cdot|l\_{\mathbf{i}\_2} + m\_{\mathbf{i}\_2}^2 + n\_{\mathbf{i}\_2}^2}{2}) \qquad \dots \text{ (\heartsuit)}$$

$$\text{and} \qquad \sin \Theta = \sqrt{\left(l\_1 m\_2 - l\_2 \, m\_1\right)^2 - \left(m\_1 n\_2 - m\_2 \, n\_1\right)^2 + \left(n\_1 l\_2 - n\_2 \, l\_1\right)^2} \tag{4} \qquad \dots \text{(4)}$$

Two lines with direction ratios *a*<sup>1</sup> , *b*<sup>1</sup> , *c*<sup>1</sup> and *a*<sup>2</sup> , *b*<sup>2</sup> , *c*<sup>2</sup> are

(i) perpendicular i.e. if θ = 90° by (1)

$$a\_1 a\_2 + b\_1 b\_2 + c\_1 c\_2 = 0$$

(ii) parallel i.e. if θ = 0 by (2)

$$\frac{a\_1}{a\_2} = \frac{b\_1}{b\_2} = \frac{c\_1}{c\_2}$$

Now, we find the angle between two lines when their equations are given. If θ is acute the angle between the lines 

1 2

$$
\vec{r} = \vec{a}\_1 + \lambda\_1 \vec{b}\_1 \text{ and } \vec{r} = \vec{a}\_2 + \mu \vec{b}\_2
$$

$$
\text{then}
\qquad
\begin{aligned}
\vec{r} &= \vec{a}\_1 + \lambda\_1 \vec{b}\_1 \text{ and } \vec{r} = \vec{a}\_2 + \mu \vec{b}\_2 \\
\vec{b}\_1 \cdot \vec{b}\_2 \\
\overline{b}\_1 \left| \vec{b}\_2 \right|
\end{aligned}
$$

In Cartesian form, if θ is the angle between the lines

$$\sum\_{1}^{\infty} \frac{x - x\_1^{\varepsilon}}{a\_1} = \frac{y - y\_1}{b\_1} = \frac{z - z\_1}{c\_1} \tag{1}$$

= ... (2)

and <sup>2</sup>

where, *a*<sup>1</sup> , *b*1, *c*1 and *a*2, *b*<sup>2</sup> , *c*2 are the direction ratios of the lines (1) and (2), respectively, then

$$\cos \Theta = \left| \frac{a\_1 a\_2 + b\_1 b\_2 + c\_1 c\_2}{\sqrt{a\_1^2 + b\_1^2 + c\_1^2} \sqrt{a\_2^2 + b\_2^2 + c\_2^2}} \right|$$

2 2 2 2

*y y z z b c* − −

**Example 7** Find the angle between the pair of lines given by

2

=

*x x a* −

$$\vec{r} = \left(\hat{\mathfrak{z}}\hat{\mathfrak{i}} + \hat{\mathfrak{z}}\hat{\mathfrak{j}} - 4\hat{\mathfrak{k}} + \hat{\mathfrak{k}}(\hat{\mathfrak{i}} + \hat{\mathfrak{z}}\hat{\mathfrak{j}} + \hat{\mathfrak{z}}\hat{\mathfrak{k}})\right)$$

$$\text{and} \qquad \vec{r} = \mathfrak{H}\hat{i} - 2\hat{j} + \mathfrak{\mu}(3\hat{i} + 2\hat{j} + 6\hat{k})$$

**Solution** Here <sup>1</sup> r *b* = ˆ ˆ ˆ *i j k* + + 2 2 and <sup>2</sup> r *b* = ˆ ˆ ˆ 3 2 6 *i j k* + + The angle θ between the two lines is given by

$$\begin{aligned} \cos \Theta &= \left| \frac{\vec{b}\_1 \cdot \vec{b}\_2}{\|\vec{b}\_1\| \|\vec{b}\_2\|} \right| = \left| \frac{(\hat{i} + 2\hat{j} + 2\hat{k}) \cdot (3\hat{i} + 2\hat{j} + 6\hat{k})}{\sqrt{1 + 4 + 4} \sqrt{9 + 4 + 36}} \right| \\ &= \left| \frac{3 + 4 + 12}{3 \times 7} \right| = \frac{19}{21} \end{aligned}$$
 
$$\begin{aligned} \text{Hence} \qquad \Theta &= \cos^{-1} \left( \frac{19}{21} \right) \end{aligned}$$

**Example 8** Find the angle between the pair of lines

$$\frac{\frac{x+3}{3}}{\frac{x+1}{1}} = \frac{y-1}{5} = \frac{z+3}{4}$$

$$\frac{x+1}{1} = \frac{y-4}{1} = \frac{z-5}{2}$$

and

**Solution** The direction ratios of the first line are 3, 5, 4 and the direction ratios of the second line are 1, 1, 2. If θ is the angle between them, then

$$\cos \theta = \left| \frac{3.1 + 5.1 + 4.2}{\sqrt{3^2 + 5^2 + 4^2}} \sqrt{1^2 + 1^2 + 2^2} \right| = \frac{16}{\sqrt{50}\sqrt{6}} = \frac{16}{5\sqrt{2}\sqrt{6}} = \frac{8\sqrt{3}}{15}.$$
  $\text{Hence, the required angle is } \cos^{-1} \left( \frac{8\sqrt{3}}{15} \right).$ 

## **11.5 Shortest Distance between Two Lines**

If two lines in space intersect at a point, then the shortest distance between them is zero. Also, if two lines in space are parallel, then the shortest distance between them will be the perpendicular distance, i.e. the length of the perpendicular drawn from a point on one line onto the other line.

Further, in a space, there are lines which are neither intersecting nor parallel. In fact, such pair of lines are *non coplanar* and are called *skew lines*. For example, let us consider a room of size 1, 3, 2 units along *x*, *y* and *z*-axes respectively Fig 11.5.

![](_page_8_Figure_14.jpeg)

**Fig 11.5**

#### 386 MATHEMATICS

The line GE that goes diagonally across the ceiling and the line DB passes through one corner of the ceiling directly above A and goes diagonally down the wall. These lines are skew because they are not parallel and also never meet.

By the shortest distance between two lines we mean the join of a point in one line with one point on the other line so that the length of the segment so obtained is the smallest.

For skew lines, the line of the shortest distance will be perpendicular to both the lines.

### **11.5.1** *Distance between two skew lines*

We now determine the shortest distance between two skew lines in the following way: Let *l* <sup>1</sup>and *l* <sup>2</sup>be two skew lines with equations (Fig. 11.6)

$$
\vec{r} = \vec{a}\_1 + \lambda\_1 \vec{b}\_1 \tag{1}
$$

and 
$$
\vec{r} = \vec{a}\_2 + \mu\_1 \vec{b}\_2
$$

**T** Take any point S on *l* 1 with position vector 1 a r and T on *l* 2 , with position vector <sup>2</sup> a r . Then the magnitude of the shortest distance vector

will be equal to that of the projection of ST along the direction of the line of shortest distance (See 10.6.2). uuur

If PQ is the shortest distance vector between *l* 1 and *l* <sup>2</sup>, then it being perpendicular to both <sup>1</sup> r *b* and <sup>2</sup> r *b* , the unit vector *n*ˆ along PQ uuur would therefore be

![](_page_9_Figure_11.jpeg)

$$
\vec{\hat{a}} = \frac{\vec{b}\_1 \times \vec{b}\_2}{|\vec{b}\_1 \times \vec{b}\_2|} \tag{3}
$$

Then PQ

$$
\overline{\mathbb{P}Q} = d \quad \hat{n}
$$

where, *d* is the magnitude of the shortest distance vector. Let θ be the angle between ST uur and PQ uuur . Then

$$\mathbf{But}$$

$$\begin{aligned} \text{But} \\ \begin{aligned} \text{But} \\ \text{But} \end{aligned} \qquad \cos\theta = \left| \frac{\overrightarrow{\text{PQ}} \cdot \overrightarrow{\text{ST}}}{|\overrightarrow{\text{PQ}}\,|\,|\,|\overrightarrow{\text{ST}}\,|} \right| \\ &= \left| \frac{d \,\hat{n} \cdot (\vec{\tilde{a}}\_2 - \vec{a}\_1)}{d \,\text{ST}} \right| \\ &= \left| \frac{(\vec{b}\_1 \times \vec{b}\_2) \cdot (\vec{a}\_2 - \vec{a}\_1)}{\text{ST} \left| \vec{b}\_1 \times \vec{b}\_2 \right|} \right| \end{aligned} \qquad \text{(since } \overrightarrow{\text{ST}} = \vec{a}\_2 - \vec{a}\_1)$$

Hence, the required shortest distance is

$$d = \text{PQ} = \text{ST l} \cos \theta \,\text{l}$$
 or 
$$d = \left| \frac{(\vec{b}\_1 \times \vec{b}\_2) \dots (\vec{a}\_2 \times \vec{a}\_1)}{|\vec{b}\_1 \times \vec{b}\_2|} \right| $$
 Cuntzion  $\mathbf{r} = \mathbf{r} \times \mathbf{r}$ .

= <sup>1</sup> −

*z z*

1

### **Cartesian form**

The shortest distance between the lines

*l* 1 : *x x*

− <sup>1</sup>

*a* 1 *b c* 1 1 and *l* 2 : *x x a* − <sup>2</sup> 2 = *y y b z z c* − = <sup>2</sup> − 2 2 2

=

#### *x x y y z z a b c a b c b c b c c a c a a b* **2 1 2 1 2 1 1 1 1 2 2 2 1 2 2 1 2 1 2 2 1 2 1 2 − − − ( − + − + ) ( ) ( −** *a b***2 1 2 )**

*y y*

−

is

## **11.5.2** *Distance between parallel lines*

If two lines *l* 1 and *l* <sup>2</sup>are parallel, then they are coplanar. Let the lines be given by

$$\begin{pmatrix} \vec{r} \ \vec{=} \vec{a}\_1 + \lambda \vec{b}\_2 \\ \vdots \\ \end{pmatrix} \tag{1}$$

and … (2)

where, 1 a r is the position vector of a point S on *l* <sup>1</sup>and <sup>2</sup> a r is the position vector of a point T on *l* 2 Fig 11.7.

As *l* 1 , *l* <sup>2</sup>are coplanar, if the foot of the perpendicular from T on the line *l* 1 is P, then the distance between the lines *l* <sup>1</sup>and *l* <sup>2</sup>= |TP|.

Let θ be the angle between the vectors ST uur and . Then

× = ST r uur *b* ˆ ... (3)

where *n*ˆ is the unit vector perpendicular to the plane of the lines *l* <sup>1</sup>and *l* 2.

$$\begin{array}{cc} \text{But} \\ \text{But} \\ \end{array} \qquad \qquad \qquad \qquad \begin{array}{cc} \blacksquare & \blacksquare & \blacksquare \\ \end{array} \begin{array}{c} \blacksquare & \blacksquare & \blacksquare \\ \end{array}$$

![](_page_10_Figure_20.jpeg)

#### 388 MATHEMATICS

Therefore, from (3), we get

$$
\vec{b} \times (\vec{a}\_2 - \vec{a}\_1) = \vec{b} \mid \text{PT } \hat{n} \qquad \text{(since } \text{PT} = \text{ST} \sin \theta)
$$

$$
|\vec{b} \times (\vec{a}\_2 - \vec{a}\_1)| = |\vec{b} \mid \text{PT} \cdot 1 \qquad \text{(as } \|\hat{n}\| = 1)
$$

Hence, the distance between the given parallel lines is

$$d = |\overline{\mathcal{PT}}| = \left| \frac{\vec{b} \times (\vec{a}\_2 - \vec{a}\_1)}{|\vec{b}|} \right| $$

**Example 9** Find the shortest distance between the lines *l* 1 and *l* <sup>2</sup>whose vector equations are

$$\vec{r} = \begin{pmatrix} \hat{\imath} + \hat{\jmath} + \hat{\varkappa} & (2\hat{\imath} - \hat{\jmath} + \hat{k}) \end{pmatrix}\_{\diamondsuit \diamondsuit \diamondsuit} \begin{pmatrix} \bigvee & \cdots & (1) \\ \bigvee & \cdots & (2) \end{pmatrix}$$

and = ˆ ˆ ˆ ˆ ˆ ˆ 2 *i j k i j k* + − + µ − + (3 5 2 ) ... (2)

**Solution** Comparing (1) and (2) with = 1 1 + λ r r *a b* and 2 2 r a b = + <sup>µ</sup> <sup>r</sup> r r respectively, r r

$$\begin{aligned} \text{we get} \\ \begin{aligned} \text{We get} \\ \end{aligned} \qquad \begin{aligned} \ddot{\vec{a}}\_1 &= \hat{i}\hat{i} + \hat{j}, \ \vec{b}\_1 = 2\hat{i}\hat{i} - 3\hat{j} + \hat{k} \\ \end{aligned} \\ \text{Therefore} \\ \begin{aligned} \text{Therefore} \\ \ddot{\vec{a}}\_2 &= \hat{i}\hat{i} + \hat{k} \\ \end{aligned} \qquad \begin{aligned} \ddot{\vec{a}}\_1 &= 2\hat{i} + \hat{j} - \hat{k} \\ \end{aligned} \text{and} \\ \begin{aligned} \ddot{\vec{a}}\_2 &= \hat{i}\hat{i} + \hat{k} \\ \end{aligned} \\ \begin{aligned} \ddot{\vec{a}}\_1 &= (2\hat{i} - \hat{j} + \hat{k}) \times (3\hat{i} - 5\hat{j} + 2\hat{k}) \\ \end{aligned} \\ \begin{aligned} \ddot{\vec{a}}\_2 &= \hat{i} + \hat{j} - \hat{k} \\ \end{aligned} \end{aligned} \qquad \begin{aligned} \ddot{\vec{a}}\_1 &= 2\hat{i} + \hat{j} - \hat{k} \\ \end{aligned} \\ \begin{aligned} \ddot{\vec{a}}\_2 &= \hat{i} + \hat{j} - 2\hat{k} \\ \end{aligned} \\ \begin{aligned} \ddot{\vec{a}}\_1 &= 2\hat{i} - \hat{j} - 7\hat{k} \\ \end{aligned} \end{aligned}$$

$$\text{So}\\
\bullet \qquad \bigvee\_{\bigvee \dots \bigvee \dots \bigvee} \quad \bigvee\_{\bigvee \dots \bigvee \dots \bigvee} \\
\bullet \qquad \bigvee\_{1 \dots 1} \times \bar{b}\_2 \mid = \sqrt[k]{9 + 1 + 49} \\
= \sqrt{59}$$

Hence, the shortest distance between the given lines is given by

$$d = \left\lfloor \frac{(\vec{\mathbf{b}}\_1 \times \vec{\mathbf{b}}\_2) \dots (\vec{\mathbf{a}}\_2 - \vec{\mathbf{a}}\_1)}{|\vec{\mathbf{b}}\_1 \times \vec{\mathbf{b}}\_2|} \right\rfloor^{\cdot} = \frac{|\: \vec{\mathbf{3}} - \vec{\mathbf{0}} + \mathcal{T} \: \vert}{\sqrt{59}} = \frac{10}{\sqrt{59}}$$

**Example 10** Find the distance between the lines *l* 1 and *l* <sup>2</sup>given by

$$\begin{aligned} \vec{r} &= \hat{i} + 2\hat{j} - 4\hat{k} + \hat{\lambda} \left( 2\hat{i} + 3\hat{j} + 6\hat{k} \right) \\ \text{and} \\ \vec{r} &= 3\hat{i} + 3\hat{j} - 5\hat{k} + \mu \left( 2\hat{i} + 3\hat{j} + 6\hat{k} \right) \end{aligned}$$

**Solution** The two lines are parallel (Why? ) We have

$$\vec{\mathbf{a}}\_1 = \hat{\vec{i}} + 2\hat{\vec{j}} - 4\hat{k} \text{ , } \vec{\mathbf{a}}\_2 = \hat{\vec{i}}3\hat{\vec{i}} + 3\hat{\vec{j}} - 5\hat{k} \text{ , and } \vec{b} = \hat{\vec{i}}2\hat{\vec{i}} + 3\hat{\vec{j}} + 6\hat{k}$$

Therefore, the distance between the lines is given by

$$d = \left| \begin{array}{c} \vec{b} \times (\vec{a}\_2 - \vec{a}\_1) \\ \hline |\vec{b}| \end{array} \right| = \left| \begin{array}{ccc|c} \hat{i} & \hat{j} & \hat{k} \\ 2 & 3 & 6 \\ 2 & 1 & -1 \\ \hline \sqrt{4 + 9 + 36} \end{array} \right| $$

or =

49 49 7 **EXERCISE 11.2**

= =

| 9 14 4 | 293 293

**1.** Show that the three lines with direction cosines

ˆ ˆ ˆ

− + − *i j k*

12 3 4 4 12 3 3 4 12 , , ; , , ; , , 13 13 13 13 13 13 13 13 13 − − − are mutually perpendicular.

- **2.** Show that the line through the points (1, 1, 2), (3, 4, 2) is perpendicular to the line through the points (0, 3, 2) and (3, 5, 6).
- **3.** Show that the line through the points (4, 7, 8), (2, 3, 4) is parallel to the line through the points (– 1, – 2, 1), (1, 2, 5).
- **4.** Find the equation of the line which passes through the point (1, 2, 3) and is parallel to the vector ˆ ˆ ˆ 3 2 2 *i j k* + − .
- **5.** Find the equation of the line in vector and in cartesian form that passes through the point with position vector ˆ ˆ 2 4 *i j k* − + and is in the direction ˆ ˆ ˆ *i j k* + − 2 .
- **6.** Find the cartesian equation of the line which passes through the point (– 2, 4, 5)

$$\text{and parallel to the line given by } \frac{x+3}{3} = \frac{y-4}{5} = \frac{z+8}{6} \dots$$

- **7.** The cartesian equation of a line is 5 4 6 3 7 2 *x y z* − + − = = . Write its vector form.
- **8.** Find the angle between the following pairs of lines:

$$\begin{aligned} \text{(i)} \quad \vec{r} &= 2\hat{i} - \mathbf{5}\hat{j} + \hat{k} + \lambda \left(3\hat{i} + 2\hat{j} + 6\hat{k}\right) \text{ and } \\ \vec{r} &= 7\hat{i} - 6\hat{k} + \mu \left(\hat{i} + 2\hat{j} + 2\hat{k}\right) \end{aligned}$$

$$\begin{aligned} \text{(ii)} \quad \vec{r} &= 3\hat{i} + \hat{j} - 2\hat{k} + \hat{\lambda}\left(\hat{i} - \hat{j} - 2\hat{k}\right) \text{ and }\\ \vec{r} &= 2\hat{i} - \hat{j} - 56\hat{k} + \mu\left(3\hat{i} - 5\hat{j} - 4\hat{k}\right) \end{aligned}$$

**9.** Find the angle between the following pair of lines:

$$\text{(i)} \quad \frac{x-2}{2} = \frac{y-1}{5} = \frac{z+3}{-3} \text{ and } \frac{x+2}{-1} = \frac{y-4}{8} = \frac{z-5}{4}$$

$$\text{(ii)} \quad \frac{x}{2} = \frac{y}{2} = \frac{z}{1} \text{ and } \frac{x-5}{4} = \frac{y-2}{1} = \frac{z-3}{8}$$

**10.** Find the values of *p* so that the lines 1 7 14 3 3 2 2 *x y z p* − − − = =

$$\text{and} \quad \frac{7-7\chi}{3\ p} = \frac{y-5}{1} = \frac{6-z}{5} \text{ are at right angles.}$$

- **11.** Show that the lines 5 2 7 5 1 *x y z* − + = = − and 1 2 3 *x y z* = = are perpendicular to each other.
- **12.** Find the shortest distance between the lines

$$\vec{r} = \begin{pmatrix} \hat{i} + 2\hat{j} + \hat{k} \end{pmatrix} + \begin{pmatrix} \lambda \ (\hat{i} - \hat{j} + \hat{k}) \end{pmatrix} \text{ and } \vec{r}$$

$$\vec{r} = 2\hat{i} - \hat{j} - \hat{k} + \mu \left( 2\hat{i} + \hat{j} + 2\hat{k} \right)$$

**13.** Find the shortest distance between the lines

$$\frac{x+1}{7} = \frac{y+1}{-6} = \frac{z(+1)}{1} \text{ and } \underbrace{\frac{x-3}{1}}\_{-1} = \frac{y+5}{-2} = \frac{z-7}{1}$$

**14.** Find the shortest distance between the lines whose vector equations are

ˆ ˆ <sup>ˆ</sup> = + + ( 2 3 ) <sup>r</sup> *r i j k* + ˆ ˆ ˆ λ − + ( 3 2 ) *i j k*

and ˆ ˆ <sup>ˆ</sup> ˆ ˆ <sup>ˆ</sup> = + + + µ + + 4 5 6 (2 3 ) <sup>r</sup> *r i j k i j k*

**15.** Find the shortest distance between the lines whose vector equations are

$$\begin{aligned} \vec{r} &= \begin{pmatrix} 1-t \end{pmatrix} \hat{i} + \begin{pmatrix} t-2 \end{pmatrix} \hat{j} + \begin{pmatrix} 3-2 \ t \end{pmatrix} \hat{k} \text{ and } \vec{r} \\\ \vec{r} &= \begin{pmatrix} s+1 \end{pmatrix} \hat{i} + \begin{pmatrix} 2s-1 \end{pmatrix} \hat{j} - \begin{pmatrix} 2s+1 \end{pmatrix} \hat{k} \end{aligned}$$

## *Miscellaneous Exercise on Chapter 11*

- **1.** Find the angle between the lines whose direction ratios are *a*, *b*, *c* and *b* – *c*, *c* – *a*, *a* – *b*.
- **2.** Find the equation of a line parallel to *x*-axis and passing through the origin.

**3.** If the lines 1 2 3 1 1 6 and 3 2 2 3 1 5 *x y z x y z k k* − − − − − − = = = = − − are perpendicular,

find the value of *k*.

- **4.** Find the shortest distance between lines ˆ ˆ ˆ ˆ <sup>ˆ</sup> <sup>ˆ</sup> = + + + λ − + 6 2 2 ( 2 2 ) <sup>r</sup> *r i j k i j k* and ˆ ˆ ˆ <sup>ˆ</sup> <sup>ˆ</sup> = − − + µ − − 4 (3 2 2 ) <sup>r</sup> *r i k i j k* .
- **5.** Find the vector equation of the line passing through the point (1, 2, 4) and perpendicular to the two lines:

$$\frac{x-8}{3} = \frac{y+19}{-16} = \frac{z-10}{7} \text{ and } \frac{x-15}{3} = \frac{y-29}{8} = \frac{z-5}{-5} \cdot 1$$

## *Summary*

- ® **Direction cosines of a line** are the cosines of the angles made by the line with the positive directions of the coordinate axes.
- ® If *l*, *m*, *n* are the direction cosines of a line, then *l* 2 + *m*<sup>2</sup> + *n* 2 = 1.
- ® Direction cosines of a line joining two points P(*x* 1 , *y* 1 , *z* 1 ) and Q(*x* 2 , *y* 2 , *z* 2 ) are

$$\frac{x\_2 - x\_1}{\text{PQ}}, \frac{y\_2 - y\_1}{\text{PQ}}, \frac{z\_2 - z\_1}{\text{PQ}}$$

where PQ = ( )<sup>2</sup> 12 2 12 2 12 )()( −+−+− *zzyyxx*

- ® **Direction ratios of a line** are the numbers which are proportional to the direction cosines of a line.
- ® If *l*, *m*, *n* are the direction cosines and *a*, *b*, *c* are the direction ratios of a line then

$$l = \frac{\overbrace{a \quad \dotsb}^{b}}{\sqrt{a^2 + b^2 + c^2}}; m = \frac{b}{\sqrt{a^2 + b^2 + c^2}}; n = \frac{c}{\sqrt{a^2 + b^2 + c^2}}$$

- ® **Skew lines** are lines in space which are neither parallel nor intersecting. They lie in different planes.
- ® **Angle between skew lines** is the angle between two intersecting lines drawn from any point (preferably through the origin) parallel to each of the skew lines.
- ® If *l*<sup>1</sup> , *m*<sup>1</sup> , *n*<sup>1</sup> and *l* 2 , *m*<sup>2</sup> , *n*<sup>2</sup> are the direction cosines of two lines; and θ is the acute angle between the two lines; then

$$\cos \Theta\_- = \|l\_1 l\_2 + m\_1 m\_2 + n\_1 n\_2\|$$

® If *a*<sup>1</sup> , *b*<sup>1</sup> , *c*<sup>1</sup> and *a*<sup>2</sup> , *b*<sup>2</sup> , *c*<sup>2</sup> are the direction ratios of two lines and θ is the acute angle between the two lines; then

$$\cos \Theta = \left| \frac{a\_1 \ a\_2 + b\_1 \ b\_2 + c\_1 \ c\_2}{\sqrt{a\_1^2 + b\_1^2 + c\_1^2} \sqrt{a\_2^2 + b\_2^2 + c\_2^2}} \right|$$

- ® Vector equation of a line that passes through the given point whose position vector is and parallel to a given vector is = + λ <sup>r</sup> r r *r a b* .
- ® Equation of a line through a point (*x*<sup>1</sup> , *y*1 , *z* 1 ) and having direction cosines *l*, *m*, *n* is

$$\frac{x - x\_1}{l} = \frac{y - y\_1}{m} = \frac{z - z\_1}{n}$$

- ® The vector equation of a line which passes through two points whose position vectors are and is = + λ − ( ) <sup>r</sup> r r r *r a b a* .
- ® If θ is the acute angle between = + λ 1 1 r r r *r a b* and = + λ 2 2 r r r *r a b* , then

$$\cos\Theta = \left| \frac{\vec{b}\_1 \cdot \vec{b}\_2}{|\vec{b}\_1| \, |\, |\, \vec{b}\_2|} \right|$$

$$\spadesuit \quad \text{If } \frac{\mathbf{x} - \mathbf{x}\_1}{l\_1} = \frac{\mathbf{y} - \mathbf{y}\_1}{m\_1} = \frac{\mathbf{y} - \mathbf{z}\_1}{m\_1} \text{ and } \frac{\mathbf{x} - \mathbf{x}\_2}{\sqrt{-l\_2}} = \frac{\mathbf{y} - \mathbf{y}\_2}{m\_2} = \frac{\mathbf{z} - \mathbf{z}\_2}{n\_2}$$

are the equations of two lines, then the acute angle between the two lines is given by cos θ = |*l* 1 *l* 2 + *m*1*m*<sup>2</sup> + *n*<sup>1</sup> *n*2 |.

- ® Shortest distance between two skew lines is the line segment perpendicular to both the lines.
- ® Shortest distance between = + λ 1 1 <sup>r</sup> r r *r a b* and = + µ 2 2 <sup>r</sup> r r *r a b* is

$$\left| \begin{array}{c} (\vec{b}\_1 \times \vec{b}\_2) \cdot (\vec{a}\_2 - \vec{a}\_1) \\ \hline |\vec{b}\_1 \times \vec{b}\_2| \end{array} \right| $$

® Shortest distance between the lines: <sup>1</sup> <sup>1</sup> <sup>1</sup> 1 1 1 *x x y y z z a b c* − − − = = and

$$\frac{x-x\_2}{a\_2} = \frac{y-y\_2}{b\_2} = \frac{z-z\_2}{c\_2} \text{ is}$$

2 1 2 1 2 1 1 1 1 2 2 2 2 2 2 1 2 2 1 1 2 2 1 1 2 2 1 ( ) ( ) ( ) *x x y y z z a b c a b c b c b c c a c a a b a b* − − − − + − + − ® Distance between parallel lines = + λ <sup>1</sup> <sup>r</sup> r r *r a b* and = + µ <sup>2</sup> <sup>r</sup> r r *r a b* is 2 1 ( ) | | × − r r r r *b a a b* **—**v**—**