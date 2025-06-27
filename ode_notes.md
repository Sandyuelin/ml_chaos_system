# First-Order Differential Equations

## Terminology
- __DE__ involves unknown y(t) and its derivatives; y is dependent variable and t is independent variable
- __Order__ of a differential equation = highest order derivative in the equation

- All solutions for DE is __general solution__ which is the collection of all its solutions. 
For instance, the equation

$$ y'' + y = 0 $$
has general solution:
 $$ y(t) = c_1cos(t) +c_2sin(t)\; c_1,c_2\subseteq R$$

Initial condition: general solution -> special solution:
$y(t_0) = y_0$

__IVP__ (initial value problem)  
$$IVP = 1st\ order\ ODE  + initial\ condition$$

## Numerical approximation

- Euler's method  
  $$ y(x_0 +h) \approx y(x_0)+ hy'(x_0)$$

## Solution of the first-order differential equation
$$main \ solveable\ first\ order\ DEs \  \begin{cases}
\text {separable equation}\\
\text {linear equation}
\end{cases}$$
### Solution for __separable equation__
 $$ y' = \frac{dy}{dt} = p(y)g(t) $$
 This gives the euqation:
 $$ \frac{dy}{p(y)} = g(t)dt$$
 Integtate both the last equation
 $$\int \frac{dy}{p(y)} =\int g(t)dt +c $$
 which c is a constant real number called integration constant. In particular, if $H(y)$ is anti-derivative of $\frac{1}{p(y)}$ and $G(t)$ is anti-derivative of $g(t)dt$ we write:
 $$H(y) = G(t) + c$$
 The convenient version is implicit equation and the integration one is explicit one

 - Revisiting the __Malthusian growth model__ $y' = ky$
     $$y' = yg(x)$$
    general solution
     $$y = Ae^{\int g(x)}$$
    for the Malthusian growth model, the general answer will be $y(x) = Ae^{kx}$ where $A = \pm e^{c}$ __together with $y = 0$__
  - Practice 
  
    (a) solve the IVP $\frac{dy}{dx} =xy^3$ 
    
     (i) y(0)=-1 (ii) y(0) = 0
  
      $for\ (i), \ y = -\sqrt{\frac{1}{1-x^2}};\ for\ (ii), \ y = 0$

  
### Solution for __linear equation__
- __integrating factor__
  
  The integrating factor $u = e^{\int P(x)dx}$ that satisfies $u' = uP(x)$ since $A=1$; 
    step-by-step:
   -  calculate $u$
   - multiply $u$ to the equation
   - calculate $y$ by the integration
     - practice: $\frac{1}{x}\frac{dy}{dx} -\frac{2y}{x^2} =xcosx, \ x>0$ there is a smarter solution by multiplying $\frac{1}{x}$ to both sides 
- __variations of parameter__
  
  steps:
    - $y' + P(x) =0$ -> $y(x)= Ae^{-\int P(x)dx}$
    - constant $A$ -> function, help cancel out some computation (?)
    - $y'+ P(x) =Q(x)$ 
    - $A'(x)e^{-\int{P(x)dx}} = Q(x)$
    - Integrate $A'(x)$ -> $A(x) = ..+ C$
    - Substitute $A$ into $y(x)$
  
### Change of variables
- __logistic equation__ (?) check slides
  $$\frac{dy}{dx} = kx(1-x)$$
  - new dependent variable: $x = \frac{P}{M}$
  - new independent vairable: $\tau = kt \ and \ y(\tau) = x(t)$ 
    $$\frac{dy(\tau)}{d\tau}$$ 
- __bernoulli equation__ :
  $$y' + P(x)y = Q(x)y^\alpha$$
  new dependent variable $u= y^s$
  $$u' = sy'y^{s-1}=s(Q(x)y^\alpha -P(x)y)y^{s-1}=sQ(x)y^{s-1+\alpha} -sP(x)y^{s} = -sP(x)u +sQ(x)y^{s-1+\alpha}$$
  By taking $1-s+\alpha = 0$, we can get $s = 1- \alpha$ and obtain
  $$u' + P(x)u = Q(x)$$ 

### Existence and Uniqueness of solutions
$y' + P(x)y = Q(x)y$ and $P, Q$ are continuous in $I\subseteq R$ with initial values, solutions for y(x) exists for all $x \subseteq I$ 

Theorem:
$y' = f(x,y)$,
$f$ and $\frac{\partial f}{\partial y}$ are continuous on $Range * Range$

