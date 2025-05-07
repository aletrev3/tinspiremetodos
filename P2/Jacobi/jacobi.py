import sympy as sp
import numpy as np 
print("Método de Gauss-Seidel\n\n")
numfunc = int(input("Número de funciones: "))
numrep = int(input("Número de repeticiones: "))
x_ini = float(input("Valor para inicializar x: "))

# Definir las variables simbólicas
x1, x2, x3, x4, x5 = sp.symbols('x1 x2 x3 x4 x5')
variables = [x1, x2, x3, x4, x5]

# Lista para guardar las funciones ingresadas
funciones = []
for i in range(numfunc): 
    xen_fun = input(f"Función {i+1} con x despejada\nx{i+1} = ")
    funciones.append(sp.sympify(xen_fun))  # Convertir a expresión simbólica

valores = [x_ini] * numfunc #inicializar x

for iteracion in range(numrep):
    print(f"\nIteración {iteracion + 1}")
    for i in range(numfunc):
        sustituciones = {variables[j]: valores[j] for j in range(numfunc)}
        valores[i] = float(funciones[i].subs(sustituciones))  # Actualiza x_i usando todos los x actuales
    for i in range(numfunc):
        print(f"x{i+1} = {valores[i]}")
        print(f"Valor total de función: {funciones[i].subs(sustituciones)}")
