import sympy as sp
import numpy as np 
import tabulate
print("Rgresion Lineal Simple\n\n")
numval = int(input("Número de valores en columna (n): "))
x_arr = []
y_arr = []
xcuadrado_arr = []
ycuadrado_arr = []
xy_arr = []
xyarr_sum = []
y_arrsum = []
x_arrsum = []
xcuadrado_arrsum = []
ycuadrado_arrsum = []
j_arr = []
j = 0
for i in range(numval): 
    x = float(input(f"Valor de x{i+1}: "))
    xcua = x**2
    xcuadrado_arr.append(xcua)
    xcuadrado_arrsum.append(xcua)
    x_arr.append(x)
    x_arrsum.append(x)
for i in range(numval): 
    y = float(input(f"Valor de y{i+1}: "))
    ycua = y**2
    ycuadrado_arr.append(ycua)
    ycuadrado_arrsum.append(ycua)
    y_arr.append(y)
    y_arrsum.append(y)
for i in range(numval): 
    xy = x_arr[i] * y_arr[i]
    xy_arr.append(xy)
    xyarr_sum.append(xy)

    j += 1
    j_arr.append(j)
sumx = sum(x_arr)
sumy = sum(y_arr)
sumxcuad = sum(xcuadrado_arr)
sumycuad = sum(ycuadrado_arr)
sumxy = sum(xy_arr)

rows = []

for i in range(len(xyarr_sum)):
    
    rows.append([j_arr[i], x_arrsum[i], y_arrsum[i], xcuadrado_arrsum[i], ycuadrado_arrsum[i], xyarr_sum[i]])
    

table = tabulate.tabulate(rows, headers=["n", "Valores de x", "Valores de y", "Valores de x^2", "Valores de y^2", "Valores de xy"], tablefmt="fancy_grid")
print(table)

tablesum = [sumx, sumy, sumxcuad, sumycuad, sumxy]
tabledos = tabulate .tabulate([tablesum], headers=["Sumatoria de x", "Sumatoria de y", "Sumatoria de x^2", "Sumatoria de y^2", "Sumatoria de xy"], tablefmt="grid")
print(tabledos)  

a = (numval * sum(xy_arr) - sum(x_arr) * sum(y_arr)) / (numval * sum(xcuadrado_arr) - sum(x_arr)**2)
b = (sum(y_arr) - a * sum(x_arr)) / numval
r = (numval * sum(xy_arr) - sum(x_arr) * sum(y_arr)) / ((numval * sum(xcuadrado_arr) - sum(x_arr)**2) * (numval * sum(ycuadrado_arr) - sum(y_arr)**2))**0.5
print(f"Valor de a: {round(a,4)}")
print(f"Valor de b: {round (b,4)}")
print(f"Valor de y = a + bx: {round(a,4)} + {round(b,4)}x")
print(f"Valor de r: {round(r,4)}")


