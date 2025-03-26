import sys
import math
import sympy as sp
import mpmath
mpmath.mp.dps = 15  # Ajustar la precisión a 15 dígitos
sys.set_int_max_str_digits(1000000)  # Aumenta el límite a 10,000 dígitos

print("Método de Punto Fijo")

funini = input("Función inicial\nx= ")  # función inicial por usuario
valini = float(input("Valor inicial de x\n"))  # valor inicial de x
valini = float(valini)  # convertir el valor inicial en un float
errabs = input("Error absoluto a obtener\n")  # error absoluto pedido
errabs = float(errabs)  # convertir el error absoluto en un float
i = 0
errorfinr = 100
errnu = 100
while errorfinr > errabs:
    i += 1
    x = sp.symbols('x')  # x como variable simbolica hasta que se le de valor
    x.evalf()
    print(x)
    # convertir la función en una expresión simbolica
    funcion = sp.sympify(funini)
    # sustituir x como variable simbolica por el valor inicial
    resultado = (funcion.subs(x, valini).evalf())
    res = resultado  # redondear el resultado a 4 decimales
    print(f"Para la iteración {i} , x= {res}")
    # asegurar que errorfin es numérico
    errorfin = abs((res - valini) / res).evalf()
    errorfinr = round(errorfin, 4)  # redondear el error a 4 decimales
    print(f"El error es de {errorfinr}")
    valini = res  # el resultado se convierte en el nuevo valor inicial
    valini.evalf()
    if errorfinr > errnu:
        print(f"Los valores convergen")
        break
    errnu = errorfinr
    
