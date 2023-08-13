# Epsilon-Delta-Definiton-Simulation
This project provides a visual simulation of the epsilon-delta ratio. Its purpose is to illustrate how the values of a function approach a specific limit point. 

![](https://github.com/farukalpay/Epsilon-Delta-Ratio-Simulation/blob/main/image.png)

Introduction
---
$$\
\forall \varepsilon > 0 \quad \exists \delta > 0 \quad 0 < |x - c| < \delta \Rightarrow |f(x) - L| < \varepsilon.
\$$

<p align="middle" width="100%">
This mathematical notation defines the epsilon-delta definition of a limit.
</p>

I have noticed that the majority of students find it challenging to feel this definition, which is crucial for calculus and real analysis. I'll make it easier for you to understand and feel by illustrating it graphically and by writing Python code.

Before we begin, i highly advise you to watch my [Video](https://www.youtube.com/watch?v=qa1pWVE8L0I) to get a better understanding of the subject.

Code Explanation
---

```
import numpy as np
import matplotlib.pyplot as plt
```
Import required libraries to perform numerical, mathematical operations and draw the graph.

```
def f(x):
    return x ** 2
```
When we call the definition f(x), it squares the value of x.

```
x_limit = 2
```
Define the limit point

```
delta_values = np.linspace(0.1, 2, 10)
```
It assigns delta values. Here, we want 10 numbers between 0.1 and 2 to be assigned as delta values. Actually, 2 is a large value for delta. For such a large delta value, the error rate will be high. Furthermore, if you find any delta value that doesn't satisfy the Epsilon-Delta definition, the limit does not exist.

```
x = np.linspace(1, 3, 400)
plt.plot(x, f(x), label='f(x) = x^2')
```
`x = np.linspace(1, 3, 400)` This line creates an array of x values ranging from 1 to 3, consisting of 400 evenly spaced points. This array of x values will be used to plot the function. `plt.plot(x, f(x), label='f(x) = x^2')` The line plots the function $f(x) = x^2\$ using the generated x values and adds a label to identify the function in the plot.

```
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
```
`for delta in delta_values` This loop iterates through the range of delta values defined earlier. For each delta value, it will create a delta-epsilon band around the limit point. `x_range = np.linspace(x_limit - delta, x_limit + delta, 400)` This line creates an array $x_{\text{range}}\$ of x values that define a range around the limit point $x_{\text{limit}}\$ (which is 2 in our code) within the interval $\[x_{\text{limit}} - \delta  ,  x_{\text{limit}} + \delta]\$ This array is used to determine the x values over which the delta-epsilon band will be plotted. $x_{\text{limit}} - \delta\$ represents the lower bound of the interval. It subtracts the delta value from the limit point, creating the starting point of the range. $x_{\text{limit}} + \delta\$ represents the upper bound of the interval. It adds the delta value to the limit point, creating the ending point of the range. `epsilon = max(abs(f(x_range) - f(x_limit)))` This line calculates the maximum difference $\epsilon$ between the function values within the $x_{\text{range}}\$ and the function value at the limit point $x_{\text{limit}}\$ This calculated value of $\epsilon$ represents the vertical range of the delta-epsilon band that we're plotting around the limit point.
