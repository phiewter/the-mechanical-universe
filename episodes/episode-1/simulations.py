import numpy as np
from matplotlib import pyplot as plt

def falling_body(t, c=1):
    return c * t**2

t_values = np.linspace(0, 5, 100)
s_values = falling_body(t_values, c=1)

plt.figure(figsize=(8, 6))
plt.plot(t_values, s_values, label=r'$s(t) = c t^2$', color='b')
plt.xlabel('Time (t)')
plt.ylabel('Distance fallen (s)')
plt.title("Galileo's Law of Falling Bodies")
plt.legend()
plt.grid()

plt.show()