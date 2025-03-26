import math
import sympy as sp

print("Método de la Secante\n\n")
funcion = input("Función original =\n")  # f(x) de usuario

X_i_l= float(input("Valor de I-L: "))
X_i= float(input("Valor de I: "))
#err= float(input ("Error: "))

x = sp.symbols('x')  # Declaración de x como variable simbólica
fun = sp.sympify(funcion)
res = 100
i=0
for i in range(20): 
    i += 1
    print(f"Iteración {i}") 
    print(f"Valor de xi-l sin funcion (A)\n{X_i_l}")
    print(f"Valor de xi sin funcion (B)\n{X_i}")
    fun_il = fun.subs(x, X_i_l)
    fun_ilr = round(fun_il, 4)
    print(f"Valor de funcion Xi-l (C)\n{fun_ilr}")
    fun_i = fun.subs(x, X_i)
    fun_ir = round(fun_i, 4)
    print(f"Valor de funcion Xi (D) \n{fun_ir}")
    res = X_i - ((fun_ir*(X_i_l - X_i))/(fun_ilr - fun_ir))
    res = round(res, 4)
    print(f"Valor de  ecuación completa\n{res}")
    X_i_l = X_i #convertir xi-l en la nueva xi 
    X_i = res #convertir el resultado en la nueva xi
    fun_ilr = fun_ir # convertir la funcion de xi f(xi) en la nueva f(xi-l)
    
