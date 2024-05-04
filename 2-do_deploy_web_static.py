#!/usr/bin/python3
"""distributes an archive to the web servers"""
from os.path import exists
from fabric.api import put, env, sudo


env.hosts = ['54.236.41.47', '100.25.131.39']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        dir_name = file_name.split(".")[0]
        tmp = f"/tmp/{file_name}"
        ex_dir = f"/data/web_static/releases/{dir_name}/"
    
        put(archive_path, tmp, use_sudo=True)
        sudo(f"mkdir -p {ex_dir}")
        sudo(f"tar -xzf {tmp} -C {ex_dir}")
        sudo(f"rm {tmp}")
    
        dir1 = f"/data/web_static/releases/{dir_name}/web_static/*"
        dir2 = f"/data/web_static/releases/{dir_name}/"

        sudo("mv {} {}".format(dir1, dir2))
        sudo(f"rm -rf /data/web_static/releases/{dir_name}/web_static")
        l1 = f"/data/web_static/releases/{dir_name}/"
        lc = "/data/web_static/current"

        sudo("rm -rf {}".format(lc))
        sudo("ln -s {} {}".format(l1, lc))
        return True
    except:
        return False