Notice that we take the derivative of y instead of x:
**$$\frac{\partial f}{\partial y}(y,x)$$**
### First-order differential equations
- $$\frac{dx}{dt} =f(x)$$ 
(1)right heand side does not explicitly depend on t is called __autonomous__ *since it does not depend on time, so below works only for autonomous euqations*

(2)We assume f satisfies the conditions of existence and uniqueness theorem that is $f$ and $\frac{\partial f}{\partial x}$ are continuous

After using separation of variables and anti-derivative, we obtain that 
$$\phi(t,x) = G^{-1}(G(x) +t)$$
$$x(t) = \phi(t-t_0,x_0)$$

- A different approach $h(t; t_0,x_0)=x(t)$
  $$\frac{\partial h}{\partial t}(t; t_0,x_0) = f(h(t; t_0,x_0))$$
  - $h(t+s; t_0+s, x_0)= h(t; t_0,x_0)$

### One-dimensional dynamical systems
A smooth dynamical system is a continuously differentiable function $\phi: \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ satisfying:

- **Initial condition**: $\phi^0(x_0) = x_0$  
- **Flow property**: $\phi^{s+t}(x_0) = \phi^t(\phi^s(x_0))= \phi^s(\phi^t(x_0))$ for all $s, t \in \mathbb{R}$  

Using notation $\phi^t(x_0) = \phi(t, x_0)$, the properties become:  

- $\phi^0 = \text{id}$ here id means $\text{id}=x$  
- $\phi^{s+t} = \phi^s \circ \phi^t =  \phi^t \circ \phi^s$  

Each $\phi^t$ is invertible with:  

$$(\phi^t)^{-1} = \phi^{-t}, \quad \text{since} \quad \phi^t \circ \phi^{-t} = \phi^{-t} \circ \phi^t = \phi^0 = \text{id}$$  

Note that $(\phi^t)^{-1} \neq \frac{1}{\phi^t}$. Here, $(\phi^t)^{-1}$ refers to the inverse function of $\phi^t$, not the reciprocal. In general, functional inverses satisfy $\phi^t \circ \phi^{-t} = \text{id}$, which means applying $\phi^t$ followed by $\phi^{-t}$ returns the original input. This is different from scalar multiplication, where reciprocals are defined for numbers rather than functions.

### From differential euqations to dynamic systems

- Def: the autonomous euqation is __complete__ if its solutions are defined for all $t \subseteq \mathbb{R}$
- flow: $\phi = (t, x_0)$
- orbit: set $\mathcal O(x_0) = \phi(t,x_0): t\subset \mathbb{R}$
   - two orbits are either identical or disjoint. If $x_2 \subseteq \mathcal O(x_1),\ x_1 \subseteq \mathcal O(x_2)$, $\mathcal O(x_1) = \mathcal O(x_2)$
  
__lemma__: from flow to function, given a smooth dynamical system $\phi$ define
$$f(x) = \frac{\partial \phi}{\partial t}(0,x)$$

### Phase line
- __Equilibria__: $x_e$ is called equilibrium of $x' = f(x)$ if $f(x_e) = 0$
- **stable and unstable**
  
### Stability and Linearization
- Linearization: 
  -  $y = x- x_e$ $y' = x' = f'(x_e+y) \approx f'(x_e)y$
  - the dynamics near the equilibrium $x_e$ is determined by the first term of $f$ at $x_e$ in Taylor expansion
  - solutions:
    $\lambda = f'(x_e)$ Then the linearized equation is $y' = \lambda y$ with solution $y = y_0e^{\lambda t}$ . 
  - eg: $x' = x -x^3$ and $x_e = 1$ The euqilibrium is 0, -1, +1, $f'(x) = 1-3x^2$ $f'(x_e) =-2$ the equilibrium is stable, with solution of $y_0e^{-2t}$
  - eg: $x' = 1 -cosx = f(x)$ $f'(x) = sinx$ and $f'(0) = 0$ and we go back to the phase lines, the equilibrium is unstable 
    - Consider Taylor expansion, $f(x) = 1 - (1 - \frac{x^2}{2}+ \frac{x^4}{4!}- ... ) \approx \frac{x^2}{2}$  Then use f'(x) works as well
- Use phase portrait to find the equation 
 - Find equation with the stated properties (assume f(x) is smooth)
    - every real number is an equilibrium: x' = 0
    - every integer is an equilibrium and there are no others: $f(x) = sin\pi x$
    - there are three equilibria and all of them are stable: dne, f(x) from postive to negative and the corresponding equilibrium will be stable, however, there will be points from negative to postive that eqilibrium in opposite, will be unstable
    - There are no equilibria: $f(x) = x^2 +1$ or $f(x) =1$
    - There are precisely 10 equilibria: $f(x) = \prod^{10}_{k = 1} (x-k)$
