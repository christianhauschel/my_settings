# %% Modules

from my_settings import plt, pretty_print, calc_grid, pplt, print, pd

import numpy as np


# %%

x = np.linspace(0, 1, 100)
y = x ** 2

fig, ax = pplt.subplots(nrows=2, ncols=2, space=10, refwidth="20em")
ax[0].plot(x, y, label="1")
ax[0].plot(x, 2*y, label="2")
ax[1].plot(x, 3*y, label="3")
ax[1].plot(x, 4*y, label="4")
ax.format(
    abc='A.', 
    abcloc='ul',
    lltitle="lltitle",
    suptitle="Suptitle",
    xlabel="$x$", 
    ylabel=r"$y = \frac{1}{2}mc^2$", 
    title="Title"
)
ax.legend(ncols=1, location="upper center")
pplt.show()

# %% Pretty Print

pretty_print("Section", "section")
pretty_print("Subsection", "subsection")
pretty_print("Subsubsection", "subsubsection")
print("Test: 123")


# %% Calc Grid

print(calc_grid(21))
print(calc_grid(14))
print(calc_grid(4))
print(calc_grid(2))
print(calc_grid(16))

# %%