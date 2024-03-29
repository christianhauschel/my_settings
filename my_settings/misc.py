from subprocess import PIPE, run, CalledProcessError
import shlex
import subprocess
from subprocess import run, check_output

def run_command(command, **kwargs):
    return run(shlex.split(command), **kwargs)


def convert_path_win2wsl(windows_path):
    windows_path = str(windows_path)

    windows_path = windows_path.replace("\\", "/")
    # if ':' in windows_path:
    #     # convert the drive letter to lowercase
    #     drive_letter = windows_path[0].lower()
    #     windows_path = drive_letter + windows_path[1:]

    # Use the 'wslpath' command to convert the Windows path to a Unix path on WSL
    try:
        process = subprocess.run(
            ["wsl", "wslpath", "-u", windows_path], stdout=subprocess.PIPE
        )
    except:
        raise Warning("Please install wslpath (https://github.com/laurent22/wslpath)!")

    # Get the converted Unix path from the command's output
    unix_path = process.stdout.decode().strip()
    return unix_path


def check_wsl_mount(device_path: str, shutdown: bool = True):
    """Checks if the given path is mounted on WSL.
    Parameters
    ----------
    device_path : str
    shutdown : bool
        True: If not mounted, WSL gets shut down.
    Returns
    -------
    bool
        mounted or not mounted
    """

    # Run the `mount` command and capture its output
    try:
        output = check_output(["wsl", "mount"], universal_newlines=True)
        if device_path in output:
            return True
    except CalledProcessError as e:
        print(e)

    if shutdown:
        run(["wsl", "--shutdown"])
    return False