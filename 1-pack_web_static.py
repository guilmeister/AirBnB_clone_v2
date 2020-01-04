#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
"""

from fabric.api import *
import datetime


def do_pack():
    """
    return the archive path if the archive has been correctly generated
    """
    date = datetime.datetime.now()
    archive = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(date.year,
                                                            date.month,
                                                            date.day,
                                                            date.hour,
                                                            date.minute,
                                                            date.second)
    local('mkdir -p versions')
    check = local('tar -cvzf {} web_static'.format(archive))
    if check.failed:
        return None
    else:
        return archive
