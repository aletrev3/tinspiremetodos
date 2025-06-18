import sympy as sp
print("Simpson 1/3 Simple\n")
funcion = input("Ingrese la función a integrar: ")
a = sp.Rational(input("Ingrese el límite inferior (a): "))  
b = sp.Rational(input("Ingrese el límite superior (b): "))
pto_med = (a+b)/2

f_a = sp.sympify(funcion).subs(sp.symbols('x'), a)#sustituir para a
f_b = sp.sympify(funcion).subs(sp.symbols('x'), b)#sustituir para b
f_m = sp.sympify(funcion).subs(sp.symbols('x'), pto_med)#sustituir para m

print(f"Función de a f({a}): {f_a}\nFunción de punto medio f({pto_med}): {f_m}\nFunción de b f({b}): {f_b}\n")

print(f"Fórmula:\n({b}-{a})/6[({f_a})+4*({f_m})+({f_b})]\n")

val_tot = ((b-a)/6)*(f_a+(4*f_m)+f_b) 
print(f"Valor de Integral:\n{val_tot}")