#!/usr/bin/python3
"""web static pack module"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """fab function"""

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local(f'tar -cvzf versions/{archive} web_static')
    print(f"web_static packed: {archive}")
    if create is not None:
        return archive
    else:
        return None

