import math
import sympy as sp

print ("Serie de McLaurin\n\n")
print("ST=f(0)+(f'(0)x)+(f''(0)x^2)/2!+(f'''(0)x^3)/3!+...+f^n(0)x^n/n!\n\n")
def derivadas():  # función que calcula las derivadas de f(x)
    funcionO = input("Función\n")  # f(x) de usuario
    numder = input("Número de derivadas\n")
    numder = int(numder)  # declaracion de variable como int
    num = 0
    st = []
    div = sp.symbols('div')
    fact = sp.factorial(div)
    numfac = 0
    for dfo_dx in range(numder):
        x = sp.symbols('x')  # declaración de x como variable simbolica
        der = dfo_dx = sp.diff(funcionO, x)  # derivar f(x)
        numfac += 1
        divfact = fact.subs(div, numfac)
        facfinal = divfact
        derres = dfo_dx.subs(x, 0)
        derredres = round(derres, 4)
        cfact = derredres / divfact
        cfactr = round(cfact, 4)
        st.append(f"(({cfactr})((x)^{num+1}))")
        print(f"{num +1} derivada resuelta = {derredres}")
        funcionO = dfo_dx  # convertir la derivada en la nueva original para derivadas de mayor grado 
        num += 1
        print(f"{num} derivada con variable: {funcionO}\n")

    # for stdiv in range (numder):
     #   stdiv += 1
      #  std.append(f"ST= {stdiv}")
    print(f" + ".join(st))


derivadas()