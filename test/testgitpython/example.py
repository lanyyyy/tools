__author__ = 'lanyyyy'
#-*- coding: utf-8 -*-
#!/usr/bin/python

import git
import os
import shutil

def main():
    # download repo
    git_url = "https://github.com/tox-dev/tox.git"
    tox_path = "/tmp/tox_tmp"
    if os.path.exists(tox_path):
        shutil.rmtree(tox_path)
    git.Repo.clone_from(git_url, tox_path )

    # generate repo
    pass


if __name__ == "__main__":
    main()
    pass
