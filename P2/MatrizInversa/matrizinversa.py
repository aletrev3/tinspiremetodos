import sympy as sp
from tabulate import tabulate

# Definir símbolos generales
x1, x2, x3, x4, x5 = sp.symbols('x1 x2 x3 x4 x5')
variables = [x1, x2, x3, x4, x5]

print("Matriz Inversa a partir de ecuaciones")
n = int(input("¿Cuántas ecuaciones/variables tiene el sistema? "))

# Leer ecuaciones
ecuaciones = []
for i in range(n):
    eq = input(f"Ingrese la ecuación #{i+1} (forma estándar: ")
    ecuaciones.append(sp.sympify(eq))

# Crear matriz de coeficientes
A = sp.Matrix([[eq.coeff(variables[j]) for j in range(n)] for eq in ecuaciones])
det = A.det()
cofactores = A.cofactor_matrix()
adjunta = cofactores.T
A_inv = A.inv() if det != 0 else "No existe (det=0)"

# Mostrar matriz A
print("\nMatriz A (coeficientes):")
sp.pprint(A)

# Mostrar determinante
print(f"\nDeterminante |A| = {det}")

# Mostrar matriz adjunta
print("\nMatriz Adjunta (traspuesta de la de cofactores):")
sp.pprint(adjunta)

# Mostrar matriz inversa
print("\nMatriz Inversa A⁻¹:")
if isinstance(A_inv, str):
    print(A_inv)
else:
    sp.pprint(A_inv)

# Mostrar matriz de cofactores con etiquetas c11, c12, etc.
cofactor_tabla = []
for i in range(n):
    fila = []
    for j in range(n):
        etiqueta = f"c{i+1}{j+1} = {cofactores[i, j]}"
        fila.append(etiqueta)
    cofactor_tabla.append(fila)

print("\nMatriz de Cofactores (con etiquetas cᵢⱼ):")
print(tabulate(cofactor_tabla, tablefmt="fancy_grid"))
