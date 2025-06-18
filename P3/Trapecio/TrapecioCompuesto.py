import sympy as sp
from tabulate import tabulate as tb
print("Trapecio Compuesto")
sum_h = 0
fun = input("Ingrese la función: ")
a = sp.Rational(input("Ingrese el valor inferior (a) ") )
b = sp.Rational(input("Ingrese el valor superior (b) "))
n = int(input("Ingrese el número de intervalos (n) "))
h_in = (b-a)/n
h = 0
fml = []
print(f"El valor de h es: {h_in}")
sum_1 = a
tabla = []
mult = []
prim_ult = []
val_imp = 0

for i in range (n+1):
    sum_h = sum_1 + h #suma de h
    (sum_h)
    fun_x = sp.sympify(fun).subs(sp.symbols('x'), sum_h) #sustituir h en función
    prim_ult.append(fun_x)
    sum_1 = sum_h
    h = (b-a)/n
    fun_mult = fun_x * 2
    fila = [i+1, sum_h, fun_x]
    tabla.append(fila)
    fml.append(fun_x)
    mult.append(fun_mult)
    if  sum_1!=a and i!=n:
        impares = fun_x+val_imp
        val_imp = impares
        print(f"val de it {sp.N(val_imp)}")

mult_h = h_in / 2
headers = ["No.", "Valor h", "Valor función"]
print(tb(tabla, headers=headers, tablefmt="grid"))
print(f"Fórmula: \n{h_in}/2*[{sp.N(prim_ult[0])} +(2*({sp.N(impares)}))+{sp.N(prim_ult[-1])}]\n")

res = (h/2)*(prim_ult[0]+(2*impares)+prim_ult[-1])
print(f"Valor de integral:\n{sp.N(res)}")