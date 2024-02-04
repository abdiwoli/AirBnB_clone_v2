#!/usr/bin/python3

from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Compresses the contents of the web_static folder into a .tgz archive.
    """
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_filename = "versions/web_static_{}.tgz".format(timestamp)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_filename))
        return archive_filename
    except Exception as e:
        return None
