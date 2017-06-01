#!/usr/bin/env python3

import shlex, subprocess
from collections import OrderedDict
from settings import projects

def scp_script(environ_cfg):
    cmd = "scp "
    if environ_cfg['cert']:
        cmd += "-i {cert} ".format(cert=environ_cfg['cert'])

    cmd += '-o ConnectTimeout=30 getbranch.sh {user}@{host}: > /dev/null'.format(
        user = environ_cfg['user'],
        host = environ_cfg['host']
    )

    #cmd_l = shlex.split(cmd)

    # TODO
    print(cmd)

    return subprocess.call(cmd, timeout=30, shell=True)


def ssh_get_branch(environ_cfg):
    cmd = "ssh "
    if environ_cfg['cert']:
        cmd += "-i {cert} ".format(cert=environ_cfg['cert'])

    cmd += '-o ConnectTimeout=30 {user}@{host} \"/home/{user}/getbranch.sh {path}\"'.format(
        user = environ_cfg['user'],
        host = environ_cfg['host'],
        path = environ_cfg['path']
    )
    cmd_l = shlex.split(cmd)

    # TODO
    print(cmd_l)

    branch = subprocess.check_output(cmd_l, universal_newlines=True, timeout=30)
    return branch.strip()


def get_project_branches(force_scp=True):
    project_branches = {}
    for project, project_cfg in projects.items():
        if not project_cfg:
            continue

        project_branches[project] = {}
        for environ, environ_cfg in project_cfg.items():
            if not environ_cfg:
                continue

            try:
                # Upload the getbranch.sh script
                if force_scp:
                    errno = scp_script(environ_cfg)
                project_branches[project][environ] = ssh_get_branch(environ_cfg)

            except subprocess.TimeoutExpired:
                project_branches[project][environ] = 'TIMEOUT'

    return OrderedDict(sorted(project_branches.items(), key=lambda t: t[0]))


if __name__ == '__main__':
    project_branches = get_project_branches()

    # TODO
    print(project_branches)
