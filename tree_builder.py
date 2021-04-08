"""Create a directory tree of random files and directories

This script is run from the command line with two command line arguments:
tree_depth and tree_breadth.

Usage: tree_builder.py tree_depth tree_breadth random_seed

       tree_depth - depth of the directory tree below the root
       tree_breadth - max number of sub_dirs in any directory
       random_seed - specifies a seed for the rng, to allow users to
                     build the same tree multiple times

The root directory will always be named TOPDIR. Note that the tree_depth
argument is also used to specify the maximum number of files in any directory.

A file named words.txt must exist in the directory from which the program is
run. This file contains potential file names, one per line.
"""

import os
import sys
import random
from typing import List

WORDS_FILE = "words.txt"
TOP_DIR = "TOPDIR"


def create_directories(root: str, max_levels: int, max_breadth: int, name_list: List, seed:int = None) -> None:
    """Create random directories in the native OS filesystem

    Note that this function is a modified version of an iterative
    implementation of the DFS algorithm.
    """
    if seed is not None:
        random.seed(seed)
    
    topleveldir = os.path.join(root, TOP_DIR)
    if os.path.exists(topleveldir):
        print("Warning:", topleveldir, "already exists. Remove", topleveldir, "and try again.")
        exit(1)

    stack = []
    stack.append(topleveldir)
    while len(stack) > 0:
        current_path = stack.pop()
        makedir(current_path)
        make_files(current_path, name_list, max_breadth)
        if level(current_path) <= max_levels:
            create_next_level_names(current_path, name_list, max_breadth, stack)


def load_names_from_file(filename: str) -> List:
    """Read names from a file and store as a list, one name per list item"""
    try:
        f = open(filename)
    except FileNotFoundError:
        exit(f"Error: file {filename} does not exist in current directory")
    name_list = f.read().split()
    f.close()
    return name_list


def get_random_name(name_list: List) -> str:
    """Randomly select a name from the name list"""
    index = random.randint(0, len(name_list))
    return name_list[index]


def makedir(pathname: str) -> None:
    """Create a directory in OS filesystem"""
    try:
        os.mkdir(pathname)
    except (FileExistsError, NotADirectoryError):
        print("Warning:", pathname, "already exists")


def create_next_level_names(current_path: str, name_list: List, max_breadth: int, stack: List) -> None:
    """Generate random names for the sub_dirs of the current directory, and add names to DFS queue"""
    num_dirs = random.randint(0, max_breadth)
    for i in range(num_dirs):
        name = get_random_name(name_list)
        pathname = os.path.join(current_path, name)
        stack.append(pathname)


def make_files(current_path: str, name_list: List, max_breadth: int) -> None:
    """Create empty files in the current directory"""
    num_files = random.randint(0, max_breadth)
    for i in range(num_files):
        name = get_random_name(name_list) + '.txt'
        filename = os.path.join(current_path, name)
        try:
            f = open(filename, 'w')
            f.close()
        except NotADirectoryError:
            print("Warning:", filename, "already exists")


def level(path: str) -> int:
    """Return the number of levels in a pathname"""
    lev = 0
    head, tail = os.path.split(path)
    while head != '':
        lev += 1
        head, tail = os.path.split(head)
    return lev


def main() -> None:
    """Process command line args and call functions to create the file tree"""
    random.seed(7)      # A seed is added to ensure the tree can be regenerated during testing
    root = '.'
    try:
        max_levels = int(sys.argv[1])
        max_breadth = int(sys.argv[2])
    except (IndexError, ValueError):
        print("Usage:", os.path.basename(sys.argv[0]), "tree_depth tree_breadth")
        exit(1)

    names = load_names_from_file(WORDS_FILE)
    create_directories(root, max_levels, max_breadth, names)


if __name__ == "__main__":
    main()
