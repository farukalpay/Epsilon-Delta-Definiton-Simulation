Introduction
---

[![Hits](https://hits.sh/github.com/farukalpay/Epsilon-Delta-Definiton-Simulation/tree/main.svg)](https://hits.sh/github.com/farukalpay/Epsilon-Delta-Definiton-Simulation/tree/main/)

$$\
\forall \varepsilon > 0, \exists \delta > 0 : 0 < |x - c| < \delta \Rightarrow |f(x) - L| < \varepsilon
\$$

<p align="middle" width="100%">
This mathematical notation defines the epsilon-delta definition of a limit.
</p>

I have noticed that the majority of students find it challenging to feel this definition, which is crucial for calculus and real analysis. I'll make it easier for you to understand and feel by illustrating it graphically and by writing Python code.

Before we begin, i highly advise you to watch my [Video](https://www.youtube.com/watch?v=qa1pWVE8L0I) to get a better understanding of the subject.

Examples
---
This simulation demonstrates the existence of the limit $\( \lim_{{x \to 2}} f(x) = 4 \)$ for the function $\( f(x) = x^2 \)$. As observed, when $\( L = 4 \)$, the rectangle we form using $\( x + \delta \)$, $\( x - \delta \)$ for $\( x \)$ and $\( L + \epsilon \)$, $\( L - \epsilon \)$ for $\( y \)$, values always contains the red point which is $L\$. This illustrates that for any chosen values of $\( \epsilon > 0\)$ there exist $\( \delta > 0\)$ such that $\( 0 < |f(x) - L| < \epsilon \)$ whenever $\( 0 < |x - c| < \delta \)$ 
![](https://github.com/farukalpay/Epsilon-Delta-Ratio-Simulation/blob/main/images/1.png)

This simulation demonstrates that the limit $\( \lim_{{x \to 2}} f(x) = 5 \)$ does not exist for the function $\( f(x) = x^2 \)$. As observed, when $\( L = 5 \)$, the rectangle we form using $\( x + \delta \)$, $\( x - \delta \)$ for $\( x \)$ and $\( L + \epsilon \)$, $\( L - \epsilon \)$ for $\( y \)$, values does not always contains the red point which is $L\$. This illustrates that there exist $\( \delta > 0\)$ such that if $\( \epsilon > 0\)$ such that if $\( 0 < |f(x) - L| > \epsilon \)$ then $\( 0 < |x - c| > \delta \)$ 
![](https://github.com/farukalpay/Epsilon-Delta-Ratio-Simulation/blob/main/images/2.png)

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
`for delta in delta_values` This loop iterates through the range of delta values defined earlier. For each delta value, it will create a delta-epsilon band around the limit point. `x_range = np.linspace(x_limit - delta, x_limit + delta, 400)` This line creates an array $x_{\text{range}}\$ of x values that define a range around the limit point $x_{\text{limit}}\$ (which is 2 in our code) within the interval $\[x_{\text{limit}} - \delta  ,  x_{\text{limit}} + \delta]\$ This array is used to determine the x values over which the delta-epsilon band will be plotted. $x_{\text{limit}} - \delta\$ represents the lower bound of the interval. It subtracts the delta value from the limit point, creating the starting point of the range. $x_{\text{limit}} + \delta\$ represents the upper bound of the interval. It adds the delta value to the limit point, creating the ending point of the range. `epsilon = max(abs(f(x_range) - f(x_limit)))` This line calculates the maximum difference $\epsilon$ between the function values within the $x_{\text{range}}\$ and the function value at the limit point $x_{\text{limit}}\$ This calculated value of $\epsilon$ represents the vertical range of the delta-epsilon band that we're plotting around the limit point. `if f(x_limit) - epsilon <= f(x_limit) <= f(x_limit) + epsilon` This line checks whether the limit exists or not. According to the Epsilon-Delta definition, $\|f(x) - L| \leq \epsilon\$ can be simplified as $f(x) - \epsilon \leq L \leq f(x) + \epsilon\$ If this inequality holds true, then the limit exists. The color and label variables are assigned based on whether the limit exists or not. `plt.fill_between(x_range, f(x_limit) - epsilon, f(x_limit) + epsilon, color=color, alpha=0.2, label=label)` This line fills the area between $x_{\text{limit}} - \epsilon\$ and $x_{\text{limit}} + \epsilon\$ over the $x_{\text{range}}\$ interval. So, the width of the shaded region corresponds to the width of the interval around the limit point, which is controlled by the value of delta.

```
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Epsilon-Delta Ratio for $f(x) = x^2$')
plt.legend()
plt.grid()
plt.show()
```
This section of code is for adding labels, a title, a legend, and displaying the plot. `plt.xlabel('x')` This sets the label for the x-axis of the plot, indicating what the x-axis represents. `plt.ylabel('f(x)')` This sets the label for the y-axis of the plot, indicating what the y-axis represents. `plt.title('Epsilon-Delta Ratio for $f(x) = x^2$')` This sets the title of the plot. `plt.legend()` This adds a legend to the plot. The legend helps identify different elements on the plot, such as the function curve and the shaded delta-epsilon bands. `plt.grid()` This adds a grid to the plot. `plt.show()` This displays the plot on the screen.
