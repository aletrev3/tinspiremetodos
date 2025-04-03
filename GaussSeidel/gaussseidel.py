import sympy as sp
print ("Método de Gauss-Seidel\n\n")
numfunc = int(input("Número de funciones: "))
num = 0 
x_ini = float(input("Valor para inicializar x: "))
x = sp.symbols('x')  # declaración de x como variable simbolica
fun = []
for i in range(numfunc):
    num += 1
    xen_fun1 = input(f"Función {num} con x despejada \n  x({num})= \n")
    x_fun1 = sp.sympify(xen_fun1)  # convertir la función en una expresión simbólica
    fun.append(f"f(x)={x_fun1}")  # agregar la función a la lista
print(f"\n".join(fun))
