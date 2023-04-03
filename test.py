# %% Modules

from my_settings import *
import numpy as np

# %% Convert Win to WSL Path

# pretty_print("Section: A console renderable that draws a border around its contents.", "section")

# path_win = r"C:\\Users"
# print(path_win, "-->", convert_path_win2wsl(path_win))

# path_win = r"A:\\Code"
# print(path_win, "-->", convert_path_win2wsl(path_win))


# pretty_print("Subsection: A console renderable that draws a border around its contents.", "subsection")


# pretty_print("Subsubsection", "subsubsection")

# %% Test Logging


logger = logger_custom(__name__, fname="out/test.log")
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
logger.exception("This is an exception message.")

# %% 

try:
    a = 3
    raise Exception("Test") 
except Exception as e:
    print_exception()


# %%

# x = np.linspace(0, 1, 100)
# y = x ** 2

# fig, ax = pplt.subplots(nrows=2, ncols=2, space=4, refwidth="20em")
# ax[0].plot(x, y, label="1")
# ax[0].plot(x, 2*y, label="2")
# ax[1].plot(x, 3*y, label="3")
# ax[1].plot(x, 4*y, label="4")
# ax.format(
#     abc='A.', 
#     abcloc='ul',
#     lltitle="lltitle",
#     suptitle="Suptitle",
#     xlabel="$x$", 
#     ylabel=r"$y = \frac{1}{2}mc^2$", 
#     title="Title"
# )
# ax.legend(ncols=1, location="upper center")
# pplt.show()

# # %% Pretty Print

# pretty_print("Section", "section")
# pretty_print("Subsection", "subsection")
# pretty_print("Subsubsection", "subsubsection")
# print("Test: 123")


# # %% Calc Grid

# print(calc_grid(21))
# print(calc_grid(14))
# print(calc_grid(4))
# print(calc_grid(2))
# print(calc_grid(16))

# # %%