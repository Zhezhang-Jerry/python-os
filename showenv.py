"""
program: showenv.py
Author: Zhe Zhang A01257572 Set B
Date: Apr 14 2021
"""

import os
import sys

def display_all_varname_perline(environ_dict):
    """ create a list to store all the variable names """
    varname_list = [varname for varname in environ_dict.keys()]

    return '\n'.join(varname_list)


def display_specy_var_value(environ_dict, variable):
    """ create a list to store specified enviroment variable and its value(s) """
    dict_specy = {}
    dict_specy[variable] = environ_dict[variable]
    list_value = dict_specy[variable].split(';')

    return dict_specy, list_value

def main():
    """ main function """
    try:
        cmd = sys.argv[1]
        vars_dict = os.environ
        if cmd == '-l':
            result = display_all_varname_perline(vars_dict)
            print(result)
        elif cmd == '-a':
            for varname, values in vars_dict.items():
                list_value = [i for i in values.split(';')]
                print(f'{varname:35}: {list_value[0]}')
                if len(values.split(';')) > 1:
                    for i in list_value[1:]:
                        x = ' ' * 36
                        print(x, i)
        else:
            dict_specy, list_value = display_specy_var_value(vars_dict, cmd)
            print(f'{cmd:35}: {list_value[0]}')
            if len(list_value) > 1:
                for i in list_value[1:]:
                    x = ' ' * 36
                    print(x, i)
    except IndexError:
        sys.exit('Usage: showenv variable, or showenv -l or showenv –a')
    except KeyError:
        sys.exit(f"Environment variable '{cmd}' does not exist.")


main()