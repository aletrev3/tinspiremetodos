import sympy as sp 

print("Integrales definidas múltiples\n")
funcion = input("Ingresar la función a integrar: ")
x = sp.Symbol('x')
y = sp.Symbol('y')
z = sp.Symbol('z')
s = sp.Symbol('s')
y = 'y'
volv = y
while volv == 'y':
    op = str(input("Para que variable vas a integrar?\nx\ny\nz\ns\n"))

    if op == 'x':
        a = sp.Rational(input("Límite inferior: "))
        b = sp.Rational(input("Límite superior: "))
        integral = sp.integrate(funcion,(x, a, b))
        print(f"Integral resultado: {integral}")
    elif op == 'y':
        a = sp.Rational(input("Límite inferior: "))
        b = sp.Rational(input("Límite superior: "))
        integral = sp.integrate(funcion,(y, a, b))
        print(f"Integral resultado {integral}")
    elif op == 'z':
        a = sp.Rational(input("Límite inferior: "))
        b = sp.Rational(input("Límite superior: "))
        integral = sp.integrate(funcion,(z, a, b))
        print(f"Integral resultado {integral}")
    elif op == 's':
        a = sp.Rational(input("Límite inferior: "))
        b = sp.Rational(input("Límite superior: "))
        integral = sp.integrate(funcion,(s, a, b))
        print(f"Integral resultado {integral}")
    funcion = integral
    volv = input("Integrar resultado para otra variable?\ny/n\n")