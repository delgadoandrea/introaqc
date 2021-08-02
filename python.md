---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(launch/thebe)=
# Introduction to Python

## Jupyter Notebooks

The most popular way to access, modify and run Python scripts is through Jupyter Notebooks. These notebooks have two main types of cells: Code and MarkDown.

- A code cell is used to write and execute your code.
- A Markdown cell is used to write text descriptions, notes, formulas or include graphics and images. On a Markdown cell, you can format your content by using Markdown, HTML, or LaTex code.

To run a given command cell in your Notebook, you can press *CTRL+ENTER*. For example, try the following few lines:

```{code-cell} ipython3
print("Hello World")
str="*"
for i in range(10):
	print(str)
	str+="*"
```

An example of a Markdown cell:

```{code-cell} ipython3
<b> This is the fourth cell.</b>

This is also a markdown cell.

LaTex is used to show mathematical expressions, formulas, etc. 

For example, $ x^2 + y ^ 2 = \frac{4}{9} $, $ \sum_{i=1}^n (i+2)^{3} $, or $ \left( \begin{array}{rr}  1 & 0 & -1 \\ 2 & -2 & 0 \\ 3 & -1 & -2  \end{array} \right) $.

<i>By double clicking on this cell, you can see the code.</i> <br> 
<u>By executing/running this cell, you can see the result content.</u>
```

## Variables

```{code-cell} ipython3
number = 5 # integer
real = -3.4 # float

name = 'Andrea' # string
surname = "Delgado" # string

boolean1 = True # Boolean 
boolean2 = False # Boolean 
```

## Strings

```{code-cell} ipython3
str1 = "I am a string"
str2 = 'I am also a string value'

# a string can be seen as a list of character (a string with length 1)
#    each of them is accessed from 0 to len(str)-1

# print the first and last characters of str1
print("the char at 0 is",str1[0])
print("the char at 0 is",str1[len(str1)-1])

# print every character of str1
for ch in str1:
    print(ch)
```

## Arithmetic Operators

**Basic Operators**

```{code-cell} ipython3
a = 13
b = 5
print("a =",a)
print("b =",b)
print()

# basics operators
print("a + b =",a+b)
print("a - b =",a-b)
print("a * b =",a*b)
print("a / b =",a/b)
```

## Objects

**Lists**
```{code-cell} ipython3
mylist = [10,8,6,4,2] 

print(mylist)
```

**Tuple**
```{code-cell} ipython3
# tuple
mytuple=(1,4,5,'string') 

print(mytuple)
```

**Dictionary**
```{code-cell} ipython3
mydictionary = {
    'name' : "Andrea",
    'surname':'Delgado',
    'age': 29
}

print(mydictionary)

print(mydictionary['surname'])
```

## Size of an object

We use the method "len()" that takes an object as the input.

```{code-cell} ipython3
# length of a string
print(len("Andrea Delgado"))

# size of a list
print(len([1,2,3,4]))

# size of a dictionary
mydictionary = { 'name' : "Andrea", 'surname':'Delgado', 'age': 29}
print(len(mydictionary))
```

## Loops

**While Loop**
```{code-cell} ipython3
i = 10
while i>0: # while condition(s):
    print(i)
    i = i - 1   
```

**For Loop**
```{code-cell} ipython3
for i in range(10): # i is in [0,1,...,9]
    print(i) 
```

```{code-cell} ipython3
for i in range(0,23,4): # i is in [0,4,8,12,16,20]
    print(i)
```

```{code-cell} ipython3
for i in range(0,23,4): # i is in [0,4,8,12,16,20]
    print(i)
```

```{code-cell} ipython3
for i in [3,8,-5,11]: 
    print(i)
```

```{code-cell} ipython3
mydictionary = {
    'name' : "Andrea",
    'surname':'Delgado',
    'age': 29,
}

for key in mydictionary:
    print("key is",key,"and its value is",mydictionary[key])
```

**Conditionals**
```{code-cell} ipython3
for a in range(4,7):
    
    # if condition(s)
    if a<5: 
        print(a,"is less than 5")
        
    # elif conditions(s)
    elif a==5: 
        print(a,"is equal to 5")
        
    # else
    else:
        print(a,"is greater than 5")
```

## Logical and Boolean Operators

**Logical Operator "And"**
```{code-cell} ipython3
i = -3
j = 4
if i<0 and j > 0:  
    print(i,"has minus sign negative AND",j,"has plus sign")
```

**Logical Operator "Or"**
```{code-cell} ipython3
i = -2
j = 2
if i==2 or j == 2:  
    print("i OR j is 2: (",i,",",j,")")
```

**Logical Operator "Not"**
```{code-cell} ipython3
i = 3
if not (i==2):
    print(i,"is NOT equal to 2")
```

**Logical Operator "Equal To"**
```{code-cell} ipython3
i = -1
if i == -1:
    print(i,"is EQUAL TO -1")
```

**Logical Operator "Not Equal To"**
```{code-cell} ipython3
i = 4
if i != 3:
    print(i,"is NOT EQUAL TO 3")
```

**Logical Operator "Less than or equal to"**
```{code-cell} ipython3
i = 2
if i <= 5:
    print(i,"is LESS THAN OR EQUAL TO 5")
```

## List Operations

**Concatenation of two lists**
```{code-cell} ipython3
list1 = [1,2,3]
list2 = [4,5,6]

#concatenation of two lists

list3 = list1 + list2
print(list3)

list4 = list2 + list1
print(list4)
```

**Apending a new element**
```{code-cell} ipython3
list = [0,1,2]

list.append(3)
print(list)

list = list + [4]
print(list)
```

## Functions
```{code-cell} ipython3
def summation_of_integers(n):
    summation = 0
    for integer in range(n+1):
        summation = summation + integer
    return summation

print(summation_of_integers(10))
print(summation_of_integers(20))
```
