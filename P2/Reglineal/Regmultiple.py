import numpy as np
import pandas as pd

# Entrada de datos
n_obs = int(input("¿Cuántos renglones vas a ingresar? "))
n_vars = int(input("¿Cuántas x vas a ingresar? "))

X = []
y = []

for i in range(n_obs):
    print(f"\nRenglón #{i+1}")
    fila = []
    for j in range(n_vars):
        valor = float(input(f"  x{j+1}: "))
        fila.append(valor)
    yi = float(input("  y: "))
    X.append(fila)
    y.append(yi)

# Convertir a arrays
X = np.array(X)
y = np.array(y)

# Crear DataFrame para la tabla
tabla = pd.DataFrame(X, columns=[f"x{j+1}" for j in range(n_vars)])
tabla["y"] = y

# Agregar productos x_i * x_j
for i in range(n_vars):
    for j in range(i, n_vars):
        tabla[f"x{i+1}*x{j+1}"] = tabla[f"x{i+1}"] * tabla[f"x{j+1}"]

# Agregar productos x_i * y
for i in range(n_vars):
    tabla[f"x{i+1}*y"] = tabla[f"x{i+1}"] * tabla["y"]

# Mostrar tabla completa
print("\n  DATOS :")
print(tabla.to_string(index=False))

# Mostrar sumatorias
sumatorias = tabla.sum().to_frame(name="∑ Valores").T
print("\n SUMATORIAS DE CADA COLUMNA:")
print(sumatorias.to_string(index=False))

# Resolver sistema de regresión lineal múltiple
# Agregar columna de unos para el término independiente a
X_with_intercept = np.hstack((np.ones((X.shape[0], 1)), X))

# Calcular coeficientes usando fórmula: β = (X'X)^-1 X'y
beta = np.linalg.inv(X_with_intercept.T @ X_with_intercept) @ X_with_intercept.T @ y

# Mostrar resultado
print("\n COEFICIENTES DE LA REGRESIÓN LINEAL MÚLTIPLE:")
print(f"a (intercepto) = {beta[0]:.4f}")
for i in range(1, len(beta)):
    print(f"b{i} (coeficiente para x{i}) = {beta[i]:.4f}")


