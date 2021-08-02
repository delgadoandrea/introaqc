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

(circuitos)=

# El Modelo de Circuitos Cuanticos

El modelo de computacion clasica de circuitos puede ser generalizado a un modelo de circuitos cuanticos. En este modelo, los qubits son transportados por cables y en su recorrido se encuentran con compuertas cuanticas que actuan sobre ellos, como en la siguiente figura. Los cables son las lineas horizontales y los cubits se propagan de izquierda a derecha en el tiempo. 

![circuito](../circuit.png)

En este ejemplo el estado de 3 cubits entra en el circuito para ser procesado por las compuertas $H$, $X$ y $R_{y}$. Como salida del circuito tenemos el estado de 3 cubits. Se realiza una medicion cubit por cubit en la base computacional. Ahora que se han establecido los conceptos de unitariedad y reversibilidad de los operadores cuanticos, podemos empezar a discutir dichos operadores en terminos de compuertas cuanticas. 
