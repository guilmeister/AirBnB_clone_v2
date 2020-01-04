#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
"""

from fabric.api import *
import datetime
import os

env.hosts = ['35.231.179.64', '34.73.152.228']


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


def do_deploy(archive_path):
    """
    script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers
    """
    status = 0
    if not os.path.isfile(archive_path):
        return False
    upload_status = put(archive_path, '/tmp/')
    if upload_status.failed:
        status = status + 1
    no_extn = archive_path.replace('.tgz', '')
    no_extn = no_exten.replace('versions/', '')
    run_mkdir = run('mkdir -p /data/web_static/releases/{}/'
                    .format(no_extn))
    if run_mkdir.failed:
        status = status + 1
    run_tar = run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
                  .format(no_extn, no_extn))
    if run_tar.failed:
        status = status + 1
    run_del = run('rm /tmp/{}'.format(no_extn))
    if run_del.failed:
        status = status + 1
    run_mv = run('mv /data/web_static/releases/{}/web_static/*'
                 .format(no_extn) + ' /data/web_static/releases/{}/'
                 .format(no_extn))
    if run_mov.failed:
        status = status + 1
    run_rm1 = run('rm -rf /data/web_static/releases/{}/web_static'
                  .format(no_extn))
    if run_rm1.failed:
        status = status + 1
    run_rm2 = run('rm -rf /data/web_static/current')
    if run_rm2.failed:
        status = status + 1
    run_ln = run('ln -s /data/web_static/releases/{}/'.format(no_extn) +
                 ' /data/web_static/current')
    if run_ln.failed:
        status = status + 1
    if status == 0:
        return True
    else:
        return False


def deploy():
    """
    script (based on the file 2-do_deploy_web_static.py) that creates and
    distributes an archive to your web servers
    """
    status = do_pack()
    if status is None:
        return False
    else:
        return do_deploy(status)
