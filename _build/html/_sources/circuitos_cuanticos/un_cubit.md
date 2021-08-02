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

(un_cubit)=

# Compuertas cuanticas aplicadas en un cubit
El caso mas sencillo es el de las compuertas cuanticas que operan en un solo cubit. Para empezar, vamos a repasar la representacion de un cubit como estado cuantico.

El estado de un cubit se puede representar de la siguiente forma:

$
    |\Psi> = \alpha|0> + \beta|1>
$

En la ecuacion anterior, $\alpha$ y $\beta$ representan numeros complejos que indican las amplitudes de probabilidad para los estados base $|0>$ y $|1>$. La suma de estas probabilidades de amplitud debe ser igual a 1 y por lo tanto, tenemos la condicion: $|\alpha|^{2} + |\beta|^{2} = 1$. Un cubit en el estado $\alpha|0> + \beta|1>$ puede ser visualizado como un punto $(\theta, \phi)$ en la esfera de Bloch, donde $\alpha = cos(\theta/2)$ y $\beta = e^{i\phi}sin(\theta/2)$. Finalmente, las bases ortogonales $|0>$ y $|1>$ pueden ser representadas como vectores de columna:

$
    |0> = \begin{pmatrix} 1 \\ 0 \end{pmatrix},
    |1> = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$

Los operadores que actuan en un cubit deben preservar la norma de los vectores base, y por lo tanto, las compuertas cuanticas que operan en un cubit son matrices unitarias de estructura 2X2. Dentro de esta categoria, las matrices de Pauli son de los operadores mas relevantes para la computacion cuantica.

$
    X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}; Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}; Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$

Otras compuertas cuanticas para un solo cubit incluyen la compuerta de Hadamard (H), la compuerta de fase (S), y la compuerta $\pi/8$ (T):

$
    H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}; S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}; T = \begin{pmatrix} 1 & 0 \\ 0 & exp(i\pi/4) \end{pmatrix}
$

**Ejercicio:** Comprobar que $H=(X+Z)/\sqrt{2}$ y $S=T^{2}$

## Las compuertas de Pauli como operadores de rotacion

Las matrices de Pauli son la base de 3 matrices unitarias muy importantes, los operadores de rotacion. Los operadores de rotacion sobre los ejes $\hat{x}, \hat{y},$ y $\hat{z}$ son generados al exponenciar las matrices de Pauli:

$
	R_{x}(\theta) = e^{-i\theta X/2} = cos\frac{\theta}{2}I - i sin\frac{\theta}{2}X = \begin{pmatrix} cos\frac{\theta}{2} & -isin\frac{\theta}{2} \\ -isin\frac{\theta}{2} & cos\frac{\theta}{2} \end{pmatrix}\\
$
$
	R_{y}(\theta) = e^{-i\theta Y/2} = cos\frac{\theta}{2}I - i sin\frac{\theta}{2}Y = \begin{pmatrix} cos\frac{\theta}{2} & -sin\frac{\theta}{2} \\ sin\frac{\theta}{2} & cos\frac{\theta}{2} \end{pmatrix}\\
$
$
	R_{z}(\theta) = e^{-i\theta Z/2} = cos\frac{\theta}{2}I - i sin\frac{\theta}{2}Z = \begin{pmatrix} e^{-i\frac{\theta}{2}} & 0 \\ 0 & e^{i\frac{\theta}{2}} \end{pmatrix}\\
$

Por ejemplo, consideremos un estado arbitrario de 1-cubit descrito en terminos de sus angulos del vector de Bloch $\sigma$ y $\tau$:

$
    cos\frac{\sigma}{2}|0> + e^{i\tau}sin\frac{\sigma}{2}|1>
$

cuya representacion en vector de columna corresponde a:

$
    \begin{pmatrix}
    cos\frac{\sigma}{2} \\ e^{i\tau}sin\frac{\sigma}{2}
    \end{pmatrix}
$

El efecto de aplicar $R_{z}(\theta)$ a este estado sera:

$
	 \begin{pmatrix} e^{-i\frac{\theta}{2}} & 0 \\ 0 & e^{-i\frac{\theta}{2}} \end{pmatrix} \begin{pmatrix}
    cos\frac{\sigma}{2} \\ e^{i\tau}sin\frac{\sigma}{2}
    \end{pmatrix} 
