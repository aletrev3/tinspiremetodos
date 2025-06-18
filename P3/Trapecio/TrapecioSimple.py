import sympy as sp
print("Trapecio Simple")
funcion = input("Ingrese la función a integrar: ")
a = sp.Rational(input("Ingrese el límite inferior (a): "))  
b = sp.Rational(input("Ingrese el límite superior (b): "))
n = int(input("Ingrese el número de subintervalos (n): "))
if n <= 0:
    raise ValueError("El número de subintervalos debe ser mayor que cero")
h = (b - a) / n  # Ancho de cada subintervalo
print (f"El ancho de intervalo es: {h}")
funcion_a = sp.sympify(funcion).subs(sp.symbols('x'), a)  # Evaluar la función en el límite inferior
funcion_b = sp.sympify(funcion).subs(sp.symbols('x'), b)  # Evaluar la función en el límite superior
for i in range(1, n):
    x = a + i * h  # Calcular el punto xi
    funcion_a += 2 * sp.sympify(funcion).subs(sp.symbols('x'), x)  # Sumar el valor de la función en xi, multiplicado por 2
integral = (h / 2) * (funcion_a + funcion_b)  # Calcular la integral usando la regla del trapecio
print(f"La integral de la función {funcion} desde {a} hasta {b} es:\n {integral.evalf()}")