import numpy as np
import pandas as pd

# Pedir datos al usuario
n_obs = int(input("¿Cuántos renglones vas a ingresar? "))
n_vars = int(input("¿Cuántas x vas a ingresar? "))

X = []
y = []

# Recolectar datos
for i in range(n_obs):
    print(f"\nRenglón #{i+1}")
    fila = []
    for j in range(n_vars):
        valor = float(input(f"  x{j+1}: "))
        fila.append(valor)
    yi = float(input("  y: "))
    X.append(fila)
    y.append(yi)

X = np.array(X)
y = np.array(y)
n = len(X)

# Crear tabla base
tabla = pd.DataFrame(X, columns=[f"x{j+1}" for j in range(n_vars)])
tabla["y"] = y

# Añadir productos x_i * x_j
for i in range(n_vars):
    for j in range(i, n_vars):
        tabla[f"x{i+1}*x{j+1}"] = tabla[f"x{i+1}"] * tabla[f"x{j+1}"]

# Añadir productos x_i * y
for i in range(n_vars):
    tabla[f"x{i+1}*y"] = tabla[f"x{i+1}"] * tabla["y"]

# Mostrar la tabla completa con valores
print("\nTABLA COMPLETA:")
print(tabla.to_string(index=False))

# Calcular y mostrar sumatorias
sumatorias = tabla.sum().to_frame(name="∑ Valores").T
print("\nSUMATORIAS:")
print(sumatorias.to_string(index=False))

