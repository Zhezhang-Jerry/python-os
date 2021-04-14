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
        for data in dirs:
            if pattern in data:
                if os.path.isfile(data) is True:
                    pathname = '[F] ' + os.path.join(cwd,data)
                # else:
                #     pathname = '[D] ' + os.path.join(cwd,data)
                    result.append(pathname)


    return '\n'.join(result)


def find_match(directories, pattern):
    result = []
    for cwd, dirs, files in os.walk(directories):
        for data in dirs:
            if pattern in data:
                if os.path.isdir(data) is True:
                    pathname = '[D] ' + os.path.join(cwd,data)
                    result.append(pathname)
            else:
                result = []
    
    return '\n'.join(result)


def main():
    try:
        dirs = sys.argv[1]
        pattern = sys.argv[2]
        cmd = sys.argv[3]
        if cmd not in ['-d', '-f', '-fd', ' ']:
            raise ValueError(f'Invalid option: {cmd}')
        if cmd == '-f':
            result = find_all(dirs, pattern)
        elif cmd == '-d':
            result = find_match(dirs, pattern)
        # elif cmd == '-fd' or cmd == '':
        #     result = match_dirs_files(dirs, pattern)
        else:
            print()
        print(result)
    except ValueError as excpt:
        print(excpt)


main()