### Bifurcation
- fold bifurcation(one parameter)
   - $f = 0\ f_x= 0\ f_{xx} \neq 0\ f_a \neq 0$
   
- culp bifurcation (two parameters)
    - $f = 0\ f_x= 0\ f_{xx} \neq 0\ f_a \neq 0$
- bifurcatio diagram: a graph showing the relationship between parameters and x when conditions satisfied ($f=0,f_x=0..$)

### Discrete-time dynamical systems
- discrete time dynamics: $x_k = p(x_{k-1})=p^k(x_0)$ and p here is a function but not a constant
$x_k = p^{-1}(x_{k+1})$
- **fixed points** : similar to equilibria we find for contituous differential euqations, in discrete time dynamics, we find $p(x_0) = x_0$
- **periodic points**: $p^k(x_0)=x_0$
   - fixed points are period 1 points

- stability:
     - eg: map p(x) = x + 3/4 sinx what is the linearized equation of the pixed point x = 0? Is it stable or not? 
        anwer: $p(x) = x + 3/4sinx = x$

        $\lambda = p'(x) = 1 + 3/4cosx  > 1$, so it is unstable

### Periodic forcing and Poincare maps

 time-periodic non-autonomous systems： $x' = f(t,x)$, $\phi(t;t_0,x_0)$ which solves the initial value problem with $x(t_0)=x_0$

 moreover, we assume the dependece of f on t is periodic such that $f(t+T,x)=f(t,x)$. Poincare map P: R->R is defined by 
 $$P^k(x_0)=\phi(kT; o,x_0)$$ 



### Linear second-order differential equations

#### basic info
- def: it is linear if it has the form 
$$a_2(x)y'' + a_1(x)y' + a_0(x)y = f(x)$$

homogeneous: f(x)=0; non-homogeneous otherwise

two function y(x) solve the equation are linearly independent 
  - $\frac{y_1(x)}{y_2(x)}$ is not constant
  - $c_1y_1(x)+c_2y_2(x) = 0$ only if $c_1=c_2=0$


**Existence and uniqueness**: unique solution y(x) satisfying the initial conditons $y(x_0) = \alpha _0 \ y'(x_0) = \alpha _1$

Superposition principle: combination of solution is also a solution

- proposition: two solutions of the homogeneous euqation $y'' +p(x)y'+q(x)y=0$ and their wronskian determinant $W(x) = y_1(x)y'_2(x)-y_1'(x)y_2(x)$ satisfies the differential equation $W' = -p(x)W$

- complex conjugate roots: $\alpha \ i\beta$

- general solutions
  - methods:
     - solve corresponding homogeneous equation to obtain two independent solutions
     - combine two solutions and add $y_p(x)$ for any solution of the non-homogeneous equation
  - situations:
     - polynomial: $Ax^k+Bx^{k-1}+...Constant$
     - exponential: $c_1e^kx$ degree same as $y_p$
     - tri,exp,poly: $e^{\alpha x}((Ax+B)sin\beta x+(Cx+D)cos \beta x)$ if alpha and beta imaginary coincides with the roots in the homogeneuous, then multiply $x$ to the previous equation

#### Higher-order linear equations with constant coefficients
-homogeneous: 
   - obtain the corresponding auxiliary equation by lettying $y=e^{rx}$
   - roots will determine the form of general solution. 
   - **rule**:
       -  r(once) = $e^{rx}$ 
       - r(multiplicity) = $x^ke^{rx}$
       - $\alpha +-\beta i = e^{\alpha x}cos\beta x/e^{\alpha x}sin\beta x$ 
- boundary value problems
  - $- y'' = Ey$ $0 \leq x \leq 1$ this is 


  ### Planar Systems
  #### Planer linear systems
  $$\mathbf x' = A\mathbf x$$
  Step 1: calculate the eigenvalues and corresponding eigenvectors
   $$det (A-rI) = 0 $$
   $$r_1, r_2 \ (A-r_1I) \vec v= 0$$
  Step2: substitute them into the general solution form 
   - two real distinct eigenvalues:
  $$\vec x(t) = c_1 e^{r_1}\vec u_1 + c_2e^{r_2} \vec u_2$$ 
  - complex: $r = \alpha +- i\beta$ with corresponding eigenvectors $ \vec u = \vec a + i$ $\vec v = \vec a - i\vec b$
  $$\vec x_1(t)= Re(e^{rt}\vec u) \ \vec x_{2} = Im(e^{rt}\vec u)$$
  - double real eigenvalue
     - if A is a diagonal matrix, then the general solution is $e^{rt}\vec c \ \ \vec c = <c_1, c_2>$ 
     - otherwise.

