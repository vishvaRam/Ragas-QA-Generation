![](_page_0_Picture_0.jpeg)

# Chapter Seven ALTERNATING CURRENT

### 7.1 INTRODUCTION

We have so far considered direct current (dc) sources and circuits with dc sources. These currents do not change direction with time. But voltages and currents that vary with time are very common. The electric mains supply in our homes and offices is a voltage that varies like a sine function with time. Such a voltage is called *alternating voltage* (ac voltage) and the current driven by it in a circuit is called the *alternating current* (ac current)\*. Today, most of the electrical devices we use require ac voltage. This is mainly because most of the electrical energy sold by power companies is transmitted and distributed as alternating current. The main reason for preferring use of ac voltage over dc voltage is that ac voltages can be easily and efficiently converted from one voltage to the other by means of transformers. Further, electrical energy can also be transmitted economically over long distances. AC circuits exhibit characteristics which are exploited in many devices of daily use. For example, whenever we tune our radio to a favourite station, we are taking advantage of a special property of ac circuits – one of many that you will study in this chapter.

<sup>\*</sup> The phrases *ac voltage* and *ac current* are contradictory and redundant, respectively, since they mean, literally, *alternating current voltage* and *alternating current current*. Still, the abbreviation *ac* to designate an electrical quantity displaying simple harmonic time dependance has become so universally accepted that we follow others in its use. Further, *voltage* – another phrase commonly used means potential difference between two points.

![](_page_1_Picture_1.jpeg)

**Nicola Tesla (1856 – 1943)** Serbian-American scientist, inventor and genius. He conceived the idea of the rotating magnetic field, which is the basis of practically all alternating current machinery, and which helped usher in the age of electric power. He also invented among other things the induction motor, the polyphase system of ac power, and the high frequency induction coil (the Tesla coil) used in radio and television sets and other electronic equipment. The SI unit of magnetic field is named in his honour.

![](_page_1_Figure_3.jpeg)

**FIGURE 7.2** In a pure resistor, the voltage and current are in phase. The minima, zero and maxima occur at the same respective times.

5

6 – 1943)

### **7.2 AC VOLTAGE APPLIED TO A RESISTOR**

Figure 7.1 shows a resistor connected to a source ε of ac voltage. The symbol for an ac source in a circuit diagram is . We consider a source which produces sinusoidally varying potential difference across its terminals. Let this potential difference, also called ac voltage, be given by

*v v t* = *<sup>m</sup>* sin<sup>ω</sup> (7.1)

where *v<sup>m</sup>* is the amplitude of the oscillating potential difference and <sup>ω</sup> is its angular frequency.

![](_page_1_Figure_11.jpeg)

**FIGURE 7.1** AC voltage applied to a resistor.

To find the value of current through the resistor, we apply Kirchhoff's loop rule ∑*ε*( )*<sup>t</sup>* <sup>=</sup> <sup>0</sup> (refer to Section 3.12), to the circuit shown in Fig. 7.1 to get

*v t i R <sup>m</sup>* sin<sup>ω</sup> =

$$\text{or } \sum \mathbf{i} = \frac{\upsilon\_m}{R} \sin \theta \,\mathrm{s}$$

*i*

Since *R* is a constant, we can write this equation as

$$\begin{aligned} \mathfrak{i} &= \mathfrak{i}\_m \sin \mathfrak{a} t \\ \text{where the current amplitude } \mathfrak{i}\_m &\text{ is given by} \end{aligned} \tag{7.2}$$

*v*

$$\mathcal{L}\_m = \frac{\mathcal{L}\_m}{\mathcal{R}}\tag{7.3}$$

Equation (7.3) is Ohm's law, which for resistors, works equally well for both ac and dc voltages. The voltage across a pure resistor and the current through it, given by Eqs. (7.1) and (7.2) are plotted as a function of time in Fig. 7.2. Note, in particular that both *v* and *i* reach zero, minimum and maximum values at the same time. Clearly, *the voltage* and *current are in phase with each other*.

We see that, like the applied voltage, the current varies sinusoidally and has corresponding positive and negative values during each cycle. Thus, the sum of the instantaneous current values over one complete cycle is zero, and the average current is zero. The fact that the average current is zero, however, does

### Alternating Current

not mean that the average power consumed is zero and that there is no dissipation of electrical energy. As you know, Joule heating is given by *i* <sup>2</sup>*R* and depends on *i* 2 (which is always positive whether *i* is positive or negative) and not on *i*. Thus, there is Joule heating and dissipation of electrical energy when an ac current passes through a resistor.

The instantaneous power dissipated in the resistor is

$$\mathbf{p} = \mathbf{i}^2 \mathbf{R} = \mathbf{i}\_m^2 \mathbf{R} \sin^2 \boldsymbol{\alpha} \mathbf{t} \tag{7.4}$$

The average value of *p* over a cycle is\*

$$\overline{\mathbf{p}} = \mathbf{t}^2 \mathbf{R} > = <\mathbf{t}\_m^2 \mathbf{R} \sin^2 \alpha \mathbf{t} > \tag{7.5\text{(a)}}$$

where the bar over a letter (here, *p*) denotes its average value and <......> denotes taking average of the quantity inside the bracket. Since, *i* 2 *<sup>m</sup>*and *R* are constants,

$$\overline{p} = \mathrm{i}\_m^2 R < \sin^2 \alpha \text{t} > \tag{7.5\text{[b]}}$$

Using the trigonometric identity, sin<sup>2</sup> <sup>w</sup>*t* = 1/2 (1– cos 2w*t*), we have < sin<sup>2</sup> <sup>w</sup>*t >* = (1/2) (1– < cos 2w*t >*) and since < cos2w*t >* = 0\*\*, we have,

$$<\sin^2\text{ or }> = \frac{1}{2}$$

Thus,

1 <sup>2</sup> 2 *p i R* = *<sup>m</sup>* [7.5(c)]

To express ac power in the same form as dc power (*P* = *I*<sup>2</sup>*R*), a special value of current is defined and used. It is called, *root mean square* (rms) or *effective current* (Fig. 7.3) and is denoted by *I rms or I*.

![](_page_2_Figure_14.jpeg)

FIGURE 7.3 The rms current *I* is related to the peak current *i<sup>m</sup>* by *I = i<sup>m</sup>* / 2 = 0.707 *i<sup>m</sup>* .

\* The average value of a function *F* (*t*) over a period *T* is given by *F t T F t t T* ( ) ( ) <sup>=</sup> ∫ 1 0 d

$$\text{Cost} < \cos 2a \,\text{at} > = \frac{1}{T} \Big|\_{\circ}^{\text{r}} \cos 2a \,\text{at} \,\text{dt} = \frac{1}{T} \Big| \frac{\sin 2a \,\text{at}}{2a} \Big|\_{\circ}^{\text{r}} = \frac{1}{2aT} [\sin 2a \,\text{r} \,\text{T} - 0] = \text{O}$$

![](_page_2_Picture_18.jpeg)

George Westinghouse (1846 – 1914) A leading proponent of the use of alternating current over direct current. Thus, he came into conflict with Thomas Alva Edison, an advocate of direct current. Westinghouse was convinced that the technology of alternating current was the key to the electrical future. He founded the famous Company named after him and enlisted the services of Nicola Tesla and other inventors in the development of alternating current motors and apparatus for the transmission of high tension current, pioneering in large scale lighting.

GEORGE WESTINGHOUSE (1846 – 1914)

179

It is defined by

$$I = \sqrt{\overline{t^2}} = \sqrt{\frac{1}{2}\overline{t\_m^2}} = \frac{\mathfrak{i}\_m}{\sqrt{2}}$$

$$= 0.707 \ \mathfrak{i}\_m \tag{7.6}$$

In terms of *I*, the average power, denoted by *P* is

$$P = \overline{P} = \frac{1}{2} \mathfrak{l}\_m^2 R = I^2 \, R \tag{7.7}$$

