import sympy as sp
from tabulate import tabulate as tb
print("Trapecio Compuesto")
sum_h = 0
fun = input("Ingrese la función: ")
a = float(input("Ingrese el valor inferior (a) ") )
b = float(input("Ingrese el valor superior (b) "))
n = int(input("Ingrese el número de intervalos (n) "))
h_in = (b-a)/n
h = 0
fml = []
print(f"El valor de h es: {h_in}")
sum_1 = 0
tabla = []
mult = []
prim_ult = []
for i in range (n+1):
    sum_h = sum_1 + h #suma de h
    (sum_h)
    fun_x = sp.sympify(fun).subs(sp.symbols('x'), sum_h) #sustituir h en función
    sum_1 = sum_h
    h = (b-a)/n
    fun_mult = fun_x * 2
    fila = [i+1,sum_h, fun_x]
    tabla.append(fila)
    fml.append(f" {fun_x}")
    mult.append(fun_mult)
    prim_ult.append(fun_x)
mult_h = h_in / 2
headers = ["No.", "Valor h", "Valor función"]
print(tb(tabla, headers=headers, tablefmt="grid")) 
fun_imp = " + 2 *".join(fml[:-1])
print(f"Fórmula: \n{h_in}/2 [{fun_imp} + {fun_x}]\n")
tot = sum(mult[1:-1])
sum_tot = prim_ult[0]+prim_ult[-1]
form_res = (tot+sum_tot)*mult_h
print(f"Valor de integral \n{form_res}")


