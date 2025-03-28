import math
math_functions = {name: getattr(math, name) for name in dir(math) if not name.startswith("__")} #importar expresiones 
print("x= exp(8*x) Para e^(8x)\nx= cos(x) Para coseno de x\nx= log(x) Para logaritmo natural (ln x)\nx= sin(x) + x**2 Para sen(x) + x^2")
print("Método de Punto Fijo")

funini = input("Función inicial\nx= ")  # función inicial por usuario
valini = float(input("Valor inicial de x\n"))  # valor inicial de x
errabs = float(input("Error absoluto a obtener\n"))  # error absoluto pedido
i = 0
errorfinr = 100 #valor inicial para comparar errores
errornu = 100 #valor inicial para comparar errores
while errorfinr > errabs: #se repite mientras el error obtenido sea ,ayor que el necesario
    funcion = eval(funini, {"x": valini, **math_functions})  # Evaluar la función con todas las funciones de math    print(funcion)
    i += 1
    print(f"Para la iteración {i} , x= {funcion}")
    # asegurar que errorfin es numérico
    errorfin = abs((funcion - valini) / funcion) #formula para error abs
    errorfinr = round(errorfin, 4)  # redondear el error a 4 decimales
    print(f"El error es de {errorfinr}")
    valini = funcion  # el resultado se convierte en el nuevo valor inicial
    if errorfinr > errornu: #si los valore aumentan, se detiene el ciclo
        print(f"Los valores convergen")
        break
    errornu = errorfinr #convertir el error en el nuevo error para comparar
    print(errornu)