Similarly, we define the *rms voltage* or *effective voltage* by

$$V = \frac{\upsilon\_m}{\sqrt{2}} = 0.707 \ \upsilon\_m \tag{7.8}$$

From Eq. (7.3), we have

$$\begin{array}{ll} \upsilon\_{m} = i\_{m}R\\ \text{or, } \frac{\upsilon\_{m}}{\sqrt{2}} = \frac{i\_{m}}{\sqrt{2}}R\\ \text{or, } \ V = IR \end{array} \qquad\qquad \bigvee\_{\begin{subarray}{c} \iota\_{\bigwedge^{\forall} \chi} \bigvee \\ \iota\_{\bigwedge^{\forall} \chi} \bigvee \end{subarray}} \bigvee\_{\begin{subarray}{c} \chi \bigvee \\ \bigvee \\ \bigvee \\ \text{right} \end{subarray}} \bigvee\_{\begin{subarray}{c} \chi \bigvee \\ \bigvee \\ \bigvee \\ \bigvee \\ \text{right} \end{subarray}} \Big\vee \begin{array}{ll} \bigvee \\ \bigvee \\ \bigvee\_{\begin{subarray}{c} \chi \bigvee \\ \chi \bigvee \\ \bigvee \\ \bigvee \\ \text{right} \end{subarray}} \Big\vee \begin{array}{ll} \bigvee \\ \bigvee \\ \bigvee \\ \bigvee \\ \begin{array}{ll} \Pi & \Pi & \Pi & \Pi & \Pi & \Pi & \Pi & \Pi \end{array} \end{array} \tag{7.9}$$

Equation (7.9) gives the relation between ac current and ac voltage and is similar to that in the dc case. This shows the advantage of introducing the concept of rms values. In terms of rms values, the equation for power [Eq. (7.7)] and relation between current and voltage in ac circuits are essentially the same as those for the dc case.

It is customary to measure and specify rms values for ac quantities. For example, the household line voltage of 220 V is an rms value with a peak voltage of

*vm* = 2 *V* = (1.414)(220 V) = 311 V

In fact, the *I* or rms current is the equivalent dc current that would produce the same average power loss as the alternating current. Equation (7.7) can also be written as

*P* = *V* 2 / *R* = *I V* (since *V* = *I R*)

Example 7.1 A light bulb is rated at 100W for a 220 V supply. Find (a) the resistance of the bulb; (b) the peak voltage of the source; and (c) the rms current through the bulb.

#### Solution

(a) We are given *P* = 100 W and *V* = 220 V. The resistance of the bulb is

$$R = \frac{V^{\circ}}{P} = \frac{\left(220\,\text{V}\right)^{\circ}}{1\,\text{OO}\,\text{W}} = 484\,\Omega$$

(b) The peak voltage of the source is

*v V <sup>m</sup>* = = 2 311V

(c) Since, *P* = *I V*

$$I = \frac{P}{V} = \frac{100\,\text{W}}{220\,\text{V}} = 0.454\,\text{A}$$

# 7.3 REPRESENTATION OF AC CURRENT AND VOLTAGE BY ROTATING VECTORS — PHASORS

In the previous section, we learnt that the current through a resistor is in phase with the ac voltage. But this is not so in the case of an inductor, a capacitor or a combination of these circuit elements. In order to show

phase relationship between voltage and current in an ac circuit, we use the notion of *phasors*. The analysis of an ac circuit is facilitated by the use of a phasor diagram. A phasor\* is a vector which rotates about the origin with angular speed w, as shown in Fig. 7.4. The vertical components of phasors V and I represent the sinusoidally varying quantities *v* and *i*. The magnitudes of phasors V and I represent the amplitudes or the peak values *v<sup>m</sup>* and *i<sup>m</sup>* of these oscillating quantities. Figure 7.4(a) shows the voltage and current phasors and their relationship at time *t* 1 for the case of an ac source connected to a resistor i.e., corresponding to the circuit shown in Fig. 7.1. The projection of

![](_page_4_Figure_4.jpeg)

circuit in Fig 7.1. (b) Graph of *v* and *i* versus w*t*.

voltage and current phasors on vertical axis, i.e., *v<sup>m</sup>* sinw *t* and *i<sup>m</sup>* sinw *t*, respectively represent the value of voltage and current at that instant. As they rotate with frequency w, curves in Fig. 7.4(b) are generated. From Fig. 7.4(a) we see that phasors V and I for the case of a resistor are

in the same direction. This is so for all times. This means that the phase angle between the voltage and the current is zero.

# 7.4 AC VOLTAGE APPLIED TO AN INDUCTOR

Figure 7.5 shows an ac source connected to an inductor. Usually, inductors have appreciable resistance in their windings, but we shall

assume that this inductor has negligible resistance. Thus, the circuit is a purely inductive ac circuit. Let the voltage across the source be *v* = *v<sup>m</sup>* sinw *t*. Using

the Kirchhoff's loop rule, ∑*<sup>ε</sup>* ( ) *<sup>t</sup>* <sup>=</sup> <sup>0</sup> , and since there is no resistor in the circuit,

$$\boldsymbol{\upsilon} - L \frac{\mathbf{d}t}{\mathbf{d}t} = \mathbf{0} \tag{7.10}$$

where the second term is the self-induced Faraday emf in the inductor; and *L* is the self-inductance of

![](_page_4_Figure_15.jpeg)

FIGURE 7.5 An ac source connected to an inductor.

<sup>\*</sup> Though voltage and current in ac circuit are represented by phasors – rotating vectors, they are not vectors themselves. They are scalar quantities. It so happens that the amplitudes and phases of harmonically varying scalars combine mathematically in the same way as do the projections of rotating vectors of corresponding magnitudes and directions. The *rotating vectors* that *represent* harmonically varying scalar quantities are introduced only to provide us with a simple way of adding these quantities using a rule that we already know.

the inductor. The negative sign follows from Lenz's law (Chapter 6). Combining Eqs. (7.1) and (7.10), we have

$$\frac{\text{d}l}{\text{d}t} = \frac{\upsilon}{L} = \frac{\upsilon\_m}{L} \sin \alpha t \tag{7.11}$$

Equation (7.11) implies that the equation for *i*(*t*), the current as a function of time, must be such that its slope d*i*/d*t* is a sinusoidally varying quantity, with the same phase as the source voltage and an amplitude given by *v<sup>m</sup> /L*. To obtain the current, we integrate d*i*/d*t* with respect to time:

$$\begin{aligned} \int \frac{\mathrm{d}t}{\mathrm{d}t} \mathrm{d}t &= \frac{\upsilon\_m}{L} \int \sin(a\mathfrak{t}) \mathrm{d}t \\ \text{and get,} \\ \end{aligned} $$

$$d = -\frac{\upsilon\_m}{\alpha L} \cos(\alpha t) + \text{constant}$$

The integration constant has the dimension of current and is timeindependent. Since the source has an emf which oscillates symmetrically about zero, the current it sustains also oscillates symmetrically about zero, so that no constant or time-independent component of the current exists. Therefore, the integration constant is zero.

Using

$$t - \cos(\alpha t) = \sin\left(\alpha t - \frac{\pi}{2}\right), \text{ we have}$$

$$t = t\_m \sin\left(\alpha t - \frac{\pi}{2}\right) \tag{7.12}$$

where *<sup>m</sup> m v i L* = ω is the amplitude of the current. The quantity w *L* is analogous to the resistance and is called *inductive reactance*, denoted by *X<sup>L</sup>* :

$$X\_{\downarrow} = \alpha \ll L \tag{7.13}$$

The amplitude of the current is, then

$$\mathbf{M}\_m = \frac{\mathbf{\nu}\_m}{\mathbf{X}\_L} \tag{7.14}$$

