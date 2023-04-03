from subprocess import PIPE, run
import shlex
import subprocess


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
