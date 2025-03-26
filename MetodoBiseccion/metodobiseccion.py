import math
import sympy as sp

print("Método de Bisección\n\n")
funcion = input("Función original =\n")  # f(x) de usuario
neg = input("Valor menor: ")
neg = float(neg)
pos = input("Valor mayor: ")
pos = float(pos)
tolerancia = float(input("toleracia ")) # Definir una tolerancia de error
max_iter = 25  # Número máximo de iteraciones

x = sp.symbols('x')  # Declaración de x como variable simbólica
fun = sp.sympify(funcion)  # Convertir la función de texto a una expresión simbólica

for i in range(max_iter):
    # Evaluamos la función en los extremos del intervalo
    funneg = fun.subs(x, neg)
    funpos = fun.subs(x, pos)

    # Si el producto de las funciones evaluadas en los extremos es negativo, hay raíz en el intervalo
    if funneg * funpos < 0:
        # Calcular el punto medio
        intr = (neg + pos) / 2
        funpm = fun.subs(x, intr)  # Evaluamos la función en el punto medio
        
        # Mostrar el punto medio y su valor
        print(f"Iteración {i+1}: Intervalo = [{neg}, {pos}], \n Punto medio = {intr}, \n f(m) = {funpm}")
        
        # Si el valor de la función en el punto medio es suficientemente cercano a cero, hemos encontrado la raíz
        if abs(funpm) < tolerancia:
            print(f"La raíz es {intr}")
            break
        
        # Actualizar el intervalo según el signo de la función en el punto medio
        if funpm * funneg < 0:
            pos = intr  # La raíz está en el intervalo [neg, intr]
        elif funpm * funpos < 0:
            neg = intr  # La raíz está en el intervalo [intr, pos]
    
    else:
        print("La función no tiene raíz en el intervalo")
        break
   
 


