#!/usr/bin/python3
"""deletes out-of-date archives"""
from fabric.api import env, run, local
env.hosts = ['54.236.41.47', '100.25.131.39']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    if number < 0:
        raise ValueError("number must be non-negative")

    # Get a list of archive files in both locations
    local_archives = local("ls -tr versions/*.tgz | \
        awk '{print $NF}'", capture=True).splitlines()
    remote_archives = run("ls -tr /data/web_static/releases/*.tgz | \
        awk '{print $NF}'", hosts=env.hosts).splitlines()

    # Keep the specified number of most recent archives in each location
    local_to_keep = local_archives[-number:]
    remote_to_keep = remote_archives[-number:]

    # Delete unnecessary local archives
    for archive in local_archives:
        if archive not in local_to_keep:
            run(f"rm versions/{archive}", hosts=env.hosts)

    # Delete unnecessary remote archives
    for archive in remote_archives:
        if archive not in remote_to_keep:
            run(f"rm /data/web_static/releases/{archive}", hosts=env.hosts)
