# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b1O7X5x0gktQeDG2is0qkVxdfLboL86d
"""

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from math import *
# Función cuadrática. Encontrar una raiz real positvia gráficamente 
def f1(x):
    return cos(x)/(np.exp(x))
def f2(x):
    return x


# Valores del eje X que toma el gráfico.
x=np.linspace(-0,1,100)
# Graficar ambas funciones.
plt.plot(x, [f1(i) for i in x])
plt.plot(x, [f2(i) for i in x])
plt.axhline(0, color="red")
plt.axvline(0, color="green")
plt.xlim(-1,1)
plt.ylim(-1, 1)
plt.title("Función")
# Mostrarlo.
plt.grid()
plt.show()

# Función cuadrática.
def f1(x):
    return -x-4+10**(x)
# Valores del eje X que toma el gráfico.
x=np.linspace(-1,1,10)
# Graficar ambas funciones.
plt.plot(x, [f1(i) for i in x])
plt.axhline(0, color="red")
plt.axvline(0, color="green")
plt.xlim(-1,1)
plt.ylim(-1, 1)
plt.title("Función -x-4+10**(x) ")
plt.savefig("output.png") # Guardar gráfico como imágen PNG.
# Mostrarlo.
plt.grid()
plt.show()

"""TABULACIONES"""

import pandas as pd 
def f1(x):
    return -x-4+10**(x)
X=np.linspace(0,1,11)
l1=[]
l2=[]
for x in X :
     l1.append(x)
     l2.append(f1(x))
df = pd.DataFrame()
df['x'] =l1
df['f(x)'] =l2
print(df)

X=np.linspace(0.60,0.70,11)
l3=[]
l4=[]
for x in X :
     l3.append(x)
     l4.append(f1(x))
df['x'] =l3
df['f(x)']=l4
print(df)

X=np.linspace(0.66,0.67,11)
l5=[]
l6=[]
for x in X :
     l5.append(x)
     l6.append(f1(x))
df = pd.DataFrame()
df['x'] =l5
df['f(x)']=l6
print(df)

"""METODO DE BISECCIÓN"""

import pandas as pd 
from math import *
L1=[]
L2=[]
L3=[]
L4=[]

def f(x):
     return x*log(x)-1.2

def bis(f,a,b,N,tol):

  for k in range(N):
    x=(a+b)/2
    if(x<tol):
      break 
    elif(f(x)*f(b)<0):
      a=x
    elif(f(x)*f(a)<0):
      b=x
    else:
      break
    L1.append(a)
    L2.append(b)
    L3.append(x)
    L4.append(f(x))

bis(f,1,2,30,10**(-4))
df = pd.DataFrame()

df['a']=L1
df['b']=L2
df['x']=L3
df['f(x)']=L4
print(df)

from math import *
import numpy as np
import matplotlib . pyplot as plt
def funcion1(x):
    return x**3 + x -4
# Ingreso datos de entrada para los diferentes métodos a trabajar
a = 1
b = 2

# guarda valores iniciales
a0 = a
b0 = b

#guarda valores iniciales del error y del número de iteraciones
tol = 0.0001 #float(input("Ingrese el valor de la tolerancia: "))
nmax = 100 #float(input("Ingrese el número máximo de iteraciones: "))
error = 100
niter = 0
# Método de Bisección

# evaluo primer valor medio
m = a + (b - a)/2

#Evaluacion de la función en los puntos a, b y m
fa = funcion1(a)
fb = funcion1(b)
fm = funcion1(m)

print("# iter\t\t a \t\t f(a) \t\t b \t\t f(b) \t\t m \t\t f(m) \t\t error")
print("{0} \t\t {1:6.4f} \t {2:6.4f} \t {3:6.4f} \t {4:6.4f} \t {5:6.4f} \t {6:6.4f} \t {7:6.4f}".format(niter, a0, fa, b0, fb, m, fm, error ))

# ciclo iterativo
while error > tol and niter < nmax:
    m = a + (b - a) / 2
    if np.sign(fa) == np.sign(fm):
        a = m
        fa = funcion1(a)
    else:
        b = m
        fb = funcion1(b)
    
    m = a + (b - a)/2
    fm = funcion1(m)
    error = abs(b - a)
    niter += 1
    print("{0} \t\t {1:6.6f} \t {2:6.6f} \t {3:6.6f} \t {4:6.6f} \t {5:6.6f} \t {6:6.6f} \t {7:6.6f}".format(niter, a, fa, b, fb, m, fm, error ))

print("La raíz de la función dada en el intervalo [{0:6.4f},{1:6.4f}] es {2:6.7f}".format(a0,b0,m))