- draw:
   - real distinct eigenvalues: for positive eigenvalues, the corresponding eigenvectors $+-\vec u$ should direct outward; negative then inward
      - two positive: unstable
      - two negative: stable
      - one positive one negative: saddle
  - complex conjugate eigenvalues
     - positive real part: unstable spiral (outward)
     - negative real part: stable spiral (inward direction)
- trace-determinant plane:
   - tr = diagonal number addition
   - det: A-rI

#### Classification of Linear Systems (Trace-Determinant Plane)

| **Region**               | **Condition**               | **Behavior**                                                                 |
|--------------------------|-----------------------------|------------------------------------------------------------------------------|
| **Saddle**              | $$ D < 0 $$                | Unstable trajectories; hyperbolic curves.                                   |
| **Node**                | $$ D > 0, \, T^2 > 4D $$   | - **Stable Node** if $$ T < 0 $$ (trajectories converge to origin). <br> - **Unstable Node** if $$ T > 0 $$ (trajectories diverge). |
| **Spiral**              | $$ D > 0, \, T^2 < 4D $$   | - **Stable Spiral** if $$ T < 0 $$ (inward spirals). <br> - **Unstable Spiral** if $$ T > 0 $$ (outward spirals). |
| **Center**              | $$ T = 0, \, D > 0 $$      | Neutral stability; closed orbits (ellipses or circles).                     |

---


1. **Parabola Boundary**: The curve $$ D = \frac{T^2}{4} $$ separates nodes (real eigenvalues) from spirals (complex eigenvalues).
2. **Stability**:
   - **Stable**: $$ T < 0 $$ (trajectories move toward origin).
   - **Unstable**: $$ T > 0 $$ (trajectories move away from origin).
3. **Saddle**: Exists only when $$ D < 0 $$ (eigenvalues have opposite signs).

### General Theory of Linear Dynamical Systems

#### Linear Systems
 $$\mathbf x' = A\mathbf x + f(x)$$
 - **Existence and Uniqueness Theorem**:  if $A(t)$ and $f(t)$ are continuous on and open interval, and $t_0$ in the interval then for any initial vector $x_0$ the initial value problem has a unique 
 solution 
 - The unique solution to homogeneous initial value problem with $x(t_0)= 0$ with $A$ continuous is $x(t) = \vec 0$
 - **superposition principle**: any linear combination of solutions of  $\mathbf x' = A\mathbf x$ is also a solution

 #### Properties of homogenuous equation

 - **genneral solution** is the linear combination of linearly independent solutions, A is continuous. If x(t) is any solution of the equation the nthere are unique constants such that x(t) = linear combinations
 - **linear independence** all constants are zeros when the linear combination = 0
 
 - fundamental solution and matrix

     -fundamental solution: those independent solutions

     -fundamental matrix(solution corresponding matrix): invertible since 
$x(t) = X(t)\vec c \ \vec c = <c_1,c_2...>$ thus, $\vec c = X^{-1}(t_0)\vec x_0$ and substitue it to $x(t) = X(t)X^{-1}(t_0)\vec x_0$
    - differentiation rules for matrix-valued functions
       - If $X(t)$ and $Y(t)$ are differentiable at $t$, then so is their product: $\frac{d}{dt}[X(t)Y(t)] = X'(t)Y(t) + X(t)Y'(t)$
       
       - If $X(t)$ is invertible and differentiable at $t$, then so is $X^{-1}(t)$, and: $\frac{d}{dt}[X^{-1}(t)] = -X^{-1}(t)X'(t)X^{-1}(t)$

       - If $X(t)$ is differentiable, then $\det X(t)$ is also differentiable. If $X(t)$ is invertible:$
