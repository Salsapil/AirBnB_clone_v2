#!/usr/bin/python3
"""distributes an archive to the web servers"""
from os.path import exists
from fabric.api import env, put, run, sudo


# Define web server hosts
env.hosts = ['54.236.41.47', '100.25.131.39']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        # Extract filename and directory for deployment
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        deploy_dir = f"/data/web_static/releases/{no_ext}"

        # Upload archive to temporary location
        put(archive_path, f"/tmp/{filename}")

        # Create release directory if it doesn't exist
        sudo(f"mkdir -p {deploy_dir}")

        # Uncompress archive to release directory
        sudo(f"tar -xzf /tmp/{filename} -C {deploy_dir}")

        # Remove uploaded archive
        run(f"rm /tmp/{filename}")

        # Move extracted files (avoiding nested structure)
        source_dir = f"/data/web_static/releases/{no_ext}/web_static"
        destination_dir = f"/data/web_static/releases/{no_ext}"
        run(f"mv {source_dir}/* {destination_dir}/")

        # Remove empty web_static directory from extracted archive
        sudo(f"rm -rf /data/web_static/releases/{no_ext}/web_static")

        # Remove existing symbolic link
        sudo(f"rm -rf /data/web_static/current")

        # Create new symbolic link to deployed version
        sudo(f"ln -s {deploy_dir} /data/web_static/current")

        return True

    except:
        return False
