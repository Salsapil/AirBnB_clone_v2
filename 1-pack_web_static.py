#!/usr/bin/python3
"""web static pack module"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    try:
        now = datetime.now()
        filename = f"web_static_{now.strftime('%Y%m%d%H%M%S')}.tgz"
        versions_dir = "versions"
        os.makedirs(versions_dir, exist_ok=True)
        archive_path = os.path.join(versions_dir, filename)
        local(f"tar -cvzf {archive_path} web_static")

        print(f"web_static packed: {archive_path}")
        return archive_path

    except:
        return None
