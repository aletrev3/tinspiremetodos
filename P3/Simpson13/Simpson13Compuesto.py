import sympy as sp
from tabulate import tabulate as tb

print("Simpson 1/3 Compuesto\n")
funcion = input("Ingrese la función a integrar: ")
a = sp.Rational(input("Ingrese el límite inferior (a): "))  
b = sp.Rational(input("Ingrese el límite superior (b): "))
n = int(input("Ingrese el número de intervalos (n): "))
if n%2 != 0:
    print("El número de intervalos debe ser par")
    exit()
h_in = (b-a)/n
h = sp.Rational(0)
fml = []
print(f"El valor de h es: {h_in}")

sum_1 = a
tabla = []
val_imp = 0
val_par = 0
prim_ult = []



for i in range (n+1):
    sum_h = sum_1 + h #suma de h
    (sum_h)
    fun_x = sp.sympify(funcion).subs(sp.symbols('x'), sum_h) #sustituir h en función
    sum_1 = sum_h
    h = (b-a)/n
    fila = [i+1,sum_h, fun_x]
    tabla.append(fila)
    fml.append(f" {fun_x}")
    i+=1
    if i%2 !=0 and sum_1!=a and i!=n+1:
        impares = fun_x+val_imp
        val_imp = impares
    elif i%2 == 0:
        pares = fun_x+val_par
        val_par = pares
    prim_ult.append(fun_x)

mult_h = h_in / 2
headers = ["No.", "Valor h", "Valor función"]
print(tb(tabla, headers=headers, tablefmt="grid")) 
print(f"Suma de valores impares: {pares}\n")
print(f"Suma de valores pares: {impares}\n")

print(f"Fórmula:\nI = ({h})/3[({prim_ult[0]}) + (4*({pares}))+(2*({impares}))+({prim_ult[-1]})]")
val_tot = (h/3)*(prim_ult[0]+(4*pares)+(2*impares)+prim_ult[-1])

print(f"Valor de la Integral:\n{val_tot} ")