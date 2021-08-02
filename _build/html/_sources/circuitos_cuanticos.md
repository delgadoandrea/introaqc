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

(circuitos_cuanticos)=

# Un Modelo Cuantico de Computacion

Hasta ahora hemos discutido el proceso de codificacion de informacion en estados cuanticos, asi como algunas de las propiedades unicas de dicha informacion cuantica, tales como estados entrelazados y la medicion. En este capitulo, desarrollaremos los mecanismos basicos para el procesamiento de informacion cuantica. Dicho proceso es mediado por la transformacion de sistemas cuanticos. Para entender como funciona la computacion cuantica, debemos entender que tipo de transformaciones son permitidas por la naturaleza y cuales no.

Toda transformacion en un sistema de *n-cubits* puede ser expresada como una secuencia de transformaciones en sistemas de uno o mas cubits. La eficiencia de una tranformacion cuantica es cuantificada en terminos del numero de compuertas utilizadas, como vamos a ver mas adelante.

Los temas a abordar en este capitulo incluyen:

- Transformaciones unitarias
- Compuertas cuanticas aplicadas a un solo cubit
- Compuertas cuanticas aplicadas a multiples cubits
- Operaciones no-reversibles