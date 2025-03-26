import sys
import sympy as sp
import mpmath

mpmath.mp.dps = 15  # Ajustar la precisión a 15 dígitos
sys.set_int_max_str_digits(1000000)  # Aumentar el límite de dígitos grandes

print("Método de Punto Fijo\n")

# Entrada de la función inicial
funini = input("Función inicial\nx = ")  
x = sp.symbols('x')  # Declarar x como variable simbólica

# Convertir la función de usuario en una expresión simbólica
funcion = sp.sympify(funini)

# Valor inicial de x
valini = float(input("Valor inicial de x\n"))

# Error absoluto deseado
errabs = float(input("Error absoluto a obtener\n"))

i = 0
errorfinr = 100  # Se inicia con un valor alto
errnu = None  # Inicializar variable para detectar convergencia

while errorfinr > errabs:
    i += 1

    # Evaluar la función en el valor actual de x
    resultado = funcion.subs(x, valini).evalf()  

    print(f"Iteración {i}: x = {resultado}")

    # Calcular el error relativo correctamente
    if i > 1:  # Evitar calcular error en la primera iteración
        errorfin = abs((resultado - valini))
        errorfinr = round(errorfin, 6)  # Redondear el error
        print(f"Error = {errorfinr}")

    # Verificar convergencia en la segunda iteración en adelante
    if errnu is not None and errorfinr > errnu:
        print("Valores no convergen.")
        break

    errnu = errorfinr
    valini = resultado
