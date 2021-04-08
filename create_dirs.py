"""
program: create_dirs.py
Author: Zhe Zhang A01257572 Set B
Date: Apr 8 2021
"""

import os

def main():
    os.mkdir('TOPDIR')
    os.chdir('TOPDIR')

    open('FA.txt', 'w').close()
    open('FB.txt', 'w').close()
    os.mkdir('D1')
    os.mkdir('D2')
    os.mkdir('D3')

    os.chdir('D1')
    open('FC.txt', 'w').close()
    os.mkdir('D1-1')
    os.chdir('D1-1')
    open('FF.txt', 'w').close()

    os.chdir('..\\..\\D2')
    open('FD.txt', 'w').close()

    os.chdir('..\\D3')
    open('FE.txt', 'w').close()
    os.mkdir('D3-1')
    os.chdir('D3-1')
    open('target.txt', 'w').close()


main()
