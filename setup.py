from setuptools import setup

setup(
      name="my_settings", 
      version="0.2",
      description="Common settings/functions for plots and other stuff...", 
      packages=["my_settings"], 
      author="Christian Hauschel", 
      zip_safe=False,
      install_requires=[
          "matplotlib>=3.4.0,<3.6",
          "numpy",
          "seaborn",
          "pandas",
          "rich",
          "proplot"
      ]	
)

