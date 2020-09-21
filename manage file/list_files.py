#!/usr/bin/env python3
import os
src = "C:/Users/Chris/python-workspace"

def get_pathlist(folder):
    print(folder)
    pathlist = []

    for root, dirs, files in os.walk(folder):
        path = root[len(folder):]        
        if dirs != []:
            for d in dirs:                
                pathlist.append((path, d))
        for f in files:            
            pathlist.append((path, f))

    return pathlist


if __name__ == "__main__":
    src_pathlist = get_pathlist(src)
    for item in src_pathlist:
        print(item)
