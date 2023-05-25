# %%  Modules


from subprocess import PIPE, run, CalledProcessError
import shlex
import subprocess
from subprocess import run, check_output
from my_settings import check_wsl_mount

# %%

print(check_wsl_mount("/mnt/a"))


# %% RUN ALL