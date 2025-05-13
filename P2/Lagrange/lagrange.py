def lagrange_interpolation():
    n = int(input("¿Cuántas 'n' vas a ingresar? "))
    
    xs = []
    ys = []
    
    for i in range(n):
        x = float(input(f"Ingrese x{i}: "))
        y = float(input(f"Ingrese f(x{i}): "))
        xs.append(x)
        ys.append(y)

    x_eval = float(input("\n¿Para qué valor de f(x) deseas evaluar el polinomio? "))

    print("\n---- CÁLCULO DE LOS POLINOMIOS BASE L_i(x) ----\n")
    L_values = []

    for i in range(n):
        numerator_terms = []
        denominator_terms = []  
        num_product = 1
        den_product = 1

        for j in range(n):
            if i != j:
                num = x_eval - xs[j]
                den = xs[i] - xs[j]
                numerator_terms.append(f"({x_eval} - {xs[j]})")
                denominator_terms.append(f"({xs[i]} - {xs[j]})")
                num_product *= num
                den_product *= den

        print(f"L{i}({x_eval}) = {' * '.join(numerator_terms)} / {' * '.join(denominator_terms)}")
        print(f"         = ({num_product}) / ({den_product}) = {num_product / den_product:.6f}\n")

        L_values.append(num_product / den_product)

    print("---- CONSTRUCCIÓN DEL POLINOMIO ----\n")
    terms = []
    result = 0
    for i in range(n):
        term = ys[i] * L_values[i]
        terms.append(f"{ys[i]} * L{i}({x_eval})")
        print(f"{ys[i]} * {L_values[i]:.6f} = {term:.6f}")
        result += term

    print("\nPolinomio evaluado:")
    print("P(x) =", " + ".join(terms))
    print(f"\nResultado final: P({x_eval}) = {result:.6f}")

# Ejecutar el programa
lagrange_interpolation()
