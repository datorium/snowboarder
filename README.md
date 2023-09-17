# Simulation of a Snowboarder Sliding on a Sloped Half-Pipe

## Abstract

This paper provides a detailed mathematical model and simulation of a snowboarder sliding along a sloped half-pipe. Through the framework of classical physics, the snowboarder's trajectory, influenced by Earth's gravitational force and the half-pipe's shape, is meticulously modeled and depicted.

## 1. Introduction

The exploration of motion under the influence of gravitational forces has been central in physics. This paper presents the intriguing case of a snowboarder descending along a parabolic half-pipe, which is set at an incline relative to the ground.

## 2. Assumptions and Parameters

**Assumptions:**  
- The half-pipe's cross-section is parabolic.
- There is no air resistance.
- The snowboarder experiences no friction while sliding along the half-pipe.
- Earth's gravitational force impacts the snowboarder.
- The half-pipe is tilted at an angle relative to the ground, prompting the snowboarder to slide downwards along its length.

**Parameters:**  
- Snowboarder's weight: 50kg.
- Length of the half-pipe: $L = 180$ meters.
- Height of the half-pipe: $H = 7$ meters.
- Width (lip to lip) of the half-pipe: $W = 20$ meters.
- Slope of the half-pipe: 18 degrees.
- Gravitational acceleration: $g = 9.81$ m/s^2.

## 3. Mathematical Model

**Two-dimensional Force Model:**  
This model considers forces acting on an object in two distinct dimensions. For our simulation:
- The Y-direction (vertical) factors in the forces due to the parabolic shape.
- The X-direction (along the slope) accounts for the gravitational component pulling the snowboarder down the incline.

**Parabolic Cross-section:**  
The half-pipe's cross-section is modeled by a parabola described by:

$$Z=aY^2$$

Where:

$$a=\frac{H}{(W/2)^2}$$

is a constant.

**Slope Adjustment:**  
The half-pipe's slope leads to:

$$Z_{adjusted} = Z - X \tan(18^\circ) + \text{elevation adjustment}$$

**Forces on the Snowboarder:**  
The snowboarder is subjected to two forces:
1. Gravitational force due to the parabolic shape.
2. Gravitational force causing the descent along the slope.

**Energy Calculations:**  
- Kinetic Energy (K.E): $\frac{1}{2} m v^2$
- Potential Energy (P.E): $mgh$

Energy conservation is described by:

$$K.E_{initial} + P.E_{initial} = K.E_{final} + P.E_{final}$$

## 4. Analytical Derivation

To derive an analytical solution for the snowboarder's path:

1. **Half-Pipe Equation**: It's represented as $Z = aY^2 - X \tan(\theta)$, with $\theta$ as the slope angle.

2. **Forces**: The snowboarder faces gravitational force ($F_g = mg$) and a varying normal force due to the parabolic pipe shape.

3. **Equations of Motion**: Using Newton's second law, we get differential equations describing the snowboarder's motion.

### Challenges:

- The system yields **non-linear differential equations**, tough to solve analytically.
- Multiple variables lead to **coupled differential equations**, adding complexity.
- The parabolic shape creates **path dependency**, making the motion hard to express simply.

Given these challenges, numerical methods, which approximate solutions, are preferred for practicality and efficiency.


## 5. Simulation

**Initial Conditions:**  
- The snowboarder commences from the top of the left lip with velocities $v_x = 0$ and $v_y = 0$.

**Forces and Acceleration:**  
- $F_{gravity_y} = -2 \times a \times y_{dot} \times g$
- $F_{slope_x} = g \times \sin(18^\circ)$
- $a_y = F_{gravity_y}$
- $a_x = F_{slope_x}$

Using incremental time steps ($dt = 0.01s$), the snowboarder's velocities and positions are continually updated until reaching the half-pipe's end.

## 6. Visualization

A 3D graphical representation was employed to illustrate:
1. The sloped half-pipe.
2. The snowboarder's trajectory along the half-pipe.
3. The snowboarder's path projection on the ground, visualized as a blue dashed line on the ground plane.

![image](https://github.com/datorium/snowboarder/assets/45357320/d1eeecb1-6329-4871-912f-914f093c6707)
![image](https://github.com/datorium/snowboarder/assets/45357320/fb914e16-acf8-41e7-bece-8f39214e8c74)


## 7. Conclusion

Through this exploration, the dynamic motion of a snowboarder sliding down a sloped half-pipe is captured, offering insights into the intricate interplay of gravitational forces, geometry, and movement.
