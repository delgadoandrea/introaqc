---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(compuertas_universales)=

# Compuertas Universales UX

Las compuertas de **tipo universal** o **UX** se refieren al tipo de compuertas *universales* que permiten rotaciones sobre el espacio de Hilbert. Dependiendo del número de parametros que una compuerta de tipo *UX* tome  de argumento, dicha compuerta puede suponer una rotacion sobre uno o mas ejes x,y, o z en la esfera de Bloch.

## Compuerta U3

La compuerta **U3** requiere tres parametros que permiten la rotacion sobre los ejes x,y y z. La representacion de la compuerta U3 se define mediante la matriz:
$
U_{3(\theta,\phi,\lambda)} = 
\begin{pmatrix}
cos\frac{\theta}{2} & -e^{i\lambda}sin\frac{\theta}{2} \\
e^{i\phi}sin\frac{\theta}{2} & e^{i\phi + \lambda}cos\frac{\theta}{2}
\end{pmatrix}
$

En esta matriz, $\theta$, $\phi$ y $\lambda$ representan los angulos de rotacion (en radianes) sobre el eje x, y y z, respectivamente. Para que el operador representado por la matriz U3 satisfaga las condiciones de unitariedad, dichos angulos deben estar confinados a los rangos $0 \leq \theta \leq \pi$, $0 \leq \phi \leq 2\pi$ y $0 \leq \lambda \leq 2\pi$. Las compuertas U2 y U1 representan subconjuntos de las compuertas U3. En realidasd, la compuerta U3 siempre es utilizada en el *backend* de Qiskit y cuando llamamos las compuertas U2 y U1, el parametro $\theta$ se fija en el valor $\pi/2$.


## Compuerta U2
La compuerta **U2** requiere dos parametros que corresponden a los parametros $\phi$ y $\lambda$ en la compuerta *U3*. La representacion de matrix de la compuerta U2 es la siguiente:

$
U_{2(\phi,\lambda)} = \frac{1}{\sqrt{2}}
\begin{pmatrix}
1 & e^{-i\lambda} \\
e^{i\phi} & e^{i(\phi + \lambda)}
\end{pmatrix}
$

## Compuerta U1
La compuerta **U1** unicamente requiere un parametro y es aplicado mediante una rotacion sobre el eje z. Por lo tanto, la compuerta U1 tiene una representacion equivalente a la compuerta $R_{z}$:

$
U_{1(\lambda)} = 
\begin{pmatrix}
1 & 0 \\
0 & e^{\lambda}
\end{pmatrix}
$
%$
%U_{1(\lambda)} = 
%\begin{\pmatrix}
%1 & 0 \\
%0 & e^{\lambda}
%\end{pmatrix}
%$

El angulo $\lambda$ aqui, corresponde a el angulo de rotacion en radianes sobre el eje z, y por lo tanto ejecuta una **rotacion de fase**.