#!/usr/bin/env python
# coding: utf-8

# (circuitos)=
# 
# # El Modelo de Circuitos Cuanticos
# 
# El modelo de computacion clasica de circuitos puede ser generalizado a un modelo de circuitos cuanticos. En este modelo, los qubits son transportados por cables y en su recorrido se encuentran con compuertas cuanticas que actuan sobre ellos, como en la siguiente figura. Los cables son las lineas horizontales y los cubits se propagan de izquierda a derecha en el tiempo. 
# 
# ![circuito](../../circuit.png)
# 
# En este ejemplo el estado de 3 cubits entra en el circuito para ser procesado por las compuertas $H$, $X$ y $R_{y}$. Como salida del circuito tenemos el estado de 3 cubits. Se realiza una medicion cubit por cubit en la base computacional. Ahora que se han establecido los conceptos de unitariedad y reversibilidad de los operadores cuanticos, podemos empezar a discutir dichos operadores en terminos de compuertas cuanticas. El caso mas sencillo es el de las compuertas cuanticas que operan en un solo cubit. Para empezar, vamos a repasar la representacion de un cubit como estado cuantico.
# 
# El estado de un cubit se puede representar de la siguiente forma:
# 
# $
#     |\Psi> = \alpha|0> + \beta|1>
# $
# 
# En la ecuacion anterior, $\alpha$ y $\beta$ representan numeros complejos que indican las amplitudes de probabilidad para los estados base $|0>$ y $|1>$. La suma de estas probabilidades de amplitud debe ser igual a 1 y por lo tanto, tenemos la condicion: $|\alpha|^{2} + |\beta|^{2} = 1$. Un cubit en el estado $\alpha|0> + \beta|1>$ puede ser visualizado como un punto $(\theta, \phi)$ en la esfera de Bloch, donde $\alpha = cos(\theta/2)$ y $\beta = e^{i\phi}sin(\theta/2)$. Finalmente, las bases ortogonales $|0>$ y $|1>$ pueden ser representadas como vectores de columna:
# 
# $
#     |0> = \begin{pmatrix} 1 \\ 0 \end{pmatrix},
#     |1> = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
# $
# 
# Los operadores que actuan en un cubit deben preservar la norma de los vectores base, y por lo tanto, las compuertas cuanticas que operan en un cubit son matrices unitarias de estructura 2X2. Dentro de esta categoria, las matrices de Pauli son de los operadores mas relevantes para la computacion cuantica.
# 
# $
#     X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}; Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}; Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
# $
# 
# Otras compuertas cuanticas para un solo cubit incluyen la compuerta de Hadamard (H), la compuerta de fase (S), y la compuerta $\pi/8$ (T):
# 
# $
#     H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}; S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}; T = \begin{pmatrix} 1 & 0 \\ 0 & exp(i\pi/4) \end{pmatrix}
# $
# 
# **Ejercicio:** Comprobar que $H=(X+Z)/\sqrt{2}$ y $S=T^{2}$
# 
# Las matrices de Pauli son la base de 3 matrices unitarias muy importantes, los operadores de rotacion. Los operadores de rotacion sobre los ejes $\hat{x}, \hat{y},$ y $\hat{z}$ son generados al exponenciar las matrices de Pauli:
# 
# $
# 	R_{x}(\theta) = e^{-i\theta X/2} = cos\frac{\theta}{2}I - i sin\frac{\theta}{2}X = \begin{pmatrix} cos\frac{\theta}{2} & -isin\frac{\theta}{2} \\ -isin\frac{\theta}{2} & cos\frac{\theta}{2} \end{pmatrix}\\
# $
# $
# 	R_{y}(\theta) = e^{-i\theta Y/2} = cos\frac{\theta}{2}I - i sin\frac{\theta}{2}Y = \begin{pmatrix} cos\frac{\theta}{2} & -sin\frac{\theta}{2} \\ sin\frac{\theta}{2} & cos\frac{\theta}{2} \end{pmatrix}\\
# $
# $
# 	R_{z}(\theta) = e^{-i\theta Z/2} = cos\frac{\theta}{2}I - i sin\frac{\theta}{2}Z = \begin{pmatrix} e^{-i\frac{\theta}{2}} & 0 \\ 0 & e^{-i\frac{\theta}{2}} \end{pmatrix}\\
# $
# 
# Por ejemplo, consideremos un estado arbitrario de 1-cubit descrito en terminos de sus angulos del vector de Bloch $\sigma$ y $\tau$:
# 
# $
#     cos\frac{\sigma}{2}|0> + e^{i\tau}sin\frac{\sigma}{2}|1>
# $
# 
# cuya representacion en vector de columna corresponde a:
# 
# $
#     \begin{pmatrix}
#     cos\frac{\sigma}{2} \\ e^{i\tau}sin\frac{\sigma}{2}
#     \end{pmatrix}
# $
# 
# El efecto de aplicar $R_{z}(\theta)$ a este estado sera:
# 
# $
# 	 \begin{pmatrix} e^{-i\frac{\theta}{2}} & 0 \\ 0 & e^{-i\frac{\theta}{2}} \end{pmatrix} \begin{pmatrix}
#     cos\frac{\sigma}{2} \\ e^{i\tau}sin\frac{\sigma}{2}
#     \end{pmatrix} 
# $
# $
#     =  \begin{pmatrix}
#     e^{-i\frac{\theta}{2}}cos\frac{\sigma}{2} \\ e^{-i\frac{\theta}{2}}e^{i\tau}sin\frac{\sigma}{2} \end{pmatrix}\\
# $
# $   
#     = e^{-i\frac{\theta}{2}}\begin{pmatrix}
#     cos\frac{\sigma}{2} \\ e^{i\theta}e^{i\tau}sin\frac{\sigma}{2} \\
#     \end{pmatrix}\\
# $
# $
#     = e^{-i\frac{\theta}{2}}(cos\frac{\theta}{2}|0> + e^{i(\tau + \theta})sin\frac{\theta}{2}|1>)
# $
# 
# Eliminando la fase global, el estado resultante de aplicar $R_{z}(\theta)$ es:
# 
# $
#     cos\frac{\theta}{2}|0> + e^{i(\tau + \theta})sin\frac{\theta}{2}|1>
# $
# 
# y por lo tanto, podemos concluir que la compuerta $R_{z}(\theta)$ ha cambiado el angulo $\tau$ a $\tau + \theta$, lo que representa una rotacion de $\theta$ alrededor del eje $z$ de la esfera de Bloch.
