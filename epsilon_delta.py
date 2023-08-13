import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x ** 2

# Define the limit point
x_limit = 2

# Define a range of delta values
delta_values = np.linspace(0.1, 2, 10)

# Plot the function
x = np.linspace(1, 3, 400)
plt.plot(x, f(x), label='f(x) = x^2')

# Plot the delta-epsilon band
for delta in delta_values:
    x_range = np.linspace(x_limit - delta, x_limit + delta, 400)
    epsilon = max(abs(f(x_range) - f(x_limit)))  # Calculate epsilon based on function behavior
    
    # Check if the limit point is inside the epsilon-delta band
    if f(x_limit) - epsilon <= 5 <= f(x_limit) + epsilon:
        color = 'grey'
        label = f'Limit Exists for Δ = {delta:.2f}'
    else:
        color = 'red'
        label = f'Limit Does Not Exist for Δ = {delta:.2f}'
    
    plt.fill_between(x_range, f(x_limit) - epsilon, f(x_limit) + epsilon, color=color, alpha=0.2, label=label)

# Highlight the limit point
plt.plot(x_limit, 5, 'ro', label=f'x = {x_limit}, L = {f(x_limit)}')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Epsilon-Delta Ratio for $f(x) = x^2$')
plt.legend()

# Show the plot
plt.grid()
plt.show()
