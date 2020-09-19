#!/usr/bin/env python3

import subprocess
import os
from multiprocessing import Pool

src = os.path.expanduser("~/data/prod/")
dest = os.path.expanduser("~/data/prod_backup/")

def get_pathlist(folder):
    print(folder)
    pathlist = []

    for root, dirs, files in os.walk(folder):
        path = root[len(folder):]
        print(dirs)
        print(files)
        if dirs != []:
            for d in dirs:
                pathlist.append((path, d))
        for f in files:
            pathlist.append((path, f))

    return pathlist

def backup(path):
    source = os.path.join(src, path[0], path[1])
    destination = os.path.join(dest, path[0])
    subprocess.call(['rsync', '-arq', source, destination])

if __name__ == "__main__":
    src_pathlist = get_pathlist(src)

#    with Pool(len(src_pathlist), maxtasksperchild=1) as pool:
    p = Pool(len(src_pathlist))
    p.map(backup, src_pathlist)
