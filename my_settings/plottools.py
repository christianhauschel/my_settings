import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d, Axes3D

import numpy as np


def calc_grid(n: int) -> tuple:
    """
    Calc number of cols/rows for subplots.
    """

    def nearest_square(num):
        num1 = np.floor(np.sqrt(num)) ** 2
        return np.sqrt(num1)

    n_rows = int(nearest_square(n))
    n_cols = n_rows

    while True:
        if n_cols * n_rows < n:
            n_cols += 1
        else:
            break
    return n_rows, n_cols


def set_3daxes_equal(ax: plt.Axes) -> None:
    """
    Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Arguments
    ---------

    ax: a matplotlib axis, e.g., as output from plt.gca().

    References
    ----------

    https://stackoverflow.com/questions/13685386/matplotlib-equal-unit-length-with-equal-aspect-ratio-z-axis-is-not-equal-to
    """

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5 * max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


class Arrow3D(FancyArrowPatch):
    """
    Matplotlib 3D Arrow.

    Example
    -------

    ```python
    a = Arrow3D(
            [x_0, v[0]],
            [y_0, v[1]],
            [z_0, v[2]],
            mutation_scale=20, lw=3, arrowstyle="-|>", color="r"
        )
    ax.add_artist(a)
    ```

    References
    ----------

    https://stackoverflow.com/questions/22867620/putting-arrowheads-on-vectors-in-matplotlibs-3d-plot
    """

    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)
