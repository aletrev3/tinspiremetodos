import math
import sympy as sp 

print("Serie de Taylor")
def derivadas (): #función que calcula las derivadas de f(x)
    funcionO = input("Función\n") #f(x) de usuario
    numder = input ("Número de derivadas\n")
    numder = int(numder) #declaracion de variable como int
    num = 0
    for dfo_dx in range (numder):
        x = sp.symbols('x') #declaración de x como variable simbolica
        der = dfo_dx = sp.diff (funcionO,x) #derivar f(x)
        funcionO = dfo_dx #convertir la derivada en la nueva original para derivadas de mayor grado
        num += 1
        print(f"{num} derivada: {funcionO}\n")
        
        
      
derivadas()


  



