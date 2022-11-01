from setuptools import setup

setup(
      name="my_settings", 
      version="0.2",
      description="Common settings/functions for plots and other stuff...", 
      packages=["my_settings"], 
      author="Christian Hauschel", 
      zip_safe=False,
      install_requires=[
          "matplotlib==3.4.0",
          "numpy>=1.21.2",
          "seaborn>=0.11.2",
          "pandas>=1.3.3",
          "rich>=10.12.0",
          "proplot>=0.9.3"
      ]	
)

