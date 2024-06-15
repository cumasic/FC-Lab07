import numpy as np
import matplotlib.pyplot as plt

# Método de la función a integrar
def f(x):
    return (1-x**2)**1.5

# Intervalo de integración
a, b = 0, 1

# Número de puntos aleatorios
N = 1000000

# Genera puntos aleatorios uniformemente distribuidos en [a, b]
x_random = np.random.uniform(a, b, N)

# Evalua la función en los puntos aleatorios
f_random = f(x_random)

# Calcula la integral aproximada
integral_approx = (b - a) * np.mean(f_random)

# Calcula el valor exacto o casi exacto de la integral para la función f(x) 
integral_exact = 0.58904

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
x = np.linspace(a, b, 100)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='$f(x) = (1-x^2)^3/2$')
plt.scatter(x_random, f_random, color='red', s=1, label='Puntos aleatorios')
plt.axhline(y=integral_approx, color='green', linestyle='--', label=f'Integral aproximada = {integral_approx:.5f}')
plt.fill_between(x, 0, y, alpha=0.1)
plt.title('Integración por el Método de Monte Carlo')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()