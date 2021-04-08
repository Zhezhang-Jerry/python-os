"""
program: finder.py
Author: Zhe Zhang A01257572 Set B
Date: Apr 8 2021
"""

import os
import sys

def find_all(directories, pattern):
    result = []
    for cwd, dirs, files in os.walk(directories):
        for data in files:
            if pattern in data:
                pathname = os.path.join(cwd,data)
                result.append(pathname)

    return '\n'.join(result)


def main():
    # dirs = sys.argv[1]
    # pattern = sys.argv[2]
    # cmd = sys.argv[3]
    dirs = 'TOPDIR'
    pattern = 'tar'
    cmd = '-f'
    result = ''
    if cmd == '-f':
        result = find_all(dirs, pattern)
    # elif cmd == '-d':
    #     result = find_match(dirs, pattern)
    # elif cmd == '-fd' or cmd == '':
    #     result = match_dirs_files(dirs, pattern)
    print(result)



main()

