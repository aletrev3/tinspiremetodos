import math
import sympy as sp

print("Método de la Secante\n\n")
funcion = input("Función original =\n")  # f(x) de usuario

X_i_l= float(input("Valor de I-L: "))
X_i= float(input("Valor de I: "))

x = sp.symbols('x')  # Declaración de x como variable simbólica
fun = sp.sympify(funcion)
res = 100
i = 0
prev_res = None  # Variable para almacenar el resultado anterior

for i in range(20): 
    i += 1
    print(f"Iteración {i}") 
    print(f"Valor de xi-l sin funcion (A): {X_i_l}")
    print(f"Valor de xi sin funcion (B): {X_i}")
    fun_il = fun.subs(x, X_i_l)
    fun_ilr = round(fun_il, 4)
    print(f"Valor de funcion Xi-l (C): {fun_ilr}")
    fun_i = fun.subs(x, X_i)
    fun_ir = round(fun_i, 4)
    print(f"Valor de funcion Xi (D): {fun_ir}")
    res = X_i - ((fun_ir * (X_i_l - X_i)) / (fun_ilr - fun_ir))
    res = round(res, 4)
    print(f"Valor de ecuación completa: {res}")
    
    if prev_res is not None:
        errorfin = abs((res - prev_res) / res).evalf()
        errorfinr = round(errorfin, 4)  # Redondear el error a 4 decimales
        print(f"El error es de: {errorfinr}")
    else:
        print("El error no se puede calcular en la primera iteración")
    
    prev_res = res  # Almacenar el resultado actual para la siguiente iteración
    X_i_l = X_i  # Convertir xi-l en la nueva xi 
    X_i = res  # Convertir el resultado en la nueva xi
    fun_ilr = fun_ir  # Convertir la función de xi f(xi) en la nueva f(xi-l)
