import math
import sympy as sp

print("Newton Raphson\n\n")

funcion = input("Función original =\n")  # f(x) de usuario
x = sp.symbols('x')  # Declaración de x como variable simbólica
valdex = float(input("Valor de x = "))
derfun = dfo_dx = sp.diff(funcion, x)
valdexf = funcion.subs(x, valdex)
valdexfr = round(valdexf, 4)
valdexr = derfun.subs(x, valdex)
valdexrr = round(valdexr, 4)
print(f"Valor de derivada con x = {valdexrr}") 

print(f"Valor de x (A)= {valdex}")
print(f"Valor de funcion con x (B)= {valdexfr}")
print(f"Derivada de funcion original (C) = {derfun}")
x_i = valdex - (valdexfr / derfun)
x_i_l = valdex - (valdexfr / derfun)
print(f"Valor de funcion xi = {x_i_l}")
valdex = x_i_l

#2*x^3-11.7*x^2+17.7*x-5