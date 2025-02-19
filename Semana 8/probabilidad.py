import as:
# Datos proporcionados
lambda_poisson = 15.5  # tasa media de árboles por Ha
k = 20  # número de árboles
e = math.e  # constante de Euler

# Cálculo de la probabilidad de Poisson
probabilidad_poisson = (lambda_poisson**k * math.exp(-lambda_poisson)) / math.factorial(k)
probabilidad_poisson
print(probabilidad_poisson)