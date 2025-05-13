import sympy as sp

print("Método de Gauss-Jacobi\n")

# Entradas del usuario
numfunc = int(input("Número de funciones (variables): "))
numrep = int(input("Número de repeticiones: "))
x_ini = float(input("Valor inicial para todas las variables: "))

# Definir variables simbólicas
x1, x2, x3, x4, x5 = sp.symbols('x1 x2 x3 x4 x5')
variables = [x1, x2, x3, x4, x5]

# Leer las funciones despejadas
funciones = []
for i in range(numfunc): 
    xen_fun = input(f"Ingrese la función despejada para x{i+1} :\nx{i+1} = ")
    funciones.append(sp.sympify(xen_fun))

# Inicialización de valores
valores_actuales = [x_ini] * numfunc  # Usados para calcular nuevas aproximaciones
valores_nuevos = [x_ini] * numfunc    # Guardan los nuevos valores calculados

# Iteraciones
for iteracion in range(numrep):
    print(f"\nIteración {iteracion + 1}")
    
    for i in range(numfunc):
        sustituciones = {variables[j]: valores_actuales[j] for j in range(numfunc)}
        valores_nuevos[i] = float(funciones[i].subs(sustituciones))
    
    for i in range(numfunc):
        print(f"x{i+1} = {valores_nuevos[i]}")
    
    # Actualizar todos los valores al final (diferencia con Gauss-Seidel)
    valores_actuales = valores_nuevos.copy()

