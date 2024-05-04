#!/usr/bin/python3
"""do clean module """
import os
from fabric.api import env, sudo

env.hosts = ["34.201.165.130", "34.224.62.173"]


def do_clean(number=0):
    """do clean function"""

    arch_count = int(number)

    if arch_count == 0 or arch_count == 1:
        arch_count = 1

    files = [
        os.path.join("versions", f)
        for f in os.listdir("versions")
        if os.path.isfile(os.path.join("versions", f))
    ]
    remote_files = [
        os.path.join("versions", f)
        for f in os.listdir("versions")
        if os.path.isfile(os.path.join("/data/web_static/releases", f))
    ]
    files.sort(key=os.path.getmtime, reverse=True)
    files_to_remove = files[arch_count:]
    for file in remote_files:

        sudo("rm {}".format(file))

    for file in files_to_remove:
        os.remove(file)
