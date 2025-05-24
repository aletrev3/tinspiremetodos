import sympy as sp

print("Método de Romberg")

# Entrada de usuario
funcion_str = input("Ingrese la función a integrar (en x): ")
a = float(input("Ingrese el límite inferior (a): "))  
b = float(input("Ingrese el límite superior (b): "))
k = int(input("Ingrese la profundidad: "))

# Definir variable simbólica
x = sp.symbols('x')

# Convertir la cadena a expresión simbólica
funcion = sp.sympify(funcion_str)

# Inicializar matriz de Romberg
matriz = [[0 for _ in range(k+1)] for _ in range(k+1)]

# Paso 1: T[0][0] usando método del trapecio básico
h = b - a
matriz[0][0] = (h / 2) * (funcion.subs(x, a) + funcion.subs(x, b))

# Rellenar matriz de Romberg
for i in range(1, k+1):
    h = h / 2
    suma = 0
    # Sumar los términos intermedios
    for j in range(1, 2**i, 2):
        suma += funcion.subs(x, a + j * h)

    matriz[i][0] = (matriz[i-1][0] / 2) + h * suma

    # Extrapolación de Richardson
    for j in range(1, i+1):
        matriz[i][j] = (4**j * matriz[i][j-1] - matriz[i-1][j-1]) / (4**j - 1)

# Resultado final
print(f"\nAproximación de la integral de {funcion_str} desde {a} hasta {b} es: {matriz[k][k].evalf()}")

# (Opcional) Mostrar toda la tabla de Romberg
print("\nTabla de Romberg:")
for fila in matriz:
    print([float(v.evalf()) for v in fila if v != 0])