$
$
    =  \begin{pmatrix}
    e^{-i\frac{\theta}{2}}cos\frac{\sigma}{2} \\ e^{-i\frac{\theta}{2}}e^{i\tau}sin\frac{\sigma}{2} \end{pmatrix}\\
$
$   
    = e^{-i\frac{\theta}{2}}\begin{pmatrix}
    cos\frac{\sigma}{2} \\ e^{i\theta}e^{i\tau}sin\frac{\sigma}{2} \\
    \end{pmatrix}\\
$
$
    = e^{-i\frac{\theta}{2}}(cos\frac{\theta}{2}|0> + e^{i(\tau + \theta})sin\frac{\theta}{2}|1>)
$

Eliminando la fase global, el estado resultante de aplicar $R_{z}(\theta)$ es:

$
    cos\frac{\theta}{2}|0> + e^{i(\tau + \theta})sin\frac{\theta}{2}|1>
$

y por lo tanto, podemos concluir que la compuerta $R_{z}(\theta)$ ha cambiado el angulo $\tau$ a $\tau + \theta$, lo que representa una rotacion de $\theta$ alrededor del eje $z$ de la esfera de Bloch.

**Nota:** La compuerta $R_{Z}$ se puede re-escribir de la siguiente manera:

$
    R_{z}(\theta) = \begin{pmatrix} e^{-i\frac{\theta}{2}} & 0 \\ 0 & e^{i\frac{\theta}{2}} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{pmatrix}
$

y de esta manera, recuperamos las compuertas de Pauli cuando $\theta = \pi$, es decir, $R_{X}(\pi) = X, R_{Y}(\pi) = Y, R_{Z}(\pi) = Z$. Ademas, las compuertas de rotacion generadas por las matrices de Pauli, y mas especificamente, su producto, nos permiten representar otras compuertas de un cubit, como la compuerta de Hadamard, por ejemplo.

**Ejercicio**
La compuerta de Hadamard se puede representar como el producto de las rotaciones $R_{x}$ y $R_{z}$, si $\theta = \frac{\pi}{2}$ y un factor de fase igual a $e^{-i\pi/2}$.

Si definimos un vector unitario $\hat{n}=(n_{x}, n_{y}, n_{z})$ en tres dimensiones, podemos generalizar las definiciones previas de compuertas de rotacion generadas por las compuertas de Pauli definiendo una rotacion de $\theta$ sobre dicho eje $\hat{n}$ mediante la siguiente expresion:

$
R_{\hat{n}}(\theta) = e^{-i\frac{\theta\hat{n}\cdot\sigma}{2}} = cos\frac{\theta}{2}I - i sin\frac{\theta}{2}(n_{x}X + n_{y}Y + n_{z}Z)
$

**Ejercicio**
Al principio de la seccion, hablabamos de la importancia de reducir el numero de compuertas que utilizamos en durante el proceso de desarrollo de algoritmos, y por lo tanto, podemos hacer uso de algunas identidades como la siguiente: $XYX=-Y$. Como ejercicio, comprobar que esta identidad es valida, y despues comprobar que la siguiente identidad, $XR_{y}(\theta)X = R_{y}(-\theta)$, tambien es valida.


### Compuertas de un solo cubit como producto de los operadores de rotacion

Cualquier compuerta cuantica de un solo cubit generada por una transformacion unitaria *U*, puede ser representada de la siguiente forma:

$
U = exp(i\alpha)R_{\hat{n}}(\theta)
$

para los numeros reales $\alpha$ y $\theta$ y el vector tri-dimensional $\hat{n}$ que definimos en la seccion anterior.

**Ejemplo**
Los valores $\alpha, \theta$, y $\hat{n}$ para los cuales la compuerta de Hadamard y la compuerta S se pueden representar como $exp(i\alpha)R_{\hat{n}}(\theta)$ corresponden a $alpha= \frac{\pi}{2}$, $\theta = \pi$ y $\vec{n} = \frac{1}{\sqrt{2}} (1,0,1)$. Empezamos por expander $R_{\hat{n}}$ para obtener:
$
U = exp(i\alpha)R_{\hat{n}}(\theta) = exp(i\alpha) \left( cos\frac{\theta}{2}I - i sin\frac{\theta}{2} (n_{x}X + n_{y}Y + n_{z}Z) \right)
$

