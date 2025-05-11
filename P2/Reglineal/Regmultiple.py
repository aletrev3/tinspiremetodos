import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Entrada de datos
n_obs = int(input("¿Cuántas columnas vas a ingresar? "))
n_vars = int(input("¿Cuántos renglones tiene cada columna? "))

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

# Convertir a arrays y dataframe
X = np.array(X)
y = np.array(y)

df = pd.DataFrame(X, columns=[f"x{i+1}" for i in range(n_vars)])
df["y"] = y

# Entrenar modelo
model = LinearRegression()
model.fit(X, y)

# Mostrar tabla de datos
print("\n=== TABLA DE DATOS INGRESADOS ===")
print(df.to_string(index=False))

# Mostrar ecuación
print("\n=== ECUACIÓN DE REGRESIÓN LINEAL MÚLTIPLE ===")
print(f"Intercepto (a): {model.intercept_:.4f}")
for i, coef in enumerate(model.coef_):
    print(f"b{i+1} (coef x{i+1}): {coef:.4f}")
    
ecuacion = f"y = {model.intercept_:.4f}"
for i, coef in enumerate(model.coef_):
    ecuacion += f" + ({coef:.4f})*x{i+1}"
print("\nEcuación completa:")
print(ecuacion)

# Evaluación del modelo
y_pred = model.predict(X)
print("\n=== MÉTRICAS DEL MODELO ===")
print("Error cuadrático medio (MSE):", mean_squared_error(y, y_pred))

# Predicción con valores nuevos 
while True:
    respuesta = input("\n¿Deseas predecir y con nuevos valores? (s/n): ").lower()
    if respuesta != 's':
        break

    nuevos_valores = []
    print("Introduce los valores de las variables independientes:")
    for i in range(n_vars):
        val = float(input(f"  x{i+1}: "))
        nuevos_valores.append(val)

    nuevos_valores_np = np.array([nuevos_valores])
    prediccion = model.predict(nuevos_valores_np)[0]

    # Desglose paso a paso
    print("\n=== ECUACIÓN CON NUEVOS VALORES ===")
    print(f"y = {model.intercept_:.4f}", end=" ")
    suma = model.intercept_
    for i, (coef, valor) in enumerate(zip(model.coef_, nuevos_valores)):
        prod = coef * valor
        suma += prod
        print(f"+ ({coef:.4f} * {valor})", end=" ")
    print(f"\n=> y N = {suma:.4f}")
