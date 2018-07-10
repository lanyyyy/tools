__author__ = 'lanyyyy'
#-*- coding: utf-8 -*-
#!/usr/bin/python

import git
import os

def main():
    # download repo
    git_url = "https://github.com/tox-dev/tox.git"
    git.Repo.clone_from(git_url, os.getcwd())
    pass


if __name__ == "__main__":
    main()
    pass
