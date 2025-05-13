from fractions import Fraction
import numpy as np

def print_step(matrix, step_desc, row_labels):
    """ Imprime la matriz y la descripción del paso en fracciones """
    print(step_desc)
    print("\t".join(row_labels))
    for i, row in enumerate(matrix):
        print(f"{row_labels[i]}:\t" + "\t".join(f"{Fraction(num).limit_denominator()}" for num in row))
    print("\n" + "="*60 + "\n")

def gauss_jordan(matrix):
    """ Aplica el método de Gauss-Jordan paso a paso """
    matrix = np.array(matrix, dtype=float)
    n, m = matrix.shape
    row_labels = [f"R{i+1}" for i in range(n)]

    step_count = 1
    for i in range(n):
        # Si el pivote es cero, intercambiamos filas
        if matrix[i, i] == 0:
            for j in range(i + 1, n):
                if matrix[j, i] != 0:
                    matrix[[i, j]] = matrix[[j, i]]
                    row_labels[i], row_labels[j] = row_labels[j], row_labels[i]
                    print_step(matrix, f"Paso {step_count}: Intercambio de filas {row_labels[i]} ↔ {row_labels[j]}", row_labels)
                    step_count += 1
                    break

        # Normalizamos la fila dividiendo por el pivote
        pivot = matrix[i, i]
        matrix[i] = matrix[i] / pivot
        print_step(matrix, f"Paso {step_count}: {row_labels[i]} / {Fraction(pivot).limit_denominator()}", row_labels)
        step_count += 1

        # Hacemos ceros en las demás filas
        for k in range(n):
            if k != i:
                factor = matrix[k, i]
                matrix[k] -= factor * matrix[i]
                print_step(matrix, f"Paso {step_count}: {row_labels[k]} - ({Fraction(factor).limit_denominator()}) * {row_labels[i]}", row_labels)
                step_count += 1

    # Extraemos la solución en fracciones
    solution = [Fraction(val).limit_denominator() for val in matrix[:, -1]]
    print("Solución Final:")
    for i, val in enumerate(solution):
        print(f"x{i+1} = {val}")
    return solution

def main():
    n = int(input("Ingrese el número de ecuaciones: "))
    matrix = []

    print("Ingrese la matriz aumentada fila por fila:")
    for i in range(n):
        row = list(map(float, input(f"Fila {i+1}: ").split()))
        if len(row) != n + 1:
            print("Error: la fila debe tener el mismo número de columnas que el número de incógnitas más uno (término independiente).")
            return
        matrix.append(row)

    gauss_jordan(matrix)

if __name__ == "__main__":
    main()
