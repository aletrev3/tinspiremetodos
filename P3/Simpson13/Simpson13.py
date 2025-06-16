import sympy as sp
print("Simpson 1/3")
funcion = input("Ingrese la función a integrar: ")
a = float(input("Ingrese el límite inferior (a): "))  
b = float(input("Ingrese el límite superior (b): "))
n = int(input("Ingrese el número de subintervalos (n): "))
if n%2 !=0:
    print("El número de subintervalos debe ser par")
h = (b - a) / n  # Ancho de cada subintervalo
funcion_a = sp.sympify(funcion).subs(sp.symbols('x'), a)  # Evaluar la función en el límite inferior
funcion_b = sp.sympify(funcion).subs(sp.symbols('x'),b)
for i in range(1, n-1):
    x = a + i * h  # Calcular el punto xi
    if i % 2 == 0:
        funcion_a += 2 * sp.sympify(funcion).subs(sp.symbols('x'), x)  # Sumar el valor de la función en xi, multiplicado por 2
    else:
        funcion_a += 4 * sp.sympify(funcion).subs(sp.symbols('x'), x)  # Sumar el valor de la función en xi, multiplicado por 4
integral = (h / 3) * (funcion_a + funcion_b)  # Calcular la integral usando la regla de Simpson
print(f"La integral de la función {funcion} desde {a} hasta {b} es: {integral.evalf()}")

