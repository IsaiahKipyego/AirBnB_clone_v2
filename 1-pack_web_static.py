#!/usr/bin/python3
""" generates a .tgz archive from web_static folder """
from fabric.operations import local
from datetime import datetime
from os import path


def do_pack():
    """
    compresses a file and creates a directory if missing
    """
    # check if directory is present
    if not path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    # create the name of file with current time
    location = 'versions/web_static_{}.tgz'.format(
        datetime.utcnow().strftime("%Y%m%d%H%M%S"))

    # compress the file
    if local("tar -cvzf {} web_static".format(location)).failed:
        return None
    return location
