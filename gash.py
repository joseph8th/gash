#!/usr/bin/env python3

import subprocess
from collections import OrderedDict
from settings import projects

def scp_script(environ_cfg):
    cmd = "scp "
    if environ_cfg['cert']:
        cmd += "-i {cert} ".format(cert=environ_cfg['cert'])

    cmd += 'getbranch.sh {user}@{host}: > /dev/null'.format(
        user = environ_cfg['user'],
        host = environ_cfg['host']
    )

    # TODO
    #print(cmd)
    #cmd_l = cmd.split()
    return subprocess.call(cmd, shell=True)


def ssh_get_branch(environ_cfg):
    cmd = "ssh "
    if environ_cfg['cert']:
        cmd += "-i {cert} ".format(cert=environ_cfg['cert'])

    cmd += '{user}@{host} "/home/{user}/getbranch.sh {path}"'.format(
        user = environ_cfg['user'],
        host = environ_cfg['host'],
        path = environ_cfg['path']
    )

    # TODO
    #print(cmd)

    branch = subprocess.check_output(cmd, universal_newlines=True, shell=True)
    return branch.strip()


def get_project_branches(force_scp=False):
    project_branches = {}
    for project, project_cfg in projects.items():
        if not project_cfg:
            continue

        project_branches[project] = {}
        for environ, environ_cfg in project_cfg.items():
            if not environ_cfg:
                continue

            # Upload the getbranch.sh script
            if force_scp:
                errno = scp_script(environ_cfg)

            project_branches[project][environ] = ssh_get_branch(environ_cfg)

    return OrderedDict(sorted(project_branches.items(), key=lambda t: t[0]))
    #return project_branches


if __name__ == '__main__':
    project_branches = get_project_branches()

    # TODO
    print(project_branches)
