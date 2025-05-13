import numpy as np

def imprimir_matriz(matriz, mensaje=""):
    if mensaje:
        print(f"\n{mensaje}")
    for fila in matriz:
        print("  ".join(f"{elem:8.3f}" for elem in fila))
    print()

def gauss_jordan():
    n = int(input("¿Cuántas ecuaciones (y variables) tiene el sistema?: "))

    matriz = []
    print("\nIngresa los coeficientes y el término independiente para cada ecuación:")
    for i in range(n):
        fila = []
        for j in range(n):
            val = float(input(f"Coeficiente x{j+1} en ecuación {i+1}: "))
            fila.append(val)
        b = float(input(f"Término independiente en ecuación {i+1}: "))
        fila.append(b)
        matriz.append(fila)

    A = np.array(matriz, dtype=float)
    imprimir_matriz(A, "Matriz aumentada inicial:")

    # Gauss-Jordan
    for i in range(n):
        # Hacer el pivote 1
        pivote = A[i][i]
        if pivote == 0:
            print(f"No se puede dividir por 0 en la fila {i+1}.")
            return
        A[i] = A[i] / pivote
        imprimir_matriz(A, f"Paso {i+1}.1: Fila {i+1} dividida entre {pivote:.3f} para hacer 1 el pivote.")

        # Hacer ceros en la columna i
        for j in range(n):
            if j != i:
                factor = A[j][i]
                A[j] = A[j] - factor * A[i]
                imprimir_matriz(A, f"Paso {i+1}.2: Fila {j+1} menos {factor:.3f} × Fila {i+1}.")

    # Mostrar resultado
    imprimir_matriz(A, "Matriz reducida final (solución):")
    for i in range(n):
        print(f"x{i+1} = {A[i][-1]:.3f}")

# Ejecutar el programa
gauss_jordan()
