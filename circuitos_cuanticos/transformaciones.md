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

(transformaciones)=

# Transformaciones Unitarias

En este curso, nos referimos a una **transformacion cuantica**, a aquella transformacion que hace un mapeo de un sistema cuantico a si mismo. De esta manera, las mediciones que pudieramos ejecutar en dichos sistemas cuanticos no representan transformaciones, y el resultado de aplicar una operacion de medicion a un estado en especifico es simplemente probabilistico.

Por otro lado, la naturaleza no permite tranformaciones arbitrarias en un sistema cuantico. Por el contrario, la naturaleza limita las transformaciones aplicadas a aquellas que respetan las propiedades ligadas a la medicion y superposicion cuantica. Las transformaciones que satisfacen dichas propiedades son de tipo unitario y tienen las siguientes propiedades:


- Son transformaciones lineares en el espacio vectorial asociado al estado cuantico. Es decir, para cualquier transformacion *U*:
    $
        U(a_{1}|\Phi_{1}> + ... + a_{k}|\Phi_{k}>) = a_{1}U|\Phi_{1}> + ... + a_{k}U|\Phi_{k}>
    $
- La transformacion *U* conserva el producto interno entre dos estados $\Phi$ y $\Psi$:
    $
        <\Phi|U^{\dagger}U|\Psi> = <\Phi|\Psi>
    $
Esta propiedad implica que bajo cualquier transformacion unitaria *U*, los vectores de longitud unitaria se transforman en vectores de longitud unitaria y por lo tanto, que los espacios ortogonales se mantienen ortogonales despues de la transformacion.
- El adjunto de la transformacion unitaria $U$ debe ser igual a su inverso:
    $
        U^{\dagger} = U^{-1}
    $
Esto como resultado del hecho de que la segunda condicion solo aplica si $U^{\dagger}U = I$

Por lo tanto, podemos definir a los operadores unitarios como transformaciones unitarias en el espacio de Hilbert, que resultan en la transformacion de un vector de estado, que no cambia su longitud. Por ejemplo, para un cubit, los estados base pueden ser descritos en el espacio de Hilbert como bases ortonormales $|v_{0}> = \alpha|0> + \beta|1>$, y $|v_{1}> = \gamma|0> + \delta|1>$, donde $\alpha, \beta, \gamma$ y $\delta$ son variables complejas.

Una transformacion linear en un espacio vectorial complejo puede ser descrito por una matriz *U*:

$$
    U =\begin{pmatrix}
    \alpha & \gamma \\
    \beta & \delta\\
    \end{pmatrix}
$$

con matriz adjunta:

$$
    U^{\dagger} = \begin{pmatrix}
    \alpha^{\dagger} & \beta^{\dagger} \\
    \gamma^{\dagger} & \delta^{\dagger}\\
    \end{pmatrix}
$$

**Ejercicio**
Verificar que $UU^{\dagger} = U^{\dagger}U = I$

Por lo tanto, la condicion de unitariedad asegura tambien, que las transformaciones unitarias son reversibles. Esto quiere decir, que si aplicamos un operador unitario a un cubit por medio de una compuerta cuantica, seguida del operador adjunto de dicha compuerta, el resultado seria equivalente a aplicar la matriz de indentidad al vector original.

Una implicacion importante de esta propiedad es la no-perdida de informacion. Si necesitaramos regresar al estado anterior, solo necesitamos repetir todas las operaciones unitarias que se aplicaron al sistema.

Cabe mencionar que la condicion de unitariedad simplemente asegura que el operador $U$ no viola ninguno de los principios generales de la teoria cuantica. Esto no implica que la transformacion puede ser implementada eficientemente. En el siguiente modulo de este curso vamos a ver que es el caso de las compuertas de Toffoli, por mencionar un ejemplo.

En el modelo estandar de circuitos dentro de la computacion cuantica, todo proceso de informacion es mediado por transformaciones cuanticas, y la medicion solo se utiliza hasta el final, para recuperar los resultados. Por lo tanto, es importante hace enfasis en el hecho de que los terminos *transformacion cuantica* u *operador cuantico* se refieren a los operadores unitarios que actuan en el espacio vectorial de un estado cuantico determinado. Los operadores de medicion no entran dentro de esta descripcion.