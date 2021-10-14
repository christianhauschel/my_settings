from my_settings import plt, pretty_print, calc_grid

import numpy as np

x = np.linspace(0, 1, 100)
y = x ** 2

# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set(xlabel="$x$", ylabel=r"$y = \frac{1}{2}mc^2$", title="Title")
# plt.show()


pretty_print("Section", "section")
pretty_print("Subsection", "subsection")
pretty_print("Subsubsection", "subsubsection")
print("Test")


print(calc_grid(21))
print(calc_grid(14))
print(calc_grid(4))
print(calc_grid(2))
print(calc_grid(16))