\frac{d}{dt}[\det X(t)] = \text{tr}(X'(t)X^{-1}(t)) \cdot \det X(t)
$
  
  - If X(t) and Y(t) are two fundamental matrices for the system x′
=
A(t)x, then there exists a constant invertible matrix C such that Y(t) = X(t)C.
  - Abel's formula: W(t) = detX(t) then W'(t) = tr(A)W(t)

#### Matrix exponential
- def: constant matrix A and fundamental matrix E(t) of x' = Ax satisfying E(0) = I, that is E(t) is the unique matrix satisfying the initial value problem E' = AE, E(0)=I. Then the exponential of matrix At is 
$$e^{At}= E(t)$$
- series expression for the matrix exponential:
     - $e^{At} = \sum_{k=0}^{\infin} \frac {1}{k!}a^k$
- $AB=BA\ e^{A+B}=e^Ae^B$
    - proof: $H(t) = e^{At}\ H'(t) = AH(t)$ $F(t) = e^{Bt}$
    $G(t) = e^{(A+B)t}$ calculate the derivative 


### Nonlinear Planer Systems
general form: $x' = f(x,y)$
$y' = g(x,y)$
#### Lotka-Volterra system
two interacting populations x, y:

$x' = Ax-Bxy$ $y' = -Cy+Bxy$
#### Simple pendulum

$x'=y\ y'= $
#### Van der Pol oscillator
#### Duffing oscillator

### Reduction to one dimension
Assume that a solution curve (x(t),y(t)) is a graph over x. y = h(x)
$$y'(x) = \frac{dy}{dx} = \frac{Y(x,y)}{X(x,y)}$$

### Equilibria and stability

#### Hartma-Grobman theorem
cannot be applied when it is non-hyperbolic, and it is a center

### Energy method and Lyapunov's stability theorem
energy method:$x' = y \ y' = f(x)$ which equals to $x'' = f(x)$

- potential and energy conservation 
      $E(x,y)= \frac{1}{2}y^2 +U(x)\ U'(x)= -f(x)$
       It is a conserved quantity becasue the derivative of $E(x,y)=0$

- level sets: $E(x,y)= h$ and solving the equation $h= \frac{1}{2}y^2+U(x)$
    - this makes sense only when $h-U(x)\geq 0$

     - the picture missing the direction for $x' = y \ y \gt 0 \ x'\gt 0$, then x moves from left to right
     - level sets should be smooth and it is vertical/infinite slope at the intersection on x axis
    - U(x) is tangent to h level sets thus
    - **phase portrait without arrows is incorrect**
- stability:
- linearizaton: $U''(x_e) \gt 0$ then potential has a minimum at $x_e$ the eigenvalues are $+- \sqrt {U''(x_e)}$ and therefore the equilibrium fro the linear system is center thus Hartma-Grobman theorem does not apply here.
$$E(x,y) \approx U(x_e) + \frac{1}{2} y^2+\frac{1}{2}U''(x_e)(x-x_e)^2$$
- $x'' = f(x)-by\ b\gt 0$ the derivative of $E(x,y)$ is $=by^2 \leq 0$


Lyapunov's method:
linear regression does not work, then we can use Lyapunov's theorem
- positive/negative (semi-)definite
   - def: $D$ is open disk 
- Lyapunov's stability theorem:
     Let the function $V(x)$ be positive definite  
on an open set $D$ which contains 0, and assume that 0 is an isolated equilibrium of the planar system  
$$
x' = f(x).
$$

**(i)** If the function $\dot{V}(x)$ is negative semidefinite on $D$, then 0 is **stable**.

**(ii)** If the function $\dot{V}(x)$ is negative definite on $D$, then 0 is **asymptotically stable**.
 
- V is positive definite V and prove V point is positive negative or negative definite

### Periodic solutions
$$rr'=xx'+yy'$$

$$r^2\theta = xy'-yx'$$

periodic solutions enclose equilibria:

- suppose that $L$ is non-trivial periodic solutions of a planar system
   - (a)L encloses at lease one equilibrium of the system

  - (b)if L encloses exactly one equilibrium, then it cannot be a saddle

Bendixson's negative criterion:
- a planar system defined in a simply connected domain and assume that $f_1\ f_2$ have continuous partial derivatives in $D$,$div f = \partial f_1/\partial x_1 + \partial f_2+\partial x_2$ does ot change sign in $D$ then the systems does not have any non-constant periodic orbits in $D$

- Proof: Green theorem

A way to understand the Bensixson theorem: why we need the change in sign of the divergence

- In vector field: negative divergence, area will shrink; positive divergence, area will expand.closed curve, then area must remain the same, 

Poincare-Bendixson theorem:
  - planar system in a closed bounded rigion, $f_1\ f_2$ have continuous partial derivatives in the region, systems has no equilibria. Then any solutions is either periodic or approaching to limit cycles

#### Stability of Periodic solutions

#### Hopf bifurcation
- supercritical
- subcritical

steps: calculate the $D\vec f$ and see tr and d

$x_0' = f(x_0)$ then $x_0$ is stable if $|f'(x_0)| < 1$ 

if eigenvalues change from negative to positive;
if limit cycle stable or unstable

#### Poincare for non-autonomous differential equations
- forced duffing equation

- chaos: is associated with sensitive dependence on initial conditions. then we denote $d_k$ the distance between two trajectories at time k