y ahora sustituyendo los valores para $\alpha, \theta$ y $\vec{n}$:

$
U = exp\left(\frac{i\pi}{2}\right) \left( cos\frac{\pi}{2} I - isin\frac{\pi}{2} \left( \frac{X}{\sqrt{2}} + \frac{Z}{\sqrt{2}} \right) \right)
$

y por lo tanto:

$
U = \frac{X}{\sqrt{2}} + \frac{Z}{\sqrt{2}} = H
$

## Descomposicion de compuertas de 1-cubit

Cualquier operador unitario arbitrario que actue en un solo cubit puede representarse mediante una combinacion de rotaciones y cambios de amplitud en dicho cubit. Ahora, vamos a obtener una expresion mas general para representar las compuertas de 1-cubit. Esta descomposicion tendra mucha utilidad cuando abordemos el tema de operaciones controladas.

### Descomposicion Z-Y para un operador unitario aplicado a un cubit

Suponiendo que *U* es una operacion unitaria en un cubit, existen numeros reales $\alpha, \beta, \gamma$ y $\delta$ tales que:

$
U = e^{i\alpha}R_{z}(\beta)R_{y}(\gamma)R_{z}(\delta) (*)
$

y por lo tanto:

$
U = \begin{pmatrix}
	e^{i(\alpha - \beta/2- \delta/2)}cos\frac{\gamma}{2} & -e^{i(\alpha - \beta/2 + \delta/2)}sin\frac{\gamma}{2}\\
	e^{i(\alpha + \beta/2- \delta/2)}sin\frac{\gamma}{2} & e^{i(\alpha + \beta/2 + \delta/2)}cos\frac{\gamma}{2}
	\end{pmatrix}
$

La idea general de representar las transformaciones aplicadas a un cubit de esta manera, es visualizar que dichas transformaciones representan en realidad, una combinacion de tres tipos de transformacion:

- Cambio de fase por un factor $\delta$: $K(\delta) = e^{i\delta}I$
- Una rotacion por un factor $\beta$: 
$
R(\beta) = \begin{pmatrix} cos\beta & sin\beta \\ -sin\beta & cos\beta \end{pmatrix}
$
- Una rotacion de fase por un factor $\alpha$: 
$
T(\alpha) = \begin{pmatrix} e^{i\alpha} & 0 \\ 0 & e^{-i\alpha} \end{pmatrix}
$

donde las siguientes condiciones aplican:
$
K(\delta_{1} + \delta_{2}) = K(\delta_{1})K(\delta_{2})
$

$
R(\beta_{1} + \beta_{2}) = R(\beta_{1})R(\beta_{2})
$

y 

$
T(\alpha_{1}+\alpha_{2}) = T(\alpha_{1}) +  T(\alpha_{2})
$

y el operador *K* commuta con si mismo, *T* y *R*. Ademas, para compuertas que actuan en un solo cubit, no se incluye el operador *K*, sino simplemente el factor escalar $K(\delta) = e^{i\delta}$, ya que solo representa un cambio de fase global que es equivalente a la matriz de identidad en sistemas de un cubit. Visualmente, podemos representar las transformaciones *R* y *T* como rotaciones de un factor de 2$\alpha$ sobre el eje *y-* y *z-* en la esfera de Bloch, respectivamente. De esta manera, cualquier tranformacion unitaria, se puede descomponer en una secuencia de tranformaciones de la forma:

$
U = K(\delta)T(\alpha)R(\beta)T(\gamma)
$

En conclusion, esta representacion general de compuertas que actuan en un solo cubit, nos permitira desarrollar el formalismo necesario para construit compuertas que actuen en multiples cubits en secciones siguientes.

Por ultimo, vamos a utilizar la expresion para representar U mediante el producto de tres tipos de transformacions para definir el siguiente corolario que tiene aplicaciones en la construccion de compuertas controladas.

### Corolario
Toda compuerta unitaria *U* de 1-cubit se puede escribir en la forma:

$
U = e^{i\alpha}AXBXC,
$

donde A, B y C son operadores unitarios que cumplen $ABC=I$.
