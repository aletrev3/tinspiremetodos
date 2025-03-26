import sympy as sp

print("Método de Newton-Raphson\n\n")
funcion = input("Función original =\n")  
x = sp.symbols('x')  
valdex = float(input("Valor de x = "))
derfun = sp.diff(funcion, x)
error = float(input("Error máximo permitido: "))
print(f"Derivada sin sustituir x = {derfun}")
errrealr = float('inf') 
i = 0 
while errrealr > error:
    valdexf = sp.sympify(funcion).subs(x, valdex)
    valdexfr = round(valdexf, 4)
    valdexr = derfun.subs(x, valdex)
    valdexrr = round(valdexr, 4)     
    i += 1
    print(f"\nIteración {i}:")
    # Imprimir resultados
    print(f"Valor de x (A) = {valdex}")
    print(f"Valor de la función con x (B) = {valdexfr}")
    print(f"Valor de la derivada con x (C) = {valdexrr}") 
    x_i = valdex - (valdexfr / valdexrr)
    x_i = round(x_i, 4)
    print(f"Valor de xi+1 = {x_i}")

    # Calcular el error real
    errreal = abs((x_i - valdex) / x_i)
    errrealr = round(errreal, 4)
    print(f"Error real = {errrealr}")

    # Actualizar el valor de x para la siguiente iteración
    valdex = x_i



