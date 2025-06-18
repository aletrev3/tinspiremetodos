import sympy as sp
from tabulate import tabulate as tb

print("Simpson 3/8 Compuesto\n")
funcion = input("Ingrese la función a integrar: ")
a = sp.Rational(input("Ingrese el límite inferior (a): "))  
b = sp.Rational(input("Ingrese el límite superior (b): "))
n = int(input("Ingrese el número de intervalos (n): "))
sum_1 = a
tabla = []
if n%3 != 0:
    print("El número de intervalos debe ser múltiplo de 3")
    exit()
h_in = (b-a)/n
h = sp.Rational(0)
val_sum_j = 0
j = 1
g = 2
val_sum_g = 0
k = 0
val_sum_k = 0
fml = []


for i in range (n+1):
    j+=1
    g+=1
    k+=1
    sum_h = sum_1 + h #suma de h
    (sum_h)
    fun_x = sp.sympify(funcion).subs(sp.symbols('x'), sum_h) #sustituir h en función
    sum_1 = sum_h
    h = (b-a)/n
    fila = [i+1, sum_h, fun_x]
    tabla.append(fila)
    print(f"i = {i+1}")
    fml.append(fun_x)

    if j%3 == 0:
        mult_j = fun_x + val_sum_j
        val_sum_j = mult_j
    elif g%3 == 0 and i+1 != 1:
        mult_g = fun_x + val_sum_g
        val_sum_g = mult_g
    elif k%3 == 0 and k!= 0:
        mult_k = fun_x + val_sum_k
        val_sum_k= mult_k

headers = ["No.", "Valor h", "Valor función"]
print(tb(tabla, headers=headers, tablefmt="grid"))

print(f"k suma: {sp.N(mult_k)}")
print(f"g suma: {sp.N(mult_g)}")
print(f"j suma: {sp.N(mult_j)}\n")

print(f"Fórmula:\n(3/8*({h})*[{sp.N(fml[0])}+(3*({sp.N(mult_k)}))+(3*({sp.N(mult_g)}))+(2*({sp.N(mult_j)}))+{sp.N(fml[-1])}]\n")

valor = ((3/8)*h)*(fml[0]+(3*mult_k)+(3*mult_g)+(2*mult_j)+fml[-1])
print(f"Valor de integral:\n {sp.N(valor)}")





