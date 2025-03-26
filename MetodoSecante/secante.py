import math
import sympy as sp

print("Método de la Secante\n\n")
funcion = input("Función original =\n")  # f(x) de usuario

X_i_l= input("Valor de I-L: ")
X_i= input("Valor de I: ")
err= input("Error: ")

x = sp.symbols('x')  # Declaración de x como variable simbólica
fun = sp.sympify(funcion)
while True:  
    fun_il = fun.subs(x, X_i_l)
    fun_ilr = round(fun_il, 4)
    print(fun_ilr)
    fun_i = fun.subs(x, X_i)
    fun_ir = round(fun_i, 4)
    print(fun_ir)
    fun_ir = fun_ilr #convertir la funcion en la nueva original
    
