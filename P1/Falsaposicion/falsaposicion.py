import math
import sympy as sp

print("Regla de la Falsa Posicion\n\n")

funcion = input("Función original =\n")  # f(x) de usuario
xi = float(input("Valor de xi: "))
xu = float(input("Valor de xu: "))
err = float(input("Error: "))
x = sp.symbols('x')  # Declaración de x como variable simbólica
fun = sp.sympify(funcion)
i = 0
perr = 100
prev_xr = None  # Variable para almacenar el xr anterior

while perr > err:
    i += 1
    print(f"Iteración {i}")
    print(f"Xi sin función (A): {xi}")
    print(f"Xu sin función(B): {xu}")
    fun_xi = fun.subs(x, xi)
    fun_xir = round(fun_xi, 4)
    print(f"Funcion de xi (C): {fun_xir}")
    fun_xu = fun.subs(x, xu)
    fun_xur = round(fun_xu, 4)
    print(f"Funcion de xu (D): {fun_xur}")
    xr = xu - ((fun_xur * (xi - xu)) / (fun_xir- fun_xur))
    print(f"Valor de xr: {xr}")
    fun_xr = fun.subs(x, xr)
    print(f"Función de xr: {fun_xr}")
    
    if prev_xr is not None:
        perr = abs((xr - prev_xr) / xr)
        perrr = round(perr, 4)  # Redondear el error a 4 decimales
        print(f"Valor del error: {perrr}")
    else:
        print("El error no se puede calcular en la primera iteración")
    
    prev_xr = xr  # Almacenar xr actual para la siguiente iteración
    
    if fun_xir * fun_xr < 0:
        xu = xr  # Sustituir xu si hay cambio de signo
    else:
        xi = xr  # Sustituir xi si hay cambio de signo