The dimension of inductive reactance is the same as that of resistance and its SI unit is ohm (W). The inductive reactance limits the current in a purely inductive circuit in the same way as the resistance limits the current in a purely resistive circuit. The inductive reactance is directly proportional to the inductance and to the frequency of the current.

A comparison of Eqs. (7.1) and (7.12) for the source voltage and the current in an inductor shows that the current lags the voltage by p/2 or one-quarter (1/4) cycle. Figure 7.6 (a) shows the voltage and the current phasors in the present case at instant *t* 1 . The current phasor I is p/2 behind the voltage phasor V. When rotated with frequency w counterclockwise, they generate the voltage and current given by Eqs. (7.1) and (7.12), respectively and as shown in Fig. 7.6(b).

![](_page_5_Picture_15.jpeg)

![](_page_6_Figure_1.jpeg)

FIGURE 7.6 (a) A Phasor diagram for the circuit in Fig. 7.5. (b) Graph of *v* and *i* versus w*t*.

We see that the current reaches its maximum value later than the

voltage by one-fourth of a period *T* 4 2 = π/ *ω* . You have seen that an inductor has reactance that limits current similar to resistance in a dc circuit. Does it also consume power like a resistance? Let us try to find out.

The instantaneous power supplied to the inductor is

$$p\_L = i\,\upsilon = i\_m \sin\left(\alpha \, t - \frac{\pi}{2}\right) \times \upsilon\_m \sin\left(\alpha t\right)$$

$$= -i\_m \upsilon\_m \cos(\alpha t) \sin(\alpha t)$$

$$= -\frac{i\_m \upsilon\_m}{2} \sin(2\alpha t)$$

So, the average power over a complete cycle is

$$P\_{\mathcal{L}} = \left\langle -\frac{\mathfrak{l}\_m \upsilon\_m}{2} \sin \left( 2 \alpha t \right) \right\rangle$$

$$= -\frac{\mathfrak{l}\_m \upsilon\_m}{2} \left\langle \sin \left( 2 \alpha t \right) \right\rangle = 0,$$

since the average of sin (2w*t*) over a complete cycle is zero.

Thus, the *average power supplied to an inductor over one complete cycle is zero*.

Example 7.2 A pure inductor of 25.0 mH is connected to a source of 220 V. Find the inductive reactance and rms current in the circuit if the frequency of the source is 50 Hz.

Solution The inductive reactance,

$$\begin{aligned} X\_L &= 2 \,\pi \,\nu L = 2 \times 3.14 \times 50 \times 25 \times 10^{-3} \,\Omega\\ &= 7.85 \Omega \end{aligned}$$

The rms current in the circuit is

$$I = \frac{V}{X\_L} = \frac{220\,\text{V}}{7.85\,\Omega} = 28\,\text{A}$$

![](_page_7_Picture_0.jpeg)

# 7.5 AC VOLTAGE APPLIED TO A CAPACITOR

Figure 7.7 shows an ac source e generating ac voltage *v* = *v<sup>m</sup>* sin wt connected to a capacitor only, a purely capacitive ac circuit.

![](_page_7_Figure_3.jpeg)

![](_page_7_Figure_4.jpeg)

When a capacitor is connected to a voltage source in a dc circuit, current will flow for the short time required to charge the capacitor. As charge accumulates on the capacitor plates, the voltage across them increases, opposing the current. That is, a capacitor in a dc circuit will limit or oppose the current as it charges. When the capacitor is fully charged, the current in the circuit falls to zero.

When the capacitor is connected to an ac source, as in Fig. 7.7, it limits or regulates the current, but does not completely prevent the flow of charge. The capacitor is alternately charged and discharged as the current reverses each half cycle. Let *q* be the

charge on the capacitor at any time *t*. The instantaneous voltage *v* across the capacitor is

*q v C* = (7.15)

From the Kirchhoff's loop rule, the voltage across the source and the capacitor are equal,

$$\upsilon\_m \sin \alpha t = \frac{q}{C}$$

To find the current, we use the relation <sup>d</sup> d *q i t* =

$$\overline{\mathbf{d}} = \frac{\mathbf{d}}{\mathbf{d}t} \left( \upsilon\_m \mathbf{C} \sin(\alpha t) \right) = \alpha \mathbf{C} \,\upsilon\_m \cos(\alpha t).$$

Using the relation, cos( ) sin *<sup>ω</sup> <sup>ω</sup> t t* = + π 2 , we have

$$\mathbf{t} = \mathbf{t}\_m \sin \left( \cot \tau + \frac{\pi}{2} \right) \tag{7.16}$$

where the amplitude of the oscillating current is *i<sup>m</sup>* = w*Cv<sup>m</sup>* . We can rewrite it as

$$\mathfrak{i}\_m = \frac{\upsilon\_m}{\langle 1/\,\, aC \rangle}$$

