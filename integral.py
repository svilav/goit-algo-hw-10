import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа


N = 10000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = f(x_random)
integral_mc = (b - a) * np.mean(y_random)


result_quad, error = spi.quad(f, a, b)


x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


print("Інтеграл методом Монте-Карло: ", integral_mc)
print("Інтеграл за допомогою quad: ", result_quad)
print("Абсолютна помилка методу Монте-Карло: ", abs(integral_mc - result_quad))
