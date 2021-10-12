from my_settings import plt 

import numpy as np

x = np.linspace(0, 1, 100)
y = x ** 2

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(xlabel="$x$", ylabel=r"$y = \frac{1}{2}mc^2$", title="Title")
plt.show()