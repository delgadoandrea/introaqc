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

(antes_de_empezar)=

# Antes de empezar...

## IBM Qiskit

Qiskit es un kit de desarrollo de software (SDK) para programar los ordenadores cuanticos de IBM, por medio de pulsos y circuitos cuanticos. Qiskit esta basado en Python. Puedes accesar a Qiskit mediante:

1.  [El IBM Quantum Lab](https://quantum-computing.ibm.com) (online). 
2.  Instalando Qiskit localmente en tu ordenador. 

## Formato del libro

El libro esta desarrollado dentro de un ambiente interactivo, es decir, puedes ejecutar la mayoria de los comandos *desde tu Browser*. Este ecosistema interactivo es posible mediante la ejecucion de *kernels* en un servidor publico en [**MyBinder**](https://mybinder.org).

Por ejemplo, da click en el boton {fa}`rocket` --> {guilabel}`Live Code` en la parte superior de la pagina, y ejecuta el codigo siguiente:

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

x = np.arange(500)
y = np.random.randn(500)

fig, ax = plt.subplots()
ax.scatter(x, y, c=y, s=x)
```