Comparing it to *i<sup>m</sup>* = *v<sup>m</sup>* /*R* for a purely resistive circuit, we find that (1/w*C)* plays the role of resistance. It is called *capacitive reactance* and is denoted by *X<sup>c</sup>* ,

$$X\_c = 1/\alpha C$$

so that the amplitude of the current is

$$\mathfrak{i}\_m = \frac{\mathfrak{U}\_m}{X\_{\mathbb{C}}} \tag{7.18}$$

184

The dimension of capacitive reactance is the same as that of resistance and its SI unit is ohm (Ω). The capacitive reactance limits the amplitude of the current in a purely capacitive circuit in the same way as the resistance limits the current in a purely resistive circuit. But it is inversely proportional to the frequency and the capacitance.

A comparison of Eq. (7.16) with the equation of source voltage, Eq. (7.1) shows that the current is π/2 ahead of voltage.

Figure 7.8(a) shows the phasor diagram at an instant *t* 1 . Here the current phasor **I** is π/2 ahead of the voltage phasor **V** as they rotate counterclockwise. Figure 7.8(b) shows the variation of voltage and current with time. We see that the current reaches its maximum value earlier than the voltage by one-fourth of a period.

The instantaneous power supplied to the capacitor is

$$\begin{array}{l} \mathbf{p}\_c = \mathbf{i}\,\boldsymbol{\nu} = \mathbf{i}\_m \cos(\omega t) \boldsymbol{\nu}\_m \sin(\omega t) \\ = \mathbf{i}\_m \boldsymbol{\nu}\_m \cos(\omega t) \sin(\omega t) \\ = \frac{\mathbf{i}\_m \boldsymbol{\nu}\_m}{2} \sin(2\omega t) \end{array} \tag{7.19}$$

So, as in the case of an inductor, the average power

$$P\_C = \left\langle \frac{\mathfrak{l}\_m \upsilon\_m}{2} \sin(2\alpha t) \right\rangle = \frac{\mathfrak{l}\_m \upsilon\_m}{2} \left\langle \sin(2\alpha t) \right\rangle = 0$$

since <sin (2ω*t*)> = 0 over a complete cycle.

Thus, we see that in the case of an inductor, the current lags the voltage by π/2 and in the case of a capacitor, the current leads the voltage by π/2.

**Example 7.3** A lamp is connected in series with a capacitor. Predict your observations for dc and ac connections. What happens in each case if the capacitance of the capacitor is reduced?

**Solution** When a dc source is connected to a capacitor, the capacitor gets charged and after charging no current flows in the circuit and the lamp will not glow. There will be no change even if *C* is reduced. With ac source, the capacitor offers capacitative reactance (1/ω*C*) and the current flows in the circuit. Consequently, the lamp will shine. Reducing *C* will increase reactance and the lamp will shine less brightly than before.

**Example 7.4** A 15.0 µF capacitor is connected to a 220 V, 50 Hz source. Find the capacitive reactance and the current (rms and peak) in the circuit. If the frequency is doubled, what happens to the capacitive reactance and the current?

**Solution** The capacitive reactance is

$$X\_{\rm C} = \frac{1}{2\,\pi\,\nu\,\text{C}} = \frac{1}{2\pi (50\,\text{Hz})(15.0 \times 10^{-6}\,\text{F})} = 212\,\Omega$$

The rms current is

![](_page_8_Figure_15.jpeg)

**FIGURE 7.8** (a) A Phasor diagram for the circuit in Fig. 7.7. (b) Graph of *v* and *i* versus ω*t*.

> **EXAMPLE 7.3 EXAMPLE**

 **7.4**

$$I = \frac{V}{X\_C} = \frac{220\,\text{V}}{212\,\Omega} = 1.04\,\text{A}$$

The peak current is

*i I <sup>m</sup>* = = 2 (1.41)(1.04 ) 1.47 *A A* =

This current oscillates between +1.47A and –1.47 A, and is ahead of the voltage by p/2.

If the frequency is doubled, the capacitive reactance is halved and consequently, the current is doubled.

Example 7.5 A light bulb and an open coil inductor are connected to an ac source through a key as shown in Fig. 7.9.

![](_page_9_Figure_7.jpeg)

The switch is closed and after sometime, an iron rod is inserted into the interior of the inductor. The glow of the light bulb (a) increases; (b) decreases; (c) is unchanged, as the iron rod is inserted. Give your answer with reasons.

EXAMPLE 7.5 EXAMPLE 7.4

Solution As the iron rod is inserted, the magnetic field inside the coil magnetizes the iron increasing the magnetic field inside it. Hence, the inductance of the coil increases. Consequently, the inductive reactance of the coil increases. As a result, a larger fraction of the applied ac voltage appears across the inductor, leaving less voltage across the bulb. Therefore, the glow of the light bulb decreases.

### 7.6 AC VOLTAGE APPLIED TO <sup>A</sup> SERIES LCR CIRCUIT

Figure 7.10 shows a series LCR circuit connected to an ac source e. As usual, we take the voltage of the source to be *v = v<sup>m</sup>* sin w*t*.

![](_page_9_Figure_13.jpeg)

If *q* is the charge on the capacitor and *i* the current, at time *t*, we have, from Kirchhoff's loop rule:

$$L\frac{d\mathbf{l}}{dt} + \mathbf{l}\,R + \frac{q}{C} = \boldsymbol{\upsilon} \tag{7.20}$$

We want to determine the instantaneous current *i* and its phase relationship to the applied alternating voltage *v*. We shall solve this problem by two methods. First, we use the technique of phasors and in the second method, we solve Eq. (7.20) analytically to obtain the time– dependence of *i*.

#### 7.6.1 Phasor-diagram solution

From the circuit shown in Fig. 7.10, we see that the resistor, inductor and capacitor are in series. Therefore, the ac current in each element is the same at any time, having the same amplitude and phase. Let it be

$$\mathbf{i} = \mathbf{i}\_m \sin \{ \alpha t + \phi \}\tag{7.21}$$

where f is the phase difference between the voltage across the source and the current in the circuit. On the basis of what we have learnt in the previous sections, we shall construct a phasor diagram for the present case.

Let I be the phasor representing the current in the circuit as given by Eq. (7.21). Further, let V<sup>L</sup> , V<sup>R</sup> , V<sup>C</sup> , and V represent the voltage across the inductor, resistor, capacitor and the source, respectively. From previous section, we know that V<sup>R</sup> is parallel to I, V<sup>C</sup> is p/2

behind I and V<sup>L</sup> is p/2 ahead of I. V<sup>L</sup> , V<sup>R</sup> , V<sup>C</sup> and I are shown in Fig. 7.11(a) with apppropriate phaserelations.

The length of these phasors or the amplitude of V<sup>R</sup> , V<sup>C</sup> and V<sup>L</sup> are:

$$\boldsymbol{\upsilon}\_{\mathcal{C}m} = \mathfrak{i}\_m \boldsymbol{R}, \ \boldsymbol{\upsilon}\_{\mathcal{C}m} = \mathfrak{i}\_m \boldsymbol{X}\_{\mathcal{C}}, \ \boldsymbol{\upsilon}\_{\mathcal{L}m} = \mathfrak{i}\_m \boldsymbol{X}\_{\mathcal{L}}\tag{7.22}$$

The voltage Equation (7.20) for the circuit can be written as

$$
\omega\_{\rm L} + \upsilon\_{\rm R} + \upsilon\_{\rm C} = \upsilon \tag{7.23}
$$

The phasor relation whose vertical component gives the above equation is

$$\mathbf{v\_L + \mathbf{v\_R + \mathbf{v\_C = v\_L}}} = \mathbf{v} \tag{7.24}$$

This relation is represented in Fig. 7.11(b). Since VC and V<sup>L</sup> are always along the same line and in

opposite directions, they can be combined into a single phasor (V<sup>C</sup> + V<sup>L</sup> ) which has a magnitude ½*vCm* – *vLm*½. Since V is represented as the hypotenuse of a right-triangle whose sides are V<sup>R</sup> and (V<sup>C</sup> + V<sup>L</sup> ), the pythagorean theorem gives:

$$
\boldsymbol{\upsilon}\_{m}^{2} = \boldsymbol{\upsilon}\_{\text{R}m}^{2} + \left(\boldsymbol{\upsilon}\_{\text{C}m} - \boldsymbol{\upsilon}\_{\text{L}m}\right)^{2}
$$

Substituting the values of *vRm*, *vCm*, and *vLm* from Eq. (7.22) into the above equation, we have

$$\begin{aligned} \boldsymbol{\upsilon}\_{m}^{2} &= \{\mathbf{i}\_{m}\mathbf{R}\}^{2} + \{\mathbf{i}\_{m}\mathbf{X}\_{C} - \mathbf{i}\_{m}\mathbf{X}\_{L}\}^{2} \\ &= \mathbf{i}\_{m}^{2} \left[\boldsymbol{R}^{2} + \{\mathbf{X}\_{C} - \mathbf{X}\_{L}\right\}^{2}\right] \\ &\quad \cdot \quad \boldsymbol{\upsilon}\_{m} = \frac{\mathbf{\upsilon}\_{m}}{\sqrt{\mathbf{R}^{2} + \{\mathbf{X}\_{C} - \mathbf{X}\_{L}\}^{2}}} \\ &\quad \text{or,} \quad \boldsymbol{l}\_{m} = \frac{\mathbf{\upsilon}\_{m}}{\sqrt{\mathbf{R}^{2} + \{\mathbf{X}\_{C} - \mathbf{X}\_{L}\}^{2}}} \end{aligned} \tag{7.25(a)}$$

By analogy to the resistance in a circuit, we introduce the *impedance Z* in an ac circuit:

$$\mathbf{f}\_m = \frac{\mathcal{U}\_m}{\mathbf{Z}} \tag{7.25\text{[b]}}$$

where <sup>2</sup> <sup>2</sup> ( ) *Z R X X* = + − *C L* (7.26)

FIGURE 7.11 (a) Relation between the phasors V<sup>L</sup> , V<sup>R</sup> , V<sup>C</sup> , and *I*, (b) Relation between the phasors V<sup>L</sup> , V<sup>R</sup> , and (V<sup>L</sup> + V<sup>C</sup> ) for the circuit in Fig. 7.10.

[7.25(a)]

![](_page_10_Figure_23.jpeg)

![](_page_11_Figure_1.jpeg)

diagram.

Since phasor I is always parallel to phasor V<sup>R</sup> , the phase angle f is the angle between V<sup>R</sup> and V and can be determined from Fig. 7.12:

$$
\tan \phi = \frac{\upsilon\_{Cm} - \upsilon\_{Lm}}{\upsilon\_{Rm}}
$$

$$
\text{Using Eq. (7.22), we have}
$$

$$
\tan \phi = \frac{X\_C - X\_L}{R} \tag{7.27}
$$

Equations (7.26) and (7.27) are graphically shown in Fig. (7.12). This is called *Impedance diagram* which is a right-triangle with *Z* as its hypotenuse.

Equation 7.25(a) gives the amplitude of the current and Eq. (7.27) gives the phase angle. With these, Eq. (7.21) is completely specified.

If *X<sup>C</sup>* > *X<sup>L</sup>* , f is positive and the circuit is predominantly capacitive. Consequently, the current in the circuit leads the source voltage. If *XC* < *X<sup>L</sup>* , f is negative and the circuit is predominantly inductive. Consequently, the current in the circuit lags the source voltage.

Figure 7.13 shows the phasor diagram and variation of *v* and *i* with w *t* for the case *X<sup>C</sup>* > *X<sup>L</sup>* .

![](_page_11_Figure_8.jpeg)

![](_page_11_Figure_9.jpeg)

Thus, we have obtained the amplitude and phase of current for an *LCR* series circuit using the technique of phasors. But this method of analysing ac circuits suffers from certain disadvantages. First, the phasor diagram say nothing about the initial condition. One can take any arbitrary value of *t* (say, *t* 1 , as done throughout this chapter) and draw different phasors which show the relative angle between different phasors. The solution so obtained is called the *steady-state solution*. This is not a general solution. Additionally, we do have a *transient solution* which exists even for *v* = 0. The general solution is the sum of the transient solution and the steady-state

solution. After a sufficiently long time, the effects of the transient solution die out and the behaviour of the circuit is described by the steady-state solution.

### 7.6.2 Resonance

An interesting characteristic of the series *RLC* circuit is the phenomenon of resonance. The phenomenon of resonance is common among systems that have a tendency to oscillate at a particular frequency. This frequency is called the system's *natural frequency*. If such a system is driven by an energy source at a frequency that is near the natural frequency, the amplitude of oscillation is found to be large. A familiar example of this phenomenon is a child on a swing. The swing has a natural frequency for swinging back and forth like a pendulum. If the child pulls on the

rope at regular intervals and the frequency of the pulls is almost the same as the frequency of swinging, the amplitude of the swinging will be large.

For an *RLC* circuit driven with voltage of amplitude *v<sup>m</sup>* and frequency <sup>w</sup>, we found that the current amplitude is given by

$$\mathfrak{u}\_m = \frac{\upsilon\_m}{Z} = \frac{\upsilon\_m}{\sqrt{R^2 + (X\_C - X\_L)^2}}$$

with *X<sup>c</sup>* = 1/w*C* and *X<sup>L</sup>* = w *L*. So if w is varied, then at a particular frequency

<sup>w</sup><sup>0</sup> , *X<sup>c</sup>* = *X<sup>L</sup>* , and the impedance is minimum ( ) 2 2 *Z R R* = + = 0 . This frequency is called the *resonant frequency*:

$$X\_c = X\_L \text{ or } \frac{1}{a\_0 \text{ C}} = a\_0 \text{ L}$$

$$\text{or} \quad a\_0 = \frac{1}{\sqrt{LC}}\tag{7.28}$$

*LC* At resonant frequency, the current amplitude is maximum; *i<sup>m</sup> = v<sup>m</sup> /R*.

Figure 7.16 shows the variation of *i<sup>m</sup>* with <sup>w</sup> in a *RLC* series circuit with *L* = 1.00 mH, *C* = 1.00 nF for two values of *R*: (i) *R* = 100 W and (ii) *R* = 200 W. For the source applied *v<sup>m</sup>* =

100 V. <sup>w</sup><sup>0</sup> for this case is 1 *LC* = 1.00×10<sup>6</sup>

rad/s.

We see that the current amplitude is maximum at the resonant frequency. Since *i<sup>m</sup>* = *v<sup>m</sup>* / *R* at resonance, the current amplitude for case (i) is twice to that for case (ii).

Resonant circuits have a variety of applications, for example, in the tuning mechanism of a radio or a TV set. The antenna of a radio accepts signals from many broadcasting stations. The signals picked up in the antenna acts as a source in the tuning circuit of the radio, so the circuit can be driven at many frequencies. But to hear one particular radio station, we tune the radio. In tuning, we vary the capacitance of a capacitor in the tuning circuit such that the resonant frequency of the circuit becomes nearly equal to the frequency of the radio signal received. When this happens, the amplitude of the current with the frequency of the signal of the particular radio station in the circuit is maximum.

*It is important to note that resonance phenomenon is exhibited by a circuit only if both L and C are present in the circuit. Only then do the voltages across L and C cancel each other (both being out of phase) and the current amplitude is v<sup>m</sup> /R, the total source voltage appearing across R. This means that we cannot have resonance in a RL or RC circuit.*

![](_page_12_Figure_14.jpeg)

![](_page_12_Figure_15.jpeg)

Example 7.6 A resistor of 200 W and a capacitor of 15.0 mF are connected in series to a 220 V, 50 Hz ac source. (a) Calculate the current in the circuit; (b) Calculate the voltage (rms) across the resistor and the capacitor. Is the algebraic sum of these voltages more than the source voltage? If yes, resolve the paradox.

#### Solution

Given

F <sup>6</sup> *R C* 200 , 15.0 15.0 10 F <sup>−</sup> = Ω = µ = ×

*V* = = 220 V, 50Hz <sup>ν</sup>

(a) In order to calculate the current, we need the impedance of the circuit. It is

$$\begin{aligned} Z &= \sqrt{R^2 + X\_C^2} = \sqrt{R^2 + \left[2\pi\,\nu C\right]^{-2}} \\ &= \sqrt{\left[200\,\Omega\right]^2 + \left[2 \times 3.14 \times 50 \times 15.0 \times 10^{-6}\,\text{F}\right]^{1/2}} \\ &= \sqrt{\left[200\,\Omega\right]^2 + \left[212.3\,\Omega\right]^2} \\ &\dots \end{aligned}$$

= Ω 291.67

Therefore, the current in the circuit is

$$I = \frac{V}{Z} = \frac{220\,\text{V}}{291.5\,\Omega} = 0.755\,\text{A}$$

(b) Since the current is the same throughout the circuit, we have *V I R <sup>R</sup>* = = (0.755 A)(200 ) 151V Ω =

*V I X C C* = = (0.755 A)(212.3 ) 160.3 V Ω =

The algebraic sum of the two voltages, *V<sup>R</sup>* and *V<sup>C</sup>* is 311.3 V which is more than the source voltage of 220 V. How to resolve this paradox? As you have learnt in the text, the two voltages are not in the same phase. Therefore, *they cannot be added like ordinary numbers*. The two voltages are out of phase by ninety degrees. Therefore, the total of these voltages must be obtained using the Pythagorean theorem:

$$\begin{aligned} V\_{R \leftrightarrow C} &= \sqrt{V\_R^2 + V\_C^2} \\ &= 220 \text{ V} \end{aligned}$$

Thus, if the phase difference between two voltages is properly taken into account, the total voltage across the resistor and the capacitor is equal to the voltage of the source.

### 7.7 POWER IN AC CIRCUIT: THE POWER FACTOR

We have seen that a voltage *v = v<sup>m</sup>* sinw*t* applied to a series *RLC* circuit drives a current in the circuit given by *i* = *i<sup>m</sup>* sin(w*t* + f) where

$$\mathfrak{i}\_m = \frac{\upsilon\_m}{Z} \quad \text{and} \quad \phi = \tan^{-1}\left(\frac{X\_C - X\_L}{R}\right).$$

Therefore, the instantaneous power *p* supplied by the source is

$$p = \upsilon \, t = \left(\upsilon\_m \sin \alpha t\right) \times \left[l\_m \sin(\alpha t + \phi)\right]$$

$$\dot{l} = \frac{\upsilon\_m l\_m}{2} \left[\cos \phi - \cos(2\alpha t + \phi)\right] \tag{7.29}$$

The average power over a cycle is given by the average of the two terms in R.H.S. of Eq. (7.29). It is only the second term which is time-dependent. Its average is zero (the positive half of the cosine cancels the negative half). Therefore,

$$P = \frac{\upsilon\_m l\_m}{2} \cos \phi = \frac{\upsilon\_m}{\sqrt{2}} \frac{l\_m}{\sqrt{2}} \cos \phi$$

$$\dot{I} = V \, I \cos \phi \,\tag{7.30(a)}$$

This can also be written as,

2 *P I Z* = cosφ [7.30(b)]

So, the average power dissipated depends not only on the voltage and current but also on the cosine of the phase angle φ between them. The quantity cosφ is called the power factor. Let us discuss the following cases:

Case (i) (i) Case Resistive circuit: If the circuit contains only pure R, it is called resistive. In that case φ = 0, cos φ =1.Thereis maximum power dissipation.

Case (ii) (ii) Case Purely inductive or capacitive circuit: If the circuit contains only an inductor or capacitor, we know that the phase difference between voltage and current is π/2. Therefore, cos φ = 0, and no power is dissipated even though a current is flowing in the circuit. This current is sometimes referred to as wattless current.

Case (iii) (iii) LCR series circuit: In an LCR series circuit, power dissipated is given by Eq. (7.30) where φ = tan–1 (<sup>X</sup><sup>c</sup> –<sup>X</sup><sup>L</sup> )/ R. So, φ may be non-zero in a RL or RC or RCL circuit. Even in such cases, power is dissipated only in the resistor.

Case (iv) Case (iv)Case Power dissipated at resonance in LCR circuit: At resonance Xc –<sup>X</sup><sup>L</sup> = 0, and φ = 0. Therefore, cosφ = 1 and P = I <sup>2</sup>Z = <sup>I</sup> <sup>2</sup> <sup>R</sup>. That is, maximum power is dissipated in a circuit (through R) at resonance.

Example 7.7 (a) For circuits used for transporting electric power, a low power factor implies large power loss in transmission. Explain.

(b) Power factor can often be improved by the use of a capacitor of appropriate capacitance in the circuit. Explain.

Solution SolutionSolution (a) We know that P =<sup>I</sup> <sup>V</sup> cosφ where cosφ is the power factor. To supply a given power at a given voltage, if cosφ is small, we have to increase current accordingly. But this will lead to large power loss (I <sup>2</sup>R) in transmission.

(b)Suppose in a circuit, current I lags the voltage by an angle φ. Then power factor cosφ =R/Z.

We can improve the power factor (tending to 1) by making Z tend to <sup>R</sup>. Let us understand, with the help of a phasor diagram (Fig. 7.15)

![](_page_15_Figure_1.jpeg)

how this can be achieved. Let us resolve I into two components. I *p* along the applied voltage V and I *q* perpendicular to the applied voltage. I *q* as you have learnt in Section 7.7, is called the wattless component since corresponding to this component of current, there is no power loss. I<sup>P</sup> is known as the power component because it is in phase with the voltage and corresponds to power loss in the circuit.

It's clear from this analysis that if we want to improve power factor, we must completely neutralize the lagging wattless current I q by an equal leading wattless current I¢ q . This can be done by connecting a capacitor of appropriate value in parallel so that I q and I¢ q cancel each other and *P* is effectively *I* <sup>p</sup> *V*.

Example 7.8 A sinusoidal voltage of peak value 283 V and frequency 50 Hz is applied to a series *LCR* circuit in which R = 3 W, *L* = 25.48 mH, and C = 796 mF. Find (a) the impedance of the circuit; (b) the phase difference between the voltage across the source and the current; (c) the power dissipated in the circuit; and (d) the power factor.

#### Solution

(a) To find the impedance of the circuit, we first calculate *X*<sup>L</sup> and *X*<sup>C</sup> .

$$\begin{array}{l} X\_L = 2 \text{ } \pi \upsilon L\\ \cdot = 2 \times 3.14 \times 50 \times 25.48 \times 10^{-3} \,\Omega = 8 \,\Omega\\ X\_C = \frac{1}{2 \pi \upsilon C} \\\\ 1 & 4 \Omega \end{array}$$

6 4 2 3.14 50 796 10<sup>−</sup> = = Ω × × × ×

Therefore,

$$\begin{split} Z &= \sqrt{\mathbf{R}^2 + (X\_L - X\_C)^2} = \sqrt{\mathbf{S}^2 + (\mathbf{S} - 4)^2} \\ &= \mathbf{5} \ \Omega \end{split}$$

(b) Phase difference, f = tan–1 *X X C L R* −

$$=\tan^{-1}\left(\frac{4-8}{3}\right) = -53.1^{\circ}$$

EXAMPLE 7.7

### Alternating Current

Since f is negative, the current in the circuit lags the voltage across the source.

(c) The power dissipated in the circuit is

$$P = I^2 R$$

$$\begin{aligned} \text{Now,} \quad I &= \frac{\dot{t}\_m}{\sqrt{2}} = \frac{1}{\sqrt{2}} \left( \frac{283}{5} \right) = 40 \text{A} \\ \text{Therefore,} \quad P &= \text{(40A)}^2 \times 3 \,\Omega = 4800 \,\text{W} \end{aligned}$$

(d) Power factor = cos cos –53.1 0.6 -

Example 7.9 Suppose the frequency of the source in the previous example can be varied. (a) What is the frequency of the source at which resonance occurs? (b) Calculate the impedance, the current, and the power dissipated at the resonant condition.

#### Solution

(a) The frequency at which the resonance occurs is

$$\begin{aligned} \rho\_0 &= \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{25.48 \times 10^{-3} \times 796 \times 10^{-6}}} \\ &= 222.1 \,\text{rad/s} \\\\ \nu\_r &= \frac{\rho\_0}{2\pi} = \frac{221.1}{2 \times 3.14} \,\text{Hz} = 35.4 \,\text{Hz} \end{aligned}$$

(b) The impedance *Z* at resonant condition is equal to the resistance:

$$Z = R = 3\,\Omega$$

The rms current at resonance is

$$=\frac{V}{Z} = \frac{V}{R} = \left(\frac{283}{\sqrt{2}}\right)\frac{1}{3} = 66.7 \text{A}$$

The power dissipated at resonance is

<sup>2</sup> <sup>2</sup> *P I R* = × = × = (66.7) 3 13.35 kW

You can see that in the present case, power dissipated at resonance is more than the power dissipated in Example 7.8.

Example 7.10 At an airport, a person is made to walk through the doorway of a metal detector, for security reasons. If she/he is carrying anything made of metal, the metal detector emits a sound. On what principle does this detector work?

Solution The metal detector works on the principle of resonance in ac circuits. When you walk through a metal detector, you are, in fact, walking through a coil of many turns. The coil is connected to a capacitor tuned so that the circuit is in resonance. When you walk through with metal in your pocket, the impedance of the circuit changes – resulting in significant change in current in the circuit. This change in current is detected and the electronic circuitry causes a sound to be emitted as an alarm.

 EXAMPLE 7.9 EXAMPLE 7.8 E

XAMPLE 7.10

193

# 7.8 TRANSFORMERS

For many purposes, it is necessary to change (or transform) an alternating voltage from one to another of greater or smaller value. This is done with a device called *transformer* using the principle of mutual induction.

A transformer consists of two sets of coils, insulated from each other. They are wound on a soft-iron core, either one on top of the other as in Fig. 7.16(a) or on separate limbs of the core as in Fig. 7.16(b). One of the coils called the *primary coil* has *N p* turns. The other coil is called the *secondary coil*; it has *N<sup>s</sup>* turns. Often the primary coil is the input coil and the secondary coil is the output coil of the transformer.

![](_page_17_Figure_4.jpeg)

![](_page_17_Figure_5.jpeg)

When an alternating voltage is applied to the primary, the resulting current produces an alternating magnetic flux which links the secondary and induces an emf in it. The value of this emf depends on the number of turns in the secondary. We consider an ideal transformer in which the primary has negligible resistance and all the flux in the core links both primary and secondary windings. Let f be the flux in each turn in the core at time *t* due to current in the primary when a voltage *v<sup>p</sup>* is applied to it.

Then the induced emf or voltage <sup>e</sup> *s* , in the secondary with *N<sup>s</sup>* turns is

$$
\varepsilon\_s = -N\_s \frac{\mathrm{d}\phi}{\mathrm{d}t} \tag{7.31}
$$

The alternating flux f also induces an emf, called back emf in the primary. This is

$$
\varepsilon\_p = -N\_p \frac{\mathbf{d}\phi}{\mathbf{d}t} \tag{7.32}
$$

But <sup>e</sup>*<sup>p</sup> = v<sup>p</sup> .* If this were not so, the primary current would be infinite since the primary has zero resistance (as assumed). If the secondary is an open circuit or the current taken from it is small, then to a good approximation

$$\varepsilon\_s = \upsilon\_s$$

where *v<sup>s</sup>* is the voltage across the secondary. Therefore, Eqs. (7.31) and (7.32) can be written as

$$\upsilon\_s = -N\_s \frac{d\phi}{dt} \tag{7.31\text{(a)}}$$

$$
\omega\_p = -N\_p \frac{d\phi}{dt} \tag{7.32\text{(a)}}
$$

From Eqs. [7.31 (a)] and [7.32 (a)], we have

$$\frac{\upsilon\_s}{\upsilon\_p} = \frac{N\_s}{N\_p} \tag{7.33}$$

Note that the above relation has been obtained using three assumptions: (i) the primary resistance and current are small; (ii) the same flux links both the primary and the secondary as very little flux escapes from the core, and (iii) the secondary current is small.

If the transformer is assumed to be 100% efficient (no energy losses), the power input is equal to the power output, and since *p* = *i v*,

$$\mathfrak{i}\_p \mathfrak{v}\_p = \mathfrak{i}\_s \mathfrak{v}\_s \tag{7.34}$$

Although some energy is always lost, this is a good approximation, since a well designed transformer may have an efficiency of more than 95%. Combining Eqs. (7.33) and (7.34), we have

*p s s s p p i v N i v N* = = (7.35)

Since *i* and *v* both oscillate with the same frequency as the ac source, Eq. (7.35) also gives the ratio of the amplitudes or rms values of corresponding quantities.

Now, we can see how a transformer affects the voltage and current. We have:

$$V\_s = \left(\frac{N\_s}{N\_p}\right) V\_p \quad \text{and} \quad I\_s = \left(\frac{N\_p}{N\_s}\right) I\_p \tag{7.36}$$

That is, if the secondary coil has a greater number of turns than the primary (*N<sup>s</sup>* > *N p* ), the voltage is stepped up (*V<sup>s</sup>* > *V p* ). This type of arrangement is called a *step-up transformer*. However, in this arrangement, there is less current in the secondary than in the primary (*N<sup>p</sup>* /*N<sup>s</sup>* < 1 and *I s* < *I p* ). For example, if the primary coil of a transformer has 100 turns and the secondary has 200 turns, *N<sup>s</sup>* /*N p* = 2 and *N p* /*N<sup>s</sup>* =1/2. Thus, a 220V input at 10A will step-up to 440 V output at 5.0 A.

If the secondary coil has less turns than the primary (*N<sup>s</sup>* < *N p* ), we have a *step-down transformer*. In this case, *V<sup>s</sup>* < *V p* and *I s* > *I p* . That is, the voltage is stepped down, or reduced, and the current is increased.

The equations obtained above apply to ideal transformers (without any energy losses). But in actual transformers, small energy losses do occur due to the following reasons:

(i) *Flux Leakage*: There is always some flux leakage; that is, not all of the flux due to primary passes through the secondary due to poor

![](_page_19_Picture_0.jpeg)

design of the core or the air gaps in the core. It can be reduced by winding the primary and secondary coils one over the other.

- (ii) *Resistance of the windings*: The wire used for the windings has some resistance and so, energy is lost due to heat produced in the wire (*I* <sup>2</sup>*R*). In high current, low voltage windings, these are minimised by using thick wire.
- (iii) *Eddy currents*: The alternating magnetic flux induces eddy currents in the iron core and causes heating. The effect is reduced by using a laminated core.
- (iv) *Hysteresis*: The magnetisation of the core is repeatedly reversed by the alternating magnetic field. The resulting expenditure of energy in the core appears as heat and is kept to a minimum by using a magnetic material which has a low hysteresis loss.

The large scale transmission and distribution of electrical energy over long distances is done with the use of transformers. The voltage output of the generator is stepped-up (so that current is reduced and consequently, the *I* <sup>2</sup>*R* loss is cut down). It is then transmitted over long distances to an area sub-station near the consumers. There the voltage is stepped down. It is further stepped down at distributing sub-stations and utility poles before a power supply of 240 V reaches our homes.

#### SUMMARY

1. An alternating voltage *v v t* = ω *<sup>m</sup>* sin applied to a resistor *R* drives a

current *i* = *i<sup>m</sup>* sinw*t* in the resistor, *m m v i R* = . The current is in phase with

- the applied voltage.
- 2. For an alternating current *i* = *i<sup>m</sup>* sin <sup>w</sup>*t* passing through a resistor *R*, the average power loss *P* (averaged over a cycle) due to joule heating is ( 1/2 )*i* 2 *<sup>m</sup>R*. To express it in the same form as the dc power (*P* = *I* <sup>2</sup>*R*), a special value of current is used. It is called *root mean square* (rms) *current* and is donoted by *I*:

$$I = \frac{\mathbf{i}\_m}{\sqrt{2}} = \mathbf{0}.7 \mathbf{0} \mathbf{7} \mathbf{0} \mathbf{7} \mathbf{i}\_m$$

Similarly, the *rms voltage* is defined by

$$V = \frac{\upsilon\_m}{\sqrt{2}} = \mathbf{0}.7\mathbf{0}7\,\upsilon\_m$$

We have *P = IV = I* 2*R*

3. An ac voltage *v* = *v<sup>m</sup>* sin w*t* applied to a pure inductor *L*, drives a current in the inductor *i = i<sup>m</sup>* sin (w*t* – p/2), where *i<sup>m</sup>* = *v<sup>m</sup>* /*X<sup>L</sup>* . *X<sup>L</sup>* = w*L* is called *inductive reactance*. The current in the inductor lags the voltage by p/2. The average power supplied to an inductor over one complete cycle is zero.

### Alternating Current

4. An ac voltage *v* = *v<sup>m</sup>* sinw*t* applied to a capacitor drives a current in the capacitor: *i = i<sup>m</sup>* sin (w*t* + p/2). Here,

$$\dot{\mathbf{u}}\_m = \frac{\boldsymbol{\upsilon}\_m}{\mathbf{X}\_{\mathbf{C}}}, \text{ } X\_{\mathbf{C}} = \frac{1}{o\mathbf{C}} \text{ is called capacitance reactance.}$$

The current through the capacitor is p/2 ahead of the applied voltage. As in the case of inductor, the average power supplied to a capacitor over one complete cycle is zero.

5. For a series *RLC* circuit driven by voltage *v = v<sup>m</sup>* sin <sup>w</sup>*t*, the current is given by *i = i<sup>m</sup>* sin (w*t* + f)

$$\text{where}\qquad \mathbf{i}\_m = \frac{\boldsymbol{\upsilon}\_m}{\sqrt{\mathbf{R}^2 + \left(\mathbf{X}\_C - \mathbf{X}\_L\right)^2}}$$

$$\text{and } \phi = \tan^{-1} \frac{X\_C - X\_L}{R}$$

( ) <sup>2</sup> <sup>2</sup> *Z R X X* = + − *C L* is called the *impedance* of the circuit.

The average power loss over a complete cycle is given by

*P* = *V I* cosf

The term cosf is called the *power factor*.

- 6. In a purely inductive or capacitive circuit, cosf = 0 and no power is dissipated even though a current is flowing in the circuit. In such cases, current is referred to as a *wattless current*.
- 7. The phase relationship between current and voltage in an ac circuit can be shown conveniently by representing voltage and current by rotating vectors called *phasors*. A phasor is a vector which rotates about the origin with angular speed <sup>w</sup>. The magnitude of a phasor represents the amplitude or peak value of the quantity (voltage or current) represented by the phasor.

The analysis of an ac circuit is facilitated by the use of a phasor diagram.

8. A transformer consists of an iron core on which are bound a primary coil of *N<sup>p</sup>* turns and a secondary coil of *N<sup>s</sup>* turns. If the primary coil is connected to an ac source, the primary and secondary voltages are related by

$$\mathbf{V}\_{\mathbf{s}} = \left(\frac{N\_{\mathbf{s}}}{N\_{\mathbf{p}}}\right)\_{\boldsymbol{\wedge}} \mathbf{V}\_{\mathbf{p}} \overset{\wedge}{\boldsymbol{\wedge}} \overset{\wedge}{\boldsymbol{\wedge}}$$

and the currents are related by

$$I\_{\rm s} = \left(\frac{N\_p}{N\_{\rm s}}\right) I\_p$$

If the secondary coil has a greater number of turns than the primary, the voltage is stepped-up (*V<sup>s</sup>* > *V<sup>p</sup>* ). This type of arrangement is called a *stepup transformer*. If the secondary coil has turns less than the primary, we have a *step-down transformer*.

![](_page_21_Picture_0.jpeg)

| Physical quantity                                  | Symbol        | Dimensions                                                                             | Unit | Remarks                                                                                                                                      |
|----------------------------------------------------|---------------|----------------------------------------------------------------------------------------|------|----------------------------------------------------------------------------------------------------------------------------------------------|
| rms voltage                                        | V             | [M L2 T<br>–3 A<br>–1]                                                                 | V    | vm<br>V<br>=<br>,<br>v m<br>is<br>the<br>2<br>amplitude of the ac voltage.                                                                   |
| rms current                                        | I             | [ A]                                                                                   | A    | im<br>I =<br>, im<br>is the amplitude of<br>2<br>the ac current.                                                                             |
| Reactance:<br>Inductive<br>Capacitive<br>Impedance | XL<br>XC<br>Z | 2 T<br>–3 A<br>–2]<br>[M L<br>2 T<br>–3 A<br>–2]<br>[M L<br>2 T<br>–3 A<br>–2]<br>[M L |      | XL<br>=  L<br>XC<br>= 1/ C<br>Depends<br>on<br>elements                                                                                    |
| Resonant<br>frequency                              | or w0<br>wr   | –1]<br>[T                                                                              | Hz   | present in the circuit.<br>1<br><br>for a<br>w0<br>LC                                                                                       |
| Quality factor                                     | Q             | Dimensionless                                                                          |      | series RLC circuit<br>L<br>1<br>ω<br>0<br>Q<br>=<br>=<br>for a series<br>R<br>C R<br>ω<br>0                                                  |
| Power factor                                       |               | Dimensionless                                                                          |      | RLC circuit.<br>=<br>cosf,<br>f<br>is<br>the<br>phase<br>difference<br>between<br>voltage<br>applied<br>and<br>current<br>in<br>the circuit. |

#### POINTS TO PONDER

1. When a value is given for ac voltage or current, it is ordinarily the rms value. The voltage across the terminals of an outlet in your room is normally 240 V. This refers to the *rms* value of the voltage. The amplitude of this voltage is

$$\upsilon\_m = \sqrt{2}V = \sqrt{2}(240) = 340\,\text{V}$$

- 2. The power rating of an element used in ac circuits refers to its average power rating.
- 3. The power consumed in an ac circuit is never negative.
- 4. Both alternating current and direct current are measured in amperes. But how is the ampere defined for an alternating current? It cannot be derived from the mutual attraction of two parallel wires carrying ac currents, as the dc ampere is derived. An ac current changes direction

with the source frequency and the attractive force would average to zero. Thus, the ac ampere must be defined in terms of some property that is independent of the direction of the current. Joule heating is such a property, and there is one ampere of *rms* value of alternating current in a circuit if the current produces the same average heating effect as one ampere of dc current would produce under the same conditions.

5. In an ac circuit, while adding voltages across different elements, one should take care of their phases properly. For example, if *V<sup>R</sup>* and *V<sup>C</sup>* are voltages across *R* and *C,* respectively in an *RC* circuit, then the

total voltage across *RC* combination is 2 2 *V V V RC R C* = + and not *VR + V<sup>C</sup>* since *V<sup>C</sup>* is p/2 out of phase of *V<sup>R</sup>* .

- 6. Though in a phasor diagram, voltage and current are represented by vectors, these quantities are not really vectors themselves. They are scalar quantities. It so happens that the amplitudes and phases of harmonically varying scalars combine mathematically in the same way as do the projections of rotating vectors of corresponding magnitudes and directions. The 'rotating vectors' that represent harmonically varying scalar quantities are introduced only to provide us with a simple way of adding these quantities using a rule that we already know as the law of vector addition.
- 7. There are no power losses associated with pure capacitances and pure inductances in an ac circuit. The only element that dissipates energy in an ac circuit is the resistive element.
- 8. In a *RLC* circuit, resonance phenomenon occur when *X<sup>L</sup> = X<sup>C</sup>* or

0 1 *LC* <sup>ω</sup> = . For resonance to occur, the presence of both *L* and *C*

elements in the circuit is a must. With only one of these (*L* or *C* ) elements, there is no possibility of voltage cancellation and hence, no resonance is possible.

- 9. The power factor in a *RLC* circuit is a measure of how close the circuit is to expending the maximum power.
- 10. In generators and motors, the roles of input and output are reversed. In a motor, electric energy is the input and mechanical energy is the output. In a generator, mechanical energy is the input and electric energy is the output. Both devices simply transform energy from one form to another.
- 11. A transformer (step-up) changes a low-voltage into a high-voltage. This does not violate the law of conservation of energy. The current is reduced by the same proportion.

# EXERCISES

- 7.1 A 100 W resistor is connected to a 220 V, 50 Hz ac supply.
	- (a) What is the rms value of current in the circuit?
	- (b) What is the net power consumed over a full cycle?
- 7.2 (a) The peak voltage of an ac supply is 300 V. What is the rms voltage?
	- (b) The rms value of current in an ac circuit is 10 A. What is the peak current?
- 7.3 A 44 mH inductor is connected to 220 V, 50 Hz ac supply. Determine the rms value of the current in the circuit.
- 7.4 A 60 mF capacitor is connected to a 110 V, 60 Hz ac supply. Determine the rms value of the current in the circuit.
- 7.5 In Exercises 7.3 and 7.4, what is the net power absorbed by each circuit over a complete cycle. Explain your answer.
- 7.6 A charged 30 mF capacitor is connected to a 27 mH inductor. What is the angular frequency of free oscillations of the circuit?
- 7.7 A series *LCR* circuit with *R* = 20 W, *L* = 1.5 H and *C* = 35 mF is connected to a variable-frequency 200 V ac supply. When the frequency of the supply equals the natural frequency of the circuit, what is the average power transferred to the circuit in one complete cycle?
- 7.8 Figure 7.17 shows a series *LCR* circuit connected to a variable frequency 230 V source. *L* = 5.0 H, *C* = 80mF, *R* = 40 W.

![](_page_23_Figure_13.jpeg)

- (a) Determine the source frequency which drives the circuit in resonance.
- (b) Obtain the impedance of the circuit and the amplitude of current at the resonating frequency.
- (c) Determine the rms potential drops across the three elements of the circuit. Show that the potential drop across the *LC* combination is zero at the resonating frequency.