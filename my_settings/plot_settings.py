# ==============================================================================
# Plot Settings
# ==============================================================================

import matplotlib.pyplot as plt
# import matplotlib
# import seaborn as sns
# from platform import system

# ---------------------------------------
# Themes
# ---------------------------------------

# matplotlib.rc_file_defaults() # reset
# sns.set()

# Styles
    # ['seaborn-dark',
    #  'seaborn-darkgrid',
    #  'seaborn-ticks',
    #  'fivethirtyeight',
    #  'seaborn-whitegrid',
    #  'classic',
    #  '_classic_test',
    #  'seaborn-talk',
    #  'seaborn-dark-palette',
    #  'seaborn-bright',
    #  'seaborn-pastel',
    #  'grayscale',
    #  'seaborn-notebook',
    #  'ggplot',
    #  'seaborn-colorblind',
    #  'seaborn-muted',
    #  'seaborn',
    #  'seaborn-paper',
    #  'bmh',
    #  'seaborn-white',
    #  'dark_background',
    #  'seaborn-poster',
    #  'seaborn-deep']

# Size (Context)
# sns.set_context("notebook")
    # paper
    # notebook
    # talk
    # poster

# Style
# sns.set_style("white")


# ---------------------------------------
# Fonts 
# ---------------------------------------


# plt.rcParams.update({
#     "text.usetex": False,
#     "font.family": "sans",
# })

# TeX, Serif
# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "serif"
# })

# # Arial, No TeX
# plt.rcParams.update({
#     "text.usetex": False,
#     "font.family": "sans",
#     "font.sans-serif": "Arial",
# })

# # TeX, Palatino
# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "serif",
#     "font.serif": ["Palatino"],
# })


# ==============================================================================
# Common Modules
# ==============================================================================

import pandas as pd
import numpy as np
import proplot as pplt


pplt.rc.cycle = "FlatUI"