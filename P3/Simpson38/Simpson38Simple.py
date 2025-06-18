import sympy as sp
from tabulate import tabulate as tb

print("Simpson 3/8 Simple\n")
funcion = input("Ingrese la función a integrar: ")
a = sp.Rational(input("Ingrese el límite inferior (a): "))  
b = sp.Rational(input("Ingrese el límite superior (b): "))
h = (b-a)/3
fun_x0 = sp.sympify(funcion).subs(sp.symbols('x'), (a))
fun_x1 = sp.sympify(funcion).subs(sp.symbols('x'), (a+h))
fun_x2 = sp.sympify(funcion).subs(sp.symbols('x'), (a+(2*h)))
fun_x3 = sp.sympify(funcion).subs(sp.symbols('x'), (a+(3*h)))

print(f"Fórmula:\n(3/8({sp.N(h)}))*[({sp.N(fun_x0)})+(3*({sp.N(fun_x1)}))+(3*({sp.N(fun_x2)}))+({sp.N(fun_x3)})]))")


valor = ((3/8)*h)*(fun_x0+(3*fun_x1)+(3*fun_x2)+fun_x3)
print(f"Valor de integral: {sp.N(valor)}\n")

