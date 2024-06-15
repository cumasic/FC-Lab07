import numpy as np
import matplotlib.pyplot as plt

# Método de la función a integrar
def f(x):
    return x*((1+x**2)**-2)

# Cambio de variable para el intervalo [0, ∞) a [0, 1)
def Cambio_Variable_f(u):
    x = u / (1 - u)
    return f(x) * (1 / (1 - u)**2)

# Número de puntos aleatorios
N = 1000000

# Genera puntos aleatorios uniformemente distribuidos en [0, 1)
u_random = np.random.uniform(0, 1, N)

# Evalua la función con cambio de variable en los puntos aleatorios
f_random = Cambio_Variable_f(u_random)

# Calcula la integral aproximada
integral_approx = np.mean(f_random)

# Calcula el valor exacto de la integral para la función f(x) 
integral_exact = 0.5

# Calcula el error absoluto
error_abs = abs(integral_exact - integral_approx)

# Calcula el error relativo
error_rel = (error_abs / integral_exact) * 100

# Calcula el error de MonteCarlo
error_MC = 1 / N**0.5

# Imprime resultados
print(f'Integral aproximada: {integral_approx}')
print(f'Integral exacta: {integral_exact}')
print(f'Error de MonteCarlo: {error_MC}')
print(f'Error relativo: {error_rel:.5f}%')

# Gráfico representativo
x = np.linspace(0, 5, 100)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='$f(x) = x*((1+x^2)^-2)$')
plt.scatter(u_random / (1 - u_random), f_random, color='red', s=1, label='Puntos aleatorios')
plt.axhline(y=integral_approx, color='green', linestyle='--', label=f'Integral aproximada = {integral_approx:.5f}')
plt.fill_between(x, 0, y, alpha=0.1)
plt.title('Integración por el Método de Monte Carlo con Intervalo [0, ∞)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()