import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 2

x_limit = 2

delta_values = np.linspace(0.1, 2, 200)

x = np.linspace(1, 3, 400)
plt.plot(x, f(x), label='f(x) = x^2')

for delta in delta_values:
    epsilon = delta ** 2
    plt.fill_between([x_limit - delta, x_limit + delta], [0, 0], [epsilon, epsilon], color='gray', alpha=0.2)

plt.plot(x_limit, x_limit ** 2, 'ro', label=f'x = {x_limit}')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Epsilon Delta Ratio for $f(x) = x^2$')
plt.legend()

plt.grid()
plt.show()
