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

(cubits_multiples)=

# Compuertas aplicadas a estados de múltiples cúbits

Dos o más cúbits pueden combinar sus estados por medio del producto tensorial de sus estados individuales. El producto tensorial de dos cúbits tiene la siguiente representación:

$
|a> \otimes |b> = |ab>
$

Para dos cubits, representados en la base estandar, es decir mediante su proyeccion en los vectores base $|0>$ y $|1>$ con amplitudes $v_{0}$ y $v_{1}$, respectivamente, su producto tensorial es el siguiente:

$
V_{00}|00> + V_{01}|01> + V_{10}|10> + V_{11}|11> = 
\begin{pmatrix}
V_{00} \\ V_{01} \\ V_{10}\\ V_{11} \end{pmatrix}
= |\Psi> 
$

De esta manera, el vector que resulta de aplicar el producto tensorial genera los estados base del sistema formado por los dos cubits, $|\Psi>$. Las compuertas de dos o mas cúbits son representadas por matrices cuadradas de tamaño $2^{n}\times2^{n}$ donde $n$ es el numero de cubits involucrados. Los operadores o transformaciones que se aplican a estados de multiples cubits, dentro del contexto de la computacion cuantica, son unitarios y reversibles, como en el caso de operadores y compuertas cuanticas aplicadas a un cubit. Por lo tanto, cuando una compuerta es aplicada a un estado de multiples cubits, $|\Psi_{1}>$, se produce un segundo estado $|\Psi_{2}>$:

$
U|\Psi_{1}> = |\Psi_{2}>
$

Algunas de las compuertas que vamos a explorar en esta seccion incluyen:

- La compuerta **CNOT**.
- La compuerta **$CU_{1}(\lambda)$**
- La compuerta **SWAP**
- La compuerta de **Toffoli**

Las propiedades de estas compuertas se describen en la siguiente tabla:

| Compuerta  | Matriz |  Efecto  | 
| ---------- | ------ |  ------- |
| *CX/CNOT*  | $\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$ | Aplica el efecto de la compuerta NOT al segundo cubit cuando el primero se encuentra en el estado |1> |
| C$U_{1}(\lambda)$ | $\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & e^{i\lambda} \end{pmatrix}$ | Aplica el efecto de la compuerta U1 al segundo cubit cuando el primero se encuentra en el estado |1> |
| Swap | $\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$ | Intercambia los estados cuanticos del primer y segundo cubit | 
| CCX/Toffoli | $\begin{pmatrix} 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\  0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\\end{pmatrix}$ | Aplica el efecto de la compuerta NOT al tercer cubit cuando el primero y el segundo se encuentran en el estado |1> | 

## Compuerta CNOT

La compuerta **CNOT** o **Control-NOT** es similar a la compuerta clasica **XOR**. Se compone de dos partes, la parte de *Control*, que decide si se aplica una operacion determinada en el cubit de tipo *Target*, en este caso, la compuerta *NOT*. En la seccion pasada comprobamos que la compuerta *NOT*, ejecuta una rotacion sobre el eje *x* por un valor de $\pi/2$. La compuerta *CNOT* se denomina a menudo **Control-X(CX)**. La representacion de matriz de la compuerta *CNOT* se puede encontrar en la tabla de arriba y podemos notar algunas caracteristicas importantes:

- Es una matrix de $4\times 4$, ya que es resultado del producto tensorial de dos cubits.
- La parte superior izquierda corresponde a la matriz de identidad y la parte inferior derecha corresponde a la matriz X de Pauli.

La siguiente tabla ilustra el resultado de aplicar la compuerta CNOT a diferentes combinaciones de estados |0> y |1> para un sistema de dos cubits:

| Input | Output |
|-------|--------|
||00>   |  |00>  |
||01>   |  |01>  |
||10>   |  |11>  |
||11>   |  |10>  |

Como podemos observar, cuando el cubit de control (el primero o de lado izquierdo) es 0, no hay cambio en el sistema, podemos decir que se aplica la matriz de identidad. En cambio, cuando el cubit target es 1, la operacion X es ejecutada en el cubit de tipo target.

## Compuerta de Toffoli

La compuerta de Toffoli adquiere su nombre por el profesor Tomasso Toffoli de la universidad de Boston. Esta compuerta es muy similar a las compuertas de control en dos cubits, con la diferencia de que esta compuerta tiene multiples cubits de control y un solo target. Para simplificar la descripcion de compuertas con multiples cubits de control, se sigue la siguiente convencion: se utiliza la expresion **CCX** para denominar a la compuerta que tiene dos cubits de control y **CCCX** a la compuerta que tiene tres cubits de control. 

La representacion general de la compuerta de Toffoli es una matrix 8X8 que es reultado del producto tensorial de los estados base de 3 cubits.

## Compuerta Swap

La compuerta Swap intercambia los estados de dos cubits. Su representacion de matriz se puede encontrar en la tabla de arriba.
