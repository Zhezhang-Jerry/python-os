"""
program: finder.py
Author: Zhe Zhang A01257572 Set B
Date: Apr 14 2021
"""

import os
import sys

def get_path(dirs):
    """ Use the input directory to store all files and folders into a path_list """
    path_list = []
    detail_name = ""

    for content in os.walk(dirs):
        for detail in content:
            if dirs not in detail:
                details = (detail_name.join(detail))
                path = os.path.join(content[0], details)
                if os.path.isfile(path):
                    path_list.append(f'[F] {path}')
                if os.path.isdir(path):
                    path_list.append(f'[D] {path}')
    
    return path_list


def find_match_files(dlist, pattern):
    """ find files that includes the pattern """
    result = [path_name for path_name in dlist if pattern in path_name and path_name[1] == 'F']

    return '\n'.join(result)


def find_match_dirs(dlist, pattern):
    """ find directories that includes the pattern """
    result = [path_name for path_name in dlist if pattern in path_name and path_name[1] == 'D']

    return '\n'.join(result)


def find_all(dlist, pattern):
    """ find all files and directories that includes the pattern """
    result = [path_name for path_name in dlist if pattern in path_name]

    return '\n'.join(result)


def main():
    """ Main function // use nested try-except to seperate different IndexError """
    try:
        dirs = sys.argv[1]
        path_list = get_path(dirs)
        if path_list == []:
            print(f'Invalid starting directory: {dirs}')
        pattern = sys.argv[2]
        try:
            cmd = sys.argv[3]
            if cmd == '-f':
                result = find_match_files(path_list, pattern)
            elif cmd == '-d':
                result = find_match_dirs(path_list, pattern)
            elif cmd == '-fd':
                result = find_all(path_list, pattern)
            else:
                result = f'Invalid option: {cmd}'
            print(result)
        except IndexError:
            result = find_all(path_list, pattern)
            print(result)
    except IndexError:
        print('Usage: finder start_dir search_pattern [-fd]')


main()

